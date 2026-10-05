# Step 2: 事実の正典（protocol_facts.json）と例数

## 目的
本文で何度も出てくる事実を 1 か所に確定させる（E2）。本文（Step 3）はこのファイルからだけ書く。

## 2a. 設計の型を決める
`assets/design_archetypes.yaml` から、主要評価項目の型（binary_responder / continuous_change / time_to_event / count_rate）と
比較の型（superiority_placebo / superiority_active / non_inferiority）を選び、facts の `design.archetype` に書く。
解析・欠測・中間事象の雛形・例数のコマンドはここから決まる（疾患パックが上書きしてよい）。

## 2b. protocol_facts.json を作る

材料: `intervention_metadata.json`（USER）・`01_ctg_reference.json`（CTG）・疾患パック（確定版 or `waypoints/disease_pack_draft.yaml`）（PACK）・archetype（STD）。
下の JSON の値は AD の場合の例。形はどの適応症でも同じ。
各値に `src` を付ける。USER > CTG（参照試験で一致しているもの）> PACK の順で採る。

```json
{
  "design": {"phase": 3, "type": "...", "arms": [...], "ratio": "1:1:1", "strata": [...],
             "periods": {"screening_days": "[TBD]", "treatment_weeks": 16, "follow_up_weeks": 12},
             "src": {"arms": "USER", "strata": "PACK:atopic_dermatitis"}},
  "population": {"inclusion": [{"text": "...", "src": "CTG:NCT05398445 + PACK"}], "exclusion": [...], "washout_table": [...]},
  "endpoints": [
    {"id": "P1", "level": "primary", "text": "Proportion of participants achieving vIGA-AD 0/1 with ≥2-point reduction from baseline at Week 16",
     "timepoint": "Week 16", "type": "binary", "src": "PACK + CTG"},
    {"id": "P2", "level": "primary", "text": "...EASI-75 at Week 16", "timepoint": "Week 16", "type": "binary"},
    {"id": "KS1", "level": "key_secondary", "...": "..."}
  ],
  "estimands": {"intercurrent_events": [{"ice": "Initiation of rescue therapy for AD", "strategy": "composite"},
                                        {"ice": "Permanent discontinuation of IP without rescue", "strategy": "treatment policy"}],
                "supportive": [...]},
  "rescue": [{"therapy": "...", "ip_action": "...", "estimand_ice": "Initiation of rescue therapy for AD"}],
  "multiplicity": {"coprimary": "conjunctive", "doses": "...", "key_secondary_order": ["KS1","KS2"]},
  "sample_size": {"see": "waypoints/sample_size.json"},
  "soa": {"visits": [{"name": "Screening", "week": "-5 to -1"}, {"name": "Day 1", "week": 0}, ...], "rows": "PACK:soa_rows"}
}
```

規則:
- `endpoints[].text` は本文の 1.1・3・10 節に**逐語で**入る（check_protocol C2）。後で言い換えない。
- `rescue[].estimand_ice` は `estimands.intercurrent_events[].ice` のどれかと同じ文字列（C4）。
- 評価項目の時点は `soa.visits` に必ず在る（C3）。
- key secondary は 4〜6 個に絞る（PACK:analysis / PREC:Lebri:s21/p28）。

## 2c. 例数（scripts/sample_size.py）

1. 仮定を集める: 疾患パックの `sample_size_priors.candidates`（出典つき）と、利用者の想定効果。
   **MCP では結果の数値は取れない**（has_results=true でも値なし）。数値は添付文書 14 節・論文から取り、`[PRIOR:<出典>]` を付ける。
   出典の無い仮定しか無い場合は、その旨を明記し、反応率を振った感度表を必ず付ける。
2. 実行。archetype ごとのコマンド:
   - binary_responder（単一）: `sample_size.py binary --p-control .. --p-active ..`
   - binary_responder（co-primary）: 下の例
   - continuous_change: `sample_size.py continuous --delta .. --sd .. --missing inflate`
   - time_to_event: `sample_size.py tte --hr .. --median-control .. --accrual .. --follow-up ..`
   - non_inferiority（二値）: `sample_size.py ni_binary --p-control .. --p-active .. --margin .. --alpha 0.025 --sides 1`
   - count_rate: 未対応 → `[TBD]` と統計担当への依頼を書く
   例（co-primary、2 用量 + プラセボ、1:1:1、NRI、脱落 10%）:

```bash
uv run scripts/sample_size.py coprimary \
  --p-control 0.10 0.15 --p-active 0.30 0.45 \
  --arms-active 2 --ratio 1 --alpha 0.05 --alpha-split bonferroni \
  --power 0.90 --dropout 0.10 --missing nri --rho 0.5 \
  --out waypoints/sample_size.json
```

3. **key secondary も計算する**: 表示を狙う key secondary（OS・反応率など）ごとに同じ script を `--label` 付きで回す。
4. **安全性曝露を決める**: `assets/design_archetypes.yaml` の `safety_exposure.applicability_by_family` で ICH E1 の適用を判定。
   - 適用: プログラム全体の目標（約 1500 例、6 か月 300–600 例、1 年 100 例、臨床用量で）のうち、この試験（＋延長試験）で賄う数を利用者に確認して `--exposure-n` に入れる。不明なら [TBD] とし、計算からは外して 10.11 に「未割当」と書く。
   - 対象外（例 腫瘍）: `--exposure-n 0 --exposure-reason "<理由>"`。
5. **最終例数**: `uv run scripts/sample_size.py combine --inputs <各 JSON> --exposure-n N --exposure-reason "..." --out waypoints/sample_size_final.json`
6. `sample_size_final.json` の `final_n_total` と `driven_by`、各要素の数を `protocol_facts.json` に写す（数値は写すだけ。手で丸めない）。
7. 参照試験の実登録数（CTG `enrollment`）は「同規模の先例」として 10.11 節の根拠に書く（新試験の例数そのものではない）。

## 2d. 確認の停止
次の 5 点だけを表で利用者に見せ、OK をもらってから Step 3 へ:
群と割付比／主要評価項目と時点／中間事象と戦略／key secondary の順序／例数（総数と主な仮定）。
下書きパックを使った場合は、パックの inclusion・endpoints.primary・rescue_table の行も一緒に見せる。
