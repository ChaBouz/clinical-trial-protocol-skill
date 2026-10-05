# Title Page

| Item | Content |
|---|---|
| Full title | A Phase 3, Randomized, Double-Masked, Double-Dummy, Active-Controlled, Parallel-Group Study to Evaluate the Efficacy and Safety of XYZ-123 Ophthalmic Solution Versus Aflibercept 8 mg Intravitreal Injection as Maintenance Therapy in Participants With Neovascular Age-Related Macular Degeneration After Aflibercept Induction [DERIVED] |
| Short title / acronym | [TBD] |
| Sponsor protocol number | [TBD] |
| Phase | 3 [USER] |
| Investigational product | XYZ-123 ophthalmic solution (vascular endothelial growth factor receptor [VEGFR] inhibitor; topical eye drop) [USER] |
| Active comparator | Aflibercept 8 mg intravitreal injection [USER] |
| Regulatory identifiers (IND, EU CT number, jRCT) | [TBD] |
| Sponsor name and address | [TBD] |
| Version / date / amendment | Draft v0.1, 2026-10-04, no amendments [DERIVED] |
| Confidentiality statement | This document contains confidential information of the sponsor. It must not be disclosed to any third party without the written authorization of the sponsor, except to the extent necessary to obtain informed consent or to conduct the trial under applicable regulations. [STD] |

> 【設計変更コメント】本書の設計は利用者の入力に、製薬会社のニュースリリース（XYZ-123 の第 2 相として読み替え）を反映して補った。入力からの変更点と理由は `design_decisions.md`（D1–D13）にまとめ、本文では該当箇所に「【設計変更コメント D#】」を残した。ラベル `[USER:P2-release]` はこのリリース由来を示す。

# 1 PROTOCOL SUMMARY

## 1.1 Protocol Synopsis

**Short title.** XYZ-123 maintenance therapy versus aflibercept 8 mg in nAMD after aflibercept induction [DERIVED]

**Rationale (short).** Neovascular age-related macular degeneration (nAMD) is treated with repeated intravitreal (IVT) injections of anti-vascular endothelial growth factor (anti-VEGF) agents, which impose a treatment burden on participants and clinics [DERIVED]. XYZ-123 is a topical VEGFR inhibitor being developed as a non-invasive maintenance approach after anti-VEGF IVT induction [USER:P2-release]. In a Phase 2, randomized, double-masked, three-dose study without a control arm, participants who responded to aflibercept induction were randomized to XYZ-123 0.5% QD, 2.0% QD or 2.0% BID. Between about 65% and 69% of participants had no BCVA loss of 15 letters or more and no rescue therapy through Week 52, but the high dose did not show superiority over the low dose, no dose response was seen, and the study was not controlled [USER:P2-release]. This Phase 3 study compares XYZ-123 with continued aflibercept 8 mg under double-masked conditions.

**Objectives, endpoints and estimands.** The primary and secondary endpoints are given in the table below. Section 3 gives the five attributes of each estimand.

| ID | Level | Endpoint | Timepoint |
|---|---|---|---|
| P1 | Primary | Reduction of 15 or more letters in BCVA (Best corrected visual acuity) as measured by ETDRS visual acuity chart from baseline Week 48 | Week 48 |
| KS1 | Key secondary | Proportion of participants with a 15-letter or greater BCVA loss from baseline or rescue therapy at any time from Week 8 to Week 52 | Week 52 |
| KS2 | Key secondary | Time to first occurrence of a 15-letter or greater BCVA loss from baseline or rescue therapy through Week 52 | Week 52 |
| KS3 | Key secondary | Change from baseline in BCVA (ETDRS letters) at Week 48 | Week 48 |
| KS4 | Key secondary | Change from baseline in central subfield thickness (CST) by SD-OCT at Week 48 | Week 48 |
| KS5 | Key secondary | Proportion of participants with no intraretinal fluid and no subretinal fluid in the central subfield at Week 48 | Week 48 |
| S1 | Secondary | Proportion of participants with a reduction of 15 or more letters in BCVA compared with the best BCVA recorded before Week 48 or rescue therapy through Week 48 | Week 48 |
| S2 | Secondary | Change from baseline in NEI VFQ-25 total score at Week 48 | Week 48 |
| SAF1 | Safety | Ocular and non-ocular treatment-emergent adverse events, including dry eye and punctate keratitis | through Week 56 |

[USER][USER:P2-release][CTG:NCT04423718][CTG:NCT02307682][PREC:Rani:s13/Q1f]

Participants who receive rescue therapy by Week 48 are counted as having the P1 event (composite strategy for the rescue intercurrent event). Participants who permanently discontinue randomized treatment without rescue are followed and analyzed under a treatment-policy strategy [PREC:Rani:s13/Q1i].

> 【設計変更コメント D3・D4】主要評価項目の定義は入力どおり（Week 48、ベースラインからの 15 文字以上の低下）。リリースの第 2 相主要評価項目が「15 文字以上の低下またはレスキュー」の複合だったため、救済を事象に数える戦略を加えた。★ 第 2 相の 52 週の複合事象率は 31.1〜34.9%（対照なし）で、対照の aflibercept の「15 文字以上の低下」は 2.4〜5.6%（救済を含まない値）[PRIOR:CTG:NCT02307682][PRIOR:CTG:NCT04270747]。事象の定義が違う値の比較だが、差が大きければ非劣性は示せない。EOP2 での協議が要る。

**Overall design.** Phase 3, randomized, double-masked (double-dummy), active-controlled, parallel-group, non-inferiority study in participants with nAMD who have responded to aflibercept 8 mg induction. All participants receive three aflibercept 8 mg IVT injections 4 weeks apart (±7 days) during a 12-week run-in. Participants who meet the response criteria at Run-in Week 12 are randomized 1:1 (Week 0) to XYZ-123 eye drops with sham injections or to aflibercept 8 mg IVT injections with vehicle eye drops for 52 weeks [USER][DERIVED]. Randomization is stratified by region (US, EU, Japan) and baseline BCVA (<64, ≥64 letters) [CTG:NCT04270747]. The primary timepoint is Week 48; participants complete a safety follow-up visit at Week 56 [USER][TBD].

**Number of participants.** The provisional lower bound is 668 randomized participants (334 per arm), set by the safety exposure target; the primary non-inferiority sample size depends on the margin, which is [TBD] (Section 10.11) [DERIVED]. The number of participants entering the run-in is [TBD] because the response rate to induction is not known.

**Arms and duration.** Arm A: XYZ-123 ophthalmic solution, 0.5% once daily (QD) to the study eye, plus sham IVT procedures at visits when an aflibercept injection would be due in Arm B [USER:P2-release][DERIVED]. Arm B: aflibercept 8 mg IVT, with maintenance injections 8 to 16 weeks apart (±1 week) according to masked assessment of visual and anatomic findings, plus vehicle eye drops at the same frequency as Arm A [USER]. Duration: screening [TBD], run-in 12 weeks, randomized treatment 52 weeks, safety follow-up to Week 56 [USER][DERIVED].

**Key eligibility.** Age 50 years or older; active choroidal neovascularization (CNV) secondary to nAMD in the study eye with intraretinal and/or subretinal fluid at screening; no prior treatment for nAMD in the study eye; good response to the three induction injections by criteria that are [TBD]; BCVA ETDRS letter score within a range that is [TBD]; ability to use eye drops reliably [CTG:NCT04423718][CTG:NCT06856577][PACK:neovascular_amd].

**Statistical methods (short).** The primary analysis compares the proportion of participants with the P1 event between arms using a stratified Newcombe confidence interval with Mantel-Haenszel weights; non-inferiority is concluded if the upper bound of the one-sided 97.5% confidence interval for the difference (XYZ-123 minus aflibercept 8 mg) is below the margin [TBD] [CTG:NCT04270747][STD]. Primary analysis sets are the full analysis set and the per-protocol set; both must support non-inferiority [STD]. Key secondary endpoints KS1 to KS5 are tested in a fixed sequence only if non-inferiority is shown [DERIVED].

**Data monitoring committee.** An independent Data Monitoring Committee reviews unmasked safety data, including ocular surface events and non-ocular events, at intervals defined in its charter [STD][TBD].

**Masking.** Participants, investigators, the masked visual acuity examiners and the masked assessor of disease activity do not know the treatment arm. Because XYZ-123 is given as eye drops and aflibercept as an injection, the study is double-dummy: Arm A receives sham procedures and Arm B receives vehicle eye drops. A separate, unmasked injector performs all injections and sham procedures and takes no other part in assessments [DERIVED][PREC:Brolu:s20/Q13].

**Rescue and concomitant therapy.** Aflibercept 8 mg may be given as rescue outside the masked schedule only when the protocol-defined rescue criteria are met; rescue is recorded and counted as an event in the primary analysis. Other treatments for nAMD in the study eye are prohibited. Rescue criteria and the prohibited and non-recommended therapy tables are in Section 6.10 [DERIVED][TBD].

**Safety assessments.** Adverse events, vital signs including blood pressure, intraocular pressure, slit-lamp examination and fluorescein corneal staining are assessed at each visit. Dry eye and punctate keratitis, which were seen in some participants in the Phase 2 study, are adverse events of special interest, and blood pressure is monitored because of the concern with systemic VEGF inhibition [USER:P2-release][DERIVED].

> 【設計変更コメント D1・D2】入力は「XYZ-123 点眼を 44 週（単独）vs aflibercept 8 mg」だった。(D1) リリースの第 2 相が「抗 VEGF 導入後の維持療法」だったため、導入期（aflibercept 8 mg を 4 週ごと 3 回）を全例に置き、反応良好例を無作為化する設計に変えた。反応良好の基準はリリースに無く [TBD]。(D2) ICH E1 の 1 年曝露（慢性・反復投与で ≥100 例）に 44 週では届かないため、無作為化後の投与期間を 52 週にした。主要評価は Week 48 のまま。

## 1.2 Trial Schema

```mermaid
flowchart LR
  S[Screening\n[TBD]] --> R1[Run-in Week 0\naflibercept 8 mg IVT]
  R1 --> R2[Run-in Week 4\naflibercept 8 mg IVT]
  R2 --> R3[Run-in Week 8\naflibercept 8 mg IVT]
  R3 --> RZ{Run-in Week 12\nResponse criteria met?\nRandomization 1:1 = Week 0}
  RZ -- No --> X[Not randomized\nscreen failure / off study treatment]
  RZ -- Yes --> A[Arm A: XYZ-123 0.5% QD eye drops\n+ sham injections\nWeek 0 to Week 52]
  RZ -- Yes --> B[Arm B: aflibercept 8 mg IVT\n8-16 weeks apart + vehicle drops\nWeek 0 to Week 52]
  A --> P[Primary timepoint: Week 48]
  B --> P
  P --> E[Week 52 End of Treatment\nWeek 56 Safety Follow-up]
```

Stratification factors: geographic region (US, EU, Japan) and baseline BCVA (<64 letters, ≥64 letters) [CTG:NCT04270747][DERIVED]. Allocation ratio 1:1 [USER]. Rescue aflibercept 8 mg may be given in either arm when the rescue criteria in Section 6.10 are met; a rescue is counted as an event in the primary analysis [DERIVED].

## 1.3 Schedule of Activities

The schedule has two parts. In both arms, participants attend visits every 4 weeks after randomization so that the masking of the different dosing routes and intervals is preserved [DERIVED]. Windows are given in the notes; windows that the source does not define are [TBD]. Safety events are collected through Week 56 [DERIVED].

**Table 1. Screening, run-in and Weeks 0 to 24**

| Procedure | Scr | RI-0 | RI-4 | RI-8 | Wk 0 (Rand.) | Wk 4 | Wk 8 | Wk 12 | Wk 16 | Wk 20 | Wk 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Informed consent | X | | | | | | | | | | |
| Eligibility (inclusion/exclusion) | X | X | | | X | | | | | | |
| Demographics, medical history | X | | | | | | | | | | |
| Vital signs, blood pressure | X | X | X | X | X | X | X | X | X | X | X |
| BCVA (ETDRS) | X | X | X | X | X | X | X | X | X | X | X |
| SD-OCT | X | X | X | X | X | X | X | X | X | X | X |
| Fundus photography / fluorescein angiography | X | | | | X | | | | | | |
| Intraocular pressure | X | X | X | X | X | X | X | X | X | X | X |
| Slit-lamp exam and fluorescein corneal staining | X | X | X | X | X | X | X | X | X | X | X |
| Dilated fundus examination | X | | | | X | | | | | | X |
| Ocular surface symptoms | X | X | | | X | X | X | X | X | X | X |
| Hematology, chemistry, urinalysis | X | | | | X | | | | X | | |
| Pregnancy test (WOCBP) | X | | | | X | | | | | | |
| AE and concomitant medications | X | X | X | X | X | X | X | X | X | X | X |
| Aflibercept 8 mg IVT (run-in) | | X | X | X | | | | | | | |
| Aflibercept 8 mg IVT or sham (masked schedule) | | | | | | See note 4 | See note 4 | See note 4 | See note 4 | See note 4 | See note 4 |
| XYZ-123 or vehicle eye drops: dispensing, diary review | | | | | X | X | X | X | X | X | X |
| Rescue assessment | | | | | | X | X | X | X | X | X |
| NEI VFQ-25 | | | | | X | | | X | | | X |
| Plasma PK sample | | | | | | | | X | | | X |
| ADA sample | | | | | | | | [TBD] | | | [TBD] |

**Table 2. Weeks 28 to 56**

| Procedure | Wk 28 | Wk 32 | Wk 36 | Wk 40 | Wk 44 | Wk 48 (primary) | Wk 52 (EOT) | Wk 56 (Follow-up) |
|---|---|---|---|---|---|---|---|---|
| Vital signs, blood pressure | X | X | X | X | X | X | X | X |
| BCVA (ETDRS) | X | X | X | X | X | X | X | X |
| SD-OCT | X | X | X | X | X | X | X | X |
| Fundus photography / fluorescein angiography | | | | | | X | X | |
| Intraocular pressure | X | X | X | X | X | X | X | X |
| Slit-lamp exam and fluorescein corneal staining | X | X | X | X | X | X | X | X |
| Dilated fundus examination | | | | | | X | X | |
| Ocular surface symptoms | X | X | X | X | X | X | X | X |
| Hematology, chemistry, urinalysis | | | | | | X | X | |
| AE and concomitant medications | X | X | X | X | X | X | X | X |
| Aflibercept 8 mg IVT or sham (masked schedule) | See note 4 | See note 4 | See note 4 | See note 4 | See note 4 | See note 4 | See note 4 | |
| XYZ-123 or vehicle eye drops: dispensing, diary review | X | X | X | X | X | X | X (last use) | |
| Rescue assessment | X | X | X | X | X | X | X | X |
| NEI VFQ-25 | | | | | | X | X | |
| Plasma PK sample | | | | | | X | X | |
| ADA sample | | | | | | [TBD] | [TBD] | |

**Notes.**
1. Abbreviations: Scr = screening; RI = run-in week; Rand. = randomization; EOT = End of Treatment; WOCBP = women of childbearing potential [DERIVED].
2. Run-in injections are given at Run-in Week 0, 4 and 8 with a window of ±7 days, as in the approved aflibercept 8 mg initiation regimen; randomization takes place at Run-in Week 12 (Week 0), 4 weeks after the third injection [USER][DERIVED].
3. The window for each post-randomization visit is [TBD]. Run-in visits have a window of ±7 days [USER].
4. At each visit the masked assessor applies the interval rule in Section 6.3. The unmasked injector then gives an aflibercept 8 mg injection (Arm B) or a sham procedure (Arm A) if the participant is due. Injections in Arm B are 8 to 16 weeks apart (±1 week) [USER][DERIVED].
5. The primary timepoint is Week 48 for P1, KS3, KS4, KS5, S1 and S2. KS1 and KS2 are assessed to Week 52. Safety events are collected through Week 56 [USER][DERIVED].
6. BCVA is always measured before pupil dilation and before any other procedure that could affect vision, by a masked, certified examiner [DERIVED].
7. Participants who discontinue randomized treatment should continue attending visits (Section 7.1) [PREC:Rani:s13/Q1i].
8. Rescue criteria, response criteria at Run-in Week 12 and the laboratory panel are [TBD] and are specified in Section 6.10, Section 5.2 and Section 12 [DERIVED].
# 2 INTRODUCTION

## 2.1 Purpose of Trial

The purpose of this trial is to determine whether XYZ-123 ophthalmic solution, used as maintenance therapy after aflibercept induction, is non-inferior to continued aflibercept 8 mg intravitreal (IVT) injection in preventing loss of visual acuity in participants with neovascular age-related macular degeneration (nAMD) [USER][DERIVED]. Current anti-VEGF treatment of nAMD requires repeated IVT injections. Each injection carries procedure-related risks and each visit places a burden on participants, caregivers and clinics; undertreatment in routine care is a recognized reason for vision loss [DERIVED]. A topical maintenance therapy that keeps vision after a successful induction would offer a non-invasive alternative [USER:P2-release].

The trial also characterizes the safety of 52 weeks of continuous topical XYZ-123 exposure, with attention to the ocular surface, so that the safety database meets the exposure recommended by ICH E1 for a long-term treatment of a non-life-threatening condition [STD][DERIVED].

> 【設計変更コメント D2】ICH E1 が求める長期曝露（1 年・100 例以上）を満たすため、入力の 44 週を 52 週に変更した。

## 2.2 Assessment of Risks and Benefits

**Disease background.** nAMD is characterized by active choroidal neovascularization (CNV) with intraretinal fluid (IRF) and/or subretinal fluid (SRF) that affects the central macula; untreated, it leads to loss of central vision. The disease affects older adults, and the registration trials in nAMD enrolled participants aged 50 years or older [CTG:NCT04423718][CTG:NCT02307682][PACK:neovascular_amd]. Anti-VEGF IVT injections are the standard of care. The approved aflibercept 8 mg regimen consists of three initial injections about 4 weeks apart (±7 days) followed by an injection once every 8 to 16 weeks (±1 week), and some participants may need to return to 4-week dosing [PRIOR:aflibercept 8 mg US prescribing information, accessed 2026-10-04].

**Product mechanism and prior data.** XYZ-123 is a VEGFR inhibitor formulated as an ophthalmic solution for topical use [USER]. Nonclinical and early clinical data are in the Investigator's Brochure [TBD:IB]. In the Phase 2 study, participants who responded to aflibercept IVT induction were randomized to XYZ-123 0.5% QD, 2.0% QD or 2.0% BID [USER:P2-release]. The proportion of participants without a BCVA loss of 15 letters or more or rescue therapy was about 65% to 69% in all groups. The incidence of the composite event at Week 52 was 31.8% (0.5% QD), 34.9% (2.0% QD) and 31.1% (2.0% BID); Kaplan-Meier analysis showed that about 62% to 67% had no event from Week 8 to Week 52. In participants who completed the study, mean BCVA and central subfield thickness (CST) were generally maintained. The primary comparison, high dose versus low dose, did not show a statistically significant difference [USER:P2-release]. The study had no control group and showed no dose response, so these results do not show that XYZ-123 is active; this trial is designed to answer that question against an active comparator [USER:P2-release][DERIVED].

**Known and potential risks.**

| Risk | Basis | Mitigation in this trial |
|---|---|---|
| Dry eye and punctate keratitis | Seen in some participants in the Phase 2 study [USER:P2-release] | Slit-lamp and fluorescein corneal staining at every visit; adverse event of special interest; rules for interruption (Section 6.4) |
| Increased blood pressure (systemic VEGF inhibition) | Concern from systemic VEGF inhibition; no clinically important trend in Phase 2 [USER:P2-release] | Blood pressure at every visit; adverse event of special interest [DERIVED] |
| IVT injection and sham procedure: endophthalmitis, retinal detachment, increased intraocular pressure, thromboembolic events | Events of interest in a comparable aflibercept trial [CTG:NCT04270747] | Aseptic technique, intraocular pressure checks, training of unmasked injectors [DERIVED] |
| Loss of vision from randomization to a treatment of unproven activity | Phase 2 had no control; composite event rate 31.1% to 34.9% [USER:P2-release] | Visits every 4 weeks, masked rescue criteria, aflibercept 8 mg rescue, Data Monitoring Committee review (Section 11) [DERIVED] |
| Systemic exposure and ocular toxicity not yet characterized at 52 weeks | No long-term data | Plasma PK samples; ocular safety assessments [TBD:IB] |

**Potential benefits.** Participants in both arms receive the approved induction regimen and close monitoring. Participants in Arm A may keep their vision with eye drops and fewer injections if XYZ-123 is effective; benefit is not established [DERIVED].

**Overall benefit-risk conclusion.** The risks are acceptable for participants who respond to induction because they are monitored every 4 weeks, can receive rescue aflibercept 8 mg, and the study includes safeguards for the ocular surface and blood pressure. Whether the benefit-risk balance is acceptable to regulators depends on the efficacy of XYZ-123 versus the active comparator, which this trial will determine [DERIVED].
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
# 4 TRIAL DESIGN

## 4.1 Description of Trial Design

| Element | Description |
|---|---|
| Phase | 3 [USER] |
| Design | Randomized, double-masked (double-dummy), active-controlled, parallel-group, non-inferiority; maintenance therapy after aflibercept induction [USER][DERIVED] |
| Allocation ratio | 1:1 [USER] |
| Stratification | Geographic region (US, EU, Japan); baseline BCVA (<64 letters, ≥64 letters) [CTG:NCT04270747][DERIVED] |
| Masking | Double-masked. Participants, investigators, masked examiners and the masked disease activity assessor do not know the arm; unmasked injectors perform all injections and sham procedures [DERIVED][PREC:Brolu:s20/Q13] |
| Arms | Arm A: XYZ-123 0.5% QD eye drops plus sham procedures. Arm B: aflibercept 8 mg IVT plus vehicle eye drops [USER][USER:P2-release] |
| Periods | Screening [TBD]; run-in 12 weeks (aflibercept 8 mg at Run-in Weeks 0, 4 and 8, each ±7 days); randomization at Run-in Week 12 (Week 0); randomized treatment 52 weeks; primary timepoint Week 48; safety follow-up visit Week 56 [USER][DERIVED] |
| Countries | US, EU and Japan [USER]; the number of sites is [TBD] |
| Participants | At least 668 randomized (334 per arm); the number entering the run-in is [TBD] (Section 10.11) [DERIVED] |
| Oversight | Independent Data Monitoring Committee [STD]; no interim efficacy analysis is planned (Section 10.9) [DERIVED] |

In the run-in, all participants receive three aflibercept 8 mg injections. At Run-in Week 12, the investigator confirms the response criteria (Section 5.2) using the masked reading of the SD-OCT and BCVA data, and eligible participants are randomized in the interactive response technology (IRT) system. After randomization, participants attend every 4 weeks. At each visit a masked assessor applies the interval rule that decides whether an aflibercept injection is due in Arm B; an unmasked injector gives the injection (Arm B) or the matching sham procedure (Arm A). Participants in both arms use eye drops at the same frequency, XYZ-123 in Arm A and vehicle in Arm B [DERIVED][USER].

> 【設計変更コメント D1・D6・D7】導入期、ダブルダミー（sham 注射とビヒクル点眼）、4 週ごとの来院は、入力の設計に補った。盲検化の手段は先例が条件つきで認めている sham 手技に基づく [PREC:Brolu:s20/Q13]。間隔決定の規則は [TBD]。

## 4.2 Rationale for Trial Design

**Control.** Aflibercept 8 mg IVT is the active comparator because it is the standard of care that represents the maintenance effect to be matched, and its regimen of three initial injections followed by injections every 8 to 16 weeks (±1 week) is the approved regimen in the US [USER][PRIOR:aflibercept 8 mg US prescribing information, accessed 2026-10-04]. The approval status and availability of aflibercept 8 mg in the EU and Japan are [TBD]. Where aflibercept 8 mg is not approved for use, the sponsor and regulators agree a locally approved aflibercept comparator before the site is opened [DERIVED]. A placebo-only maintenance arm is not used because participants with nAMD who lose vision may have irreversible damage [DERIVED].

> 【設計変更コメント D12】aflibercept 8 mg の日本での承認・入手状況を未確認。承認条件に合わなければ対照薬を変更する。

**Duration.** Treatment lasts 52 weeks after randomization so that participants exposed to XYZ-123 reach a full year of exposure, as ICH E1 recommends for long-term treatment of a non-life-threatening condition (at least 100 participants exposed for one year) [STD]. The primary endpoint is assessed at Week 48, about 11 months after randomization. In a precedent for a different nAMD product, the FDA stated that "the primary endpoint of change in BCVA from baseline should be at least 9 months after the treatment period" and accepted an average over Weeks 36, 40 and 44 [PREC:Rani:s13/Q1b][DERIVED]. The 48-week primary timepoint and the 52-week treatment period are derived from the input of 44 weeks of treatment and Week 48 [USER].

> 【設計変更コメント D2】入力は 44 週投与・Week 48 評価。ICH E1 の 1 年曝露を満たすため投与を 52 週にした。

**Endpoint.** The primary endpoint is a loss of 15 or more letters, a loss that the FDA considers clinically significant [PREC:Rani:s2/p4c]. It is analyzed as a proportion with rescue counted as an event, which matches the primary composite endpoint of the Phase 2 study [USER:P2-release]. The commonly used primary endpoint in nAMD trials of aflibercept comparisons is the change in BCVA from baseline, analyzed with a 4-letter margin [CTG:NCT04423718][CTG:NCT02307682][CTG:NCT04005352]; that endpoint is a key secondary endpoint (KS3). The margin for the proportion difference is [TBD] and must be justified before the protocol is finalized [DERIVED].

**Population.** Participants who responded to induction are used because the Phase 2 study evaluated XYZ-123 as maintenance therapy in this population, and randomizing untreated participants to a topical agent of unproven activity would expose them to avoidable vision loss [USER:P2-release][DERIVED]. Participants are 50 years or older, as in the reference nAMD trials [CTG:NCT04423718].

**Patient input.** Patient input on the acceptability of eye drops versus injections and on the visit schedule is [TBD].

## 4.3 Access to Trial Intervention After End of Trial

Arrangements for access to XYZ-123 after the trial, and the treatment participants receive after Week 56 (return to standard anti-VEGF care, or an extension study), are [TBD]. Participants who complete Week 52 are treated according to local standard of care after the safety follow-up visit [DERIVED].

## 4.4 Start of Trial and End of Trial

The start of the trial is the date the first participant signs informed consent. The end of the trial is the date of the last visit of the last participant (Week 56 or early termination), including follow-up of ongoing adverse events of special interest [STD][DERIVED]. A participant is considered to have completed the trial when the Week 56 visit has been completed.
# 5 TRIAL POPULATION

## 5.1 Description of Trial Population and Rationale

The population is adults with neovascular age-related macular degeneration (nAMD), 50 years and older (Adult, Older Adult), who have not been treated for nAMD before the run-in and who responded to three aflibercept 8 mg induction injections [USER][USER:P2-release]. The population matches the participants of the reference nAMD trials in age and in the requirement for active choroidal neovascularization (CNV) with fluid [CTG:NCT04423718][CTG:NCT02307682][CTG:NCT04270747]. Participants must be able to use eye drops reliably, because the experimental treatment is topical [CTG:NCT06856577][DERIVED].

One eye, the study eye, is evaluated. If both eyes are eligible, the eye with the worse BCVA at Run-in Week 0 is the study eye; if the BCVA is equal, the investigator selects the study eye, with the right eye as the default. The fellow eye is observed for safety but is not randomized [DERIVED]. Participants from the US, the EU and Japan are enrolled [USER].

## 5.2 Inclusion Criteria

Participants must meet all of the following criteria at screening (and at Run-in Week 0 and randomization where stated):

1. The participant (or legally authorized representative where permitted by local law) has given written informed consent before any study-specific procedure [STD].
2. The participant is 50 years or older at screening [CTG:NCT04423718][CTG:NCT02307682][CTG:NCT04270747][USER].
3. Active subfoveal CNV secondary to nAMD, including juxtafoveal lesions that affect the fovea, in the study eye, confirmed by SD-OCT and fluorescein angiography or fundus photography read by the central reading center [CTG:NCT04423718][CTG:NCT04270747].
4. Total area of CNV (classic and occult components) comprises more than 50% of the total lesion area in the study eye [CTG:NCT04423718].
5. Intraretinal fluid (IRF) and/or subretinal fluid (SRF) affects the central subfield of the study eye on SD-OCT at screening [CTG:NCT04423718][CTG:NCT04005352].
6. The participant has not received any treatment for nAMD in the study eye before the first run-in injection [CTG:NCT04423718][CTG:NCT04005352].
7. BCVA ETDRS letter score in the study eye is within a range that is [TBD] at screening and at Run-in Week 0; the ranges used in reference trials were 78 to 24, 78 to 23, 73 to 34 and 83 to 38 letters, and the lower and upper limits are set so that a loss of 15 letters can be measured [CTG:NCT04423718][CTG:NCT02307682][CTG:NCT04270747][CTG:NCT04005352].
8. The decrease in BCVA is determined by the investigator to be primarily the result of nAMD in the study eye [CTG:NCT04423718].
9. At Run-in Week 12 the participant has responded to the three aflibercept 8 mg injections, defined by criteria for BCVA and for IRF, SRF and CST on SD-OCT that are [TBD] and that are confirmed by the central reading center before randomization [USER:P2-release][TBD].
10. The participant is able to use eye drops reliably according to the protocol, shown by correct instillation at a run-in demonstration and by a diary completion rate of at least a threshold that is [TBD] [CTG:NCT06856577][DERIVED].
11. Contraception by men or women of childbearing potential is consistent with local regulations on highly effective contraception for participants in clinical studies [CTG:NCT04423718].

> 【設計変更コメント D1】基準 9（導入への反応）はリリースが「導入期間で良好な反応を示した患者」とだけ述べ、基準を示していないため [TBD]。基準 7 の BCVA の範囲は参照試験で割れており、既定値を置いていない。

## 5.3 Exclusion Criteria

**Table 5.3-1. Exclusion criteria**

| # | Category | Criterion | Source |
|---|---|---|---|
| 1 | Study eye: disease | Causes of CNV other than nAMD, including pathologic myopia (spherical equivalent of 8 diopters or more negative or axial length of 25 mm or more), ocular histoplasmosis, angioid streaks, choroidal rupture or multifocal choroiditis | [CTG:NCT04423718][CTG:NCT04270747] |
| 2 | Study eye: disease | Scar, fibrosis or atrophy involving the central subfield or the center of the fovea | [CTG:NCT04423718][CTG:NCT04270747] |
| 3 | Study eye: disease | Retinal pigment epithelial tear or rip involving the macula | [CTG:NCT04423718] |
| 4 | Study eye: disease | Subretinal blood affecting the foveal center point and/or more than 50% of the lesion | [CTG:NCT02307682] |
| 5 | Study eye: disease | Vitreous hemorrhage within 4 weeks before randomization, or current vitreous hemorrhage | [CTG:NCT02307682][CTG:NCT04270747] |
| 6 | Study eye: disease | Uncontrolled glaucoma, defined as intraocular pressure (IOP) above 25 mmHg despite anti-glaucoma medication | [CTG:NCT04423718] |
| 7 | Either eye: disease | History of idiopathic or autoimmune uveitis or other intraocular inflammation | [CTG:NCT04423718][CTG:NCT06856577] |
| 8 | Either eye: infection | Active or suspected ocular or periocular infection or inflammation, including infectious blepharitis, keratitis, scleritis or conjunctivitis, at screening, run-in or randomization | [CTG:NCT04423718][CTG:NCT04270747] |
| 9 | Either eye: disease | Diabetic retinopathy, diabetic macular edema or any retinal vascular disease other than nAMD | [CTG:NCT04423718] |
| 10 | Study eye: history | Prior vitrectomy, macular laser or photodynamic therapy, or history of retinal detachment | [CTG:NCT04270747][CTG:NCT06856577] |
| 11 | Study eye: surgery | Intraocular or periocular surgery within 3 months before randomization | [CTG:NCT04270747] |
| 12 | Study eye: media | Significant media opacity, including cataract, that could interfere with BCVA or imaging | [CTG:NCT04270747] |
| 13 | Ocular surface | Moderate to severe dry eye disease, punctate keratitis, corneal disease (dystrophy or transplant) or other ocular surface disorder that could confound the evaluation of XYZ-123 safety, defined by criteria that are [TBD] | [DERIVED][USER:P2-release] |
| 14 | Ocular surface | Use of contact lenses or of topical ocular medications that cannot be stopped for the duration of the study | [DERIVED] |
| 15 | Systemic: cardiovascular | Uncontrolled blood pressure, defined as systolic above 160 mmHg or diastolic above 95 mmHg | [CTG:NCT04423718] |
| 16 | Systemic: cardiovascular | Stroke or myocardial infarction within 6 months before Run-in Week 0 | [CTG:NCT04005352][CTG:NCT06856577] |
| 17 | Systemic: therapy | Systemic anti-VEGF therapy at any time | [CTG:NCT04005352][CTG:NCT04270747] |
| 18 | Systemic: infection | Active infection for which systemic anti-infectives were used within 4 weeks before randomization, or recurrent or chronic infection that could make the study detrimental | [CTG:NCT04270747] |
| 19 | Systemic: malignancy | Malignancy within 5 years, except treated and cured cutaneous squamous or basal cell carcinoma, in situ cervical cancer or in situ breast ductal carcinoma | [CTG:NCT04270747] |
| 20 | Systemic: disease | Uncontrolled, clinically significant systemic disease such as diabetes mellitus, hypertension, heart failure of NYHA class III or IV, renal disease or liver disease | [CTG:NCT04270747] |
| 21 | Systemic: immune | Systemic immunosuppressive drugs within 90 days before screening (short oral corticosteroid courses and inhaled, nasal or dermal steroids are permitted) | [CTG:NCT06856577] |
| 22 | Systemic: bleeding | History of ongoing bleeding disorder (aspirin and anticoagulants are permitted) | [CTG:NCT06856577] |
| 23 | Pregnancy | Pregnant or breastfeeding women, or women who plan to become pregnant during the study | [CTG:NCT04270747][CTG:NCT06856577] |
| 24 | Allergy | Hypersensitivity to aflibercept, XYZ-123 or any excipient, or to fluorescein, anesthesia or antiseptic used in study procedures | [CTG:NCT04270747] |
| 25 | Other trials | Other investigational drug or device within 30 days or 5 half-lives, whichever is longer, before screening | [CTG:NCT04270747] |
| 26 | Prior nAMD therapy | Any prior treatment for nAMD in the study eye before the first run-in injection; anti-VEGF or other treatment for nAMD in the fellow eye within 30 days before Run-in Week 0 | [CTG:NCT04423718][CTG:NCT04270747] |
| 27 | Compliance | Participant is unlikely to complete all study visits or to follow the study procedures, including the eye-drop diary | [CTG:NCT04270747] |
| 28 | Other | Any other condition that, in the opinion of the investigator, would pose a risk to participant safety or interfere with the study evaluation | [CTG:NCT04270747] |

**Table 5.3-2. Prior therapy and washout**

| Therapy | Washout before Run-in Week 0 / randomization | Source |
|---|---|---|
| Any anti-VEGF or other treatment for nAMD in the study eye | Not permitted at any time before the run-in | [CTG:NCT04423718] |
| Systemic anti-VEGF therapy | Not permitted at any time | [CTG:NCT04270747] |
| Intravitreal therapy (including corticosteroids), either eye | 4 weeks; long-acting steroids 3 months | [CTG:NCT04270747] |
| Intraocular or periocular surgery, study eye | 3 months | [CTG:NCT04270747] |
| Systemic immunosuppressive drugs | 90 days | [CTG:NCT06856577] |
| Other investigational product | 30 days or 5 half-lives, whichever is longer | [CTG:NCT04270747] |
| Anti-VEGF in the fellow eye | 30 days | [CTG:NCT04270747] |
| Topical ocular medications for dry eye or glaucoma | [TBD] | [DERIVED] |

> 【設計変更コメント D11】基準 13・14 は、リリースの第 2 相でドライアイと点状角膜炎が一部の患者で見られたことから加えた。判定基準は [TBD]。

## 5.4 Lifestyle Considerations

Participants must not wear contact lenses while using the eye drops, and they should not use other eye drops in the study eye except those permitted in Section 6.10. Participants are advised not to drive or operate machinery until vision has recovered after pupil dilation or an injection procedure. Participants report any new ocular symptoms promptly [DERIVED].

## 5.5 Screen Failures

A screen failure is a participant who signs consent but is not randomized. Participants who do not meet the response criteria at Run-in Week 12 are run-in failures; they leave the study and are managed with standard anti-VEGF care, and their data up to that point are recorded. Rescreening of participants who failed a screening criterion that can change, such as a transient infection, is allowed once with sponsor approval; the number of allowed rescreens and the minimum interval are [TBD] [DERIVED][TBD].
# 6 TRIAL INTERVENTION AND CONCOMITANT THERAPY

## 6.1 Description of Investigational Trial Intervention

| Product | Description | Source |
|---|---|---|
| XYZ-123 ophthalmic solution | A vascular endothelial growth factor receptor (VEGFR) inhibitor formulated as an eye drop; strength 0.5% [dose provisional, Section 6.2]; formulation, excipients, container, labeling and shelf life are [TBD:CMC] | [USER][USER:P2-release] |
| Vehicle ophthalmic solution | Matching eye drop without active ingredient, in an identical container and with the same appearance, odor and instillation frequency | [DERIVED] |
| Aflibercept 8 mg injection | Aflibercept 8 mg (0.07 mL of a 114.3 mg/mL solution) for IVT injection | [USER][PRIOR:aflibercept 8 mg US prescribing information, accessed 2026-10-04] |
| Sham procedure | Procedure that mimics an IVT injection without penetrating the eye, with the same anesthetic and antiseptic preparation, performed by the unmasked injector | [DERIVED][PREC:Brolu:s20/Q13] |

All participants receive aflibercept 8 mg during the run-in. The run-in injections are supplied by the sponsor as part of the study and are described in Section 6.9 [DERIVED].

## 6.2 Rationale for Investigational Trial Intervention Dose and Regimen

In the Phase 2 study, participants were randomized to XYZ-123 0.5% QD, 2.0% QD or 2.0% BID for 52 weeks. The composite event incidence at Week 52 was 31.8%, 34.9% and 31.1%, respectively, and the high dose (2.0% BID) did not show a statistically significant difference from the low dose; no dose response was seen. All doses up to 2.0% BID were generally well tolerated, and dry eye and punctate keratitis occurred in some participants [USER:P2-release]. This Phase 3 study uses one XYZ-123 dose. The provisional dose is 0.5% QD, the lowest dose tested, because a lower dose gives the lowest ocular surface exposure and simplest regimen when the Phase 2 data show no efficacy advantage of higher doses [DERIVED]. This dose is [TBD] until the sponsor confirms it, using the Phase 2 safety data by dose and a discussion with regulators at the End-of-Phase 2 meeting [TBD].

> 【設計変更コメント D5】入力に用量がなかったため、第 2 相の最小用量 0.5% QD を暫定にした。★ 注意点が 2 つある。(1) 第 2 相に対照群がなく、用量反応性がないことは「全用量で同程度に有効」だけでなく「いずれも不活性」の可能性を排除できない。(2) リリースの効果の段落は低用量を「0.05%QD」と書き、試験概要と結果の段落は 0.5% QD と書いている。後者を採ったが、元の資料で確認すること。

A precedent for another nAMD product records that the FDA recommended studying at least two doses for at least 9 months to select the Phase 3 dose; the XYZ-123 Phase 2 study evaluated three dose levels for 52 weeks [PREC:Brolu:s20/Q8][USER:P2-release]. The regimen of aflibercept 8 mg is the approved regimen: three injections 4 weeks apart (±7 days), then an injection every 8 to 16 weeks (±1 week) [USER][PRIOR:aflibercept 8 mg US prescribing information, accessed 2026-10-04].

## 6.3 Investigational Trial Intervention Administration

**Eye drops (XYZ-123 or vehicle).** Participants instill one drop in the study eye once daily (QD), at about the same time each day, from the day of randomization through Week 52 [USER:P2-release][DERIVED]. The first drop is given at the Week 0 visit under the supervision of study staff, who check the technique. Participants record each instillation in a diary, and staff review the diary at each visit. If a dose is missed, the participant does not instill a double dose; the participant instills the next scheduled dose and records the missed dose. If a participant forgets the dose for most of a day, no make-up dose is taken [DERIVED].

**Aflibercept 8 mg and sham (unmasked injector).** At each visit, the masked assessor records the disease activity findings and applies the interval rule: in Arm B the first maintenance interval and each later interval is 8 to 16 weeks (±1 week) and is shortened or extended according to visual and anatomic findings under rules that are [TBD] [USER][TBD]. The masked assessor notifies the unmasked injector only that an injection procedure is due, not the reason. The unmasked injector gives the aflibercept 8 mg injection in Arm B or the matching sham procedure in Arm A, using the same preparation and anesthesia. Injections are performed under aseptic conditions, in accordance with the approved labeling [DERIVED][PREC:Brolu:s20/Q13].

**Post-dose monitoring.** After each injection or sham procedure, the unmasked injector or a designated unmasked staff member checks that the participant can count fingers and that the optic nerve head is perfused, and measures intraocular pressure (IOP) when the injector judges it necessary. Participants are told to call the site immediately if they have eye pain, redness, loss of vision or light sensitivity in the days after the procedure [DERIVED].

## 6.4 Investigational Trial Intervention Dose Modification

The XYZ-123 dose is not adjusted. Treatment may be interrupted and resumed or permanently discontinued according to the table below. Interruptions do not change the randomized arm and participants continue all visits [PREC:Rani:s13/Q1i][DERIVED].

| Event | Action with XYZ-123 or vehicle drops | Source |
|---|---|---|
| Dry eye or punctate keratitis of moderate severity or the severity grade that is [TBD] | Interrupt eye drops; treat with permitted lubricants; resume when the event improves to grade [TBD] | [USER:P2-release][DERIVED][TBD] |
| Dry eye or punctate keratitis that does not resolve within a period that is [TBD] after interruption, or severe corneal findings | Permanently discontinue randomized drops; continue visits | [DERIVED][TBD] |
| Ocular infection in the study eye | Interrupt until the infection is treated and resolved | [DERIVED] |
| Blood pressure above the limit that is [TBD] on repeated measurement | Refer for medical care; investigator decides on interruption | [USER:P2-release][DERIVED] |
| Pregnancy | Permanently discontinue drops; follow Section 9 | [STD] |
| Serious allergic reaction | Permanently discontinue randomized treatment | [STD] |

## 6.5 Management of Investigational Trial Intervention Overdose

An overdose is the instillation of more than the scheduled number of drops, or an IVT injection of a volume higher than 8 mg (0.07 mL). There is no specific antidote. For topical overdose, the participant rinses the eye with water, and the investigator assesses the ocular surface. For an IVT overdose, IOP is monitored and treated as needed. The investigator records any overdose as an adverse event of special interest, whether or not there are symptoms, and reports it to the sponsor within 24 hours of awareness [STD][DERIVED].

## 6.6 Preparation, Storage, Handling and Accountability

Preparation, storage conditions, stability, packaging, labeling, dispensing and return of XYZ-123 and vehicle, and the handling of aflibercept 8 mg by the unmasked pharmacist, are described in the pharmacy manual [TBD:pharmacy manual]. The investigator or designee keeps drug accountability records for every bottle dispensed and returned, including dates, quantities, lot numbers and weights where applicable, and the unmasked monitor reconciles them at each monitoring visit [STD].

## 6.7 Investigational Trial Intervention Assignment, Randomisation and Blinding

**Assignment.** Eligible participants are randomized 1:1 at Run-in Week 12 (Week 0) through an interactive response technology (IRT) system, stratified by region (US, EU, Japan) and baseline BCVA (<64 letters, ≥64 letters) [USER][CTG:NCT04270747][DERIVED]. The randomization list uses permuted blocks within strata and is held by the IRT vendor [STD].

**Blinding method.** The study is double-masked and double-dummy. Arm A uses XYZ-123 drops and sham procedures. Arm B uses vehicle drops and aflibercept 8 mg injections. All other staff and participants are masked to the arm [DERIVED].

**Who is unmasked.** The unmasked injector and the unmasked pharmacist or drug manager and the unmasked monitor are unmasked. They do not take part in assessments or the interval decision. The IRT vendor and the independent Data Monitoring Committee statistician may have access to unmasked data [DERIVED].

**Emergency unblinding.** The investigator may unblind a participant in the IRT only when knowledge of the treatment is needed for urgent medical management of a serious event; the investigator tries to contact the sponsor first when time permits, records the reason and date, and the sponsor is told of every unblinding. A participant whose arm is unmasked may stay in the study for safety follow-up [STD][DERIVED].

## 6.8 Investigational Trial Intervention Adherence

Adherence to eye drops is measured by the participant diary, review at each visit, and weighing or counting of returned containers where applicable. Adherence is reported by arm. Participants with adherence below a threshold that is [TBD] are retrained and the reason is recorded; adherence below the threshold is a protocol deviation that is reviewed before analysis [DERIVED][TBD]. Injections are given by the unmasked injector at the clinic, so adherence to injections is the receipt of each scheduled injection or sham procedure [DERIVED].

## 6.9 Description of Noninvestigational Trial Intervention

The run-in aflibercept 8 mg injections (Run-in Weeks 0, 4 and 8, each ±7 days) are noninvestigational background treatment that precedes randomization, and the rescue aflibercept 8 mg is a noninvestigational treatment. Ancillary medications used in procedures (topical anesthetic, antiseptic, pupil-dilating drops, fluorescein) are standard and are supplied by the site according to local practice [USER][DERIVED].

## 6.10 Concomitant Therapy

Concomitant medications and procedures from 30 days before screening through Week 56 are recorded with the name, dose, route, indication and dates [STD]. The following tables apply from randomization.

**Table 6.10-1. Prohibited therapy**

| Therapy | Action | Source |
|---|---|---|
| Any anti-VEGF, other pharmacologic or procedural treatment for nAMD in the study eye outside the masked schedule or rescue (including photodynamic therapy, laser photocoagulation, vitrectomy, intravitreal steroids) | Count as prohibited nAMD treatment; the event is a P1 event; the investigator decides on discontinuation of randomized treatment and the participant stays in the study | [CTG:NCT04423718][CTG:NCT04270747][DERIVED] |
| Systemic anti-VEGF therapy | Stop systemic therapy; permanent discontinuation of randomized drops if it cannot be stopped | [CTG:NCT04270747] |
| Other investigational products | Permanent discontinuation of randomized treatment | [CTG:NCT04270747] |
| Topical ocular medications in the study eye other than permitted lubricants and dilating drops (for example, topical steroids and glaucoma medications started after randomization) | Record; the investigator decides whether to interrupt; discuss with the medical monitor | [DERIVED] |

**Table 6.10-2. Non-recommended therapy**

| Therapy | Comment | Source |
|---|---|---|
| Anti-VEGF intravitreal treatment in the fellow eye | Allowed only when medically necessary; record; the sponsor assesses the effect on systemic exposure and masking | [DERIVED][TBD] |
| Systemic drugs that affect blood pressure or wound healing started after randomization | Record; use with caution | [DERIVED] |
| Contact lens wear | Not recommended while using the drops | [DERIVED] |

**Table 6.10-3. Rescue therapy**

| Rescue therapy | Randomized treatment | Estimand intercurrent event | Source |
|---|---|---|---|
| Aflibercept 8 mg IVT given outside the masked schedule when protocol-defined rescue criteria are met; in Arm B, an injection at an interval shorter than 8 weeks is also rescue | Continue randomized treatment and all visits [TBD] | Rescue therapy for nAMD (aflibercept 8 mg outside the masked schedule): composite, counted as an event | [DERIVED][PREC:Rani:s13/Q1f] |
| Other nAMD therapy in the study eye (other anti-VEGF, photodynamic therapy, vitrectomy) | Investigator decides; participant stays in the study [TBD] | Other prohibited nAMD treatment in the study eye: composite, counted as an event | [DERIVED] |

**Rescue criteria.** The masked assessor evaluates the rescue criteria at each visit. The criteria include a reduction of 15 letters or more in BCVA compared with the best BCVA, which the FDA accepted as a treatment failure in a precedent for another nAMD product, and anatomic criteria on SD-OCT that are [TBD] [PREC:Rani:s13/Q1f][TBD]. The reasons for rescue, the BCVA and SD-OCT findings that triggered it, and the dates are recorded on the case report form, and participants who receive rescue are followed through Week 56 [PREC:Rani:s13/Q1f][PREC:Rani:s13/Q1i].

> 【設計変更コメント D8】救済の基準・手順は入力になかった。先例（治療失敗＝最良 BCVA から 15 文字以上の低下、救済後も追跡）に合わせて枠を作り、解剖学的基準の数値は [TBD]。対照群（aflibercept）は間隔の決定が治療の一部なので、8 週未満の間隔の注射を救済とみなして群間の非対称を避けた。
# 7 PARTICIPANT DISCONTINUATION OF TRIAL INTERVENTION AND DISCONTINUATION OR WITHDRAWAL FROM TRIAL

Participants who discontinue randomized treatment are encouraged to stay in the study and to attend all scheduled visits through Week 56, so that efficacy and safety data are collected after the discontinuation and can be used under a treatment-policy strategy [PREC:Rani:s13/Q1i]. The investigator records the reason for every discontinuation in detail [PREC:Rani:s13/Q1i].

## 7.1 Discontinuation of Trial Intervention

Randomized treatment (XYZ-123 or vehicle drops, and aflibercept 8 mg or sham procedures) is discontinued permanently when any of the following occurs:

| Reason | Detail | Source |
|---|---|---|
| Adverse event | A new or worsening event, such as a corneal event that does not resolve with the interruption in Section 6.4, ocular infection with endophthalmitis, or a serious allergic reaction, for which continued treatment is not in the participant's interest | [DERIVED][STD] |
| Pregnancy | Confirmed pregnancy | [STD] |
| Prohibited therapy that cannot be stopped | Systemic anti-VEGF therapy or another investigational product | [CTG:NCT04270747] |
| Investigator or sponsor decision | In the interest of the participant | [STD] |
| Participant request to stop treatment | The participant may stop treatment at any time without giving a reason | [STD] |
| Lack of adherence | Persistent non-adherence that cannot be corrected after retraining | [DERIVED] |

Participants who stop treatment remain in the study. They attend an early discontinuation visit with the Week 52 assessments, then the planned visits through Week 56 when possible. If the participant cannot return, the investigator collects BCVA and safety information by the best available means and records the reason [PREC:Rani:s13/Q1i][DERIVED]. Participants who receive rescue therapy are not discontinued from the study; they continue to be followed (Section 6.10) [PREC:Rani:s13/Q1f]. After discontinuation, the participant is treated by the investigator with the standard of care, which may include anti-VEGF therapy, and these treatments are recorded as concomitant therapy; the events are handled under the intercurrent event strategies in Section 3 [DERIVED].

## 7.2 Participant Withdrawal from the Trial

A participant may withdraw consent for the trial at any time. The investigator asks the participant for the reason and whether data collection can continue in a limited way, for example a final safety visit or a survival and vital status check by public records where the law allows. Data collected before withdrawal are kept and used, as described in the informed consent form. Withdrawn participants are not replaced after randomization [STD][DERIVED]. An early termination visit is scheduled with the Week 52 assessments when the participant agrees.

## 7.3 Lost to Follow-Up

A participant is lost to follow-up when the participant cannot be reached for a scheduled visit and the site has made at least three documented attempts, including phone calls and a registered letter or equivalent, over a period of at least [TBD] weeks. The site records the attempts in the source documents. If the participant later returns, the investigator resumes visits as soon as possible [STD][DERIVED][TBD].
# 8 TRIAL ASSESSMENTS AND PROCEDURES

## 8.1 Trial Assessments and Procedures Considerations

All procedures follow the Schedule of Activities in Section 1.3. The following rules apply to every visit:

- The order of procedures at a visit is fixed to protect the measurements: (1) patient-reported questionnaire (NEI VFQ-25) when scheduled, (2) BCVA, (3) vital signs and blood pressure, (4) IOP, (5) slit-lamp examination and fluorescein corneal staining, (6) pupil dilation, (7) SD-OCT and imaging, (8) dilated fundus examination, (9) masked assessor evaluation of disease activity and rescue criteria, (10) injection or sham procedure by the unmasked injector, (11) eye-drop dispensing and diary review [DERIVED].
- The masked examiners (BCVA examiner, masked investigator, masked assessor) and the unmasked injector are different people. The BCVA examiner performs no other study task. The roles are recorded in the delegation log [DERIVED][PREC:Brolu:s20/Q13].
- Examiners are trained and certified before they assess participants, and their certification is kept in the investigator site file [DERIVED].
- Imaging (SD-OCT, fundus photography and fluorescein angiography) is sent to a central reading center, whose readers are masked to the arm and to the visit sequence where possible [DERIVED].
- The visit window for post-randomization visits is [TBD]. The run-in injections have a window of ±7 days [USER][TBD].
- Source documents for every assessment (BCVA sheets, imaging acquisition logs, diary review notes, injection and sham records) are kept at the site, and data are entered into the electronic case report form within a period that is [TBD] after the visit; unmasked injection records are stored separately from the masked source documents [DERIVED][TBD].
- Rescreening and unscheduled visits are recorded in the case report form. An unscheduled visit for a possible rescue event repeats BCVA, SD-OCT and the masked assessor evaluation [DERIVED].

## 8.2 Screening/Baseline Assessments and Procedures

**Screening.** After informed consent, the site performs the following within the screening window of [TBD] days: eligibility review; demographics and medical history, including ocular history and prior eye treatments; concomitant medication review; vital signs and blood pressure; BCVA with refraction; IOP; slit-lamp examination with fluorescein corneal staining; dilated fundus examination; SD-OCT; fundus photography and fluorescein angiography; blood and urine tests; pregnancy test for women of childbearing potential; and ocular surface symptom assessment. The central reading center confirms the imaging eligibility criteria (Section 5.2) before the first run-in injection [STD][CTG:NCT04270747][DERIVED].

**Run-in.** The participant receives aflibercept 8 mg at Run-in Weeks 0, 4 and 8 (each ±7 days) and has BCVA, SD-OCT, IOP, slit-lamp examination, vital signs and adverse event assessment at each visit. The study-eye selection and the eye-drop instillation demonstration take place at Run-in Week 0 [USER][DERIVED].

**Run-in Week 12 (randomization, Week 0).** Before randomization, the site repeats BCVA, SD-OCT, imaging, laboratory tests and the pregnancy test; the NEI VFQ-25 is completed; the central reading center confirms the response criteria in Section 5.2; the investigator confirms eligibility; and the baseline value for all efficacy analyses is the last assessment before the first dose of randomized treatment at Week 0 [DERIVED][TBD].

**Response confirmation at Run-in Week 12.** The site uploads the SD-OCT images, the BCVA data and the clinical findings to the central reading center, which returns a masked read of the fluid status and CST within a period that is [TBD]. The investigator reviews the BCVA and the read against the response criteria, and the sponsor's masked medical monitor adjudicates a disagreement. If the participant does not meet the criteria, the investigator treats the participant according to standard of care, and the participant is recorded as a run-in failure with the reason; only participants who meet the criteria are randomized [USER:P2-release][DERIVED][TBD].

**Eye-drop instillation training.** At Run-in Week 0 and again at Week 0, a staff member demonstrates the instillation technique, watches the participant instill a drop of saline, and provides written instructions and a diary. Participants who need help, such as those with tremor or limited vision, may be helped by a caregiver, who is also trained and recorded [DERIVED].

## 8.3 Efficacy Assessments and Procedures

**Best corrected visual acuity (BCVA).**

| Element | Specification |
|---|---|
| Instrument | Early Treatment Diabetic Retinopathy Study (ETDRS) visual acuity chart at 4 meters; version of the chart and refraction protocol [TBD: ETDRS BCVA chart/protocol version — checked 2026-10-04, not confirmed] [INSTR:ETDRS BCVA:2026-10-04] |
| Score | Number of letters read correctly, 0 (worst) to 100 (best) [CTG:NCT04423718] |
| Rater | Masked, certified BCVA examiner who performs no other study procedure; the same examiner is used at every visit where possible [DERIVED] |
| Conditions | Best refraction at screening and at each visit as defined in the manual, standardized room lighting and chart distance; before pupil dilation and before any procedure that could affect vision [DERIVED] |
| Baseline | BCVA at Week 0 (last assessment before the first dose of randomized treatment) [DERIVED] |
| Event used in the primary endpoint | Reduction of 15 or more letters from baseline at Week 48; a loss of 15 letters from baseline is regarded as clinically significant [USER][PREC:Rani:s2/p4c] |
| Best-BCVA event (S1) | Reduction of 15 letters or more compared with the best BCVA recorded before the visit [PREC:Rani:s13/Q1f] |
| Timepoints | Every visit (Table 1 and Table 2 in Section 1.3); primary timepoint Week 48 |
| Recording | Entered on the case report form with the chart, distance, refraction and examiner identification; the examiner reports a result that differs by 10 letters or more from the previous visit to the medical monitor for verification [DERIVED][TBD] |

**Spectral-domain optical coherence tomography (SD-OCT).** CST is the average thickness in the central 1 mm diameter subfield, measured by SD-OCT on the same type of device at each visit where possible [CTG:NCT04270747]. The central reading center grades intraretinal fluid (IRF), subretinal fluid (SRF) and sub-RPE fluid as present or absent in the central subfield, and reports CST in micrometers. Device models, scan protocol and the fluid grading manual are in the imaging manual [DERIVED][TBD:imaging manual].

**Fundus photography and fluorescein angiography.** The central reading center measures the CNV lesion and total lesion size at screening, Week 0, Week 48 and Week 52, and confirms the CNV percentage of the lesion for eligibility [CTG:NCT04423718][DERIVED].

**Masked assessment of disease activity and rescue.** At each post-randomization visit the masked assessor records visual, SD-OCT and clinical findings on a standard form, applies the interval rule (Arm B) and the rescue criteria (Section 6.10), and decides whether an injection or sham procedure is due and whether rescue is needed. Rules are [TBD] [DERIVED][TBD].

**BCVA procedure details.** Examiners test the study eye first and then the fellow eye, with the study eye tested at the same chart distance (4 meters) at every visit. If the participant cannot read at least 20 letters at 4 meters, the examiner repeats the test at 1 meter according to the manual and the score is calculated as the manual specifies. Letters are scored one by one and a letter is correct only when read correctly; the examiner stops the line when the participant misses all letters or the participant refuses to guess. The examiner enters the number of letters, the distance and the refraction on the case report form, and the sponsor's quality system compares the sphere and cylinder refraction between visits. A BCVA that cannot be measured because of a ocular or systemic condition is recorded as missing with a reason, and the participant is not assigned an imputed value by the site [DERIVED][TBD:BCVA manual].

**Derived efficacy variables.** The variables are derived from the case report form and the central reading center data as follows [DERIVED][USER].

| Variable | Derivation |
|---|---|
| P1 event | Participant has a BCVA at Week 48 that is 15 or more letters below the Week 0 baseline, or has received rescue therapy or other prohibited nAMD treatment in the study eye on or before Week 48 |
| S1 event | Participant has a BCVA at any visit before Week 48 or at Week 48 that is 15 or more letters below the best BCVA recorded at an earlier visit, or rescue therapy on or before Week 48 |
| KS1 event | Any BCVA loss of 15 or more letters from baseline, or rescue, from Week 8 through Week 52 |
| KS2 time | Days from randomization to the first event in KS1; participants without an event are censored at Week 52 or at the last BCVA assessment |
| KS3, KS4 | Value at the visit minus the Week 0 baseline; the visit window used for assignment is [TBD] |
| KS5 | Absence of both IRF and SRF in the central subfield by the central reading center at the visit |

The central reading center sends the imaging data transfer to the sponsor's data management group on the schedule set in the imaging manual. The central reading center and the investigator resolve discrepancies in a masked process; the investigator's local reading is used for medical care and the central reading is used for analysis [DERIVED].

**Patient-reported outcome: NEI VFQ-25.** The 25-item National Eye Institute Visual Function Questionnaire, version 2000 of RAND, is completed at Week 0, Week 12, Week 24, Week 48 and Week 52, before any other procedure, in the participant's language and with a standardized administration mode; the composite score is the average of the subscale scores, from 0 (worst) to 100 (best, no vision problems) [CTG:NCT04423718][INSTR:NEI VFQ-25:2026-10-04]. The questionnaire is not licensed for a fee but requires a credit line to RAND and the National Eye Institute in publications, and its translations are the responsibility of the sponsor [INSTR:NEI VFQ-25:2026-10-04][TBD].

**Eye-drop diary.** The participant records each instillation, missed dose and ocular symptom; site staff review it at each visit. A threshold for completeness is [TBD] [DERIVED][TBD].

## 8.4 Safety Assessments and Procedures

| Assessment | Timing | Method and records | Source |
|---|---|---|---|
| Adverse events | Every visit; spontaneous and by non-leading questions | Section 9 | [STD] |
| Vital signs and blood pressure | Every visit, seated after rest | Same cuff and arm; two readings; blood pressure is an adverse event of special interest because of systemic VEGF inhibition; values above the limit that is [TBD] are repeated | [USER:P2-release][DERIVED][TBD] |
| Intraocular pressure | Every visit; after an injection or sham procedure when needed | Same method at every visit; an increase to a level that is [TBD] triggers treatment | [CTG:NCT04270747][DERIVED][TBD] |
| Slit-lamp examination | Every visit | Eyelids, conjunctiva, cornea, anterior chamber, lens; anterior chamber cell and flare graded; findings reported for both eyes | [DERIVED] |
| Fluorescein corneal staining | Every visit | Corneal staining graded on a scale that is [TBD] by the masked investigator; punctate keratitis recorded as an adverse event of special interest | [USER:P2-release][TBD] |
| Ocular surface symptoms | Screening, Run-in Week 0, Week 0 and every visit | Symptom questionnaire [TBD: instrument and version not confirmed]; dry eye adverse events recorded | [USER:P2-release][TBD] |
| Dilated fundus examination | Screening, Week 0, Week 24, Week 48, Week 52 and as needed | Retinal detachment, tear, vitreous hemorrhage, vasculitis or occlusion | [CTG:NCT04270747][DERIVED] |
| Laboratory tests | Screening, Week 0, Week 16, Week 48 and Week 52 | Hematology, chemistry and urinalysis (Section 12) | [STD] |
| Pregnancy test | Screening and Week 0 for women of childbearing potential | Urine or serum test | [STD] |
| Post-injection check | After each injection or sham | Counting fingers and optic nerve perfusion; IOP when needed | [DERIVED] |

Events of interest for the injection procedure are endophthalmitis, retinal detachment, increased intraocular pressure and thromboembolic events [CTG:NCT04270747]. The investigator evaluates ocular findings in both eyes. A participant with a corneal finding is examined by the masked investigator within a period that is [TBD], and the medical monitor is told of any severe finding [DERIVED][TBD]. Safety findings are reviewed by the sponsor's safety physician and the Data Monitoring Committee (Section 11) [STD].

**Ocular examination elements.** At each visit the masked investigator examines both eyes and records: lids and lashes (blepharitis, chalazion), conjunctiva (hyperemia, discharge, follicles), cornea (staining, edema, infiltrates, epithelial defects), anterior chamber (cells and flare), lens (opacity, change since the previous visit), vitreous (cells, hemorrhage) and, after dilation when scheduled, the retina and optic nerve [DERIVED]. The ophthalmologist records the grading scale used for each sign and compares it with the previous visit. Any new corneal finding in the study eye is graded and photographed according to the manual when the site has the equipment [DERIVED][TBD].

**Intraocular pressure.** IOP is measured with the same type of tonometer at each visit by a masked examiner, and not at the same visit as the injection by the unmasked injector. After an injection or sham procedure, IOP is checked when the injector considers it necessary, such as when the participant reports pain or the optic nerve head is not perfused. The IOP level that requires treatment and the level that requires a call to the medical monitor are [TBD] [DERIVED][TBD].

**Blood pressure and vital signs.** The participant sits for 5 minutes, and two readings are taken 1 to 2 minutes apart with the same cuff size on the same arm; the average is recorded. Pulse, body temperature and weight are recorded at screening and Week 48 or Week 52 [DERIVED]. Participants with an elevated reading have it repeated after rest, and those who remain above the limit that is [TBD] are referred to their physician and the event is recorded as an AESI [USER:P2-release][TBD].

**Clinical laboratory tests.** The central laboratory analyses the tests listed in Section 12. The investigator reviews the results, records any clinically significant abnormal value as an AE, and repeats a value that is [TBD] outside the reference range. Results are reported to the site within a period that is [TBD] and are not shared with masked staff if they could reveal the arm (none are expected to do so) [STD][DERIVED].

**Safety review.** The sponsor's safety physician reviews AEs and SAEs on an ongoing basis, with special attention to the AESIs listed in Section 9. The independent Data Monitoring Committee reviews unmasked safety data by arm, including the number of participants with corneal events, blood pressure events and injection-related events, at the intervals set in its charter. Rules for pausing enrollment or treatment because of a safety signal, such as a higher than expected rate of corneal events or endophthalmitis, are in the charter and are [TBD] [STD][TBD].

**Physical examination.** A symptom-directed physical examination is done when clinically indicated and the findings are recorded as medical history or as an AE according to the timing [DERIVED].

## 8.5 Pharmacokinetics

Plasma samples for XYZ-123 are collected at Week 12, Week 24, Week 48 and Week 52, before the morning dose where possible, with the time of the last instillation recorded. The aim is to describe the systemic exposure from topical use over 52 weeks and to relate it to blood pressure and other systemic findings. The analyte list, sampling times relative to dose and the bioanalytical method are [TBD] [DERIVED][TBD]. The date and time of the last instillation before each sample and of the sample are recorded, and the samples are processed, frozen and shipped according to the laboratory manual. Plasma concentrations are summarized for Arm A only; samples from Arm B participants are collected to keep the masking and are analyzed only if the sponsor decides to test the vehicle for assay interference [DERIVED][TBD]. Because the participants are older adults who may use other medications, the concomitant therapy at each PK visit is recorded so that interactions can be reviewed [DERIVED].

## 8.6 Biomarkers / Immunogenicity

Anti-drug antibody (ADA) sampling for XYZ-123 depends on the molecule type and is [TBD]; the SoA marks the visits as [TBD]. A comparator-specific ADA assessment of aflibercept is not planned [DERIVED][TBD]. Biomarker samples are not collected unless the sponsor adds them by an amendment; imaging biomarkers are covered by the central reading center [DERIVED]. If the molecule type of XYZ-123 makes ADA testing relevant, the sampling visits, the assay and the handling of positive samples are described in the laboratory manual and the SoA marks are completed by an amendment before the first participant is randomized [TBD].
# 9 ADVERSE EVENTS, SERIOUS ADVERSE EVENTS, PRODUCT COMPLAINTS, PREGNANCY AND POSTPARTUM INFORMATION, AND SPECIAL SAFETY SITUATIONS

**Definition of an adverse event (AE).** An AE is any untoward medical occurrence associated with the use of an intervention in humans, whether or not it is considered intervention-related (21 CFR 312.32(a)). In this trial an AE includes any untoward medical occurrence in a participant who has signed consent, from consent until the end of the safety collection period, including events related to the study procedures, the run-in aflibercept injections, the sham procedure and the vehicle [STD].

**Definition of a serious adverse event (SAE).** An AE or suspected adverse reaction is serious if, in the view of the investigator or the sponsor, it results in death, is life-threatening, requires inpatient hospitalization or prolongation of existing hospitalization, results in a persistent or significant incapacity or substantial disruption of the ability to conduct normal life functions, or is a congenital anomaly or birth defect. Important medical events that may not meet these criteria may be serious when, based on appropriate medical judgment, they may jeopardize the participant and may require medical or surgical intervention. For this trial, endophthalmitis, retinal detachment, and a loss of vision requiring an urgent medical or surgical procedure are considered important medical events and are assessed for seriousness by the investigator [STD][DERIVED].

**Study eye and fellow eye.** Every ocular AE is recorded with the eye affected: study eye, fellow eye or both eyes. Events in the study eye that are an efficacy outcome, such as a BCVA loss that meets the P1 definition or the need for rescue, are recorded as efficacy data and are reported as AEs only when they are serious or when the investigator considers them an AE (for example, a vision loss caused by endophthalmitis) [DERIVED].

**Severity.** The investigator grades each AE as mild (requires minimal or no treatment and does not interfere with daily activities), moderate (a low level of inconvenience or concern with the therapeutic measures; may cause some interference with functioning) or severe (interrupts the participant's usual daily activity and may require systemic drug therapy or other treatment). "Severe" is not the same as "serious" [STD]. Ocular surface findings are also graded on the corneal staining scale that is [TBD] [TBD].

**Causality.** The investigator assesses, for each AE, whether there is a reasonable possibility that XYZ-123 or vehicle drops, aflibercept 8 mg, the sham or injection procedure, or a study procedure caused it, using the categories related and not related, with the clinical reasoning recorded. The study product must always be considered a suspect. The assessment is made separately for each study treatment where the investigator can tell them apart; because the study is masked, the investigator assesses relatedness to "study treatment" and "injection procedure" [STD][DERIVED].

**Expectedness.** The sponsor determines whether a suspected adverse reaction is expected using the reference safety information in the Investigator's Brochure for XYZ-123 [TBD:IB] and the approved labeling for aflibercept 8 mg. An event is unexpected when its nature, severity or frequency is not consistent with that information [STD].

**Collection period and follow-up.** Non-serious AEs and SAEs are collected from the time of informed consent through the Week 56 visit (or 30 days after the last dose of randomized treatment if the participant discontinues early). SAEs and AESIs that start after this period and are considered related are reported when the investigator becomes aware of them. At each visit the investigator asks non-leading questions about AEs and examines the eyes. Medical conditions present at screening are medical history; they are recorded as AEs only if they worsen. Events are followed until resolution, stabilization, or the end of the study follow-up, and the investigator records onset, end, severity, relationship, action taken with treatment and outcome [STD][DERIVED].

**Reporting by the investigator.** The investigator reports every SAE, whether or not related to the study treatment, to the sponsor immediately and no later than 24 hours after becoming aware of it, using the SAE form. The report includes an assessment of whether there is a reasonable possibility that the drug caused the event (21 CFR 312.64(b)). AESIs are reported to the sponsor within 24 hours when they are serious and on the regular case report form when they are not [STD][DERIVED].

**Regulatory reporting by the sponsor.** The sponsor notifies the FDA and all participating investigators of potential serious risks, in an IND safety report, as soon as possible and no later than 15 calendar days after the sponsor determines that the information qualifies for reporting; unexpected fatal or life-threatening suspected adverse reactions are reported as soon as possible and no later than 7 calendar days after the sponsor's initial receipt of the information (21 CFR 312.32(c)). In the EU, suspected unexpected serious adverse reactions are reported according to the Clinical Trials Regulation, and in Japan according to the applicable PMDA requirements; country-specific timelines are in Section 12 [STD][TBD].

## Adverse events of special interest (AESI)

| AESI | Reason | Handling | Source |
|---|---|---|---|
| Dry eye | Seen in some participants in the Phase 2 study | Record severity, corneal staining and management; interruption rules in Section 6.4 | [USER:P2-release] |
| Punctate keratitis and other corneal findings | Seen in some participants in the Phase 2 study | Record corneal staining grade at each visit; slit-lamp findings; interruption rules in Section 6.4 | [USER:P2-release] |
| Increase in blood pressure or hypertension | Concern from systemic VEGF inhibition; no clinically important trend in Phase 2 | Measure blood pressure at each visit; refer for treatment above the limit that is [TBD] | [USER:P2-release][DERIVED][TBD] |
| Endophthalmitis | Risk of IVT injection and sham | Report as an SAE; urgent management | [CTG:NCT04270747] |
| Retinal detachment, retinal tear, vitreous hemorrhage | Risk of IVT injection | Report; dilated fundus examination | [CTG:NCT04270747] |
| Intraocular pressure increase | Risk of IVT injection | Measure IOP; treat above the level that is [TBD] | [CTG:NCT04270747][TBD] |
| Intraocular inflammation (including uveitis and retinal vasculitis) | Class effect of intravitreal anti-VEGF agents | Report; slit-lamp and fundus examination | [DERIVED] |
| Arterial thromboembolic events | Systemic VEGF inhibition | Report; adjudication by the Data Monitoring Committee when requested | [CTG:NCT04270747][DERIVED] |
| Overdose, medication error and misuse of the study treatment | Special safety situation | Report within 24 hours | [STD] |

## Clinical management of events of special interest

| Event | Participant instruction | Investigator action | Source |
|---|---|---|---|
| Dry eye, punctate keratitis | Report eye pain, redness, light sensitivity or blurred vision at once | Examine within a period that is [TBD]; grade corneal staining; treat with permitted lubricants; interrupt drops per Section 6.4; add visits as needed | [USER:P2-release][TBD] |
| Blood pressure increase | Report severe headache, chest pain or vision changes | Repeat and confirm; refer to physician; consider interruption of drops if the cause is thought to be study treatment | [DERIVED][TBD] |
| Pain, redness or vision loss after an injection or sham procedure | Call the site on the same day | Examine for endophthalmitis, IOP increase, retinal detachment; treat urgently; report as an SAE when criteria are met | [CTG:NCT04270747][DERIVED] |
| Signs of intraocular inflammation | Report floaters, pain, light sensitivity | Slit-lamp and fundus examination; treat per local standard; report | [DERIVED] |

## Disease-related events and efficacy outcomes

Loss of vision, retinal fluid, retinal hemorrhage and the need for additional anti-VEGF treatment are expected features of nAMD. Events that are the study efficacy outcomes (P1, KS1, S1 and rescue) are recorded in the efficacy data and are not reported as AEs unless they meet the SAE definition, the investigator suspects a relationship with the study treatment, or they are caused by another AE. This avoids double capture of events in both the efficacy and safety data [DERIVED].

## Safety oversight and reporting of events to participants

The sponsor's medical monitor reviews safety data in real time, and the independent Data Monitoring Committee reviews the cumulative data (Section 11). Participants are told of new safety information that may change their willingness to continue, and the informed consent form is updated by amendment, with re-consent when required by the IRB or ethics committee. Incidental findings in imaging, such as a retinal lesion, are reported to the investigator, who informs the participant and refers for care [STD][DERIVED].

## Unanticipated problems

An unanticipated problem is an incident, experience or outcome that is unexpected, related or possibly related to participation in the research, and suggests that the research places participants or others at greater risk than was previously known. The investigator reports such a problem to the sponsor and to the IRB or ethics committee according to local rules and timelines [STD][TBD].

## Product complaints

A product complaint is any report on the quality, labeling, packaging or performance of XYZ-123, vehicle or aflibercept 8 mg, including a leaking container or a failed dropper. The site reports a complaint to the sponsor within 1 business day, keeps the product when possible, and records an AE if there was one [STD][DERIVED].

## Pregnancy and postpartum information

The trial enrolls participants aged 50 years and older, so pregnancy is unlikely, but women of childbearing potential may participate when they meet Section 5.2. The investigator reports a pregnancy to the sponsor within 24 hours of awareness, stops randomized treatment, and follows the pregnancy to its outcome and the infant to a period that is [TBD] when the participant agrees; pregnancy is not an AE, but any complication or outcome meeting the SAE definition is reported as an SAE. Contraception requirements are in Section 12 [STD][CTG:NCT04423718][TBD].

## Other special safety situations

Misuse, abuse, medication errors, lack of efficacy that results in loss of vision, and occupational exposure are recorded as special situations and reported to the sponsor within 24 hours when they result in an AE. Unanticipated problems involving risks to participants or others are reported to the IRB or ethics committee according to local rules [STD].
# 10 STATISTICAL CONSIDERATIONS

## 10.1 General Considerations

The statistical analysis plan (SAP) is finalized and signed before the database lock and before unmasking, and it gives the details of the methods in this chapter. Analyses are done by arm as randomized unless stated. Continuous data are summarized by n, mean, standard deviation, median and range; categorical data by counts and percentages. The primary hypothesis is one-sided with a type I error of 0.025; confidence intervals for the primary comparison are one-sided 97.5% intervals, and other confidence intervals are two-sided 95% intervals unless stated [STD]. The study eye is the unit of analysis. The statistical software and version are in the SAP [TBD].

## 10.2 Analysis Sets

| Set | Definition | Use |
|---|---|---|
| Run-in set | All participants who receive at least one run-in aflibercept 8 mg injection | Run-in disposition and response rate |
| Randomized set | All participants randomized | Disposition |
| Full analysis set (FAS) | All randomized participants who receive at least one dose of randomized treatment (drops or injection/sham), analyzed as randomized | Primary analysis; all efficacy analyses |
| Per-protocol set (PPS) | FAS participants without major protocol deviations that could affect the P1 assessment (defined in the SAP before unmasking), including adherence to the eye-drop regimen at or above the threshold that is [TBD] | Primary analysis for non-inferiority |
| Safety set | All participants who receive at least one dose of randomized treatment, analyzed as treated | Safety analyses |
| PK set | Participants in Arm A with at least one evaluable plasma concentration | PK summaries |

Non-inferiority is concluded only if it is shown in both the FAS and the PPS, because an analysis that includes deviations can bias a non-inferiority comparison toward similarity [STD][DERIVED].

## 10.3 Analyses of Demographics and Other Baseline Variables

Demographics (age, sex, race, ethnicity, region), baseline BCVA and SD-OCT variables, CNV and lesion size, lesion type, time since nAMD diagnosis, run-in response measures, prior and concomitant therapy and medical history are summarized by arm for the randomized set and the FAS. No tests of baseline differences are done [DERIVED][STD].

## 10.4 Analyses Associated with the Primary Objective(s)

**Estimand.** The primary estimand is described in Section 3.1. The endpoint is: Reduction of 15 or more letters in BCVA (Best corrected visual acuity) as measured by ETDRS visual acuity chart from baseline Week 48. Rescue therapy and other prohibited nAMD treatment in the study eye by Week 48 are counted as events (composite strategy); permanent discontinuation of randomized treatment without rescue is handled with a treatment-policy strategy [USER][DERIVED].

**Hypotheses.** H0: the difference in event proportions (XYZ-123 minus aflibercept 8 mg) is greater than or equal to the non-inferiority margin δ. H1: the difference is less than δ. The margin δ is [TBD] and is justified before the SAP is finalized (Section 4.2) [DERIVED][TBD].

**Primary analysis.** The difference in the proportion of participants with the P1 event is estimated with a stratified Newcombe confidence interval using Mantel-Haenszel weights, with strata for region and baseline BCVA (<64, ≥64 letters). Non-inferiority is concluded if the upper bound of the one-sided 97.5% confidence interval is below δ. The analysis is done in the FAS and in the PPS [CTG:NCT04270747][STD]. Where a stratum is too small, strata are pooled using a rule given in the SAP before unmasking [DERIVED].

**Missing data.** A participant who has no BCVA at Week 48 and has no event before Week 48 is handled in the primary analysis by multiple imputation of the Week 48 BCVA within each arm, under the assumption that data are missing at random given baseline BCVA, region and the BCVA at earlier visits; the number of imputations, the imputation model and the random seed are specified in the SAP [PREC:Rani:s13/Q1i][DERIVED]. All reasons for early discontinuation are collected, and participants who stop treatment are followed so that most Week 48 values exist [PREC:Rani:s13/Q1i].

**Sensitivity analyses.**

1. Tipping-point analysis, in which the imputed events in Arm A are increased and those in Arm B are decreased until the conclusion changes [DERIVED].
2. Worst-case analysis, in which every participant with a missing Week 48 value and no event is counted as an event in Arm A and as no event in Arm B [DERIVED].
3. Analysis using BCVA values collected after rescue (treatment-policy strategy for rescue) [PREC:Rani:s13/Q1i].
4. Analysis in the PPS, and analysis using the best-BCVA definition of the event (S1) [DERIVED].
5. Analysis with a logistic regression model adjusted for the stratification factors, to give an adjusted risk difference [DERIVED].

**Supportive estimand.** A hypothetical estimand for rescue, in which a participant who receives rescue is analyzed as if rescue had not been available, is estimated by multiple imputation of the BCVA after rescue; this is supportive and is not used for the non-inferiority conclusion [CTG:NCT04423718][DERIVED].

> 【設計変更コメント D13】主要解析は参照試験の割合の解析（層別 Newcombe、MH 重み）を採った。マージン δ は [TBD]。

## 10.5 Analyses Associated with the Secondary Objective(s)

Secondary endpoints are analyzed in the FAS with the estimand attributes in Section 3.2.

| ID | Endpoint | Method |
|---|---|---|
| KS1 | Proportion of participants with a 15-letter or greater BCVA loss from baseline or rescue therapy at any time from Week 8 to Week 52 | Stratified Newcombe interval of the difference in proportions, as for P1 |
| KS2 | Time to first occurrence of a 15-letter or greater BCVA loss from baseline or rescue therapy through Week 52 | Kaplan-Meier estimates by arm; stratified log-rank test and stratified Cox model for the hazard ratio; participants without an event are censored at Week 52 or the last BCVA assessment |
| KS3 | Change from baseline in BCVA (ETDRS letters) at Week 48 | Mixed model for repeated measures on all post-baseline visits with treatment, visit, treatment-by-visit, baseline BCVA and the strata; supportive trimmed mean analysis for participants who receive rescue or discontinue because of an AE |
| KS4 | Change from baseline in central subfield thickness (CST) by SD-OCT at Week 48 | Same model as KS3 with baseline CST |
| KS5 | Proportion of participants with no intraretinal fluid and no subretinal fluid in the central subfield at Week 48 | Stratified Newcombe interval or Cochran-Mantel-Haenszel test; rescue counted as not dry |
| S1 | Proportion of participants with a reduction of 15 or more letters in BCVA compared with the best BCVA recorded before Week 48 or rescue therapy through Week 48 | As for P1 |
| S2 | Change from baseline in NEI VFQ-25 total score at Week 48 | ANCOVA with baseline score and strata; missing values handled by multiple imputation |

[CTG:NCT04423718][CTG:NCT04270747][PREC:Rani:s13/Q1i][PREC:Rani:s13/Q1f][USER:P2-release][DERIVED]

## 10.6 Analyses Associated with the Exploratory Objective(s)

Exploratory analyses are described in the SAP and are descriptive; no adjustment for multiplicity is made (Section 3.3) [DERIVED].

## 10.7 Safety Analyses

Safety is analyzed in the Safety set. The endpoint is: Ocular and non-ocular treatment-emergent adverse events, including dry eye and punctate keratitis. Treatment-emergent AEs are those that start or worsen at or after the first dose of randomized treatment; AEs in the run-in are listed separately. The analysis presents the number and percentage of participants and the number of events by system organ class and preferred term, by eye (study, fellow), severity and relationship, for SAEs, AEs leading to discontinuation and AESIs (corneal events, blood pressure events, injection-related events, intraocular inflammation and thromboembolic events). Exposure is summarized by days of use of XYZ-123 or vehicle and by the number of injections or sham procedures. Vital signs including blood pressure, IOP, corneal staining grades, laboratory values and shifts are summarized by visit. The number of participants with at least 52 weeks of exposure is reported against the exposure target in Section 10.11 [STD][USER:P2-release][DERIVED].

## 10.8 Other Analyses

Subgroup analyses of the primary endpoint are done by region (US, EU, Japan), baseline BCVA (<64, ≥64 letters), age (<75, ≥75 years), lesion type and run-in response measures; interactions are not tested, and the results are displayed in forest plots for consistency [CTG:NCT04270747][CTG:NCT02307682][DERIVED]. Results in Japanese participants are summarized separately to support the regional submission [TBD].

## 10.9 Interim Analyses

No interim analysis of efficacy is planned. The Data Monitoring Committee reviews safety data periodically. A blinded review of the pooled event rate may be done before the last participant is randomized to check the assumed event rate used for the sample size; any change in sample size is made without unmasking, according to a plan in the SAP and with notification to regulators [DERIVED][TBD].

## 10.10 Multiplicity Adjustments

The trial has a single primary non-inferiority hypothesis tested at a one-sided type I error of 0.025. If non-inferiority is concluded in both the FAS and the PPS, the key secondary endpoints are tested in the fixed order KS1, KS2, KS3, KS4, KS5 at the same one-sided 0.025 level, and testing stops at the first non-significant result. The hypothesis type and margin for each key secondary are in the SAP: for KS3 the margin is 4 letters, as in the reference nAMD trials, and for the others they are [TBD] [CTG:NCT04423718][CTG:NCT02307682][CTG:NCT04005352][DERIVED][TBD]. There is a single XYZ-123 dose, so no adjustment for multiple doses is needed. Other secondary and exploratory endpoints are not adjusted [STD].

## 10.11 Sample Size Determination

**Primary endpoint (non-inferiority on a risk difference).** The sample size depends on the proportion of participants with the P1 event in the aflibercept 8 mg arm, on the assumed difference, and on the margin δ. The assumed proportions come from published results of aflibercept 2 mg in comparable studies, because the proportion for 8 mg is not available in the registry results:

| Assumption | Value | Source |
|---|---|---|
| Control proportion with a loss of 15 letters or more at Week 48 | 5.6% | [PRIOR:CTG:NCT02307682 results, aflibercept 2 mg, accessed 2026-10-04] |
| Control proportion, alternative | 2.4% (100% minus 97.6% who maintained vision at Week 52) | [PRIOR:CTG:NCT04270747 results, accessed 2026-10-04][DERIVED] |
| Difference between arms | 0 (sensitivity table only) | [DERIVED] |
| Margin δ | [TBD] | [TBD] |
| One-sided alpha, power, dropout inflation | 0.025, 0.90, 10% | [STD][USER] |

**Sensitivity table.** Participants required (total, 1:1) for a non-inferiority test on the risk difference; the first number is the total before and the second after allowance for 10% dropout [DERIVED].

| Control proportion | Margin 4 points | 5 points | 6 points | 7 points | 8 points | 10 points |
|---|---|---|---|---|---|---|
| 2.4% | 616 / 685 | 394 / 438 | 274 / 305 | 202 / 225 | 154 / 172 | 100 / 112 |
| 5.6% | 1,390 / 1,545 | 890 / 989 | 618 / 687 | 454 / 505 | 348 / 387 | 224 / 249 |

**Safety exposure.** ICH E1 recommends that, for long-term treatment of a non-life-threatening condition, about 1,500 participants are exposed in the program, 300 to 600 for 6 months and at least 100 for a minimum of one year, at the intended dose [STD]. The FDA recommended in a precedent for another nAMD product that at least 300 participants complete 12 months of follow-up and that about 500 or more complete treatment at the proposed concentration and frequency [PREC:Rani:s13/Q3]. The trial allocates 300 participants completing 52 weeks of XYZ-123 at the Phase 3 dose; with 10% dropout this is 334 per arm and 668 in total at a 1:1 ratio. The remaining exposure, including the Phase 2 participants (different dose levels), is [TBD] [STD][DERIVED].

**Final sample size.** The final number is the largest of the components:

| Component | Total randomized |
|---|---|
| Primary non-inferiority (control 5.6%, margin 10 points) | 249 |
| Primary non-inferiority (control 5.6%, margin 7 points) | 505 |
| Safety exposure allocated to this trial | 668 |
| **Final (provisional lower bound)** | **668, driven by safety exposure** |

At 668 participants the study has 0.90 power for non-inferiority when the margin is about 7 points or larger with a 5.6% control proportion, and about 5 points or larger with a 2.4% control proportion, assuming no difference between arms. The final number is confirmed when the margin is agreed [DERIVED][TBD]. For comparison, the reference nAMD trials randomized 1,011, 1,775, 576, 734 and 311 participants [CTG:NCT04423718][CTG:NCT02307682][CTG:NCT04270747][CTG:NCT04005352][CTG:NCT06856577]. The number of participants who enter the run-in is [TBD] and depends on the proportion who respond to induction.

> 【設計変更コメント D4・D9】★ 上の感度表は「群間差なし」の仮定。リリースの第 2 相では XYZ-123 の複合事象率が 31.1〜34.9%（対照なし）で、対照の「15 文字以上の低下」の 2.4〜5.6% と事象の定義が異なる値だが、差が大きいと現実的なマージンでは非劣性を示せない。マージン、主要評価項目の型、デザインを EOP2 で協議し、統計担当が例数を確認すること。総例数 668 は安全性曝露（ICH E1・FDA 先例）で決まった暫定の下限。
# 11 TRIAL OVERSIGHT AND OTHER GENERAL CONSIDERATIONS

**Statement of compliance.** The trial is conducted in accordance with the protocol, the principles of the Declaration of Helsinki, ICH Good Clinical Practice (ICH E6(R3)), and applicable regulatory requirements: in the US, 21 CFR Parts 50, 54, 56, 312 and 11; in the EU, Regulation (EU) No 536/2014; in Japan, the Ministry of Health, Labour and Welfare GCP ordinance and related notifications [STD]. The sponsor and investigators follow the more stringent requirement where the sources differ [STD][DERIVED].

**Ethical review.** The protocol, the informed consent form, participant materials (including diary and questionnaire translations), recruitment materials and amendments are submitted to the IRB or independent ethics committee of each site or country, and the trial starts at a site only after written approval. Substantial amendments are not implemented before approval, except to remove an immediate hazard to participants [STD].

**Informed consent.** The investigator or a delegate explains the trial to the participant in language the participant understands, including that the participants first receive aflibercept 8 mg in the run-in, that randomization is possible only if they respond, that they may be assigned to an eye-drop treatment whose activity is not yet established, that they may receive sham procedures, that rescue treatment is available, and the risks described in Section 2.2. Because participants are 50 years or older and have impaired central vision, the consent form is provided in large print and read aloud when needed, and a witness signs when the participant cannot read it. The participant signs and dates the form before any study procedure, receives a copy, and may withdraw at any time without a penalty. New information that could change willingness to continue is given to participants, with re-consent when required [STD][DERIVED]. The consent form states how data and samples are used and how long they are kept [STD].

**Confidentiality and data protection.** Participants are identified by a coded number. Personal data are processed according to the applicable data protection laws, such as the General Data Protection Regulation in the EU, HIPAA in the US and the Act on the Protection of Personal Information in Japan. Source data, including images sent to the central reading center, are free of direct identifiers where possible. Monitors, auditors, IRBs and regulators may inspect source documents under confidentiality [STD][DERIVED].

**Future use of stored data and samples.** Plasma samples and imaging data are used for the objectives in this protocol. Use for other research needs separate consent where the law requires it; storage conditions and the duration are in the laboratory and imaging manuals [STD][TBD].

**Key roles and committees.**

| Body | Role | Source |
|---|---|---|
| Sponsor | Overall responsibility for trial conduct, quality, safety reporting and data | [STD][TBD:sponsor] |
| Coordinating investigator and steering committee | Scientific oversight and protocol advice | [DERIVED][TBD] |
| Independent Data Monitoring Committee (DMC) | Reviews unmasked safety data periodically, with attention to corneal events, blood pressure events and injection-related events, and recommends continuation, modification or stopping; the membership, meeting schedule and rules are in the DMC charter | [STD][TBD] |
| Central reading center | Masked grading of SD-OCT, fundus photography and fluorescein angiography | [DERIVED] |
| Unmasked injection and pharmacy staff | Prepare and administer injections and sham procedures and are separated from masked staff | [DERIVED][PREC:Brolu:s20/Q13] |
| Interactive response technology vendor | Randomization and drug supply | [STD] |
| Central laboratory | Safety laboratory tests and PK analysis | [STD] |
| Medical monitor and safety physician | Review of AEs, protocol questions, eligibility queries | [STD] |

**Safety oversight.** The sponsor's safety physician reviews AEs and SAEs continuously and sends safety reports to regulators and investigators as required (Section 9). The DMC reviews the data at the intervals in its charter and may request unmasked ocular and non-ocular safety summaries by arm [STD].

**Clinical monitoring.** The sponsor uses a risk-based monitoring plan: the critical data and processes are the P1 outcome (BCVA at Week 48 and rescue), masking, eligibility, eye-drop adherence, SAE reporting and consent. Monitors review source data against the case report form, with more intensive review of BCVA procedures and rescue decisions, and the plan describes triggers for added visits to a site. An unmasked monitor handles drug accountability and unmasked records [STD][DERIVED].

**Vendor oversight and training.** The sponsor keeps written agreements with the central laboratory, the central reading center, the interactive response technology vendor and the contract research organization, defines the tasks each performs, and reviews their performance and quality metrics at intervals set in the oversight plan. Investigators and site staff are trained on the protocol, on the masked and unmasked roles, on the BCVA procedure, on the eye-drop instruction and diary, on the sham procedure, and on adverse event and rescue reporting before they start, and the training is documented in the trial master file; staff who join later are trained before they perform study tasks [STD][DERIVED].

**Quality assurance and quality control.** The sponsor operates quality systems, audits sites and vendors, and keeps the audit reports. Investigators allow audits and inspections by the sponsor and regulators. Deviations from the protocol are recorded, and important deviations (for example in eligibility, in masking or in the BCVA procedure) are reported to the IRB when required. Corrective and preventive actions are documented [STD].

**Data handling and record keeping.** Data are collected in an electronic case report form with audit trails, and the sponsor holds the database. Imaging and ancillary data are transferred under data transfer agreements. The investigator keeps essential documents and source records for the period that the regulations require, and the sponsor tells the investigator when the records may be destroyed; the retention period is [TBD] and is not shorter than the legal minimum in each country [STD][TBD].

**Protocol deviations.** The investigator does not deviate from the protocol except to eliminate an immediate hazard to participants; any deviation is documented and reported to the sponsor. Major deviations are classified before unmasking according to the SAP and are used to define the per-protocol set [STD][DERIVED].

**Study discontinuation and closure.** The sponsor may stop the trial or a site for safety, regulatory, quality or operational reasons, with notice to the IRBs, regulators and investigators. Participants are told and are given alternative treatment, and the investigator ensures their follow-up care [STD].

**Publication, registration and data sharing.** The trial is registered in public registries before the first participant is enrolled (ClinicalTrials.gov; the EU clinical trials information system; jRCT in Japan), and results are posted within the required time. The sponsor publishes the results regardless of the outcome, and the investigators follow the sponsor's publication policy. Participant-level data sharing is according to the sponsor's policy [STD][TBD].

**Financial disclosure and conflict of interest.** Investigators and subinvestigators disclose financial interests as required by regulation (21 CFR Part 54 in the US), and the disclosures are updated during the trial and for one year after its completion [STD].

**Insurance and compensation.** Insurance for participants and compensation for study-related injury are provided as required by the law of each country and are described in the consent form [STD][TBD].
# 12 APPENDIX: SUPPORTING DETAILS

## 12.1 Clinical Laboratory Tests

The central laboratory analyses the following at screening, Week 0, Week 16, Week 48 and Week 52 (Section 1.3); the panel is confirmed in the laboratory manual [STD][TBD:laboratory manual].

| Panel | Tests |
|---|---|
| Hematology | Hemoglobin, hematocrit, red cell count, white cell count with differential, platelet count |
| Chemistry | Sodium, potassium, chloride, bicarbonate, urea or BUN, creatinine with estimated glomerular filtration rate, glucose, calcium, total protein, albumin, total bilirubin, alanine aminotransferase, aspartate aminotransferase, alkaline phosphatase |
| Urinalysis | Dipstick for protein, glucose and blood; microscopy when abnormal; urine protein quantification when the dipstick shows protein (VEGF pathway inhibition can cause proteinuria) [DERIVED] |
| Pregnancy | Urine or serum human chorionic gonadotropin for women of childbearing potential |
| Coagulation | Not routine; done when clinically indicated, and at screening when a bleeding disorder is suspected |

## 12.2 Contraception and Pregnancy

Women are of childbearing potential unless postmenopausal (12 months without menses with no other cause), surgically sterile or otherwise permanently infertile. Women of childbearing potential and men with partners of childbearing potential use highly effective contraception consistent with local regulations while on study and for a period after the last dose that is [TBD] [CTG:NCT04423718][STD][TBD]. Men do not donate sperm for the same period. Pregnancy testing is done at screening and at Week 0 and whenever pregnancy is suspected. Pregnancy handling is in Section 9 [STD].

## 12.3 Sample Storage

Plasma PK samples are stored at the temperature in the laboratory manual until analysis, and the remaining samples are kept for the period stated in the consent form and then destroyed, unless the participant consents to further use. Imaging data are archived at the central reading center for the period the regulations require [STD][TBD].

## 12.4 Hepatotoxicity Rules

Hepatotoxicity is not an identified risk of topical XYZ-123 at the exposure expected after eye-drop use, so no stopping rules based on liver tests are specified. Liver tests are part of the safety panel (Section 12.1); any ALT or AST value above 3 times the upper limit of normal with bilirubin above 2 times the upper limit of normal is evaluated by the investigator and reported as an adverse event of special interest to the sponsor within 24 hours, and a decision on drug interruption follows the medical monitor's advice [DERIVED][STD].

## 12.5 Disease-Specific Tables

**BCVA letters and approximate Snellen equivalents.**

| ETDRS letters | Approximate Snellen equivalent | Source |
|---|---|---|
| 78 | 20/32 | [CTG:NCT04423718] |
| 69 | 20/40 | [CTG:NCT04423718] |
| 35 | 20/200 | [CTG:NCT06856577] |
| 24 | 20/320 | [CTG:NCT04423718] |

**Rescue and masked schedule summary.**

| Item | Arm A | Arm B |
|---|---|---|
| Eye drops | XYZ-123 0.5% QD [dose provisional] | Vehicle, same frequency |
| Injection procedure | Sham when an injection is due in Arm B | Aflibercept 8 mg every 8 to 16 weeks (±1 week) per masked interval rule |
| Rescue | Aflibercept 8 mg when rescue criteria are met; counted as an event | Aflibercept 8 mg when rescue criteria are met or at an interval shorter than 8 weeks; counted as an event |

[USER][USER:P2-release][DERIVED]

**NEI VFQ-25.** The full text of the 25-item questionnaire, version 2000, is held at the sites in the validated language version [TBD:licensed instrument text][INSTR:NEI VFQ-25:2026-10-04].

**Ocular surface scales.** The corneal fluorescein staining scale and the dry eye symptom questionnaire are [TBD: instrument and version not confirmed].

## 12.6 Country-Specific Requirements

| Region | Requirement | Source |
|---|---|---|
| United States | IND under 21 CFR Part 312; IRB review under 21 CFR Part 56; informed consent under 21 CFR Part 50; financial disclosure under 21 CFR Part 54; SAE reporting under 21 CFR 312.32; ClinicalTrials.gov registration | [STD] |
| European Union | Clinical Trials Regulation (EU) No 536/2014 and the clinical trials information system; SUSAR reporting timelines; GDPR; national ethics review | [STD][TBD] |
| Japan | MHLW GCP ordinance and clinical trial notification to PMDA; jRCT registration; reporting of serious adverse reactions to PMDA; local IRB review; Japanese-language consent documents; availability and approval status of aflibercept 8 mg in Japan | [STD][TBD] |
| All countries | Country-specific consent, insurance, data transfer agreements and import of study products | [TBD] |

> 【設計変更コメント D12】日本での aflibercept 8 mg の承認・入手状況は未確認。確認が取れない場合は、対照薬を日本で承認済みの aflibercept に変更する案を PMDA と協議する。

# 13 APPENDIX: GLOSSARY OF TERMS AND ABBREVIATIONS

| Abbreviation | Meaning |
|---|---|
| ADA | Anti-drug antibody |
| AE | Adverse event |
| AESI | Adverse event of special interest |
| ALT / AST | Alanine aminotransferase / aspartate aminotransferase |
| ANCOVA | Analysis of covariance |
| BCVA | Best corrected visual acuity |
| BID | Twice daily |
| BUN | Blood urea nitrogen |
| CFR | Code of Federal Regulations |
| CMC | Chemistry, manufacturing and controls |
| CNV | Choroidal neovascularization |
| CST | Central subfield thickness |
| DMC | Data Monitoring Committee |
| EOP2 | End-of-Phase 2 (meeting) |
| EOT | End of Treatment |
| ETDRS | Early Treatment Diabetic Retinopathy Study |
| FAS | Full analysis set |
| FDA | United States Food and Drug Administration |
| GCP | Good Clinical Practice |
| GDPR | General Data Protection Regulation |
| HIPAA | Health Insurance Portability and Accountability Act |
| IB | Investigator's Brochure |
| ICH | International Council for Harmonisation |
| IND | Investigational New Drug application |
| IOP | Intraocular pressure |
| IRB | Institutional Review Board |
| IRF | Intraretinal fluid |
| IRT | Interactive response technology |
| IVT | Intravitreal |
| LS means | Least-squares means |
| MH | Mantel-Haenszel |
| MHLW | Ministry of Health, Labour and Welfare (Japan) |
| nAMD | Neovascular age-related macular degeneration |
| NEI VFQ-25 | National Eye Institute Visual Function Questionnaire, 25 items |
| NYHA | New York Heart Association |
| P1 | Primary endpoint |
| PK | Pharmacokinetics |
| PMDA | Pharmaceuticals and Medical Devices Agency (Japan) |
| PPS | Per-protocol set |
| QD | Once daily |
| RAND | RAND Corporation (developer of the NEI VFQ-25 version used) |
| Rand. | Randomization |
| RI | Run-in |
| RPE | Retinal pigment epithelium |
| SAE | Serious adverse event |
| SAP | Statistical analysis plan |
| Scr | Screening |
| SD-OCT | Spectral-domain optical coherence tomography |
| SoA | Schedule of Activities |
| SRF | Subretinal fluid |
| SUSAR | Suspected unexpected serious adverse reaction |
| VEGF | Vascular endothelial growth factor |
| VEGFR | Vascular endothelial growth factor receptor |
| Wk | Week |
| WOCBP | Women of childbearing potential |

# 14 APPENDIX: REFERENCES

1. ClinicalTrials.gov registry records NCT04423718, NCT02307682, NCT04270747, NCT04005352 and NCT06856577, accessed 2026-10-04 (including results sections where posted) [CTG:NCT04423718][CTG:NCT02307682][CTG:NCT04270747][CTG:NCT04005352][CTG:NCT06856577].
2. FDA correspondence for neovascular AMD products (verbatim excerpts, product names omitted): [PREC:Rani:s13/Q1b], [PREC:Rani:s13/Q1f], [PREC:Rani:s13/Q1i], [PREC:Rani:s13/Q3], [PREC:Rani:s2/p4c], [PREC:Fari:s40/p49c], [PREC:Brolu:s20/Q8], [PREC:Brolu:s20/Q13].
3. Aflibercept 8 mg (US prescribing information), https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/761355s005lbl.pdf, as found by web search on 2026-10-04 [PRIOR:aflibercept 8 mg US prescribing information].
4. RAND. NEI VFQ-25, version 2000, interviewer-administered format. https://www.rand.org/content/dam/rand/www/external/health/surveys_tools/vfq/vfq25survey_intadmin.pdf [INSTR:NEI VFQ-25:2026-10-04].
5. ICH E1: The extent of population exposure to assess clinical safety for drugs intended for long-term treatment of non-life-threatening conditions (1994) [STD].
6. ICH E6(R3): Guideline for Good Clinical Practice [STD].
7. 21 CFR Parts 11, 50, 54, 56 and 312, including 312.32 and 312.64 [STD].
8. Regulation (EU) No 536/2014 on clinical trials on medicinal products for human use [STD].
9. World Medical Association. Declaration of Helsinki [STD].
10. Phase 2 study results of XYZ-123 (news release supplied by the sponsor; fictional product) [USER:P2-release].
