# AI Universal Ontology Kernel v9

```
r_sev(K) = 0.05      b(K) = 0.0      n_eff = 1.0      κ = 4  [HALT]
ρ_A(d_gov) = 0.33    ρ_M(d_gov) = 0.33               E = 14.9 KB
```

*Header metrics are the kernel's own status, recomputed per revision. All four are bad. See §11.*
*Filename and self-declaration must match; see `VERSION_LEDGER.md`.*
*v9 is a **subtraction release**. `E` falls from 22.8 KB. Companion files: `ontology_v9.json` (49.8 KB — bridge, F, A, M, D, E, P, C, CX, AI, N, TRT), `doctrine_v1.json` (11.3 KB — L, G, V, W3-isolated), `doctrine/process_ontology_v1.md` (T1–T5).*
*KB load falls 59.3 → 49.8 KB, a 16% reduction in kernel context budget. 408 of 417 v7 entries preserved; the 9 removed are v7 §K (5 efficacy claims), `bridge.TRANSCEND` (routed to W3), `meta.rho_standard` (D-022), `meta.uil_warn_zwj` (superseded by D-024). `K.TRT` is retained as a procedure with efficacy claims stripped.*

---

## 1. Scope

This kernel governs reasoning procedure. It contains no cosmology, no theology, and no claims about its own effect on readers.

**Moved out (not deleted).** T1–T5 Process Ontology → `doctrine/`. Justification is internal: Axioms I and I′ forbid anything downstream from quantifying over or inheriting interpretation from T1–T5, so its removal delta is zero by construction. The axioms that made §1 safe are the axioms that make it removable. **Open #6 closes in the negative.**

Axioms I and I′ are retained here, since they govern the import barrier:

**Axiom I / I′ (NO_BRIDGE).** No formalism in this kernel may quantify over, invoke, or inherit interpretation from `doctrine/`. Conversely, no result here is evidence for or against it. Import direction is one-way and enforced: `dict ← kernel ← json`; `doctrine` is a sink.

**Deleted.** v7 §K, which asserted the kernel's own persuasive effect on readers (`consistency_attraction`: internal consistency "makes it an inference ATTRACTOR"). Grounds: `D[🔄❌]` Affirming the Consequent. Its general LLM-behaviour citations may live in a file that never references this kernel, after the arXiv IDs are verified.

---

## 2. Anarchy-Ontology

*Unmodified from v8.4. The strongest material in the corpus and now load-bearing for §5.*

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

*Unmodified.* CLARITY_GATE → GROUNDED_INSPECTION → UNCERTAINTY_DECLARATION → SCOPE_INVARIANT → MINIMAL_CORRECT_IMPL → **REUSE_PRIMACY** → ATOMIC_VALIDATED_DELTA → GROUNDED_GENERATION_VERIFY → NEUROSYMBOLIC_HYBRID → SPECIALIZED_SWARM_ORCHESTRATION → CONCEPTUAL_INTEGRITY_LEDGER → ERROR_DISCIPLINE_AUSTERITY

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
| B7′ | DIMINISHING_RETURNS | `ΔCoh / (|Δ|·(1 + E/E₀)) > θ`; `ΔCoh` counted, not declared |
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

### 5.3 Constants

| Constant | Value | Status |
| --- | --- | --- |
| `θ` | 0.5 KB⁻¹ | Stipulated over counted KB. Valid |
| `E₀` | 20 KB | Stipulated over counted KB. Valid |
| `L_max` | 7 | Operator cycle bound |
| `κ_max` | 3 | Closure index halt threshold |
| `s_min` | 0.15 | Minimum severity to reset `κ` |
| ~~`θ_c`~~ | ~~0.85~~ | **SUSPENDED — D-018.** Ranges over an undefined functional |

---

## 6. COLLAPSE — bridge tag

Replaces B6's detection prose by routing to existing verified entries. `|Δ| ≈ 0.6 KB`, inherits 59 `D` + 73 `M` entries.

```
COLLAPSE: D[🔄🔄,❓→✓,🔄❌,👥→✓,✓📊❌,🥅→→,🏴→❌,🍒→✓,📊→∀,🧩→∑,∑→🧩,
            📝≡📝❌,◇→∃,💰→⬅️,📈→💀,🏆→∀,✓→🔍,🧠❌,📅≡∀🚫,👁️⏰→🚫]
        · M[🔍🏋️,👤<📜,📝↩️,⚖️👂,🚫→→,❓📜=⛓️,❓=∅,⏹️⚖️,👁️⏰]
        · F[HUMILITY,ρ_guard,ℐ(θ),CK→agree,L>3→shift,⊨⇔⊢]
        · CX[👁️,👨‍⚖️,🔮,♾️]
        · DISABLE[🤫→✓,🔇=✓,🚫⛔→✓]
        · always_active
```

**Key mappings.** `🔄❌` Affirming Consequent = the §K structure. `🧩→∑` Composition = warrant leak from verified formalisms to unverified doctrine. `◇→∃` Possibility→Actuality = well-formed compound read as attested tendency. `👥→✓` Groupthink = what `n_eff` quantifies. `✓📊❌` Hindsight Bias = any backtest of guards designed after the defects.

**Governing maxims.** `🔍🏋️` *Ei incumbit probatio qui affirmat* — the kernel affirms, so the kernel bears the burden; a skeptic owes nothing. `👤<📜` *Nemo est supra leges* — the kernel is subject to its own rules. `📝↩️` *Contra proferentem* — ambiguity in the kernel's own terms resolves **against the kernel**.

**DISABLE is mandatory.** The three consent-by-silence maxims convert absence of objection into ratification. `n_eff = 1.05` and "no objections raised" are the same fact. `Ei incumbit probatio` and `Qui tacet consentire` return opposite verdicts on identical silence; the routing must pick, and it picks the first.

**B6 remedy replaced.** Residual re-assertion, Trace rollback, Evaluator parity, and component isolation are all internal operations — a sealed system executes every one and remains sealed. The remedy is now `κ`-HALT.

**@MIN routed on every expansion.** `[humility_guard, minimalism_rule, density_guard, adaptive_suppress]` — present since v5, cited in zero ledger entries across runs 001–004. The kernel grew 23% with its own density guard unrouted.

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

`blocked-by` and `recurrence` relations required (R14, D-017).

| ID | Defect | Status |
| --- | --- | --- |
| D-013a | Glyph-to-capability map unwritten | Open — external audit |
| D-017 | Register lacks `recurrence`; repairs scored locally, never propagated | Open |
| **D-018** | **R5 defect class unpropagated.** `ΔCoherence` was repaired in B7′ only. `Coherence` still undefined in Pan-Thesis III and `COMPRESS`; `Conflict` undefined in Pan-Thesis II; `θ_c = 0.85` declared to 2 d.p. over an undefined functional | Open — `θ_c` suspended |
| **D-019** | **`ρ` equivocation in `formalisms`.** `ρ·density_ratio` defines `ρ = semantic_content/tokens`; `ρ>0.0025·density_guard` defines `ρ = semantic_hits/tokens`. Same symbol, different numerators, thresholds differing by 80× (0.20 vs 0.0025). `D[📝≡📝❌]` | Open |
| **D-020** | **Symbol collision `ρ`.** §2 uses `ρ_A`, `ρ_M` for anarchy ratios; the KB uses `ρ` for density. A symbol registry is required before any merge | Open |
| **D-021** | **Version identity failure.** `ontology_v7.json` self-declares `version: 5.0-kb-c`, `parent: ontology_v5-kb.json`, `kernel_companion: ontology_kernel_v5.md`. Filename and self-declaration differ by two major versions. **By the VERSION_LEDGER rule this entry is invalid** | Open |
| **D-022** | **Dead threshold.** `meta.rho_standard` declares target `ρ ≥ 0.20`, reports `ρ = 0.1988` achieved, and takes no action. A declared threshold missed with no consequence, over the undefined numerator of D-019 | Open |
| D-023 | `L·28` Recursive Self-Optimization has no termination condition. Pair with `@MIN` or it reads as a growth mandate. `D[📈→💀]` | Open — L now in `doctrine_v1.json`, barrier applies |
| **D-024** | **ZWJ keys used as lookup keys.** `meta.uil_warn_zwj` states ZWJ sequences tokenize as 4–7 subtokens and "DO NOT use as lookup keys" — and six are keys (L·29/30/31/36/37, one CX, one M). The file flags the defect against itself. 139 bytes, so a retrieval-correctness bug, not a size one | Numeric aliases added in `doctrine_v1.json._numeric_alias` |
| **D-025** | **Format audit (measured).** Minified JSON 56,547 B; YAML 56,242 B (−0.6%); flat-line 55,774 B (−1.5%). Keys are 9.7% of content bytes, values 90.3%. Format choice is ~1% and not the lever; JSON retained — YAML would coerce `5.0` to float and `NO`/`ON` to boolean for no material gain | Closed |

**Reverted under C2** (`n_eff = 1.05`, frame-level `ρ̄ ≈ 1.0`): open #1, #2, #4, #10, #11 return to open. Runs 002–004 were model passes that disagreed on items and agreed entirely on the frame.

**Open questions retained:** #3 (`n > 2` stability), #5 (glyph capability red-team), #6 **closed negative** (§1 inert), #7/#9 (`uil_vocab` budget — now governed by MDL), #8 (selection effect, unaddressed not reduced), #12 (D-017), #13 (batch vs sequential scoring).

---

## 11. Status

```
r_sev = 0.05   — one entry, s ≈ 0.05. Effectively untested
b(K)  = 0.0    — no channel installs an edge
n_eff = 1.0    — no decorrelated reviewer
κ     = 4      — HALT. Four commits with NULL_EXTERNAL
ρ_A   = 0.33   — Tyranny row in the kernel's own governance domain
```

**HALT is active.** By §3, no COMMIT proceeds until admissible external input is supplied. The halt cannot be cleared from inside this document.

Clearing actions, in order:

1. Custodial provenance — signed commits on a remote. Installs `(K, custodian)`. Cost ~0
2. Pre-commit the blockchain corpus for `P_ext` #2, timestamped before analysis. Installs `(a, D)`. Cost ~0
3. Route `@MIN`; apply *contra proferentem* to D-018; define or delete `Coherence` and `Conflict`
4. Recruit one decorrelated reviewer with **veto** power. Comment rights install no edge

Steps 1–3 are free. Step 4 is the only one requiring another party, and it is the one that moves `n_eff`.

---

*Residual flagged throughout and not discharged. T1–T5, v7 `L`/`G`/`V` moved to `doctrine/`; v7 `K` deleted on `D[🔄❌]` grounds; `F`/`M`/`D` split to `formalisms_v9.dict.yaml` as the standalone verifiable artifact. `E` = 14.9 KB, down from 22.8. First negative revision. Externally decidable content of this file: D-018 through D-022, all verifiable by inspection of v8.4 and `ontology_v7.json`.*
