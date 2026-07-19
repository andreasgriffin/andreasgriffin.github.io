---
aliases:
- /my/knowledge/supported-hardware-signers/metrovault/
title: MetroVault
signer: metrovault
bucket: knowledge
---

MetroVault သည် Android စက်ဟောင်းတစ်လုံးကို Bitcoin-Safe အတွက် သီးသန့် အော့ဖ်လိုင်း Bitcoin လက်မှတ်ရေးထိုးစက်အဖြစ် ပြောင်းလဲပေးနိုင်သည်။ သင်နေ့စဉ်သုံးဖုန်းပေါ်တွင် ၎င်းကို မတင်ပါနှင့်။ ပထမဦးစွာ စက်ကို reset လုပ်ပါ၊ **အော့ဖ်လိုင်း** အနေဖြင့် အင်တာနက်မှ ခွဲထားပါ၊ ထို့နောက် လက်မှတ်ရေးထိုးရန်အတွက်သာ အသုံးပြုပါ။

## မည်သည်များကို မျှော်လင့်ရမည်နည်း

- တင်သွင်းမီ Android စက်ဟောင်းတစ်လုံးကို reset လုပ်ပြီး signer အဖြစ်သာ အသုံးပြုပါ။
- အခြား app များကို မတင်ပါနှင့်၊ account များသို့ sign in မလုပ်ပါနှင့်၊ SIM card မထည့်ပါနှင့်၊ စက်ကို အင်တာနက်သို့ ပြန်မချိတ်ပါနှင့်။
- Wallet data, descriptor များနှင့် PSBT များကို QR code များဖြင့် Bitcoin-Safe နှင့် အပြန်အလှန် ဖလှယ်ပါ။
- Bitcoin-Safe အတွက် multisig descriptor များကို register လုပ်ပြီး signer data ကို export လုပ်ပါ။
- လက်မှတ်မထိုးမီ MetroVault စခရင်ပေါ်ရှိ အသေးစိတ်အားလုံးကို စစ်ဆေးပါ။

## Android စက်ကို reset လုပ်ပြီး အော့ဖ်လိုင်း signer အဖြစ်သာ အသုံးပြုပါ

MetroVault ၏ မူရင်း documentation တွင် ယခု [device setup guide အပြည့်အစုံ](https://github.com/gorunjinian/MetroVault/blob/main/docs/DEVICE_SETUP.md) ရှိသည်။ ထို guide ကို အဆင့်လိုက် တိတိကျကျလိုက်နာရန်နှင့် မဖြစ်မနေလိုအပ်ချက်အဖြစ် ယူဆရန် အပြင်းအထန် အကြံပြုပါသည်: factory reset လုပ်ထားပြီး setup ပြီးနောက်လည်း အင်တာနက်မှ ခွဲထားသည့် သီးသန့် **အော့ဖ်လိုင်းဖုန်း** ကို အသုံးပြုပြီး လက်မှတ်ရေးထိုးရန်အတွက်သာ သုံးပါ။

1. တင်သွင်းမီ ဖုန်းကို factory reset လုပ်ပါ။
2. Google account setup ကို ကျော်ပြီး စက်ကို offline ထားပါ။
3. Airplane mode ကို အမြဲဖွင့်ထားပါ။
4. Wi-Fi, Bluetooth, NFC နှင့် mobile data ကို ပိတ်ပါ။
5. SIM card ကို ဖယ်ရှားပါ။
6. USB debugging ကို ပိတ်ပါ။
7. အခြား app များကို မတင်ပါနှင့်၊ လက်မှတ်ရေးထိုးခြင်းမှအပ အခြားမည်သည့်အရာအတွက်မျှ ဖုန်းကို မသုံးပါနှင့်။

Production အသုံးပြုမှုအတွက် ဖြစ်နိုင်သမျှ source code မှ build လုပ်ပါ။ စက်ကို offline နှင့် signer-only အနေဖြင့် မထိန်းထားနိုင်ပါက MetroVault ၏ production funds အတွက် မသုံးပါနှင့်။
