---
title: "Tor Yapılandırması"
description: "Start9 veya Umbrel aracılığıyla kendi düğümünüzü kullanın"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [
  "aileler için güvenli Bitcoin cüzdanı",
  "bitcoin",
  "bitcoin biriktirme",
  "donanım imzalayıcı",
  "Bitcoin saklama sağlayıcıları",
  "Finansal Danışmanlar",
  "bitcoin cüzdanı",
  "trezor",
  "ABD bitcoin",
  "BTC",
  "HODL",
  "BitcoinGüvenliği",
  "Tor Yapılandırması"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---

### {{< page-title >}}  
 

- Tor çalışıyorsa proxy'yi `127.0.0.1:9050` olarak ayarlayın  
- Electrum sunucusunu `abcdef.onion:50001` olarak ayarlayın; burada `50001` şifrelenmemiş Electrum bağlantısı için varsayılan porttur (Tor zaten şifreli)  
- Mempool.space örneğini `http://abcdef.onion` veya `http://abcdef.onion:80` olarak ayarlayın (Tor tarayıcısında da çalışması gerekir)

 </br>

 
 ![tor config](config.png)
 { .img-fluid .mb-5 }