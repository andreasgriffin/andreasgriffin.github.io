---
aliases:
  - "/plugins/sync-chat/"
title: "Sync & Chat"
date: "2026-11-04"
description: "Coordinate multisig signers in Bitcoin-Safe: discover peers on the same wallet, sync labels and categories, chat securely, and share PSBTs in one click."
draft: false
tags: ["Plugins", "sync-chat-mainpage"]
images: ["logo.png"]
weight: 30
lead: "Coordinate multisig signers and keep wallet context in sync from within Bitcoin-Safe."
features:
  - "Discover other devices using the same wallet descriptor"
  - "Sync labels and categories between signers"
  - "Chat securely and share PSBTs in one click"
media:
  - type: video
    src: "/library/label-sync/label-sync.mp4"
    heading: "See it in action"
    caption: "Labels and categories sync between two Bitcoin-Safe computers."
  - type: youtube
    link: "https://www.youtube.com/watch?v=oQB2qzYZ_cw"
    caption: "Walkthrough of collaborative multisig signing."
faq:
  title: "Sync & Chat questions"
  items:
    - question: "How do devices find each other?"
      answer: "Sync & Chat discovers the other devices and signers that use the same wallet descriptor, so every co-signer works from the same wallet."
    - question: "What gets synchronized?"
      answer: "Coin categories and labels are synced between signers, even across different operating systems. You can also share PSBTs in one click."
    - question: "Is the chat private?"
      answer: "Yes. Wallet chat is encrypted and runs over Nostr, and label backups are stored encrypted via Nostr as well."
related_docs:
  - "library/label-sync"
---

## Coordinate a multisig wallet

Sync & Chat keeps the people who sign a shared wallet in step. Every device on the same wallet descriptor is discovered automatically, so labels, categories, and transactions stay consistent for all signers.

For the complete walkthrough of collaborative multisig signing, see [Collaboration in a Multisig]({{< ref "library/collaboration/" >}}).
