---
title: "即時トランザクション通知"
description: "Bitcoin Safe が即時トランザクション通知を受け取る仕組み"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [
  "家族向けの安全なビットコインウォレット",
  "ビットコイン",
  "ビットコイン貯蓄",
  "ハードウェア署名デバイス",
  "ビットコイン保管者",
  "ファイナンシャルアドバイザー",
  "ビットコインウォレット",
  "trezor",
  "usa bitcoin",
  "BTC",
  "HODL",
  "ビットコインセキュリティ",
  "即時トランザクション通知"
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
 
  


**Bitcoin Safe**（バージョン **1.5.0** 以降）は、ウォレットに関連する着信の Bitcoin トランザクションの即時通知をサポートします。仕組みは次のとおりです：




##### 1. 📡 Bitcoin P2P ネットワークのリッスン

Bitcoin Safe は、グローバルなピアツーピア（**P2P**）ネットワークに参加する1つ以上の **Bitcoin Core ノード** に直接接続します。これらのノードは、**mempool** に含めることを目的とした新たにブロードキャストされたトランザクションを継続的に交換します。

Bitcoin Safe はこれらのブロードキャストメッセージを受動的にリッスンし、次の点をチェックします：

* 任意のトランザクションがあなたのウォレットの **アドレス** または **UTXO** に関係しているかどうか

✅ **プライバシー保護**
この方法は**完全にプライベート**です。外部に対してウォレットに関する情報を**何も明らかにしません**。
Bitcoin Safe は通常の Bitcoin Core ノードと同様に振る舞います：公開された P2P トラフィックのみをリッスンし、ウォレット固有の何かを発表したり要求したりすることは一切ありません。



##### 2. 🧠 マッチが見つかった — 次に何が起こるか？

マッチするトランザクションが見つかった場合、使用しているバックエンドに応じて Bitcoin Safe は異なる反応をします：

###### Option A: ⚡ Electrum または Esplora バックエンド

* Bitcoin Safe はバックグラウンド同期を**トリガー**して、サーバーから完全なトランザクションとウォレット状態を取得します。

###### Option B: 🔍 Compact Block Filters（Neutrino モード）

* ウォレットは **未確認トランザクションを直接ローカルのウォレットデータに追加** します — 追加の照会は不要です。



#### ⚙️ オプトイン / オプトアウトの挙動

ユーザーの設定とプライバシーを尊重するために：

* 🔒 **既存ユーザー** がバージョン 1.5.0 以降にアップグレードする場合、この機能は **デフォルトでオプトイン** になっています — ネットワーク設定で手動で有効化できます。
* 🚀 **新規ユーザー** については、この機能は **デフォルトで有効（オプトアウト可能）** です。これは **プライバシーを保護** しつつ、ウォレットの活動をリアルタイムで追跡する上で非常に有用だからです。

いつでもこの機能を切り替えて完全に制御できます。
 
 

![Notification settings screenshot](config.png)
{ .img-fluid .mb-5 }


#### ⚠️  確認済み（confirmed）トランザクションのみを信頼してください

Bitcoin Safe はブロードキャストされたトランザクションが有効であることを検証することはできません。攻撃者、特にあなたが接続している Electrum サーバーと Bitcoin ノードの両方を支配している者は、次のようなことが可能です：

* あなたのアドレスを含む偽のトランザクションを作成する
* ウォレット通知を引き起こすためにそれをブロードキャストする
* それが **無効** であるか、**コンセンサスルールと競合する** ために決して確認されないようにする


  


#### ✅ 要約

バージョン **1.5.0** 以降、Bitcoin Safe は即時トランザクション通知を次の方法でサポートします：

* P2P Bitcoin ネットワークを受動的にリッスン（Bitcoin Core と同様）
* ウォレットの **アドレス** や **UTXO** に関係するトランザクションをマッチング
* Electrum/Esplora を介して完全な詳細を取得、または Compact Block Filters を通じて直接追加
* 外部にウォレットデータを決して明らかにしないこと