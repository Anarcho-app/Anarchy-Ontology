# Anarchy-Ontology

A relativized formal language distinguishing **anarchy** (structural facts about a ruled-by relation \(R\)) from **anarchism** (ascriptive attitudes toward a target relation).

The framework forces explicit indices and keeps the two layers strictly separate. No theorem bridges structural facts about \(R\) to ascriptive facts about speakers. It is offered as a clarifying instrument, not as a political program or complete theory of power.

### Motivation and Scope

Most disputes about anarchy and anarchism collapse two independent questions or suppress required indices. This document isolates those questions. Every structural claim must carry a relation-domain index and a node-subdomain index. Unindexed claims are treated as ill-formed.

The framework is limited and provisional:

- It does not decide whether any historical figure “was an anarchist.”
- It does not rank regimes normatively.
- It relocates disagreement to explicit premises (most often a sortal assignment) rather than claiming to dissolve it.

**Strongest external objection (acknowledged):** high-density formal treatment of anarchism, especially when paired with close analysis of early Christian texts, currently attracts pathologizing dismissal in some reception environments. This is treated as a social constraint on presentation, not as a reason to dilute the formal content.

---

## I. Structural Layer — Anarchy

### Core Definition

\[
\mathrm{An}_R(x) \iff \neg \exists y \, (y \neq x \land x \, R \, y)
\]

- \(R\) is an irreflexive ruled-by relation on a finite set \(S\).
- \(x \, R \, y\) means “\(x\) is ruled by \(y\)”.

\[
A_R = \{ x \in S \mid \mathrm{An}_R(x) \}
\]

Self-rule is not counted as being ruled (*auto-nomos* is compatible with \(\mathrm{An}_R\)).

### Two Predicates

- **Local:** \(\mathrm{an\text{-}archy}_1(x) := \mathrm{An}_R(x)\)
- **Systemic:** \(\mathrm{An\text{-}archy}_2(S,R) := (\rho_M = 0)\)  
  (every ruler is itself ruled)

### Apex vs Hermit

\[
\begin{align*}
\text{apex} &\iff \mathrm{An}_R(x) \land \exists z \, (z \, R \, x) \\
\text{hermit} &\iff \mathrm{An}_R(x) \land \neg \exists z \, (z \, R \, x)
\end{align*}
\]

### Relativization

Every claim requires two indices: relation domain \(d\) and node subdomain \(D \subseteq S\).

\[
\mathrm{An}^D_R(x) \iff x \in D \land \neg \exists y \in D \, (y \neq x \land x \, R \, y)
\]

\[
\rho^D_A = \frac{|A^D_R|}{|D|}, \qquad \rho^D_M = \frac{|A^{D,\mathrm{apex}}_R|}{|D|}
\]

Three practical subdomains:

- **Sortal:** \(S = H \uplus T\) (humans vs non-human/transcendent nodes)
- **Communal:** \(C \subseteq H\)
- **Full:** \(D = S\)

**Theorem (Sortal Divergence)**  
\(\rho^H_A\) and \(\rho_M\) are independent. A unique \(t \in T\) ruling all of \(H\) yields:

\[
\rho^H_A = 1 \quad \text{while} \quad \rho_M = \frac{1}{|S|} > 0
\]

The same configuration is maximal anarchy under the human sort and pure monarchy under the unsorted reading. Disputes over “theocratic anarchism” reduce to this single divergence.

### Key Ratios

\[
\begin{align*}
\rho_A &= \frac{|A_R|}{|S|} \\
\rho_M &= \frac{|A_R^{\mathrm{apex}}|}{|S|} \\
\beta &= \frac{|R|}{|S|} \\
\sigma &= \frac{|R|}{|\{ y \mid \exists x \, (x \, R \, y) \}|}
\end{align*}
\]

Identity: \(\beta = \sigma \cdot \rho_{\mathrm{rul}}\).

### Regimes

| Regime | Characterization |
|--------|------------------|
| Concentration | Low \(\rho_A\), high \(\sigma\) |
| Universal | \(A_R = S \iff R = \varnothing\) |
| Residual | \(A_R \neq \varnothing\) while \(R \neq \varnothing\) |
| Apexless | \(\rho_M = 0\) with \(\|R\| > 0\) |
| Tyranny | \(\|A_R^{\mathrm{apex}}\| = 1\), minimal \(\rho_A\) |
| Horizontal | \(R \upharpoonright D = \varnothing\) with \(R \neq \varnothing\) |

### Core Lemmas and Theorems

- **Antitone:** \(R \subseteq R' \implies A_{R'} \subseteq A_R\)
- **Amplification:** Deleting \((a,b)\) enlarges \(A_R\) iff \(b\) was \(a\)’s unique ruler
- **Universality:** \(A_R = S \iff R = \varnothing\)
- **Restriction monotone:** Shrinking the subdomain can only create anarchy

**Theorem (Circularity)**  
If \(\rho_M = 0\) and \(R \neq \varnothing\), then \(R\) contains a cycle.

**Corollary**  
Horizontal anarchy over \(D\) does **not** imply apexlessness. The two notions pull in opposite directions.

**Aggregation Theorem**  
Any isomorphism-invariant measure that depends only on the set \(A_R\) is a function of \(\rho_A\) and \(|S|\). Systemic anarchy cannot be recovered from personal anarchy alone.

### Edge Rule (Stipulative)

\(x \, R \, y\) holds when \(y\) can impose a directive that \(x\) cannot unilaterally refuse without sanction, and \(y\) is an identifiable person, office, or (under explicit sortal extension) transcendent node. Above household scale, nodes are offices.

| Case | \(\|S\|\) | \(\|R\|\) | \(\rho_A\) | \(\rho_M\) | \(\beta\) | \(\sigma\) |
|------|-----------|-----------|------------|------------|-----------|-----------|
| Household (2+2) | 4 | 4 | 0.50 | 0.50 | 1.00 | 2.00 |
| Monarchy | 5 | 4 | 0.20 | 0.20 | 0.80 | 1.33 |
| Constitutional republic | 5 | 11 | 0.00 | 0.00 | 2.20 | 2.75 |
| Sortal star | 4 | 3 | 0.25 | 0.25 | 0.75 | 3.00 |

---

## II. Ascriptive Layer — Anarchism

> “One of the problems with dealing with anarchism is that there are many people whose ideas are anarchist, but who do not necessarily call themselves anarchists.”  
> — Howard Zinn (2008)

### Predicates

\[
\begin{align*}
L(x) &\iff x \text{ self-identifies as an anarchist} \\
I^k_j(x) &\iff \text{interpreter } j \text{ reads } x \text{ as advocating } R^* \text{ with property } k
\end{align*}
\]

### Three Advocacy Types

- \(I^1\): maximize \(\rho_A\) (individualist)
- \(I^2\): force \(\rho_M = 0\) (acephalous)
- \(I^3_D\): force \(R \upharpoonright D = \varnothing\) (horizontal / sortal)

\(I^3_H\) is satisfied by configurations that maximally violate \(I^2\). The two targets are incompatible.

### Key Points

- \(I^k_j(x) \not\Rightarrow L(x)\). The label-free set is non-empty.
- The word “anarchist” is mid-19th century; all pre-1840 subjects have \(L(x) = \bot\) by construction.
- Titles (\(\mathrm{Ttl}\)) are a third, independent object. Abolishing honorifics does not delete edges of \(R\).
- Servant-inversion constrains conduct along an edge; it does not delete the edge.

No aggregation theorem connects the density of labels or interpretations to any structural ratio.

---

## III. Worked Example: Early Christian Source Texts

A single test case exercising every index. The formalism does not settle doctrinal questions; it isolates the precise point at which doctrine must be supplied.

### Structural Readings

- **Political domain:** \(\mathrm{An}(x) = \bot\)
- **Religious domain (unsorted):** \(\rho_M > 0\) (Matt 28:18, 19:28, 18:15–18)
- **Religious domain (sorted \(H/T\)):** \(\rho^H_A = 1\), \(\rho_M = 1/|S|\) (Matt 23:8–10)
- **Communal restriction:** horizontal claim inside \(C\) (Mark 10:42–45)

Two internal tensions are resolved only by distinguishing titles from edges and conduct-along-edges from edge deletion. Under that resolution the material is not \(I^2\).

### The Hinge

\(\rho^H_A = 1\) requires the relevant node to be placed in \(T\). If placed in \(H\), both ratios change immediately. The entire anarchism reading turns on this single sortal assignment — a doctrinal commitment the formalism cannot supply.

Readers who assign \(T\) and readers who assign \(H\) are both reasoning correctly from their respective premises.

### Methodological Note

A prior likelihood-ratio calculation claiming decisive support for an anarchist reading is rejected on standard grounds: dependence among passages, incomplete hypothesis space, selection on the conclusion, free magnitude parameters, bundling of separable claims, and equivocation between structural and ascriptive layers.

---

## Historical Note

Residual personal anarchy (\(\rho_A > 0\)) has coexisted at every scale. Horizontal anarchy over a declared subdomain is common. Athens 404 BCE supplies an early case of \(\rho_M = 0\) with \(\|R\| > 0\).

---

## Limitations

- The edge rule is stipulative and needs sharper operational criteria.
- The framework is static; no dynamics are supplied.
- Stability of \(\rho_M = 0\) under perturbation remains open.
- Empirical measurement protocols are not developed here.
- The framework is silent on normative evaluation.
- High formal density on this topic currently carries elevated reception risk in some environments. That is a social fact about reception, not an internal defect of the distinctions.

---

## Citation

Cite by commit hash when precision is required.

## License

No license currently declared. Scholarly quotation with attribution is permitted.