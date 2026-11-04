---
aliases:
  - "/plugins/sync-chat/"
title: "Sync & Chat"
description: "Discover peers on your wallet, sync labels and categories, chat securely, and share PSBTs in one click."
draft: false
tags: ["Plugins", "sync-chat-mainpage"]
images: ["logo.png"]
weight: 30
faq:
  title: "Sync & Chat questions"
  items:
    - question: "How do devices find each other?"
      answer: "Sync & Chat looks for other devices that use the same wallet descriptor. The descriptor is hashed before it is used for discovery, so it is not exposed in plain form. Each discovered device must also be added and trusted manually before it can take part in the chat. This keeps the chat safe even if the descriptor is not secret."
    - question: "How does collaboration work in practice?"
      answer: "1. Setup (once): add and trust each participant's device.\n2. Create: one participant creates a PSBT and adds their signature.\n3. Share: the PSBT goes to all participants, or only to selected ones.\n4. Sign: each participant adds their signature until the transaction is fully signed.\n5. Broadcast: the last signer broadcasts the transaction, and it then appears in every participant's wallet."
    - question: "What gets synchronized?"
      answer: "Sync & Chat handles:\n- Coin categories and labels, synced between signers, even across different operating systems\n- Sharing PSBTs in one click"
    - question: "Is the chat private?"
      answer: "Yes. Wallet chat is encrypted and runs over Nostr, and label backups are stored encrypted via Nostr as well."
---

### {{< page-title >}}

<p class="lead">Coordinate multisig signers and keep wallet context in sync from within Bitcoin-Safe.</p>

<ul class="plugin-features">
<li>Discover other devices using the same wallet descriptor</li>
<li>Sync labels and categories between signers</li>
<li>Chat securely and share PSBTs in one click</li>
</ul>

### Label synchronisation

{{< video src="../../library/label-sync/label-sync.mp4" controls="true" >}}

### Collaborative signing

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

For the complete walkthrough of collaborative multisig signing, see [Collaboration in a Multisig]({{< ref "library/collaboration/" >}}).

### Frequently asked questions

<details>
<summary>How do devices find each other?</summary>

Sync & Chat looks for other devices that use the same wallet descriptor. The descriptor is hashed before it is used for discovery, so it is not exposed in plain form. Each discovered device must also be added and trusted manually before it can take part in the chat. This keeps the chat safe even if the descriptor is not secret.

</details>

<details>
<summary>How does collaboration work in practice?</summary>

1. **Setup (once):** Add and trust each participant's device.
2. **Create:** One participant creates a PSBT and adds their signature.
3. **Share:** The PSBT goes to all participants, or only to selected ones.
4. **Sign:** Each participant adds their signature until the transaction is fully signed.
5. **Broadcast:** The last signer broadcasts the transaction, and it then appears in every participant's wallet.

</details>

<details>
<summary>What gets synchronized?</summary>

Sync & Chat handles:

- Coin categories and labels, synced between signers, even across different operating systems
- Sharing PSBTs in one click

</details>

<details>
<summary>Is the chat private?</summary>

Yes. Wallet chat is encrypted and runs over Nostr, and label backups are stored encrypted via Nostr as well.

</details>

{{< sync-page-box >}}
