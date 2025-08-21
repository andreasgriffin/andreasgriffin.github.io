---
title: "การตั้งค่า Tor"
description: "ใช้โหนดของคุณเองผ่าน Start9 หรือ Umbrel"
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
 

- ตั้งพร็อกซีเป็น `127.0.0.1:9050` หากคุณมี Tor กำลังรัน  
- ตั้งค่าเซิร์ฟเวอร์ Electrum เป็น `abcdef.onion:50001` โดยที่ `50001` เป็นพอร์ตเริ่มต้นสำหรับการเชื่อมต่อ Electrum ที่ไม่เข้ารหัส (Tor ถูกเข้ารหัสอยู่แล้ว)
- ตั้งค่าอินสแตนซ์ Mempool Space เป็น `http://abcdef.onion` หรือ `http://abcdef.onion:80` (น่าจะใช้งานได้ในเบราว์เซอร์ Tor ด้วย)

 </br>

 
 ![tor config](config.png)
 { .img-fluid .mb-5 }