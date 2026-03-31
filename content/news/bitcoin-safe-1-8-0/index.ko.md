---
title: "Bitcoin Safe 1.8.0"
date: "2026-03-31"
description: "Bitcoin Safe 1.8.0 릴리스 노트입니다. 잔액 차트 확대, 사용자 지정 nLocktime, 앱 잠금 모드, 더 쉬운 업데이트가 포함됩니다."
videos:
  - "https://www.youtube.com/watch?v=S0O40-p_w0M"
---

## 새로운 기능

#### 잔액 차트 확대

잔액 차트 확대 기능이 추가되었습니다 ([#492](https://github.com/andreasgriffin/bitcoin-safe/pull/492)).

{{< video src="zoom.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 잔액 차트 확대" description="Bitcoin Safe 1.8.0의 잔액 차트 확대 미리보기." >}}

#### 사용자 지정 nLocktime

사용자 지정 nLocktime 지원이 추가되었습니다. 이를 통해 거래가 확인될 수 있는 가장 이른 블록 높이 또는 시간을 설정할 수 있습니다 ([#481](https://github.com/andreasgriffin/bitcoin-safe/pull/481)).

{{< video src="nLocktime.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 사용자 지정 nLocktime" description="Bitcoin Safe 1.8.0의 사용자 지정 nLocktime 지원 미리보기." >}}

#### Jade Bluetooth 지원

Jade용 Bluetooth 지원이 추가되었습니다 ([#517](https://github.com/andreasgriffin/bitcoin-safe/pull/517)).

{{< video src="bluetooth.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 Jade Bluetooth 지원" description="Bitcoin Safe 1.8.0의 Jade Bluetooth 지원 미리보기." >}}

#### 앱 잠금 모드

앱 잠금 모드가 추가되었습니다. 이는 앱이 백그라운드에서 계속 실행되는 동안 잠그는 방법입니다 ([#519](https://github.com/andreasgriffin/bitcoin-safe/pull/519)).

{{< video src="app-lock.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 앱 잠금 모드" description="Bitcoin Safe 1.8.0의 앱 잠금 모드 미리보기." >}}

또한 Windows에서의 원활한 업데이트 기능과 macOS 및 Linux에서 더 쉬운 업데이트가 포함됩니다 ([#513](https://github.com/andreasgriffin/bitcoin-safe/pull/513)).

## 개선 사항

- 알림 기록을 이제 트레이 아이콘에서 확인할 수 있습니다 ([#493](https://github.com/andreasgriffin/bitcoin-safe/pull/493))
- 버그 수정과 작은 UI 개선

## 기여

- [@bsn21m](https://github.com/bsn21m)이 [#538](https://github.com/andreasgriffin/bitcoin-safe/pull/538)에서 첫 기여를 했습니다
- [bdk](https://github.com/bitcoindevkit/) 팀과 [@rustaceanrob](https://github.com/rustaceanrob)에게 감사드립니다
- 디자인과 UX 지원을 해준 [@design-rrr](https://github.com/design-rrr)에게 큰 감사를 전합니다
