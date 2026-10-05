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
