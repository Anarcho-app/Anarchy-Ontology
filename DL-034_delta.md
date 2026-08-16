# Delta Package — DL-034a, DL-034b, DL-035

*Revised 2026-08-16 against `uil_grammar_v1.yaml`, `uil_vocab.yaml`, `uil_sorts.yaml`, `uil_sort_annotations.yaml`, `uil_constructors.yaml`. **Unreviewed and unapplied.***

**Headline: the physics admission FAILS the gate under an honest count, and the recommendation is a logged exemption, not a re-score.** Details in §3 and §6.

---

## 0. Correction to the previous revision

The prior draft of this document defined a four-rule "UIL conformance standard" inferred from `ontology_v18.json`'s emoji keys. That inference was **wrong**. The actual UIL system:

| Layer | Reality | What the prior draft assumed |
|---|---|---|
| Base vocabulary | **176 ASCII uppercase tokens** (`CAUSE`, `INTERVENE`, `MARKOV_BLANKET`), each with a `latex` symbol field (`▷`, `⊛`, `⊙`) | emoji glyphs |
| Sorts | **6, two tiers** — Entity / Procedure / Proposition / Quantity (primary), Relation / Proof (structural). Use-based | not modelled |
| Constructors | **10, `addition_only`, permanent once introduced**, each with operational semantics | not modelled |
| Composites | 47 | not modelled |
| Formalism map | 643 entries | not modelled |

The emoji in `ontology_v18.json` are neither base glyphs nor latex symbols — they are a **third, undocumented keying layer**. That is worth its own defect id if you agree; this package does not open one.

### 0.1 UIL conformance, restated correctly

| # | Rule | Source |
|---|------|--------|
| U1 | Keys are ASCII identifiers matching the grammar's `<identifier>` production. No emoji, no ZWJ. | `uil_grammar_v1.yaml` |
| U2 | Every record carries a **sort** from the existing six. Use-based: sort is what you DO with it, not what it IS. | `uil_sorts.yaml` |
| U3 | New files **do not extend** `base_glyphs` (`fixed_point`) or `constructors` (`addition_only`, permanent). Classify with the existing system; do not enlarge it. | `uil_vocab.yaml`, `uil_constructors.yaml` |
| U4 | Two reserved symbol sets are spelled in ASCII: host variables (rho, beta, kappa, sigma, lambda, epsilon, theta, Gamma, delta) and **all ten constructor symbols**, which dispatch. | D-020, D-042 |

`physics_v1.json` v1.1 conforms to all four and declares each in `meta`.

---

## 1. Three deltas — score and apply SEPARATELY

| id | Content | Gate |
|---|---|---|
| **DL-034a** | CX observer repair (D-041) | **PASS** |
| **DL-034b** | `physics_v1.json` admission (PAR-08) | **FAIL** — logged exemption recommended |
| **DL-035** | PAR-01 partial discharge (34 of 37 names resolve) | **PASS** |

**Do not bundle these.** DL-035 scores high enough to carry DL-034b over the gate if combined, and doing so would be the exact pattern the ledger records as never having happened: no pass resolved by inflating the numerator. Bundling a large win with a failing delta is the same move by another route. Kept separate on purpose.

---

## 2. DL-034a — CX observer repair

### D-041 (new)

| Field | Value |
|---|---|
| **Defect** | Sortal conflation in `CX[🔮]`. The essence string welds `Awareness_changes_reality` to `Bayesian_witness`. These name incompatible operations: the first is quantum-measurement collapse, where the observable has no determinate value before measurement; the second is classical conditioning, where it does. |
| **Grounds** | `D[📝≡📝❌]` Equivocation, primary. `D[◇→∃]` secondary. |
| **Decidable by** | Inspection. The contradiction is internal to one value string. |
| **recurrence** | PAR-08 / `physics_v1.json _quantum_scope`, and now specifically PH-006 vs PH-008: order-sensitivity is strictly weaker than contextuality, which is the precise error the conflation makes. |

**Before (v18, verbatim — no DELETE op exists, bytes preserved here):**

```
"🔮": "Observer=Awareness_changes_reality,Bayesian_witness ¬Paralyzed/Oblivious · game · F[ℐ(θ),MB(X),faith] · L[13,34,26]"
```

**After:**

```
"🔮": "Observer=Bayesian_witness,belief_update_under_evidence ¬Paralyzed/Oblivious · game · F[ℐ(θ),MB(X),faith] · L[13,34,26]"
```

Operation **REPAIR**, warrant **W1**. Key, shadow, domain, F refs and L refs unchanged — the surviving F refs (Fisher information, Markov blanket, faithfulness) are all classical-inference objects and were always consistent with `Bayesian_witness`. The removed clause was the entry's only quantum-flavoured content, which is itself evidence the weld was decorative.

**Grounds are internal.** PH-001 and PH-008 are how this was noticed; they are **not** what it stands on. Had the physics file been the warrant, this repair would be W3 and would leak physics into CX — the exact failure the sink exists to prevent.

### Gate

ΔCoh = `defects_repaired` 1 = **1**. |Δ| ≈ 0.20 KB.

```
B7' = 1 / (0.20 × 2.435) = 2.05   vs θ = 0.5   → PASS
```

---

## 3. DL-034b — physics_v1.json admission

### PAR-08

```json
"PAR-08": "physics_v1.json admitted as constraint-only sink · sort-annotated per uil_sorts, extends no vocabulary · symbol discipline covers host variables AND all 10 UIL constructor symbols, D-020 and D-042 unreachable by construction · ADMITTED UNDER LOGGED EXEMPTION, B7' FAILED — see DL-034b · discharge: D-020 and D-042 closed and no-free-collision assertion passes, permitting promotion of eligible PH entries into F[] with sorts carried · 2026-11-13 · default:remains sink, no promotion, no escalation"
```

### Gate — this is the part that matters

ΔCoh, conservative, amended B7′ rule:

```
attack_surface_reduced   +1   (named containment boundary)
opens_introduced         -1   (PAR-08)
                        ----
ΔCoh                      0
```

```
B7' = 0 / (0.90 × 2.435) = 0.00   vs θ = 0.5   → FAIL
```

Generous count (`+1 falsifiability_added` for the four externally-checkable quantum constraints): ΔCoh = 1, B7′ = 1/(0.90 × 2.435) = **0.456** — **still FAIL**, by 9%.

**Both conventions reject it.** The v1.0 draft of this package scored it 0.51 conservative on a smaller file and flagged that anything above |Δ| ≈ 0.82 KB would fail. Expanding the quantum block pushed it over. The prediction held and the gate fired.

**Recommended disposition: admit under a LOGGED EXEMPTION, precedent v10.** The v10 installing revision was exempted from two of the three slow-delta rules, gated by the third, and the ledger records that the exemption was logged rather than taken silently. The same shape applies here. The alternative honest routes:

1. **Exemption** — admit, log the failing score, cite the v10 precedent. Recommended.
2. **Trim** — cut to 6 entries and pass at ~0.51. Costs the quantum block, which is the file's strongest content.
3. **Hold** — do not admit; keep `physics_v1.json` outside the corpus until D-042 closes and the promotion path is real.

What is **not** available: re-scoring ΔCoh upward until it passes.

---

## 4. DL-035 — PAR-01 partial discharge

PAR-01 states that 47 `R[].mech[]` names resolve to no record in any supplied file, discharge condition "each resolves or is struck", default strike. With `uil_vocab.yaml` supplied, this is now decidable.

```python
import yaml
d = yaml.safe_load(open('uil_vocab.yaml'))
known = (set(d['base_glyphs']) | set(d['composite_glyphs'])
         | set(d['formalism_glyph_map']) | set(d['aliases']) | set(d['args']))
mech = sorted({m for r in R.values() for m in r.mech})   # 37 unique
hit, miss = [m for m in mech if m in known], [m for m in mech if m not in known]
```

**Result: 34 resolve, 3 do not.**

```
UNRESOLVED → EMPATHIC_SIGNAL · LAYER_HEALTH_WEIGHT · PARITY_PROFILE
```

**Two findings, not one.** The count is also wrong: the `R01..R10` mech lists hold **39 names with duplicates, 37 unique** (`MEMTOOL` and `PARITY_PROFILE` each appear twice). "47" has no referent.

**Disposition:** DISCHARGE PAR-01 for the 34; default `strike` applies to the remaining 3, which by the ledger's own definition removes the *reference*, never the target — the three names stay in `R08`/`R03`/`R06`/`R10` and lose only their claim to resolve.

### Gate

Two counting conventions disagree sharply here, and the divergence is itself a finding:

| Convention | ΔCoh | B7′ (|Δ| ≈ 0.35 KB) | Verdict |
|---|---|---|---|
| Amended B7′ rule (`opens_closed` etc.) | 1 | 1.17 | PASS |
| Declared ΔCoh unit (one reference-graph edge made to resolve) | 34 | 39.9 | PASS |

Both pass, so nothing turns on it here — but **the two rules differ by 34× on the same delta**, and there is no reconciliation between them anywhere in the corpus. That is D-018-adjacent: two counting rules for one quantity, no stated relation. Worth an id.

---

## 5. D-042 (new) — UIL constructor / operator symbol collision

Seven of ten constructor symbols also appear in the grammar's generic `<operator>` production. Four collide with live corpus usage:

| Symbol | As constructor | Also means | Where |
|---|---|---|---|
| `→` | `apply` — **MCP tool dispatch** | "implies" | `ontology_v18.json meta.format` |
| `→` | | generic arrow | dozens of D / M / F keys |
| `∇` | `measure` — run measurement | gradient | `F[∇L=0·kkt_conditions]` |
| `≡` | `attest` — attach proof | identity | `D[📝≡📝❌]` |
| `∀` | `quantify` | universal, inside fallacy names | `D[📊→∀]`, `D[🏆→∀]`, `D[1️⃣→∀]` |

Four are **consistent, not collided**: `⊢` matches `entail`'s type signature; `↾` matches kernel §2's `R↾D` restriction exactly; `∧` and `∨` are used as conjunction and disjunction throughout. `∝` and `∘` appear nowhere else.

**Why this outranks D-020.** A rho ambiguity misleads a reader. A `→` ambiguity means a UIL token stream cannot be distinguished from a dispatch instruction — the constructor file states plainly that `apply` **is** the MCP tool dispatch. Same defect class, but this one is executable.

**Blocked-by chain, first real one in the corpus:** `D-042 → D-020 → D-019 → D-022`.

---

## 6. Governor accounting

E = 29.2 KB, E₀ = 20 KB, E_ref = 28.7 KB → denominator factor **2.435**. θ = 0.5 KB⁻¹.

| Delta | ΔCoh | |Δ| est. | B7′ | Verdict |
|---|---|---|---|---|
| DL-034a | 1 | 0.20 | 2.05 | PASS |
| DL-034b | 0 / 1 | 0.90 | 0.00 / 0.46 | **FAIL both** |
| DL-035 | 1 / 34 | 0.35 | 1.17 / 39.9 | PASS |

**Slow-delta rule (a), |Δ_bytes| ≤ 0.02·E_prev = 584 B.** Kernel-side edits total ~75 B (companion line only). Passes.

**Rule (b), n_deltas ≤ 12.** Three. Passes.

**All |Δ| figures are estimates I produced, not measurements.** `D[🍒→✓]` fires undischarged across all three: authored and scored by the same party, with no pre-committed corpus. Recount before applying — DL-034b's verdict is already FAIL and will not improve, but DL-034a sits at 2.05 and would only fail above |Δ| ≈ 0.82 KB.

**Governor gap, restated.** E is bytes of the *kernel* `.md`. A 11 KB companion file costs the governor 75 bytes. That is what makes the modular design fit rule (a) — and it may be a hole rather than a feature, since the rule is satisfiable by moving material sideways into companions, which is what DL-034b does. Flagged, not exploited silently.

---

## 7. What this package does not do

- **Does not close D-020.** Still open, still four unregistered instances beyond rho (theta, Gamma, beta, kappa). Now joined by D-042 above it in the chain.
- **Does not fully discharge PAR-01.** 34 of 37; three strike by default.
- **Does not move n_eff.** 1.0. No decorrelated reviewer, including for `physics_v1.json` itself, whose ten entries and sort assignments are unchecked.
- **Does not move r_sev.** Every PH entry is a published result nobody would bet against. That is what a constraint file is for, and also why it earns no credibility.
- **Does not move b(K).** No edge installed into the ruled-by relation.

**Honest summary:** one contradiction removed, one containment boundary built that the gate rejects, thirty-four references resolved, two miscounts corrected, one executable-grade defect found. The largest single item is DL-035, and it was decidable only because a file was supplied — which is the whole lesson. The binding constraint remains n_eff = 1.0, and none of this reaches it.
