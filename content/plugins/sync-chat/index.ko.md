---
title: "Sync & Chat"
description: "지갑의 참여자를 찾고, 레이블과 카테고리를 동기화하며, 안전하게 채팅하고, PSBT를 한 번의 클릭으로 공유하세요."
draft: false
tags: ["Plugins", "sync-chat-mainpage"]
images: ["logo.png"]
weight: 30
faq:
  title: "Sync & Chat 관련 질문"
  items:
    - question: "기기들은 어떻게 서로를 찾나요?"
      answer: "Sync & Chat은 같은 지갑 디스크립터를 사용하는 다른 기기를 찾습니다. 디스크립터는 검색에 쓰이기 전에 해시되므로 평문으로 노출되지 않습니다. 또한 발견된 각 기기는 수동으로 추가하고 신뢰할 수 있는 것으로 표시해야만 채팅에 참여할 수 있습니다. 따라서 디스크립터가 비밀이 아니더라도 채팅은 안전하게 유지됩니다."
    - question: "실제로 공동 작업은 어떻게 진행되나요?"
      answer: "1. 설정(최초 1회): 각 참여자의 기기를 추가하고 신뢰할 수 있는 것으로 표시합니다.\n2. 생성: 참여자 중 한 명이 PSBT를 만들고 자신의 서명을 추가합니다.\n3. 공유: PSBT를 모든 참여자 또는 선택한 참여자에게 보냅니다.\n4. 서명: 각 참여자가 거래에 서명을 추가하여 거래가 완전히 서명될 때까지 진행합니다.\n5. 전송: 마지막 서명자가 거래를 브로드캐스트하면, 거래가 모든 참여자의 지갑에 나타납니다."
    - question: "무엇이 동기화되나요?"
      answer: "Sync & Chat은 다음을 동기화합니다:\n- 서명자 간의 코인 카테고리와 레이블(서로 다른 운영체제 간에도 동기화)\n- 한 번의 클릭으로 PSBT 공유"
    - question: "채팅은 비공개인가요?"
      answer: "네. 지갑 채팅은 암호화되어 Nostr를 통해 전달됩니다. 레이블 백업도 Nostr를 통해 암호화된 상태로 저장됩니다."
---

### {{< page-title >}}

<p class="lead">멀티시그 서명자들을 조율하고, Bitcoin-Safe에서 바로 지갑 정보를 동기화된 상태로 유지하세요.</p>

<ul class="plugin-features">
<li>같은 지갑 디스크립터를 사용하는 다른 기기 찾기</li>
<li>서명자 간 레이블과 카테고리 동기화</li>
<li>안전하게 채팅하고 PSBT를 한 번의 클릭으로 공유</li>
</ul>

### 레이블 동기화

{{< video src="../../library/label-sync/label-sync.mp4" controls="true" >}}

### 공동 서명

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

멀티시그 공동 서명의 전체 안내는 [멀티시그에서의 공동 작업]({{< ref "library/collaboration/" >}})을 참고하세요.

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
<summary>기기들은 어떻게 서로를 찾나요?</summary>

Sync & Chat은 같은 지갑 디스크립터를 사용하는 다른 기기를 찾습니다. 디스크립터는 검색에 쓰이기 전에 해시되므로 평문으로 노출되지 않습니다. 또한 발견된 각 기기는 수동으로 추가하고 신뢰할 수 있는 것으로 표시해야만 채팅에 참여할 수 있습니다. 따라서 디스크립터가 비밀이 아니더라도 채팅은 안전하게 유지됩니다.

</details>

<details>
<summary>실제로 공동 작업은 어떻게 진행되나요?</summary>

1. **설정(최초 1회):** 각 참여자의 기기를 추가하고 신뢰할 수 있는 것으로 표시합니다.
2. **생성:** 참여자 중 한 명이 PSBT를 만들고 자신의 서명을 추가합니다.
3. **공유:** PSBT를 모든 참여자 또는 선택한 참여자에게 보냅니다.
4. **서명:** 각 참여자가 거래에 서명을 추가하여 거래가 완전히 서명될 때까지 진행합니다.
5. **전송:** 마지막 서명자가 거래를 브로드캐스트하면, 거래가 모든 참여자의 지갑에 나타납니다.

</details>

<details>
<summary>무엇이 동기화되나요?</summary>

Sync & Chat은 다음을 동기화합니다:

- 서명자 간의 코인 카테고리와 레이블(서로 다른 운영체제 간에도 동기화)
- 한 번의 클릭으로 PSBT 공유

</details>

<details>
<summary>채팅은 비공개인가요?</summary>

네. 지갑 채팅은 암호화되어 Nostr를 통해 전달됩니다. 레이블 백업도 Nostr를 통해 암호화된 상태로 저장됩니다.

</details>

{{< sync-page-box >}}
</content>
