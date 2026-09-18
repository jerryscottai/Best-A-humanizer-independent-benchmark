# AI Humanizer Benchmark cycle changelog

Auto-generated from version-stamp diffs at publish time. Each entry shows
which methodology stamps moved between this cycle and the previous one,
with the rationale from the admin-side change log.

---

## August 2026 (published 2026-08-03)

No methodology, scoring, or prompt-set changes since the previous cycle.

- Current version stamps:
  - `methodology_version`: 1.4.0
  - `scoring_version`: 1.6.0
  - `prompt_set_version`: 1.0.0

📦 [Transparency bundle](data/cycles/August%202026/)

---

## July 2026 (published 2026-07-02)

No methodology, scoring, or prompt-set changes since the previous cycle.

- Current version stamps:
  - `methodology_version`: 1.4.0
  - `scoring_version`: 1.6.0
  - `prompt_set_version`: 1.0.0

📦 [Transparency bundle](data/cycles/July%202026/)

---

## June 2026 (published 2026-06-02)

First published cycle.

- `methodology_version`: 1.4.0
  Tools that could not be run at all during the cycle (site down, paywall,
  captcha loop, no output returned, or terms that prohibit automated
  submission) are reported in `unavailable_humanizers` rather than ranked
  with a zero. Their raw tests are deliberately not published, and the
  verifier rejects any cycle where an excluded tool appears in the scoring
  replay.

- `scoring_version`: 1.6.0
  Per-test meaning preservation is published as the raw input/output
  embedding cosine; the aggregated sub-score rescales the `[0.75, 1.0]`
  on-topic band onto `[0, 1]` so realistic differences spread across the
  full scale. The severe-meaning-drift penalty still triggers on the raw
  per-test value. Readability is a language-model writing-quality rating of
  the output. Each quality-failure penalty can subtract up to 10 points
  from a tool's composite.

- `prompt_set_version`: 1.0.0
  11 templates across 7 writing categories, three samples per template.

📦 [Transparency bundle](data/cycles/June%202026/)
