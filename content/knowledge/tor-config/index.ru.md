---
title: "Конфигурация Tor"
description: "Используйте собственный узел через Start9 или Umbrel"
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
 

- Установите прокси на `127.0.0.1:9050`, если у вас запущен Tor  
- Установите сервер Electrum на `abcdef.onion:50001`, где `50001` — порт по умолчанию для незашифрованного транспорта Electrum  (Tor и так обеспечивает шифрование)
- Установите экземпляр mempool space на `http://abcdef.onion` или `http://abcdef.onion:80` (это также должно работать в Tor Browser)

 </br>

 
 ![tor config](config.png)
 { .img-fluid .mb-5 }