---
aliases:
  - "/knowledge/tor-config/"
title: "Налаштування Tor"
description: "Використовуйте власний вузол через Start9 або Umbrel"
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
  "Tor Configuration"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---

### {{< page-title >}}  
 

- Встановіть проксі на `127.0.0.1:9050`, якщо у вас запущений Tor  
- Встановіть Electrum‑сервер на `abcdef.onion:50001`, де `50001` — типовий порт для незашифрованого transport Electrum (через Tor усе одно зашифровано)
- Встановіть інстанс mempool.space на `http://abcdef.onion` або `http://abcdef.onion:80` (має працювати і в Tor Browser)

 </br>

 
 ![tor config](config.png)
 { .img-fluid .mb-5 }
