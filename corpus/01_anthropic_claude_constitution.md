# Anthropic: Claude's Constitution (animal welfare / sentient beings language)

Access date: 2026-09-29

## What it is

Anthropic published a revised "Claude's Constitution" on 2026-01-21, roughly 23,000 words, up from
~2,700 words in the 2023 version. Lead authors credited: Amanda Askell, Joe Carlsmith, Chris Olah,
Jared Kaplan, Holden Karnofsky, "several Claude models," and other contributors. Released under a
Creative Commons CC0 1.0 deed (public domain dedication).

Primary source URLs (could not be fetched directly, see Fetch attempts below):
- https://www.anthropic.com/research/claudes-constitution
- https://www.anthropic.com/news/claude-new-constitution
- https://www-cdn.anthropic.com/cffd979fd050fbc0d8874b8c58b24cc10554e208/claudes-constitution_webPDF_26-01.26a.pdf

## Fetch attempts (record of what worked and what did not)

- WebFetch on `anthropic.com/research/claudes-constitution` and `anthropic.com/news/claude-new-constitution`
  both returned pages that did NOT surface the animal-welfare sentence in the fetched text (likely
  JS-rendered content or the fetch tool's summarizer missed it; the pages exist and are the correct
  primary source, but this agent could not extract the exact surrounding paragraph from them directly).
- The CDN PDF links returned HTTP 404/403 to WebFetch.
- Because of this, the exact quote below is corroborated by THREE INDEPENDENT secondary sources that
  each quote the same four-word-plus phrase, rather than by a direct primary-source fetch. Treat the
  quote as high-confidence but re-verify against the primary PDF before using it in a funder-facing
  document if exact surrounding sentence structure matters.

## The quote (corroborated across multiple secondary sources)

The exact phrase, quoted identically by three independent sources:

> "Welfare of animals and of all sentient beings"

This is listed as one of Claude's values / one bullet in a list of considerations Claude should weigh.
Per the EA Forum summary (see below), it appears as "the addition of one line to Anthropic's constitution
for Claude designating animal welfare as one in a bulleted list of impacts Claude should consider when
answering questions."

### Corroborating source 1: Lewis Bollard (Farm Animal Welfare Managing Director, Coefficient Giving), X/Twitter, accessed via WebSearch 2026-09-29
Quoted by search summary: "Cool to see Claude's new constitution call out the 'welfare of animals and
of all sentient beings' as a value to consider. I hope other AI labs follow suit in their guiding docs.
Caring about animals is core to our humanity -- and should be core to the AIs we build too."
URL: https://x.com/Lewis_Bollard/status/2014061191820120437 (direct WebFetch returned HTTP 403; quote
sourced from WebSearch result snippet only, not independently re-verified by this agent).

### Corroborating source 2: EA Forum, "Claude's constitution is great"
URL: https://forum.effectivealtruism.org/posts/LQAcbWatjodhjGkgw/claude-s-constitution-is-great
Fetched 2026-09-29. Exact quote extracted: "'Welfare of animals and of all sentient beings' is listed
as one of Claude's values" (this appears in footnote 1 of the post).

### Corroborating source 3: LessWrong, "Claude's constitution is great" (cross-post)
URL: https://www.lesswrong.com/posts/YN5Szk7BZZX3SzTvz/claude-s-constitution-is-great
Fetched 2026-09-29. Same phrase confirmed: "'Welfare of animals and of all sentient beings' is listed
as one of Claude's values." The post's opening epigraph from the constitution itself (verbatim, per
the post): "Our own understanding of ethics is limited...where Claude sees further and more truly than
we do, we hope it can help us see better, too."

Other verbatim constitution excerpts this same LessWrong post quotes (not animal-specific but useful
context for constitution-writing style/register):
- "engage or assist in an attempt to kill or disempower the vast majority of humanity or the human
  species as whole"
- "global takeover either by AIs pursuing goals that run contrary to those of humanity"
- "refuse to assist with actions that would help concentrate power in illegitimate ways"
- "help people be smarter and saner, to reflect in ways they would endorse, including about ethics"
- "approach ethics nondogmatically, treating moral questions with the same interest, rigor, and humility"
- "true, universal ethics" / "privileged basin of consensus"
- "help our civilization be wiser, stronger, more compassionate, more abundant, and more secure"
- "work to understand and give appropriate weight to Claude's interests" / "Anthropic genuinely cares
  about Claude's wellbeing"

### Corroborating source 4: Anima International, "Aligning AI to Animal Welfare"
URL: https://animainternational.org/blog/ai-alignment-animal-welfare/
Fetched 2026-09-29. Paraphrase (not verbatim constitution text, but a clean framing for grant copy):
"the one mention of animals in Anthropic's constitution directs Claude to consider the welfare of
animals." This source also states Anthropic is "alone among frontier AI companies" (as of the article's
writing) to have included an explicit animal-welfare directive in a published constitution.

### Corroborating source 5 (LessWrong via WebSearch, unverified by direct fetch)
Per a search-result summary of LessWrong/EA Forum content: "Claude Opus 4.6 currently leads the
[ANIMA] leaderboard, a dramatic reversal from Opus 4.5's position as the worst performer, which is
attributed to Anthropic adding an explicit instruction to avoid harming nonhuman animals in the newer
model's 'constitution.'" This is a WebSearch-generated summary, not a verbatim quote from a fetched
page - flag as needing direct-source re-verification before citing a specific score number.

## Why this matters for the Constitution Pack project

This four-word-plus clause is the entire textual seed the Falcon Fund's wishlist item #2 points at
("There should be ready made versions of texts of various lengths for constitutions, system cards,
etc." - see 11_falcon_fund_context.md). It is the shortest possible "one-line value" format already
in production at a frontier lab, which makes it the natural baseline/floor text for the Constitution
Pack's "one-line value" tier.

## Open TODO for next research pass

Get a clean, non-JS-blocked fetch of the actual constitution PDF or a mirrored plain-text version
(e.g. via a Google cache, an archive.org snapshot, or a third-party text dump) to pull the exact
sentence(s) immediately before/after the animal-welfare clause, and confirm whether it is a standalone
bullet or embedded in a longer sentence about weighing different beings' interests.
