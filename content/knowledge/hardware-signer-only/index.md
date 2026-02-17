---
aliases:
  - "/knowledge/hardware-signer-only/"
title: "Hardware Signers Required"
description: "Bitcoin Safe enforces hardware-only seeds on Mainnet to maximize security and avoid the risks of software-based key storage. Here's why that matters."
draft: false
tags: ["Featured", "Knowledge" ]
keywords: [
  "Bitcoin Safe",
  "hardware wallet",
  "software seed",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "multisig",
  "PSBT",
  "self-custody",
  "Bitcoin security",
  "address poisoning",
  "Bitcoin tools"
]
images: ["logo.png" ]
# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=dbSmQmt0uDI"
weight: 21
---

 

![Bitcoin Safe logo](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }

## 🚫 Why does Bitcoin Safe block software seeds on Mainnet?

🤔 Isn't that inconvenient?

🔥 Turns out — it's a **major security upgrade**.

Bitcoin Safe **only allows software seeds on Testnet, Signet, and Regtest** — never on Mainnet. Here's why:

### ✅ Reasons why software seeds are blocked on Mainnet

- 🧠 **Software seeds are insecure** 
  - Computers are full of risks: clipboard hijackers, malware, browser exploits.
  - One slip, and your seed is compromised — it's game over.
  - Cold storage should never start hot.

</br>

- 🧊 **Cold storage must be born cold**
  - Users often generate seeds in software wallets then migrate to hardware.
  - But the initial exposure already happened — there's no going back.
  - True cold storage = created on a hardware signer from the start.

</br>

- 🎣 **Phishing thrives on software habits**
  - Typing seeds into apps trains you to trust bad UX patterns.
  - Hardware-only forces better habits and limits exposure.
  - ✅ Seedless Mainnet = fewer phishing victims.

</br>

- 🧪 **Developers still get flexibility**
  - Software seeds *are* allowed on:
    - Testnet
    - Signet
    - Regtest
  - Ideal for devs. No risk to real sats. 🧡



</br>


- 🔐 **Mainnet requires hardware signers — no exceptions**
  - 🔌 USB, 📷 QR, and 💾 SD card with all major  devices
    - [Coldcard]({{< ref "knowledge/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Foundation Passport]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Ledger]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Keystone]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "knowledge/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "knowledge/supported-hardware-signers" >}})
  - [View all supported signers →]({{< ref "knowledge/supported-hardware-signers" >}})


---

## 🛡️ Address poisoning protection

Bitcoin Safe **color-codes receive addresses** to make address poisoning obvious:

- 🟢 Green = verified receive address  
- 🟡 Yellow = change address  

If someone tries to poison your clipboard with a fake address, you'll see it instantly.

![Address poisoning detection example](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ Address verification via USB or QR

Verify receive addresses directly on your hardware signer — no need to trust the screen.

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ Supported hardware signers

{{< hardware-signer-scroll-row >}}

---



## 🤝 Collaborative multisig made easy

Bitcoin Safe makes multisig user-friendly and team-ready:

- 🔐 Encrypted Nostr chat  
- 🔁 1-click PSBT sharing  
- 🔌 USB, 📷 QR, and 💾 SD card

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ Powerful features for all users

- 🟧 Singlesig wallet wizard  
- 🟨 2-of-3 multisig setup  
- 🟩 Any n-of-m configuration  
- 🖨️ Printable PDF backup sheets  
- 🔁 Label sync via Nostr  
- 🔍 Full money-flow diagram & searchable transaction history

![Transaction diagram in Bitcoin Safe](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 Global and user-friendly

- Multilingual support: {{< flags-short >}}
- Works on: Windows, macOS & Linux  
- Drag-and-drop PSBT / CSV  
- Advanced filters for transactions, UTXOs, amounts, and more

---

## 💡 TL;DR

Bitcoin Safe = Real Bitcoin savings:

✅ Hardware-only on Mainnet  
✅ No software seed exposure  
✅ Beginner-friendly multisig  
✅ Developer-friendly testing environments  
✅ Family & team-ready features  

🔗 [Bitcoin-Safe.org]({{< ref "/" >}})  
🎥 YouTube channel →: https://youtube.com/@BitcoinSafeOrg
