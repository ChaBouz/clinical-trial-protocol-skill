# Clinical Trial Protocol Skill v001.2（DRAFT）— 使い方

> **ライセンスと由来**: Apache License 2.0（`LICENSE`）。Anthropic が公開した sample skill「clinical-trial-protocol-skill」v1.1.1（[anthropics/life-sciences](https://github.com/anthropics/life-sciences)）を元に、2026 年に Tad が改変・拡張したもので、Anthropic の公式版ではありません。
> v1.1.1 から変更せずに含めたファイル・改変したファイルの一覧は `NOTICE`、変更の履歴は `CHANGELOG.md` にあります。
> 版の名前「v001.2」は、Anthropic の版（v1.x）と取り違えないための、この系統だけの名前です。
>
> **★作り方と安全性について**: この版は、Tad が Claude（Cowork）との対話で作成・改変したものです。
> 指示書・道具（scripts）・出力の正確性と安全性は、作者が完全には確認できていません。使う人の責任で中身をレビューし、
> 出力は必ず専門家（臨床・統計・薬事）が確認してください。

医薬品の第 2/3 相臨床試験の**治験実施計画書（プロトコル）の草案**を、ICH M11（臨床試験プロトコルの国際的な共通様式）の 14 節で書く Claude の skill です。
適応症を問いません。すべての段落・表の行に**出典ラベル**（どの情報から書いたか）が付き、出典の無い数値は空欄（`[TBD]`）として残ります。

- skill とは: Claude に渡す「手順書と道具のひとまとまり」。このフォルダ全体が 1 つの skill です（Claude が最初に読むのは `SKILL.md`）
- この README は**人が読む説明書**です。Claude への指示の正典は `SKILL.md` と `references/` です

> ★出力は予備的な草案です。規制当局・IRB の判断や医学・法務・規制の助言ではありません。
> 統計担当による例数の確認、当局との事前相談、IRB 審査、`[TBD]` と `[DERIVED]` のレビューが必要です。

---

## 1. 全体の流れ

```
準備（1 回だけ）            始める                      Claude が進める                         人が見る
─────────────────    ───────────────────    ──────────────────────────────    ─────────────────
リポジトリに            「…の SKILL.md に従って、    環境の確認 → Step 0（設計を聞く）        Step 0 で答える
このフォルダを置く        <適応症> の第 3 相の         → Step 1（材料集め）                    Step 2 の後で確かめる
                      プロトコルを作って」         → Step 2（事実と例数）→ ★止まる         できあがりをレビュー
                                               → Step 3（本文 12 回）→ Step 4（検査）
```

前もって作るものはありません。疾患パック（§6-1）・先例の材料（§6-2）が無くても最後まで動きます。

## 2. 準備（1 回だけ）

### 2-1. リポジトリに置く

GitHub のリポジトリ（Claude Code で開くもの）の**直下**に、このフォルダを名前を変えずに置きます。別の版の skill が隣に在ってもかまいません。

```
<リポジトリ>/
├── clinical-trial-protocol-skill-v001.2-draft/   ← このフォルダ
└── （ほかのフォルダ。例 旧版 clinical-trial-protocol-skill-v1.1.1/ が在ってもよい）
```

作業の結果は、実行すると `<リポジトリ>/runs/<作業の名前>/` にできます（このフォルダの中には書きません）。

### 2-2. Claude Code で開く

Claude Code でこのリポジトリを開きます（GitHub に接続した Claude Code でも、手元の Claude Code でも同じ）。
`uv`（Python の実行の道具）や通信の可否は、始めたときに Claude が自動で確かめて表示します。

### 2-3. 任意: ClinicalTrials.gov のコネクタ

ClinicalTrials.gov（米国の臨床試験登録サイト。以下 CTG）のコネクタ（MCP: Claude に外部のデータを読ませる仕組み）を Claude Code に接続すると、
似た試験の登録情報を引けるので、適格基準や評価項目の質が上がります。無くても動きます（§6-4）。

## 3. 始め方（最初の依頼は 1 文）

Claude Code に次の 1 文を送ります。`<適応症>` は日本語・英語・略号のどれでもかまいません。

```
clinical-trial-protocol-skill-v001.2-draft の SKILL.md に従って、<適応症> の第 3 相のプロトコルを作って
```

例: `clinical-trial-protocol-skill-v001.2-draft の SKILL.md に従って、wAMD の第 3 相のプロトコルを作って`

- **フォルダ名を書く理由**: リポジトリに置いただけのフォルダは、Claude Code が skill として自動では読み込みません。
  また、旧版が隣に在ると同じ skill 名なので取り違えるおそれがあります。フォルダ名を書けば、その版だけが使われます
- 研究（材料集め）だけでよければ「…のプロトコルの材料集めだけして」と書きます（Step 0〜1 で止まる）
- それ以外の指定（作業フォルダの場所、環境の確認、旧版を使わないこと）は SKILL.md に書いてあるので、依頼に書く必要はありません

送ると、Claude は最初に次のような表示を出します:

```
🧬 CLINICAL TRIAL PROTOCOL v001.2（ICH M11）
環境: CTG MCP 可 ／ CTG 通信 不可 ／ uv 可 ／ 先例の材料 neovascular_amd
1. 研究のみ  2. フルプロトコル  3. 進行中の作業を続ける  4. 終了
```

CTG の MCP も通信も「不可」のときは、続けるかを聞かれます（続けると参照試験に由来する所が `[TBD]` になる。手で補うなら §6-4）。

## 4. 進み方と、人がすること

| Step | Claude がすること | 人がすること | できるファイル（`runs/<作業の名前>/waypoints/` の下） |
|---|---|---|---|
| 0 設計の入力 | 適応症の名前を決め、設計を聞く | ★答える（§4-1） | `intervention_metadata.json` |
| 1 材料集め | CTG から参照試験 5 本、疾患パックの下書き、評価尺度の最新版、先例 | — | `01_research_summary.md` ほか |
| 2 事実と例数 | 目的・評価項目・群・時点・救済療法・中間事象を 1 か所に固め、例数を計算 | ★**止まるので確かめる**（§4-2） | `protocol_facts.json`, `sample_size*.json` |
| 3 本文 | 章ごとに 12 回に分けて書き、各回で分量を検査 | — | `sec_01.md`〜`sec_12.md` |
| 4 連結と検査 | 全文をつなぎ、番号・食い違い・分量・先例の ID を検査 | ★レビューする（§4-3） | `protocol_complete.md`, `check_report.json` |

### 4-1. Step 0 で答えること

- **適応症の名前**: Claude が、在る名前と別名に照らして候補を示すので、確かめて答えます。
  - 例: "アトピー性皮膚炎" "AD" は `atopic_dermatitis` に機械で一致する（疾患パックに別名が書いてある）
  - 一致しない言葉は、Claude が医学的に近い候補を示します。広い語と狭い語のずれ（例 "Eczema" は湿疹の総称、アトピー性皮膚炎はその一型）は説明して確かめます。黙って寄せることはありません
  - 該当が無ければ新しい名前（英語の病名を小文字・`_` つなぎ。例 `plaque_psoriasis`）を作ります
- **設計**: 表が出るので、分かる所だけ答えます。`templates/step0_design_input.md` を埋めて貼ってもかまいません。空欄は `[TBD]` のまま残ります（推測で埋まらない）

### 4-2. Step 2 の後で確かめること（ここが一番大事）

Claude が次を示して止まります。ここが合っていれば、以降の本文は同じ事実から機械的にそろいます。

1. 群（用量・頻度）と割付比
2. 主要評価項目・時点と、比べ方（優越性か非劣性か）
3. estimand（何をどう推定するかの枠組み。中間事象とその扱い）
4. 例数（どの仮定から、何に対する何例か）
5. 疾患パックが下書きなら、その要点（疾患領域 `therapeutic_area_family` が合っているか。合う領域が無ければ `general` と示される）

直したい所は言葉で伝えれば、Claude が `protocol_facts.json` を直してから先へ進みます。

### 4-3. できあがりとレビュー

- 全文: `runs/<作業の名前>/waypoints/protocol_complete.md`
- 検査の結果: `check_report.json`（食い違いの数、節ごとの `[TBD]` の数、ラベルの数）
- レビューの順: ① `[DERIVED]` の段落（Claude が膨らませた所）② `[TBD]` の一覧（スポンサーが埋める所）③ 検査で落ちた所

### 4-4. 続きから

途中で止まっても、同じ 1 文（または「続きから」）を送れば、Claude が `runs/` の中の進行中の作業を示し、次の Step から再開します。

## 5. 出典ラベルと 4 つの決まり

| ラベル | 意味 |
|---|---|
| `[USER]` | 利用者が Step 0 で決めた設計 |
| `[CTG:<NCT>:<欄>]` | ClinicalTrials.gov の登録情報 |
| `[PACK:<適応症>]` | 疾患パックの既定値 |
| `[PREC:<ID>]` | 当局の先例（会議録・書簡など）。先例の材料か疾患パックに在る ID だけ |
| `[STD]` | ICH E6(R3)/E9(R1)・21 CFR などの定型 |
| `[PRIOR:<出典>]` | 例数の仮定に使った公表結果（添付文書・論文） |
| `[INSTR:<尺度>:<確認日>]` | 評価尺度の版。開発者・権利者の公式情報で確認した日付つき |
| `[DERIVED]` | 上の材料から Claude が膨らませた記述（★要レビュー） |
| `[TBD]` / `[TBD:<何>]` | スポンサーが埋める値 |

- **E1** 数値は出典があるときだけ書く。無ければ `[TBD]`（推測で埋めない）
- **E2** 同じ事実は 1 か所（`protocol_facts.json`）に置き、全節はそこから書く
- **E3** 参照試験のスポンサー名・薬剤名・施設名・連絡先を新試験に写さない
- **E4** 詳しく書く節は「誰が・いつ・何を・どの基準で・記録先」まで書く

## 6. 質を上げる任意の材料

どれも任意で、互いに独立です。疾患パックと先例は、**適応症の名前（`indication_key`）が同じこと**だけで結び付きます。

```
clinical-trial-protocol-skill-v001.2-draft/
├── disease_packs/<indication_key>.yaml   … 疾患パック（確定版なら使う／無ければ CTG から下書き）
└── precedents/<indication_key>/          … 先例の材料（在れば使う／無ければ飛ばす）
```

★同じ適応症には同じ名前を使う（`atopic_dermatitis` が在るのに `ad` を作らない）。名前が違うと別の適応症として扱われます。
在る名前の一覧: `uv run clinical-trial-protocol-skill-v001.2-draft/scripts/list_indications.py`（リポジトリの直下で）

### 6-1. 疾患パック（`disease_packs/<indication_key>.yaml`）

適応症に固有の「書き始めの値」（選択・除外基準、ウォッシュアウト、評価項目、尺度、救済療法、estimand、解析、例数の仮定、安全性の監視、来院の行）をまとめた YAML ファイル（字下げで構造を表す設定ファイル）。

1. 雛形 `disease_packs/_template.yaml` を `disease_packs/<indication_key>.yaml` としてコピーする（★先頭の `_` を外す。`_` で始まるものは雛形として無視される）
2. 頭のコメントに沿って「★書く」「★選ぶ」の所を埋める。分からない値は `"[TBD]"` のまま。別名（`meta.aliases`）も書いておくと Step 0 で機械で一致する
3. 各行の `src` に出典を書く（`CTG:<NCT>` / `REF:<節>` / `PREC:<ID>` / `PI:<ラベル>` / `GUIDANCE:<名前>` / `STD` / `DERIVED`）
4. 検査: `uv run scripts/validate_pack.py disease_packs/<indication_key>.yaml` → `OK`（このフォルダで）
5. 臨床・統計の担当が確認したら `meta.status: confirmed` にする（★`draft` のままだと使われず、CTG からの下書きが使われる）

楽な作り方: 一度パック無しで回すと、Step 1 が `runs/<作業の名前>/waypoints/disease_pack_draft.yaml` を作ります。それをコピーして直すと早い。
形の正典は `disease_packs/_schema.yaml`、実例は `disease_packs/atopic_dermatitis.yaml`（`status: draft`）。

### 6-2. 先例の材料（`precedents/<indication_key>/`）

当局と企業のやり取り（例: FDA の会議録・書簡。米国では Drugs@FDA の承認パッケージの「Administrative and Correspondence Documents」で公開）の**原文の逐語**を置くと、
Claude はそれを読んで、当局が求めたこと（例: 欠測の扱いの詳細、安全性データベースの大きさ）を `[PREC]` つきで本文に書きます。
使われるのは Step 1（先例を選んで `01_precedents.md` にまとめる）・Step 3（章ごとに読む）・Step 4（ID の検査）です。

作り方: 雛形 `precedents/_template/` を `precedents/<indication_key>/` にコピーして書き換える。形の約束は `precedents/README.md`。
検査: `uv run scripts/validate_precedents.py precedents/<indication_key>` → 「問題 0 件」（このフォルダで）

### 6-3. 参照プロトコル（`reference_protocols/`）

手元のフルプロトコルの PDF を置くと、Step 1 で節ごとの頁数を数え、分量の目安と比べます。

### 6-4. CTG の情報を手で渡す（コネクタも通信も使えないとき）

1. ブラウザで `https://clinicaltrials.gov/api/v2/studies/<NCT番号>?format=json` を開き、`<NCT番号>.json` として保存する（参照にしたい試験ごと。5 本まで）
2. `runs/<作業の名前>/waypoints/ctg/` に置く（作業の名前は Step 0 で Claude が表示する）
3. Claude に「ctg に JSON を置いた」と伝える → Step 1 がそれを読む

### 6-5. 疾患領域（`therapeutic_area_family`）

疾患領域ごとの重み付け（例 腫瘍なら用量調整の表、眼科なら試験眼の選び方）は `assets/design_archetypes.yaml` にあります
（oncology / immunology_inflammation / cardiometabolic / neuroscience / respiratory / infectious_disease / ophthalmology）。
**合う領域が無くても何もしなくてよい**: 受け皿の `general`（重み付けなし）が使われ、Step 2 の確認で示されます。
重み付けを足したいときだけ、`therapeutic_area_families` に既存の領域と同じ形で 1 項目足します（任意・上級）。

## 7. 道具（scripts）

Claude が工程の中で自動で回します。人が回すときは、このフォルダで `uv run scripts/<名前>.py`（`uv` が無ければ `pip install -r scripts/requirements.txt` のあと `python scripts/<名前>.py`）。

| 道具 | 何をするか | 例（このフォルダで） |
|---|---|---|
| `list_indications.py` | 適応症の名前の一覧と、言葉の照合 | `uv run scripts/list_indications.py --match "アトピー性皮膚炎"` |
| `validate_pack.py` | 疾患パックの形の検査 | `uv run scripts/validate_pack.py disease_packs/<indication_key>.yaml` |
| `validate_precedents.py` | 先例の材料の形の検査 | `uv run scripts/validate_precedents.py precedents/<indication_key>` |
| `check_prec_ids.py` | `[PREC]` の ID が、同じ適応症の先例の材料（と疾患パック）に実在するか | `uv run scripts/check_prec_ids.py disease_packs/<indication_key>.yaml`（本文なら `--indication <indication_key> <ファイル>`） |
| `sample_size.py` | 例数（二値・co-primary・連続量・生存時間・非劣性・多群・NRI） | `uv run scripts/sample_size.py binary --p-control 0.10 --p-active 0.38 --power 0.9 --dropout 0 --missing inflate --alpha-split none` |
| `check_protocol.py` | 全文の検査（見出しの番号・節どうしの食い違い・分量） | `uv run scripts/check_protocol.py <全文.md> --spec assets/section_spec_m11.yaml --facts <protocol_facts.json>` |
| `ctg_fetch.py` | CTG の 1 試験の全記録、または検索（通信できる環境だけ） | `uv run scripts/ctg_fetch.py NCT01234567 --out x.json` |

co-primary: 2 つの主要評価項目の両方で有意であることを成功とする設計。NRI: 欠測を「反応しなかった」とみなす扱い。

## 8. フォルダの中身

| 場所 | 何か | 人が触るか |
|---|---|---|
| `SKILL.md` | Claude が最初に読む指示 | 触らない |
| `references/` | 各 Step の詳しい指示と、節ごとの書き方 | 触らない |
| `assets/` | M11 の枠（`section_spec_m11.yaml`）・設計の型と疾患領域（`design_archetypes.yaml`）・CTG の欄の対応・定型文の文例集 | 領域を足すときだけ（§6-5） |
| `disease_packs/` | 形の正典 `_schema.yaml`・雛形 `_template.yaml`・疾患パック | ★パックを作る（§6-1） |
| `precedents/` | 形の約束 `README.md`・雛形 `_template/`・先例の材料 | ★材料を置く（§6-2） |
| `templates/step0_design_input.md` | Step 0 の入力シート | 写して埋める |
| `reference_protocols/` | 参照プロトコル | 置く（§6-3） |
| `scripts/` | 道具（§7）と `requirements.txt` | 回す |
| `CHANGELOG.md` | 変更の記録 | 読む |
| `LICENSE` ・ `NOTICE` | ライセンス（Apache License 2.0）と、由来・元の版から変えたファイルの一覧 | 配るときは必ず一緒に置く |

## 9. よくある質問

**Q. 依頼の 1 文に、フォルダ名を書かないとどうなりますか？**
A. Claude Code がこの skill を見つけられないか、隣の旧版を使うおそれがあります。必ずフォルダ名を書いてください。
（このフォルダを Claude Code の skills の置き場所 `.claude/skills/` に置けば、フォルダ名なしでも使えます。その場合は旧版を同じ所に置かない）

**Q. 疾患パックが無い適応症でも使えますか？**
A. 使えます。Step 1 が CTG の参照試験 5 本から下書きのパックを作り、Step 2 の確認で示します（確定版ではないと明記されます）。

**Q. `[TBD]` がたくさん残ります。**
A. 仕様です。出典の無い数値を推測で埋めない（E1）ので、用量の根拠・CMC・IB の数値・連絡先などは空欄で残ります。

**Q. 先例の材料はどこで手に入りますか？**
A. 米国なら Drugs@FDA の承認パッケージの会議録・書簡が公開されています。原文を `precedents/_template/` の形で置いてください（§6-2）。

**Q. 結果の `runs/` を GitHub に残したくありません。**
A. リポジトリの直下の `.gitignore` に `runs/` と書いてください。

**Q. 医療機器の試験に使えますか？**
A. この版は医薬品だけです（機器の道は未改訂）。
