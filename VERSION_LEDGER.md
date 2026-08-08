# VERSION_LEDGER

Append-only. One row per version. Filename and self-declared version must match or the entry is invalid.

| Filename | Self-declared | Compiled | $E$ at compile (KB) | CONTINUITY hash (sha256, body pre-§10) |
| --- | --- | --- | --- | --- |
| `ontology_kernel_v8.2.md` | v8.3 | 2026-08-08 | 10.0 (est., residual) | not recorded |
| `ontology_kernel_v8.4.md` | v8.4 (run 001) | 2026-08-08 | 19.0 | superseded |
| `ontology_kernel_v8.4.md` | v8.4 (run 002) | 2026-08-08 | 20.7 | superseded |
| `ontology_kernel_v8.4.md` | v8.4 (run 003) | 2026-08-08 | 21.2 | `f2b178ae54c934c82924a2474fccfa3509b54bf7aa0c64ef87f78f51002d8614` |

**Row 1 defect (logged, not corrected).** The v8.2-named file self-declared v8.3 and listed `ontology_kernel_v8.3.md` as itself. Under Pan-Thesis X this failed the meta-rule the document declares non-negotiable. Retained here rather than silently fixed, per append-only discipline.

**Hash scope.** Computed over the document from the title through the end of §9, excluding the Findings Log (§10) and footer. Recomputable by truncating at the `## 10. Findings Log` header. Per B8 this value is `HOST`-computed over the serialized file, not model-emitted.

```
verify:  python3 -c "import hashlib;print(hashlib.sha256(open('ontology_kernel_v8.4.md',encoding='utf-8').read().split('## 10. Findings Log')[0].encode()).hexdigest())"
```
