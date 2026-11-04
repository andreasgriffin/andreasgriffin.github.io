---
title: "안전하지 않은 COLDCARD 시드"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "Coinkite 기기에서 생성한 시드로 보호된 자금을 옮기기 위한 간단한 안내입니다."
---

[Coinkite는 영향을 받는 COLDCARD 펌웨어의 시드 생성 취약점을 공개했습니다](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). [예측 가능한 RNG fallback과 32비트 reseed에 관한 Block의 기술 분석](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware)도 확인하세요. 펌웨어를 업데이트해도 기존 시드는 복구되지 않습니다.

**Coinkite 제품으로 시드를 생성했다면 가능한 한 빨리 이전하세요!**

## 이전 체크리스트

1. **COLDCARD가 아닌 서명 기기**([지원 기기 보기]({{< ref "library/supported-hardware-signers" >}}))에서 완전히 새로운 시드를 생성하세요. 기존 시드를 재사용하지 마세요. 그런 다음 해당 서명 기기를 Bitcoin-Safe 설정 마법사와 함께 사용하여 새로운 [단일 서명 지갑]({{< ref "library/setup-singlesig-wallet" >}}) 또는 [다중 서명 지갑]({{< ref "library/setup-multisig-wallet" >}})을 만드세요.
   - COLDCARD가 아닌 하드웨어 서명 기기가 없다면, 공장 초기화한 전용 Android 기기를 오프라인으로 유지하고 서명에만 사용하는 조건으로 [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}})를 이용할 수 있습니다.
   - 새 지갑이 올바르게 설정되었는지 확인하기 위해 마법사의 수신 및 전송 테스트를 완료하세요. 백업과 새 서명 기기에 표시된 수신 주소를 확인하고, 소액의 테스트 금액을 받은 뒤 새 지갑의 다른 검증된 주소로 self-send를 성공적으로 수행하세요.
2. 이전 거래에 서명하세요.
   - **영향받은 지갑이 단일 서명 지갑인 경우:** 빠르게 확인되도록 높은 수수료로 일반적인 방식으로 브로드캐스트하세요.
   - **영향받은 지갑이 다중 서명 지갑인 경우:** 공개 mempool에 공개 키가 노출되므로 일반적인 방식으로 브로드캐스트하지 마세요. 서명된 raw transaction을 복사하여 [MARA Slipstream](https://slipstream.mara.com/)으로 직접 제출하세요.
3. 전체 잔액이 새 지갑에 도착해 확인될 때까지 기존 COLDCARD를 보관한 다음 최신 펌웨어로 업데이트하세요.

다른 사람의 이전을 돕는 경우 시드 단어를 공유하거나 촬영하거나 입력해 달라고 절대 요청하지 마세요. 시드는 비공개로 유지하고 서명 기기에만 입력해야 합니다.
