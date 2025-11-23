---
aliases:
  - "/knowledge/compact-block-filters/"
title: "Compact Block Filters"
description: "Understand what compact block filters are and how they improve privacy over Electrum servers."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "compact block filters"
  - "CBF"
  - "privacy"
  - "Bitcoin wallet"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}


Bitcoin Safe   1.6.0 introduces **Compact Block Filters (CBF)** as an optional way to sync your wallet.  Instead of asking a centralized Electrum server for your wallet history, Bitcoin Safe can now download a tiny summary file for every block directly from random Bitcoin Core peers. These summaries act like a short checklist that lets your wallet decide on its own whether a block might contain one of your transactions.

Because Bitcoin Safe makes the decision locally, no third-party server ever learns which addresses or transactions you care about. You get the same confirmation data that a full node would keep, but in a lighter format that fits everyday devices.

**Why it feels better:**

- 📦 **Small downloads:** Each filter is only a few kilobytes, so you can sync through normal home connections without storing the whole blockchain.
- 🔐 **Direct from the network:** Bitcoin Safe talks to multiple random Bitcoin Core nodes, just like other nodes do, reducing the chance that any single observer can profile you.
- 🕵️ **Local matching:** Your wallet checks the filters locally. If a filter looks relevant, only then does it fetch the specific block, keeping your addresses private.

Electrum servers, by contrast, search the blockchain on your behalf. Every request shares addresses of your wallet with the server operator, who could log that information. With compact block filters, Bitcoin Safe downloads the same neutral data that every node shares. No one can tell which addresses belong to you because your wallet never reveals them in the first place.

Below is a simple view of how Bitcoin Safe connects when CBF is enabled. Notice how it mirrors the way Bitcoin Core nodes already talk to each other:


![Bitcoin Safe downloads compact block filters from several random Bitcoin Core peers.](logo.jpg)
{ .img-fluid .mb-5   style="max-width: 450px;" }


You can choose how many peers Bitcoin Safe should connect to. More peers need more bandwidth and result in a slower sync time.  The default is 2.  

 
### What to expect when syncing

CBF changes how long you wait depending on what you are doing:

1. ✨ **Setting up or recovering a wallet:** Whether you create a new wallet or recover an existing one, the initial sync pulls filters for the entire history of your wallet. Expect this one-time process to take **between 5 and 30 minutes**, depending on your internet speed.
2. 🚀 **Opening a wallet that was already synced:** Bitcoin Safe only needs to grab the newest filters since your last session. That catch-up usually finishes in **under 30 seconds**.
3. 🔄 **Switching from Electrum servers to CBF:** Since the wallet was previously synced with Electrum servers,   Bitcoin Safe only needs to grab the newest filters, which will be usually **less than 30 seconds**.

### Stay informed about unconfirmed payments

Compact block filters cover **confirmed blocks** only. To hear about incoming transactions before they are confirmed, make sure you also enable [Instant transaction notifications]({{< ref "knowledge/instant-transactions-notifications/" >}}). That feature listens to the live peer-to-peer messages from a random Bitcoin node so you can react to mempool activity without giving up privacy.


<br>
<br>



### Technical details


- *For developers who want to go deeper:* compact block filters follow the [BIP158 specification](https://bips.dev/158/) and are explored in [Elle Mouton’s overview of Golomb-coded sets](https://ellemouton.com/posts/bip158/). Bitcoin Safe’s implementation relies on the open-source [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto).
- You can add your own Bitcoin core node to the peers for Compact Block Filter syncing, by choosing the _Initial node_ of the _Bitcoin network monitoring_.


![](inital-node.png)
{ .img-fluid .mb-5   style="max-width: 414px;" }

