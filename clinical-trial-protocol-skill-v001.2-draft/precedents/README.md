# precedents/ — 当局の先例の材料（任意）

規制当局と企業のやり取り（例: FDA の会議録・書簡）の**原文の逐語**を、適応症ごとに置く場所。
プロトコルを書くときの `[PREC]` の材料になる（Step 1g・Step 3）。

**任意です。** このフォルダに適応症の材料が無ければ、Step 1g は飛ばされ、`[PREC]` は疾患パックに書かれたものだけになる。
skill はこのフォルダの中身を作らない。利用者が用意して、下の形で置く（手作りでも、別の道具の出力でもよい）。

**疾患パックとは独立。** `disease_packs/<indication_key>.yaml` が無くても、先例の材料だけ置いてよい（逆も同じ）。
2 つを結ぶのはフォルダ名とファイル名が同じ `indication_key` であることだけ。Step 0 で利用者が名前を選ぶとき、
`disease_packs/` と `precedents/` に在る名前が一覧で示されるので、同じ適応症には同じ名前を使う。

## 作り方（雛形から）

1. `precedents/_template/` を `precedents/<indication_key>/` という名前でコピーする（★先頭の `_` を外す。`_` で始まるフォルダは無視される）
2. 原本（会議録・書簡など）の文を、`verbatim/` の下のファイルに**1 文字も変えずに** `~~~~text` の囲みで置く
3. 論点ごとに `topics/<key>.md`（索引）を書き、各項目から逐語の行の範囲を指す
4. `index.md` の表に、索引ファイルと対応する M11 の節を書く
5. 使う ID を `prec_ids.txt` に 1 行 1 つ書く
6. 検査: `uv run scripts/validate_precedents.py precedents/<indication_key>` → 「問題 0 件」

## 形の約束（検査 `scripts/validate_precedents.py` が見る所）

```
precedents/<indication_key>/
├── index.md              … 必須。「M11 の節」の列を持つ表に、topics/ の全ファイルを載せる
├── topics/<key>.md       … 必須（1 つ以上）。論点ごとの索引（逐語は置かない）
├── prec_ids.txt          … 必須。ID を 1 行に 1 つ（重複・空白なし）
└── <逐語のファイル>       … 置き場所と名前は自由（例 verbatim/xxx.md）
```

| 所 | 約束 |
|---|---|
| 索引の項目の見出し | `### <番号>. [PREC:<ID>] <見出し>`（ID は prec_ids.txt に在るもの） |
| 索引の項目の本文の場所 | 見出しの下に `- 本文: \`<precedents/<indication_key>/ からの道>\` <開始行>–<終了行> 行` |
| 逐語 | 原文そのまま。`~~~~text` で始まり `~~~~` で終わる囲みに入れる。要約しない。指す行の範囲に囲みが 1 つ以上 |
| index.md の別名（任意） | `- 別名: atopic dermatitis, AD, アトピー性皮膚炎` の 1 行（カンマ区切り）。Step 0 で利用者の言葉と完全一致で照合される（`scripts/list_indications.py`） |
| 索引のその他の行 | 自由（会議・原本・抜粋など）。抜粋は「選ぶための目印」で、引用や数値の出典には使わない |
| ID の書式 | 材料の側で決めてよい（空白・`]`・カンマを含まない）。本文では `[PREC:<ID>]` |

## 使う側の決まり（SKILL.md・references から）

- 先例を出典にできる数値は、逐語のファイルの中に**逐語で在る**ものだけ（E1）。索引の抜粋や Claude の要約は出典にならない
- 記憶にある先例に `[PREC]` を付けない。ID は `prec_ids.txt`（または疾患パック）に在るものだけ
- 参照企業の薬剤名・試験番号は本文に写さない（E3）

ID の検査: `uv run scripts/check_prec_ids.py --indication <indication_key> <ファイル>`（同じ適応症の材料だけで照らす。実在しない ID があれば exit 1）。
