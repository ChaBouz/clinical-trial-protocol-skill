# 01_precedents.md — aplastic_anemia（2026-10-25）

**先例の材料（`precedents/aplastic_anemia/`）は無い。** Step 1g の手順（索引 → 逐語）は行わず、`[PREC:<ID>]` は使わない（`check_prec_ids.py` で照らせる ID が無いため）。

代わりに、利用者提供の FDA 承認パッケージ **NDA 22291 Orig1s021（PROMACTA/eltrombopag, 承認 2018-11-16, 291 頁）** を
`[PRIOR:NDA22291-S021:<箇所>]` として使う。下の逐語は pdftotext で取り出した本文から 1 文字も変えずに写した（改行のみ空白に置換）。
出典 URL（利用者提示）: https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/022291Orig1s021.pdf

## 適格基準（重症度・対象）
- [PRIOR:NDA22291-S021:label-14.3] 難治 SAA の根拠試験 US28T（NCT00922883）
  - 要点: 1 回以上の IST に不十分な反応、かつ血小板 ≤30×10^9/L の SAA 43 例の単群試験 [DERIVED]
  - 逐語: "PROMACTA was studied in a single-arm, single-center, open-label trial (Study ETB115AUS28T, referred to as Study US28T [NCT00922883]) in 43 patients with severe aplastic anemia who had an insufficient response to at least one prior immunosuppressive therapy and who had a platelet count less than or equal to 30 x 109/L."
  - 当てはめ: パック inclusion.refractory / platelets ／ M11 5.2
- [PRIOR:NDA22291-S021:summary-review] SAA の定義
  - 逐語: "All of the patients met the criteria for severe aplastic anemia: bone marrow cellularity <30% and at least two of the following: ANC<500/μL, platelet count <20,000/μL and reticulocytes <20,000/μL."
  - 注: 臨床審査（p.40）と CTG:NCT01623167 は網赤血球 <60,000/µL。資料内で網赤血球の閾値が割れる → options（どちらかを選ばない）

## 評価項目（反応の定義）
- [PRIOR:NDA22291-S021:label-14.3] 難治 SAA の血液学的反応
  - 逐語: "Hematologic response was defined as meeting 1 or more of the following criteria: 1) platelet count increases to 20 x 109/L above baseline, or stable platelet counts with transfusion independence for a minimum of 8 weeks; 2) hemoglobin increase by greater than 1.5 g/dL, or a reduction in greater than or equal to 4 units of RBC transfusions for 8 consecutive weeks; 3) ANC increase of 100% or an ANC increase greater than 0.5 x 109/L."
  - 当てはめ: パック endpoints.primary.rules ／ M11 3, 8.1
- [PRIOR:NDA22291-S021:clinical-review-p41] 増殖因子・輸血による改善の扱い
  - 逐語: "Improvement in blood counts following administration of therapies such as growth factors or transfusions (including re-introduction of eltrombopag after Month 3 for subjects in Cohort 2) were not considered as fulfilling the criteria for response."
  - 当てはめ: estimand の中間事象 ／ M11 3

## 用量・投与期間（同機序の小分子の情報。抗体の用量の根拠にはならない）
- [PRIOR:NDA22291-S021:label-2.3]
  - 逐語: "Hematologic response requires dose titration, generally up to 150 mg, and may take up to 16 weeks after starting PROMACTA [see Clinical Studies (14.3)]."
  - 逐語: "Discontinuation: If no hematologic response has occurred after 16 weeks of therapy with PROMACTA, discontinue therapy."
  - 逐語: "For patients with severe aplastic anemia of Asian ancestry or those with mild, moderate, or severe hepatic impairment (Child-Pugh Class A, B, C), initiate PROMACTA at a reduced dose of 25 mg once daily"
  - 当てはめ: 反応判定の時点（16 週）・無効中止の規則 ／ M11 4.3, 7.1。日本人の曝露差は抗体では機序が違う（eltrombopag の東アジア人での曝露増加は小分子の PK による）→ 本剤では [TBD]
- [PRIOR:NDA22291-S021:label-2.3] 血小板過剰時の減量・休薬（Table 7）
  - 逐語: "> 400 x 109/L                    Stop PROMACTA for 1 week."（表の行。空白は原文のまま）
  - 当てはめ: 6.4 の用量調整表の「形」。抗体は半減期が長く「1 週休薬」では濃度が下がらない → 閾値は借り、措置は DERIVED

## 安全性
- [PRIOR:NDA22291-S021:label-6.1] 難治 SAA での染色体異常
  - 逐語: "In this trial, patients had bone marrow aspirates evaluated for cytogenetic abnormalities. Eight patients had a new cytogenetic abnormality reported on therapy, including 5 patients who had complex changes in chromosome 7."
- [PRIOR:NDA22291-S021:clinical-review-8.5] AESI
  - 逐語: "Adverse events of special interest included the following: bleeding, hepatobiliary events, thromboembolic events, renal events, hematological malignancies (incidence of new malignancy or worsening of current malignancy with suspected causality to study treatment particularly myelodysplasia), bone marrow fibrosis (development or progression of bone marrow fibrosis), recurrence of thrombocytopenia after eltrombopag withdrawal and cytogenetic abnormalities."
  - 当てはめ: パック safety_monitoring ／ M11 8.4, 9
- [PRIOR:NDA22291-S021:clinical-review-8.4.10] 免疫原性
  - 逐語: "No information regarding immunogenicity was included in this application."
  - 当てはめ: 小分子の eltrombopag では免疫原性の先例が無い → 抗体の本剤では ADA・中和抗体の計画を STD（FDA Immunogenicity Testing guidance）で新たに書く ／ M11 8.5
- [PRIOR:NDA22291-S021:clinical-review-8.8.1] クローン進展の背景リスク
  - 逐語: "In other studies, the risk was estimated to be approximately 15% at 5 years and the incidence of conversion to abnormal karyotype was about 50% within the first 30 months."

## デザイン（単群の受け入れ）
- [PRIOR:NDA22291-S021:clinical-review-1.2]
  - 逐語: "Therefore, although the primary efficacy evaluation was based on a small number of patients studied in a single-arm trial, considering that SAA is a rare and life-threatening disease with limited treatment options, the AUS01T trial results provides substantial evidence of efficacy of eltrombopag administered in combination with standard IST in adult and pediatric patients (≥2 years) with SAA as first-line therapy."
  - 当てはめ: 単群・非盲検の根拠 ／ M11 4.2
