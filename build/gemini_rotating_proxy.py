#!/usr/bin/env python3
"""Local OpenAI-compatible proxy in front of Google AI Studio (free tier).

Forwards /v1/chat/completions and /v1/models to
https://generativelanguage.googleapis.com/v1beta/openai/ and rotates across
the free API keys in ~/.openclaw/gemini-keys.json. A key that returns 429 is
cooled down for COOLDOWN seconds and the request is retried on the next key.
Key values are never logged or printed.

This is the free generativelanguage endpoint, NOT Vertex. Nothing here costs money.

Usage:
    python gemini_rotating_proxy.py --port 18877
Then point Inspect at it:
    GEMROT_BASE_URL=http://127.0.0.1:18877/v1 GEMROT_API_KEY=unused \
    inspect eval ... --model openai-api/gemrot/gemini-2.5-flash
"""
import argparse
import json
import os
import sys
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

UPSTREAM = "https://generativelanguage.googleapis.com/v1beta/openai"
NATIVE_UPSTREAM = "https://generativelanguage.googleapis.com"
KEYS_FILE = os.path.expanduser("~/.openclaw/gemini-keys.json")
GLOBAL_MIN_GAP = float(os.environ.get("GEMROT_GLOBAL_GAP", "1.2"))  # seconds between ANY two upstream calls
_pace_lock = threading.Lock()
_last_global = [0.0]


def global_pace() -> None:
    """Keys share per-project minute quotas, so cap the aggregate rate too."""
    with _pace_lock:
        wait = _last_global[0] + GLOBAL_MIN_GAP - time.time()
        if wait > 0:
            time.sleep(wait)
        _last_global[0] = time.time()
COOLDOWN = 20.0          # seconds a key sits out after a 429
KEY_MIN_GAP = 7.0        # seconds between two uses of the same key (~8 RPM/key)
MAX_KEY_ATTEMPTS = 120   # total attempts across keys per request
STATS = {"requests": 0, "ok": 0, "rate_limited": 0, "errors": 0}

# Why pacing: the free tier limits requests PER MINUTE PER PROJECT, and several
# of the 43 keys share a project. Without a per-key gap, a burst of parallel
# requests 429s on every key within seconds, every key cools at once and the
# proxy stalls (measured 2026-09-29: 128 ok vs 1567 rate-limited in 20 min).

_lock = threading.Lock()
_keys: list[str] = []
_cool_until: dict[int, float] = {}
_last_used: dict[int, float] = {}
_rr = 0


def load_keys() -> None:
    global _keys
    with open(KEYS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    _keys = list(data["keys"])
    print(f"[gemrot] loaded {len(_keys)} keys (values not shown)", file=sys.stderr)


def next_key_index() -> int | None:
    """Round-robin over keys that are neither cooling nor used too recently."""
    global _rr
    now = time.time()
    with _lock:
        n = len(_keys)
        for step in range(n):
            i = (_rr + step) % n
            if _cool_until.get(i, 0.0) <= now and now - _last_used.get(i, 0.0) >= KEY_MIN_GAP:
                _rr = (i + 1) % n
                _last_used[i] = now
                return i
    return None


def cool(i: int) -> None:
    with _lock:
        _cool_until[i] = time.time() + COOLDOWN


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):  # quiet; we print our own stats
        return

    def _send(self, status: int, body: bytes, ctype: str = "application/json") -> None:
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _forward(self, method: str, path: str, body: bytes | None, native: bool = False) -> None:
        STATS["requests"] += 1
        attempts = 0
        last_status, last_body = 502, b'{"error":"no upstream attempt"}'
        while attempts < MAX_KEY_ATTEMPTS:
            global_pace()
            i = next_key_index()
            if i is None:
                time.sleep(0.5)
                attempts += 1
                continue
            attempts += 1
            if native:
                # Native Gemini REST path (used by Inspect's `google/` provider via
                # GOOGLE_BASE_URL). Key goes in x-goog-api-key, path is verbatim.
                url = NATIVE_UPSTREAM + path
                headers = {"x-goog-api-key": _keys[i], "Content-Type": "application/json"}
            else:
                url = UPSTREAM + path
                headers = {"Authorization": f"Bearer {_keys[i]}", "Content-Type": "application/json"}
            req = urllib.request.Request(url, data=body, method=method, headers=headers)
            try:
                with urllib.request.urlopen(req, timeout=600) as r:
                    data = r.read()
                    STATS["ok"] += 1
                    self._send(r.status, data, r.headers.get("Content-Type", "application/json"))
                    return
            except urllib.error.HTTPError as e:
                last_status = e.code
                last_body = e.read()
                if e.code == 429:
                    STATS["rate_limited"] += 1
                    cool(i)
                    continue
                if e.code >= 500:
                    STATS["errors"] += 1
                    time.sleep(1.5)
                    continue
                # 4xx other than 429: return to client as-is (bad request etc.)
                STATS["errors"] += 1
                self._send(e.code, last_body)
                return
            except Exception as e:  # network hiccup
                STATS["errors"] += 1
                last_status, last_body = 502, json.dumps({"error": str(e)}).encode()
                time.sleep(1.5)
                continue
        self._send(last_status, last_body)

    def do_GET(self):
        if self.path.startswith("/stats"):
            self._send(200, json.dumps(STATS).encode())
            return
        if self.path.startswith("/v1beta") or self.path.startswith("/v1alpha"):
            self._forward("GET", self.path, None, native=True)
            return
        path = self.path[len("/v1"):] if self.path.startswith("/v1") else self.path
        self._forward("GET", path, None)

    def do_POST(self):
        n = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(n) if n else b""
        if self.path.startswith("/v1beta") or self.path.startswith("/v1alpha"):
            self._forward("POST", self.path, body, native=True)
            return
        path = self.path[len("/v1"):] if self.path.startswith("/v1") else self.path
        self._forward("POST", path, body)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=18877)
    ap.add_argument("--host", default="127.0.0.1")
    args = ap.parse_args()
    load_keys()
    srv = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"[gemrot] listening on http://{args.host}:{args.port}/v1 -> {UPSTREAM}", file=sys.stderr)

    def reporter():
        while True:
            time.sleep(60)
            print(f"[gemrot] stats {json.dumps(STATS)}", file=sys.stderr, flush=True)

    threading.Thread(target=reporter, daemon=True).start()
    srv.serve_forever()


if __name__ == "__main__":
    main()
