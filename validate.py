#!/usr/bin/env python3
"""
validate.py — Anarchy-Ontology corpus validator.

Implements the invariants the corpus already DECLARES but never CHECKED.
Every check maps to a declared rule; none introduces a new claim (W1).

Usage:
    python3 validate.py [--repo .] [--uil-dir DIR] [--json]

Exit 0 = all checks PASS or BLOCKED. Exit 1 = any FAIL.

BLOCKED is distinct from FAIL: the check is well-defined but its input is
absent from the repo. A BLOCKED check is a finding about the corpus, not
about the validator.
"""
from __future__ import annotations
import argparse, json, re, sys, unicodedata
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

PASS, FAIL, BLOCK, WARN = "PASS", "FAIL", "BLOCKED", "WARN"
results: list[tuple[str, str, str, list[str]]] = []


def report(cid, status, headline, detail=None):
    results.append((cid, status, headline, detail or []))


# ── C1  E rule (kernel meta._E_rule / D-033) ────────────────────────────────
def c1_e_rule(repo: Path):
    k = repo / "ontology_kernel_v18.md"
    if not k.exists():
        return report("C1", BLOCK, "kernel absent")
    actual = len(k.read_bytes()) / 1000
    m = re.search(r"`?E`?\s*=\s*([\d.]+)\s*KB", k.read_text(encoding="utf-8"))
    if not m:
        return report("C1", FAIL, "no declared E in kernel")
    decl = float(m.group(1))
    ok = abs(decl - actual) < 0.05
    report("C1", PASS if ok else FAIL,
           f"E declared {decl} KB, measured {actual:.1f} KB",
           [] if ok else [f"delta {abs(decl-actual):.2f} KB — D-033 rule is bytes/1000, UTF-8"])


# ── C2  companion byte declarations ─────────────────────────────────────────
def c2_companions(repo: Path):
    k = repo / "ontology_kernel_v18.md"
    if not k.exists():
        return report("C2", BLOCK, "kernel absent")
    txt = k.read_text(encoding="utf-8")
    bad, seen = [], 0
    for name, decl in re.findall(r"`([\w./-]+\.(?:json|yaml|md))`\s*\(([\d.]+)\s*KB", txt):
        f = repo / name
        if not f.exists():
            bad.append(f"{name}: DECLARED {decl} KB but ABSENT from repo")
            continue
        seen += 1
        act = len(f.read_bytes()) / 1000
        if abs(float(decl) - act) >= 0.1:
            bad.append(f"{name}: declared {decl} KB, measured {act:.1f} KB")
    report("C2", PASS if not bad else FAIL,
           f"{seen} companion size declarations checked", bad)


# ── C3  VERSION_LEDGER row for current version ──────────────────────────────
def c3_ledger(repo: Path):
    k, led = repo / "ontology_kernel_v18.md", repo / "VERSION_LEDGER.md"
    if not (k.exists() and led.exists()):
        return report("C3", BLOCK, "kernel or ledger absent")
    ver = re.search(r"ontology_kernel_v(\d+)\.md", k.name).group(1)
    rows = re.findall(r"ontology_kernel_v([\d.]+)\.md", led.read_text(encoding="utf-8"))
    ok = ver in rows
    report("C3", PASS if ok else FAIL,
           f"VERSION_LEDGER row for v{ver}",
           [] if ok else [f"ledger holds rows up to v{max(rows, key=lambda s: float(s.split('.')[0]))}; "
                          f"v{ver} has NO ROW. Ledger rule: 'One row per version.'"])


# ── C4  defect register canonicity (kernel §10 claims register is canonical) ─
def c4_defects(repo: Path):
    k, reg = repo / "ontology_kernel_v18.md", repo / "DEFECT_REGISTER.md"
    if not (k.exists() and reg.exists()):
        return report("C4", BLOCK, "kernel or register absent")
    ktxt, rtxt = k.read_text(encoding="utf-8"), reg.read_text(encoding="utf-8")
    kids = set(re.findall(r"\bD-(\d{3}[a-z]?)\b", ktxt))
    rids = set(re.findall(r"\bD-(\d{3}[a-z]?)\b", rtxt))
    orphan = sorted(kids - rids, key=lambda s: (len(s), s))
    detail = []
    if orphan:
        detail.append(f"{len(orphan)} ids in kernel §10 absent from canonical register: "
                      f"D-{', D-'.join(orphan)}")
        detail.append("kernel §10 declares 'Canonical: DEFECT_REGISTER.md ... This table is a "
                      "rendered view'. The rendered view is the ONLY source for these.")
    if "blocked-by" not in rtxt.lower():
        detail.append("register has NO blocked-by column; DL-019 declared it added (D-031 pattern)")
    report("C4", PASS if not detail else FAIL,
           f"kernel §10 ids={len(kids)}, register ids={len(rids)}", detail)


# ── C5  key/parse rule: rsplit('·',1) on F keys (D-027) ─────────────────────
def c5_parse(repo: Path, ont: dict):
    bad = []
    for key in ont.get("F", {}):
        if "·" not in key:
            bad.append(f"F key without separator: {key!r}")
            continue
        uil, name = key.rsplit("·", 1)
        if not name or not re.fullmatch(r"[a-z][a-z0-9_]*", name):
            bad.append(f"F key name not snake_case after rsplit: {key!r} -> {name!r}")
    report("C5", PASS if not bad else FAIL,
           f"{len(ont.get('F', {}))} F keys parsed by rsplit('·',1)", bad)


# ── C6  reference resolution (FORMALISM CLOSURE / orphan-freeness) ──────────
SKIP_SECTIONS = {"B", "W", "PE", "KB", "GY", "US", "SH", "MDL", "UIL", "ZWJ",
                 "CTC", "APE", "BPE", "TEST", "H", "T", "S", "R13", "MCS"}


def _balanced_refs(text):
    """Yield (section, body) with bracket balancing — refs contain nested [] and ()."""
    for m in re.finditer(r"\b([A-Z]{1,3})\[", text):
        sec, i, depth = m.group(1), m.end(), 1
        while i < len(text) and depth:
            depth += (text[i] == "[") - (text[i] == "]")
            i += 1
        if depth == 0:
            yield sec, text[m.end():i - 1]


def _split_top(body):
    """Split on commas at bracket/paren depth 0."""
    out, buf, d = [], "", 0
    for ch in body:
        d += ch in "([" 
        d -= ch in ")]"
        if ch == "," and d == 0:
            out.append(buf); buf = ""
        else:
            buf += ch
    out.append(buf)
    return [t.strip() for t in out if t.strip()]


def c6_refs(repo, ont, doc):
    fkeys = set(ont.get("F", {}))
    fnames = {k.rsplit("·", 1)[1] for k in fkeys}
    fuil = {k.rsplit("·", 1)[0] for k in fkeys}
    idx = {s: set(v) for s, v in ont.items() if isinstance(v, dict)}
    idx["F"] = fnames | fkeys | fuil
    lk = set()
    for k in doc.get("L", {}):
        lk.add(k)
        if "·" in k:
            lk.add(k.rsplit("·", 1)[1])
    idx["L"] = lk

    by_name = by_uil = checked = 0
    unresolved, uil_refs, expect = [], [], []

    def walk(node, path):
        nonlocal checked, by_name, by_uil
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, f"{path}.{k}")
        elif isinstance(node, str):
            for sec, body in _balanced_refs(node):
                if sec in SKIP_SECTIONS or sec not in idx:
                    continue
                for tok in _split_top(body):
                    if ".." in tok or tok.startswith("_") or "–" in tok or "-" in tok[:1]:
                        continue
                    checked += 1
                    if sec == "E" and re.search(r"[|²ₙ₊₁−∇]|\(.*,.*\)", tok):
                        expect.append(f"E[{tok[:34]}]  ({path})")
                        continue
                    if sec != "F":
                        if tok not in idx[sec]:
                            unresolved.append(f"{sec}[{tok}]  ({path})")
                        continue
                    if tok in fnames or tok in fkeys:
                        by_name += 1
                    elif tok in fuil:
                        by_uil += 1
                        uil_refs.append(f"F[{tok}]  ({path})")
                    else:
                        unresolved.append(f"F[{tok}]  ({path})")

    walk(ont, "ont")
    ded = lambda xs: list(dict.fromkeys(x.split("  (")[0] for x in xs))
    u, g, e = ded(unresolved), ded(uil_refs), ded(expect)
    detail = [f"F refs by NAME (conformant): {by_name}",
              f"F refs by UIL PREFIX (violates bridge._note + D-036): {by_uil} "
              f"— {len(g)} distinct"]
    if g:
        detail.append("  e.g. " + ", ".join(g[:8]))
    if e:
        detail.append(f"E[...] AMBIGUOUS: {len(e)} distinct uses are the expectation "
                      f"operator, not Entities refs — ref grammar cannot disambiguate")
    if u:
        detail.append(f"TRULY UNRESOLVED: {len(u)} distinct")
        detail += ["  " + x for x in u]
    report("C6", PASS if not (u or g) else FAIL,
           f"{checked} refs checked", detail)


# ── C7  file-level orphan freeness (grammar invariant 1) ────────────────────
def c7_orphans(repo: Path):
    files = [p for p in repo.iterdir() if p.is_file() and p.name != ".DS_Store"]
    blobs = {p.name: p.read_text(encoding="utf-8", errors="replace") for p in files}
    orph = []
    for name in blobs:
        incoming = sum(1 for other, txt in blobs.items() if other != name and name in txt)
        if incoming == 0:
            orph.append(f"{name}: 0 incoming references — orphan")
    report("C7", PASS if not orph else FAIL,
           f"{len(files)} files, orphan-freeness per grammar invariant 1", orph)


# ── C8  PAR expiry ──────────────────────────────────────────────────────────
def c8_par(ont: dict, today="2026-08-16"):
    rows, expired = ont.get("PAR", {}), []
    for k, v in rows.items():
        if k.startswith("_") or not isinstance(v, str):
            continue
        m = re.search(r"(20\d\d-\d\d-\d\d)", v)
        if m and m.group(1) < today and "DISCHARGED" not in v:
            expired.append(f"{k}: expired {m.group(1)}, default applies")
    report("C8", PASS if not expired else FAIL,
           f"{len([k for k in rows if not k.startswith('_')])} PAR holdings, none past expiry", expired)


# ── C9  symbol free-collision (D-020 / D-042) ───────────────────────────────
def c9_symbols(repo: Path):
    if not (repo / "SYMBOL_REGISTRY.md").exists():
        return report("C9", BLOCK, "assert_no_free_collision: SYMBOL_REGISTRY.md absent",
                      ["D-020 open. PAR-08 discharge blocked. Check is written and will run "
                       "the moment a registry exists."])
    report("C9", WARN, "registry present — collision logic not implemented in v1.0")


# ── C10  UIL sort coverage ──────────────────────────────────────────────────
def c10_uil(repo: Path, uil_dir: Path | None):
    src = None
    for cand in ([repo] + ([uil_dir] if uil_dir else [])):
        if (cand / "uil_vocab.yaml").exists():
            src = cand
            break
    if src is None or yaml is None:
        return report("C10", BLOCK, "uil_vocab.yaml not in repo",
                      ["X01 declares 'ontology = YAML + uil_vocab + dictionaries' RESIDENT.",
                       "The file is absent from the repo, so X01's RESIDENT status is unbacked.",
                       "PAR-01 (34/37 resolvable) and PAR-05 both blocked on this."])
    v = yaml.safe_load((src / "uil_vocab.yaml").read_text(encoding="utf-8"))
    ann = yaml.safe_load((src / "uil_sort_annotations.yaml").read_text(encoding="utf-8"))["annotations"]
    detail, ok = [], True
    for sec in ("base_glyphs", "composite_glyphs"):
        n = len(v.get(sec, {}))
        cov = len(set(v.get(sec, {})) & set(ann))
        line = f"{sec}: {cov}/{n} sorted"
        if cov < n:
            ok = False
            line += f"  ({n-cov} UNSORTED)"
        detail.append(line)
    real = {k: x for k, x in v.get("aliases", {}).items()
            if k not in ("version", "purpose", "note") and not k.startswith("_")}
    known = set().union(*(set(v.get(s, {})) for s in
                          ("base_glyphs", "composite_glyphs", "formalism_glyph_map", "args")))
    dang = [k for k, x in real.items() if (x if isinstance(x, str) else str(x)) not in known]
    if dang:
        ok = False
        detail.append(f"aliases: {len(dang)}/{len(real)} DANGLING (build_obsidian_pages.py input)")
    report("C10", PASS if ok else FAIL, f"UIL vocabulary integrity ({src})", detail)


# ── C11  physics_v1.json conformance (its own declared discipline) ──────────
RESERVED_SYM = set("ρβκσλεθΓδ∇≡∀↾∝∘⊢")


def c11_physics(repo: Path):
    p = repo / "physics_v1.json"
    if not p.exists():
        return report("C11", BLOCK, "physics_v1.json absent")
    d = json.loads(p.read_text(encoding="utf-8"))
    sorts = {"Entity", "Procedure", "Proposition", "Quantity", "Relation", "Proof"}
    bad = []
    for k, val in d.get("PH", {}).items():
        if not re.fullmatch(r"PH-\d{3}", k):
            bad.append(f"{k}: key violates PH-NNN rule")
        parts = [s.strip() for s in val.split("·")]
        if len(parts) < 6:
            bad.append(f"{k}: {len(parts)} fields, schema requires 6")
        elif parts[1] not in sorts:
            bad.append(f"{k}: sort {parts[1]!r} not in uil_sorts")
        for ch in val + k:
            if ch in RESERVED_SYM:
                bad.append(f"{k}: reserved symbol {ch!r} present")
                break
            if unicodedata.category(ch) == "So" and ord(ch) > 0x2100:
                bad.append(f"{k}: emoji {ch!r} present")
                break
    report("C11", PASS if not bad else FAIL,
           f"{len(d.get('PH', {}))} PH entries, sort + symbol discipline", bad)


# ── C12  JSON wellformedness + leaf count (assert_superset input) ───────────
def c12_leaves(ont: dict):
    def count(n):
        return sum(count(v) for v in n.values()) if isinstance(n, dict) else 1
    report("C12", PASS, f"ontology_v18.json parses; {count(ont)} leaf fields")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--uil-dir", default=None)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    repo = Path(a.repo).resolve()
    uil = Path(a.uil_dir).resolve() if a.uil_dir else None

    ont = json.loads((repo / "ontology_v18.json").read_text(encoding="utf-8"))
    doc = json.loads((repo / "doctrine_v1.json").read_text(encoding="utf-8"))

    c1_e_rule(repo); c2_companions(repo); c3_ledger(repo); c4_defects(repo)
    c5_parse(repo, ont); c6_refs(repo, ont, doc); c7_orphans(repo); c8_par(ont)
    c9_symbols(repo); c10_uil(repo, uil); c11_physics(repo); c12_leaves(ont)

    if a.json:
        print(json.dumps([{"id": c, "status": s, "headline": h, "detail": d}
                          for c, s, h, d in results], indent=2, ensure_ascii=False))
    else:
        w = {PASS: 0, FAIL: 0, BLOCK: 0, WARN: 0}
        print(f"\nvalidate.py — {repo}\n" + "=" * 72)
        for cid, st, hl, det in results:
            w[st] += 1
            print(f"[{st:7}] {cid}  {hl}")
            for line in det:
                print(f"            · {line}")
        print("=" * 72)
        print(f"PASS {w[PASS]}   FAIL {w[FAIL]}   BLOCKED {w[BLOCK]}   WARN {w[WARN]}\n")
    return 1 if any(s == FAIL for _, s, _, _ in results) else 0


if __name__ == "__main__":
    sys.exit(main())
