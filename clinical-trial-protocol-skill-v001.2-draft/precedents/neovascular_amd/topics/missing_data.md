# 先例の索引: 欠測データの扱い（neovascular_amd）

- 論点の key: `missing_data` ／ 読むべき M11 の節: 10
- 塊の数: 2（薬剤ごと: brolucizumab 0, faricimab 0, ranibizumab 2）

> ★このファイルは**索引**。逐語の引用は置いていない。引用は各項目の「本文」の行を開いて読む（例: Read で `drugs/lebrikizumab/s2.md` の 120〜160 行目）。
> ★「目印」は選ぶための抜粋（当たった語の前後）で、改行を空白にし前後を切っている。**本文の引用・数値の出典には使わない。**

> ★読み方の注意
> - 引用（`~~~~text` の枠の中）は SCIA の `60_meaning` の `text` を**1 文字も変えずに**写したもの（原文の英語）。紙のフッタ（"U.S. Food and Drug Administration / Silver Spring…"）や OCR の記号（`\geq` 等）、黒塗り `(b) (4)` も原文のまま。
> - 論点（Issue）・話し手の札（sponsor/agency/record）・会議の種別は SCIA が**機械で**付けたもの。人の確認は通していない。札が誤っている所がある（例: FDA の推奨が sponsor の札で入る）。話し手は引用の文面で確かめる。
> - 論点の索引への振り分けは、抽出側の語の規則による機械の**索引の補助**。各項目の「当たった語」で当否を判断する。
> - 表は SCIA の本文に文字として残っていない（表・図の中身はここに無い）。表の値が要るときは原本 PDF を見る。
> - 生成: 2026-10-04 ／ 2026-10-04T15:01:33+00:00。元ファイルの指紋は `_manifest.json`。

本文に使うときの出典ラベル: `[PREC:<略号>:s<区分の開始頁>/<論点>]`（例 `[PREC:Lebri:s2/Q4]` ＝ lebrikizumab の原本 PDF の p2 から始まる会議・書簡の Question 4）。
数値を本文に書けるのは、その数値が引用の中に逐語で在るときだけ（E1）。ラベルの ID が実在するかは skill の `uv run scripts/check_prec_ids.py --indication <適応症の名前> <ファイル>` が照らす。

## 目次

| # | PREC | 薬剤 | 会議 | 見出し | 字数 | 本文（行） |
|---|---|---|---|---|---|---|
| 1 | `Rani:s2/p4c` | Rani | Type B, August 17, 2020 from 2:00pm – 3:00pm (EST) | CLINICAL/STATISTICAL/SAFETY | 4,430 | `drugs/ranibizumab/s2.md` 189–331 |
| 2 | `Rani:s13/Q1i` | Rani | 種別未判定, 署名 04/08/2018 | Question 1i | 879 | `drugs/ranibizumab/s13.md` 436–466 |

### 1. [PREC:Rani:s2/p4c] CLINICAL/STATISTICAL/SAFETY（塊 1/1）
- 本文: `drugs/ranibizumab/s2.md` 189–331 行 ／ 抽出元: `SCIA_v1_dash_Root/data/main/60_meaning/FDA_Ranibizumab_Ophtha_761197Orig1s000.jsonl` 8 行目（`FDA|FDA_Ranibizumab_Ophtha_761197Orig1s000|s2|p4c`）・p4–7
- 原本: FDA 761197Orig1s000, Administrative and Correspondence Documents（Drugs@FDA） の PDF p4–7
- Type B, August 17, 2020 from 2:00pm – 3:00pm (EST) ／ 振り分け: 機械 ／ 当たった語: "missing" ／ 他の論点: safety/design
- 目印: …o this information, the expectation is it will be used to fill in any missing information for a new BLA. The Agency confirmed that cross-referencin…

### 2. [PREC:Rani:s13/Q1i] Question 1i（塊 1/1）
- 本文: `drugs/ranibizumab/s13.md` 436–466 行 ／ 抽出元: `SCIA_v1_dash_Root/data/main/60_meaning/FDA_Ranibizumab_Ophtha_761197Orig1s000.jsonl` 24 行目（`FDA|FDA_Ranibizumab_Ophtha_761197Orig1s000|s13|Q1i`）・p18
- 原本: FDA 761197Orig1s000, Administrative and Correspondence Documents（Drugs@FDA） の PDF p18
- 種別未判定, 署名 04/08/2018 ／ 振り分け: 機械 ／ 当たった語: "imput", "dropout" ／ 他の論点: endpoints/estimand_rescue/safety
- 目印: … plan for statistical analysis of the primary endpoint, including the imputation methods?…
