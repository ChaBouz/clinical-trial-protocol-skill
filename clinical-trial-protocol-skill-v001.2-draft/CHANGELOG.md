# CHANGELOG

## v001.2-draft（2026-10-05, 12 回目）— 版の名前の変更と公開の準備
- **版の名前を v1.2-draft → v001.2-draft に変更**（Anthropic の版 v1.x と取り違えないため。この系統だけの名前）。
  フォルダ名を `clinical-trial-protocol-skill-v001.2-draft/` に、SKILL.md の skill の名前を `clinical-trial-protocol-skill-v001` に変更（旧版 v1.1.1 と同じ名前で取り違えるのを防ぐ）。
  以下の履歴の「v1.2-draft」は、この版の改名前の呼び名
- 作者の表示を Tad に。README・NOTICE・SKILL.md の免責に「Claude（Cowork）との対話で作成・改変した。正確性と安全性は完全には確認していない」を明記
- NOTICE に、同梱の先例の材料（precedents/neovascular_amd。Drugs@FDA で公開された FDA コレスポンデンスの逐語）の説明を追加

## v1.2-draft 追補（2026-10-05, 11 回目）— 公開のためのライセンス表示
- 元の v1.1.1（Anthropic の anthropics/life-sciences）が Apache License 2.0 であることを確認（元のフォルダの LICENSE）
- 新設 `LICENSE`（Apache License 2.0 の全文）、`NOTICE`（由来・v1.1.1 から変更せずに含めたファイル 8 個・改変したファイル・新しく書いたファイル・Anthropic の公式版ではないこと）
- `SKILL.md`・`README.md` の頭に改変の表示（Apache License 2.0 §4(b)）を追加。README に「ライセンスと由来」

## v1.2-draft 追補（2026-10-05, 10 回目）— 初めての人が README だけで動かせるように整理
- **最初の依頼を 1 文に**: SKILL.md「開始時」で、環境の確認（CTG MCP・CTG 通信・uv・先例の材料と疾患パックの一覧）、進行中の作業の一覧、
  依頼文からのモード・適応症・相の読み取りを Claude が自分で行う。依頼は「<フォルダ名> の SKILL.md に従って、<適応症> の第 3 相のプロトコルを作って」だけ
- **作業フォルダの既定**: `<作業を始めたフォルダ>/runs/<intervention_id>/`。指示書の `waypoints/` はその下。skill のフォルダの中には書かない（SKILL.md「道の決まり」・00-initialize）
- **疾患領域の受け皿 `general`**（design_archetypes）: 合う領域が無いとき Step 1e はこれを選び、Step 2 で伝える。新しい領域をその場で作らない → 人が事前に領域を足す手順は不要に
- **CTG の代わりの順**（01-research 1a）: MCP → `ctg_fetch.py search`（新設の検索。★通信できる環境で未検証）→ 利用者が手で置いた JSON（README §6-4）→ CTG なし
- **`check_prec_ids.py` を同じ適応症の材料だけで照らすように**（`--indication`。パックはファイル名から決まる）。
  以前は別の適応症の先例が置かれていると、それを既知の ID に数え、AD パックの正しい ID 35 個を「実在しない」と誤って落としていた（2026-10-05 の通しの確認で発見）
- README を作り直した（全体の流れ・リポジトリへの置き方・1 文の始め方・Step ごとに人がすること・Step 2 で見る 5 点・できあがりの場所・続きから・任意の材料・CTG を手で渡す方法・疾患領域）
- 新設 `.gitignore`（.DS_Store・__pycache__・waypoints/・runs/）

## v1.2-draft 追補（2026-10-04, 9 回目）— 眼科と、リポジトリから使うとき
- `assets/design_archetypes.yaml` に `ophthalmology`（眼科）の疾患領域を追加（既定の評価項目の型＝連続量、study eye／fellow eye、中央判定の画像、眼の安全性）。
  それまで眼科の選択肢が無く、Step 1e の下書きパックが `validate_pack.py` で落ちるか、合わない領域を選ぶしかなかった。中身は一般的な既定で要レビュー
- SKILL.md の前提に「道の決まり」: scripts/ などは SKILL_DIR から、`waypoints/` は作業フォルダから（SKILL_DIR の中に作らない）。同じ場所に別の版が在っても、この SKILL_DIR だけを読む
- README §2-1: skills の置き場所に置かずにリポジトリから使うときの最初の依頼の例（読む SKILL.md・作業フォルダ・旧版を使わないことを指定）

## v1.2-draft 追補（2026-10-04, 8 回目）— 適応症の名前の揺れ
- Step 0 の名前の決め方を 2 段に: ①`scripts/list_indications.py --match` で、在る名前と**別名**に機械で完全一致（大文字小文字・全角半角・空白・ハイフンは無視）
  ②一致しなければ Claude が医学的に同じ・近い候補を示し、**利用者が選ぶ**。広い語と狭い語のずれ（例 "Eczema" と atopic_dermatitis）は説明して確かめ、黙って寄せない
- 別名の置き場所: 疾患パックの `meta.aliases`（`_schema.yaml` の optional に追加）、先例の `index.md` の「- 別名:」の行（`precedents/README.md` に追加）
- `atopic_dermatitis.yaml` に別名（atopic dermatitis, AD, atopic eczema, アトピー性皮膚炎）。広すぎる "eczema" は入れていない
- 新設 `scripts/list_indications.py`（一覧と照合。一致 exit 0／一致なし exit 3／複数 exit 4）。`intervention_metadata.json` に利用者の元の言葉 `indication_input` を追加
- 入力シートの適応症の欄を「日本語・英語・略号のどれでもよい」に。README に「名前の揺れ」と「先例はどこで使われるか」を追加
- 確認（2026-10-04）: "アトピー性皮膚炎"・"Atopic-Dermatitis"・"ad"・"atopic eczema" → atopic_dermatitis に一致（exit 0）、"Eczema" → 一致なし（exit 3）

## v1.2-draft 追補（2026-10-04, 7 回目）— 人のための説明書と雛形
- 新設 `README.md`: 人が読む使い方（できること・要るもの・入れ方・最短の手順・工程ごとの人が見る所・ラベルと決まり・任意の材料の作り方・道具の使い方・フォルダの中身・よくある質問）
- 新設 `disease_packs/_template.yaml`: 疾患パックの雛形（「★書く」「★選ぶ」の印・出典の書き方・作り方の手順つき。`validate_pack.py` が OK を返す形）
- 新設 `precedents/_template/`（index.md・topics/・verbatim/・prec_ids.txt）: 先例の材料の雛形。`precedents/README.md` を作り方と形の約束（索引の見出し・「本文:」の行の書き方）に書き直した
- 新設 `scripts/validate_precedents.py`: 先例の材料の形の検査（必須ファイル・M11 の節の表・ID の重複・索引の ID が prec_ids.txt に在るか・指す行の範囲が在り逐語の囲みを含むか）
- 新設 `templates/step0_design_input.md`: Step 0 の入力シート。00-initialize に「貼られたらその値を使う」を追加
- `_` で始まるファイル・フォルダは雛形として、Step 0 の一覧・`check_prec_ids.py` の既知の ID から除く
- 確認（2026-10-04）: 雛形のパック → `validate_pack.py` OK ／ 雛形の先例 → `validate_precedents.py` 問題 0 件 ／
  わざと壊した先例（行の範囲の超過・ID の重複）→ 2 件を検出して exit 1 ／ 雛形を置いた状態で AD パックの PREC は「未検証」のまま（雛形の ID を既知に数えない）

## v1.2-draft 追補（2026-10-04, 6 回目）— 当局の先例（[PREC]）を任意の材料として読めるように
- `precedents/<適応症>/`（任意）: 当局と企業のやり取りの逐語を置く場所。**skill は中身を作らず、無くても全工程が動く**。
  置く形の約束は `precedents/README.md`（index.md の M11 の節の表・topics/ の索引・逐語のファイル・prec_ids.txt）
- 01-research に **1g 先例を集める**（材料が在るときだけ。`waypoints/01_precedents.md`）。1e の下書きパックの src に 1g の ID を足す規則
- 03-write-sections: 各回で、その節に対応する先例を読む（index.md の M11 の節の列で選ぶ）。膨らませ規則に 2'（先例が求めた事項を `[PREC]` つきで）。記憶から `[PREC]` を付けない
- SKILL.md: `[PREC:<ID>]` の書式、E1 に「先例の数値は逐語に在るものだけ」、前提に任意の材料として追加
- 新設 `scripts/check_prec_ids.py`: 本文・パック・waypoints の `PREC:` の ID が、precedents の `prec_ids.txt` か疾患パックに在るか（不在があれば exit 1。照らす材料が無ければ「未検証」と表示して exit 0）。04 の検査に追加
- 新設 `scripts/requirements.txt`（全 script の依存の和。正典は各 script の頭の PEP 723）
- `disease_packs/atopic_dermatitis.yaml`: PREC の書き方の説明を、公開の原本（Drugs@FDA の Administrative and Correspondence Documents の PDF の頁と Question 番号）で引ける形に書き直した。略号と申請番号の対応を明記
- 確認（2026-10-04）: precedents が無い状態で、AD パックの PREC 35 個は「未検証」で exit 0、存在しない ID を含む本文は exit 1。
  AD の材料を置いた写しでは、パックの 35 個がすべて実在（不在 0）
- Step 0 で**適応症の名前 `indication_key`** を決めるようにした（`disease_packs/` と `precedents/` に在る名前を一覧で示して選ぶ。無ければ新しく作る）。
  疾患パック `disease_packs/<indication_key>.yaml` と先例 `precedents/<indication_key>/` はこの名前で**別々に**探し、どちらも任意。
  以前は 1g の `precedents/<疾患>/` の <疾患> が何かを決める手順が無く、下書きパックの道ではどのフォルダを読むか定まらなかった。
  `intervention_metadata.json` に `indication_key`・`precedents` を追加。下書きパックの `meta.disease` も同じ名前にする
- 未対応（次の候補）: ①先例の材料を置いて Step 1g・3 を通す試運転

## v1.2-draft 追補（2026-10-04, 5 回目）— 腫瘍での試運転（trial_runs/ZX-202）を受けて
- `sample_size.py combine`: 安全性曝露が対象外（0）でも理由つきで行を出す。未決は「TBD（未割当）」と表示（以前は理由が消えていた）
- `check_protocol.py` C7: 疾患領域の重み付けは「3–6 pp」のように pp の付いた数だけを頁数として読む（"RECIST 1.1" を 1.1 頁と誤読していた）
- `check_protocol.py` 申告 C8: 数値を含むのに出典が DERIVED だけの段落を一覧（fail にはしない。言葉で書いた数は拾えない）
- 未対応（次の候補）: ①例数を key secondary が決めたとき主要評価項目の解析時期を検査する ②疾患パックに assessment_schedule（画像評価の間隔）の欄 ③03 の E1 に「数を言葉で書くのも数値」を明記

## v1.2-draft 追補（2026-10-03, 4 回目）
- 粒度の検査 C7（check_protocol）: 節の語数 < 目安頁×250 語×0.5 で fail。250 語/頁は参照プロトコル本文 82 頁・21,418 語から。付録 12〜14 は申告のみ。`--only-c7` で書きかけの 1 章にも使える
- Step 3 を 4 回 → 章ごと 12 回に分割（sec_01〜sec_12）
- 例数: 最終 N = max(主要, key secondary, 安全性曝露)。`sample_size.py combine` と `design_archetypes.safety_exposure`（ICH E1: 約 1500 例・6 か月 300–600 例・1 年 100 例。生命を脅かす疾患は対象外）

## v1.2-draft 追補（2026-10-03, 3 回目）
- 評価尺度の最新版を確かめる手順（01-research 1f, `waypoints/instrument_versions.json`, ラベル `[INSTR]`）を追加。参照プロトコルの版数は当時の版として扱い、最新版の根拠にしない（利用者の指摘）

## v1.2-draft 追補（2026-10-03, 2 回目）— 適応症に依存しない形へ
- `assets/design_archetypes.yaml` 新設: 評価項目の型（二値・連続量・生存時間・発生率）× 比較の型 × 疾患領域 → estimand の雛形・解析・欠測・多重性・例数のコマンド・節の重み
- `disease_packs/_schema.yaml` 新設。確定版パックが無い適応症は Step 1e が CTG の参照試験 5 本から下書きパックを作る（`scripts/validate_pack.py` で形を検査）。`atopic_dermatitis.yaml` は status: draft（保留）
- v1.1.1 の 02〜04 の詳しい書き方は捨てず `references/section_guides_v1.1.1/` に置き、`references/section_guides.md` で M11 の節に付け替え（腫瘍の既定・機器の分岐・番号と行数は無視する規則つき）。旧 05（連結）は新 04 に統合
- MCP の get_trial_details は群・用量・割付・盲検・結果を返さないことを確認（データは CTG に在る）。`scripts/ctg_fetch.py`（API v2 直接・この環境では未検証）と、MCP の advanced_query で列挙型の値を当てる手順（01-research 1a-2）を追加
- `scripts/sample_size.py` に生存時間（Schoenfeld、331 事象＝閉形式と一致）と非劣性（二値、337/群＝閉形式と一致）を追加
- 試運転（`trial_runs/ZX-101/`）で見つかった未対応: 粒度の検査が無い／安全性曝露（ICH E1）が例数の規則に無い

## v1.2-draft（2026-10-03）

### 方針の変更
- CTG（MCP）は「要旨」として起点にだけ使い、**枠（section_spec_m11.yaml）× 疾患パック × 定型**で肉付けする形に変更。
- 骨格を NIH テンプレートから **ICH M11（Step 4, 2025-11-19）** の 14 節へ。NIH テンプレートは定型文の文例集として残す。
- 全段落に出典ラベル（USER / CTG / PACK / PREC / STD / PRIOR / DERIVED / TBD）。数値は出典があるときだけ（E1）。
- 事実の正典 `protocol_facts.json` を新設し、評価項目・中間事象・救済療法を 1 か所に（E2）。
- 医薬品に限定（医療機器の道は未改訂。旧版は `references/legacy_v1.1.1/`）。

### v1.1.1 の不具合の扱い
| v1.1.1 の不具合 | v1.2 |
|---|---|
| SKILL.md が存在しない `05-generate-document.md` を指す | 指示書を 00〜04 に作り直し、SKILL.md の表と一致 |
| 節番号の重複・ずれ（Section 4 が 2 回、連結時に 1 ずれ） | 番号は spec からだけ取る。check_protocol C1 が検査 |
| Step 4 がまだ無い `02_protocol_draft.md` を読む | facts（Step 2）から読む |
| 目次をテンプレートの 188〜368 行目から写す | spec から生成 |
| 研究の後に「研究に進みますか」と聞く文言 | 01-research.md で修正 |
| Web 検索の可否が README と 01 で矛盾 | 情報源を USER/CTG/PACK/PREC/PRIOR/STD に整理 |
| requirements.txt が無い | PEP 723（`uv run`） |
| MCP 必須（無いと止まる） | 任意。無ければ PACK だけで進む |
| 腫瘍寄りの例（ECOG・RECIST・余命） | 疾患パックへ分離（AD パックを追加） |
| 例数が 2 群・単一評価項目だけ | `sample_size.py`: co-primary（相関つき同時検出力）・多群（Bonferroni）・NRI |

### 追加ファイル
- `assets/section_spec_m11.yaml`, `assets/ctg_mcp_field_map.yaml`
- `disease_packs/atopic_dermatitis.yaml`
- `references/00-initialize.md` 〜 `04-assemble-and-check.md`
- `scripts/sample_size.py`, `scripts/check_protocol.py`
- `reference_protocols/NCT05398445_ctg_mcp_get_trial_details.json`（MCP の返り値の実物。欄の確認用）

### 検証（2026-10-03）
- YAML 3 本が構文解析できる
- `sample_size.py binary --p-control 0.10 --p-active 0.38 --power 0.9 --dropout 0 --missing inflate --alpha-split none`
  → 1 群 44 例（教科書の閉形式〔非プール分散〕の 44 と一致）
- `check_protocol.py`: 正しい見本で fails 0（exit 0）。壊した見本で C1〜C6 の 6 種すべてが検出された（exit 1）

### まだやっていないこと
- 架空の AD 候補薬で Step 0〜4 を通しで回す試運転
- 疾患パックの `sample_size_priors` は DUPIXENT の SOLO 1/2 のみ取得済み。他剤は未取得
- 青年（12–17 歳）を含む場合の規則（PK 部分試験・体重別用量）は PACK に未記載
- 医療機器の道
