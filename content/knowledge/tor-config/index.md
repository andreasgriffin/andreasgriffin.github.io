---
aliases:
  - "/knowledge/tor-config/"
title: "Tor Configuration"
description: "Use your own node via Start9 or Umbrel"
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
 

- Set the proxy to `127.0.0.1:9050`  if you have a tor running  
- Set the electrum server to `abcdef.onion:50001`  where `50001` is the default port for non encrypted electrum transport  (tor is encrypted anyway)
- Set the mempool space instance to `http://abcdef.onion` or `http://abcdef.onion:80` (it should also work in the tor browser)

 </br>

 
 ![tor config](config.png)
 { .img-fluid .mb-5 }
 