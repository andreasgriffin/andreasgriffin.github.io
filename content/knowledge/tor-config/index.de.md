---
title: "Tor-Konfiguration"
description: "Verwende deinen eigenen Node über Start9 oder Umbrel"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [ "tor"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---

### {{< page-title >}}  
 

- Setze den Proxy auf `127.0.0.1:9050`  wenn du Tor laufen hast  
- Setze den Electrum-Server auf `abcdef.onion:50001`  wobei `50001` der Standardport für unverschlüsselten Electrum-Transport ist  (Tor ist sowieso verschlüsselt)
- Setze die mempool.space-Instanz auf `http://abcdef.onion` oder `http://abcdef.onion:80` (es sollte auch im Tor-Browser funktionieren)

 </br>

 
 ![Tor-Konfiguration](config.png)
 { .img-fluid .mb-5 }