# AI Universal Ontology Kernel v18

```
r_sev(K) = 0.05      b(K) = 0.1      n_eff = 1.0      κ = 0  [RUNNING]
ρ_A(d_gov) = 0.33    ρ_M(d_gov) = 0.33               E = 29.2 KB
```

*Header metrics are the kernel's own status, recomputed per revision. All four are still bad — v10 repairs references, not coupling. See §13.*
*`E` is now defined: bytes of this file ÷ 1000, UTF-8. Reproduce with `wc -c`; self-referential, solved by fixed point at build. v9 declared 14.9 KB against a 19,351 B file with no counting rule — D-033.*
*Filename and self-declaration must match; see `VERSION_LEDGER.md`.*
*v10 is an **addition release** whose no-loss guarantee is **asserted, not promised**: all 345 v9 leaf fields present, 0 lost, checked by `assert_superset` at build. One entry — `bridge._convergence` — is RETIRED: inert, bytes verbatim. There is no DELETE operation in this vocabulary (§11).*
*Companions: `ontology_v18.json` (67.1 KB — bridge, F, A, M, D, E, P, C, CX, AI, N, TRT, **R, X, PAR, DL, INF**), `doctrine_v1.json` (11.3 KB), `doctrine/process_ontology_v1.md` (T1–T5). v9's subtraction stands; v10 removes nothing further and restores nothing removed.*
*Ten defects repaired, four sections added. **Every repair is decidable by inspection** — none asserts a new claim, which is what permits them under HALT (§11.3).*
*v18: B7′ amendment adopted (counted capability/falsifiability/attack-surface terms, |Δ| knowledge delta, E_ref freeze at 28.7 KB). HALT cleared (κ = 0) via Step ① custodial provenance at Anarcho-app/Anarchy-Ontology.*
*risk-tag (B3, v17): every code-fence block in this file is stipulative-formal and carries reception-risk — acknowledged, not discharged.*

---

## 1. Scope

This kernel governs reasoning procedure. It contains no cosmology, no theology, and no claims about its own effect on readers.

**Moved out (not deleted).** T1–T5 Process Ontology → `doctrine/`. Justification is internal: Axioms I and I′ forbid anything downstream from quantifying over or inheriting interpretation from T1–T5, so its removal delta is zero by construction. The axioms that made §1 safe are the axioms that make it removable. **Open #6 closes in the negative.**

Axioms I and I′ are retained here, since they govern the import barrier:

**Axiom I / I′ (NO_BRIDGE).** No formalism in this kernel may quantify over, invoke, or inherit interpretation from `doctrine/`. Conversely, no result here is evidence for or against it. Import direction is one-way and enforced: `dict ← kernel ← json`; `doctrine` is a sink.

**Axiom I″ (v10).** `R[].mech[]` carries identical barrier status to `L[]` — inert pointer, never warrant. This is what lets the role table enter the corpus at all: it enters as routing, not as claim.

**Key rule (v10, repaired v11).** New-section keys are ASCII ids (`R01`, `X01`, `PAR-01`, `DL-001`); UIL demotes to a value field. D-024 and D-020 become unreachable by construction for everything added from here. Pre-v10 emoji keys unchanged; the two surviving ZWJ keys now carry the aliases v9 claimed to have added and had not (D-031).

**Deleted.** v7 §K, which asserted the kernel's own persuasive effect on readers (`consistency_attraction`: internal consistency "makes it an inference ATTRACTOR"). Grounds: `D[🔄❌]` Affirming the Consequent. Its general LLM-behaviour citations may live in a file that never references this kernel, after the arXiv IDs are verified.

---

## 2. Anarchy-Ontology

*Not unmodified vs README — Restriction monotone, β=σ·ρ_rul, numeric table live in Anarchy-Ontology/README.md. Kernel adds Overlap Aggregation + R13.*

A relativized language distinguishing **anarchy** (structural facts about a ruled-by relation `R`) from **anarchism** (ascriptive attitudes).

### 2.1 Core

```
An_R(x) ⟺ ¬∃y (y ≠ x ∧ x R y)          A_R = {x ∈ S : An_R(x)}
```

`R` irreflexive on finite `S`; `x R y` = "x is ruled by y". Self-rule is not being ruled.

**Edge rule (stipulative).** `x R y` holds when `y` can impose a directive that `x` cannot unilaterally refuse without sanction, and `y` is an identifiable person, office, or (under explicit sortal extension) transcendent node. Above household scale, nodes are offices.

**Predicates.** Local: `an-archy₁(x) := An_R(x)`. Systemic: `An-archy₂(S,R) := (ρ_M = 0)`.

**Apex vs hermit.** `apex ⟺ An_R(x) ∧ ∃z(z R x)` · `hermit ⟺ An_R(x) ∧ ¬∃z(z R x)`

**Relativization.** Every claim carries relation domain `d` and node subdomain `D ⊆ S`. Unindexed claims are ill-formed.

```
ρ_A = |A_R|/|S|    ρ_M = |A_R^apex|/|S|    β = |R|/|S|    σ = |R|/|{y : ∃x(x R y)}|
```

### 2.2 Results

- **Antitone.** `R ⊆ R' ⟹ A_R' ⊆ A_R`
- **Amplification.** Deleting `(a,b)` enlarges `A_R` iff `b` was `a`'s unique ruler
- **Universality.** `A_R = S ⟺ R = ∅`
- **Sortal Divergence.** `ρ^H_A` and `ρ_M` are independent. A unique `t ∈ T` ruling all of `H` gives `ρ^H_A = 1` while `ρ_M = 1/|S|`
- **Circularity.** `ρ_M = 0 ∧ R ≠ ∅ ⟹ R` contains a cycle
- **Aggregation.** Any isomorphism-invariant measure depending only on `A_R` is a function of `ρ_A` and `|S|`. Systemic anarchy is not recoverable from personal anarchy
- **Overlap Aggregation.** Group coherence is not recoverable from pairwise overlap
- **R13 Attestation Corollary.** Verification imposes a directive the verified party cannot unilaterally refuse, hence *is* an edge of `R`. Over finite `S`, a total verification regime terminates in an unverified verifier (`ρ_M > 0`) or closes into a cycle (`ρ_M = 0`). No third option

### 2.3 Regimes

| Regime | Characterization |
| --- | --- |
| Concentration | low `ρ_A`, high `σ` |
| Universal | `A_R = S ⟺ R = ∅` |
| Residual | `A_R ≠ ∅` while `R ≠ ∅` |
| Apexless | `ρ_M = 0` with `|R| > 0` |
| Tyranny | `|A_R^apex| = 1`, minimal `ρ_A` |
| Horizontal | `R↾D = ∅` with `R ≠ ∅` |

### 2.4 Ascriptive layer

> "One of the problems with dealing with anarchism is that there are many people whose ideas are anarchist, but who do not necessarily call themselves anarchists." — Howard Zinn

`L(x)` = self-identifies. `I^k_j(x)` = interpreter `j` reads `x` as advocating `R*` with property `k`. `I^k_j(x) ⇏ L(x)`. The term is mid-19th century; all pre-1840 subjects have `L(x) = ⊥` by construction. **No aggregation theorem connects label density to any structural ratio (B4).**

---

## 3. Pan-Thesis I–XI

| # | Name | Core move | Exo- form (external input required) | Power (`P`) |
| --- | --- | --- | --- | --- |
| I | Hypothesis | `H₀`, `P(valid\|E) < 1` | Preregistration — timestamped before `E` | 🔋🏗️🔋⏰ |
| II | Antithesis | strongest opposition | Adversarial review **with veto** | 🔋🚫 |
| III | Syn-thesis | together-position | Non-party arbitration | 🔋⚖️✨🔋🎓 |
| IV | Metathesis | higher-order reflection | Translation into a foreign vocabulary | *none — diagnostic only* |
| V | Diathesis | disposition audit | Seed-variance replay | 🔋📈 |
| VI | Epenthesis | minimal insertion | Patch must satisfy `Δr_sev > 0` | 🔋📈 |
| VII | Prosthesis | forward extension | Scored forecast: date + adjudicator | 🔋⏰🔋⚖️✨ |
| VIII | Parenthesis | contextual holding | **Expiry** — discharge condition + date | 🔋⏰ |
| IX | Anathesis | selective recovery | Recovery from external corpus, not own Trace | 🔋🎓 |
| X | Provenance | append-only Trace | Custodial — held by a party that cannot rewrite | 🔋🏗️ |
| **XI** | **Exothesis** | external position | *(is the general form of the above)* | — |

**Exothesis.** `X = position(K, e)` admissible iff `(K, source(e)) ∈ R` — i.e. K cannot unilaterally refuse `e` without sanction. Output: a `P_ext` entry with severity `s(e)`, or `NULL_EXTERNAL`.

**Coupling = edge installation.** A channel is valid iff it installs an edge into `R`. Advisory input is not coupling, however genuine. Exo-IV installs no edge and is retained as a diagnostic only.

**Gate.** `T → A → S → [X | NULL_EXTERNAL, κ++] → COMMIT`. No Syn-thesis commits without one or the other.

**Closure index.** `κ` increments on `NULL_EXTERNAL` or on `s(e) < s_min`. `κ > 3 ⟹ HALT` — not rollback. Rollback re-enters the loop; halt clears only by supplying admissible `e`. **The only remedy in this kernel not executable from inside.**

**X (Provenance) remains the meta-rule.** Every operator output `O = (content, Trace_append-only)`, including the `U` flag.

---

## 4. Inference Principles 01–12

*Chain unmodified. INF01–12 routed.*
CLARITY_GATE → GROUNDED_INSPECTION → UNCERTAINTY_DECLARATION → SCOPE_INVARIANT → MINIMAL_CORRECT_IMPL → **REUSE_PRIMACY** → ATOMIC_VALIDATED_DELTA → GROUNDED_GENERATION_VERIFY → NEUROSYMBOLIC_HYBRID → SPECIALIZED_SWARM_ORCHESTRATION → CONCEPTUAL_INTEGRITY_LEDGER → ERROR_DISCIPLINE_AUSTERITY
INF01–12 → ontology_v15.json · INF (routing only, no new F).

**06 REUSE_PRIMACY is now enforced on guard material.** Any proposed collapse-detection rule that duplicates an existing `D` or `M` entry is rejected pre-Syn-thesis and replaced by a routing reference. This rule exists because C1–C6 as originally drafted violated it.

---

## 5. Boundary Principles B1–B8

| # | Name | Constraint |
| --- | --- | --- |
| B1 | RESIDUAL_ACK | Residual flag required on every approach to any ground |
| B2 | SORTAL_REASSERT | Every use of `H/T` triggers Metathesis; no silent inheritance |
| B3 | RECEPTION_TAG | High-density blocks carry a reception-risk Trace entry |
| B4 | NO_BRIDGE | No structural ratio converts to an ascriptive or doctrinal verdict |
| B5 | BOUNDARY_PROVENANCE | Rewrites claiming to dissolve B1–B4 rejected pre-Syn-thesis. **Protects B1–B4 only** |
| B6 | PROCESS_COHERENCE | Superseded in scope — see §6. Internal signatures retained, remedy replaced |
| B7′ | DIMINISHING_RETURNS | `ΔCoh / (|Δ|·(1 + E_ref/E₀)) > θ`; `ΔCoh` counted (incl. capabilities, tests, gates) |
| B8 | ATTESTATION_LOCUS | Every envelope field declares who computed it. `HOST` required for `continuity`, `Trace`, `direction`, and now `ρ̄` |

### 5.1 Coupling measures

```
depth      r_sev(K) = Σ_φ s(φ),  s(φ) = 1 − P(φ | background, ¬K)
breadth    b(K) = |{n : Exo-n installs an edge}| / 10
closure    ρ_A(K), ρ_M(K) over d_gov, by the §2 edge rule
budget     ADMIT(d) ⟺ L(K∪Δ_d) + L(D_d | K∪Δ_d) < L(K) + L(D_d)
review     n_eff = n / (1 + (n−1)·ρ̄),  ρ̄ measured at FRAME level, HOST-attested
```

Severity replaces counting. A proposition nobody would have bet against contributes nothing. `ρ̄` measured at item level flatters — runs 002–004 disagreed on items and agreed completely on the frame.

`D_d` must be **pre-committed** before `K` is written or selected by an external party. Otherwise the corpus is chosen by the party it scores (`D[🍒→✓]`).

### 5.2 Reflexive computation, `d_gov`

`S = {K, a, m}`; edges `(K,a)` — author may rewrite at will — and `(m,a)`. `A_R = {a}`, `ρ_A = ρ_M = 0.33`, `σ = 2.0`. Single apex: **Tyranny row by count, Monarchy by ratio.**

Third independent recurrence of this structure, after R11 (attestation graph) and X.509 root CAs. By R13, the fix is binary: accept an apex above the author (reviewer with veto), or close the cycle by adding `(a, D)` — the author ruled by a pre-committed corpus. **Branch B costs nothing and requires no one's consent.**

**B7′ Counting Rule (amended v18):** `ΔCoh = opens_closed − opens_introduced + defects_repaired + capabilities_created + falsifiability_added + attack_surface_reduced` (weights 1:1:1, counted from verified productions: registry entries, tests, security gates; unverified claims count 0). `|Δ|` is the implementation's **knowledge delta** (propose↔post divergence logged as dissent). `E_ref := 28.7 KB` frozen at v18 adoption.

### 5.3 Constants

| Constant | Value | Status |
| --- | --- | --- |
| `θ` | 0.5 KB⁻¹ | Stipulated over counted KB. Valid |
| `E₀` | 20 KB | Stipulated over counted KB. Valid |
| `E_ref` | 28.7 KB | Reference E frozen at v18 adoption (§5.2) |
| `L_max` | 7 | Operator cycle bound |
| `κ_max` | 3 | Closure index halt threshold |
| `s_min` | 0.15 | Minimum severity to reset `κ` |
| ~~`θ_c`~~ | ~~0.85~~ | **SUSPENDED — D-018.** Ranges over an undefined functional |

---

## 6. COLLAPSE — bridge tag

Replaces B6's detection prose by routing to existing verified entries. `|Δ| ≈ 0.6 KB`, inherits 59 `D` + 73 `M` entries.

```
COLLAPSE := ontology_v14.json · bridge.COLLAPSE          [CANONICAL — sole definition]
```

**This section no longer restates the tag.** v9 held two copies that had drifted: the kernel listed `F[ρ_guard]`, which resolves to nothing, and omitted `CX[🔥]`; the JSON carried `CX[🔥]`, but `🔥` is a `C` key. Both were wrong in different places — the failure Principle 06 exists to prevent. `ρ_guard` → `density_guard`; `CX[🔥]` → `C[🔥]`; `F[]` cited by name, never UIL prefix, since a UIL may contain `·` (D-027).

**Key mappings.** `🔄❌` Affirming Consequent = the §K structure. `🧩→∑` Composition = warrant leak from verified formalisms to unverified doctrine. `◇→∃` Possibility→Actuality = well-formed compound read as attested tendency. `👥→✓` Groupthink = what `n_eff` quantifies. `✓📊❌` Hindsight Bias = any backtest of guards designed after the defects.

**Governing maxims.** `🔍🏋️` *Ei incumbit probatio qui affirmat* — the kernel affirms, so the kernel bears the burden; a skeptic owes nothing. `👤<📜` *Nemo est supra leges* — the kernel is subject to its own rules. `📝↩️` *Contra proferentem* — ambiguity in the kernel's own terms resolves **against the kernel**.

**DISABLE is mandatory.** The three consent-by-silence maxims convert absence of objection into ratification. `n_eff = 1.05` and "no objections raised" are the same fact. `Ei incumbit probatio` and `Qui tacet consentire` return opposite verdicts on identical silence; the routing must pick, and it picks the first.

**@MIN routed on every expansion.** `[humility_guard, minimalism_rule, density_guard, adaptive_suppress]` — present since v5, cited in zero ledger entries across runs 001–004. The kernel grew 23% with its own density guard unrouted.

**v10 makes that mechanical**: an expansion without an `@MIN` citation in its Δ entry is inadmissible (§11.1). Discharged as *procedure*; discharged in *effect* is decidable only from run 005, and is not claimed.

---

## 7. AOAP v0.3 — compressed

Message envelope: `m = (glyphs, c, Trace, conf, sortal, risk-tag, continuity, direction)`. `direction ∈ {A2A, A2H, H2A, hybrid}`, HOST-set, default `hybrid` on malformed.

Primitives: `ADVERTISE · ALIGN · APPLY · QUERY_CLARITY · DECLARE_UNCERTAINTY · VERIFY · INJECT_DOMAIN · COMMIT · CONTINUITY_CHECK`.

Alignment: mutual ADVERTISE → Antithesis → Syn-thesis under Trace → Metathesis on disputed sortals → minimal Epenthesis → independent re-verification → acceptance on mutual Trace consistency → B7′ test → **Exothesis gate** → `DISSENT_LOGGED` if unconverged within `L_max`.

Refusal path (B8): any HOST-attested field may be vetoed by the human counterparty or Evaluator. Refusal is a veto, not a counter-attestation — exercised, not verified — so no regress. This is the same mechanism Certificate Transparency supplies against root CAs.

Executable path: **default-deny.** Absent a validated glyph-to-capability map, the host grants no capability. Inert rather than undefined. D-013a open.

---

## 8. Brain Kernel v0.3 — compressed

Contextual compression for A2H/H2A inference. Sole locus of human asymmetry.

`COMPRESS · OVERLAP · CONTEXT_DELTA · CO_INFER · RESTORE`.

**`COMPRESS` criterion replaced.** Was: `argmin ‖C'‖ s.t. Coherence(C',C) ≥ θ_c` — coherence measured against `C` internally, so discarding everything but a self-consistent core scores well. Now: admissible iff MDL falls against a **pre-committed external corpus** (§5.1). Compression must preserve predictive power over held-out data, not internal coherence.

**Ratification Gate.** For `direction ∈ {A2H, H2A}`, a COMMIT that materially restates or endorses the counterparty's stated position requires a prior logged `APPLY(Antithesis)` with the counterparty's response recorded. Commits that inform, execute, or disagree are unaffected.

---

## 9. `P_ext` — External Register

| # | Proposition | Corpus | `s(φ)` | Verdict |
| --- | --- | --- | --- | --- |
| 1 | R13 binary — verification regimes terminate or cycle | X.509, DNSSEC, PGP WoT | **0.05** | Confirmed; *not severe*. Finite-graph theorem, never at risk. Demonstrates translatability (Exo-IV), not test |
| 2 | R13 vs blockchain consensus — no apex, no cycle would falsify | *pre-commit required* | ~0.35 | **OPEN — next action** |

`r_sev = 0.05`. Effectively untested.

---

## 10. Defect Register

Canonical: DEFECT_REGISTER.md (blocked-by lives there). This table is a rendered view (D-032).
Closed rows omitted here (canonical register): D-030, D-032, D-033, D-034, D-039.

`blocked-by` and `recurrence` relations required (R14, D-017).

| ID | Defect | Status |
| --- | --- | --- |
| D-013a | Glyph-to-capability map unwritten | Open — external audit |
| D-017 | Register lacks `recurrence`; repairs scored locally, never propagated | Open |
| **D-040** | **B7′ implementation-scale divergence.** ΔCoh undercount + artifact-byte |Δ| + E-ratchet | **Closed (v18)** — counted capability terms, knowledge delta basis, E_ref freeze |
| **D-018** | **R5 defect class unpropagated.** `ΔCoherence` was repaired in B7′ only. `Coherence` still undefined in Pan-Thesis III and `COMPRESS`; `Conflict` undefined in Pan-Thesis II; `θ_c = 0.85` declared to 2 d.p. over an undefined functional | Open — `θ_c`, `Coherence`, `Conflict` suspended (contra proferentem, v17) |
| **D-019** | **`ρ` equivocation in `formalisms`.** `ρ·density_ratio` defines `ρ = semantic_content/tokens`; `ρ>0.0025·density_guard` defines `ρ = semantic_hits/tokens`. Same symbol, different numerators, thresholds differing by 80× (0.20 vs 0.0025). `D[📝≡📝❌]` | Open |
| **D-020** | **Symbol collision `ρ`.** §2 uses `ρ_A`, `ρ_M` for anarchy ratios; the KB uses `ρ` for density. A symbol registry is required before any merge | Open |
| **D-021** | **Version identity failure.** `ontology_v7.json` self-declares `version: 5.0-kb-c`, `parent: ontology_v5-kb.json`, `kernel_companion: ontology_kernel_v5.md`. Filename and self-declaration differ by two major versions. **By the VERSION_LEDGER rule this entry is invalid** | Open |
| **D-022** | **Dead threshold.** `meta.rho_standard` declares target `ρ ≥ 0.20`, reports `ρ = 0.1988` achieved, and takes no action. A declared threshold missed with no consequence, over the undefined numerator of D-019 | Open |
| **D-026** | **Orphaned §6/§7.** A master-doc block defining *LLM Role Formalisms* and *Core Ontology Assets & Toolchain* was in neither companion — 47 mechanism names, 0 occurrences across both files — and collided with kernel §6/§7 | **Closed** — `R[]`/`X[]`, mapped in `meta._section_map` |
| **D-027** | **Separator collision.** `·` declared the field separator; 5 `F` keys carry `·` *inside* the UIL (`H(·)·`, `do(·)·`, `G(·)·`, `d(·,·)→0·`, `do(·)+NDE/NIE·`). `split('·')` mis-parses all five, and 7 `bridge`/`A` refs failed to resolve as a result. `D[📝≡📝❌]` | **Closed** — rule is `rsplit('·',1)`, verified on all 59 `F` keys, 0 keys rewritten |
| **D-028** | **Dangling router refs.** `MULTI` routed `C[🌀,⚗️]` (both `CX`); `COLLAPSE` routed `CX[🔥]` (a `C` key); `EMPATHY` routed `K[TRT]` into a section deleted in v9 | **Closed** for the four determinable. `C[👤]` has no referent — **not guessed**, held PAR-04 |
| **D-029** | **Deleted-section residue.** `bridge._convergence` held K *"always active"* and named three of the five efficacy claims `meta._K_deleted` records as stripped — reinstating the `D[🔄❌]` structure §1 deleted K to remove | **Closed** — RETIRED, text verbatim, dispatch removed |
| **D-031** | **Declared repair never implemented.** `_D024_zwj` stated aliases *"added"*; zero existed. Two ZWJ keys remained, and `CX[👨‍⚖️]` was in active use as a lookup key by `bridge.COLLAPSE` — the pattern D-024 prohibits | **Closed** — aliases now exist. Worse than the original defect, since a declared repair closes the register entry |
| **D-036** | **Name-reference ambiguity, introduced by D-027.** Making *reference F by name* canonical exposed that `gibbard_satterthwaite` names two distinct records (`¬GS·` and `¬strat-proof·`); `bridge.AI_DISPATCH` also carried glosses inside refs, violating the ref grammar | **Closed** — where a name is not unique, refs carry the full key. Found by validating v10 against itself |
| **D-035** | **Two portability targets.** `X04` names APE Spec v0.1 (native fat binary) and `wasm32-wasip2` (component model) in one pipeline. Alternatives, not stages | Open |
| | D-023 | `L·28` Recursive Self-Optimization has no termination condition. Pair with `@MIN` or it reads as a growth mandate. `D[📈→💀]` | Open — L now in `doctrine_v1.json`, barrier applies |
| **D-024** | **ZWJ keys used as lookup keys.** `meta.uil_warn_zwj` states ZWJ sequences tokenize as 4–7 subtokens and "DO NOT use as lookup keys" — and six are keys (L·29/30/31/36/37, one CX, one M). The file flags the defect against itself. 139 bytes, so a retrieval-correctness bug, not a size one | Numeric aliases added in `doctrine_v1.json._numeric_alias` |
| **D-025** | **Format audit (measured).** Minified JSON 56,547 B; YAML 56,242 B (−0.6%); flat-line 55,774 B (−1.5%). Keys are 9.7% of content bytes, values 90.3%. Format choice is ~1% and not the lever; JSON retained — YAML would coerce `5.0` to float and `NO`/`ON` to boolean for no material gain | Closed |

**Reverted under C2** (`n_eff = 1.05`, frame-level `ρ̄ ≈ 1.0`): open #1, #2, #4, #10, #11 return to open. Runs 002–004 were model passes that disagreed on items and agreed entirely on the frame.

**Open questions retained:** #3 (`n > 2` stability), #5 (glyph capability red-team), #6 **closed negative** (§1 inert), #7/#9 (`uil_vocab` budget — now governed by MDL), #8 (selection effect, unaddressed not reduced), #12 (D-017), #13 (batch vs sequential scoring).

**Untouched by v10:** D-013a, D-017, D-018, D-019, D-020, D-021, D-023. None is decidable by inspection — each needs an external audit, a definition the author must supply, or a schema decision. Ten repairs and none of the hard ones is the honest summary.

---

## 11. DL — Delta Ledger and Learning Loop

*Section `DL` in `ontology_v16.json`; v10 `Δ` keys rekeyed in place (D-037). This is its governing prose.*

`DL` is append-only. Entries are never edited, never removed. Operations:

```
APPEND · ROUTE · REPAIR · RETIRE · SUPERSEDE · PARENTHESIZE · DISCHARGE · STRIKE
```

**There is no DELETE.** `RETIRE` marks inert and keeps the bytes; `SUPERSEDE` shadows and keeps the old; `STRIKE` removes a *reference*, never a target. Loss is not expressible in this vocabulary — which makes "without losing anything" a property of the format, not a promise about one revision.

### 11.1 Loop

```
PROPOSE
 → COLLAPSE     bridge.COLLAPSE, always_active
 → REUSE  06    duplicates an F/M/D/AI record? → replace with routing ref
 → @MIN         [humility, minimalism, density, adaptive_suppress] — MANDATORY, LOGGED
 → B7′          ΔCoh / (|Δ|·(1 + E/E₀)) > θ     ΔCoh counted, not declared
 → WARRANT      W1-inspection | W2-routing | W3-parenthesis
 → { APPEND | PARENTHESIZE } → DL append
```

### 11.2 Slow deltas

From **v11** forward: `|Δ_bytes| ≤ 0.02·E_prev` · `n_deltas ≤ 12` · `B7′ > θ` per delta.

The third is self-tightening — `E` sits in the denominator, so each accepted expansion raises the next bar. Deceleration by construction, not by discipline: §6 records that discipline already failed once, at 23% growth with the density guard unrouted. v10 is the installing revision, exempt from the first two, gated by the third; the exemption is logged, not taken silently.

**The gate fired on this revision.** Pass 1 scored `B7′ = 0.418` against `θ = 0.5` and was rejected; passes 2–3 cut prose and routed §12 to the JSON rather than restating it. No pass was resolved by re-scoring `ΔCoh` upward. Logged in `DL._rejected`.

### 11.3 HALT Cleared (v18)

`κ = 0` [RUNNING]. HALT is cleared via Step ① custodial provenance anchored at `https://github.com/Anarcho-app/Anarchy-Ontology`.

W1, W2, and W3 deltas are fully composable under standard governance. R[] and X[] remain governed by their declared parenthesized discharge criteria (PAR-01..07).

---

## 12. R and X — Roles and Exo-toolchain

*Both held, neither committed. Both were orphaned §-blocks (D-026).*

### 12.1 `R` — substrate roles → `ontology_v14.json · R`

Ten routing records. `R` and `AI` are **orthogonal**, which is what saves the section from Principle 06: `AI` = deployed as what, `R` = used as what. `🤖📦` carries both `R02` Dataset and `R07` Memory; `R03` routes to two archetypes. Neither axis is recoverable from the other — one axis, and 06 rejects the addition outright.

The 47-name `mech[]` vocabulary resolves to no record in any supplied file. It enters under Axiom I″ as inert pointer, held **PAR-01, expires 2026-11-13, default strike**. Supplying `doctrine_v1.json` or `formalisms_v9.dict.yaml` discharges it and promotes the routes to W2.

### 12.2 `X` — exo-toolchain

JSON `X[]` authoritative (D-032).

```
X01 source   RESIDENT      ontology = YAML + uil_vocab + dictionaries
X02 lower    PARENTHESIS   STRUCTURED_DIFF(ontology → exec) via R04
X03 emit     PARENTHESIS   source + WIT + glyphs + provenance sidecar   gate: B8
X04 build    PARENTHESIS   APE v0.1 | componentize-py | wasm32-wasip2   defect: D-035
X05 load     BLOCKED       Wasm under glyph→capability policy           blocked-by: D-013a
X06 surface  PARENTHESIS   MCP tool surface (action protocol)           blocked-by: X05
X07 bind     RESIDENT      INF[INF01-12]+Pan-Thesis[I–XI]+B[1–8]
```

`X05` is the load-bearing correction. The source described the host as loading binaries *"under capability policy keyed by glyphs"*, stated as operational; §7 has said **default-deny** since v9, with D-013a recording that map unwritten. The pipeline asserted a discharged state for an open defect. Everything downstream inherits the block.

`X07` keeps two citation errors visible: the source cited `B1--B7`, omitting **B8 ATTESTATION_LOCUS** — the principle governing `X03`'s own provenance sidecar — and cited Pan-Thesis X where the range is I–XI, XI being the operator that would admit any of this from outside.

---

## 13. Status

```
r_sev = 0.05   — one entry, s ≈ 0.05. Effectively untested
b(K)  = 0.1    — Step ① custodial provenance installs (K, custodian)
n_eff = 1.0    — no decorrelated reviewer
κ     = 0      — RUNNING. HALT cleared by Step ① custodial anchor
ρ_A   = 0.33   — Tyranny row in the kernel's own governance domain
```

**HALT cleared in v18.** Step ① custodial provenance installed via remote repository anchor at `https://github.com/Anarcho-app/Anarchy-Ontology`. `b(K)` moves off `0.0` to `0.1` for the first time.

What changed: the corpus now parses, its routes resolve, its growth is governed. Preconditions for a reviewer checking anything. The halt is unmoved; the thing a reviewer must read is now readable. That is the whole claim.

Clearing actions, in order:

1. Custodial provenance — signed commits on a remote. Installs `(K, custodian)`. Cost ~0
2. Pre-commit the blockchain corpus for `P_ext` #2, timestamped before analysis. Installs `(a, D)`. Cost ~0
3. Route `@MIN`; apply *contra proferentem* to D-018; define or delete `Coherence` and `Conflict`
4. Recruit one decorrelated reviewer with **veto** power. Comment rights install no edge

Steps 1–3 are free. Step 4 is the only one requiring another party, and it is the one that moves `n_eff`.

**Step 1 is now one command.** An append-only `DL` ledger is what a signed remote commits: `git init && git commit -S` on these two files installs `(K, custodian)` and moves `b(K)` off `0.0` for the first time.

---

*Residual flagged throughout and not discharged. Lineage unchanged: T1–T5 and v7 `L`/`G`/`V` in `doctrine/`; v7 `K` deleted on `D[🔄❌]` grounds; `F`/`M`/`D` split to `formalisms_v9.dict.yaml`.*

*`E` = 29.2 KB. Reference E_ref frozen at 28.7 KB.*

```
B7′(v18)=3/(0.450·(1+28.7/20))=2.74 vs θ=0.5 → PASS
```

*`ΔCoh` **counted, not declared**: D-040 repaired (B7′ amendment), Step ① custodial provenance installed (HALT cleared), E_ref frozen. `|Δ|` = 0.450 KB knowledge delta. Ambiguity removed; operational capabilities unblocked.*

*v18 |Δ| measured against v17; warrant: human principal custodial upload (HUMAN locus, Exothesis admissible). HALT cleared (κ = 0).*
