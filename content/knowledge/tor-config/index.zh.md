---
title: "Tor 配置"
description: "通过 Start9 或 Umbrel 使用您自己的节点"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [ "Tor"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---

### {{< page-title >}}  
 

- 如果您正在运行 Tor，请将代理设置为 `127.0.0.1:9050`  
- 将 Electrum 服务器设置为 `abcdef.onion:50001`，其中 `50001` 是非加密 Electrum 传输的默认端口（反正 Tor 已经是加密的）  
- 将 mempool space 实例设置为 `http://abcdef.onion` 或 `http://abcdef.onion:80`（在 Tor 浏览器中也应可用）

 </br>

 
 ![Tor 配置](config.png)
 { .img-fluid .mb-5 }