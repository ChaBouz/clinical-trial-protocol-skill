# 節ごとの書き方ガイド（v1.1.1 の指示を M11 の節に付け替えたもの）

v1.1.1 の `02/03/04` には、節ごとの詳しい書き方（AE の定義・報告期限・統計の記述・運営の定型 等）が
約 11 万字あった。v001.2 ではそれを捨てず `references/section_guides_v1.1.1/` に置き、
**どの M11 の節を書くときに、旧版のどの見出しを読むか**をこの表で指定する。

## 読み方の決まり（旧版の指示より優先）

1. 節番号・見出し・分量は `assets/section_spec_m11.yaml` が正。旧版の「(N lines)」「Section 4」などの番号と行数は無視する。
2. 旧版の腫瘍の既定（ECOG・余命・組織検体・RECIST・臓器機能表・CTCAE）は、
   `design_archetypes.yaml` の `therapeutic_area_families` が **oncology** のとき、または疾患パックが指定したときだけ使う。
   それ以外は疾患パック（無ければ下書きパック）の区分を使い、AE の重症度は mild/moderate/severe。
3. 旧版の「医療機器（device）」の分岐は読まない（この版は医薬品のみ）。
4. 旧版に無い estimand・中間事象・多重性の形は `design_archetypes.yaml` から。
5. 旧版の例文に数値（30 日、24 時間 等）があるものは [STD] として使ってよいが、試験固有の数値（用量・閾値・例数）は E1 に従う。

## 対応表（M11 の節 → 旧版のファイルと見出し）

| M11 | 旧版のファイル | 旧版の見出し（文字列で探す） | 付け加える点 |
|---|---|---|---|
| TP | 02-protocol-foundation.md | `### Title Page` | M11 の表紙項目（spec の TP.items） |
| 11（遵守声明） | 02-protocol-foundation.md | `### STATEMENT OF COMPLIANCE` | ICH E6(R3) に読み替え |
| 1.1 | 02 | `#### Section 1.1: Synopsis` | estimand の要約表を追加 |
| 1.2 | 02 | `#### Section 1.2: Schema` | — |
| 1.3 | 02 | `#### Section 1.3: Schedule of Activities` | 行はパックの soa_rows。腫瘍の画像評価行は oncology のときだけ |
| 2.1 | 02 | `#### Section 2.1: Study Rationale` | — |
| 2.2 | 02 | `#### Section 2.2: Background` と `#### Section 2.3: Risk/Benefit Assessment` | M11 では 2.2 に統合 |
| 3 | 02 | `### Section 4: OBJECTIVES AND ENDPOINTS` | estimand の 5 属性の表を必須（archetypes） |
| 4.1, 4.2, 4.4 | 02 | `### Section 4: STUDY DESIGN`（4.1/4.2/4.4） | 4.2 に患者の声（patient input）の有無 |
| 6.2 | 02 | 同上の 4.3 Justification for Dose | M11 では 6.2 |
| 5.1–5.5 | 02 | `### Section 5: STUDY POPULATION` | 規則 2（腫瘍の既定を外す）。洗い出し期間は表 |
| 6.1, 6.3 | 03-protocol-intervention.md | `#### 6.1 Study Intervention(s) Administration` | — |
| 6.4 | 03 | `#### 6.2 Dose Modifications` | 減量の無い薬は中断・再開・永久中止の表 |
| 6.5 | — | — | 過量投与（STD） |
| 6.6 | 03 | `#### 6.3 Preparation/Handling/Storage/Accountability` | — |
| 6.7 | 03 | `#### 6.4 Measures to Minimize Bias` | 層別は facts から |
| 6.8 | 03 | `#### 6.5 Study Intervention Compliance` | — |
| 6.9 | — | — | 基礎治療・背景治療（パック） |
| 6.10 | 03 | `#### 6.6 Concomitant Therapy` | 禁止・非推奨・救済の 3 表。救済と中間事象を 1 対 1 |
| 7.1–7.3 | 03 | `### Section 7: ...DISCONTINUATION...` | 中止後も来院継続（treatment policy 用） |
| 8.1, 8.2 | 04-protocol-operations.md | `### Section 8:` の冒頭 | — |
| 8.3 | 04 | `#### 8.1 Efficacy Assessments` | 評価者・訓練・想起・得点・responder・時点（パックの instruments） |
| 8.4 | 04 | `#### 8.2 Safety and Other Assessments` | — |
| 9 | 04 | `#### 8.3 Adverse Events and Serious Adverse Events` と `#### 8.4 Unanticipated Problems` | 重症度は規則 2。AESI はパック |
| 10.1–10.3 | 04 | `#### 9.3 Populations for Analyses` と `#### 9.4 Statistical Analyses` の一般 | estimand ごとに書く |
| 10.4–10.9 | 04 | `#### 9.4 Statistical Analyses` | 解析・欠測は archetypes |
| 10.10 | — | — | archetypes の multiplicity_patterns |
| 10.11 | 04 | `#### 9.2 Sample Size Determination` | 数値は scripts/sample_size.py の出力のみ |
| 11 | 04 | `#### 10.1`〜`#### 10.13` | 同意・中止・秘密保持・委員会・モニタリング・QA/QC・記録・逸脱・公開・利益相反 |
| 12 | — | — | パックの appendix_tables、国別要件 |
| 13 | 04 | `#### 10.14 Abbreviations` | 本文から自動抽出 |
| 14 | 04 | `### Section 11: REFERENCES` | 本文で引用したものだけ |
