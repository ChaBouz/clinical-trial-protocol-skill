# 出力の見本: wAMD（滲出型加齢黄斑変性）の第 3 相プロトコル案

`wamd-ph3/waypoints/` は、この skill を Claude Code で 1 回通しで回したときの途中結果と出力です（2026-10-05）。
生成したときの skill は改名前の「v1.2-draft」で、中身は v001.2-draft とほぼ同じです（違いは版の名前・ライセンスの表示など。`CHANGELOG.md` を参照）。

## まず読むファイル

| ファイル | 中身 |
|---|---|
| `wamd-ph3/waypoints/protocol_complete.md` | プロトコル案の全文（ICH M11 の 14 節） |
| `wamd-ph3/waypoints/design_decisions.md` | 入力から設計を変えた点と理由（本文にも「【設計変更コメント D#】」） |
| `wamd-ph3/waypoints/protocol_facts.json` | 群・評価項目・時点などの正典（全節はここから書かれる） |
| `wamd-ph3/waypoints/check_report.json` | 整合性の検査の結果 |

## ★注意

- **候補薬「XYZ-123」は架空です。** 第 2 相の結果として、公開された製薬会社のニュースリリースの数値を例として借りています。実在の薬・試験の計画ではありません。
- これは skill の動きを示す見本で、医学的・統計的に妥当な計画ではありません。生成した Claude 自身が「主要評価項目で非劣性が成立しない可能性が高い」など、
  要確認の点を残しています（`design_decisions.md`）。
- `[TBD]`（スポンサーが埋める値）と `[DERIVED]`（Claude が膨らませた記述。要レビュー）が多く残っています。
- この版は Claude（Cowork）との対話で作成した skill で生成したもので、正確性と安全性は完全には確認されていません。
