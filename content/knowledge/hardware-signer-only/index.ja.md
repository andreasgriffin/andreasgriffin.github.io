---
title: "メインネットでハードウェア署名器が必須"
description: "Bitcoin Safe はメインネット上でソフトウェア由来のシードを禁止し、ハードウェアのみを許可することでセキュリティを最大化し、ソフトウェアベースの鍵保管のリスクを避けます。その理由をご説明します。"
draft: false
tags: ["Featured", "Knowledge" ]
keywords: [
  "Bitcoin Safe",
  "ハードウェアウォレット",
  "ソフトウェアシード",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "マルチシグ",
  "PSBT",
  "セルフカストディ",
  "ビットコインのセキュリティ",
  "アドレスポイズニング",
  "ビットコインツール"
]
images: ["logo.png" ]
# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=dbSmQmt0uDI"
weight: 21
---

 

![](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }

## 🚫 なぜ Bitcoin Safe はメインネットでソフトウェアシードをブロックするのか？

🤔 面倒に感じませんか？

🔥 実は — これは**大きなセキュリティ向上**です。

Bitcoin Safe は **ソフトウェアシードをテストネット、Signet、Regtestでのみ許可し**、メインネットでは決して許可しません。理由は以下の通りです。

### ✅ メインネットでソフトウェアシードがブロックされる理由

- 🧠 **ソフトウェアシードは安全ではない**
  - コンピュータにはリスクが満載です：クリップボードハイジャッカー、マルウェア、ブラウザの脆弱性。
  - 一度のミスでシードが漏洩すれば — 終わりです。
  - コールドストレージは決してホットな状態から始めてはいけません。

</br>

- 🧊 **コールドストレージは「最初から冷」であるべき**
  - ユーザーはしばしばソフトウェアウォレットでシードを作成してからハードウェアに移すことがあります。
  - しかし最初の露出が既に起きていると、取り返しがつきません。
  - 真のコールドストレージ = 最初からハードウェア署名器で作成すること。

</br>

- 🎣 **フィッシングはソフトウェア習慣を利用する**
  - アプリにシードを入力する習慣は、悪い UX パターンを信頼するように訓練してしまいます。
  - ハードウェアのみを強制すると、より良い習慣が促され、露出が制限されます。
  - ✅ シードレスなメインネット = フィッシング被害が減少。

</br>

- 🧪 **開発者には柔軟性を提供**
  - ソフトウェアシードは以下で許可されています：
    - Testnet
    - Signet
    - Regtest
  - 開発者には理想的。実際のサトシにリスクはありません。🧡



</br>


- 🔐 **メインネットではハードウェア署名器が必須 — 例外なし**
  - 🔌 USB、📷 QR、💾 SDカードをサポートする主要デバイス：
    - [Coldcard]({{< ref "knowledge/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Foundation Passport]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Ledger]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Keystone]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "knowledge/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "knowledge/supported-hardware-signers" >}})
  - [サポートされている署名器をすべて表示 →]({{< ref "knowledge/supported-hardware-signers" >}})


---

## 🛡️ アドレスポイズニング保護

Bitcoin Safe は受取アドレスを**色分け表示**して、アドレスポイズニングを一目で判別できるようにします：

- 🟢 緑 = 検証済みの受取アドレス  
- 🟡 黄 = つり銭（チェンジ）アドレス  

誰かがあなたのクリップボードを偽アドレスで汚染しようとしても、すぐに気づけます。

![アドレスポイズニング検出の例](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ USB または QR によるアドレス検証

受取アドレスをハードウェア署名器上で直接検証できます — 画面だけを信頼する必要はありません。

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ 各ハードウェア署名器向けの手順
 
- {{<text-name-with-logo>}} には各ハードウェア署名器ごとのスクリーンショット付き手順が含まれており、各ステップを案内します 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-hardware-signer-screenshots >}}
    </div>

   
---



## 🤝 共同で使えるマルチシグを簡単に

Bitcoin Safe はマルチシグを使いやすく、チーム対応にします：

- 🔐 暗号化された Nostr チャット  
- 🔁 ワンクリックでの PSBT 共有  
- 🔌 USB、📷 QR、💾 SDカード

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ すべてのユーザー向けの強力な機能

- 🟧 シングルシグウォレットウィザード  
- 🟨 2-of-3 マルチシグ設定  
- 🟩 任意の n-of-m 構成  
- 🖨️ 印刷可能な PDF バックアップシート  
- 🔁 Nostr 経由のラベル同期  
- 🔍 資金の流れ図 & 検索可能な取引履歴

![Bitcoin Safe のトランザクション図](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 グローバルで使いやすい

- 多言語対応: {{< flags-short >}}
- 対応 OS: Windows、macOS & Linux  
- PSBT / CSV のドラッグ＆ドロップ  
- トランザクション、UTXO、金額などの高度なフィルタ

---

## 💡 要点

Bitcoin Safe = 本物のビットコイン貯蓄:

✅ メインネットではハードウェアのみ  
✅ ソフトウェアシードの露出なし  
✅ 初心者に優しいマルチシグ  
✅ 開発者向けのテスト環境  
✅ 家族やチーム向けの機能  

🔗 [Bitcoin-Safe.org]({{< ref "/" >}})  
🎥 YouTube チャンネル →: https://youtube.com/@BitcoinSafeOrg