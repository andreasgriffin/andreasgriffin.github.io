---
title: "보안과 재현 가능성"
description: "Bitcoin Safe는 재현 가능한 빌드, 서명된 커밋, 서명된 릴리스, 독립적인 외부 모니터링을 포함한 높은 수준의 바이너리 보안 기준을 따릅니다."
draft: false
tags: ["Featured", "Features", "Security"]
images: ["logo.png"]
keywords: ["reproducible builds", "verify binaries", "signed commits", "signed releases", "appimage", "flatpak", "windows exe", "binary security"]
weight: 18
---

### {{< page-title >}}
{{< page-description >}}
<br>

![Bitcoin Safe의 재현 가능한 빌드 결과](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 500px;" }

웹사이트에서 다운로드하는 앱이 공개 소스 코드와 실제로 일치하도록, 다운로드 무결성을 보호하는 여러 계층을 구현했습니다:

- **재현 가능한 빌드**: Linux `deb`, `AppImage`, `Flatpak` 빌드와 Windows `portable exe`, `setup exe`는 바이트 단위로 재현할 수 있습니다. 다시 빌드한 파일이 정확히 일치한다면, 해당 바이너리가 같은 소스 코드에서 만들어졌다는 강력한 증거가 됩니다.
- **서명된 저장소 기록**: [Bitcoin Safe GitHub 저장소](https://github.com/andreasgriffin/bitcoin-safe/commits/main)는 검증된 서명 커밋을 공개하므로, 검토자는 릴리스에 포함된 코드를 누가 작성했는지 확인할 수 있습니다.
- **서명된 바이너리**: 릴리스 파일은 Bitcoin Safe의 [공개 PGP 키]({{< gpg_key_link >}})로 서명되며, Windows 바이너리는 [코드 서명 정책]({{< ref "code-signing-policy" >}})도 따릅니다.
- **독립적인 재현성 검사**: [WalletScrutiny](https://walletscrutiny.com/desktop/bitcoin.safe/)는 Bitcoin Safe를 독립적으로 추적하고 데스크톱 릴리스에 대한 재현 가능한 검증 상태를 보여줍니다.
- **지속적인 서명 모니터링**: [BinaryWatch](https://binarywatch.org/)는 Bitcoin Safe 릴리스 파일과 그 서명이 Bitcoin Safe의 [공개 PGP 키]({{< gpg_key_link >}})에 대해 계속 유효한지 정기적으로 확인합니다.
- **업데이트 검증**: 업데이트는 Bitcoin Safe 안에 표시되며, 그 서명은 자동으로 검증됩니다.

이러한 조치를 모두 합치면 Bitcoin Safe는 바이너리 보안을 사후적인 추가 요소가 아니라 사용자 안전의 핵심으로 다루는 소수의 프로젝트에 속하게 됩니다.

### 보안은 Bitcoin Safe의 모든 측면에서 가장 중요한 기준입니다

바이너리 무결성뿐 아니라 Bitcoin Safe는 안전한 기본값, 좋은 운영 관행, 명확한 사용자 안내를 중심으로 설계되었습니다. 몇 가지 예시는 다음과 같습니다:

- **하드웨어 중심 보관**: Bitcoin Safe는 [하드웨어 사인러]({{< ref "knowledge/supported-hardware-signers" >}})를 요구하므로, 시드가 일반적인 컴퓨터의 핫 시크릿이 아니라 전용 장치에 남아 있게 됩니다.
- **더 안전한 설정 흐름**: 설정 마법사는 [하드웨어 사인러]({{< ref "knowledge/supported-hardware-signers" >}}) 테스트, [PDF 백업 시트]({{< ref "features/pdf-export/" >}}), 그리고 장치와 시드 백업을 어떻게 보관할지에 대한 안내를 포함해 실제 사용에 준비된 wallet을 만들 수 있도록 도와줍니다.
- **수신 주소 확인**: Bitcoin Safe는 공유하기 전에 사인러 자체에서 [수신 주소를 확인]({{< ref "knowledge/verify-receive-address/" >}})하기 쉽게 해줍니다.
- **address poisoning 감지**: 의심스러운 [유사 주소]({{< ref "features/address-poisoning/" >}})에 대해 경고합니다.
- **multisig 보안**: Bitcoin Safe는 multisig wallet을 지원하므로, 더 큰 자금을 단일 실패 지점이 아니라 여러 장치나 여러 사람으로 보호할 수 있습니다.
- **multisig를 더 쉽게 만드는 협업**: Bitcoin Safe는 [multisig 협업]({{< ref "features/collaboration/" >}})을 실용적으로 만들어, 실제 사용에서 설정과 서명 조정을 훨씬 더 쉽게 해줍니다.
- **명확한 서명 흐름**: 장치별 서명 화면은 PSBT 검토 중 혼란을 줄이고, 사용자가 올바른 사인러에서 올바른 작업을 하도록 도와줍니다.
