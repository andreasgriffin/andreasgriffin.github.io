---
title: "Tor 구성"
description: "Start9 또는 Umbrel을 통해 자체 노드를 사용하세요"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [
  "가족을 위한 안전한 비트코인 지갑",
  "비트코인",
  "비트코인 저축",
  "하드웨어 서명기",
  "비트코인 수탁자",
  "재무 고문",
  "비트코인 지갑",
  "trezor",
  "미국 비트코인",
  "BTC",
  "HODL",
  "비트코인 보안",
  "Tor 구성"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---

### {{< page-title >}}  
 

- Tor가 실행 중인 경우 프록시를 `127.0.0.1:9050`(으)로 설정하세요  
- Electrum 서버를 `abcdef.onion:50001`로 설정하세요. 여기서 `50001`은 암호화되지 않은 Electrum 전송의 기본 포트입니다(어차피 Tor은 암호화되어 있습니다)  
- mempool space 인스턴스를 `http://abcdef.onion` 또는 `http://abcdef.onion:80`로 설정하세요( Tor 브라우저에서도 작동해야 합니다)

 </br>

 
 ![Tor 구성](config.png)
 { .img-fluid .mb-5 }