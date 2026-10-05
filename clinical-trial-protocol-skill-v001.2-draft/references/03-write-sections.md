# Step 3: 本文を書く（節ごとに 12 回に分ける）

## 目的
`assets/section_spec_m11.yaml` の枠どおりに、各節を `protocol_facts.json` と疾患パックから書く。
**1 回に書くのは 1 つの章だけ**（4 回にまとめると分量が目安の 1 割程度しか出ないことが試運転で分かった）。
1 回ごとにファイルへ書き、粒度の検査を通してから次へ進む。

| 回 | 節 | 出力 |
|---|---|---|
| 1 | Title Page, 1（Synopsis・Schema・SoA） | `waypoints/sec_01.md` |
| 2〜11 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11（1 回 1 章） | `waypoints/sec_02.md` 〜 `sec_11.md` |
| 12 | 12, 13, 14（付録） | `waypoints/sec_12.md` |

各回の最後に粒度だけを測る（書きかけのファイルにも使える）:

```bash
uv run scripts/check_protocol.py waypoints/sec_NN.md --spec assets/section_spec_m11.yaml \
  --facts waypoints/protocol_facts.json --only-c7
```

C7 が fail の節は、**水増しではなく items の抜けを埋めて**書き足す（誰が・いつ・何を・どの基準で・記録先、
旧版の書き方ガイドの細目、定型文）。2 回書き足しても目安に届かない節は、理由（例: 試験に該当しない項目が多い）を
`waypoints/granularity_notes.md` に書いて次へ進む。

## 各回の手順

1. spec から該当節を読み、節ごとに `items`・`depth`・`target_pages`/`target_items`・`src`・`rule` を確認する。
   疾患領域の重み（`design_archetypes.yaml` の `therapeutic_area_families.<family>.emphasis`）があれば target_pages を上書きする。
   次に `references/section_guides.md` の対応表で、その節に当たる旧版の見出しを `references/section_guides_v1.1.1/` から読む
   （書く内容の細目。番号・行数・腫瘍の既定・機器の分岐は section_guides.md の規則で無視する）。
   先例の材料が在る適応症では、`waypoints/01_precedents.md` のうち、その節に対応する論点（`precedents/<indication_key>/index.md` の M11 の節の列）を読む。
   足りなければ `precedents/<indication_key>/topics/<key>.md` の目次から選び、索引が指す逐語のファイルの該当行を読む（1g の 3〜4 と同じ読み方）。
2. 見出しは spec の `id` と `title` を**そのまま**使う: `# 3 TRIAL OBJECTIVES AND ASSOCIATED ESTIMANDS`、`## 3.1 Primary Objective(s) and Associated Estimand(s)`。
   spec に無い 3 段目（例 6.10.1）は作ってよいが、2 段目の番号は変えない。
3. 書く順番（膨らませ規則）:
   1. `protocol_facts.json` の値を置く（`[USER]` / `[CTG:...]` / `[PACK:...]`）
   2. 疾患パックの規則・表で手順を完全な文にする（誰が・いつ・何を・どの基準で・記録先）
   2'. 当局の先例が求めた事項（例 欠測の補完方法の詳細・安全性データベースの大きさ）を、新試験の規定として書く `[PREC:<ID>]`。
      先例の数値は引用に逐語で在るものだけ。参照企業の試験番号・薬剤名は写さない（E3）。先例と USER の設計が食い違えば USER を優先し、4.2 節に理由を書く
   3. 足りない定型は `assets/NIH-FDA-Protocol-Template_STD-library.md` の文例を、試験に合わせて書き換えて使う `[STD]`
   4. それでも足りない説明は Claude が書く `[DERIVED]`。数値は書かない（E1）
4. 段落・表の行の末尾に出典ラベルを付ける。1 段落に複数の出典があれば併記: `[CTG:NCT05398445:eligibility_criteria][PACK:atopic_dermatitis]`。
5. 分量: `target_pages` の ±50% に収める（1 頁 ≒ 450 語）。大きく下回る節は items の抜けを疑う。
6. 書いた後、その回のファイルに対して: 見出しの数・`[TBD]` の数・ラベルの数を表示する。

## 節ごとの注意（spec の rule に加えて）

- **1.1 Synopsis**: 3・4・5・6・10 節の要約。評価項目の文は facts から逐語。
- **1.3 SoA**: 行＝疾患パックの `soa_rows`、列＝facts の `soa.visits`（週と許容幅）。全評価項目の時点の列があること。
- **3**: 目的ごとに estimand の 5 属性（集団・変数・中間事象と戦略・要約・治療）の表。
- **5.2/5.3**: CTG の逐語を起点に、パックの操作的定義で完全な文に。洗い出し期間は表。
- **6.10**: 禁止療法・非推奨療法・救済療法の 3 表。救済療法の行は facts.rescue と同じ並び。
- **9**: AE/SAE の定義と報告期限は STD、AESI は疾患パックの機序別候補から。
- **10.11**: `sample_size.json` の数値のみ。仮定に `[PRIOR:...]`、感度表を付ける。
- **12**: 疾患パックの `appendix_tables`（例 AD: 外用ステロイドの強さの表・尺度の全文）。尺度の全文が手元に無ければ `[TBD:licensed instrument text]`。

## してはいけないこと
- 参照試験のスポンサー名・薬剤名・施設・連絡先を本文に写す（E3）。先例の薬剤名・試験番号も同じ
- `[PREC]` を記憶から付ける（逐語を読んでいない ID は付けない）
- facts に無い評価項目・時点を本文で新たに作る（作るなら先に facts を直す）
- 旧版 `references/section_guides_v1.1.1/` の節番号・行数をそのまま使う／適応症に合わない腫瘍の既定を使う
