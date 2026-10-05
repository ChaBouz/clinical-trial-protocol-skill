# 01_research_summary.md（wamd-ph3 / neovascular_amd / 第 3 相）

## 環境と材料
- CTG MCP: 可 ／ CTG 通信（ctg_fetch.py）: 可（2026-10-04 に許可後、再確認）→ 参照 5 本の API 全記録を取得（群・割付・盲検・結果欄）。
- 疾患パック: 確定版なし → `disease_pack_draft.yaml`（draft、validate OK）
- 先例: neovascular_amd（brolucizumab / faricimab / ranibizumab の FDA コレスポンデンス）→ `01_precedents.md`（PREC ID 12 件すべて実在）
- 参照試験 5 本: NCT04423718 (PULSAR, aflibercept 8 mg vs 2 mg)、NCT02307682 (HAWK)、NCT04270747 (ABP 938)、NCT04005352 (TALON)、NCT06856577 (ARTEMIS, 点眼の使用可否を含む)
  選択は ①nAMD・50 歳以上 ②aflibercept 対照 ③新しい ④結果あり（ARTEMIS のみ結果なし）。★aflibercept 8 mg を試験薬とする PULSAR を入れたが、本試験は 8 mg が**対照**。

## 突き合わせ（CTG × パック × 先例 × USER）
| 項目 | 一致 | CTG にだけ在る | 先例 | USER との差 |
|---|---|---|---|---|
| 年齢 | 50 歳以上 5/5 | — | — | 一致 |
| BCVA 適格範囲 | 割れた（5 通り） | 78–24 / 78–23 / 73–34 / 83–38 / 78–35 | — | USER 未指定 → [TBD] |
| 主要評価項目 | BCVA 変化量 4/5（時点 Week 48 前後） | TALON は治療間隔 | BCVA 変化量・≥9 か月後（Rani:s13/Q1b, Brolu:s20/Q10） | ★**USER は「15 文字以上の低下」（割合）**。参照にも先例にも主要の例なし |
| NI マージン | — | ARTEMIS は NI（マージン値は MCP に無し） | BCVA 変化量で ≤4.5 文字 / 4 文字 | USER 未指定。割合のマージンは先例なし → [TBD] |
| 盲検 | DOUBLE 以上 5/5 | — | sham は最適でない・条件つき（Brolu:s20/Q13） | ★点眼 vs 硝子体内注射 → ダブルダミー必須 |
| aflibercept 8 mg の用法 | — | — | PI: 4 週ごと 3 回 → 8〜16 週（±1 週）（Eylea HD の添付文書の検索抜粋で確認） | USER の指定と一致 |
| 治療期間 | — | HAWK 96 週、ABP 938 48 週 | — | USER 44 週、主要 Week 48（最終投与から 4 週） |
| 救済・治療失敗 | — | — | 最良 BCVA から 15 文字以上低下 = 治療失敗（Rani:s13/Q1f）、trimmed mean（Q1i） | 要確認 |
| 安全性データベース | — | — | ≥500 例が治療完了・300 例が 12 か月以上（Rani:s13/Q3） | 44 週では 12 か月に届かない → LTE か別試験で補う（DERIVED） |

## 取れなかったもの・注意
- 参照試験の設計欄（群・用量・割付比）と結果値（例数の仮定）は MCP で取れない。→ `sample_size_priors` は空。
- 点眼薬の nAMD 試験の先例は無い。

## 追記（CTG 通信が可になった後、2026-10-04）
- 取得: `ctg/<NCT>.api.json`（5 本）。群・盲検の当事者・層別因子・結果欄が読めた。★本節の値は CTG の結果欄から。
- 対照群（aflibercept 2 mg）の ≥15 文字低下: HAWK Week 48 = 5.6%、ABP 938 Week 52 の視力維持 97.6%（→ 2.4%）。PULSAR の結果欄に 8 mg 群の低下率は無い。
- BCVA 変化量の NI マージン: PULSAR・HAWK・TALON とも 4 文字（片側 α 0.025）。割合のマージンは参照にも先例にも無い。
- 盲検: PULSAR は 4 者盲検、ARTEMIS は『aflibercept 群に sham、試験群にも sham 注射』で、ダブルダミーの前例（硝子体内注射 vs 注射）。点眼 vs 注射の前例は無い。
- 層別: ABP 938 は region（East Asia/Europe/North America）× baseline BCVA（<64/≥64）。
