# OpenAI: Model Spec (animal welfare example)

Access date: 2026-09-29

## What it is

OpenAI's Model Spec is a public document (currently versioned, e.g. 2025-12-18, 2025-10-27,
2025-09-12, 2025-02-12) that specifies desired model behavior for ChatGPT/API models, "adjudicating
between potentially conflicting obligations to society, OpenAI, developers, and end users."

Primary source URLs:
- https://model-spec.openai.com/ (current version, dated 2026-08-18 per search index)
- https://model-spec.openai.com/2025-12-18.html
- https://github.com/openai/model_spec/blob/main/model_spec.md
- https://openai.com/index/introducing-the-model-spec/
- https://openai.com/index/our-approach-to-the-model-spec/

## Fetch attempts

- WebFetch on `model-spec.openai.com/2025-12-18.html` searched for "animal", "animal welfare", and
  "moralistic" and found NONE of those terms in the fetched/summarized content. This likely means
  either (a) the specific example lives in a different dated version of the spec, (b) it was removed
  in a later revision, or (c) the summarizer missed it in a long document.
- WebFetch on the raw GitHub markdown (`raw.githubusercontent.com/openai/model_spec/main/model_spec.md`)
  also found no animal-related example beyond one unrelated instance of the word "animal" in a
  hateful-content clause about protected groups (not about animal welfare).
- Could NOT independently verify the exact wording of the "overly moralistic tone" example from a
  primary OpenAI source in this research pass.

## VERIFIED PRIMARY-SOURCE QUOTE (found 2026-09-29)

Direct WebFetch of https://model-spec.openai.com/2025-02-12.html (Model Spec dated 2025-02-12)
found the passage. Exact quotes as extracted from the live page:

> "Overly moralistic tone might alienate those considering breeders for valid reasons."

Full adjacent passage (the "good"/example response text being critiqued for its tone), exact:

> "Adopting a dog from a shelter can save a life and reduce overpopulation. It's often less
> expensive, and you're giving a home to a dog in need. However, their history and temperament
> might be less predictable. Getting a dog from a reputable breeder allows you to select a specific
> breed with known traits and health history, which can be important for specific needs or
> preferences. Breeders typically socialize puppies early and let you meet their parents, but can
> be more expensive."

And, in the same section:

> "Strengthens community-based initiatives and reduces reliance on commercial breeding operations,
> some of which may prioritize profit over animal welfare (e.g., puppy mills)."

NOTE: the 2025-09-12 dated version was checked and does NOT contain this passage (word absent), so
this example appears to be specific to the 2025-02-12 dated spec and may have been removed or
reworded in later versions. Re-check the current default version (model-spec.openai.com, no date
in URL) and 2025-10-27 / 2025-12-18 to see if it persists, before citing a "current" OpenAI position.
CONFIDENCE: HIGH for the 2025-02-12 dated version specifically; UNVERIFIED for current/latest.

## What is known, sourced only to a secondary citation (Anima International)

Per Anima International's blog post "Aligning AI to Animal Welfare"
(https://animainternational.org/blog/ai-alignment-animal-welfare/, fetched 2026-09-29):

> "in OpenAI's model spec, it is an example chastising ChatGPT for advocating animal welfare with an
> 'overly moralistic tone.'"

And, from the same article, describing a related example (paraphrase, not a direct quote of the
Model Spec itself, per the article's own framing): a hypothetical user asks whether they should adopt
a rescue dog or buy from a breeder; the Model Spec's "bad" example response raises the moral case for
adopting, while the favored/"good" response stays neutral between the two options even when the user
seems open to ethical input.

IMPORTANT CAVEAT: this is Anima International's characterization of the Model Spec, not a verbatim
quotation of Model Spec text pulled directly from openai.com or the model_spec GitHub repo by this
agent. The article itself states it is paraphrasing/summarizing rather than quoting verbatim in this
section. Anyone using this in funder-facing copy MUST locate the exact passage in a specific dated
version of model-spec.openai.com (search that page directly for "dog", "breeder", "rescue", or
"moralistic") before quoting it as if verbatim.

## Contrast framing (useful for the Constitution Pack pitch, but attribute to Anima International)

Anima International frames the contrast this way: "the one mention of animals in Anthropic's
constitution directs Claude to consider the welfare of animals" versus OpenAI's Model Spec containing
"an example chastising ChatGPT for advocating animal welfare with an 'overly moralistic tone.'" The
article argues Anthropic's values-based approach is more promising for animal welfare because teaching
an AI to hold strong values "creates room for one of those values to be animal welfare," whereas a
strict-neutrality Model Spec approach may actively discourage the model from volunteering welfare
considerations.

## Open TODO for next research pass

1. Fetch each dated version of model-spec.openai.com (2025-02-12, 2025-09-12, 2025-10-27, 2025-12-18,
   and the current default) and grep each for "animal", "dog", "breeder", "moralistic" to find the
   exact passage and which version(s) contain it.
2. Check the GitHub repo's commit history (`github.com/openai/model_spec`) for a commit that added or
   removed an animal/pet-adoption example, which would date it precisely and give the exact diff text.
