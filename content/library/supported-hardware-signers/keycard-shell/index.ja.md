---
aliases:
- /ja/knowledge/supported-hardware-signers/keycard-shell/
title: Keycard Shell
signer: keycard-shell
bucket: knowledge
---

## 想定しておくこと

- QR を使って Keycard Shell を Bitcoin-Safe と組み合わせて利用します。ベンダーアプリは不要です。
- 鍵は Keycard のセキュアエレメント内で生成され、保存されます。Shell は PSBT を読み取り、取引内容を自身の画面に表示し、端末上で確認した後にのみ署名します。
- マルチシグ（P2WSH）と完全な PSBT のワークフローに対応しています。マルチシグディスクリプタを登録し、Bitcoin-Safe 用に署名者データをエクスポートしてください。
- 署名する前に、Shell の画面で各出力と手数料を確認してください。
