---
title: "تكوين Tor"
description: "استخدم عقدتك الخاصة عبر Start9 أو Umbrel"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [
  "محفظة بيتكوين آمنة للعائلات",
  "بيتكوين",
  "الادخار بعملة بيتكوين",
  "جهاز توقيع مادي",
  "أمناء بيتكوين",
  "مستشارون ماليون",
  "محفظة بيتكوين",
  "trezor",
  "بيتكوين الولايات المتحدة",
  "BTC",
  "HODL",
  "أمن البيتكوين",
  "تكوين Tor"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---

### {{< page-title >}}  
 

- اضبط البروكسي إلى `127.0.0.1:9050` إذا كان Tor يعمل  
- اضبط خادم Electrum إلى `abcdef.onion:50001` حيث أن `50001` هو المنفذ الافتراضي لنقل Electrum غير المشفر (بالمناسبة Tor مشفَّر)  
- اضبط مثيل Mempool Space إلى `http://abcdef.onion` أو `http://abcdef.onion:80` (ينبغي أن يعمل أيضًا في متصفح Tor)

 </br>

 
 ![تكوين تور](config.png)
 { .img-fluid .mb-5 }