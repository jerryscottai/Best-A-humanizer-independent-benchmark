# AI Humanizer Benchmark: Rankings & Public Audit Record

**The best AI humanizers, ranked by a monthly benchmark.** This benchmark measures how well each AI humanizer bypasses the major AI detectors (GPTZero, Originality.ai, Copyleaks, Winston AI, and ZeroGPT) while preserving the original meaning and readability. We pay for every tool ourselves and run each one by hand on the most undetectable setting it advertises; there are no affiliate deals and no vendor-supplied numbers. Every input, every humanized output, every detector verdict, and the scoring code itself is published in this repository, so anyone can reproduce the rankings from scratch.

<!-- RANKINGS:START -->
## 🏆 Best AI humanizers: August 2026

| # | AI humanizer | Score / 100 | Bypass | Meaning | Readability | Consistency | Penalty | Standout |
|--:|--------------|:-----------:|:------:|:-------:|:-----------:|:-----------:|:-------:|----------|
| 1 | [GPTHuman AI](data/humanizers/gpthuman.json) | 88.28 | 94% | 77% | 91% | 96% | 0 | Best overall writing quality |
| 2 | [Undetectable.ai](data/humanizers/undetectable.json) | 82.53 | 82% | 87% | 69% | 93% | 0 | Best meaning and length preservation |
| 3 | [WriteHuman](data/humanizers/writehuman.json) | 76.60 | 84% | 66% | 77% | 90% | -1.0 | Best concise rewrite |
| 4 | [NoteGPT](data/humanizers/notegpt.json) | 69.79 | 88% | 60% | 78% | 91% | -8.0 | Most conversational rewrite |
| 5 | [ZeroGPT Humanizer](data/humanizers/zerogpt-humanizer.json) | 65.35 | 76% | 66% | 45% | 71% | -2.0 | Good fidelity, weak grammar |
| 6 | [UnAIMyText](data/humanizers/unaimytext.json) | 60.64 | 72% | 56% | 42% | 86% | -3.0 | Verbose and inconsistent |
| 7 | [HIX Bypass](data/humanizers/hix-bypass.json) | 52.42 | 70% | 47% | 39% | 89% | -7.0 | Most editing required |

_The composite (out of 100) weights detector bypass (42%), meaning preservation (32%), readability (16%), and consistency across writing categories (10%); the Bypass, Meaning, Readability, and Consistency columns are those sub-scores. Penalty is the total points deducted for quality failures (meaning drift, length inflation or deflation, refusals, or output returned unchanged) — already reflected in the score. We pay for every tool ourselves and run each one by hand on its most undetectable advertised setting. Scored against 5 AI detectors; every score is reproducible from the data in this repo._
<!-- RANKINGS:END -->

**GPTHuman AI takes the top spot for August 2026.** It was the only tool to combine the highest bypass rate in the field with clean, publication-quality prose — no obvious grammatical errors, logical paragraph structure, and genuine sentence-level variation rather than mechanical synonym replacement. It took no quality penalty at all. Undetectable.ai preserved the source more faithfully and hit the target length exactly, but two visible errors in a single short passage kept it in second.

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

> **A note on ZeroGPT.** ZeroGPT ships both an AI detector and a humanizer. The detector is one of the five this benchmark scores against (`zerogpt`); the humanizer is ranked above as `zerogpt-humanizer`. They are separate products and are never scored against each other.

Per-detector breakdowns, per-category sub-scores, penalty details, and the full three-cycle history for every tool are in [`data/humanizers/`](data/humanizers/) and in each cycle's `leaderboard.json`.

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

## How to verify a cycle

```bash
git clone https://github.com/jerryscottai/Best-A-humanizer-independent-benchmark.git
cd Best-A-humanizer-independent-benchmark
npm install
npm run verify                                   # verify every published cycle
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

If all five pass for every cycle, no one (including the benchmark operator) could have altered the prompts, inputs, outputs, detector verdicts, or scoring math after the cycle started without breaking the chain.

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
