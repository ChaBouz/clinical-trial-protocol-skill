# clinical-trial-protocol-skill v001.2（DRAFT）

医薬品の第 2/3 相臨床試験の**治験実施計画書（プロトコル）の草案**を、ICH M11 の 14 節で書く Claude の skill です。
すべての段落・表の行に出典ラベルが付き、出典の無い数値は空欄（`[TBD]`）として残ります。

- skill 本体と使い方: [`clinical-trial-protocol-skill-v001.2-draft/`](clinical-trial-protocol-skill-v001.2-draft/)（★まずその中の `README.md` を読む）
- 出力の見本: [`samples/`](samples/)（架空の候補薬の第 3 相プロトコル案。下の注意を読む）

## ★作り方と安全性について

この版は、Tad が **Claude（Cowork）との対話で作成・改変**したものです。
指示書・道具（scripts）・出力の正確性と安全性は、作者が完全には確認できていません。
使う人の責任で中身をレビューし、作ったプロトコル案は必ず専門家（臨床・統計・薬事）が確認してください。
出力は予備的な草案であり、規制当局・IRB の判断や医学・法務・規制の助言ではありません。

## 由来とライセンス

- Anthropic が公開した sample skill「clinical-trial-protocol-skill」v1.1.1（[anthropics/life-sciences](https://github.com/anthropics/life-sciences)、Apache License 2.0）を元に改変・拡張したものです。**Anthropic の公式版ではありません。**
- 版の名前「v001.2」は、Anthropic の版（v1.x）と取り違えないための、この系統だけの名前です。
- ライセンス: Apache License 2.0（[`LICENSE`](LICENSE)）。由来・変更したファイルの一覧は skill のフォルダの `NOTICE`、変更の履歴は `CHANGELOG.md`。
