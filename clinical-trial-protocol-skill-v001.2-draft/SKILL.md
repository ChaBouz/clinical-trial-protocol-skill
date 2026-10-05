---
name: clinical-trial-protocol-skill-v001
description: 医薬品の第2/3相臨床試験のフルプロトコル（ICH M11 形式）を、適応症を問わず、ClinicalTrials.gov の登録情報（MCP）・設計の型・疾患パック（無ければ CTG から下書き）から、出典ラベルつきで作成する。「プロトコルを作って」「〇〇の第3相のプロトコル案」「臨床試験計画書のドラフト」「Create a clinical trial protocol」などで使う。
---

# Clinical Trial Protocol Skill v001.2（DRAFT 2026-10-04）

> 改変の表示（Apache License 2.0 §4(b)）: Anthropic の sample skill「clinical-trial-protocol-skill」v1.1.1 を、2026 年に Tad が改変・書き直したもの。由来と変更の一覧は `NOTICE`・`CHANGELOG.md`、ライセンスは `LICENSE`。

## 0. この skill の考え方（最初に読む）

ClinicalTrials.gov（以下 CTG）から MCP で取れるのは**プロトコルの要旨**である。
参照試験 NCT05398445 で実測すると、適格基準は CTG で選択 6・除外 3 項目、プロトコルでは選択 12・除外 30 項目。
MCP の `get_trial_details` は群・用量・割付・盲検・結果の数値を返さない（CTG には在る。取り方は `references/01-research.md` 1a-2）。
∴ CTG を全部引用してもプロトコルにはならない。この skill は次の 4 つで「枠を埋める」（どれも適応症に依存しない形）:

1. **枠と粒度** — `assets/section_spec_m11.yaml`（ICH M11 の 14 節、節ごとの必須項目・深さ・目安頁数・情報源）。
   節番号と見出しは**ここからだけ**取る。指示書の中に節番号を手で書かない。
2. **設計の型** — `assets/design_archetypes.yaml`（主要評価項目の型 × 比較の型 → estimand の雛形・解析・欠測・多重性・例数のコマンド。疾患領域ごとの重み付け）。
3. **疾患パック** — `disease_packs/<disease>.yaml`（形は `disease_packs/_schema.yaml`）。確定版が無い適応症は、Step 1e が CTG の参照試験 5 本から
   **下書きパック** `waypoints/disease_pack_draft.yaml` を作る。`atopic_dermatitis.yaml` は確定版の一例（status: draft、未確認）。
4. **膨らませ規則** — CTG の事実 → 疾患パック → 規制/GCP の定型（`assets/NIH-FDA-Protocol-Template_STD-library.md` を文例集として使う）の順で肉付けし、すべての段落・表の行に**出典ラベル**を付ける。

### 出典ラベル（本文に付ける）

| ラベル | 意味 |
|---|---|
| `[USER]` | 利用者が Step 0 で決めた設計（群・用量・割付比・期間・地域） |
| `[CTG:<NCT>:<field>]` | CTG の登録情報から引用 |
| `[PACK:<disease>]` | 疾患パックの既定値 |
| `[PREC:<ID>]` | 当局の先例（FDA の会議録・書簡など）。`precedents/<適応症>/` の逐語を読んで付ける（Step 1g。材料は任意）か、疾患パックの `PREC:` を写す。ID の実在は `scripts/check_prec_ids.py` が照らす |
| `[STD]` | ICH E6(R3)/E9(R1)/21 CFR などの定型 |
| `[PRIOR:<出典>]` | 例数の仮定に使う公表結果（添付文書・論文） |
| `[INSTR:<尺度>:<確認日>]` | 評価尺度の版。開発者・権利者の公式情報で確認した日付つき（Step 1f） |
| `[DERIVED]` | 上の材料から Claude が膨らませた記述（要レビュー） |
| `[TBD]` / `[TBD:<何>]` | スポンサーが埋める値 |

### 絶対に守ること

- **E1 数値は出典があるときだけ書く。** 用量・閾値・例数・期間・割合に出典（USER/CTG/PACK/PREC/PRIOR/計算結果）が無ければ `[TBD]`。推測で埋めない。
  PREC を出典にできる数値は、`precedents/` の逐語のファイル（または疾患パックが指す原本）に**逐語で在る**ものだけ。記憶にある先例は出典にならない（ID を書けないものは書かない）。
- **E2 同じ事実は 1 か所。** 目的・評価項目・群・時点・救済療法・中間事象は `waypoints/protocol_facts.json` に置き、全節はそこから書く（言い換えない）。
- **E3 参照試験の固有情報を新試験に写さない。** 参照試験のスポンサー名・薬剤名・施設名・連絡先は使わない。使うのは「形」と「標準値」だけ。
- **E4 depth の守り:** `full` は「誰が・いつ・何を・どの基準で・記録先」まで。`summary` は要点と参照先。`pointer` は参照のみ。

## 1. 前提

- **ClinicalTrials.gov の MCP**（任意だが推奨）: `get_trial_details`, `analyze_endpoints`, `search_trials`, `search_by_eligibility`。
- **clinicaltrials.gov への直接の通信**（任意）: `scripts/ctg_fetch.py`（1 試験の全記録、または検索）。
  MCP も通信も無ければ、利用者が手で置いた CTG の JSON を読む。それも無ければ CTG なしで進む（01-research 1a の順。工程は止めない）。
- **Python**: `uv run scripts/<name>.py`（PEP 723。依存は script の頭に書いてある）。`uv` が無ければ `pip install -r scripts/requirements.txt` のあと `python`。
- **任意: 当局の先例の材料**（`precedents/<適応症>/`。形は `precedents/README.md`）。無ければ Step 1g を飛ばす（工程は止めない）。

### 道の決まり（★全 Step 共通）

- **SKILL_DIR** ＝ この SKILL.md のあるフォルダ。`scripts/`・`assets/`・`references/`・`disease_packs/`・`precedents/`・`templates/` は SKILL_DIR からの道。
  同じ場所に別の版の skill（例 `clinical-trial-protocol-skill-v1.1.1`）が在っても、**SKILL_DIR の中のファイルだけを読む**。
- **作業フォルダ** ＝ 利用者が指定した場所。指定が無ければ `<作業を始めたフォルダ>/runs/<intervention_id>/`（`intervention_id` は Step 0 で製品名から作る。例 `xyz-123`）。
  指示書の `waypoints/…` は `<作業フォルダ>/waypoints/…` と読む。**SKILL_DIR の中には何も書かない**。
- script は SKILL_DIR からの道で呼ぶ（例 作業を始めたフォルダが SKILL_DIR の親なら `uv run <SKILL_DIR の名前>/scripts/sample_size.py …`）。
  spec などの引数も同じ（例 `--spec <SKILL_DIR>/assets/section_spec_m11.yaml`）。

## 2. 手順（waypoints/ に途中結果を置き、どこからでも再開できる）

| Step | 読む指示書 | 出力 |
|---|---|---|
| 0 設計の入力 | `references/00-initialize.md` | `waypoints/intervention_metadata.json`（適応症の名前 `indication_key` を含む） |
| 1 材料集め | `references/01-research.md` | `waypoints/01_ctg_reference.json`, `waypoints/01_research_summary.md`, `waypoints/instrument_versions.json`, `waypoints/01_precedents.md` |
| 2 事実の正典と例数 | `references/02-facts-and-sample-size.md` | `waypoints/protocol_facts.json`, `waypoints/sample_size.json` |
| 3 本文を書く（章ごとに 12 回） | `references/03-write-sections.md` | `waypoints/sec_01.md`〜`sec_12.md` |
| 4 連結と検査 | `references/04-assemble-and-check.md` | `waypoints/protocol_complete.md`, `waypoints/check_report.json` |

- 指示書は**その Step を実行するときに初めて読む**（先読みしない）。
- 各 Step の終わりに `intervention_metadata.json` の `completed_steps` を更新する。
- Step 2 の後で一度止まり、`protocol_facts.json` の要点（群・主要評価項目・estimand・例数）を利用者に見せて確認を取る。
  ここが合っていれば以降の本文は機械的に揃う。

## 3. 開始時（利用者の依頼が短くても、ここで全部そろえる）

1. **環境を確かめて 1 行ずつ表示する**（利用者に頼まれなくても行う。どれも無くて止めない）:
   - ClinicalTrials.gov の MCP: 使えるか（`search_trials` を 1 回、`page_size=1` で呼ぶ）
   - clinicaltrials.gov への通信: `uv run <SKILL_DIR>/scripts/ctg_fetch.py NCT05398445 --out <一時ファイル>` が exit 0 か
   - `uv`: `uv --version`（無ければ `python3` と requirements.txt で代える）
   - 先例の材料と疾患パック: `uv run <SKILL_DIR>/scripts/list_indications.py` の一覧
   MCP も通信も使えないときは、「参照試験の情報が取れない。CTG の JSON を手で置けば使える（README §6-4）。このまま進めると、
   参照試験に由来する基準・評価項目は [TBD] が増える」と伝えて、続けるかを聞く。
2. **進行中の作業を探す**: `<作業を始めたフォルダ>/runs/*/waypoints/intervention_metadata.json` を一覧にする。
3. 表示して、利用者の選択を待つ:
```
🧬 CLINICAL TRIAL PROTOCOL v001.2（ICH M11）
環境: CTG MCP <可/不可> ／ CTG 通信 <可/不可> ／ uv <可/不可> ／ 先例の材料 <在る名前 or なし>
[進行中があれば] 進行中: runs/<id>/ <薬剤名> / 完了: <steps> / 次: <step>

1. 研究のみ（Step 0–1）: 参照試験と先例の要約
2. フルプロトコル（Step 0–4）
3. 進行中の作業を続ける
4. 終了
```
   利用者の最初の依頼に適応症・相・モードが書いてあれば、それを使い、聞き直さない（例「wAMD の第 3 相のプロトコルを作って」→ モード 2、適応症 "wAMD"、相 3 として Step 0 へ）。

## 4. 参照ファイル

- `assets/section_spec_m11.yaml` — 枠と粒度（正典）
- `assets/ctg_mcp_field_map.yaml` — MCP の欄 → M11 の節
- `assets/design_archetypes.yaml` — 設計の型（適応症に依存しない）
- `assets/NIH-FDA-Protocol-Template_STD-library.md` — 定型文の文例集（AE 定義・監査・同意 等）。**構成には使わない**
- `disease_packs/_schema.yaml` — 疾患パックの形。`disease_packs/atopic_dermatitis.yaml` はその一例
- `references/section_guides.md` — M11 の節 → 旧版の詳しい書き方（`references/section_guides_v1.1.1/`）の対応表と、旧版を読むときの規則
- `reference_protocols/` — 利用者が任意で置くフルプロトコル PDF（粒度の確認用。必須ではない）
- `scripts/sample_size.py` — 例数（二値・co-primary・連続量・生存時間・非劣性、多群、NRI）
- `scripts/check_protocol.py` — 整合性検査
- `scripts/validate_pack.py` — 疾患パック（確定版・下書き）の形の検査
- `scripts/ctg_fetch.py` — CTG API v2 の全記録を取る（通信できる環境のみ）
- `precedents/<適応症>/` — （任意）当局の先例の逐語。利用者が用意して置く。置く形は `precedents/README.md`、雛形は `precedents/_template/`。無ければ Step 1g を飛ばす
- `disease_packs/_template.yaml` — 疾患パックの雛形（人が作るとき用）。`_` で始まるファイル・フォルダは雛形なので、パックや材料として使わない
- `templates/step0_design_input.md` — Step 0 の入力シート（人が埋めて貼る）
- `scripts/validate_precedents.py` — 先例の材料の形の検査
- `scripts/list_indications.py` — 適応症の名前（indication_key）の一覧と、利用者の言葉の照合（Step 0）
- `README.md` — 人のための使い方（Claude の指示の正典はこの SKILL.md と references/）
- `scripts/check_prec_ids.py` — 本文・パックの `PREC:` の ID が実在するかの検査
- `scripts/requirements.txt` — 全 script の依存の和（uv を使わない環境向け。正典は各 script の頭の PEP 723）

## 5. 免責（最終サマリーに必ず表示）

この版（v001.2）は Claude（Cowork）との対話で作成・改変したものであり、指示書・道具・出力の正確性と安全性は完全には確認されていない。

本 skill の出力は予備的な草案であり、規制当局・IRB の判断や医学/法務/規制の助言ではない。
統計担当による例数の確認、当局との事前相談（Pre-IND / EOP2 等）、IRB 審査、`[TBD]` と `[DERIVED]` のレビューが必要。
