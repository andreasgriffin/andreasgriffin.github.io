---
title: "コード署名ポリシーと Bitcoin Safe プライバシーポリシー"
description: "コード署名ポリシー"
draft: false
tags: ["legal"]
menu:
  footer:
    weight: 90
---


## コード署名ポリシー


無料のコード署名は [SignPath.io](https://about.signpath.io/) により提供され、証明書は [SignPath Foundation](https://signpath.org/) によって発行されます。


## プライバシーポリシー
このプログラムはデフォルトで以下を使用します
- ブロックチェーンデータを取得するために [blockstream.com](https://blockstream.com/) の electrum/esplora サーバーを使用します
- [mempool.space](https://mempool.space/) からメンプールの手数料情報を取得します

両方とも「ネットワーク設定」で自分の（個人用）サーバーを指定できます。

Sync&Chat 機能を有効にすると、[デフォルトのリレー](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py) が暗号化されたデータを承認済みの信頼できるデバイスに送信するために使用されます。自身のリレーは Sync&Chat 設定で指定できます。

このプログラムは、ユーザーまたはインストールや運用を行う人が明示的に要求しない限り、他のネットワークシステムへその他の情報を転送することはありません。