---
title: "Configuration de Tor"
description: "Utilisez votre propre nœud via Start9 ou Umbrel"
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
 

- Configurez le proxy sur `127.0.0.1:9050` si Tor est en cours d'exécution  
- Configurez le serveur Electrum sur `abcdef.onion:50001` où `50001` est le port par défaut pour le transport Electrum non chiffré (Tor est chiffré de toute façon)
- Définissez l'instance mempool.space sur `http://abcdef.onion` ou `http://abcdef.onion:80` (cela devrait aussi fonctionner dans le navigateur Tor)

 </br>

 
 ![configuration Tor](config.png)
 { .img-fluid .mb-5 }