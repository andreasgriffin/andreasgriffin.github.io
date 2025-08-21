---
title: "Configuración de Tor"
description: "Utiliza tu propio nodo mediante Start9 o Umbrel"
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
 

- Configura el proxy en `127.0.0.1:9050`  si tienes Tor en ejecución  
- Configura el servidor Electrum en `abcdef.onion:50001`  donde `50001` es el puerto predeterminado para el transporte Electrum no cifrado  (Tor está cifrado de todos modos)
- Configura la instancia de mempool space en `http://abcdef.onion` o `http://abcdef.onion:80` (también debería funcionar en el Tor Browser)

 </br>

 
 ![configuración de Tor](config.png)
 { .img-fluid .mb-5 }