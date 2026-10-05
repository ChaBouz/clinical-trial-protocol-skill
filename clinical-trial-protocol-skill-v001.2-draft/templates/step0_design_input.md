# Step 0 の入力シート（雛形・2026-10-04）

このシートを写して埋め、skill を起動したあと Step 0 で Claude に貼り付ける。
**埋められる所だけでよい。** 空欄は「未記入なら」の列のとおりに扱われる（推測では埋まらない。[TBD] として残る）。
数値（用量・例数・期間）は、自分で決めた値か出典のある値だけを書く。

## A. 必須

| 欄 | 書く値 | 例 |
|---|---|---|
| 製品名・開発コード（仮名可） |  | XYZ-123 |
| 種類・作用機序・投与経路 |  | anti-IL-13 monoclonal antibody, subcutaneous |
| 適応症 |  | アトピー性皮膚炎（日本語・英語・略号のどれでもよい。Claude が在る名前・別名と照合し、名前 `indication_key` を確かめてから決める） |

## B. 設計（空欄なら疾患パックの既定値、それも無ければ [TBD]）

| 欄 | 書く値 | 例 |
|---|---|---|
| 対象集団 |  | moderate-to-severe AD, adults ≥18 y, inadequate response to topical therapy |
| 相 |  | 3 |
| 設計 |  | randomized, double-blind, placebo-controlled, parallel-group, monotherapy |
| 群（用量・頻度・負荷投与） |  | XYZ 300 mg Q2W（Day 1 600 mg）／ XYZ 300 mg Q4W（同）／ Placebo |
| 割付比 |  | 1:1:1 |
| 投与期間（週）・主要評価の時点（週） |  | 16 / 16 |
| 追跡期間（週）・継続試験の有無 |  | 12 / LTE あり |
| 地域 |  | US, EU, Japan |
| 層別因子 |  | baseline severity, region |
| 主要評価項目 |  | IGA 0/1 (≥2-point improvement) and EASI-75 co-primary at Week 16 |
| 比較の型 |  | superiority vs placebo（ほか: superiority vs active ／ non-inferiority） |

## C. 例数の条件（空欄なら左の既定）

| 欄 | 既定 | 書く値 |
|---|---|---|
| 検出力 | 0.90 |  |
| 有意水準（両側） | 0.05 |  |
| 脱落率 | 0.10 |  |

## D. 任意

| 欄 | 書く値 | 例 |
|---|---|---|
| 参照にしたい試験の NCT 番号 |  | NCT01234567（空欄なら Step 1 で 5 本探す） |
| スポンサー情報（社名・住所・医学専門家） |  | （空欄なら [TBD]） |
| 治験薬概要書（IB）の既知のリスク |  | （空欄なら [TBD:IB]） |
| その他の資料の要点（第 2 相の結果など） |  | （出典つきで） |
