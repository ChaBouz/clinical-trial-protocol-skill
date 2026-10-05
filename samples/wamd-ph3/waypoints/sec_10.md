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
