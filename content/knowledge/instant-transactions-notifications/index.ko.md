---
title: "즉시 거래 알림"
description: "Bitcoin Safe가 즉시 거래 알림을 받는 방법"
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
  "즉시 거래 알림"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---



![](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }


### {{< page-title >}}  
 
  


**Bitcoin Safe** (버전 **1.5.0**부터) 는 지갑과 관련된 들어오는 비트코인 거래에 대한 즉시 알림을 지원합니다. 내부적으로는 다음과 같이 동작합니다:




##### 1. 📡 Bitcoin P2P 네트워크 수신

Bitcoin Safe는 전 세계적인 **피어 투 피어(P2P)** 네트워크에 참여하는 하나 이상의 **Bitcoin Core 노드**에 직접 연결합니다. 이 노드들은 **mempool**에 포함되기 위해 브로드캐스트된 신규 거래를 지속적으로 주고받습니다.

Bitcoin Safe는 이러한 브로드캐스트 메시지를 수동으로 수신(listen)하면서 다음을 확인합니다:

* 지갑의 **주소** 또는 **UTXO**가 관련된 거래인지 여부

✅ **개인정보 보호**
이 방식은 **완전히 비공개적**입니다. 외부에 당신의 지갑에 관한 어떤 정보도 **노출하지 않습니다**.
Bitcoin Safe는 일반적인 Bitcoin Core 노드처럼 동작합니다: 공개 P2P 트래픽만 수신하며 — 지갑에 특정한 정보를 발표하거나 요청하지 않습니다.



##### 2. 🧠 매치 발견 — 다음에 무슨 일이 일어나나요?

일치하는 거래가 발견되면, 사용 중인 백엔드에 따라 Bitcoin Safe는 다르게 반응합니다:

###### 옵션 A: ⚡ Electrum 또는 Esplora 백엔드

* Bitcoin Safe는 **백그라운드 동기화**를 트리거하여 서버로부터 전체 거래 및 지갑 상태를 가져옵니다.

###### 옵션 B: 🔍 Compact Block Filters (Neutrino 모드)

* 지갑은 **미확정 거래를 로컬 지갑 데이터에 바로 추가**합니다 — 추가 조회가 필요 없습니다.



#### ⚙️ 옵트인 / 옵트아웃 동작

사용자 선호도 및 프라이버시 설정을 존중하기 위해:

* 🔒 **기존 사용자**가 버전 1.5.0 이상으로 업그레이드할 경우, 이 기능은 **기본적으로 옵트인(사용자 수동 활성화 필요)** 상태입니다 — 네트워크 설정에서 수동으로 활성화할 수 있습니다.
* 🚀 **신규 사용자**의 경우, 이 기능은 **기본적으로 활성화(옵트아웃 가능)** 되어 있습니다. 이 기능은 **프라이버시를 보호**하면서 지갑 활동을 실시간으로 추적하는 데 매우 유용하기 때문입니다.

언제든지 이 기능을 켜고 끌 수 있으므로 사용자는 완전한 제어권을 가집니다。
 
 


#### ⚠️  확인된(컨펌된) 거래만 신뢰할 수 있습니다

Bitcoin Safe는 브로드캐스트된 거래가 실제로 유효한지 자체적으로 검증할 수 없습니다. 특히 Electrum 서버와 연결된 Bitcoin 노드 둘 다를 공격자가 통제하는 경우, 공격자는 다음을 수행할 수 있습니다:

* 사용자의 주소를 포함한 가짜 거래를 만들어내고
* 지갑 알림을 유발하기 위해 이를 브로드캐스트하고
* 그 거래가 **유효하지 않거나 합의 규칙과 충돌**하도록 하여 절대 확정되지 않게 만들 수 있습니다


  


#### ✅ 요약

버전 **1.5.0**부터 Bitcoin Safe는 즉시 거래 알림을 다음과 같이 지원합니다:

* Bitcoin Core처럼 P2P 비트코인 네트워크를 수동으로 수신
* 지갑의 **주소** 또는 **UTXO**가 관련된 거래를 매칭
* Electrum/Esplora를 통해 전체 상세 정보를 가져오거나 Compact Block Filters로 직접 추가
* 외부에 지갑 데이터를 절대 노출하지 않음