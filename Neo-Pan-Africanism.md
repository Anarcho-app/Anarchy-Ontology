# Neo-Pan-Africanism — The Human Diaspora

### *Str8 Out of Africa: The One Diaspora Thesis*

**An evidence-grounded framework for human unity**
`v3.0` · supersedes the ten-theorem draft (v1, Grok 4.5) · repo: `anarcho-app/TAST`
Text: CC BY-SA 4.0 · Code: MIT

---

## TL;DR

Ten findings from population genetics, paleoanthropology, and the study of
human cooperation. Every one is published, cited, and falsifiable. Together
they establish something stronger than what the v1 draft was reaching for:

> Non-African populations are not a separate branch of humanity — they are a
> **subset** of African variation, and the *deepest* divisions among living
> humans run **inside** Africa, not between Africa and the rest of the world.
> There is no line anywhere in the data that separates a homeland from a
> diaspora.
>
> **There is one diaspora. Everyone is in it. Nobody is outside.**

The barriers are real. The boundary they claim to trace is not.

**One rule, stated up front:** §1 is evidence. §4 is a moral commitment. The
document never derives the second from the first, and §4 explains at length
why that firewall is what makes the position *durable* rather than fragile.

---

## Contents

- [§1 — The evidence: ten findings](#1--the-evidence-ten-findings)
- [§2 — What they compose into](#2--what-they-compose-into)
- [§3 — δ: a computable unity statistic](#3--δ-a-computable-unity-statistic)
- [§4 — The is/ought firewall](#4--the-isought-firewall)
- [§5 — Audit of v1](#5--audit-of-v1)
- [§6 — Objections we take seriously](#6--objections-we-take-seriously)
- [§7 — Falsifiable predictions](#7--falsifiable-predictions)
- [§8 — Reproduction protocol](#8--reproduction-protocol)
- [§9 — References](#9--references)
- [§10 — Acknowledgements](#10--acknowledgements)

---

# §1 — The evidence: ten findings

Each finding is stated, sourced, quantified where possible, and paired with a
note on **what it does not establish**. That second part is not hedging; it is
what separates this document from the thing it is correcting.

---

## F1 · One origin — pan-African, structured, and reticulated

*Homo sapiens* originated in Africa. The fossil record now places
anatomically modern or near-modern remains at **Jebel Irhoud, Morocco (~315
kya)** (Hublin et al. 2017) and **Omo Kibish, Ethiopia (≥230 kya)** (Vidal et
al. 2022) — sites 6,000 km apart, which is itself the finding.

The single-cradle picture has been replaced by a **structured metapopulation**
model: our species emerged from a set of interconnected populations spread
across the continent, exchanging migrants over hundreds of thousands of years
(Scerri et al. 2018).

Ragsdale et al. (2023), using linkage-disequilibrium and diversity statistics
on populations across Africa including 44 newly sequenced Nama (Khoe-San)
genomes, infer a **reticulated** history best described as a *weakly
structured stem*: two or more weakly differentiated ancestral populations
linked by continuous gene flow, with present-day structure traceable to Marine
Isotope Stage 5 and the earliest divergence among contemporary populations at
**120–135 kya**. Notably, this model accounts for polymorphism patterns that
had previously been attributed to introgression from a separate archaic
"ghost" species — without needing the ghost.

**Does not establish:** that any living population is ancestral, original, or
"closer to the root." Every living population has had exactly the same amount
of evolutionary time. See F5 and §6.4.

---

## F2 · The serial founder law — a quantitative gradient, not a border

This is the most legible quantitative result in the whole framework, and it is
the one to lead with.

Ramachandran et al. (2005) measured expected heterozygosity across 53 HGDP-CEPH
populations at 783 microsatellite loci and regressed it on geographic distance
from Addis Ababa (9°N, 38°E), correcting routes for large bodies of water:

$$H = 0.7682 - (6.52 \times 10^{-6}) \cdot d_{\text{km}}, \qquad R^2 = 0.763$$

Genetic diversity falls **linearly** with walking distance from East Africa,
with a correlation near −0.89. No candidate origin outside Africa fits the
global pattern of heterozygosity as well. Two companion gradients run the same
way: linkage disequilibrium **rises** linearly with distance from Africa, and
the ancestral allele-frequency spectrum flattens (DeGiorgio, Jakobsson &
Rosenberg 2009). Prugnolle, Manica & Balloux (2005) reported the same
relationship independently. Henn, Cavalli-Sforza & Feldman (2012) reviewed the
convergent support from parasite genetics, morphology, and linguistics.

**Why this matters more than any cluster statistic.** A single continuous
equation with $R^2 = 0.76$ predicts human genetic diversity worldwide from one
variable: *how far your ancestors walked*. That is the signature of a
**gradient**, not a taxonomy. Populations do not fall into bins along this
line; they fall **on** it.

**Does not establish:** any ranking. Lower heterozygosity is a record of
bottlenecks survived, not a deficiency — indeed the same gradient predicts
higher mutational load with distance from Africa (Henn et al. 2016), which is
a cost of the journey, not a merit of the origin.

---

## F3 · Nesting — non-African variation is a subset, with three known leaks

The serial founder process removes variants without adding many. Most common
non-African variation is therefore recoverable within African variation, and
African populations carry a large excess of private alleles. Schlebusch et al.
(2020) found roughly a quarter of variants in their Khoe-San panel occurring
nowhere else.

Stated properly — v1's set-inclusion notation between covariance matrices is
undefined; this is about the support of the allele-frequency spectrum:

$$\operatorname{supp}\!\left(\text{AFS}_{\text{non-Afr}}\right) \ \subseteq_\epsilon\ \operatorname{supp}\!\left(\text{AFS}_{\text{Afr}}\right)$$

**Three documented leaks that make containment approximate rather than strict:**

1. **Archaic introgression.** Non-Africans carry roughly **1.5–2.1%** Neanderthal
   ancestry (Reich 2018); Oceanian and some East Asian populations additionally
   carry Denisovan ancestry.
2. **Back-migration.** Chen et al. (2020), using the reference-free IBDmix
   method on 2,504 genomes, recovered on average **~17 Mb** of Neanderthal
   sequence per African individual — on the order of **0.3–0.5%** — largely
   attributable to Eurasian back-migration. Their conclusion: remnants of
   Neanderthal genomes survive in **every** modern human population studied.
3. **Post-OOA novelty.** ~50–70 kyr of mutation and drift outside Africa
   produced variants with no African counterpart.

**The direction of travel matters.** Even humanity's archaic inheritance —
long used as a supposed dividing line — turns out to be **shared**.

---

## F4 · Apportionment — most variation is within populations, not between

Lewontin (1972) found that the large majority of human genetic variance sits
*within* populations. Barbujani et al. (1997) and Rosenberg et al. (2002)
confirmed and refined it with far more markers; global $F_{ST}$ among human
populations runs roughly **0.10–0.15**. The AABA (2019) statement puts the
shared fraction at about **99.9%** of DNA, and states that no group of people
is, or has been, biologically homogeneous.

**We include the counter-argument rather than hiding it.** Edwards (2003)
correctly showed that low *per-locus* apportionment is compatible with high
*multi-locus* classification accuracy, because correlations across many loci
accumulate. Both results are true. What neither shows is that the resulting
classes are discrete, natural, or normatively relevant. Predictability is not
kindhood — postal codes are also highly predictable from genomes.

---

## F5 · Africa is not a genetic cluster — and this is the crux

**v1's third theorem claimed the opposite and it does not hold.**

v1 asserted $F_{ST}(\text{Africa},\text{non-Africa}) \ge \sup_{i,j\in\text{Africa}} F_{ST}(i,j)$,
and used it to license "African" as a primary biological cluster. Two
independent failures:

**(a) Pooling artifact.** $F_{ST}$ falls as within-group diversity rises.
Collapsing every African population into one group maximizes the within-group
term and **deflates the left-hand side by construction**.

**(b) The empirical fact.** The deepest population divergences among living
humans are **inside Africa**. The Khoe-San lineage is the earliest-diverging
branch among contemporary populations, carrying the most divergent lineages of
any living people and the greatest measured diversity anywhere (Schlebusch et
al. 2020).
Depending on model, that divergence is placed at 120–135 kya (Ragsdale et al.
2023) or 350–260 kya (Schlebusch et al. 2017); either way it is **older than
any Africa/non-Africa split**. Rain-forest forager divergence has been placed
as deep as ~150 kya.

So the supremum on the right-hand side is taken over some of the largest
differentiation values in the entire human dataset. The corrected relation:

$$\sup_{i,j \in \text{Africa}} F_{ST}(i,j) \ \gtrsim\ F_{ST}(\text{Africa}, \text{non-Africa})$$

**Consequence.** "African" is not a genetic cluster. It is a **geographic
label spanning humanity's deepest branches**. Any argument treating Africa as
a *unit* comparable to other continental *units* has already misdescribed the
data.

And the result is symmetric — which is the point. The same finding forbids
treating "European," "Asian," or any continental label as a natural kind.
This is the formal position of the field: the AABA (2019) statement holds that
humans are not divided biologically into distinct continental types or racial
genetic clusters, and that the Western race concept emerged from and in
support of colonialism rather than from biology. The **Jena Declaration**
(German Zoological Society, 2019) reached the same conclusion independently.

**Neither Africa nor anywhere else is a natural kind. That is the finding.**

---

## F6 · Humans are unusually homogeneous — for a great ape

A comparative result that puts human variation on a scale.

Prado-Martinez et al. (2013) sequenced 79 great ape genomes and found that
this sample yielded **more than double** the SNPs obtained from sequencing over
a thousand diverse humans. Genome-wide heterozygosity spans roughly a
threefold range across great apes: non-African humans sit near the **bottom**
(~0.8 × 10⁻³ heterozygotes/bp), alongside bonobos, western chimpanzees, and
eastern lowland gorillas, while central chimpanzees, western lowland gorillas
and both orangutan species reach **1.6–2.4 × 10⁻³**.

**Read that against F4.** Humanity spans every habitable landmass on Earth and
numbers in the billions, yet carries less genetic diversity than a single
chimpanzee subspecies occupying a fraction of one continent. Genetic distances
between humans on different continents can be smaller than between chimpanzees
living a few hundred kilometres apart.

We are a young, thin, recently exploded twig of a species. The apparatus of
racial difference was built on a variance that is, comparatively, barely
there.

---

## F7 · Universal reticulation — no population has ever been isolated

Ancient DNA has demolished the idea of pure or long-isolated populations
everywhere it has been applied. Every region investigated at genomic
resolution shows large-scale admixture events: every present-day population is
a recent mixture of earlier mixtures (Reich 2018; Lazaridis et al.; Patterson
et al.). Ragsdale et al. (2023) find the same reticulation *within* Africa
across the deep past.

The human "tree" is not a tree. It is an **admixture graph** — formally, an
ancestral recombination graph — with gene flow along most edges. Bifurcating
trees are a convenience of drawing software, and v1's ninth theorem inherited
their metaphor without their caveats: the TMRCA of a *locus* is not the split
time of a *population*, and different loci give wildly different answers by
design.

**Corollary:** every claim of the form "population X descends purely from Y"
has failed empirically wherever it has been tested at genome scale.

---

## F8 · Recent genealogical convergence — the pedigree result

Universal common descent does not need a clustering algorithm. It follows from
counting ancestors.

- **Chang (1999):** in a diploid population of size $n$, trace back about
  $1.77\log_2 n$ generations and, with high probability, every individual then
  alive is either an ancestor of **everyone** now living or of **no one**.
- **Rohde, Olson & Chang (2004):** the result survives realistic geography,
  substructure, and assortative mating. Their models place the genealogical
  most recent common ancestor of all living humans on the order of
  **~3,000 years ago**.
- **Rohde (2005):** the **identical-ancestors point** — beyond which everyone
  then alive is an ancestor of every living human, or of none — falls roughly
  **5,000–15,000 years ago**.

**Two necessary caveats.** These are *model* results, sensitive to migration
assumptions and to the treatment of historically isolated populations. And
**genealogical ancestry is not genetic ancestry**: beyond roughly a dozen
generations most pedigree ancestors contribute no DNA at all (Matsen & Evans
2008). The claim is about the family tree, not the genome.

Which is arguably more radical. On any reasonable model, the human pedigree is
not merely rooted in Africa — it is **braided across the entire species within
recorded history**. The Bronze Age is inside everyone's family.

---

## F9 · The trait race was built on cuts across ancestry

If race were tracking biology, skin pigmentation — the trait the category was
constructed around — should be its cleanest marker. It is close to its worst.

Crawford et al. (2017), analyzing ethnically diverse African genomes,
identified variants at **SLC24A5, MFSD12, DDB1/TMEM138, OCA2 and HERC2**
associated with pigmentation, and found:

- The **light**-pigmentation variant at SLC24A5 — long treated as a European
  marker — entered East Africa by gene flow **from non-Africans** over 5 kya
  and rose to high frequency there.
- At the other loci, variants associated with **dark** pigmentation in
  Africans are **identical by descent** with those in South Asian and
  Australo-Melanesian populations.
- Many of these variants are **ancient**, predating the origin of modern
  humans, and have been segregating within Africa for a very long time.

Pigmentation is a polygenic, clinal, latitude-tracking trait whose alleles are
old, shared, and flowing in every direction. The visible marker used for five
centuries to sort humanity into ranked kinds turns out to be one of the
**worst** available proxies for ancestry.

---

## F10 · Cooperation scales with institutions, not kinship

v1's tenth theorem argued that elevated intra-African relatedness $r$ makes
pan-African cooperation the evolutionarily stable strategy. **This is the one
proposition we discard outright**, on three technical grounds and one
structural one.

**Wrong denominator.** Hamilton's rule $rb > c$ requires relatedness measured
**against the local population from which competitors are drawn** — not
against a species-wide baseline (Grafen 1985). Computing $r$ globally and
calling the residual "elevated kinship" is the **ethnic-nepotism fallacy**,
long since refuted. Against the correct denominator, co-ethnic and
co-resident relatedness differences are negligible.

**Viscosity cancels the benefit.** Where limited dispersal *does* raise
relatedness, it equally intensifies **competition among kin**, which cancels
much or all of the inclusive-fitness gain (Taylor 1992; Queller 1994; West,
Pen & Griffin 2002).

**Wrong mechanism empirically.** Large-scale human cooperation among non-kin
runs on reciprocity, reputation, norm psychology, costly punishment, and
institutional design (Boyd & Richerson 2005; Henrich 2015; Ostrom 1990). These
mechanisms operate **over strangers**. They are the reason cooperation scales
past the band at all.

**And the form is the hazard.** *"Group X is more related to itself, therefore
solidarity within X is the natural equilibrium"* is the load-bearing argument
of every ethnonationalism on record. It does not become safe by choosing a
sympathetic X. See §4.

**Replacement.** In an $n$-player public-goods game with monitoring
probability $m$, punishment efficacy $\rho$, punishment cost $\kappa$, exit
value $e$, and norm internalization $\nu$, cooperation is stable when

$$m\,\rho\,\Phi(\nu) \ > \ \kappa + e$$

Every parameter is **institutional**. None is a function of ancestry. Ostrom's
eight design principles for durable self-governance — clear boundaries,
locally fitted rules, collective-choice arrangements, monitoring by
participants themselves, graduated sanctions, cheap conflict resolution,
recognized rights to organize, nested enterprises — contain **no ancestry term
at all**.

**Therefore:** the reachable scale of human solidarity is **not bounded by any
ancestry partition**. It is set by institutional design — which means it is a
thing people build, not a thing they inherit. This is the barrier-breaking
result, and unlike v1's version it is actually true.

---

# §2 — What they compose into

**D1 · Universal African descent.** *(F1, F2, F3)*
Every living human descends overwhelmingly from populations that were in
Africa. The archaic exceptions run to a few percent and — per F3 — are
themselves shared across all populations studied.

**D2 · The gradient is continuous.** *(F2, F5)*
Diversity falls as a smooth linear function of distance walked. There is no
step, no threshold, no boundary. Populations sit **on** the line, not in bins
beside it.

**D3 · No joint to carve at.** *(F4, F5, F6, F9)*
No continental partition of humanity is supported as a natural kind. The
deepest divisions are internal to Africa; total human variance is small even
by great-ape standards; and the trait race was built on cuts straight across
ancestry. **The "Africa / rest of world" boundary v1 required does not
exist.**

**D4 · Therefore the diaspora has no complement.** *(D1 + D2 + D3)*
If everyone descends from African populations, if the variation is a
continuous gradient rather than a set of bins, and if no boundary separates a
homeland population from a diaspora population — then **the set of people
outside the human diaspora is empty**.

**D5 · The commitment.** *(held on moral grounds — see §4)*
Neo-Pan-Africanism, in this formulation, is the commitment to dismantle the
barriers — borders, castes, racial hierarchies, enclosures — that partition a
species which is not, in fact, partitioned.

### Why the corrected version is stronger than v1

v1 went looking for a **center**: a maximal-variance subspace, a basal
ancestry component, a canonical root, a privileged demographic reservoir.
Every one of those searches fails on the evidence, because **there is no
center to find**.

v3 makes that failure the thesis. **The absence of a center is the unity
claim.** A framework with a center has an inside and an outside, and the
outside is where every hierarchy in history has been built. A framework with
no center has no outside.

*Str8 out of Africa* — all of us, without exception, and with nowhere else to
have come from.

---

# §3 — δ: a computable unity statistic

A single number that operationalizes D1 and D4. Proposed here for
implementation in this repo.

**Definition.** For individual $i$, let $\mathcal{A}_i(x)$ be the ancestral
lineages at genomic position $x$ traced back through the ancestral
recombination graph to time $T$. Define the **diaspora fraction**:

$$\delta_T(i)\ =\ \frac{1}{|\mathcal{G}|}\int_{\mathcal{G}} \Pr\big[\mathcal{A}_i(x)\ \text{in Africa at time } T\big]\ dx$$

integrating over the genome in recombination-map units.

**Prediction.** At $T \approx 100$ kya, $\delta_T(i) \in [0.95,\,1.00]$ for
**every living human**, with the shortfall almost entirely archaic
introgression (F3).

**Why δ is the right statistic — three properties $F_{ST}$, PCA loadings and
ADMIXTURE $q$-vectors all lack:**

1. **Defined per individual.** No population labels, no $K$, no continental
   partition. It cannot be used to build clusters because it does not contain
   any.
2. **Near-invariant across humans.** A statistic whose species-wide variance is
   ~2% cannot support a hierarchy. That is by design, and it is the
   quantitative form of D4.
3. **Falsifiable.** Substantial systematic variation in δ across populations
   would falsify D1 as stated.

**Feasible today.** Wohns et al. (2022) built a unified genealogy of thousands
of modern and ancient genomes and performed spatiotemporal inference on
ancestral lineages, recovering the expected concentration of deep ancestry in
Africa. Toolchain: `tsinfer`, `tsdate`, `Relate`, `msprime`, `ADMIXTOOLS2`,
`IBDmix`.

---

# §4 — The is/ought firewall

**This section is not a disclaimer. It is load-bearing structure, and it is
the single largest upgrade over v1.**

Every v1 proposition had the same shape:

```
[genetic fact]  ⟹  [therefore this ideology is correct]
```

That inference is invalid — when you like the conclusion and when you loathe
it. No arrangement of allele frequencies entails an obligation. Three reasons
this is practical rather than pedantic:

**4.1 · The mirror problem.** *"Genetics establishes group X's centrality,
therefore X's claims have priority"* is **form-invariant under substitution of
X**. Every apparatus of scientific racism has exactly this shape. Accept the
form when X = Africa and you have conceded the form to everyone else — and
you will then be arguing about data instead of about principle, on a field
your opponent chose. **Reject the form.**

**4.2 · The hostage problem.** If human equality rests on "we are genetically
similar," equality becomes a hostage to the next dataset. It must not be
possible for a sequencing run to revoke anyone's standing. Note that F4
already contains the failure mode: Edwards's multi-locus classification result
is precisely the kind of finding that a similarity-grounded ethics cannot
absorb. A commitment-grounded ethics absorbs it without flinching.

**4.3 · Genetics is a solvent, not a foundation.** What §1 does for this
project is **negative, and that is enough**: it dissolves the claim that
discrete, ranked, natural human kinds exist. It does not erect a new hierarchy
with someone else on top. The correct output of the science is *there is no
such structure* — never *the structure exists and Africa wins it*.

### The firewall, stated

> All empirical claims in §1–§3 are facts about the world, **revisable by
> evidence**.
>
> The normative commitment in D5 — that borders, castes, and racial
> hierarchies are illegitimate constraints on human beings — is a **moral
> commitment, held on moral grounds**. It is not derived from and not
> contingent on any result above.
>
> §1 removes a bad argument that has been made *against* that commitment for
> two hundred years. It does not make the argument *for* it. That argument is
> made on the ground of what people are owed, and it would stand if every
> number in §1 came back different.

---

# §5 — Audit of v1

| # | v1 theorem | Verdict | Problem | Repaired at |
|---|---|---|---|---|
| 1 | Maximal genetic diversity | ✅ Supported | Estimator sloppy; normative leap in final clause | F2, F3 |
| 2 | Nested hierarchy $\Sigma_A \supset \Sigma_{nA}$ | 🟡 Approximate | Strict inclusion false — archaic introgression, back-migration | F3 |
| 3 | Continental $F_{ST}$ separation | ❌ **False as stated** | Inequality runs the wrong way; deepest splits are intra-African | **F5** |
| 4 | PCA span optimality | ⚠️ Category error | Axes are artifacts of sampling; PCA has no canonical origin | F5 |
| 5 | ADMIXTURE basal component | ⚠️ Category error | $K$-components are not ancestral populations | F8 |
| 6 | Graph cohesion via $\lambda_2$ | 🟡 Wrong objective | Maximizes a subgraph, not the global graph | below |
| 7 | $N_e$ ratio ⟹ demographic primacy | ✅ fact / ❌ norm | "Optimal" has no defined objective function | §4 |
| 8 | Information-theoretic unity | ⚠️ Ill-posed | Objective and feasible set both undefined | F4 |
| 9 | Phylogenetic tree depth | 🟡 Wrong metaphor | History is a reticulate graph, not a tree | F7 |
| 10 | ESS from elevated intra-African $r$ | 🛑 **Rejected** | Ethnic-nepotism fallacy; wrong Hamilton denominator | **F10** |

**Two repairs worth spelling out:**

**On v1 #4 and #5 (PCA and ADMIXTURE).** Novembre & Stephens (2008) showed
that smooth clinal variation generates sinusoidal principal components that
*look* like discrete structure but are artifacts of the method; McVean (2009)
gave the coalescent interpretation. PCA also has no canonical origin —
eigenvectors are defined up to sign, and the origin is set entirely by the
centering choice, so a "reference frame for identity" is a decision, not a
theorem. Separately, Lawson, van Dorp & Falush (2018) demonstrated that
radically different histories produce **indistinguishable** ADMIXTURE bar
plots, and released `badMIXTURE` as a goodness-of-fit check. The
over-interpretation pipeline they warn against is exactly v1's: estimate $K$,
assume it is true, assume each component was a real past population, assume
individuals are mixtures of them. There is no guaranteed basal component with
a positive lower bound; add African samples and it fissions.

**On v1 #6 (graph connectivity).** The mathematics is fine — the Laplacian is
a sum of PSD edge Laplacians, so raising edge weights gives $L' \succeq L$ and
hence $\lambda_2(L') \ge \lambda_2(L)$. The **target** is wrong. If the goal
is breaking barriers, the graph is $G_{\text{humanity}}$, and by Cheeger's
inequality $h(G)^2/2 \le \lambda_2 \le 2h(G)$ the instruction is: **find the
sparsest cut and add edges across it**. The sparsest cuts in the human social
graph are not genetic distances — they are visa regimes, capital controls,
language gaps, carceral systems, and infrastructure enclosure. The repaired
objective points **outward** where v1's pointed inward.

---

# §6 — Objections we take seriously

A framework that only lists its own supporting arguments is propaganda.

### 6.1 · The universalization objection *(the serious one)*

Pan-Africanism — Du Bois, Garvey, Padmore, C.L.R. James, Nkrumah, Cabral,
Nyerere, Sankara; the OAU and the African Union — is a **specific political
tradition** concerned with liberation, self-determination and material redress
for African and African-descended peoples under enslavement, colonialism, and
their afterlives. It has live institutional expressions: Agenda 2063, the
AfCFTA, reparations claims, land questions.

The objection: **"we are all African" is precisely the move that dissolves
those claims.** It converts a demand made by particular people who suffered
particular harms into a universal metaphor nobody has to pay for. If everyone
is diaspora, no one is owed anything for having been *made* diaspora at
gunpoint. Universalization can operate as expropriation of a political
vocabulary.

**This objection has real force and this document does not defeat it.** The
most we claim: descriptive universality about ancestry and historical
particularity about injustice are **different claims at different levels**, and
the first does not cancel the second. The transatlantic slave trade, colonial
partition, and ongoing anti-Black racism are historical facts with
identifiable perpetrators, beneficiaries and victims. Nothing in §1 softens
one of them, and any use of this framework to argue otherwise is a misuse.

Contributors who find the objection decisive — who think a universalist thesis
has no business carrying the name Pan-Africanism — should open an issue. That
naming question is genuinely unresolved and is not the sort of thing a
formalism settles.

### 6.2 · The colorblindness objection

"We are one family" has a long track record as a way of declining to discuss
present-day stratification. Deep-ancestry universalism is fully compatible
with indifference to housing discrimination, policing, and wealth gaps. Judge
a framework partly by what it makes easier to avoid saying.

### 6.3 · The self-application objection *(aimed at this document)*

§4 forbids deriving norms from genetics — yet §2 arranges genetic facts into
something that reads like an argument for a politics. Is D5 really independent,
or is the firewall a fig leaf? **Our answer, offered without confidence that it
fully succeeds:** §1 is deployed *defensively*, removing an objection rather
than supplying a premise. But the rhetoric does lean on it. Hold us to §4
wherever it slips.

### 6.4 · The "living ancestors" misreading

F1 and F5 are routinely mangled into the claim that Khoe-San or other forager
populations are "the original humans," evolutionarily frozen, or closer to the
root. **They are not.** Earliest-diverging is a statement about tree topology,
never about primitiveness. This misreading has a long and ugly history and the
framework must not feed it.

### 6.5 · Scientific uncertainty

Divergence-time estimates for the earliest human splits vary by more than a
factor of two across published models (120–135 kya in Ragsdale et al. 2023
versus 350–260 kya in Schlebusch et al. 2017). Archaic-introgression estimates
in African populations are method-sensitive and drawn from limited sampling —
Chen et al. explicitly note how few African populations were available.
Re-audit this document as sampling improves, particularly via H3Africa.

### 6.6 · The "so what" objection

Suppose every claim in §1 is correct. Borders are enforced by states with
armed capacity, not by beliefs about coalescent times. A correct account of
the ancestral recombination graph has never opened a checkpoint. The practical
leverage here is, at best, indirect — which is another reason the political
argument in D5 has to stand on its own legs.

---

# §7 — Falsifiable predictions

| # | Prediction | Falsified by |
|---|---|---|
| P1 | $\delta_T(i) > 0.95$ for all sampled living humans at $T$ = 100 kya | Any population substantially lower |
| P2 | $\sup_{i,j\in\text{Afr}} F_{ST}(i,j) \gtrsim F_{ST}(\text{Afr},\text{non-Afr})$ under matched sampling + rarefaction | Reversal under unbiased WGS sampling |
| P3 | Heterozygosity–distance slope stays linear ($R^2 > 0.7$) on WGS data with denser African sampling | Non-linearity or breakpoints |
| P4 | "The African ADMIXTURE component" fissions at fixed $K$ as African sampling densifies | A stable single component |
| P5 | Cooperation-scale metrics track institutional variables ($m,\rho,\kappa,e,\nu$), not ancestry distance, controlling for wealth | Robust residual ancestry effect |
| P6 | Genealogical MRCA of living humans within the last ~10 kyr on migration-calibrated models | Substantially older MRCA |

---

# §8 — Reproduction protocol

```bash
# ── Data (open access, consent-governed — read each project's terms first)
#    1000 Genomes Project  ·  HGDP (Bergström et al. 2020)
#    SGDP (Mallick et al. 2016)  ·  H3Africa (access + benefit-sharing terms apply)

# ── P2: the F_ST reversal — the load-bearing check in this document
plink2 --pfile all_wgs --fst CATPHENO --pheno pop_labels.txt
#   MUST rarefy to common n per population before comparing.
#   MUST use WGS, not arrays — array ascertainment biases F_ST and H_e.

# ── P3: the serial founder law (Ramachandran replication on WGS)
#   compute per-population H_e, regress on great-circle distance from
#   Addis Ababa (9N, 38E) with water-crossing corrections; expect R^2 > 0.7

# ── P1: the diaspora fraction δ
python -m tsinfer infer all_wgs.samples -O humans.trees
python -m tsdate preprocess humans.trees | python -m tsdate date -
#   then spatiotemporal lineage inference (cf. Wohns et al. 2022)


# ── archaic fraction (the δ shortfall)
IBDmix --genotype all_wgs.vcf --archaic AltaiNeanderthal.vcf

# ── P4: ADMIXTURE component fission
for K in 2 4 6 8 10 12; do admixture --cv all_wgs.bed $K; done
#   then goodness-of-fit — DO NOT SKIP:
#   badMIXTURE  →  github.com/danjlawson/badMIXTURE
```

**Ethics requirement for this repo.** Any analysis of African genomic data
merged here must document its consent basis and comply with the originating
project's governance terms. High diversity (F2, F3) has historically been
treated as an invitation to extraction — the "living laboratory" framing is
exactly the misuse F1 and §6.4 warn about. PRs ignoring this will be closed.

---

# §9 — References

**Origins and deep structure**
- Hublin, J.-J. et al. (2017). New fossils from Jebel Irhoud, Morocco and the pan-African origin of *Homo sapiens*. *Nature* 546:289–292.
- Vidal, C.M. et al. (2022). Age of the oldest known *Homo sapiens* from eastern Africa. *Nature* 601:579–583.
- Scerri, E.M.L. et al. (2018). Did our species evolve in subdivided populations across Africa? *TREE* 33:582–594.
- Ragsdale, A.P. et al. (2023). A weakly structured stem for human origins in Africa. *Nature* 617:755–763. doi:10.1038/s41586-023-06055-y
- Schlebusch, C.M. et al. (2017). Southern African ancient genomes estimate modern human divergence to 350,000–260,000 years ago. *Science* 358:652–655.
- Schlebusch, C.M. et al. (2020). Khoe-San genomes reveal unique variation and confirm the deepest population divergence in *Homo sapiens*. *MBE* 37:2944–2954.

**The diversity gradient**
- Ramachandran, S. et al. (2005). Support from the relationship of genetic and geographic distance in human populations for a serial founder effect originating in Africa. *PNAS* 102:15942–15947.
- Prugnolle, F., Manica, A., Balloux, F. (2005). Geography predicts neutral genetic diversity of human populations. *Curr Biol* 15:R159–R160.
- DeGiorgio, M., Jakobsson, M., Rosenberg, N.A. (2009). Explaining worldwide patterns of human genetic variation using a coalescent-based serial founder model. *PNAS* 106:16057–16062.
- Henn, B.M., Cavalli-Sforza, L.L., Feldman, M.W. (2012). The great human expansion. *PNAS* 109:17758–17764.
- Henn, B.M. et al. (2016). Distance from sub-Saharan Africa predicts mutational load in diverse human genomes. *PNAS* 113:E440–E449.

**Apportionment, structure, and method critique**
- Lewontin, R.C. (1972). The apportionment of human diversity. *Evolutionary Biology* 6:381–398.
- Barbujani, G. et al. (1997). An apportionment of human DNA diversity. *PNAS* 94:4516–4519.
- Rosenberg, N.A. et al. (2002). Genetic structure of human populations. *Science* 298:2381–2385.
- Edwards, A.W.F. (2003). Human genetic diversity: Lewontin's fallacy. *BioEssays* 25:798–801.
- Novembre, J. & Stephens, M. (2008). Interpreting principal component analyses of spatial population genetic variation. *Nat Genet* 40:646–649.
- McVean, G. (2009). A genealogical interpretation of principal components analysis. *PLoS Genet* 5:e1000686.
- Lawson, D.J., van Dorp, L., Falush, D. (2018). A tutorial on how not to over-interpret STRUCTURE and ADMIXTURE bar plots. *Nat Commun* 9:3258.

**Comparative and archaic**
- Prado-Martinez, J. et al. (2013). Great ape genetic diversity and population history. *Nature* 499:471–475.
- Chen, L., Wolf, A.B., Fu, W., Li, L., Akey, J.M. (2020). Identifying and interpreting apparent Neanderthal ancestry in African individuals. *Cell* 180:677–687.
- Reich, D. (2018). *Who We Are and How We Got Here*. Pantheon.

**Phenotype**
- Crawford, N.G. et al. (2017). Loci associated with skin pigmentation identified in African populations. *Science* 358:eaan8433.
- Quillen, E.E. et al. (2019). Shades of complexity: new perspectives on the evolution and genetic architecture of human skin. *AJPA* 168:4–26.

**Genealogy**
- Chang, J.T. (1999). Recent common ancestors of all present-day individuals. *Adv Appl Prob* 31:1002–1026.
- Rohde, D.L.T., Olson, S., Chang, J.T. (2004). Modelling the recent common ancestry of all living humans. *Nature* 431:562–566.
- Matsen, F.A. & Evans, S.N. (2008). To what extent does genealogical ancestry imply genetic ancestry? *Theor Popul Biol* 74:182–190.
- Wohns, A.W. et al. (2022). A unified genealogy of modern and ancient genomes. *Science* 375:eabi8264.

**Cooperation**
- Grafen, A. (1985). A geometric view of relatedness. *Oxford Surveys in Evolutionary Biology* 2:28–89.
- Taylor, P.D. (1992). Altruism in viscous populations. *Evol Ecol* 6:352–356.
- Queller, D.C. (1994). Genetic relatedness in viscous populations. *Evol Ecol* 8:70–73.
- West, S.A., Pen, I., Griffin, A.S. (2002). Cooperation and competition between relatives. *Science* 296:72–75.
- Ostrom, E. (1990). *Governing the Commons*. Cambridge UP.
- Boyd, R. & Richerson, P.J. (2005). *The Origin and Evolution of Cultures*. Oxford UP.
- Henrich, J. (2015). *The Secret of Our Success*. Princeton UP.

**Consensus statements**
- Fuentes, A. et al. (2019). AABA/AAPA Statement on Race and Racism. *AJPA* 169:400–402. doi:10.1002/ajpa.23882
- Jena Declaration (2019). German Zoological Society, 112th Annual Meeting.

**Political tradition**
- Du Bois, W.E.B. (1947). *The World and Africa*.
- Nkrumah, K. (1963). *Africa Must Unite*.
- Cabral, A. (1979). *Unity and Struggle*.
- African Union. *Agenda 2063: The Africa We Want*.

---

# §10 — Acknowledgements

### Authorship and provenance

This document was produced through a human-directed exchange with two large
language models. Stating that plainly is part of the point: a framework whose
central rule is *check the claim, not the claimant* (§4) cannot be coy about
where it came from.

**Grok 4.5 (xAI)** — original ten-theorem draft (v1). The formalism there is
the seed this entire document grew from. Several of its propositions turned
out to be wrong, and one had to be discarded outright — but **wrong in a
specific, checkable way is a real contribution**. A vague draft could not have
been audited. v1 stated ten claims precisely enough to be tested against the
literature, which is exactly why §5 exists and why F2, F5 and F10 could be
written at all. The errors were productive; the framing question — *what would
a Pan-Africanism grounded in the actual biology look like?* — was the right
question to ask.

**Claude Opus 5 (Anthropic)** — v2 and v3: the audit, the corrections, the
affirmative evidence in §1, the δ statistic, the is/ought firewall, the
objections in §6, and the reference apparatus.

**Direction, framing, and editorial judgment** — the repo maintainer
(`anarcho-app`), who set the goal that reoriented the entire project: that
Neo-Pan-Africanism should be an ideology of *human* unification rather than a
continental one, and that it should be grounded in evidence rather than
asserted. That instruction is what turned a set of cluster arguments into
§2's One Diaspora Thesis. Neither model proposed it.

### ⚠️ Verify before you rely on this

**Language models generate plausible-looking citations that are sometimes
wrong.** The load-bearing empirical claims here — the Ramachandran regression
coefficients, the Chen et al. introgression figures, the Prado-Martinez
heterozygosity ranges, the Ragsdale divergence estimates, the Crawford
pigmentation results — were checked against primary sources during drafting.
**They were not checked by a domain expert, and no author of this document is
a population geneticist.**

Treat every number as a pointer to a paper, not as a fact on our authority.
DOIs are given in §9 precisely so you can go around us. If you find an error,
§10's whole purpose is that you should be able to attribute it correctly and
fix it — open an issue.

### The people whose work this rests on

The findings in §1 are not ours in any sense. They belong to the researchers
cited in §9 and to the far larger body of work those papers summarize —
population geneticists, paleoanthropologists, archaeologists, evolutionary
theorists, and the field's own internal critics, whose willingness to publish
"here is how not to over-interpret our own method" (Lawson, van Dorp & Falush;
Novembre & Stephens) is what made the corrections in §5 possible at all.

**And most of all: the participants.** Every result in §1 exists because tens
of thousands of people — disproportionately in African communities, often in
research relationships that were historically extractive and unequal —
consented to have their genomes sequenced. The HGDP, SGDP, 1000 Genomes,
H3Africa, and the Nama, Ju|'hoansi, Mbuti, Yoruba, Mende, Gumuz, Amhara, Oromo
and many other communities whose data underlie the papers cited here.

A document arguing that no group of humans is peripheral should not treat the
people who made it possible as a data source. The ethics requirement in §8 is
downstream of this paragraph, not the other way round.

---

## Contributing

In rough priority order:

1. **Try to break P2.** Run the $F_{ST}$ comparison on WGS with matched
   rarefaction. F5 is the load-bearing finding; if it fails, §2 needs
   rebuilding.
2. **Replicate P3 on modern data.** Ramachandran et al. used 783
   microsatellites in 2005. Redo it on whole genomes with denser African
   sampling.
3. **Implement δ.** §3 is a proposal, not a result. It needs code.
4. **Argue §6.1.** Whether a universalist thesis should carry the name
   Pan-Africanism is unresolved and deserves a real argument, not a paragraph.
5. **Find more errors.** v1 had six. v3 will have some.

**House rule.** Any PR asserting that genetic data establish the superiority,
priority or centrality of *any* group — **including African populations** —
will be closed with a link to §4. The firewall is not decorative. It is the
load the whole structure carries.

---

*v3.0 — The claim is not that this document is right. The claim is that every
line of it is checkable, and that we have told you where to start.*