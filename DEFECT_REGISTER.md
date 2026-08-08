# DEFECT_REGISTER

Append-only. Instrument of B7': makes the `defects repaired` term of $\Delta$Coh auditable.

**Deferral note.** Per the operational criterion added in run 003 (5.2), this register is scored normally at the next revision. If it fails, it is removed.

**Admission note.** This file was admitted under the B7' bootstrap exception (5.2), not by passing the inequality. Its own `defects repaired` count could not be scored, because scoring it required this register to exist. Circularity stated rather than concealed. Exception 1 of 1 for revision v8.4.

| ID | Defect | Found | Repaired by | Status |
| --- | --- | --- | --- | --- |
| D-001 | B7 denominator omitted $\lvert\Delta\rvert$ | run 001 (R3) | B7' (5.2) | repaired |
| D-002 | $n_{\text{exp}}$ counted submissions, not change; bundling free | run 001 (R4) | B7' $E$ term | repaired |
| D-003 | $\Delta$Coherence self-declared, unfalsifiable | run 001 (R5) | counted $\Delta$Coh | repaired |
| D-004 | Axiom I did not isolate T1--T5 from §9 | run 001 (R8) | Axiom I' (1.3) | repaired |
| D-005 | Filename / self-declaration mismatch (v8.2 vs v8.3) | run 001 | v8.4 + VERSION_LEDGER | repaired |
| D-006 | `direction` defaulted to A2A, the least-guarded case | run 001 | mandatory, host-set, default hybrid (8.2) | repaired |
| D-007 | §8.4 alignment procedure had no terminal state | run 001 | `DISSENT_LOGGED` (8.4 step 9) | repaired |
| D-008 | $L_{\max}$ undeclared, leaving B6 cycle detection inoperable | run 001 | declared constants (5.2) | repaired |
| D-009 | No anti-sycophancy mechanism despite 5.1 naming it the primary hazard | run 001 | Ratification Gate (§9) | repaired |
| D-010 | Findings exemption an unbounded bypass | run 002 (R9) | 4.0 KB findings cap (5.2) | repaired |
| D-011 | B7' instruments unscoreable (bootstrap circularity) | run 002 (R9/G1) | bootstrap exception (5.2) | repaired |
| D-012 | No context-budget mechanism for `uil_vocab` after R10 exclusion | run 002 (R10) | partition criterion identified (run 004); **blocked by D-013a** | open |
| D-013a | Glyph-to-capability map unwritten | run 001 | none --- awaiting external audit | open |
| D-013b | Behaviour undefined absent a map | run 001 | default-deny, fails closed (8.9) | repaired |
| D-014 | Host is a unique apex, $\rho_A = \rho_M = 0.20$ (B8-induced) | run 002 (R11) | refusal path (5.3); was **blocked by D-016** | repaired |
| D-015 | Bootstrap exception had no qualifying criterion | run 003 (E2) | register/mechanism criterion + deferral (5.2) | repaired |
| D-016 | Attestation cycles (intended) and operator cycles (B6 signature) are not distinguished | run 003 (R13) | category error --- different relations (5.1) | repaired |
| D-017 | Defect dependencies untracked; register is a flat set | run 004 (R14) | none | open |
| D-018 | Batch vs sequential B7' scoring unspecified | run 004 (R15) | none | open |

**Dependency note (R14).** D-014 was blocked by D-016; D-012 is blocked by D-013a. The register does not yet carry a `blocked-by` column (D-017), so these were found only by attempting resolution.

**Counting rule.** A `defects repaired` increment is valid only against a row transitioning to `repaired` in the same revision. Rows already `repaired` do not re-count.