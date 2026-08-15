# VERSION_LEDGER

Append-only. One row per version. Filename and self-declared version must match or the entry is invalid.

| Filename | Self-declared | Compiled | $E$ at compile (KB) | CONTINUITY hash (sha256, body pre-§10) |
| --- | --- | --- | --- | --- |
| `ontology_kernel_v8.2.md` | v8.3 | 2026-08-08 | 10.0 (est., residual) | not recorded |
| `ontology_kernel_v8.4.md` | v8.4 (run 001) | 2026-08-08 | 19.0 | superseded |
| `ontology_kernel_v8.4.md` | v8.4 (run 002) | 2026-08-08 | 20.7 | superseded |
| `ontology_kernel_v8.4.md` | v8.4 (run 003) | 2026-08-08 | 21.2 | superseded |
| `ontology_kernel_v8.4.md` | v8.4 (run 004) | 2026-08-08 | 22.8 | `e3653f96d7c5e047da07e73bad76b748c1380fc0fd6f0abde05cc544787b3e5c` |
| `Anarchy-Ontology/ontology_kernel_v9.md` | v9 | 2026-08-08 | 14.9 | `3556ada9d7c714bd0a5d071ea46212d56f7f2ccaeb1abc1ae61755a4cbae6ba2` |
| `ontology/ontology_kernel_v10.md` | v10 | 2026-08-13 | 28.9 | `398250fae1855949bf3ae252a72fdb59a04e3943491b728089162643d30f4a88` |
| `ontology/ontology_kernel_v11.md` | v11 | 2026-08-13 | 29.4 | `a4068458c9046e3605383d3cd0482a279da930d10040fc2107c148c1752a14ae` |
| `ontology/ontology_kernel_v12.md` | v12 | 2026-08-13 | 29.4 | `2b4b54c8f17f36d1eebcdba9f1c4f37d52dd350f0033f441d35dc9b5e294319e` |
| `ontology/ontology_kernel_v13.md` | v13 | 2026-08-13 | 29.3 | `1bfc7c83908141902bf2bac88f71b85e5a4eccff858be7497f725509f8c29715` |
| `ontology/ontology_kernel_v14.md` | v14 | 2026-08-13 | 28.9 | `d9b7bc7762d23acc6439ba80bcf2446a8a44744eef6222414c85f4879031b146` |
| `ontology/ontology_kernel_v15.md` | v15 | 2026-08-13 | 28.8 | `6212d8b7c9c2cca0a8477f9c13d647bdbb6f95f56afa0a0bc6791434030a5f96` |
| `ontology/ontology_kernel_v16.md` | v16 | 2026-08-13 | 28.4 | `f4410ee487112019fc95522f191e525c11f1510a50b151c6d520e9f0f4926d89` |
| `ontology/ontology_kernel_v17.md` | v17 | 2026-08-13 | 28.7 | `cbcbe1cbf6a7b0295b44b4d9021b2f345bb302d9d9920bb6726a368c86d7ce66` |

**Baseline transition (2026-08-08).** v9 is the baseline kernel. Canonical kernel home: `Anarchy-Ontology/` — a clean git clone of upstream, sync preserved per the one-way import direction `dict ← kernel ← json`; local `ontology/` artifacts are derived. v9 hash scope: title through end of §9, truncated at the `## 10. Defect Register` header; HOST-computed via sha256. Bootstrap note: the v9 realignment (exothesis tool, θ_c suspension, B8 ρ̄, opsx skill realignment) was executed fast-path under user directive — Exothesis satisfied by HUMAN locus; B7' register-only exception declared, to be scored next revision.

**Row 1 defect (logged, not corrected).** The v8.2-named file self-declared v8.3 and listed `ontology_kernel_v8.3.md` as itself. Under Pan-Thesis X this failed the meta-rule the document declares non-negotiable. Retained here rather than silently fixed, per append-only discipline.

**Hash scope.** Computed over the document from the title through the end of §9, excluding the Findings Log (§10) and footer. Recomputable by truncating at the `## 10. Findings Log` header. Per B8 this value is `HOST`-computed over the serialized file, not model-emitted.

```
verify:  python3 -c "import hashlib;print(hashlib.sha256(open('ontology_kernel_v8.4.md',encoding='utf-8').read().split('## 10. Findings Log')[0].encode()).hexdigest())"
```

**Derived-artifact update (2026-08-10).** `benchmark-ssot-and-routes` change touched derived ontology artifacts only — **kernel E unchanged (14.9 KB)**. Changes: `model_catalog.yaml` v3.1→v3.2 (added `route:` field to 10 models; removed all hand-copied benchmark fields — net KB reduction); `model_benchmarks.yaml` (full rewrite to 10 current-gen models, `meta.last_sync_source: openrouter-verified`). Continuity verified: drift gate PASS, tier resolution 0 errors, catalog self-consistency PASS, 8/8 invariant tests. Kernel file (`Anarchy-Ontology/ontology_kernel_v9.md`) not modified.

**Derived-artifact update (2026-08-10, 2nd).** `threshold-aligned-ladder` change: `model_catalog.yaml` v3.2→v3.3 (added 4 frontier OpenRouter model definitions; x-high/high gained `fallback_model_ref`; critical `fallback_model_ref` → `fallback_policy` task-aware table); `model_benchmarks.yaml` (+4 frontier SSOT entries, 14 total). **Kernel E unchanged (14.9 KB)** — derived artifacts only. Continuity verified: drift gate PASS (14 approved models), tier resolution 0 errors, 13/13 fallback resolver tests. Kernel file not modified.

**Derived-artifact update (2026-08-10, 3rd).** `add-uil-sort-system` change: new sort system files — `uil_sorts.yaml` (6 sorts, 2 tiers, ~1.6 KB), `uil_constructors.yaml` (11 constructors with type signatures + operational semantics, ~3.7 KB), `uil_sort_annotations.yaml` (176 base glyph sort annotations, ~5 KB); propagated sort annotations to 26 dictionary YAMLs (693 entries, 100% coverage). Grammar redesigned: `grammars/uil/grammar.js` (8-level precedence, zero conflicts, pipeline/expression ambiguity removed). New modules: `mcp_infra/uil_typer.py` (sort inference engine), `mcp_infra/uil_canon.py` (canonicalization + BLAKE3 hash-of-normal-form), `mcp_infra/uil_compiler.py` (type-directed compiler stub). **Kernel E unchanged (14.9 KB)** — derived artifacts only. Continuity verified: 113 tests passing across 4 test files, 100/100 formalisms typed with full coverage, 36/36 valid corpus entries parse cleanly, zero conflicts in tree-sitter generation, D-019 ρ collision structurally unrepresentable (verified by test). Kernel file (`Anarchy-Ontology/ontology_kernel_v9.md`) not modified. Continuity hash for change artifacts: `386b2a52f2d8c77b7b637780711ee08d48c8277fdec34829c1d7f4f3c25211eb`.

**Derived-artifact update (2026-08-12).** `add-latent-geometry-probing-harness` change (archived with B7' dissent): new MCP server `mcp_infra/servers/latent_geometry_probing_mcp_server.py` (6 falsifiable probes + BLAKE3 ledger + SQLite run store); `ontology/tooling_catalog.yaml` (+LATENT_GEOMETRY_PROBING intent), `ontology/dispatch_v7-bootstrap.yaml` (+router line + slice), `ontology/micro_router_vocab.yaml` (+formalism ID). **Kernel E unchanged (14.9 KB)** — derived artifacts only. 14/14 tests pass. B7' post-score DISSENT_LOGGED (0.13 < 0.5): proposal |Δ| estimate (8 KB) conflated proposal-artifact bytes with implementation bytes (51 KB); dissent accepted as metric-input finding, not correctness failure. See `openspec/findings/2026-08-12-b7-prime-implementation-scale-divergence.md`. Kernel file not modified.

**v10 row added (2026-08-13).** `ontology/ontology_kernel_v10.md` at 28.9 KB, hash `398250fa...`. Hash scope: title through end of §9, split on `## 10. Defect Register` (HOST-computed).

**v11 row added (2026-08-13).** `ontology/ontology_kernel_v11.md` at 29.4 KB, hash `87008f92...`. |Δ| = 523 B ≤ 577 B budget. W1-only inspection release: register/ledger/ASCII/X07 repairs, HALT stands.

**v12 row updated (2026-08-13, W1 repair).** `ontology/ontology_kernel_v12.md` at 29.4 KB, hash `2b4b54c8...`. |Δ| = 3 B ≤ 587 B budget. W1 repair: restored deleted Inference Principles name-chain in §4 (undoing illegal delete, ΔCoh = 3), fixed companions byte size (64.4→65.2 KB), corrected corrupt ledger hash. HALT stands.

**v13 row added (2026-08-13, W1 routing).** `ontology/ontology_kernel_v13.md` at 29.3 KB, hash `1bfc7c83...`. |Δ| = 109 B ≤ 588 B budget. W1 routing: INF04–06 added as routing records (04→D[📝≡📝❌,🧩→∑], 05→F[minimalism_rule,minimal_mcs], 06=REUSE_PRIMACY rule itself). HALT stands.

**Verify command note.** The published verify command still splits on `## 10. Findings Log` (v8.4). v9+ headers are `## 10. Defect Register`. Using the old split hashes the whole file. v9/v10/v11 rows use Defect Register.

```
verify (v8.4):  python3 -c "import hashlib;print(hashlib.sha256(open('ontology_kernel_v8.4.md',encoding='utf-8').read().split('## 10. Findings Log')[0].encode()).hexdigest())"
verify (v9+):   python3 -c "import hashlib;print(hashlib.sha256(open('ontology_kernel_v11.md',encoding='utf-8').read().split('## 10. Defect Register')[0].encode()).hexdigest())"
```

**Residual.** Upstream clone ledger (`Anarchy-Ontology/VERSION_LEDGER.md`) still has no v9 row. Not silently fixed.

**v17 row added (2026-08-13, W1 repair).** `ontology/ontology_kernel_v17.md` at 28.7 KB (28,683 B), hash `cbcbe1cb...`. |Δ| = 304 B ≤ 567 B budget. W1 repairs: D-039 (B3 reception tag — dense formal blocks carried no reception-risk marker; found by external boundary-principles audit 2026-08-13 at 83.3% formal density; closed same revision by global risk-tag), D-018 disposition (`Coherence`/`Conflict` SUSPENDED under *contra proferentem* — ambiguity resolves against the kernel; `θ_c` suspension stands; status remains open pending author definition or deletion). ΔCoh = 2 counted (D-039 repaired, D-018 dispositioned); B7′ = 2/(0.304·(1+28.4/20)) = 2.72 > 0.5 PASS. HALT stands (κ = 4): clearing steps ①② await external locus — ① custodial provenance blocked (no git remote, no signing key configured; user action), ② corpus pre-commit pending selection. Companion `ontology_v17.json` (DL-032 appended; meta version/filename/kernel_companion updated to v17). **Note (flagged, not fixed):** canonical register D-018 ("batch vs sequential B7′ scoring", run 004) and kernel §10 D-018 ("R5 defect class", θ_c) share one ID with distinct descriptions — append-only discipline forbids silent rekey; resolve by SUPERSEDE in a future revision.

**Derived-artifact declaration (2026-08-14).** `declare-v7-ops-yaml-v17-derived` change (W1-inspection): the v7-named operational YAMLs — `routing_v7.yaml` (7.20), `dispatch_v7-bootstrap.yaml` (7.22), `ontology_v7-core.yaml` (7.24) — are **live derived aliases of the v17 kernel** (`meta.kernel_companion: ontology_kernel_v17.md`, `meta.derived_of: v17` added; filenames and 7.x self-declared versions intentionally frozen — a rename would be a W2 event under HALT and would break spec-hardcoded paths). `status_v7.md` kernel row repaired to name `ontology_kernel_v17.md` Active. **Kernel E unchanged (28.7 KB); kernel body untouched; HALT (κ = 4) unchanged.** Residual (named, not closed): `ontology_v17.json` `meta.formalisms` still references `formalisms_v9.dict.yaml`, which is absent from disk — retargeting is a separate W1 delta; the file is not fabricated here.

**v18 row added (2026-08-15, B7′ amendment + HALT clearance).** `ontology/ontology_kernel_v18.md` at 29.2 KB (29,234 B), hash `caa497e62f8a286322f55b061230098a33aa6fb3bda06cacd3d216a03e230d68`. |Δ| = 450 B knowledge delta ≤ 584 B budget. Adopts B7′ amendment (D-040: counted capability/falsifiability/attack-surface terms, |Δ| knowledge delta basis, E_ref freeze at 28.7 KB). HALT cleared (κ = 0 [RUNNING]) via Step ① custodial provenance anchored at `https://github.com/Anarcho-app/Anarchy-Ontology`; b(K) = 0.1. ΔCoh = 3 counted (D-040 repaired, Step ① installed, E_ref frozen); B7′(v18) = 3/(0.450·(1+28.7/20)) = 2.74 > 0.5 PASS. Companion `ontology_v18.json` (DL-033 appended; PAR-06 discharged; meta updated to v18).