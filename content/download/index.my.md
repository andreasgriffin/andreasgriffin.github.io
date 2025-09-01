---
title: "ဒေါင်းလုဒ်"
description: "Bitcoin Safe ကို ဒေါင်းလုဒ်"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}


✅ **Bitcoin Safe သည် ဗားရှင်းအသစ်ရှိပါက အလိုအလျောက် သတိပေးပြီး မူရင်းဖြစ်ကြောင်း အတည်ပြုပါသည်။**


Windows binary ဖိုင်များကို လက်မှတ်ထိုးထားပါသည်၊ [Code signing policy]({{< ref "code-signing-policy" >}}) ကို စစ်ဆေးပါ။ ဒီနေရာမှာ [Bitcoin Safe privacy policy]({{< ref "code-signing-policy" >}}) ကို ကြည့်ရှုနိုင်သည်။ MacOS binaries များကို လက်မှတ်မထိုးထားပါက သတိပေးချက်ကို ကျေးဇူးပြု၍ မစိုးမနင်းပါနှင့်။

<br>
<br>

###  macOS 

Please follow the steps to run Bitcoin Safe on macOS:
- အက်ပ်ကို သင့် App ဖိုလ်ဒါထဲသို့ ကူးထည့်ပါ။
- ဖွင့်ကြည့်ပြီး သတိပေးချက်တက်မည်ကို တွေ့ရပါမည်။
- သွားပါ *System Settings* (စနစ် ဆက်တင်များ) --> *Privacy & Security* (ကိုယ်ရေးကာကွယ်ရေးနှင့် လုံခြုံရေး) --> *Open Anyway* (သော်လည်း ဖွင့်ပါ)
- ယခု ဖွင့်နိုင်ပါပြီ။

<img src="/images/mac/copy-app.png" alt="macOS အက်ပ် ကူးထည့်ခြင်း"   /> 
<img src="/images/mac/warning.png" alt="macOS သတိပေးချက်"   /> 
<img src="/images/mac/disable.png" alt="macOS Bitcoin Safe ဖွင့်ခြင်း"   /> 

<br>
<br>

###  Verify signature

All software is signed with my private key. Verify the download is authentic by following these steps:

ကျွန်တော်၏ [public key]({{< gpg_key_link >}}) ကို import ပြုလုပ်ပြီး အောက်ပါနည်းဖြင့် လက်မှတ်ကို အတည်ပြုပါ။
{{< gpg_import_code >}}


<br> 
<br>


<!-- ### Alternative install  via pip  on Mac, Linux, or Windows 
PyPi: https://pypi.org/project/bitcoin-safe/
python -m pip install bitcoin-safe
python -m bitcoin_safe
-->