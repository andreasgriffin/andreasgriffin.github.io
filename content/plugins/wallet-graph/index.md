---
aliases:
  - "/plugins/wallet-graph/"
title: "Wallet Graph"
date: "2026-11-04"
description: "Explore your Bitcoin wallet's transaction history as an interactive graph and export every transaction and UTXO as GraphML."
draft: false
tags: ["Plugins"]
images: ["logo.png"]
weight: 20
lead: "Explore your wallet's transaction history as an interactive graph."
features:
  - "Follow transaction inputs and outputs over time"
  - "Jump between inputs, outputs, and transactions"
  - "Export transactions and UTXOs as GraphML for analysis"
media:
  - type: carousel
    srcs: ["graph1.jpg", "graph2.png"]
    per_slide: 1
    caption: "Wallet Graph shows transactions and the coins they spend as a navigable graph."
faq:
  title: "Wallet Graph questions"
  items:
    - question: "What can I do with the Wallet Graph?"
      answer: "You can follow transaction inputs and outputs over time and jump between inputs, outputs, and transactions inside one interactive view."
    - question: "Can I analyze the data outside Bitcoin-Safe?"
      answer: "Yes. Wallet Graph exports your transactions and UTXOs as GraphML, a graph format that third-party analysis tools can load."
    - question: "Which transactions does the graph show?"
      answer: "It visualizes your wallet's transaction history, including the coins (UTXOs) behind it."
---

## Analyze coin flow visually

Wallet Graph turns your wallet history into a navigable graph instead of a flat transaction list. Inputs and outputs are connected, so you can trace how funds moved through your wallet over time.

## Export as GraphML

Exporting writes your transactions and UTXOs as a GraphML file, so you can continue the analysis in external graph tools or keep it as a structured backup of your wallet history.
