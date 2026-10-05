# 先例の材料: neovascular_amd

- 別名: neovascular age-related macular degeneration, nAMD, wet AMD, wAMD, wet age-related macular degeneration, 滲出型加齢黄斑変性, 新生血管型加齢黄斑変性

FDA と企業のやり取り（FDA コレスポンデンス）を、SCIA の構造化データから**逐語のまま**書き出したもの。プロトコルを書くときの `[PREC]` の材料。

> ★読み方の注意
> - 引用（`~~~~text` の枠の中）は SCIA の `60_meaning` の `text` を**1 文字も変えずに**写したもの（原文の英語）。紙のフッタ（"U.S. Food and Drug Administration / Silver Spring…"）や OCR の記号（`\geq` 等）、黒塗り `(b) (4)` も原文のまま。
> - 論点（Issue）・話し手の札（sponsor/agency/record）・会議の種別は SCIA が**機械で**付けたもの。人の確認は通していない。札が誤っている所がある（例: FDA の推奨が sponsor の札で入る）。話し手は引用の文面で確かめる。
> - 論点の索引への振り分けは、抽出側の語の規則による機械の**索引の補助**。各項目の「当たった語」で当否を判断する。
> - 表は SCIA の本文に文字として残っていない（表・図の中身はここに無い）。表の値が要るときは原本 PDF を見る。
> - 生成: 2026-10-04 ／ 2026-10-04T15:01:33+00:00。元ファイルの指紋は `_manifest.json`。

本文に使うときの出典ラベル: `[PREC:<略号>:s<区分の開始頁>/<論点>]`（例 `[PREC:Lebri:s2/Q4]` ＝ lebrikizumab の原本 PDF の p2 から始まる会議・書簡の Question 4）。
数値を本文に書けるのは、その数値が引用の中に逐語で在るときだけ（E1）。ラベルの ID が実在するかは skill の `uv run scripts/check_prec_ids.py --indication <適応症の名前> <ファイル>` が照らす。

## 読む順番

1. 下の表で、書く節に対応する論点の索引（`topics/<key>.md`）を選ぶ（対応は「M11 の節」の列）。
2. 索引の**目次**で薬剤・会議・見出し・当たった語・字数を見て、使う項目を選ぶ。必要なら項目ごとの「目印」（抜粋）も見る。
3. 選んだ項目の「本文」に書かれた `drugs/<薬剤>/<区分>.md` の行の範囲だけを読む（逐語の引用はここにしか無い）。
4. 前後の文脈が要るときは、同じファイルの前後（同じ論点の他の塊）を読む。

## 薬剤 × 論点（塊の数）

| 論点ファイル | M11 の節 | brolucizumab | faricimab | ranibizumab | 計 |
|---|---|---|---|---|---|
| [`topics/eligibility.md`](topics/eligibility.md) 対象集団・適格基準・前治療とウォッシュアウト | 5, 5.2, 5.3 | 2 | 1 | 3 | 6 |
| [`topics/endpoints.md`](topics/endpoints.md) 主要・副次評価項目と評価時点 | 3, 8 | 5 | 0 | 6 | 11 |
| [`topics/instruments_pro.md`](topics/instruments_pro.md) 評価尺度・患者報告アウトカム（PRO）・日誌 | 8.3, 12 | 2 | 0 | 0 | 2 |
| [`topics/estimand_rescue.md`](topics/estimand_rescue.md) estimand・中間事象・救済療法・中止 | 3, 6.10, 7 | 2 | 0 | 3 | 5 |
| [`topics/analysis_methods.md`](topics/analysis_methods.md) 解析方法（主解析・調整・部分集団・解析対象集団） | 10 | 2 | 0 | 3 | 5 |
| [`topics/missing_data.md`](topics/missing_data.md) 欠測データの扱い | 10 | 0 | 0 | 2 | 2 |
| [`topics/multiplicity.md`](topics/multiplicity.md) 多重性・第 1 種の過誤・中間解析 | 10 | 1 | 0 | 0 | 1 |
| [`topics/dose_selection.md`](topics/dose_selection.md) 用量・用法の選び方（第 2 相からの根拠・負荷投与） | 2, 4, 6 | 3 | 0 | 6 | 9 |
| [`topics/safety.md`](topics/safety.md) 安全性（安全性データベースの大きさ・曝露期間・特に注目する有害事象・監視） | 8, 9, 10.11 | 6 | 7 | 7 | 20 |
| [`topics/concomitant.md`](topics/concomitant.md) 併用療法・基礎治療（外用ステロイド・保湿剤・禁止薬・ワクチン） | 6, 6.10 | 0 | 0 | 1 | 1 |
| [`topics/design.md`](topics/design.md) 試験デザイン・期間・維持期・試験の本数 | 4 | 6 | 2 | 5 | 13 |
| [`topics/pediatric.md`](topics/pediatric.md) 小児・青年（PREA・小児開発計画） | 5, 12 | 4 | 2 | 1 | 7 |
| [`topics/pk_immunogenicity.md`](topics/pk_immunogenicity.md) 薬物動態・免疫原性・相互作用 | 8 | 3 | 3 | 1 | 7 |
| [`topics/labeling.md`](topics/labeling.md) 表示（ラベル）に載せるための条件（参考） | 3, 10 | 4 | 4 | 7 | 15 |
| [`topics/out_of_protocol.md`](topics/out_of_protocol.md) プロトコル外（CMC・非臨床の論点） | — | 4 | 26 | 0 | 30 |
| [`topics/other.md`](topics/other.md) その他（どの論点の語にも当たらなかった塊） | — | 23 | 22 | 18 | 63 |

## 薬剤（文書）

| 薬剤 | 略号 | 文書 | 論点数 | 発言数 | 会議の一覧 |
|---|---|---|---|---|---|
| brolucizumab | Brolu | `FDA_Brolucizumab_Ophtha_761125Orig1s000` | 45 | 93 | [`drugs/brolucizumab/index.md`](drugs/brolucizumab/index.md) |
| faricimab | Fari | `FDA_Faricimab_Ophtha_761235Orig1s000` | 59 | 124 | [`drugs/faricimab/index.md`](drugs/faricimab/index.md) |
| ranibizumab | Rani | `FDA_Ranibizumab_Ophtha_761197Orig1s000` | 41 | 113 | [`drugs/ranibizumab/index.md`](drugs/ranibizumab/index.md) |
