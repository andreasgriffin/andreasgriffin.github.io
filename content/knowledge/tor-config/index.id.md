---
title: "Konfigurasi Tor"
description: "Gunakan node Anda sendiri melalui Start9 atau Umbrel"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [
  "dompet Bitcoin aman untuk keluarga",
  "bitcoin",
  "tabungan bitcoin",
  "penandatangan perangkat keras",
  "kustodian Bitcoin",
  "penasihat keuangan",
  "dompet bitcoin",
  "trezor",
  "usa bitcoin",
  "BTC",
  "HODL",
  "KeamananBitcoin",
  "Konfigurasi Tor"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---

### {{< page-title >}}  
 

- Atur proxy ke `127.0.0.1:9050` jika Anda menjalankan tor  
- Atur server Electrum ke `abcdef.onion:50001` di mana `50001` adalah port default untuk transport Electrum yang tidak terenkripsi (Tor sudah terenkripsi juga)
- Atur instance mempool space ke `http://abcdef.onion` atau `http://abcdef.onion:80` (seharusnya juga berfungsi di Tor Browser)

 </br>

 
 ![tor config](config.png)
 { .img-fluid .mb-5 }