---
title: "Tor विन्यास"
description: "Start9 या Umbrel के माध्यम से अपना नोड उपयोग करें"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [
  "परिवारों के लिए सुरक्षित बिटकॉइन वॉलेट",
  "बिटकॉइन",
  "बिटकॉइन बचत",
  "हार्डवेयर साइनर",
  "बिटकॉइन कस्टोडियन",
  "वित्तीय सलाहकार",
  "बिटकॉइन वॉलेट",
  "trezor",
  "यूएसए बिटकॉइन",
  "BTC",
  "HODL",
  "BitcoinSecurity",
  "Tor विन्यास"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---

### {{< page-title >}}  
 

- प्रॉक्सी को `127.0.0.1:9050` पर सेट करें यदि आपके पास Tor चल रहा है  
- Electrum सर्वर को `abcdef.onion:50001` पर सेट करें, जहाँ `50001` नॉन-एन्क्रिप्टेड Electrum ट्रांसपोर्ट के लिए डिफ़ॉल्ट पोर्ट है (Tor वैसे भी एन्क्रिप्टेड है)
- Mempool.space इंस्टेंस को `http://abcdef.onion` या `http://abcdef.onion:80` पर सेट करें (यह Tor ब्राउज़र में भी काम करना चाहिए)

 </br>

 
 ![टोर विन्यास](config.png)
 { .img-fluid .mb-5 }