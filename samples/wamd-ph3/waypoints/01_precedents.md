# 01_precedents.md（neovascular_amd。FDA コレスポンデンスの逐語から）

> 話者の札は SCIA が機械で付けたもの。逐語の文面で話者を確かめた。要点は Claude の言い換え [DERIVED]。
> ★先例はすべて**硝子体内注射（biologic）**の開発。**点眼薬**の先例は無い。当てはめは「形」と「標準値」だけで、点眼固有の論点（用量・曝露・全身安全性）の先例は無い。

## 主要評価項目・時点
- [PREC:Rani:s13/Q1b] ranibizumab（PDS）, 会議（種別未判定・署名 04/08/2018）
  - 当局の要点 [DERIVED]: 主要評価項目＝BCVA のベースラインからの変化、時点は治療期間の少なくとも 9 か月後。Week 36/40/44 の平均は可。
  - 逐語: "Agency Response: No. The primary endpoint of change in BCVA from baseline should be at least 9 months after the treatment period. It would be acceptable to average over Weeks 36, 40 and 44. We will need to review the protocol and statistical analysis plan."
  - 当てはめ: パック endpoints.primary ／ M11 3, 8。★利用者の主要評価項目は「15 文字以上の低下（割合）」で、先例の「BCVA 変化量」と型が異なる（→ 確認事項）。
- [PREC:Brolu:s20/Q10] brolucizumab, Type B (EOP2) 2013-05-08
  - 当局の要点 [DERIVED]: 主要有効性評価項目は Month 12 の遠方 BCVA のベースラインからの変化を推奨。
  - 逐語: "We recommend the change from baseline in distance BCVA at Month 12 as the primary efficacy endpoint."
- [PREC:Rani:s13/Q1k] ranibizumab: Week 36 の BCVA 変化量を代替の主要評価項目とすることに FDA が同意。
  - 逐語: "Agency Response: Yes, we agree."（質問は "Can the Agency comment on the approvability of change in BCVA from baseline at Week 36 as an alternative primary endpoint?"）
- [PREC:Rani:s2/p4c] ranibizumab, Type B 2020-08-17
  - 当局の要点 [DERIVED]: BCVA の変化と、ベースラインからの 15 文字の改善/悪化を臨床的に意味があるとみなす。
  - 逐語: "The Agency clarified it considers the change in Best Corrected Visual Acuity (BCVA) and the gain or loss of 15 letters from baseline to be clinically significant."

## 非劣性マージン（実薬 aflibercept 対照）
- [PREC:Rani:s13/Q1b]（上と同じ塊の議事）
  - 逐語: "The equivalence margin for these trials is recommended to be no more than 4.5 letters for the upper or lower margins."
  - 注: 文脈は同等性（equivalence）で BCVA 変化量のマージン。
- [PREC:Fari:s40/p49c] faricimab, Type B (EOP2) 2018-04-24
  - 逐語: "Roche proposes to use a 4-letter inferiority margin. The Agency agreed assuming that Roche's studies demonstrate similar efficacy results in the control arm (aflibercept group)."
  - 当てはめ: パック analysis.NI_margin ／ M11 10。★先例のマージンは **BCVA 変化量**（文字数）のもの。「15 文字以上の低下の割合」のマージンの先例は読めていない → [TBD]。

## 対照薬・盲検
- [PREC:Brolu:s20/Q13] brolucizumab, Type B (EOP2) 2013-05-08
  - 逐語: "Agency Response: Disagree. Adequate and well controlled studies are expected to include adequate measures to minimize bias on the part of the subjects, observers, and analysts of the data. We agree that sham injections are not the best method to minimize bias."
  - 逐語（議事）: "The Division responded that sham injections do not provide optimal masking, but if an anesthetic is given and the sham procedure includes pressure on the eye with the hub of a needle, then the masking might be adequate."
  - 当てはめ: M11 4（盲検化）。点眼（試験薬）対 硝子体内注射（aflibercept）の二重盲検は、ダブルダミー（試験薬群に sham 注射、aflibercept 群にビヒクル点眼）が必要。方法の先例は上のみ。

## 救済療法・中間事象（estimand）
- [PREC:Rani:s13/Q1f] ranibizumab
  - 逐語: "the Agency disagree with a number of the proposed definitions, but agreed that a reduction of 15 letters or more compared to the best BCVA would be a treatment failure."
  - 逐語: "The Agency stated that, to the extent possible, it would like patients to be followed throughout the trial."
  - 当てはめ: 治療失敗の定義（最良 BCVA からの 15 文字以上の低下）。★「ベースラインから」ではなく「最良 BCVA から」。
- [PREC:Rani:s13/Q1i] ranibizumab
  - 逐語: "We recommend you consider the trimmed mean approach (https://www.ncbi.nlm.nih.gov/pubmed/27523396) for patients who receive rescue therapy and patients who discontinue the study treatment due to adverse events in the primary analysis. Your proposed analysis can be conducted as supplementary analysis."
  - 逐語: "Additionally, we recommend you take measures to follow and conduct efficacy and safety evaluation for all treated patients throughout the study regardless of the occurrences of the intercurrent events that may impact the treatment effect of the study product. You should collect detailed information on the reasons of discontinuation for early study dropouts."

## 対象集団
- [PREC:Rani:s13/Q1a] ranibizumab
  - 逐語: "No, while 9 months prior to the screening visit is acceptable, it would be preferable to limit the study population to having a diagnosis of nAMD within 6 months or less to better align with the studies establishing the non-inferiority margin."
  - 注: 質問は治療歴ありの集団（anti-VEGF 反応例）。本試験は未治療（利用者の指定は年齢のみ）で、治療歴の扱いは [TBD]。

## 安全性データベース
- [PREC:Rani:s13/Q3] ranibizumab
  - 逐語: "It is recommended that the clinical program include enough patients to identify adverse events that occur at a rate of 1% or greater. To accomplish this, it is recommended that approximately 500 or more subjects using the test drug product complete treatment with a concentration of the test drug product at least as high as proposed for marketing with a frequency at least as frequent as proposed for marketing. Prior to an NDA submission, it is recommended that at least 300 patients would have completed at least 12 months of follow-up after the initiation of treatment."
  - 当てはめ: M11 10.11 / 安全性データベース（数値は逐語に在る 500・300・12 か月・1% のみ）。

## 用量選択
- [PREC:Brolu:s20/Q8] brolucizumab（議事）
  - 逐語: "The recommendation was to study at least two doses (i.e., 6 mg/mL and < 6mg/mL) for at least 9-months in order to select a dose to study in Phase 3."
  - 当てはめ: M11 2/6。★試験薬の点眼の用量・頻度は利用者が未指定（[TBD]）。第 2 相の用量設定の根拠は材料に無い。

## 先例が無かった論点（読めていない・材料に無い）
- 点眼薬の先例（局所・全身安全性、角膜・眼圧、点眼の遵守・点眼日誌）。
- 「15 文字以上の低下」を主要評価項目とする非劣性のマージン。
- 多重性（multiplicity 索引は 1 件のみで、Brolu:s20/p22 は主要評価項目が非劣性だったとの記述のみ。数値の出典にならない）。
