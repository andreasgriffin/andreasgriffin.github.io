---
title: "하드웨어 서명기 필수"
description: "Bitcoin Safe는 보안을 극대화하고 소프트웨어 기반 키 저장의 위험을 피하기 위해 메인넷에서 하드웨어 전용 시드만 허용합니다. 그 이유는 다음과 같습니다."
draft: false
tags: ["Featured", "Knowledge" ]
keywords: [
  "Bitcoin Safe",
  "하드웨어 지갑",
  "소프트웨어 시드",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "멀티시그",
  "PSBT",
  "셀프 커스터디",
  "비트코인 보안",
  "주소 포이즈닝",
  "비트코인 도구"
]
images: ["logo.png" ]
# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=dbSmQmt0uDI"
weight: 21
---


![](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }

## 🚫 왜 Bitcoin Safe는 메인넷에서 소프트웨어 시드를 차단하나요?

🤔 불편하지 않나요?

🔥 사실 — 이것은 **중대한 보안 향상**입니다.

Bitcoin Safe는 **메인넷에서는 소프트웨어 시드를 허용하지 않고, 테스트넷(Testnet), 시그넷(Signet), 레그렛(Regtest)에서만 소프트웨어 시드를 허용**합니다. 이유는 다음과 같습니다:

### ✅ 메인넷에서 소프트웨어 시드를 차단하는 이유

- 🧠 **소프트웨어 시드는 안전하지 않습니다**
  - 컴퓨터는 위험 요소로 가득합니다: 클립보드 하이재커, 맬웨어, 브라우저 취약점 등.
  - 한 번의 실수로 시드가 유출되면 — 끝입니다.
  - 콜드 스토리지는 절대 핫 환경에서 시작되어선 안 됩니다.

</br>

- 🧊 **콜드 스토리지는 처음부터 콜드여야 합니다**
  - 사용자는 종종 소프트웨어 지갑에서 시드를 생성한 뒤 하드웨어로 옮기곤 합니다.
  - 하지만 최초 노출은 이미 발생한 것이며 — 되돌릴 수 없습니다.
  - 진정한 콜드 스토리지는 처음부터 하드웨어 서명기에서 생성되어야 합니다.

</br>

- 🎣 **피싱은 소프트웨어 습관에서 번성합니다**
  - 앱에 시드를 입력하는 습관은 잘못된 UX 패턴을 신뢰하게 만듭니다.
  - 하드웨어 전용은 더 안전한 습관을 강제하고 노출을 제한합니다.
  - ✅ 메인넷에서의 시드 제거 = 피싱 피해자 감소.

</br>

- 🧪 **개발자는 여전히 유연성을 가집니다**
  - 소프트웨어 시드는 다음에서 허용됩니다:
    - Testnet
    - Signet
    - Regtest
  - 개발자에게 이상적입니다. 실제 사토시에는 위험이 없습니다. 🧡



</br>


- 🔐 **메인넷은 하드웨어 서명기를 요구합니다 — 예외 없음**
  - 🔌 USB, 📷 QR, 💾 SD 카드를 통한 모든 주요 기기 지원
    - [Coldcard]({{< ref "knowledge/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Foundation Passport]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Ledger]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Keystone]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "knowledge/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "knowledge/supported-hardware-signers" >}})
  - [지원되는 모든 서명기 보기 →]({{< ref "knowledge/supported-hardware-signers" >}})


---

## 🛡️ 주소 포이즈닝(주소 변조) 보호

Bitcoin Safe는 **수신 주소를 색상으로 구분**하여 주소 포이즈닝을 즉시 알아차리게 합니다:

- 🟢 초록 = 검증된 수신 주소  
- 🟡 노랑 = 체인지 주소  

누군가가 클립보드를 위조된 주소로 오염시키려 해도, 즉시 확인할 수 있습니다.

![주소 포이즈닝 감지 예시](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ USB 또는 QR을 통한 주소 검증

수신 주소를 하드웨어 서명기에서 직접 검증하세요 — 화면을 신뢰할 필요가 없습니다.

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ 각 하드웨어 서명기별 안내

- {{<text-name-with-logo>}} 는 각 하드웨어 서명기별 스크린샷과 지침을 포함하여 모든 단계를 안내합니다 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-hardware-signer-screenshots >}}
    </div>

   
---



## 🤝 협업형 멀티시그를 쉽게

Bitcoin Safe는 멀티시그를 사용자 친화적이고 팀에 적합하게 만듭니다:

- 🔐 암호화된 Nostr 채팅  
- 🔁 원클릭 PSBT 공유  
- 🔌 USB, 📷 QR, 💾 SD 카드

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ 모든 사용자를 위한 강력한 기능

- 🟧 싱글시그 지갑 마법사  
- 🟨 2-of-3 멀티시그 설정  
- 🟩 임의의 n-of-m 구성 지원  
- 🖨️ 인쇄 가능한 PDF 백업 시트  
- 🔁 Nostr를 통한 라벨 동기화  
- 🔍 전체 자금 흐름 다이어그램 및 검색 가능한 거래 기록

![Bitcoin Safe의 거래 다이어그램](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 글로벌하고 사용자 친화적

- 다국어 지원: {{< flags-short >}}
- 작동 환경: Windows, macOS & Linux  
- 드래그 앤 드롭 PSBT / CSV  
- 거래, UTXO, 금액 등 고급 필터

---

## 💡 요약 (TL;DR)

Bitcoin Safe = 진짜 비트코인 보관:

✅ 메인넷에서는 하드웨어 전용  
✅ 소프트웨어 시드 노출 없음  
✅ 초보자 친화적 멀티시그  
✅ 개발자 친화적 테스트 환경  
✅ 가족 및 팀용 기능 완비  

🔗 [Bitcoin-Safe.org](https://Bitcoin-Safe.org)  
🎥 YouTube 채널 →: https://youtube.com/@BitcoinSafeOrg