---
title: "Bitcoin-Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "재구성된 설정 마법사, Compact Block Filters 기반의 개인 동기화, 그리고 확장된 하드웨어 월렛 지원을 포함한 Bitcoin-Safe 2.0.0 릴리스 노트입니다."
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">릴리스 안내</p>
    <h2 class="display-6 mb-3">Bitcoin-Safe 2.0 - 안내형 월렛 설정, 개인 체인 동기화, 그리고 디바이스 중심 서명</h2>
    <p class="lead mb-4">이번 릴리스에는 새로 만든 설정 마법사, Compact Block Filters를 이용한 개인 체인 동기화, 그리고 각 하드웨어 디바이스를 중심으로 정리된 서명 흐름이 포함됩니다. cold storage가 궁금했지만 아직 망설이고 있었다면, 지금이 시도해 볼 만한 릴리스입니다.</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Bitcoin-Safe 2.0 다운로드</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">새로운 점 보기</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">단계별 월렛 설정</h2>
          <p class="mb-0">새 마법사는 각 단계를 설명하고, 모호함을 줄이며, 새로운 사용자가 multisig의 강점을 잃지 않고 올바른 경로를 고를 수 있게 도와줍니다.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">개인 월렛 동기화</h2>
          <p class="mb-0">새 월렛은 이제 기본적으로 Compact Block Filters와 동기화되므로, third-party Electrum indexer에 기대지 않고도 개인적으로 체인을 스캔할 수 있습니다.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">디바이스 중심 서명</h2>
          <p class="mb-0">서명 흐름은 이제 눈앞의 디바이스를 중심으로 유지되며, QR, USB, Bluetooth, 파일, 그리고 multisig coordination을 위한 다음 단계가 더 명확해졌습니다.</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## self-custody로 가는 안내형 경로 {#setup-flow}

첫 실행 경험이 처음부터 다시 만들어졌습니다. Bitcoin-Safe는 하드웨어 기반 multisig를 포함한 진지한 self-custody를 계속 지향하며, 2.0은 이제 새로운 사용자에게 그 설정 과정을 안내해 주는 경로를 제공합니다. 새 마법사는 지금 무엇이 일어나고 있는지, 현재 흐름의 어느 단계인지, 그리고 다음으로 넘어가기 전에 각 signer가 무엇을 필요로 하는지 설명합니다.

<p class="small text-muted">구현 세부 사항은 <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a>를 참고하세요.</p>

리디자인의 핵심 내용:

- 처음 사용하는 사람이 올바른 출발점을 고를 수 있도록 돕는 새로운 환영 화면
- 월렛 생성 중 단계별 진행 흐름
- 집중된 안내와 상황별 도움말이 포함된 디바이스별 서명 화면
- 백업이 명확하게 유지되도록 디바이스 이름과 아이콘이 들어간 recovery PDF

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## Compact Block Filters를 이용한 개인적이고 견고한 체인 동기화 {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}})는 이제 Bitcoin-Safe 2.0의 새 월렛 동기화를 담당합니다. Electrum 서버에 어떤 주소가 내 것인지 묻는 대신, Bitcoin-Safe는 무작위 Bitcoin Core peer들로부터 compact filters를 내려받아 로컬에서 확인함으로써 체인을 개인적으로 스캔할 수 있습니다.

<p class="small text-muted">구현 세부 사항은 <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a>를 참고하세요.</p>


- 월렛 동기화는 첫 실행부터 개인적으로 유지됩니다
- third-party Electrum 서버에 의존하지 않습니다
- Electrum을 선호하는 사용자를 위해 여전히 사용 가능합니다
- [초기 월렛 스캔 이후 즉시 동기화]({{< ref "library/compact-block-filters" >}})
- [relay된 트랜잭션에 대한 즉시 알림]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## 모든 디바이스를 위한 디바이스 중심 서명 흐름 {#device-focused-signing}

이번 리디자인은 월렛 생성 이후의 서명 흐름도 다시 구성합니다. 모든 signer를 위한 하나의 일반 화면 대신, Bitcoin-Safe는 현재 사용 중인 구체적인 디바이스를 중심으로 작업을 배치합니다.

<p class="small text-muted">구현 세부 사항은 <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a>를 참고하세요.</p>

- QR, USB, Bluetooth, 파일 내보내기/가져오기, 그리고 Sync & Chat 작업이 활성 signer 카드에 직접 표시됩니다
- 남아 있는 signers, 이미 서명한 디바이스, 다음에 필요한 작업을 한눈에 볼 수 있습니다
- 여러 디바이스가 섞인 multisig 흐름도 PSBT 전체에서 signer identity가 보이기 때문에 읽기 쉽습니다
- single-sig와 multisig 입력이 섞인 복잡한 트랜잭션도 올바르게 처리되어, 각 서명 단계가 명확하게 유지됩니다

![QR, USB, Bluetooth, 파일 내보내기, Chat & Sync를 위한 디바이스별 작업이 표시된 signer 카드](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## 비즈니스 워크플로와 power user를 위한 플러그인 아키텍처

Bitcoin-Safe 2.0은 Bitcoin 비즈니스와 power user를 위한 미래의 추가 플러그인을 위한 기반도 마련합니다. 앞으로 나올 것들도 계속 지켜봐 주세요 :-)

<p class="small text-muted">구현 세부 사항은 <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a>를 참고하세요.</p>

- 외부 *sources* 저장소를 통한 플러그인 배포
- 각 플러그인은 [andreasgriffin]({{< gpg_key_link >}})의 *GPG 서명*으로 보호되어 보안, 무결성, 배포를 보장합니다
- 플러그인별 버전 관리와 업데이트는 더 빠르고 독립적인 플러그인 개발을 가능하게 합니다

![QR, USB, Bluetooth, 파일 내보내기, Chat & Sync를 위한 디바이스별 작업이 표시된 signer 카드](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## 더 넓어진 디바이스 지원과 마무리 개선 {#hardware-support}

- 더 빠른 스캔을 위해 애니메이션 QR 코드가 **30%** 빨라졌습니다
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}})가 이제 USB를 통해 지원됩니다
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}})는 이제 USB와 QR에 더해 **Bluetooth**도 지원합니다
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}})와 [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}})가 지원 디바이스 목록에 추가되었습니다
- [지원되는 전체 디바이스 목록]({{< ref "library/supported-hardware-signers" >}}) 보기
- [reproducibility]({{< ref "library/reproducibility-and-security" >}})를 위한 자동 검사가 추가되었습니다
- 개선 사항의 [전체 목록](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0)은 여기에서 확인할 수 있습니다


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## 기존의 강점도 그대로 남아 있습니다

2.0 릴리스는 리셋이 아닙니다. 새로운 onboarding과 서명 흐름 아래에서도 Bitcoin-Safe는 일상에서 유용했던 기능들을 그대로 유지합니다. collaborative multisig, PDF 백업, 검색 가능한 월렛 기록, money-flow 시각화, label sync 등이 여기에 포함됩니다.

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">Bitcoin-Safe 2.0을 써볼 준비가 되셨나요?</h2>
  <p class="mb-3">최신 릴리스를 다운로드하고 새로운 onboarding, 개인 동기화, 그리고 하드웨어 월렛 개선 사항을 직접 살펴보세요.</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Bitcoin-Safe 다운로드</a>
</div>


<br><br>

## 감사합니다

이번 릴리스는 기여자, 테스터, 그리고 [프로젝트 전반의 후원자들]({{< ref "donate" >}})의 많은 노력 위에 세워졌습니다:

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r))에게 wizard 리디자인, plugin UI 작업, 그리고 **멋지고 끈질긴** UI/UX 지원에 감사드립니다
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/))에게 새 월렛의 개인 동기화를 가능하게 한 Compact Block Filter client에 감사드립니다
- Bitcoin-Safe의 핵심 라이브러리를 제공한 [Bitcoin Dev Kit 팀](https://github.com/bitcoindevkit/)에 감사드립니다
- nostr 기능을 뒷받침하는 라이브러리를 제공한 [ndk 팀](https://github.com/nostr-dev-kit/ndk)에도 감사드립니다
- release candidate를 테스트하고, 버그를 보고하고, 페이지를 번역하고, sats를 보내고, 프로젝트를 계속 앞으로 밀어 준 Bitcoin-Safe 커뮤니티의 모든 분들께 감사드립니다
- [번역자]({{< ref "donate/#translators" >}}) 여러분, 예를 들면 <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (베트남어)" title="qdyg-vn 🇻🇳 (베트남어)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (독일어)" title="bsn21m 🇩🇪 (독일어)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (스페인어)" title="cyphra 🇪🇸 (스페인어)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (중국어)" title="DaGrindDontStop 🇨🇳 (중국어)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


다음 릴리스를 후원하고 싶다면 여기에서 기부할 수 있습니다: {{< donation_btc >}}
