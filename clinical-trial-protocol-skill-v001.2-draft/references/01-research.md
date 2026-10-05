# Step 1: 材料集め（CTG・疾患パック・下書きパック）

## 目的
新試験の本文の「起点」になる事実を、出典つきで 1 か所に集める。
**CTG の値は要旨なので、ここでは集めるだけで、膨らませるのは Step 3。**
適応症は問わない。手で作った確定版の疾患パックが無ければ、1e で下書きパックを作る。

## 1a. 参照試験を選ぶ（CTG MCP）

1. `reference_nct_ids` が無ければ探す:
   `search_trials(condition=<疾患>, phase=["PHASE3"], status=["COMPLETED","ACTIVE_NOT_RECRUITING"], page_size=25)`
   （同じ機序の薬があれば `intervention=` も）。次の順で **5 本**選ぶ:
   ①同じ集団（年齢層・重症度・治療歴）②同じ比較（プラセボ／実薬／非劣性）③新しい（start_date）④has_results=true。
2. 各試験に `get_trial_details(nct_id)` を呼び、**返った JSON をそのまま** `waypoints/ctg/<NCT>.json` に保存する。
3. 横断: `analyze_endpoints(condition=<疾患>, phase=["PHASE3"], start_date_after=<8 年前>, page_size=50)` を 1 回。
   結果を `waypoints/ctg/_endpoints_landscape.json` に保存。
4. MCP が無い・失敗したら、次の順で代える（上から試す。どれも無ければその旨を表示して 1e に進む。止めない）:
   1. **通信**: `uv run scripts/ctg_fetch.py search --cond "<疾患の英語名>" --phase PHASE3 --status COMPLETED,ACTIVE_NOT_RECRUITING --max 25 --out waypoints/ctg/_search.json`
      で候補を探し、上と同じ基準で 5 本選び、各試験を `uv run scripts/ctg_fetch.py <NCT> --out waypoints/ctg/<NCT>.api.json` で取る
      （この形の JSON は MCP の返り値と欄の名前が違う。1b では API v2 の欄（`protocolSection.eligibilityModule` 等）から同じ項目を抜く）
   2. **利用者が手で置いた JSON**: `waypoints/ctg/` に `NCT*.json` が在れば、それを読む（README §6-4 の手順で利用者が置く。形は API v2）
   3. どれも無い: 「参照試験なし」と 01_research_summary.md に書き、疾患パック（在れば）・先例（在れば）・設計の型・定型だけで進む

## 1a-2. 設計情報（群・用量・割付・盲検）の取り方

**MCP の `get_trial_details` は designModule と armsInterventionsModule を返さない**（2026-10-03 実測）。
データは ClinicalTrials.gov に在る（`search_trials` の `advanced_query` で `AREA[DesignAllocation]RANDOMIZED` が当たる）。
取り方は 2 通り。上から試す。

1. **根本: API v2 を直接読む**（Claude Code など、clinicaltrials.gov に出られる環境）
   `uv run scripts/ctg_fetch.py <NCT> --out waypoints/ctg/<NCT>.api.json`
   → 群の説明（用量・頻度）・割付・盲検・結果の数値まで全部取れる。
2. **対症療法: MCP で値を当てる**（1 が失敗したとき）。`search_trials(advanced_query="AREA[NCTId]<NCT> AND AREA[<欄>]<値>", count_total=true)` の
   total が 1 なら「その値」、0 なら違う。列挙型の欄だけ確定できる:

   | 欄 | 試す値 |
   |---|---|
   | DesignAllocation | RANDOMIZED, NON_RANDOMIZED, NA |
   | DesignMasking | NONE, SINGLE, DOUBLE, TRIPLE, QUADRUPLE |
   | DesignInterventionModel | PARALLEL, CROSSOVER, SINGLE_GROUP, FACTORIAL, SEQUENTIAL |
   | DesignPrimaryPurpose | TREATMENT, PREVENTION, SUPPORTIVE_CARE, DIAGNOSTIC, OTHER |

   自由記述（用量・投与間隔）は読めない。「"Q2W" を含むか」の当否だけ確かめられる（`AREA[ArmGroupDescription]"Q2W"`）。
   当てた結果は `waypoints/ctg/<NCT>.probe.json` に {欄: 値, 方法: "probe"} で保存し、本文では `[CTG:<NCT>:probe]` と書く。

## 1b. 抽出（`waypoints/01_ctg_reference.json`）

`assets/ctg_mcp_field_map.yaml` の `fields` に従い、試験ごとに抜く。値は**逐語**（要約しない）:
題名・相・登録数・適格基準（選択／除外に分けて項目ごと）・主要/副次評価項目（measure, time_frame, description）・
国ごとの施設数（施設名・連絡先は保存しない）・1a-2 の設計情報。
評価項目の `description` に書かれた中間事象の扱い（rescue・中止）は estimand の起点なので逐語で残す。

## 1c. 突き合わせ（`waypoints/01_research_summary.md`）

疾患パック（確定版 or 1e の下書き）と CTG を並べ、**一致・CTG にだけ在る・パックにだけ在る**の 3 列で表にする。
参照試験の間で値が割れる項目（主要時点 等）は「選択肢」として残す。

## 1d. 任意: 参照プロトコル PDF
利用者が `reference_protocols/` に PDF を置いた場合だけ、目次から節ごとの頁数を数えて spec の `ref_pages` と比べる。必須ではない。

## 1e. 下書きパックを作る（確定版のパックが無い適応症）

`disease_packs/_schema.yaml` の形で `waypoints/disease_pack_draft.yaml` を作る。`meta.disease` は Step 0 の `indication_key` と同じにする。材料と規則:

| パックの欄 | 材料 | 規則 |
|---|---|---|
| meta.therapeutic_area_family / endpoint_archetype | 疾患名・主要評価項目の型 | `assets/design_archetypes.yaml` のキーから選ぶ。合う領域が無ければ `general`（受け皿）を選び、Step 2 の確認で「領域の重み付けなし」と伝える。**新しい領域をその場で作らない** |
| inclusion / exclusion | 5 本の eligibility_criteria、`search_by_eligibility(condition, eligibility_keywords=<閾値の語>)` | 各項目に agreement（"4/5"）。過半数で一致した閾値だけ既定値、割れたら options |
| exclusion の共通区分 | STD | 感染・悪性腫瘍・心血管・検査値・精神・妊娠・ワクチン・他の治験 |
| endpoints | `_endpoints_landscape.json` の common_measures と 5 本の主要評価項目 | 最頻の主要評価項目と時点を既定、他は options |
| instruments | 評価項目の description | 尺度の範囲・responder の閾値は description に在るものだけ |
| rescue_table / estimands | description 中の中間事象の扱い ＋ archetypes の ice_templates | CTG に書かれていない救済療法の規則は DERIVED と印を付ける |
| analysis | archetypes | 疾患特有の層別因子は CTG の描写から（無ければ [TBD]） |
| PREC:（各欄の src） | 1g の `waypoints/01_precedents.md` | 1g で選んだ ID だけを src に足す。先例が CTG の既定と食い違うときは options に両方を並べ、どちらかを選ばない |
| sample_size_priors | 1a-2 で API v2 の resultsSection が取れたときだけ。取れなければ添付文書・論文（出典と取得日） | 取れなければ空のまま |
| safety_monitoring | 機序（USER）＋ STD | 機序固有の AESI は DERIVED |

作ったら `uv run scripts/validate_pack.py waypoints/disease_pack_draft.yaml` を回し、OK でなければ直す。
下書きパックは Step 2 の確認の停止で利用者に見せる（確定版のパックではない、と明記）。

## 1f. 評価尺度の最新版を確かめる（`waypoints/instrument_versions.json`）

参照プロトコルや CTG に書かれた尺度の版は**その試験の当時の版**であって、今の最新版とは限らない。
主要・副次評価項目で使う尺度（例: vIGA-AD、EASI、PP-NRS、DLQI、POEM。腫瘍なら RECIST、QLQ-C30 など）ごとに:

1. 開発者・権利者の公式情報（開発元のサイト、ライセンス窓口、原著論文）を Web 検索で探す。
   CTG・参照プロトコル・二次資料（学会スライド等）の版数は「当時の版」として記録するだけで、最新版の根拠にしない。
2. 次を記録する:
   ```json
   {"vIGA-AD": {"version": "…", "version_source": "<URL か文献>", "license_holder": "…",
                "license_required": true, "checked_on": "YYYY-MM-DD", "seen_in_reference": "NCT… の当時の版（あれば）"}}
   ```
3. 公式情報で版が確認できなければ `"version": null` とし、本文は `[TBD: <尺度名> version — checked YYYY-MM-DD, not confirmed]`。推測で版数を書かない。
4. 本文（8.3 の表・12 の付録）では版を `[INSTR:<尺度名>:<checked_on>]` のラベルつきで書く。

## 1g. 当局の先例を集める（`waypoints/01_precedents.md`）— 材料が在るときだけ

`precedents/<indication_key>/index.md` が在る適応症だけ行う（`indication_key` は Step 0 で決めた名前）（材料は任意。形は `precedents/README.md`）。
無ければ「先例の材料なし」と 01_research_summary.md に書いて次へ（止めない）。`[PREC]` は疾患パックに書かれたものだけになる。
先例は当局と企業のやり取りの**原文の逐語**（多くは英語）。索引の振り分けや話し手の札が機械で付けられている材料もあるので、
話し手（当局か企業か）は逐語の文面で確かめる。

1. `index.md` の表で、論点の索引（`topics/<key>.md`）と、それぞれが対応する M11 の節を見る。
2. 新試験の設計に効く順に索引の**目次**を読み、使う項目を選ぶ。おすすめの順:
   適格基準 → 評価項目 → estimand・中間事象・救済療法 → 解析方法 → 欠測 → 多重性 → 評価尺度 → 併用療法 → 安全性 → デザイン → 用量 → 小児（含めるなら）。
   選ぶ基準は「新試験の設計（USER）に関係するか」と「会議の時期（Pre-IND／EOP2／Pre-BLA など）」。どの論点にも当たらなかった項目の置き場（other 等）は、ID で引くときだけ読む。
3. 選んだ項目の索引が指す**逐語のファイルの行の範囲だけ**を読む。
   索引の抜粋（目印）は選ぶための手がかりなので、引用にも数値の出典にも使わない。
4. `waypoints/01_precedents.md` に、論点ごとに次を書く:
   ```
   ## <論点>
   - [PREC:<ID>] <薬剤>, <会議の種別・日付>
     - 当局の要点（Claude の言葉。和文 1〜2 行）[DERIVED]
     - 逐語（決め手の文だけ。逐語のファイルから 1 文字も変えずに写す）: "…"
     - 新試験への当てはめ: パックの <欄> ／ M11 の <節>
   ```
   要点は Claude の言い換えなので、本文に入れるときは逐語の文に戻って確かめる。逐語は文の途中で切らない。
5. 書いたら `uv run scripts/check_prec_ids.py --indication <indication_key> waypoints/01_precedents.md` を回し、実在しない ID が 0 であることを確かめる。
6. 1c の突き合わせ表に「先例」の列を足し、CTG・パックと食い違う所に印を付ける（どちらが正しいかは決めない。Step 2 の停止で利用者に見せる）。

## 研究のみモードの終わり
`01_research_summary.md` と（作ったなら）下書きパックを示し、「Step 2 へ進むか」を聞く。
