# Step 0: 設計の入力（USER の値を集める）

## 目的
CTG からは取れない「新試験の設計」を利用者から集め、`waypoints/intervention_metadata.json` に書く。
ここで決めた値が本文の `[USER]` になる。分からない値は `null` のままにし、本文では `[TBD]` になる。

## 手順

1. 続きの作業（開始時に「進行中の作業を続ける」が選ばれた）なら、その `intervention_metadata.json` を表示し、「続ける／作り直す／一部更新」を聞く。
   新しい作業なら、製品名（仮名可）から `intervention_id`（小文字・`-` つなぎ。例 `xyz-123`）を作り（製品名が未定なら適応症と相から仮に作る。例 `wamd-ph3`）、作業フォルダ `runs/<intervention_id>/` を作る
   （利用者が別の場所を指定したらそこ。SKILL.md「道の決まり」）。同じ名前の作業フォルダが在れば、別の名前にするか続きにするかを聞く。
2. **適応症の名前（`indication_key`）を決める。** 疾患パックと先例の材料を探すときの共通の名前（ASCII の snake_case。例 `atopic_dermatitis`）。
   利用者の言葉（英語・日本語・略号。例 "Eczema"・"アトピー性皮膚炎"・"AD"）から、次の順で決める。**名前は推測で決めない。**
   1. 機械の照合: `uv run scripts/list_indications.py --match "<利用者の言葉>"`
      （在る名前と、疾患パックの `meta.aliases`・先例の `index.md` の「- 別名:」の行に、完全一致するか。大文字小文字・全角半角・空白・ハイフンは無視）
      - exit 0（一致）→ その名前を示し、「この名前でよいか」を一言で確かめる
      - exit 4（2 つ以上に一致）→ 候補を並べて選んでもらう
   2. exit 3（一致なし）→ `uv run scripts/list_indications.py` の一覧から、**医学的に同じ・近い**候補を Claude が示し、利用者に選んでもらう。
      - 同じ病気の別名（例 "アトピー性皮膚炎" と atopic_dermatitis）なら、その名前を候補の先頭に示す
      - 広い語・狭い語のずれ（例 "Eczema" は湿疹の総称で、アトピー性皮膚炎はその一型）は、**ずれを言葉で説明して**確かめる。黙って寄せない
      - どれにも当たらなければ、適応症から新しい名前を作って示す（英語の病名を小文字・`_` つなぎ）。★同じ適応症に別の名前を作らない
   3. 利用者が選んだ言葉が別名に無かったときは、「疾患パックの `meta.aliases`（または先例の index.md の別名の行）に足すと次から機械で一致する」と伝える（skill は書き換えない）
   4. 決めた名前で、次の 2 つを**別々に**確かめる（どちらも無くてよい。片方だけでもよい）:
      - 疾患パック `disease_packs/<indication_key>.yaml`: `meta.status: confirmed` なら使う。
        無い（または draft しか無い）ときは「Step 1e で CTG から下書きパックを作る」と伝えて進む。適応症で止めない。
      - 先例の材料 `precedents/<indication_key>/index.md`: 在れば Step 1g・Step 3 で使う。無ければ 1g を飛ばす。
   5. `intervention_metadata.json` に、決めた名前（`indication_key`）と利用者の元の言葉（`indication_input`）を両方書く。
   （`uv` が使えない環境では、Claude が `disease_packs/*.yaml` の `meta.aliases` と `precedents/*/index.md` の別名の行を読んで、同じ順で照合する）
3. 次の表を**一度に**見せて、埋められる所だけ埋めてもらう（全部埋まっていなくてよい）。
   利用者が `templates/step0_design_input.md`（入力シート）を埋めて貼ってきたら、その値を使う（空欄は下の「未記入なら」のとおり）。

| 欄 | 例（AD の場合／腫瘍の場合） | 未記入なら |
|---|---|---|
| product_name / code | "XYZ-123" | 必須（仮名可） |
| modality / mechanism | "anti-IL-13 mAb, SC" | 必須 |
| indication / population | "moderate-to-severe AD, adults" ／ "2L EGFRm NSCLC" | パックの既定 |
| phase | 3 | 3 |
| design | "randomized, double-blind, placebo-controlled, monotherapy" | パックの既定 |
| arms | [{"name":"XYZ 300 mg Q2W","loading":"600 mg Day 1"}, {"name":"Placebo"}] | [TBD] |
| allocation_ratio | "1:1" or "1:1:1" | [TBD] |
| treatment_period_weeks / primary_timepoint_week | 16 / 16 | パックの既定 |
| follow_up_weeks / extension | 12 / "LTE あり" | [TBD] |
| regions | ["US","EU","Japan"] | [TBD] |
| stratification | ["baseline severity","region"] ／ ["prior TKI","brain mets"] | パックの既定 |
| primary_endpoint_choice | "IGA 0/1 + EASI-75 co-primary" ／ "PFS by BICR" | パックの既定 |
| comparison | "superiority vs placebo" ／ "superiority vs docetaxel" ／ "non-inferiority" | superiority vs placebo |
| sample_size_inputs | power 0.9, alpha 0.05, dropout 0.10 | 左の値 |
| reference_nct_ids | ["NCT05398445"] | Step 1 で探す |
| sponsor_info | 社名・住所・医学専門家 | [TBD] |
| ib_known_risks | IB の要点（任意） | [TBD:IB] |

4. 書く JSON:

```json
{
  "intervention_id": "xyz-123",
  "intervention_type": "drug",
  "indication_key": "atopic_dermatitis",
  "indication_input": "アトピー性皮膚炎",
  "disease_pack": "<確定版のファイル名> or draft",
  "precedents": "precedents/<indication_key>/ or none",
  "user_design": { ... 上の表の欄 ... },
  "initial_context": "利用者が貼った資料の要点（あれば）",
  "created_date": "YYYY-MM-DD",
  "completed_steps": [0]
}
```

## 注意
- 医療機器の試験はこの版では対象外（旧版 `references/section_guides_v1.1.1/` の機器向けの道は未改訂）。
- 利用者が出していない用量・例数を推測で埋めない（E1）。
