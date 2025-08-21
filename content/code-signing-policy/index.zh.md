---
title: "代码签名政策与 Bitcoin Safe 隐私政策"
description: "代码签名政策"
draft: false
tags: ["legal"]
menu:
  footer:
    weight: 90
---


## 代码签名政策


免费代码签名由 [SignPath.io](https://about.signpath.io/) 提供，证书由 [SignPath Foundation](https://signpath.org/) 颁发。


## 隐私政策
本程序默认使用：
- 从 [blockstream.com](https://blockstream.com/) 的 electrum/esplora 服务器获取区块链数据
- 从 [mempool.space](https://mempool.space/) 获取 mempool 费用信息

您可以在“网络设置”中为两者指定您自己的（个人）服务器。

启用 Sync&Chat 功能时，会使用 [默认中继](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py) 将加密数据传输到您已批准的可信设备。您可以在 Sync&Chat 设置中指定您自己的中继。

除非用户或安装或操作本程序的人明确请求，否则本程序不会向其他网络系统传输任何其他信息。