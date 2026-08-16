# The Master System

*A dynamical model of when institutions have an interest in preserving the problems they exist to solve.*

---

## 1. State variables

Let $X_t$ be the **stock of the problem** (crime, illness, conflict, perceived threat), $A_t$ the **institution's capacity**, and $e_t \in [0,1]$ the **share of capacity actually directed at abatement**.

$$
\dot{X} = \underbrace{g(X)}_{\text{spontaneous growth}} \;-\; \underbrace{\theta\, e\, A}_{\text{abatement}} \;+\; \underbrace{\iota\,(1-e)\,A}_{\text{iatrogenesis}}
$$

$$
\dot{A} = A\left[\underbrace{\mu \rho X^{\beta}}_{\text{revenue feeds capacity}} - \delta\right]
$$

The second equation is a Lotka–Volterra predator equation with $X$ as prey. That is where the cycles come from mechanically:

> crisis → funding surge → abatement → problem falls → funding falls → capacity decays → problem regrows

Fire departments, pandemic preparedness, and defense budgets all oscillate for exactly this reason, **with no bad faith required**.

---

## 2. The one parameter that matters

$$
\beta \equiv \frac{\partial \ln R}{\partial \ln X}
$$

The elasticity of the institution's income with respect to the prevalence of its own problem.

Now solve the agent's actual optimization:

$$
V(X) = \max_{e(\cdot)} \int_{0}^{\infty} e^{-rt}\left[\rho X^{\beta} \pi(e) - c(e)\right] dt
$$

and define the shadow price $\lambda = V'(X)$. The whole thesis compresses to one sentence:

> **The perverse regime is $\lambda > 0$ — the problem appears as an *asset* on the institution's implicit balance sheet.**

The first-order condition on effort then reads:

$$
\underbrace{p\, \partial_e h}_{\text{paid to treat}} = \underbrace{c'(e)}_{\text{cost of effort}} + \underbrace{\lambda\, \partial_e \dot{X}}_{\text{capital destroyed by solving}}
$$

That last term is the entire phenomenon.

Clark's classic result gives the sharpest prediction available: the agent drives $X \to 0$ **only when $g'(0) < r$** — only when the problem regenerates more slowly than the institution discounts the future. Smallpox got eradicated. Anxiety, crime, and geopolitical instability regenerate faster than any discount rate, so they get held at an interior steady state $X^{\star} > 0$.

**Institutions don't eliminate their problems; they manage them toward maximum sustainable yield.**

---

## 3. But β alone over-predicts

Selling umbrellas doesn't give you an incentive to make it rain. Three parameters, not one:

| Parameter | Name | Question |
|---|---|---|
| $\beta$ | gain | Does revenue rise with $X$? |
| $\kappa$ | controllability | Can the agent actually move $X$? |
| $\varepsilon$ | discipline | Competition, liability, licensing, elections, exit |

$$
\text{Perverse equilibrium} \iff \beta \kappa > \varepsilon
$$

### Class I — genuinely perverse

*Condition: $\beta\kappa > \varepsilon$.*

Private prisons with contractual occupancy guarantees. Policing funded by civil asset forfeiture. Fee-for-service specialty medicine (supplier-induced demand has a real empirical literature going back to Evans in the 1970s). Opioid marketing. Engagement-optimized media. Cost-plus defense procurement. The weight-loss industry, whose recidivism rate *is* its retention model. These aren't allegations — they're documented, with named mechanisms.

### Class II — high gain, no control

*Condition: $\beta > 0$ but $\kappa \approx 0$.*

Morgues and funeral homes profit from death and cannot cause it. Most dentistry: fluoridation and sealants demolished the caries base and dentists advocated for both, which is $\kappa$ pointed the right way. Academia is the sharpest error on the list — solving a famous problem is the single highest-return act available to a researcher. Its real pathology is portfolio conservatism under grant cycles, not problem-preservation.

### Class III — the inversion

Insurance is backwards. Realized losses are a *cost*, so $\beta_X < 0$. Insurers wrote the fire codes, funded the seatbelt research, and invented workplace safety inspection.

---

## 4. The refinement that saves the thesis

Split the stock: $X$ **actual** versus $\hat{X}$ **perceived**. Now $\beta$ decomposes, and you get a much sharper typology:

| Signature | Regime | Examples |
|---|---|---|
| $\beta_X > 0,\ \beta_{\hat{X}} > 0$ | **harvesting** | chronic care, incarceration |
| $\beta_X \approx 0,\ \beta_{\hat{X}} > 0$ | **alarm manufacture** | media, security contractors, crisis politics |
| $\beta_X < 0,\ \beta_{\hat{X}} > 0$ | **insurance** | wants you frightened, not harmed |

This predicts something a flat list can't: media and security firms don't generate danger, they generate *belief* in danger. That's a different pathology with a different remedy, and conflating the two sends you after the wrong lever.

---

## 5. The fix

Structural, not moral: **make the agent's balance sheet hold the harm.**

- Capitation instead of fee-for-service
- Reinsurance instead of claims-paid
- Recidivism-linked instead of occupancy-linked

When the institution owns $X$, $\lambda$ flips sign and the harvesting equilibrium dissolves.

---

## Appendix A — The source list, adjudicated

The twenty claims below are the raw input the framework was built to filter. Reproduced verbatim, then scored.

Ratings are **ordinal, not cardinal**, and several are contestable — the point of the table is to show that the framework separates the list rather than ratifying it. $\beta_X$ and $\beta_{\hat{X}}$ take values in $\{+, 0, -\}$; $\kappa$ and $\varepsilon$ in $\{\text{H}, \text{M}, \text{L}\}$. A dagger (†) marks entries whose class depends on a **payment or contract structure**, not on the sector — those are the ones the Section 5 fix actually reaches.

| # | Institution | $\beta_X$ | $\beta_{\hat{X}}$ | $\kappa$ | $\varepsilon$ | Class | Signature |
|---|---|:---:|:---:|:---:|:---:|:---:|---|
| 1 | Governments / crisis management | 0 | + | M | M | I–II | alarm manufacture |
| 2 | Weapons manufacturers | + | + | L | L | I† | harvesting + alarm |
| 3 | Healthcare systems | + | + | H | L | I† | harvesting |
| 4 | Morgues & funeral homes | + | 0 | ~0 | M | II | — |
| 5 | Police departments | + | + | H | L | I† | harvesting |
| 6 | Central banks | n/a | n/a | L | M | mis-specified | — |
| 7 | Mental-health industry | 0 | + | M | L | I–II | diagnostic expansion |
| 8 | Lawyers / legal system | + | + | M | M | I† | harvesting |
| 9 | Pharmaceutical companies | + | + | M | M | I† | harvesting |
| 10 | Mainstream media | 0 | + | H | L | I | alarm manufacture |
| 11 | Prisons / incarceration | + | + | L | L | I† | harvesting |
| 12 | Dentists | + | + | M | M | II | $\kappa$ historically inverted |
| 13 | Insurance companies | − | + | M | M | III | **inversion** |
| 14 | Diet / fitness / weight-loss | + | + | H | L | I | harvesting |
| 15 | Security & private defense firms | 0 | + | H | L | I | alarm manufacture |
| 16 | Environmental bureaucracy / green industry | 0 | + | L | M | II | contested |
| 17 | Academia & research institutions | + | + | L | M | II | portfolio conservatism |
| 18 | Banks & credit industry | + | 0 | H | H† | I† | harvesting when $\varepsilon$ is severed |
| 19 | Traffic enforcement | + | 0 | H | L | I | harvesting |
| 20 | Cybersecurity firms | + | + | L | M | II | alarm manufacture |

### Item-by-item

1. **Governments are incentivized by crisis management and the sustained use of fear.** Too coarse an aggregate to score: the model applies to agencies with distinct budget lines, not to "government." Where it bites, it bites on $\hat{X}$ — authority and appropriation expand with perceived threat and rarely contract afterward (the ratchet). $\varepsilon$ is whatever the polity's elections, courts, and press actually deliver, which is the variable doing the work.

2. **Weapons manufacturers are incentivized by wars and prolonged conflict.** $\kappa$ on war initiation is low — they don't declare wars — but the peacetime threat-perception budget is the larger revenue base, so the live mechanism is $\beta_{\hat{X}}$. The genuine Class I element is contractual: cost-plus procurement pays for overruns, which is $\lambda > 0$ on the *cost* stock rather than on conflict itself.

3. **Healthcare systems are incentivized by ongoing sickness.** True under fee-for-service, false under capitation — the sector is not the unit of analysis, the reimbursement rule is. Supplier-induced demand has an empirical literature going back to Evans in the 1970s.

4. **Morgues and funeral homes are incentivized by death.** $\beta > 0$ and $\kappa \approx 0$. The paradigm Class II entry: gain without control is not an incentive problem.

5. **Police departments are incentivized by crime (and the budgets that follow it).** Budget elasticity to crime is positive but weak and lagged — appropriations are sticky and clearance is rewarded. The sharp case is **civil asset forfeiture**, where revenue is harvested directly from enforcement and $\varepsilon$ collapses.

6. **Central banks and money-printing institutions are incentivized by institutional greed and debt expansion.** Mis-specified: central banks remit profits to the treasury and do not maximize revenue, so $\beta$ has no referent in the model's sense. A defensible version of the claim is about *mandate expansion* under crisis, which is an $\hat{X}$ argument. The debt-accumulation claim belongs to item 18.

7. **Psychologists and much of the mental-health industry are incentivized by mental illness.** The mechanism is diagnostic-threshold expansion, which moves $\hat{X}$, not $X$ — and expansion has also increased genuine access, so the sign on welfare is not the sign on $\beta$. Cutting the other way: successful treatment discharges a client, and referral reputation is a real $\varepsilon$.

8. **Lawyers and the legal system are incentivized by conflict, disputes, and lawsuits.** Hourly billing puts $\lambda > 0$ on dispute duration; contingency fees put it on resolution. Same profession, opposite sign, set by fee structure.

9. **Pharmaceutical companies are incentivized by chronic and recurring illness.** Maintenance drugs are annuities and cures are one-time revenue, which is a real portfolio tilt — but curative hepatitis C therapy was developed and marketed anyway, so $\kappa$ toward cure is not zero. Patent cliffs, generics, and regulators make $\varepsilon$ stronger than the list assumes. Opioid marketing is the documented Class I instance.

10. **Mainstream media is incentivized by fear, outrage, and sensationalism.** The canonical alarm-manufacture case: $\beta_X \approx 0$, $\beta_{\hat{X}} \gg 0$. Competition is intense but competes *on* attention, so $\varepsilon$ is perverse rather than absent — more entrants make it worse.

11. **Prisons and the incarceration industry are incentivized by high inmate populations.** Private operators with contractual occupancy guarantees are Class I by construction. Public systems have $\beta > 0$ on per-inmate budget but low $\kappa$: legislatures and judges set the input.

12. **Dentists are incentivized by cavities, gum disease, and ongoing dental problems.** The profession advocated for fluoridation and sealants, which demolished its own caries base — $\kappa$ pointed the right way. Residual overtreatment exists but is a much smaller $\beta\kappa$ than the list implies.

13. **Insurance companies are incentivized by risk, accidents, and disasters.** Backwards. Realized losses are a cost, so $\beta_X < 0$; insurers wrote the fire codes, funded the seatbelt research, and invented workplace safety inspection. What they do want is $\hat{X}$: fear sells policies. Frightened, not harmed.

14. **The diet, fitness, and weight-loss industry is incentivized by obesity and body dissatisfaction.** Recidivism *is* the retention model, with no efficacy standard and no liability for failure. Worth watching as a natural experiment: an intervention with durable results has entered the market, which is $\varepsilon$ arriving through competition rather than regulation.

15. **Security companies and private defense contractors are incentivized by perceived threats and insecurity.** They do not generate danger; they generate belief in danger. Different pathology, different lever.

16. **Environmental bureaucracies and certain green industries are incentivized by ongoing ecological crises.** The strongest counter-evidence is on the record: leaded gasoline, CFCs, and acid rain were regulated to resolution and the corresponding programs shrank. Where the claim has force is in subsidy-dependent industry, whose revenue is tied to the problem remaining unsolved — a $\beta$ on the *policy*, not on the ecology. Genuinely contested; scored conservatively here.

17. **Academia and research institutions are incentivized by the continued existence (and funding) of unsolved problems.** The sharpest error on the list. Solving a famous problem is the highest-return act available to an individual researcher, so $\kappa$ points away from preservation. The real pathology is portfolio conservatism under grant cycles — safe incremental work crowding out risky work — which is a different failure with a different fix.

18. **Banks and the credit industry are incentivized by debt accumulation and interest payments.** $\beta > 0$ and $\kappa$ is high (underwriting standards, credit limits, marketing) — but default risk normally internalizes the harm, which is $\varepsilon$ built into the balance sheet. Originate-to-distribute severs exactly that link, and 2008 is what the severed version looks like. This entry is the cleanest illustration of the Section 5 fix, because the remedy already exists as risk-retention rules.

19. **Traffic enforcement agencies are incentivized by violations, tickets, and fines.** Arguably the cleanest Class I case on the list and the least ideological: revenue is harvested directly from the stock, $\kappa$ is near-total (enforcement intensity, limit placement, signal timing), and $\varepsilon$ is minimal where fines fund the enforcing body.

20. **Cybersecurity firms are incentivized by the persistence of digital threats and data breaches.** They do not create attackers, so $\kappa$ on $X$ is low; $\kappa$ on $\hat{X}$ is high. Breaches are measurable and liability is growing, which gives real $\varepsilon$. The narrow exception worth naming is vulnerability disclosure, where an offensive-capability business has an interest in the flaw persisting.

### What the filter removed

Of twenty claims, **four survive without qualification** (10, 14, 15, 19), **six survive conditional on contract structure** (2, 3, 5, 8, 9, 11, 18 — where the fix is already specified), **six are Class II or downgraded** (1, 4, 7, 12, 17, 20), **one is contested** (16), **one is inverted** (13), and **one is mis-specified** (6).

That is the value of the framework: a flat list of twenty targets becomes four fights, seven contract rewrites, and nine corrections.

---

## Notation reference

| Symbol | Meaning |
|---|---|
| $X_t$ | stock of the problem |
| $\hat{X}$ | *perceived* stock of the problem |
| $A_t$ | institutional capacity |
| $e_t \in [0,1]$ | share of capacity directed at abatement |
| $g(X)$ | spontaneous growth of the problem |
| $\theta$ | abatement efficiency |
| $\iota$ | iatrogenesis coefficient (harm from misdirected capacity) |
| $\mu, \rho$ | revenue-to-capacity conversion and revenue scale |
| $\delta$ | capacity decay rate |
| $r$ | discount rate |
| $\lambda = V'(X)$ | shadow price of the problem stock |
| $\beta$ | revenue elasticity w.r.t. problem prevalence |
| $\kappa$ | controllability of $X$ by the agent |
| $\varepsilon$ | external discipline |
