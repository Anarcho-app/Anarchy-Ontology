# Anarchy-Ontology

A relativized formal language that distinguishes **anarchy** (structural facts about a ruled-by relation \(R\)) from **anarchism** (ascriptive attitudes toward a target relation).

The framework forces explicit indices on every claim and maintains a strict separation between the two layers. No theorem is asserted that bridges structural facts about \(R\) to ascriptive facts about speakers or interpreters. It is offered as a clarifying instrument, not as a political program, a theological system, or a complete theory of power.

### Motivation, Scope, and Provisional Status

Most persistent disputes about anarchy and anarchism collapse two independent questions or suppress required indices. This document isolates those questions. Every structural claim must carry a relation-domain index and a node-subdomain index; unindexed claims are treated as ill-formed.

The framework is deliberately limited and provisional:

- It does not decide whether any historical figure “was an anarchist.”
- It does not rank regimes normatively.
- It does not claim that formal distinctions dissolve substantive political or theological disagreement; they only relocate the disagreement to an explicit premise (most often a sortal assignment).

Strongest external objection (acknowledged, not straw-manned): high-density formal treatment of anarchism, especially when paired with close analysis of early Christian source texts, currently attracts pathologizing dismissal in some reception environments regardless of internal rigor. The present text accepts that social fact as a constraint on presentation while refusing to dilute the formal content.

---

# Relativized Formalism for Anarchy and Anarchism

*(stipulated, not etymological: the earliest attested* anarchia *was systemic — Athens, 404 BCE)*

Two layers. **Structural**: facts about \(R\). **Ascriptive**: facts about what subjects call themselves and what interpreters read in them. No theorem crosses between them.

**\(-y\) vs. \(-ism\).** *Anarchy* (\(-ia\), a state) is structural: a fact about \(R\), indexed by domain. *Anarchism* (\(-ism\), a doctrine) is ascriptive: an attitude toward a target \(R^{\ast}\), indexed by interpreter. Neither entails the other in either direction. Most disputes in this area are a confusion of the two, or a suppressed index on one of them.

---

# I. Structural layer — anarchy

## Core

\[
\mathrm{An}_R(x)\;\iff\;\neg\exists y\,(y\neq x\land x\,R\,y)
\]

\(R\) = ruled-by relation, \(x\,R\,y\) = “\(x\) is ruled by \(y\)”; irreflexive; \(S\) finite.

\[
A_R=\{x\in S\mid\mathrm{An}_R(x)\},\qquad A_R=A_{R^{+}}
\]

The \(y\neq x\) clause: self-rule is not being ruled. *Auto-nomos* is compatible with \(\mathrm{An}_R\).

## Two predicates, one signature

\[
\text{an-archy}_1(x):=\mathrm{An}_R(x)\qquad\text{local, unary — a subject with no ruler}
\]

\[
\text{An-archy}_2(S,R):=(\rho_M=0)\qquad\text{systemic, shape-defined — rule exists, no ruler is un-ruled}
\]

## Apex vs. hermit

\[
\text{apex: }\mathrm{An}_R(x)\land\exists z\,(z\,R\,x)\qquad\text{hermit: }\mathrm{An}_R(x)\land\neg\exists z\,(z\,R\,x)
\]

\(A_R^{\mathrm{apex}}=\{x\in A_R\mid\exists z\,(z\,R\,x)\}\). Kings answerable to none versus the ungoverned isolate.

## Relativization

Every anarchy claim carries **two indices**: which relation, and over which subdomain. Unindexed claims are ill-formed.

**Relation domain.** \(R_d\) for \(d\in\{\text{legal},\text{economic},\text{religious},\dots\}\).

**Node subdomain.** For \(D\subseteq S\), the restriction \(R{\upharpoonright}D=R\cap(D\times D)\), and

\[
\mathrm{An}^{D}_{R}(x)\iff x\in D\land\neg\exists y\in D\,(y\neq x\land x\,R\,y)
\]

\[
A^{D}_{R}=\{x\in D\mid\mathrm{An}^{D}_R(x)\},\qquad
\rho^{D}_{A}=\frac{|A^{D}_{R}|}{|D|},\qquad
\rho^{D}_{M}=\frac{|A^{D,\mathrm{apex}}_{R}|}{|D|}
\]

\(D=S\) recovers the unrelativized case. Three subdomains matter in practice:

- **Sortal.** \(S=H\uplus T\), \(H\) = human subjects, \(T\) = non-human or transcendent nodes. \(\rho^{H}_{A}\) measures anarchy *among humans*.
- **Communal.** \(C\subseteq H\) an in-group. \(\rho^{C}_{A}\) measures anarchy *within a community*.
- **Full.** \(D=S\).

**Theorem (sortal divergence).** \(\rho^{H}_{A}\) and \(\rho_{M}\) are independent. In particular \(R{\upharpoonright}H=\varnothing\) with a unique \(t\in T\) ruling all of \(H\) gives

\[
\rho^{H}_{A}=1\quad\text{(universal anarchy among humans)}\qquad\text{while}\qquad \rho_{M}=\tfrac1{|S|}>0\quad\text{(a star: pure monarchy)}
\]

The same configuration is maximal anarchy under the sortal reading and pure monarchy under the unsorted one. Neither reading is an error; they are different indices. Every dispute over “theocratic anarchism” reduces to this divergence.

## Ratios

\[
\rho_A=\frac{|A_R|}{|S|},\quad
\rho_M=\frac{|A_R^{\mathrm{apex}}|}{|S|},\quad
\beta=\frac{|R|}{|S|},\quad
\rho_{\mathrm{rul}}=\frac{|\{y\mid\exists x,\;x\,R\,y\}|}{|S|},\quad
\sigma=\frac{|R|}{|\{y\mid\exists x,\;x\,R\,y\}|}
\]

\(\beta\) = mean rulers per subject; \(\rho_{\mathrm{rul}}\) = fraction who rule; \(\sigma\) = mean span.

**Identity.** \(\beta=\sigma\cdot\rho_{\mathrm{rul}}\). All ratios have relativized forms.

## Regimes (scale-relative)

- **Concentration**: \(\rho_A\) low, \(\sigma\) high.
- **Amplification**: edge-deletion enlarging \(A_R\).
- **Universal**: \(A_R=S\iff R=\varnothing\).
- **Residual**: \(A_R\neq\varnothing\) while \(R\neq\varnothing\).
- **Apexless**: \(\rho_M=0\) with \(|R|>0\) = \(\text{An-archy}_2\).
- **Tyranny**: \(|A_R^{\mathrm{apex}}|=1\), \(\rho_A\) minimal.
- **Horizontal**: \(R{\upharpoonright}D=\varnothing\) with \(R\neq\varnothing\) — no rule *within* \(D\), rule from outside retained.

## Lemmas

**Antitone.** \(R\subseteq R'\Rightarrow A_{R'}\subseteq A_R\).

**Amplification.** Deleting \((a,b)\) enlarges \(A_R\) iff \(b\) was \(a\)’s unique ruler.

**Universality.** \(A_R=S\iff R=\varnothing\), under irreflexivity.

**Restriction monotone.** \(D\subseteq D'\Rightarrow A^{D'}_R\cap D\subseteq A^{D}_R\). Shrinking the subdomain can only create anarchy, never destroy it.

## Apexlessness

\(\rho_M=0\) iff every ruler is ruled.

**Theorem (circularity).** If \(\rho_M=0\) and \(R\neq\varnothing\), then \(R\) contains a cycle, and every ruled vertex has an upward path into one.

*Proof.* Take \(a_0\,R\,a_1\). Then \(a_1\) is a ruler, so ruled by some \(a_2\); iterate. In a finite set the chain must repeat. \(\square\)

**Contrapositive.** Finite acyclic rule with \(R\neq\varnothing\) always has an apex. Apexless rule is circular rule.

**Corollary (horizontal vs. apexless).** Horizontal anarchy over \(D\) does not imply apexlessness. The two notions pull in opposite directions.

**Rival formalizations of “no apex” rejected.** Arbitrary thresholds on \(\rho_M\); absence of a dominating vertex; absence of a vertex reachable from all others. Each fails to capture the intended notion.

## Aggregation

**Theorem.** Let \(\Phi(S,R)\) be isomorphism-invariant and anarchy-grounded (a function of \(A_R\) as a bare subset). Then \(\Phi\) depends only on \(\rho_A\) and \(|S|\).

**Corollary.** Any Boolean claim “the system is anarchic” that is anarchy-grounded is merely a threshold on \(\rho_A\).

Systemic anarchy is not an aggregate of personal anarchy. \(\rho_M\), \(\rho^D_A\), acyclicity, and height remain well-defined independently.

## Instantiation (edge rule)

\(x\,R\,y\) holds when \(y\) can impose on \(x\) a directive that \(x\) cannot unilaterally refuse without sanction, and \(y\) is an identifiable person, office, or (under explicit sortal extension) transcendent node. Above household scale, nodes are offices. One \(R_d\) is fixed per analysis.

| Case | \(\lvert S\rvert\) | \(\lvert R\rvert\) | \(\rho_A\) | \(\rho_M\) | \(\beta\) | \(\sigma\) | \(\rho_{\mathrm{rul}}\) |
|:-----|:-----------------:|:-----------------:|:--------:|:--------:|:-------:|:-------:|:-----------------:|
| Household (2 parents, 2 children) | 4 | 4 | 0.50 | 0.50 | 1.00 | 2.00 | 0.50 |
| Monarchy (king, 2 nobles, 2 peasants) | 5 | 4 | 0.20 | 0.20 | 0.80 | 1.33 | 0.60 |
| Constitutional republic | 5 | 11 | 0.00 | 0.00 | 2.20 | 2.75 | 0.80 |
| Sortal star (\(t\in T\); 3 humans) | 4 | 3 | 0.25 | 0.25 | 0.75 | 3.00 | 0.25 |

The republic is \(\text{An-archy}_2\) (\(\rho_M=0\)) with \(\rho_A=0\). The sortal star is its opposite: \(\rho^{H}_{A}=1\) with \(\rho_M>0\).

---

# II. Ascriptive layer — anarchism

> “One of the problems with dealing with anarchism is that there are many people whose ideas are anarchist, but who do not necessarily call themselves anarchists.”  
> — Howard Zinn (2008)

## Predicates

\[
L(x)\iff x\text{ self-identifies as an anarchist}
\]

\[
I^{k}_{j}(x)\iff\text{interpreter }j\text{ reads }x\text{ as advocating a target }R^{\ast}\text{ with property }k
\]

\(L\) is near-checkable. \(I\) carries both an interpreter index and a property index. “Was \(x\) an anarchist?” is ill-formed until both are fixed.

## Advocacy types supplied by the structural layer

\[
I^{1}:\ \rho_A(R^{\ast})\uparrow \qquad\text{(individualist)}
\]

\[
I^{2}:\ \rho_M(R^{\ast})=0 \qquad\text{(acephalous)}
\]

\[
I^{3}_{D}:\ R^{\ast}{\upharpoonright}D=\varnothing \qquad\text{(horizontal / sortal)}
\]

\(I^{3}_{H}\) is satisfied by configurations that maximally violate \(I^{2}\). The two targets are incompatible; both can be held sincerely. This is the formal content of the long dispute over whether Christian anarchism counts as anarchism.

## Label and interpretation

\[
I^{k}_{j}(x)\;\not\Rightarrow\;L(x)
\]

The converse also fails. The term “anarchist” is mid-19th-century; every pre-1840 subject has \(L(x)=\bot\) by construction. Questions about earlier figures are therefore questions about \(I\) alone.

Titles (\(\mathrm{Ttl}\)) form a third, independent object. Abolishing honorifics does not delete edges of \(R\). Servant-inversion constrains conduct along an edge; it presupposes the edge and deletes nothing.

No aggregation theorem connects the density of \(L\) or \(I^{k}_{j}\) to any structural ratio.

---

# III. Worked example: early Christian source texts

A single test case that exercises every index. The formalism does not settle any doctrinal question; it isolates the exact point at which doctrine must be supplied.

### Structural readings

- Political domain: \(\mathrm{An}(x)=\bot\).
- Religious domain, unsorted: \(\rho_M>0\) (Matt 28:18; 19:28; 18:15–18).
- Religious domain, sorted \(H/T\): \(\rho^{H}_{A}=1\), \(\rho_M=1/|S|\) (Matt 23:8–10).
- Communal restriction: horizontal claim inside \(C\) (Mark 10:42–45).

Two internal tensions are resolved only by distinguishing titles from edges and conduct-along-edges from edge deletion. Under that resolution the corpus is not \(I^{2}\).

### The hinge

\(\rho^{H}_{A}=1\) requires the relevant node to be placed in \(T\). If it is placed in \(H\), both \(\rho^{H}_{A}\) and \(\rho^{H}_{M}\) change at once. The entire anarchism reading turns on that single sortal assignment — a doctrinal commitment the formalism cannot supply. Readers who assign \(T\) (Tolstoy, Ellul, and the Christian-anarchist tradition) and readers who assign \(H\) are both reasoning correctly from their respective premises.

### Ascriptive coordinates

- \(L=\bot\) (term postdates the material by centuries). Nothing follows from this in either direction.
- \(I^{3}_{H,j}\) varies with the interpreter.
- \(I^{2}_{j}\) is negative on the reading that retains the sanction procedures.

### Methodological note on a prior likelihood-ratio claim

A circulated calculation returning extremely high likelihood ratios in favor of an anarchist reading is rejected on ordinary grounds: dependence among pericopes, incomplete hypothesis space (apocalypticism and related options omitted), selection on the conclusion, free magnitude parameters, bundling of separable claims, and equivocation between structural and ascriptive layers. A defensible analysis clusters correlated passages, includes the major alternative hypotheses, and reports results as indexed \(I^{k}_{j}\) claims rather than as unindexed structural facts.

---

## Historical note

Residual personal anarchy (\(\rho_A>0\)) has coexisted at every scale; universal anarchy (\(\rho_A=1\)) has not. Horizontal anarchy over a declared subdomain is common. Athens 404 BCE supplies an early case of \(\rho_M=0\) with \(|R|>0\) and \(\rho_L=0\).

## Limitations (explicit)

- The edge rule remains stipulative and needs sharper operational criteria across domains.
- The framework is static; no dynamics are supplied.
- Stability of \(\rho_M=0\) under edge perturbation is open.
- Empirical measurement protocols for the ratios are not developed here.
- The framework is silent on normative evaluation.
- High formal density on this particular topic currently carries elevated reception risk in some environments; that is a social fact, not an internal defect of the distinctions.

## Citation

Cite by commit hash when precision is required.

## License

No license currently declared. Scholarly quotation with attribution is permitted.