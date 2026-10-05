# 先例の材料: <indication_key>

<!-- 雛形（2026-10-04）。precedents/_template/ を precedents/<indication_key>/ にコピーして書き換える。
     ★ _ で始まるフォルダ（この雛形）は skill に無視される。
     検査: uv run scripts/validate_precedents.py precedents/<indication_key> -->

当局と企業のやり取り（会議録・書簡など）の原文を、逐語のまま置いたもの。プロトコルの `[PREC]` の材料。

- 別名: （任意。例 atopic dermatitis, AD, アトピー性皮膚炎）← Step 0 の名前の照合に使う。カンマ区切り。不要ならこの行を消す
- 原本: （例）FDA, BLA 000000 Administrative and Correspondence Documents（Drugs@FDA）
- 作った人・日付: （例）氏名, 2026-10-04
- ID の書式: （例）`<略号>:s<区切りの開始頁>/<質問番号>`。本文では `[PREC:<ID>]`

## 論点の索引と M11 の節

★必須の表。Step 1g と Step 3 はこの表で、どの索引を読むかを決める（列の名前は変えない）。

| 論点の索引 | M11 の節 |
|---|---|
| [`topics/endpoints.md`](topics/endpoints.md) 主要・副次評価項目 | 3, 8 |
