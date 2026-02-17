---
title: "Bitcoin Safe를 선택해야 하는 이유"
description: "여러 데스크탑 비트코인 지갑이 있습니다. Bitcoin Safe가 돋보이는 이유를 확인하세요."
draft: false
tags: ["Featured","Features"]
images: ["logo.png"]
keywords: ["비트 코인 안전", "독특한 기능", "안전한 지갑", "사용자 친화적"]
weight: 1000
---



## {{< page-title >}} 
<!-- {{< page-description >}}  -->

<br>
<!-- <br> -->

### ✔ 안전한 비트코인 보관, 간편하게 
<!-- - ❌ 2-of-3 Multisignature is complex to use in other wallets -->
<!-- - 2-of-3 Multi-signature is a good choice  
    - Robust against loss or leak of 1 seed  -->
- The {{<text-name-with-logo>}} <a  href={{< ref "knowledge/setup-singlesig-wallet" >}} role="button">설정 마법사</a>    makes Single and  Multi-signature **easy**   for non-technical people
    --> 각 단계에 따라 안전한 지갑을 설정하세요.   
    <img  src="/images/multisig-steps.png" style="max-width: 600px; width: 100%;" alt="Multisig setup steps">
    - The <a  href={{< ref "features/pdf-export" >}}   role="button"> <img  src="pdf-export.png" width="100" alt="PDF export">  PDF Export</a>   helps you to backup the important wallet descriptor with each seed.
    - 각 하드웨어 서명자(hardware signer)와 멀티시그를 등록하세요
    - 모든 주요 하드웨어 서명자가 작동하는지 확인하기 위해 지갑으로의 수신 및 지출 테스트를 포함합니다
<br>


<br>

#### ✔ 라벨 동기화 및 백업

{{<text-name-with-logo>}}는 암호화된 <a href="https://nostr.com/ ">nostr</a> 메시지의 힘을 통해 마법처럼
- <a  href="{{< ref "features/label-sync" >}}" role="button">동기화</a>하여 컴퓨터 간에 코인 카테고리와 라벨을 일치시킵니다
- 코인 카테고리와 라벨을 백업합니다. 필요한 것은 짧은 백업 키만 백업하는 것입니다.
 

<br>

####  ✔ 다수 참여자 멀티시그 협업

3-of-5 멀티시그 지갑에 참여하시나요?

- 지갑이 생성된 후 {{<text-name-with-logo>}}는 협업을 위해 암호화된 <a href="https://nostr.com/ ">nostr</a> 그룹 채팅을 생성하고 <a  href="{{< ref "features/collaboration" >}}" role="button">PSBT 전송</a>을 통해 서명을 주고받을 수 있게 합니다. 
- 물론 <a  href="{{< ref "features/label-sync" >}}" role="button">라벨 동기화</a>도 작동합니다.
- 보안을 위해 각 참가자는 다른 사용자를 인증(간단한 클릭)해야 합니다.


<br>


#### ✔ 주소를 코인 카테고리로 정리

 <img  src="coin-categories.png" width="150" alt="Coin categories"> 
 
- 주소를 **코인 카테고리**로 그룹화할 수 있습니다. 각 주소에 라벨을 다는 것보다 더 쉽습니다.
- 생성하는 각 PSBT에 대해 일치하는 코인 카테고리를 선택하면 {{<text-name-with-logo>}}가 해당 카테고리에서만 입력(입금 UTXO)을 선택합니다.   
- {{<text-name-with-logo>}}는 PSBT나 트랜잭션이 코인 카테고리를 혼합하면 경고합니다.


<br>


#### ✔ 실수 발생 가능성 제거

사람들은 과거에 많은 값비싼 실수를 해왔습니다. 대부분은 사람들이 절대 컴퓨터에 시드를 입력하지 않는다면 예방할 수 있습니다. {{<text-name-with-logo>}}는 컴퓨터에서 시드를 사용하는 것을 방지하고 하드웨어 서명자 사용을 권장합니다.

- {{<text-name-with-logo>}}는 가장 일반적인 하드웨어 서명자들을 완벽히 지원합니다(예:  <a href="https://store.coinkite.com/promo/8BFF877000C34A86F410">Coldcard</a>, 
            <a href="https://store.coinkite.com/promo/8BFF877000C34A86F410">Coldcard Q</a>, 
            <a href="https://shop.bitbox.swiss/?ref=MOB4dk7gpm">Bitbox02</a>, 
            <a href="https://store.blockstream.com/?code=XEocg5boS77D">Blockstream Jade</a>,    
            <a href="https://affil.trezor.io/SHtN">Trezor Safe</a>,
            <a href="https://foundation.xyz/passport">Foundation Passport</a>,
            <a href="https://keyst.one/?rfsn=8630473.c25550a&utm_source=refersion&utm_medium=affiliate&utm_campaign=8630473.c25550a">Keystone</a>,
            <a href="https://shop.ledger.com/?r=400f1fff75b5">Ledger</a>,
            <a href="https://clavastack.com/en/?coupon=bitcoin-safe">Specter DIY</a>)  
- {{<text-name-with-logo>}}는 각 하드웨어 서명자에 대한 단계별 안내 스크린샷을 포함하여 모든 과정을 안내합니다 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-images "hardware-signer-screenshots" >}}
    </div>

   

<br>




#### ✔ 🔋 필수 기능 포함 🔋 


{{<text-name-with-logo>}}는 사용하기 쉽게 설계되었습니다. 그러나 모든 중요한 고급 사용자 기능도 포함되어 있습니다.
- electrum/esplora 서버, mempool 인스턴스 및 nostr 릴레이를 직접 선택하세요
- 어디서나 CSV 가져오기 및 내보내기
- RBF, 트랜잭션 취소 및 최종화된 PSBT 편집
- 그리고 훨씬 더 많은 기능: <a href="https://github.com/andreasgriffin/bitcoin-safe?tab=readme-ov-file#comprehensive-feature-list">전체 기능 목록</a>


<br>