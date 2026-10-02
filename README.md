# AI Humanizer Benchmark: Rankings & Public Audit Record

**The best AI humanizers, ranked by a monthly benchmark.** This benchmark measures how well each AI humanizer bypasses the major AI detectors (GPTZero, Originality.ai, Copyleaks, Winston AI, and ZeroGPT) while preserving the original meaning and readability. We pay for every tool ourselves and run each one by hand on the most undetectable setting it advertises; there are no affiliate deals and no vendor-supplied numbers. For the June–August 2026 cycles, every input, every humanized output, every detector verdict, and the scoring code itself is published in this repository, so anyone can reproduce those rankings from scratch. October 2026 is a [results-only cycle](#results-only-cycles).

<!-- RANKINGS:START -->
## 🏆 Best AI humanizers: October 2026

| # | AI humanizer | Score / 100 | Detector bypass | Meaning | Natural writing | Consistency | Factual reliability |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | GPTHuman AI | 96.2 | 98% | 96% | 95% | 95% | 97% |
| 2 | Undetectable.ai | 90.0 | 92% | 90% | 89% | 88% | 91% |
| 3 | StealthGPT | 89.4 | 95% | 87% | 91% | 86% | 88% |
| 4 | HIX Bypass | 88.0 | 90% | 89% | 86% | 87% | 88% |
| 5 | WriteHuman | 87.6 | 87% | 92% | 88% | 85% | 86% |
| 6 | Stealth Writer | 85.8 | 85% | 88% | 89% | 82% | 85% |
| 7 | BypassGPT | 85.4 | 93% | 82% | 84% | 85% | 83% |
| 8 | Humanize AI Pro | 83.4 | 88% | 81% | 86% | 80% | 82% |
| 9 | Phrasly | 83.2 | 83% | 85% | 84% | 83% | 81% |
| 10 | GPTinf | 81.8 | 86% | 80% | 82% | 78% | 83% |
| 11 | Humbot | 81.2 | 81% | 83% | 81% | 82% | 79% |
| 12 | SupWriter | 79.2 | 79% | 80% | 83% | 76% | 78% |
| 13 | Grammarly | 79.0 | 62% | 84% | 81% | 83% | 85% |
| 14 | Twixify | 78.0 | 84% | 77% | 79% | 74% | 76% |
| 15 | Uncheck AI | 77.6 | 77% | 81% | 78% | 77% | 75% |
| 16 | BypassAI | 76.4 | 80% | 74% | 76% | 75% | 77% |
| 17 | Undetected.ai | 75.0 | 78% | 75% | 77% | 72% | 73% |
| 18 | ReHumanize | 74.6 | 74% | 78% | 74% | 73% | 74% |
| 19 | AI Humanize io | 72.6 | 75% | 72% | 75% | 70% | 71% |
| 20 | Humaniser | 72.0 | 72% | 74% | 73% | 69% | 72% |
| 21 | AIUndetectable | 70.8 | 73% | 70% | 71% | 71% | 69% |
| 22 | StealthBypass | 69.6 | 71% | 69% | 70% | 68% | 70% |
| 23 | Penlify | 68.6 | 69% | 71% | 68% | 67% | 68% |
| 24 | Super Humanizer | 67.0 | 68% | 67% | 69% | 65% | 66% |

*October 2026 is a **results-only** cycle. Rankings are published without the full source samples, per-test outputs, detector verdicts, or commit-reveal materials required for independent re-derivation. June–August 2026 cycles remain fully reproducible.*

_Scores are out of 100 and are the equal-weight mean of the five dimension columns, as published in [`leaderboard.json`](data/cycles/October%202026/leaderboard.json). October uses a different methodology from June–August, so its scores are not directly comparable with earlier cycles._
<!-- RANKINGS:END -->

**GPTHuman AI also holds the top spot for October 2026**, ahead of Undetectable.ai and StealthGPT. October is published as a [results-only cycle](#results-only-cycles); the field-test notes below are from the fully reproducible August 2026 cycle.

### August 2026 field test

**GPTHuman AI took the top spot for August 2026.** It was the only tool to combine the highest bypass rate in the field with clean, publication-quality prose — no obvious grammatical errors, logical paragraph structure, and genuine sentence-level variation rather than mechanical synonym replacement. It took no quality penalty at all. Undetectable.ai preserved the source more faithfully and hit the target length exactly, but two visible errors in a single short passage kept it in second.

The pattern across the field is a trade: the tools that rewrite most aggressively tend to drift or inflate, and the tools that stay closest to the source tend to read as edited rather than rewritten. Only the top two managed both at once.

## What the field test found

Each tool rewrote the same source passage on its most undetectable advertised setting, then the output was read line by line against the original.

### 1. GPTHuman AI: Best overall writing quality

The strongest balance of naturalness, professional tone, and sentence-level control. No obvious grammatical errors, logical paragraph divisions, and the central argument survived intact. Showed genuine variation rather than mechanical synonym replacement — phrases like "do the heavy lifting" and "spare people from the drudgery" read naturally without tipping into the excessively casual. Not a perfect copy: a few small fidelity shifts, and the output ran longer than the source.

**Verdict:** The most publication-ready result in the field test, with minor fidelity issues that would still merit a final human review.

### 2. Undetectable.ai: Best meaning and length preservation

Returned the source length exactly and retained nearly every important element — the worked example, seasonal detail, customer questions, disclosure requirements, fact-checking, tone adjustment, and firsthand knowledge. Its best sentences were concise and faithful. Two obvious errors held it back: a sentence fragment in the opening, and an awkward determiner in the conclusion.

**Verdict:** The strongest option for preserving the source and controlling length, but not completely publication-ready without correcting two obvious errors.

### 3. WriteHuman: Best concise rewrite

Cut the passage by roughly a tenth while keeping a clear progression from AI-assisted drafting through human review to disclosure. Coherent and easy to follow, but it compressed away useful detail and leaned on repeated words. One phrasing was awkward, and it introduced a meaningful change: it suggested AI should perform the final edit, where the source assigned fact-checking, tone, and final judgment to a person.

**Verdict:** Readable and efficient, but less precise than GPTHuman or Undetectable.ai.

### 4. NoteGPT: Most conversational rewrite

The liveliest output in the test — varied sentence lengths and concrete conversational phrasing that flowed naturally and avoided the rigid cadence common in rewritten passages. The style came with tradeoffs: it expanded the passage by roughly 40% despite a neutral tone setting, altered a key noun, and added details that were not in the original.

**Verdict:** The strongest conversational version, but too long and too casual for a neutral professional rewrite.

### 5. ZeroGPT Humanizer: Good fidelity, weak grammar

Retained most of the source argument and stayed reasonably close to the original structure — the worked example, the disclosure requirement, and the role of human review all remained recognizable. The prose did not hold up: several serious errors, including garbled prepositional phrases and a mangled clause, plus missing punctuation where commas were needed.

**Verdict:** The meaning largely survived, but the prose required substantial editing.

### 6. UnAIMyText: Verbose and inconsistent

Expanded the passage by about a fifth. The broad thesis survived, but several constructions read as less natural than the source, including a malformed noun phrase and a double-conjunction error. It also introduced details that did not appear in the original passage.

**Verdict:** Understandable overall, but weakened by grammatical errors, added material, and awkward phrasing.

### 7. HIX Bypass: Most editing required

The longest and least controlled rewrite among the lower-ranked results, expanding the source by roughly a quarter. The output included malformed expressions and a broken compound modifier, and it introduced business idioms that changed the original tone and meaning.

**Verdict:** Usable only as a starting point; every paragraph needed hands-on correction.

> **A note on ZeroGPT.** ZeroGPT ships both an AI detector and a humanizer. The detector is one of the five this benchmark scores against (`zerogpt`); the humanizer was ranked in August as `zerogpt-humanizer`. They are separate products and are never scored against each other.

Per-detector breakdowns, per-category sub-scores, penalty details, and the cycle history for every tool are in [`data/humanizers/`](data/humanizers/) and in each cycle's `leaderboard.json`.

## What's in here

```
data/
  cycles/
    <cycle>/                   # one directory per published cycle
      # Transparency bundle (proves prompts weren't predictable or swapped)
      commit.json              # sha256(nonce), published at cycle start
      nonce.txt                # the nonce, published at cycle close
      prompts.json             # resolved prompts (templates with placeholders filled)
      templates.json           # the prompt templates (with [BRACKETED] tokens)
      banks.json               # the value banks the placeholders are drawn from
      select-placeholders.js   # the frozen selection algorithm
      # Reproducibility bundle (lets you re-derive the leaderboard)
      samples.json             # the source samples (input texts)
      tests.json               # every humanizer's output + per-test metrics
      detector-scores.json     # every detector verdict on every output
      scoring.js               # the frozen scoring aggregator
      cycle.json               # SHA-256 manifest of every per-cycle file above
      # Final result
      leaderboard.json         # composite + sub-scores per humanizer
  humanizers/
    <slug>.json                # per-humanizer history + field notes across all cycles
scripts/
  verify-cycle.ts              # the audit script (see below)
CHANGES.md                     # cycle-to-cycle methodology changelog
```

The benchmark itself runs from a separate private repo (corpus generation, detector integrations, humanizer adapters, API keys). This public repo receives every input, every output, every detector verdict, and a frozen copy of the scoring algorithm each cycle produces, enough that anyone can **re-derive the leaderboard from scratch**, not just spot-check it.

## Results-only cycles

October 2026 publishes the ranked results only. Its commit-reveal materials, source samples, per-test outputs, and detector verdicts are not included, so **it cannot be independently re-derived**. Its `cycle.json` sets `"results_only": true`; the verifier skips the hash-commitment, replay, and manifest checks for such cycles and only confirms that the published ranks and composites are internally consistent. June, July, and August 2026 remain fully reproducible. See [`CHANGES.md`](CHANGES.md).

## How to verify a cycle

```bash
git clone https://github.com/jerryscottai/Best-A-humanizer-independent-benchmark.git
cd Best-A-humanizer-independent-benchmark
npm install
npm run verify                                   # verify every cycle (results-only cycles are skipped)
npx tsx scripts/verify-cycle.ts "August 2026"    # verify one cycle
```

A successful verification looks like:

```
[ok] August 2026: 11 prompts verified, 7 humanizers replayed
verify-cycle OK
```

A tampered cycle looks like:

```
verify-cycle FAILED:
  - August 2026: sha256(nonce) mismatch, expected <hash-A>, got <hash-B>
  - August 2026: resolved text for "argumentative_essay" differs from published
```

The script runs five separate checks for each cycle:

1. **Hash commitment.** `sha256(nonce.txt) === commit.json.committed_hash`. Proves the nonce revealed at cycle close is the same one whose hash was published at cycle start.
2. **Algorithm replay.** Re-runs the frozen `select-placeholders.js` against `nonce.txt`, `templates.json`, and `banks.json` to re-derive the placeholder map.
3. **Substitution match.** Substitutes the re-derived placeholders into the templates and asserts the resulting prompts equal `prompts.json` byte-for-byte.
4. **Manifest integrity.** For every entry in `cycle.json.files`, recomputes the SHA-256 of the named file and asserts it matches the manifest. The four reproducibility data files (`samples.json`, `tests.json`, `detector-scores.json`, `scoring.js`) are required-minimum entries; recent cycles also manifest the transparency bundle (`commit.json`, `nonce.txt`, `prompts.json`, `templates.json`, `banks.json`, `select-placeholders.js`) and the published `leaderboard.json`. Unknown filenames in the manifest are rejected. Catches truncated, corrupted, or doctored publishes.
5. **Score replay.** Runs the frozen `scoring.js` against the raw data and asserts every humanizer's composite, sub-scores, detector breakdown, category breakdown, and penalty counts match `leaderboard.json` within `1e-4`.

If all five pass for every reproducible cycle (June–August 2026), no one (including the benchmark operator) could have altered the prompts, inputs, outputs, detector verdicts, or scoring math after the cycle started without breaking the chain.

The verifier is also wired into CI on this repo: every push to `main` runs `npm run verify` and fails the build if any cycle's chain has broken.

## The commit-reveal scheme in one paragraph

Cycle names are predictable (`June 2026`, then `July 2026`, and so on). If placeholder selection were seeded on the cycle name, a humanizer with access to the public banks and algorithm could pre-compute next month's prompts and fine-tune against them. Instead, each cycle is seeded by a random 32-byte nonce that is generated at cycle creation and kept private during the cycle. Only `sha256(nonce)` is published at start. At cycle close, after every humanizer has been scored against the prompts derived from that nonce, the nonce itself is published, and anyone can re-derive the prompts and check the hash. Vendors get auditability; they don't get predictability.

## How the score is built

Each cycle generates source samples from 11 prompt templates across 7 writing categories (academic essay, application essay, blog post, business email, discussion board, marketing copy, news article), three samples per template. Every humanizer processes every sample, and every output is submitted to all five detectors.

- **Bypass** — per test, the median of the five detectors' scores; per tool, the mean across tests. Using the median means one lenient detector can't carry a tool.
- **Meaning** — the embedding cosine between input and output, rescaled from the `[0.75, 1.0]` on-topic band onto `[0, 1]` so realistic differences spread across the full scale.
- **Readability** — a language-model writing-quality rating of the output.
- **Consistency** — `1 - stddev` of the per-category bypass means. A tool that beats detectors on blog posts and fails on business email scores poorly here.
- **Penalties** — up to 10 points per category for meaning drift, length inflation (>1.4× input), length deflation (<0.6× input), refusals, and output returned unchanged.

Both the per-test meaning and readability values are published as raw data; `scoring.js` only averages them. The script calls no model and no detector, which is what makes the leaderboard reproduce exactly from the published files.

## Corrections and disputes

If you spot an error in a cycle (a bad score, a stale humanizer record, a verifier failure on a cycle that should be clean), open an issue in this repo. We aim to respond within one cycle.

## License

- Verifier code, workflows, and configuration: [MIT](LICENSE).
- Cycle data under `data/`: [CC BY 4.0](LICENSE-data). Reproduction with attribution is welcome.

Every humanizer named here is the trademark of its respective owner. Naming a tool in this data set is a statement about a measurement, not an affiliation or an endorsement in either direction.

## Reporting issues

Found a verifier bug, a tampered cycle, or a security issue with this repo? See [SECURITY.md](SECURITY.md). For non-security audit findings, open a regular GitHub issue.
