# Anarchy in Hierarchy — Key Points & Formalisms
# Relativized Formalism for Anarchy and Anarchism
*(stipulated, not etymological: the earliest attested* anarchia *was systemic — Athens, 404 BCE)*

Two layers. **Structural**: facts about \(R\). **Ascriptive**: facts about what subjects call themselves and what interpreters read in them. No theorem crosses between them.

**\(-y\) vs. \(-ism\).** *Anarchy* (\(-ia\), a state) is structural: a fact about \(R\), indexed by domain. *Anarchism* (\(-ism\), a doctrine) is ascriptive: an attitude toward a target \(R^{*}\), indexed by interpreter. Neither entails the other in either direction. Most disputes in this area are a confusion of the two, or a suppressed index on one of them.

---

# I. Structural layer — anarchy

## Core
\[
\operatorname{An}_R(x)\;\iff\;\neg\exists y\,(y\neq x\land x\,R\,y)
\]
\(R\) = ruled-by relation, \(x\,R\,y\) = "\(x\) is ruled by \(y\)"; irreflexive; \(S\) finite.
\[
A_R=\{x\in S\mid\operatorname{An}_R(x)\},\qquad A_R=A_{R^{+}}
\]
The \(y\neq x\) clause: self-rule is not being ruled. *Auto-nomos* is compatible with \(\operatorname{An}_R\).

## Two predicates, one signature
\[
\text{an-archy}_1(x):=\operatorname{An}_R(x)\qquad\text{local, unary — a subject with no ruler}
\]
\[
\text{An-archy}_2(S,R):=(\rho_M=0)\qquad\text{systemic, shape-defined — rule exists, no ruler is un-ruled}
\]

## Apex vs. hermit
\[
\text{apex: }\operatorname{An}_R(x)\land\exists z\,(z\,R\,x)\qquad\text{hermit: }\operatorname{An}_R(x)\land\neg\exists z\,(z\,R\,x)
\]
\(A_R^{\mathrm{apex}}=\{x\in A_R\mid\exists z\,(z\,R\,x)\}\). Kings answerable to none vs. the ungoverned isolate.

## Relativization
Every anarchy claim carries **two indices**: which relation, and over which subdomain. Unindexed claims are ill-formed.

**Relation domain.** \(R_d\) for \(d\in\{\text{legal},\text{economic},\text{religious},\dots\}\).
**Node subdomain.** For \(D\subseteq S\), the restriction \(R{\upharpoonright}D=R\cap(D\times D)\), and
\[
\operatorname{An}^{D}_{R}(x)\iff x\in D\land\neg\exists y\in D\,(y\neq x\land x\,R\,y)
\]
\[
A^{D}_{R}=\{x\in D\mid\operatorname{An}^{D}_R(x)\},\qquad
\rho^{D}_{A}=\frac{|A^{D}_{R}|}{|D|},\qquad
\rho^{D}_{M}=\frac{|A^{D,\mathrm{apex}}_{R}|}{|D|}
\]
\(D=S\) recovers the unrelativized case. Three subdomains matter in practice:

- **Sortal.** \(S=H\uplus T\), \(H\) = human subjects, \(T\) = non-human or transcendent nodes. \(\rho^{H}_{A}\) measures anarchy *among humans*.
- **Communal.** \(C\subseteq H\) an in-group. \(\rho^{C}_{A}\) measures anarchy *within a community* — the "among you" scope.
- **Full.** \(D=S\).

**Theorem (sortal divergence).** \(\rho^{H}_{A}\) and \(\rho_{M}\) are independent. In particular \(R{\upharpoonright}H=\varnothing\) with a unique \(t\in T\) ruling all of \(H\) gives
\[
\rho^{H}_{A}=1\quad\text{(universal anarchy among humans)}\qquad\text{while}\qquad \rho_{M}=\tfrac1{|S|}>0\quad\text{(a star: pure monarchy)}
\]
The same configuration is **maximal anarchy** under the sortal reading and **pure monarchy** under the unsorted one. Neither reading is an error; they are different indices. Every dispute over "theocratic anarchism" is this divergence and nothing else.

## Ratios
\[
\rho_A=\frac{|A_R|}{|S|},\quad
\rho_M=\frac{|A_R^{\mathrm{apex}}|}{|S|},\quad
\beta=\frac{|R|}{|S|},\quad
\rho_{\mathrm{rul}}=\frac{|\{y\mid\exists x,\;x\,R\,y\}|}{|S|},\quad
\sigma=\frac{|R|}{|\{y\mid\exists x,\;x\,R\,y\}|}
\]
\(\beta\) = mean rulers per subject; \(\rho_{\mathrm{rul}}\) = fraction who rule; \(\sigma\) = mean span, the \(n\) in "1 : n".
**Identity.** \(\beta=\sigma\cdot\rho_{\mathrm{rul}}\). All ratios have relativized forms \(\beta^{D},\sigma^{D},\rho^{D}_{\mathrm{rul}}\).

## Regimes (scale-relative)
- **Concentration**: \(\rho_A\) low, \(\sigma\) high.
- **Amplification**: edge-deletion enlarging \(A_R\).
- **Universal**: \(A_R=S\iff R=\varnothing\).
- **Residual**: \(A_R\neq\varnothing\) while \(R\neq\varnothing\).
- **Apexless**: \(\rho_M=0\) with \(|R|>0\) = \(\text{An-archy}_2\).
- **Tyranny**: \(|A_R^{\mathrm{apex}}|=1\), \(\rho_A\) minimal.
- **Horizontal**: \(R{\upharpoonright}D=\varnothing\) with \(R\neq\varnothing\) — no rule *within* \(D\), rule from outside it retained. Sortal (\(D=H\)) or communal (\(D=C\)).

## Lemmas
**Antitone.** \(R\subseteq R'\Rightarrow A_{R'}\subseteq A_R\).
**Amplification.** Deleting \((a,b)\) enlarges \(A_R\) **iff** \(b\) was \(a\)'s unique ruler.
**Universality.** \(A_R=S\iff R=\varnothing\), under irreflexivity.
**Restriction monotone.** \(D\subseteq D'\Rightarrow A^{D'}_R\cap D\subseteq A^{D}_R\). Shrinking the subdomain can only create anarchy, never destroy it — which is why sortal restriction is the standard route to an anarchy claim.

## Apexlessness
\(\rho_M=0\) iff **every ruler is ruled**.

**Theorem (circularity).** If \(\rho_M=0\) and \(R\neq\varnothing\), then \(R\) contains a cycle, and every ruled vertex has an upward path into one.
*Proof.* Take \(a_0\,R\,a_1\). Then \(a_1\) is a ruler, so ruled by some \(a_2\); \(a_2\) is a ruler, so ruled by \(a_3\); iterate. The chain is infinite in a finite set, so it repeats. \(\square\)
**Contrapositive.** Finite acyclic rule with \(R\neq\varnothing\) always has an apex. Apexless rule is *circular* rule.

**Corollary (horizontal vs. apexless).** Horizontal anarchy over \(D\) does **not** imply apexlessness. \(R{\upharpoonright}D=\varnothing\) is compatible with a single external apex ruling all of \(D\) — indeed that is the acyclic, maximally centralized case. The two anarchies pull in opposite directions.

**Rival formalizations of "no apex", rejected.** \(\rho_M\le\tau\) (arbitrary threshold, self-defeating); *no dominating vertex* (too weak — any monarchy ruling through intermediaries passes); *no vertex reachable from all others* (too weak differently — two disjoint kingdoms pass, which is two apexes, not none).

## Aggregation
**Theorem.** Let \(\Phi(S,R)\) be isomorphism-invariant and *anarchy-grounded* — a function of \(A_R\) as a bare subset, not of \(R\)'s shape. Isomorphisms are the permutations preserving \(A_R\); two configurations are isomorphic iff they agree on \((|A_R|,|S\setminus A_R|)\). Hence every such \(\Phi\) is a function of \(\rho_A\) and \(|S|\).

**Corollary.** Any Boolean "the system is anarchic" that is anarchy-grounded is a threshold on \(\rho_A\) — arbitrary.

**Scope.** Systemic anarchy is not an *aggregate* of personal anarchy. It is not undefined: \(\rho_M\), \(\rho^D_A\), acyclicity, height are all well-defined. \(\text{An-archy}_2\) escapes the theorem because \(\rho_M\) reads which elements of \(A_R\) hold subjects.

## Instantiation
**Edge rule.** \(x\,R\,y\) iff \(y\) can impose on \(x\) a directive \(x\) cannot unilaterally refuse without sanction, and \(y\) is an identifiable person, office, or (under a declared sortal extension) transcendent node. Nodes are offices, not persons, above household scale. Fix one \(R_d\) per pass.

| Case | \(|S|\) | \(|R|\) | \(\rho_A\) | \(\rho_M\) | \(\beta\) | \(\sigma\) | \(\rho_{\mathrm{rul}}\) |
|---|---|---|---|---|---|---|---|
| Household (2 parents, 2 children) | 4 | 4 | 0.50 | 0.50 | 1.00 | 2.00 | 0.50 |
| Monarchy (king, 2 nobles, 2 peasants) | 5 | 4 | 0.20 | 0.20 | 0.80 | 1.33 | 0.60 |
| Constitutional republic (electorate, legislature, executive, court, bureau) | 5 | 11 | 0.00 | 0.00 | 2.20 | 2.75 | 0.80 |
| Sortal star (\(t\in T\); 3 humans, none ruling another) | 4 | 3 | 0.25 | 0.25 | 0.75 | 3.00 | 0.25 |

Republic edges: electorate ruled by legislature and court; legislature by electorate and court; executive by all three; court by executive and legislature; bureau by executive and legislature. \(A_R=\varnothing\).
Sortal star, restricted: \(\rho^{H}_{A}=1\), \(\rho^{H}_{M}=0\), \(R{\upharpoonright}H=\varnothing\). Unrestricted it is a star — the same shape as the monarchy row.

**Result.** The republic is \(\text{An-archy}_2\) (\(\rho_M=0\)) with zero \(\text{an-archy}_1\) (\(\rho_A=0\)) — apexless because circular. The sortal star is its exact opposite: \(\rho^{H}_{A}=1\) with \(\rho_M>0\) — universally anarchic among humans and perfectly monarchic overall. \(\rho_A\) alone separates none of the four.

---

# II. Ascriptive layer — anarchism

> "One of the problems with dealing with anarchism is that there are many people whose ideas are anarchist, but who do not necessarily call themselves anarchists."
> — Howard Zinn, *Rebels Against Tyranny*, interview by Ziga Vodovnik, CounterPunch, 12 May 2008

## Two predicates
\[
L(x)\iff x\text{ self-identifies as an anarchist}
\]
\[
I^{k}_{j}(x)\iff\text{interpreter }j\text{ reads }x\text{ as advocating a target }R^{*}\text{ with property }k
\]
\(L\) is self-ascribed and near-checkable. \(I\) requires an ascriber, so it carries the interpreter index \(j\) and the target-property index \(k\). Dropping either is the commonest error: "was \(x\) an anarchist?" is ill-formed until both are fixed.

## The advocacy types are not free — the structural layer supplies them
\[
I^{1}:\ \rho_A(R^{*})\uparrow\qquad
I^{2}:\ \rho_M(R^{*})=0\qquad
I^{3}_{D}:\ R^{*}{\upharpoonright}D=\varnothing
\]
- \(I^{1}\) **individualist** — maximize personal un-ruledness. Voluntarist and Stirnerite formulations.
- \(I^{2}\) **acephalous** — abolish the apex; accountability closes into cycles. Proudhon, Kropotkin, "abolition of the state", "rejection of coercive hierarchy".
- \(I^{3}_{D}\) **horizontal / sortal** — no rule *within* \(D\), rule from outside \(D\) permitted or required. Theocratic and hierocratic formulations take \(D=H\); communitarian and monastic ones take \(D=C\).

\(I^{3}\) is genuinely a third type, not a variant: by the horizontal/apexless corollary, \(I^{3}_{H}\) is *satisfied by* a configuration that maximally violates \(I^{2}\). An \(I^{3}\)-advocate and an \(I^{2}\)-advocate can both be sincere anarchists and want incompatible worlds. This is the formal content of the long dispute over whether Christian anarchism is anarchism; the answer is that it is \(I^{3}_{H}\) and not \(I^{2}\), and the disputants are each correct about the type they have in mind.

## Zinn's claim
\[
I^{k}_{j}(x)\;\not\Rightarrow\;L(x)
\]
The label-free set is non-empty. The converse fails independently:

| | \(L\) | \(\neg L\) |
|---|---|---|
| \(I\) | Proudhon, Kropotkin, Zinn | **Zinn's population**: Paine, Thoreau, the Transcendentalists |
| \(\neg I\) | self-described anarchists failing the criterion | most subjects |

\(L\) is time-bounded as \(I\) is not: the word dates from Proudhon in the mid-19th century, so \(L(x)=\bot\) for every pre-1840 subject **by construction**. "Was [pre-modern figure] an anarchist?" is therefore a question about \(I\) alone, and \(L\)-evidence is irrelevant to it in both directions.

## Label-free residual
\[
Z^{k}_{j}=\{x\in S\mid I^{k}_{j}(x)\land\neg L(x)\}
\]
**Not** \(\{x\in A_R\mid I\land\neg L\}\). Zinn's population is not inside \(A_R\): Thoreau was jailed, Paine prosecuted — both ruled. \(A_R\cap Z\) is a distinct, much smaller object.

## Non-aggregation, ascriptive
\[
\rho_L=\frac{|\{x\mid L(x)\}|}{|S|},\qquad \rho_{I^k}=\frac{|\{x\mid I^{k}_{j}(x)\}|}{|S|}
\]
\(\rho_{I^k}\) determines nothing about \(\rho_M\) or \(\rho^{D}_{A}\). A population wholly \(I^{2}\)-positive can sit under an unbroken apex; an apexless order can be held by a population with \(\rho_I=0\). This blocks *there are anarchists here* ⟹ *this is an anarchy*, for the same reason the structural theorem blocks *some are un-ruled* ⟹ *the system is anarchic*. Two independent failures of aggregation, one per layer, no bridge across.

## Titles are not edges
A third ascriptive object, distinct from both \(L\) and \(R\):
\[
\operatorname{Ttl}(x,\tau)\iff x\text{ bears honorific }\tau
\]
Abolishing \(\operatorname{Ttl}\) does not delete any edge of \(R\). A rule "let no one be *called* master" constrains the honorific relation; the ruled-by relation is untouched, and \(\rho_A,\rho_M,\rho^D_A\) are unchanged. Conversely an untitled office can hold every edge it held before.

**This is the single most common source of false anarchy readings.** Anti-honorific texts are read as anti-authority texts. Formally they operate on different objects, and a corpus can abolish titles while retaining sanctions with no inconsistency whatever.

Servant-inversion — "the greatest among you shall be your servant" — is a third thing again: it constrains *conduct along* an edge and reassigns the criterion for rank. It presupposes rank exists. It deletes nothing.

---

# III. Worked instantiation — the Jesus corpus

A test case exercising every index at once. The formalism does not settle any doctrinal question; it locates precisely where the doctrinal question sits.

## Structural reading, by domain

**\(R_{\text{political}}\).** \(\operatorname{An}(x)=\bot\). A Roman prefect could impose a non-refusable sanction and demonstrably did. "Political hermit" fails the edge rule.

**\(R_{\text{religious}}\), unsorted.** Matt 28:18 ("all authority is given unto me") is a maximal apex claim; Matt 19:28 assigns thrones; Matt 18:15-18 specifies a sanction procedure ending in expulsion, which is an edge with declared enforcement. \(\rho_M>0\), decisively. Not \(\text{An-archy}_2\).

**\(R_{\text{religious}}\), sorted.** Matt 23:8-10 supplies the sort partition explicitly: *father* is barred "upon the earth" because one Father is "in heaven". This is \(H/T\) in the text's own words. The claim is \(R{\upharpoonright}H=\varnothing\) with a unique \(t\in T\) — exactly the sortal star, \(\rho^{H}_{A}=1\), \(\rho_M=\tfrac1{|S|}\).

**\(R\upharpoonright C\).** "The rulers of the Gentiles exercise lordship… it shall not be so among you" (Mark 10:42-45) is scoped to \(C\), not \(H\): it *contrasts* an out-group where \(R\) holds with an in-group where it does not. This is \(I^{3}_{C}\), a communal claim, not a universal political one — and it is consistent with "my kingdom is not of this world" rather than in tension with it.

## Two internal tensions the formalism exposes

1. **Matt 23:2-3 vs. Matt 23:8-10**, same discourse. "The scribes and Pharisees sit in Moses' seat; whatsoever they bid you observe, that observe and do" *retains* a human-to-human edge with directive force. Ten verses later, human titles are barred. Both hold only if 23:8-10 operates on \(\operatorname{Ttl}\) and not on \(R\) — titles abolished, edges retained.
2. **Mark 10:42-45 vs. Matt 18:15-18.** Lordship is barred within \(C\); a binding expulsion procedure is specified within \(C\). Both hold only if 10:42-45 constrains conduct along edges rather than their existence — servant-inversion, not deletion.

Under the reading that resolves both, the corpus is **not** \(I^{2}\): it is anti-honorific and anti-domineering while retaining sanction. That is a coherent and well-attested position, and it is not apexlessness.

## The crux is one node's sort

\(\rho^{H}_{A}=1\) requires \(t\in T\). If the referent of "one is your Master" is assigned to \(H\), then \(R{\upharpoonright}H\neq\varnothing\), \(\rho^{H}_{A}\) falls from \(1\) to \(1/|H|\), and \(\rho^{H}_{M}\) rises from \(0\) to \(1/|H|\) — a human apex.

> **The entire anarchism reading turns on the sort assignment of a single node, and that assignment is a doctrinal commitment the formalism cannot supply.**

This is the honest terminus. Tolstoy and Ellul assign \(T\) and read \(I^{3}_{H}\); readers who assign \(H\) read a monarchy. Both are reasoning correctly from their premise. John 10:34 ("ye are gods") is notable here as the one text that would *dissolve* the partition rather than shift one node across it — with the caveat that its source, Psalm 82, addresses unjust judges under condemnation, and its Johannine function is christological.

## Ascriptive reading
- \(L=\bot\), trivially: the term postdates the subject by eighteen centuries. **Nothing follows from this**, in either direction.
- \(I^{3}_{H,j}\) varies with \(j\): positive for Tolstoy, Ellul, and the Christian-anarchist tradition; negative for readers assigning the Master-node to \(H\), and for readers who take Matt 23:8-10 as a \(\operatorname{Ttl}\)-constraint.
- \(I^{2}_{j}\): negative on the resolving reading above, for any \(j\) who counts Matt 28:18 and Matt 18:15-18.

Three coordinates, three different answers, no contradiction.

## On the Bayesian calculation

The likelihood-ratio computation returning \(677{,}376:1\), and its extension to \(\approx3.7\times10^{12}:1\), is not a structural result. It is \(I_{j}\) for one \(j\), with the index suppressed and a decimal expansion attached. Six defects, in order of severity:

**1. Independence fails.** Multiplying LRs requires conditional independence given the hypothesis. Matt 23:8-10 and 23:11-12 are adjacent verses in one discourse; Matt 23:11 and Mark 10:42-45 are one tradition in two recensions; Luke 17:21 and John 18:36 are one theme. These are not eight witnesses but roughly six clusters counted eight times. Taking the maximum LR per cluster instead of the product:
\[
8\times8\times6\times9\times5\times0.8=13{,}824\quad\text{not}\quad677{,}376
\]
a factor of 49 lost to double-counting alone.

**2. The hypothesis space omits the majority scholarly position.** Odds-form updating requires \(P(H_a)+P(H_0)=1\). The live options include apocalyptic eschatology (Schweitzer, Ehrman), theocratic messianism, Jewish reform, and quietism. "My kingdom is not of this world" is at least as well explained by apocalypticism as by anarchism — it is evidence against *Zealot revolt*, which is not evidence for anarchism. With the true hypothesis outside the partition, the posterior is uninterpretable.

**3. The sample is selected on the conclusion.** Updating on a filtered corpus is invalid without modeling the filter. The "adding all his words leaves it unchanged, most are LR≈1" step is where this bites: the omitted counter-evidence is not neutral. Matt 23:2-3, Matt 19:28, Matt 18:15-18, Matt 28:18 all carry LR \(<1\) and none appears. Assigning them by the same free-hand method used for the originals — say \(0.2,\,0.25,\,0.3,\,0.2\) — gives \(13{,}824\times0.003\approx41:1\). The result has moved four orders of magnitude on choices no less defensible than the originals.

**4. The LRs are outputs, not inputs.** The "Why this LR?" column justifies a *direction*; the magnitudes (6, 8, 7, 9) are free parameters fixed after the conclusion. Nothing constrains 9 rather than 2. The magnitudes are the result.

**5. \(H_a\) bundles separable claims.** As defined it mixes \(I^{1}\), \(I^{2}\), \(I^{3}\), non-violence, and interiority. Evidence for non-resistance is not evidence for apexlessness: a pacifist theocracy satisfies the first and violates the second. Matt 5:38-44 (LR 9, the single heaviest weight) bears on non-violence and is close to silent on \(\rho_M\).

**6. The conclusion equivocates \(-y\) and \(-ism\).** "Jesus' ideology was anarchism" is an \(I\)-claim; the verses cited about the kingdom's nature are read as \(-y\)-claims about \(R\). The argument slides between them.

**What survives.** A defensible version puts apocalypticism in the hypothesis space, clusters correlated pericopes, selects passages adversarially, runs sensitivity analysis, states \(\kappa\) as one of \(I^{1}/I^{2}/I^{3}_{D}\), and reports the output as \(I^{k}_{j}\) — an interpreter's reading with its indices visible. It will not return a number with eleven significant figures, and the honest finding is that the corpus supports \(I^{3}_{D}\) far better than \(I^{2}\), conditional on a sort assignment it cannot itself justify.

---

## Historical continuity
Family → tribe → chiefdom → state → religion changes only \(|S|\), the shape of \(R\), and which sorts are admitted to \(S\).
Residual personal anarchy (\(\rho_A>0\)) has coexisted at every scale; the universal state (\(\rho_A=1\)) has not. Horizontal anarchy (\(\rho^{D}_{A}=1\) for some declared \(D\)) is common and cheap — it is what every hierarchy grants its own top tier.
Athens 404 BCE — governance without archon — is \(\rho_M=0\) with \(|R|>0\): \(\text{An-archy}_2\). Note \(\rho_L=0\) there, twenty-three centuries before the word existed.

## The pendulum
> "Politics is a pendulum whose swings between anarchy and tyranny are fueled by perennially rejuvenated illusions."

Well-formed reading: a trajectory \((\rho_A(t),\rho_M(t))\) between \(\rho_M=0\) and \(|A^{\mathrm{apex}}_R|=1\). Both poles are shape-facts. The illusion, where there is one, is the expectation that either pole is stable — by the circularity theorem the apexless pole holds only while the cycles hold, and breaking one edge produces an apex immediately.

*Widely attributed, but only through quotation collections, wording unstable ("perennially" / "perpetually"), no primary source located. Used unattributed, as illustration only. Contrast the Zinn line, which has an interview of record.*

## Closure
**Structural signature:** \(R_d\); the local predicate \(\operatorname{An}\); the set-former \(A\); restriction \({\upharpoonright}D\); cardinal counting terms; edge add/delete. Every claim indexed by \((d,D)\).
**Ascriptive signature:** the unary predicates \(L\), \(I^{k}_{j}\), \(\operatorname{Ttl}\), their extensions and ratios. These attach to subjects, never to edges.

\(\text{an-archy}_1\) is exhausted by \(\operatorname{An}_R,A_R,\rho_A\) and edge operations; \(\text{An-archy}_2\) by \(\rho_M\); horizontal anarchy by \(\rho^{D}_{A}\). Nothing aggregates the first into the second, horizontal anarchy implies neither, and nothing bridges the ascriptive layer to any of them.