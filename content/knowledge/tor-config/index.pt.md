---
title: "Configuração do Tor"
description: "Use o seu próprio nó via Start9 ou Umbrel"
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
 

- Defina o proxy para `127.0.0.1:9050` se tiver um Tor a correr  
- Defina o servidor Electrum para `abcdef.onion:50001`, onde `50001` é a porta por defeito para transporte Electrum não encriptado (o Tor é encriptado na mesma)
- Defina a instância do Mempool Space para `http://abcdef.onion` ou `http://abcdef.onion:80` (deverá também funcionar no Tor Browser)

 </br>

 
 ![tor config](config.png)
 { .img-fluid .mb-5 }