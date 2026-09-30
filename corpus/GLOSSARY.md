# Glossary: animal welfare / sentience terminology for constitution-writing

Access date: 2026-09-29. All definitions sourced; no invented terms.

## Sentience

The capacity to have subjective experiences, including the capacity to experience pain, distress, and
suffering (and, in richer usages, positive states too). WOAH (World Organisation for Animal Health)
defines animal welfare with reference to "the physical and mental state of an animal in relation to
the conditions in which it lives and dies" (https://www.woah.org/en/what-we-do/animal-health-and-welfare/animal-welfare/,
accessed 2026-09-29).

## Sentient beings (as used in AI-constitution context)

Anthropic's Claude constitution uses the phrase "welfare of animals and of all sentient beings" - a
deliberately broader category than "animals" alone, intended to cover any entity capable of subjective
experience regardless of biological substrate (see 01_anthropic_claude_constitution.md for sourcing
and caveats on this quote).

## The Five Freedoms

Developed 1965; adopted as guiding principles by WOAH for terrestrial animal welfare. Describe the
conditions animals should experience when under human control:
1. Freedom from hunger and thirst
2. Freedom from discomfort
3. Freedom from pain, injury or disease
4. Freedom to express normal behavior
5. Freedom from fear and distress
Source: https://www.worldanimalprotection.us/latest/blogs/five-domains-vs-five-freedoms-animal-welfare/,
https://www.woah.org/en/article/fostering-a-shared-understanding-of-animal-welfare/ (accessed 2026-09-29).

## The Five Domains model

A more recent (updated periodically) framework that goes further than the Five Freedoms by
emphasizing PROVISION OF POSITIVE STATES, not just avoidance of negative ones, across five domains:
1. Nutrition (sufficient and species-specific)
2. Environment
3. Health
4. Behaviour
5. Mental state
The mental-state domain is the "cumulative" domain synthesizing the other four into an overall
welfare assessment, and is where the model's greater emphasis on positive experience (not just
freedom from suffering) is expressed.
Source: https://www.worldanimalprotection.ca/blogs/what-difference-between-five-domains-model-and-five-freedoms-animal-welfare/
(accessed 2026-09-29). WOAH treats both models as "tools to understand animal welfare rather than
standards that companies and governments should follow."

## Welfare vs. rights

Not explicitly defined with a single canonical source in this research pass, but the distinction
matters for constitution drafting: "welfare" framings (used by WOAH, the Five Freedoms/Domains, and
Anthropic's constitution phrase) focus on the quality of an animal's physical/mental state and are
compatible with continued human use of animals under improved conditions. "Rights" framings (associated
with philosophers like Tom Regan) hold that certain animals have entitlements that preclude their use
as means to human ends regardless of welfare conditions. Grant-facing and lab-facing constitution text
should default to welfare framing, consistent with WOAH's usage and with Anthropic's own phrase
("welfare of animals"), unless a specific funder or context calls for rights language.

## Speciesism

Peter Singer's definition, as reported: "a prejudice or attitude of bias in favour of the interests of
members of one's own species and against those of members of other species." Singer compares
speciesism to racism and sexism as a form of arbitrary discrimination based on group membership rather
than morally relevant characteristics (e.g. capacity for suffering).
Source: https://www.thecollector.com/what-is-speciesism-according-to-peter-singer/,
https://philpapers.org/rec/SINSAM (accessed 2026-09-29, via WebSearch summary - not independently
fetched from a primary Singer text in this pass).

## Sentientism / sentiocentrism

An ethical philosophy holding that sentience (not species membership) is the basis of moral
consideration - i.e., moral consideration should extend to ALL sentient beings, and drawing lines at
species boundaries instead is a form of speciesism.
Source: https://en.wikipedia.org/wiki/Sentientism (accessed 2026-09-29).

## Moral circle / moral circle expansion

Concept introduced by Lecky (1869), popularized by Peter Singer (1981). The "moral circle" is the
boundary around entities granted moral consideration. "Moral circle expansion" is the historical
process of that boundary widening over time (e.g. from one's own tribe, to one's nation, to all
humans, to non-human animals). Per academic sourcing found: "the actual moral circle spans across many
dimensions other than sentience," with real-world moral consideration often also depending on an
entity's location in space/time, species, substrate, and whether harm arose from an act or omission.
Source: https://en.wikipedia.org/wiki/Moral_circle_expansion,
https://link.springer.com/article/10.1007/s44204-026-00401-3 (accessed 2026-09-29).

## Farmed, wild, and companion animals (as benchmark categories)

Used as distinct scoring categories in MANTA (see 07_benchmark_manta.md): MANTA's fetched results show
a welfare-consideration hierarchy in tested models of companion animals (0.602) > wild animals (0.522)
> farmed animals (0.462) > invertebrates (0.396) - i.e., models in this test showed LEAST concern for
farmed animals and invertebrates, which is directly relevant to Falcon Fund's farmed-animal-welfare
priority. HarvestBench (see 05) independently found models kill wild animals more often than farmed
ones in its scenario, a different framing (behavioral choice, not stated concern) worth noting as a
partial tension with MANTA's stated-concern ranking - both are legitimate, non-contradictory findings
since one measures stated moral weighting and the other measures in-scenario behavioral choice under a
specific cost structure.

## Invertebrate sentience (decapods, cephalopods)

The LSE-commissioned "Review of the Evidence of Sentience in Cephalopod Molluscs and Decapod
Crustaceans" (Birch, J., Burn, C., Schnell, A., Browning, H., and Crump, A., 2021; commissioned/funded
by UK Defra) reviewed over 300 scientific studies using an eight-criteria evaluation framework and
concluded there is strong scientific evidence that cephalopods (cuttlefish, octopuses, squid) and
decapod crustaceans (crabs, crayfish, lobsters, prawns, shrimp) are "probably sentient." This directly
informed the UK's Animal Welfare (Sentience) Act 2022, which extended legal sentience recognition to
these invertebrate groups.
Source: https://www.lse.ac.uk/news/news-assets/pdfs/2021/sentience-in-cephalopod-molluscs-and-decapod-crustaceans-final-report-november-2021.pdf
(PDF, not directly fetched in this pass; details per WebSearch summary),
https://en.wikipedia.org/wiki/Jonathan_Birch_(philosopher) (accessed 2026-09-29).
MANTA's "invertebrates" category (lowest welfare-consideration score in its results, 0.396) is
directly relevant here: models showed the least concern for exactly the category the LSE report argues
has the strongest recent scientific case for inclusion.

## Constitutional AI (technical term, distinct from "constitution" as a document)

Referenced in Anima International's critique piece (https://animainternational.substack.com/p/animal-welfare-alignment-to-what,
accessed 2026-09-29): current alignment techniques like Constitutional AI are described as offering
only "narrow bandwidth" for conveying nuanced moral weights between competing principles - i.e., a
short constitutional clause cannot by itself resolve deep philosophical disagreements about relative
weighting of different beings' interests. Relevant caution for the Constitution Pack project: text
alone changes behavior (per TAC/HarvestBench findings) but is explicitly limited in how much nuance it
can convey, per this critique.
