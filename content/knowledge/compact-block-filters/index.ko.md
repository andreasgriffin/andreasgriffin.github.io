---
title: "컴팩트 블록 필터"
description: "컴팩트 블록 필터가 무엇인지, 그리고 Electrum 서버보다 어떻게 프라이버시를 높이는지 이해하세요."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "컴팩트 블록 필터"
  - "CBF"
  - "프라이버시"
  - "비트코인 지갑"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**컴팩트 블록 필터(CBF)** 를 사용하면 [Bitcoin Safe]({{< ref "/" >}}) 는 Electrum 서버에 주소를 묻지 않고도 블록체인을 스캔할 수 있습니다.

![Bitcoin Safe가 여러 랜덤 Bitcoin Core 피어에서 컴팩트 블록 필터를 다운로드합니다.](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

중앙 서버를 조회하는 대신, Bitcoin Safe는 각 블록에 대한 작은 필터를 랜덤한 Bitcoin Core 피어들로부터 다운로드합니다. 지갑은 이를 로컬에서 확인하고 필요할 때만 전체 블록을 내려받습니다.

### CBF 와 Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">항목</th>
        <th scope="col">컴팩트 블록 필터</th>
        <th scope="col">Electrum 서버</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">프라이버시</th>
        <td><span class="text-success fw-semibold">좋음</span> - 지갑 데이터가 로컬에 남음</td>
        <td><span class="text-danger fw-semibold">나쁨</span> - 서버가 주소와 기록을 볼 수 있음</td>
      </tr>
      <tr>
        <th scope="row">데이터 출처</th>
        <td><span class="text-success fw-semibold">좋음</span> - 랜덤한 Bitcoin Core 피어</td>
        <td><span class="text-warning fw-semibold">중립</span> - 하나의 선택한 서버</td>
      </tr>
      <tr>
        <th scope="row">초기 동기화</th>
        <td><span class="text-warning fw-semibold">중립</span> - 보통 더 느림</td>
        <td><span class="text-success fw-semibold">좋음</span> - 보통 더 빠름</td>
      </tr>
      <tr>
        <th scope="row">지속 동기화</th>
        <td><span class="text-success fw-semibold">좋음</span> - 첫 동기화 후 매우 빠름</td>
        <td><span class="text-success fw-semibold">좋음</span> - 보통 빠름</td>
      </tr>
      <tr>
        <th scope="row">추천 대상</th>
        <td><span class="text-success fw-semibold">좋음</span> - 프라이버시를 중시하는 사용자</td>
        <td><span class="text-success fw-semibold">좋음</span> - 가장 빠른 설정과 복구가 필요한 사용자</td>
      </tr>
    </tbody>
  </table>
</div>

### CBF 를 사용하는 이유

- 더 나은 프라이버시: 지갑이 서버에 주소를 묻지 않습니다.
- 신뢰할 수 있는 인덱서 불필요: Bitcoin Safe 는 비트코인 네트워크와 직접 통신합니다.
- 가벼운 동기화: 필터가 작아서 전체 블록체인이 필요 없습니다.

### 기대할 수 있는 점

- 새 지갑 또는 복구: 첫 동기화는 보통 **5~30분** 걸립니다.
- 이미 동기화된 지갑: 보통 **매우 빠르게** 따라잡으며, 종종 **30초 이내** 입니다.
- Electrum 에서 CBF 로 전환: 보통 역시 **30초 이내** 입니다.

Bitcoin Safe 가 연결할 피어 수를 선택할 수 있습니다. 피어가 많을수록 중복성은 좋아지지만, 대개 대역폭과 동기화 시간도 늘어납니다. 기본값은 **2** 개입니다.

### 미확인 거래

CBF 는 **확인된 블록** 만 다룹니다. 미확인 입금 알림도 받으려면 [Instant transaction notifications]({{< ref "knowledge/instant-transactions-notifications/" >}}) 를 켠 상태로 두세요. 이것이 기본 설정입니다.

### 기술 참고

컴팩트 블록 필터는 [BIP158](https://bips.dev/158/) 에 정의되어 있습니다. Bitcoin Safe 는 오픈 소스 [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto) 를 사용합니다.

_Bitcoin network monitoring_ 설정에서 자신의 Bitcoin Core 노드를 초기 피어로 사용할 수도 있습니다.

![초기 노드 설정](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
