# Step 4: 連結と整合性検査

## 手順

1. 12 個のファイルがあることを確かめる: `waypoints/sec_01.md`〜`sec_12.md`。無ければどの回が無いかを表示して止まる。
2. 連結:
   ```bash
   cat waypoints/sec_[0-9][0-9].md > waypoints/protocol_complete.md
   ```
3. 検査:
   ```bash
   uv run scripts/check_protocol.py waypoints/protocol_complete.md \
     --spec assets/section_spec_m11.yaml --facts waypoints/protocol_facts.json \
     > waypoints/check_report.json
   ```
   先例の材料を使った回は、続けて PREC の ID を照らす（実在しない ID が 1 つでもあれば exit 1）:
   ```bash
   uv run scripts/check_prec_ids.py --indication <indication_key> waypoints/protocol_complete.md
   ```
   exit 1（fails がある）なら、**直す前に**利用者へ fails の一覧を見せる。直すのは本文ではなく、原因の側
   （facts が古い → facts を直して該当回を書き直す／見出しの番号違い → その回を書き直す）。
4. 13 節（略語集）は本文から略語を拾って作る（最後に書き直してよい唯一の節）。
5. 完了表示:
   - 試験の要点（群・主要評価項目・例数・期間）
   - `check_report.json` の要約: fails の数、`[TBD]` の節ごとの数、ラベルごとの数
   - `[DERIVED]` の数（レビューが要る量の目安）
   - SKILL.md §5 の免責

## 任意: 出力形式
- Word（docx）が要るときは、M11 の Word テンプレートに流し込む（別 skill の docx を使う）。
- 出典ラベルを外した提出用版を作るときは、ラベル付きの版を必ず残す（レビューの記録になる）。
