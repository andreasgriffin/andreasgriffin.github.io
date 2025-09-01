---
title: "다운로드"
description: "Bitcoin Safe 다운로드"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}


✅ **Bitcoin Safe는 새 버전이 있으면 자동으로 알리고 진위 여부를 검증합니다.**


Windows용 바이너리 파일은 서명되어 있습니다. [코드 서명 정책]({{< ref "code-signing-policy" >}})을 확인하세요. 여기에서 [Bitcoin Safe 개인정보 처리방침]({{< ref "code-signing-policy" >}})도 확인할 수 있습니다. macOS용 바이너리는 서명되어 있지 않으니 경고 메시지는 무시하셔도 됩니다.

<br>
<br>

###  macOS 

Bitcoin Safe를 macOS에서 실행하려면 다음 단계를 따르세요:
- 앱 폴더에 복사하세요
- 열려고 하면 경고가 표시됩니다
- *시스템 설정* --> *개인 정보 보호 및 보안* --> *'그래도 열기'*
- 이제 앱을 열 수 있습니다


<img src="/images/mac/copy-app.png" alt="macOS 앱 복사"   /> 
<img src="/images/mac/warning.png" alt="macOS 경고"   /> 
<img src="/images/mac/disable.png" alt="macOS에서 Bitcoin Safe 열기"   /> 

<br>
<br>

###  서명 검증

모든 소프트웨어는 제 개인 키로 서명되어 있습니다. 다음 단계를 따라 다운로드가 진짜인지 확인하세요:

제 [공개 키]({{< gpg_key_link >}})를 가져온 후 다음으로 서명을 확인하세요:
{{< gpg_import_code >}}


<br> 
<br>


<!-- ### Alternative install  via pip  on Mac, Linux, or Windows 
PyPi: https://pypi.org/project/bitcoin-safe/
python -m pip install bitcoin-safe
python -m bitcoin_safe
-->