# 3 TRIAL OBJECTIVES AND ASSOCIATED ESTIMANDS

Each estimand is described by five attributes: the population, the variable (endpoint), the handling of intercurrent events, the population-level summary, and the treatment condition [STD]. The study eye is the unit of analysis; if both eyes qualify, the eye with the worse BCVA at randomization is selected, or the right eye if equal (Section 5.1) [DERIVED]. The intercurrent events are defined once and apply to every estimand:

| Intercurrent event | Strategy for P1 and binary endpoints | Source |
|---|---|---|
| Rescue therapy for nAMD (aflibercept 8 mg outside the masked schedule) | Composite: the participant is counted as having the event | [USER:P2-release][PREC:Rani:s13/Q1f] |
| Permanent discontinuation of randomized treatment without rescue | Treatment policy: data collected after discontinuation are used; participants are followed to Week 56 | [PREC:Rani:s13/Q1i] |
| Other prohibited nAMD treatment in the study eye | Composite: the participant is counted as having the event | [DERIVED] |

> 【設計変更コメント D3】リリースの第 2 相主要評価項目は「15 文字以上の低下またはレスキュー」の複合である。入力の主要評価項目（15 文字以上の低下）に、救済療法を事象とする複合戦略を加えた。FDA の先例も、15 文字以上の低下と救済を治療失敗とし、救済と投与中止の例も追跡するよう求めている [PREC:Rani:s13/Q1f][PREC:Rani:s13/Q1i]。

## 3.1 Primary Objective(s) and Associated Estimand(s)

**Primary objective.** To demonstrate that XYZ-123 ophthalmic solution is non-inferior to aflibercept 8 mg IVT injection in maintaining visual acuity through Week 48 in participants with nAMD who responded to aflibercept induction [USER][DERIVED].

| Attribute | Definition |
|---|---|
| Objective | Non-inferiority of XYZ-123 versus aflibercept 8 mg |
| Endpoint (P1) | Reduction of 15 or more letters in BCVA (Best corrected visual acuity) as measured by ETDRS visual acuity chart from baseline Week 48 |
| Baseline | BCVA at the randomization visit (Week 0) |
| Population | Participants 50 years or older with nAMD in the study eye who met the response criteria after three aflibercept 8 mg induction injections and were randomized |
| Intercurrent events and strategy | Rescue therapy and other prohibited nAMD treatment: composite (event). Permanent discontinuation of randomized treatment: treatment policy |
| Population-level summary | Difference in the proportion of participants with the event (XYZ-123 minus aflibercept 8 mg), with a stratified Newcombe one-sided 97.5% upper confidence bound compared with the non-inferiority margin [TBD] |
| Treatment condition | XYZ-123 0.5% QD eye drops plus sham procedures versus aflibercept 8 mg IVT plus vehicle eye drops, each for 52 weeks, regardless of dose adjustment of the aflibercept interval |

[USER][CTG:NCT04270747][DERIVED]

A missing BCVA value at Week 48 that is not explained by rescue is handled as described in Section 10.4 [DERIVED].

> 【設計変更コメント D4】★ 非劣性マージンは出典がなく [TBD]。BCVA 変化量の非劣性マージンは参照試験の 3 本で 4 文字、FDA 先例は 4.5 文字以下（同等性）と 4 文字（条件つき）[CTG:NCT04423718][CTG:NCT02307682][CTG:NCT04005352][PREC:Rani:s13/Q1b][PREC:Fari:s40/p49c]。割合のマージンの先例はない。第 2 相の複合事象率が 31〜35% で、対照の 15 文字以上の低下が 2.4〜5.6% なら、非劣性は成立しない見込みが高い。主要評価項目の型（割合か変化量か）、マージン、デザインを EOP2 で当局と協議すること。

## 3.2 Secondary Objective(s) and Associated Estimand(s)

**Key secondary objectives** (tested in a fixed sequence only if the primary non-inferiority hypothesis is met; Section 10.10):

| ID | Objective | Endpoint | Timepoint |
|---|---|---|---|
| KS1 | To compare the proportion of participants with a BCVA loss or rescue over the maintenance period | Proportion of participants with a 15-letter or greater BCVA loss from baseline or rescue therapy at any time from Week 8 to Week 52 | Week 52 |
| KS2 | To compare the time to first loss or rescue | Time to first occurrence of a 15-letter or greater BCVA loss from baseline or rescue therapy through Week 52 | Week 52 |
| KS3 | To compare the change in visual acuity | Change from baseline in BCVA (ETDRS letters) at Week 48 | Week 48 |
| KS4 | To compare the change in retinal thickness | Change from baseline in central subfield thickness (CST) by SD-OCT at Week 48 | Week 48 |
| KS5 | To compare the proportion of participants with a dry macula | Proportion of participants with no intraretinal fluid and no subretinal fluid in the central subfield at Week 48 | Week 48 |

[USER:P2-release][CTG:NCT04423718][CTG:NCT02307682][PREC:Rani:s13/Q1b]

**Other secondary objectives.**

| ID | Objective | Endpoint | Timepoint |
|---|---|---|---|
| S1 | To assess treatment failure relative to the best BCVA | Proportion of participants with a reduction of 15 or more letters in BCVA compared with the best BCVA recorded before Week 48 or rescue therapy through Week 48 | Week 48 |
| S2 | To assess patient-reported visual function | Change from baseline in NEI VFQ-25 total score at Week 48 | Week 48 |
| SAF1 | To assess safety and tolerability | Ocular and non-ocular treatment-emergent adverse events, including dry eye and punctate keratitis | through Week 56 |

[PREC:Rani:s13/Q1f][CTG:NCT04423718][INSTR:NEI VFQ-25:2026-10-04][USER:P2-release]

**Estimand attributes for the secondary endpoints.**

| ID | Population | Intercurrent events and strategy | Summary | Treatment condition |
|---|---|---|---|---|
| KS1, KS2 | As in 3.1 | Rescue: composite (event). Discontinuation: treatment policy. Participants without an event are censored at Week 52 or last assessment (KS2) | Difference in proportions (KS1); hazard ratio from a stratified Cox model and Kaplan-Meier estimates (KS2) | As in 3.1 |
| KS3 | As in 3.1 | Rescue: hypothetical (supportive: trimmed mean). Discontinuation: treatment policy | Difference in mean change (LS means) | As in 3.1 |
| KS4 | As in 3.1 | Rescue: hypothetical. Discontinuation: treatment policy | Difference in mean change (LS means) | As in 3.1 |
| KS5 | As in 3.1 | Rescue: composite (not dry). Discontinuation: treatment policy | Difference in proportions | As in 3.1 |
| S1 | As in 3.1 | As for P1 | Difference in proportions | As in 3.1 |
| S2 | As in 3.1 | Rescue: treatment policy. Discontinuation: treatment policy | Difference in mean change | As in 3.1 |

[CTG:NCT04423718][PREC:Rani:s13/Q1i][DERIVED]

## 3.3 Exploratory Objective(s)

Exploratory objectives are to describe the number of aflibercept 8 mg injections and sham procedures received in each arm; the BCVA and CST over time by visit; the proportion of participants rescued, by visit; the relationship of plasma XYZ-123 concentration to efficacy and ocular surface findings; and the incidence of anti-drug antibodies if measured. The results are descriptive and are not used for hypothesis testing [DERIVED][TBD].
