---
title: "Tor ဆက်တင်"
description: "Start9 သို့မဟုတ် Umbrel မှတဆင့် မိမိ၏ ကိုယ်ပိုင် node ကို အသုံးပြုပါ"
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
 

- Tor သင့်စက်တွင် လည်ပတ်နေပါက proxy ကို `127.0.0.1:9050` အဖြစ် သတ်မှတ်ပါ  
- Electrum server ကို `abcdef.onion:50001` အဖြစ် သတ်မှတ်ပါ။ `50001` သည် မကာကွယ်ထားသော Electrum သယ်ယူပို့ဆောင်မှုအတွက် ပုံမှန် port ဖြစ်သည် (Tor သည် အခြေအနေအရ ကာကွယ်ထားပါသည်)  
- Mempool.space instance ကို `http://abcdef.onion` သို့မဟုတ် `http://abcdef.onion:80` အဖြစ် သတ်မှတ်ပါ (Tor browser တွင်လည်း အလုပ်လုပ်နိုင်သည်)

 </br>

 
 ![tor config](config.png)
 { .img-fluid .mb-5 }