---
aliases:
- /ko/knowledge/supported-hardware-signers/metrovault/
title: MetroVault
signer: metrovault
bucket: knowledge
---

MetroVault는 오래된 Android 기기를 Bitcoin Safe 전용 오프라인 Bitcoin 서명 기기로 바꿔 줍니다. 일상적으로 쓰는 휴대전화에는 설치하지 마세요. 먼저 기기를 초기화하고, **오프라인** 상태로 인터넷과 분리한 채 유지하며, 서명 용도로만 사용하세요.

## 예상할 사항

- 설치 전에 오래된 Android 기기를 초기화하고 서명 장치로만 사용하세요.
- 다른 앱을 설치하지 말고, 어떤 계정에도 로그인하지 말고, SIM 카드를 넣지 말고, 기기를 다시 인터넷에 연결하지 마세요.
- 지갑 데이터, 디스크립터, PSBT를 QR 코드로 Bitcoin Safe와 주고받습니다.
- 멀티시그 디스크립터를 등록하고 Bitcoin Safe용 서명 장치 데이터를 내보냅니다.
- 서명하기 전에 MetroVault 화면의 모든 세부 정보를 확인하세요.

## Android 기기를 초기화하고 오프라인 서명 장치로만 사용하세요

MetroVault의 원본 문서에는 [권장 기기 설정](https://github.com/gorunjinian/MetroVault/#recommended-device-setup)이 있습니다. 이것을 필수 요구 사항으로 보세요. 설정 후에도 인터넷과 분리된 전용 공장 초기화 **오프라인 휴대전화**를 사용하고, 오직 서명에만 사용해야 합니다.

1. 설치 전에 휴대전화를 공장 초기화하세요.
2. Google 계정 설정을 건너뛰고 기기를 오프라인 상태로 유지하세요.
3. 비행기 모드를 항상 켜 두세요.
4. Wi-Fi, Bluetooth, NFC, 모바일 데이터를 끄세요.
5. SIM 카드를 제거하세요.
6. USB 디버깅을 끄세요.
7. 다른 앱을 설치하지 말고, 서명 외의 용도로 휴대전화를 사용하지 마세요.

실사용 환경에서는 가능하면 소스 코드에서 직접 빌드하세요. 기기를 오프라인 상태로 유지하고 서명 전용으로 사용할 수 없다면 MetroVault의 실사용 자금에는 사용하지 마세요.
