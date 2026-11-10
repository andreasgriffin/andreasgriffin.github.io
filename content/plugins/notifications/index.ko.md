---
title: "지갑 알림"
description: "Bitcoin-Safe 지갑 및 앱 알림을 설정한 대상으로 전달하세요. 전달 방식, 개인정보 보호, 전송 시점을 세밀하게 제어할 수 있습니다."
draft: false
tags: ["Plugins"]
images: ["notifications.png"]
weight: 35
faq:
  title: "지갑 알림 관련 질문"
  items:
    - question: "Bitcoin-Safe는 어디로 알림을 보낼 수 있나요?"
      answer: "Bitcoin-Safe는 다음으로 알림을 보낼 수 있습니다:\n- 웹훅: 일반 JSON 또는 Slack 호환, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy, Gotify 형식\n- Nostr 다이렉트 메시지\n- Telegram 봇\n- SMTP를 통한 이메일\n- CalDAV 캘린더"
    - question: "알림에서 민감한 정보를 제외할 수 있나요?"
      answer: "네. 민감한 세부 정보 숨기기를 켜면, 메시지에는 Bitcoin-Safe 알림 이벤트가 발생했다는 일반적인 안내만 포함됩니다."
    - question: "어떤 이벤트를 어디로 보낼지 제어할 수 있나요?"
      answer: "대상마다 고유한 규칙이 있습니다. 각 대상이 받을 이벤트 유형을 선택하세요:\n- 지갑 거래\n- 예정된 결제\n- 동기화 및 채팅\n- 경고\n\n선택적으로 무작위 전송 지연도 설정할 수 있습니다."
    - question: "앱의 잠금 해제 상태를 유지해야 하나요?"
      answer: "아니요. 잠금 및 트레이로 최소화를 사용하면 지갑이 잠겨 있어도 Bitcoin-Safe가 백그라운드에서 계속 실행됩니다."
---

### {{< page-title >}}

<p class="lead">원하는 채널을 통해 지갑 활동에 대한 알림을 받으세요.</p>

<ul class="plugin-features">
<li>받은 거래와 보낸 거래, Sync&Chat 메시지, 기한이 된 예정 결제 등 ...</li>
<li>웹훅, Nostr, Telegram, 이메일, 캘린더 등으로 알림 전달</li>
<li>각 대상이 받을 이벤트를 선택하고 민감한 세부 정보를 숨기기</li>
<li>Bitcoin-Safe를 백그라운드에서 실행: <strong>잠금 및 트레이로 최소화</strong>를 사용하면 지갑이 잠겨 있어도 앱이 계속 실행됩니다</li>
</ul>

### 웹훅 설정

{{< video "webhook.mp4" controls >}}

### Nostr 다이렉트 메시지

{{< video "nostr.mp4" controls >}}

### 캘린더 알림

{{< video "calendar.mp4" controls >}}

### 대상 연결

- 하나 이상의 대상을 추가하세요. 각 대상은 고유한 수신자와 전달 규칙을 가질 수 있습니다.
- **이메일:** 호스트, 포트, 자격 증명, 발신자, 보안 설정으로 SMTP 서버에 직접 연결합니다. 관리형 Gmail 또는 Outlook 연동이 아닙니다.
- **Telegram:** 봇을 통해 채팅으로 보냅니다. 봇과 대화를 시작하면 설정을 확인하고 최근 채팅 ID를 찾을 수 있습니다.
- **Nostr DM:** 발신자 키를 설정한 릴레이를 통해 `npub` 수신자에게 암호화된 NIP-17 메시지를 보냅니다.
- **CalDAV:** 설정된 Nextcloud 캘린더 등 기존 캘린더에 이벤트를 추가합니다.
- **웹훅:** 일반 JSON 또는 Slack 호환 엔드포인트, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy, Gotify용 형식으로 보냅니다. 일반적인 엔드포인트 유형은 자동으로 감지될 수 있습니다.
- 대상 설정을 저장하고, 지원되는 경우 테스트 기능을 사용하세요.

### 보낼 내용 선택

- 각 대상이 받을 이벤트 유형을 선택하세요:
  - 지갑 거래
  - 예정된 결제
  - 동기화 및 채팅
  - 경고
- 민감한 세부 정보를 숨길 수 있습니다. 그러면 메시지에는 Bitcoin-Safe 알림 이벤트가 발생했다는 일반적인 안내만 포함됩니다.
- 선택한 최대값까지 무작위 전송 지연을 설정하세요.
- 사용 가능하고 세부 정보가 숨겨져 있지 않다면, 지갑 거래 메시지에 블록 탐색기 링크가 포함될 수 있습니다.

### 전송 확인

- 최근 기록에는 각 이벤트, 대상, 어댑터, 시간, 결과(전송됨, 일부 전송됨, 실패)가 표시됩니다.
- 전송은 설정한 대상과 그 가용성에 따라 달라집니다. 외부 서비스로 보내는 정보를 신중하게 고려하세요.

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">Bitcoin-Safe 다운로드</h2>
<p class="text-muted mb-3">플러그인은 Bitcoin-Safe에 포함되어 있습니다. 앱을 다운로드해 직접 사용해 보세요.</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">Bitcoin-Safe 다운로드</a>
<small class="text-muted">무료 오픈소스 · Windows, macOS, Linux</small>
</div>
</section>

### 자주 묻는 질문

<details>
<summary>Bitcoin-Safe는 어디로 알림을 보낼 수 있나요?</summary>

Bitcoin-Safe는 다음으로 알림을 보낼 수 있습니다:

- 웹훅: 일반 JSON 또는 Slack 호환, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy, Gotify 형식
- Nostr 다이렉트 메시지
- Telegram 봇
- SMTP를 통한 이메일
- CalDAV 캘린더

</details>

<details>
<summary>알림에서 민감한 정보를 제외할 수 있나요?</summary>

네. 민감한 세부 정보 숨기기를 켜면, 메시지에는 Bitcoin-Safe 알림 이벤트가 발생했다는 일반적인 안내만 포함됩니다.

</details>

<details>
<summary>어떤 이벤트를 어디로 보낼지 제어할 수 있나요?</summary>

대상마다 고유한 규칙이 있습니다. 각 대상이 받을 이벤트 유형을 선택하세요:

- 지갑 거래
- 예정된 결제
- 동기화 및 채팅
- 경고

선택적으로 무작위 전송 지연도 설정할 수 있습니다.

</details>

<details>
<summary>앱의 잠금 해제 상태를 유지해야 하나요?</summary>

아니요. 잠금 및 트레이로 최소화를 사용하면 지갑이 잠겨 있어도 Bitcoin-Safe가 백그라운드에서 계속 실행됩니다.

</details>
</content>
