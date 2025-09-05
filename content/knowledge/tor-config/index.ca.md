---
title: "Configuració de Tor"
description: "Utilitza el teu propi node mitjançant Start9 o Umbrel"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [
  "moneder Bitcoin segur per a famílies",
  "bitcoin",
  "estalvi en bitcoin",
  "signador de maquinari",
  "custodis de Bitcoin",
  "assessors financers",
  "moneder de bitcoin",
  "trezor",
  "bitcoin EUA",
  "BTC",
  "HODL",
  "Seguretat de Bitcoin",
  "Configuració de Tor"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---

### {{< page-title >}}  
 

- Estableix el proxy a `127.0.0.1:9050` si tens Tor en funcionament  
- Estableix el servidor Electrum a `abcdef.onion:50001`, on `50001` és el port predeterminat per al transport Electrum no xifrat (Tor ja xifra la connexió de totes maneres)
- Configura la instància de mempool.space a `http://abcdef.onion` o `http://abcdef.onion:80` (també hauria de funcionar amb el navegador Tor)

 </br>

 
 ![configuració de Tor](config.png)
 { .img-fluid .mb-5 }