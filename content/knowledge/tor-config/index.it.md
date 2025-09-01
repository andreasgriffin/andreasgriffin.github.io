---
title: "Configurazione Tor"
description: "Usa il tuo nodo tramite Start9 o Umbrel"
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
 

- Imposta il proxy su `127.0.0.1:9050`  se hai Tor in esecuzione  
- Imposta il server Electrum su `abcdef.onion:50001`  dove `50001` è la porta predefinita per il trasporto Electrum non cifrato  (Tor è comunque cifrato)
- Imposta l'istanza di Mempool Space su `http://abcdef.onion` o `http://abcdef.onion:80` (dovrebbe funzionare anche nel browser Tor)

 </br>

 
 ![configurazione tor](config.png)
 { .img-fluid .mb-5 }