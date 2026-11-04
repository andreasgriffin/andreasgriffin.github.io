---
title: "မလုံခြုံသော COLDCARD Seed"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "Coinkite device ပေါ်တွင် ဖန်တီးထားသော seed မှ ရန်ပုံငွေများကို ရွှေ့ပြောင်းရန် အကျဉ်းချုပ်လမ်းညွှန်။"
---

[ထိခိုက်နေသော COLDCARD firmware တွင် seed ဖန်တီးမှုအားနည်းချက်ရှိကြောင်း Coinkite က ထုတ်ဖော်ထားသည်](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/)။ [ခန့်မှန်းနိုင်သော RNG fallback နှင့် 32-bit reseed အကြောင်း Block ၏ နည်းပညာဆိုင်ရာ သုံးသပ်ချက်](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware) ကိုလည်း ကြည့်ပါ။ Firmware update လုပ်ခြင်းသည် ရှိပြီးသား seed ကို ပြုပြင်မပေးနိုင်ပါ။

**Coinkite product တစ်ခုခုဖြင့် seed ဖန်တီးခဲ့ပါက မကြာမီ ရွှေ့ပြောင်းပါ!**

## ရွှေ့ပြောင်းမှု စစ်ဆေးရန်စာရင်း

1. **COLDCARD မဟုတ်သော signing device** ([ပံ့ပိုးထားသော devices များကိုကြည့်ပါ]({{< ref "library/supported-hardware-signers" >}})) ပေါ်တွင် seed အသစ်တစ်ခုကို လုံးဝအသစ်ဖန်တီးပါ။ Seed အဟောင်းကို ပြန်မသုံးပါနှင့်။ ထို့နောက် ထို signer ကို Bitcoin-Safe setup wizard နှင့် အသုံးပြုပြီး [single-signature wallet]({{< ref "library/setup-singlesig-wallet" >}}) သို့မဟုတ် [multisignature wallet]({{< ref "library/setup-multisig-wallet" >}}) အသစ်တစ်ခု ဖန်တီးပါ။
   - COLDCARD မဟုတ်သော hardware signer မရှိပါက [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}}) ကို factory reset လုပ်ထားပြီး offline အမြဲထားကာ signing အတွက်သာ အသုံးပြုသော သီးသန့် Android device ပေါ်တွင် အသုံးပြုနိုင်သည်။
   - Wallet အသစ်ကို မှန်ကန်စွာ setup လုပ်ထားကြောင်း သေချာစေရန် wizard ၏ receive-and-send test ကို ပြီးဆုံးအောင်လုပ်ပါ။ Backup နှင့် signer အသစ်ပေါ်ရှိ receive address တစ်ခုကို စစ်ဆေးပါ၊ စမ်းသပ်ရန် ပမာဏအနည်းငယ် လက်ခံပါ၊ ထို့နောက် wallet အသစ်ထဲရှိ စစ်ဆေးပြီးသား အခြား address တစ်ခုသို့ self-send ကို အောင်မြင်စွာ လုပ်ပါ။
2. ရွှေ့ပြောင်းမည့် transaction ကို sign လုပ်ပါ။
   - **ထိခိုက်နေသော wallet သည် single-signature ဖြစ်ပါက:** လျင်မြန်စွာ confirm ဖြစ်စေရန် fee မြင့်မြင့်ဖြင့် ပုံမှန်အတိုင်း broadcast လုပ်ပါ။
   - **ထိခိုက်နေသော wallet သည် multisignature ဖြစ်ပါက:** ပုံမှန်အတိုင်း broadcast မလုပ်ပါနှင့်။ ထိုသို့လုပ်ခြင်းသည် ၎င်း၏ public keys များကို public mempool တွင် ဖော်ပြပေးသည်။ Sign လုပ်ပြီးသော raw transaction ကို copy ကူးပြီး [MARA Slipstream](https://slipstream.mara.com/) မှတစ်ဆင့် တိုက်ရိုက်တင်သွင်းပါ။
3. လက်ကျန်ငွေအားလုံး wallet အသစ်သို့ ရောက်ရှိပြီး confirm ဖြစ်သည်အထိ COLDCARD အဟောင်းကို သိမ်းထားပါ၊ ထို့နောက် နောက်ဆုံး firmware သို့ update လုပ်ပါ။

တစ်စုံတစ်ယောက်ကို ရွှေ့ပြောင်းရန် ကူညီနေပါက သူ၏ seed words များကို မျှဝေရန်၊ ဓာတ်ပုံရိုက်ရန် သို့မဟုတ် စာရိုက်ရန် ဘယ်တော့မှ မတောင်းဆိုပါနှင့်။ Seed သည် လျှို့ဝှက်ထားရမည်ဖြစ်ပြီး signing device ပေါ်တွင်သာ ထည့်သွင်းရမည်။
