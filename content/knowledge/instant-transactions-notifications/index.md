---
aliases:
  - "/knowledge/instant-transactions-notifications/"
title: "Instant transaction notifications"
description: "How Bitcoin Safe Receives Instant Transaction Notifications"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [
  "secure Bitcoin wallet for families",
  "bitcoin",
  "bitcoin saving",
  "hardware signer",
  "Bitcoin Custodians",
  "Financial Advisors",
  "bitcoin wallet",
  "trezor",
  "usa bitcoin",
  "BTC",
  "HODL",
  "BitcoinSecurity",
  "Instant transaction notifications"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---



![Bitcoin Safe logo](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }


### {{< page-title >}}  
 
  


**Bitcoin Safe** (starting from version **1.5.0**) supports instant notification of incoming Bitcoin transactions relevant to your wallet. Here’s how it works under the hood:




##### 1. 📡 Listening to the Bitcoin P2P Network

Bitcoin Safe connects directly to one or more **Bitcoin Core nodes**, which participate in the global **peer-to-peer (P2P)** network. These nodes continuously exchange newly broadcasted transactions intended for inclusion in the **mempool**.

Bitcoin Safe listens passively to these broadcast messages and checks whether:

* any transaction involves **addresses** or **UTXOs** from your wallet.

✅ **Privacy Preserving**
This method is **completely private**. It does **not reveal anything** about your wallet to the outside world.
Bitcoin Safe behaves just like a regular Bitcoin Core node: it only listens to public P2P traffic — never announcing or requesting anything specific to your wallet.



##### 2. 🧠 Match Found — What Happens Next?

If a matching transaction is found, Bitcoin Safe will react differently depending on the backend you're using:

###### Option A: ⚡ Electrum or Esplora Backend

* Bitcoin Safe will **trigger a background sync** to fetch the full transaction and wallet state from the server.

###### Option B: 🔍 Compact Block Filters (Neutrino Mode)

* The wallet will **directly add the unconfirmed transaction** to your local wallet data — no further lookup needed.



#### ⚙️ Opt-In / Opt-Out Behavior

To respect user preferences and privacy settings:

* 🔒 **For existing users** upgrading to version 1.5.0 or later, this feature is **opt-in by default** — you can enable it manually in network settings.
* 🚀 **For new users**, this feature is **enabled (opt-out)** by default, since it is both **privacy-preserving** and **highly useful** for tracking wallet activity in real-time.

You remain in full control and can toggle this feature at any time.
 


![Notification settings screenshot](config.png)
{ .img-fluid .mb-5 }


#### ⚠️  Only confirmed transactions can be trusted

Bitcoin Safe cannot **not** validate that a broadcast transaction is valid. An attacker — especially one controlling both your Electrum server and the Bitcoin node you're connected to — could:

* Craft a fake transaction involving your address
* Broadcast it to trigger a wallet notification
* Ensure it never confirms, because it’s **invalid** or **conflicts with consensus rules**


  


#### ✅ Summary

From version **1.5.0**, Bitcoin Safe supports instant transaction notifications by:

* Listening passively to the P2P Bitcoin network (like Bitcoin Core)
* Matching transactions involving your wallet's **addresses** or **UTXOs**
* Fetching full details via Electrum/Esplora or adding directly via Compact Block Filters
* Never revealing any wallet data to the outside world


