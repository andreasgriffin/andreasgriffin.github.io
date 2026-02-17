---
title: "Konfiguracja Tor"
description: "Użyj własnego węzła za pośrednictwem Start9 lub Umbrel"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [
  "bezpieczny portfel Bitcoin dla rodzin",
  "bitcoin",
  "oszczędzanie w bitcoinach",
  "sprzętowy podpisywacz transakcji",
  "powiernicy Bitcoin",
  "doradcy finansowi",
  "portfel bitcoin",
  "trezor",
  "bitcoin w USA",
  "BTC",
  "HODL",
  "bezpieczeństwo Bitcoina",
  "Konfiguracja Tor"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---

### {{< page-title >}}  
 

- Ustaw proxy na `127.0.0.1:9050`, jeśli masz działający Tor  
- Ustaw serwer Electrum na `abcdef.onion:50001`, gdzie `50001` to domyślny port dla niezaszyfrowanego transportu Electrum  (i tak Tor jest szyfrowany)
- Ustaw instancję mempool.space na `http://abcdef.onion` lub `http://abcdef.onion:80` (powinno też działać w przeglądarce Tor)

 </br>

 
 ![konfiguracja Tor](config.png)
 { .img-fluid .mb-5 }