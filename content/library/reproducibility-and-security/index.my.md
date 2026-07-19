---
aliases:
  - "/my/features/reproducibility-and-security/"
title: "လုံခြုံရေးနှင့် ပြန်လည်ထုတ်လုပ်နိုင်မှု"
description: "Bitcoin-Safe သည် binary security အတွက် မြင့်မားသောစံနှုန်းများကိုလိုက်နာပြီး reproducible builds, signed commits, signed releases နှင့် လွတ်လပ်သော ပြင်ပစောင့်ကြည့်မှုတို့ကို ပံ့ပိုးထားသည်။"
draft: false
bucket: features
tags: ["Featured", "Security"]
images: ["logo.png"]
keywords: ["reproducible builds", "verify binaries", "signed commits", "signed releases", "appimage", "flatpak", "windows exe", "binary security"]
weight: 18
---

### {{< page-title >}}
{{< page-description >}}
<br>

![Bitcoin-Safe အတွက် reproducible build outputs](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 500px;" }

ဝဘ်ဆိုက်မှ ဒေါင်းလုဒ်လုပ်သော app သည် အများသိရှိနိုင်သော source code နှင့် အမှန်တကယ်ကိုက်ညီကြောင်း သေချာစေရန် download integrity ကိုကာကွယ်ပေးသော အလွှာများစွာကို ကျွန်ုပ်တို့ ထည့်သွင်းထားသည်။

- **Reproducible builds**: Linux `deb`, `AppImage`, `Flatpak` builds နှင့် Windows `portable exe`, `setup exe` ဖိုင်များကို byte-for-byte ပြန်လည်တည်ဆောက်နိုင်သည်။ ပြန်တည်ဆောက်ထားသောဖိုင်သည် တိတိကျကျတူညီပါက ထို binary သည် တူညီသော source code မှ တည်ဆောက်ထားကြောင်း အားကောင်းသော အထောက်အထားဖြစ်သည်။
- **Signed repository history**: [Bitcoin-Safe GitHub repository](https://github.com/andreasgriffin/bitcoin-safe/commits/main) သည် verified signed commits များကို ထုတ်ပြန်ပေးသောကြောင့် review လုပ်သူများက release ထဲဝင်သည့် code ကို ဘယ်သူရေးသားခဲ့သည်ကို စစ်ဆေးနိုင်သည်။
- **Signed binaries**: Release files များကို Bitcoin-Safe ၏ [public PGP key]({{< gpg_key_link >}}) ဖြင့် sign လုပ်ထားပြီး Windows binaries များသည် [code signing policy]({{< ref "code-signing-policy" >}}) ကိုလည်း လိုက်နာသည်။
- **Independent reproducibility checks**: [WalletScrutiny](https://walletscrutiny.com/desktop/bitcoin.safe/) သည် Bitcoin-Safe ကို လွတ်လပ်စွာ စောင့်ကြည့်ပြီး desktop releases များအတွက် reproducible verification status ကို ပြသပေးသည်။
- **Ongoing signature monitoring**: [BinaryWatch](https://binarywatch.org/) သည် Bitcoin-Safe release files များနှင့် ၎င်းတို့၏ signatures များသည် Bitcoin-Safe ၏ [public PGP key]({{< gpg_key_link >}}) အပေါ် ဆက်လက် valid ဖြစ်နေသလားကို ပုံမှန်စစ်ဆေးသည်။
- **Update verification**: Updates များကို Bitcoin-Safe ထဲတွင် ပြသပြီး ၎င်းတို့၏ signature ကို အလိုအလျောက် verify လုပ်ပေးသည်။

ဤအစီအမံများအားလုံးကို ပေါင်းစည်းလိုက်သောအခါ Bitcoin-Safe သည် binary security ကို နောက်မှထည့်သည့်အရာမဟုတ်ဘဲ အသုံးပြုသူလုံခြုံရေး၏ အဓိကအစိတ်အပိုင်းအဖြစ် သတ်မှတ်သော စီမံကိန်းအနည်းငယ်ထဲက တစ်ခုဖြစ်လာသည်။

### Bitcoin-Safe ၏ အစိတ်အပိုင်းတိုင်းတွင် လုံခြုံရေးသည် အဓိကဆုံး စဉ်းစားချက်ဖြစ်သည်

Binary integrity အပြင် Bitcoin-Safe သည် secure defaults, ကောင်းမွန်သော operational practices နှင့် ရှင်းလင်းသော user guidance တို့အပေါ် အခြေခံ၍ တည်ဆောက်ထားသည်။ ဥပမာအချို့မှာ:

- **Hardware-first custody**: Bitcoin-Safe သည် [hardware signers]({{< ref "library/supported-hardware-signers" >}}) ကိုလိုအပ်သောကြောင့် seed များသည် dedicated devices များပေါ်တွင်သာ နေပြီး general-purpose computer တစ်လုံးပေါ်ရှိ hot secrets မဖြစ်လာပါ။
- **ပိုမိုလုံခြုံသော setup flow**: Setup wizard သည် အသုံးပြုသူများကို အမှန်တကယ်အသုံးပြုရန် အသင့်ဖြစ်သော wallet များဖန်တီးနိုင်ရန် ကူညီပေးပြီး [hardware signer]({{< ref "library/supported-hardware-signers" >}}) testing, [PDF backup sheets]({{< ref "library/pdf-export/" >}}), hardware signers နှင့် seed backups များကို မည်သို့သိမ်းဆည်းရမည်ဆိုသည့် guidance တို့ပါဝင်သည်။
- **Receive-address verification**: Bitcoin-Safe သည် [receive addresses ကို verify လုပ်ခြင်း]({{< ref "library/verify-receive-address/" >}}) ကို မျှဝေခင် signer ပေါ်မှာပဲ အလွယ်တကူလုပ်နိုင်စေသည်။
- **Address-poisoning detection**: သံသယဖြစ်ဖွယ် [look-alike addresses]({{< ref "library/address-poisoning/" >}}) များအကြောင်း သတိပေးသည်။
- **Multisig security**: Bitcoin-Safe သည် multisignature wallets များကို ပံ့ပိုးပေးသောကြောင့် ပိုမိုကြီးမားသောငွေပမာဏများကို single point of failure တစ်ခုထက် များစွာသော devices သို့မဟုတ် လူများဖြင့် ကာကွယ်နိုင်သည်။
- **Collaboration that makes multisig easier**: Bitcoin-Safe သည် [multisignature collaboration]({{< ref "library/collaboration/" >}}) ကို လက်တွေ့အသုံးဝင်စေသောကြောင့် setup နှင့် signing ကို ညှိနှိုင်းလုပ်ဆောင်ခြင်းသည် တကယ့်အသုံးပြုမှုတွင် ပိုမိုလွယ်ကူလာသည်။
- **Clear signing flows**: Device-specific signing screens များသည် PSBT review အတွင်း ရှုပ်ထွေးမှုကို လျှော့ချပေးပြီး အသုံးပြုသူများကို မှန်ကန်သော signer ပေါ်တွင် မှန်ကန်သော action ကိုလုပ်ဆောင်စေရန် ကူညီပေးသည်။
