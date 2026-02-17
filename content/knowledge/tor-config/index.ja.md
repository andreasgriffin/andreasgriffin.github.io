---
title: "Tor の設定"
description: "Start9 や Umbrel を使って自分のノードを利用する"
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
  "Tor の設定"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---

### {{< page-title >}}  
 

- Torが動作している場合、プロキシを `127.0.0.1:9050` に設定します  
- Electrumサーバーを `abcdef.onion:50001` に設定します。`50001` は非暗号化のElectrumトランスポートのデフォルトポートです（Tor自体は暗号化されています）  
- mempool.space のインスタンスを `http://abcdef.onion` または `http://abcdef.onion:80` に設定します（Torブラウザでも動作するはずです）

 </br>

 
 ![Tor 設定](config.png)
 { .img-fluid .mb-5 }