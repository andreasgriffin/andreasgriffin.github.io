---
title: "ဟာ့ဒ်ဝဲ လက်မှတ်ထိုးသူများသာ လိုအပ်သည်"
description: "Bitcoin Safe သည် Mainnet ပေါ်တွင် ဟာ့ဒ်ဝဲမှ ထုတ်ပေးထားသော seed များကိုပဲ ချမှတ်ထားခြင်းဖြင့် လုံခြုံရေးကို အမြင့်ဆုံးထားပြီး ဆော့ဖ်ဝဲအခြေပြု key သိမ်းဆည်းမှု၏ အန္တရာယ်များကို ရှောင်ရှားစေသည်။ အကြောင်းရင်းများကို ဒီမှာ ဖော်ပြထားသည်။"
draft: false
tags: ["Featured", "Knowledge" ]
keywords: [
  "Bitcoin Safe",
  "ဟာ့ဒ်ဝဲ ဝေါလက်",
  "ဆော့ဖ်ဝဲ စီဒ်",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "multisig",
  "PSBT",
  "ကိုယ်ပိုင် ထိန်းသိမ်းမှု",
  "Bitcoin လုံခြုံရေး",
  "လိပ်စာ အဆိပ်ပေးခြင်း",
  "Bitcoin ကိရိယာများ"
]
images: ["logo.png" ]
# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=dbSmQmt0uDI"
weight: 21
---

 

![](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }

## 🚫 ဘာကြောင့် Bitcoin Safe က Mainnet ပေါ်မှာ ဆော့ဖ်ဝဲ စီဒ်ကို ပိတ်ထားတာလဲ?

🤔 အဆင်မပြေတာ မဟုတ်လား?

🔥 တကယ်တော့ — ဤနည်းဟာ **လုံခြုံရေး သာမန်တိုးတက်မှု လေးတစ်ခု** ဖြစ်ပါတယ်။

Bitcoin Safe သည် **Testnet, Signet, နှင့် Regtest တွင်သာ ဆော့ဖ်ဝဲ စီဒ် အသုံးပြုခွင့်ရှိစေပြီး Mainnet ပေါ်တွင် ဆော့ဖ်ဝဲ စီဒ်ကို မခွင့်ပြုပါ** — အကြောင်းအရင်းတွေက ဒီအတိုင်းပါ။

### ✅ Mainnet ပေါ်မှာ ဆော့ဖ်ဝဲ စီဒ်ကို ပိတ်ထားရတဲ့ အကြောင်းရင်းများ

- 🧠 **ဆော့ဖ်ဝဲ စီဒ်များမှာ လုံခြုံမှုမရှိပါ**
  - ကွန်ပျူတာတွေမှာ clipboard hijacker, malware, browser exploit စတာတွေ များပြားပါတယ်။
  - အမှားတစ်ချက်နဲ့ သင့် seed တစ်ခုလုံး လျှပ်တစ်လျှာ ဖောက်ထွင်းခံရနိုင်ပါတယ် — အကုန်ဆုံးပါပဲ။
  - Cold storage ကို ဘာမှမရှိခင်တွင် hot အခြေအနေမှာ စတင်မလုပ်သင့်ပါ။

</br>

- 🧊 **Cold storage ကို အစပျိုးချင်းမှ လည်း သန့်ရှင်းစေဖို့လိုသည်**
  - အသုံးပြုသူများသည် မကြာခဏ ဆော့ဖ်ဝဲ wallet မှာ seed ထုတ်ပြီးနောက် hardware သို့ ရွှေ့ဆိုင်းကြသည်။
  - ဒါပေမယ့် အစပိုင်း exposure ဟာ ဖြစ်ပြီးသားဖြစ်နေသဖြင့် ပြန်လည်မနေပဲဖြစ်သွားပါပြီ။
  - အမှန်တကယ်သော cold storage ဆိုတာ = အစပျိုးချင်းမှ hardware signer ပေါ်မှာဖန်တီးထားရပါတယ်။

</br>

- 🎣 **Phishing များက ဆော့ဖ်ဝဲ အလေ့အကျင့်များကို အလွယ်တကူအသက်သွင်းနိုင်သည်**
  - seed များကို apps ထဲသို့ရိုက်ထည့်ပေးရတာက မကောင်းတဲ့ UX စနစ်များကို ယုံကြည်စေပါတယ်။
  - hardware-only က အလေ့အကျင့်ကောင်းများကို အားပေးပြီး exposure ကို လျှော့ချနိုင်ပါတယ်။
  - ✅ Mainnet ပေါ်မှာ seed မရှိခြင်း = phishing ထိခိုက်သူ နည်းလာခြင်း။

</br>

- 🧪 **ဒီဗလို့ပ်တွေကို အမြဲ flexibility ပေးထားတယ်**
  - ဆော့ဖ်ဝဲ စီဒ်များကို **ခွင့်ပြုထားသည်**:
    - Testnet
    - Signet
    - Regtest
  - ဒီတွေက developer များအတွက် အကောင်းဆုံးဖြစ်ပြီး จริงစက်ကာဒဲ့ဒေါ်လာများမှု မရှိပါ။ 🧡



</br>


- 🔐 **Mainnet အတွက်တော့ ဟာ့ဒ်ဝဲ လက်မှတ်ထိုးသူများသာ — အထူးခံရမှမဟုတ်**
  - 🔌 USB, 📷 QR, နှင့် 💾 SD ကဒ်အားလုံးကို မူလထိပ်တန်း စက်ပစ္စည်းများက ထောက်ပံ့ပါသည်
    - [Coldcard]({{< ref "knowledge/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Foundation Passport]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Ledger]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Keystone]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "knowledge/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "knowledge/supported-hardware-signers" >}})
  - [ပံ့ပိုးထားသော လက်မှတ်ထိုးသူ အားလုံးကို ကြည့်ရန် →]({{< ref "knowledge/supported-hardware-signers" >}})


---

## 🛡️ လိပ်စာ အဆိပ်ပေးခြင်းမှ ကာကွယ်မှု

Bitcoin Safe သည် လိပ်စာ အဆိပ်ပေးခြင်းကို တွေ့ရန် အဆင်ပြေစေရန် လက်ခံလိပ်စာများကို အရောင်အလိုက် အမှတ်အသား ချထားပါသည်။

- 🟢 အစိမ်း = အတည်ပြုထားသော လက်ခံလိပ်စာ  
- 🟡 အဝါ = ပြောင်းလဲလိပ်စာ  

သူများက သင့် clipboard ကိုလိပ်စာနံပါတ်တွေနဲ့ မဟုတ်သော လိပ်စာဖြင့် အဆိပ်ပေးကြည့်ဖြစ်ချင်လျင် သင်သည် ထိန်းချုပ်ချက်ကို တစ်ချက်ပဲမြင်နိုင်ပါလိမ့်မည်။

![လိပ်စာ အဆိပ်ပေးခြင်းကို တွေ့မြင်နိုင်သည့် နမူနာ](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ USB သို့မဟုတ် QR ဖြင့် လိပ်စာ အတည်ပြုခြင်း

လက်ခံလိပ်စာများကို တိုက်ရိုက် သင့် ဟာ့ဒ်ဝဲ လက်မှတ်ထိုးသူပေါ်တွင် အတည်ပြုပါ — screen ကို ယုံကြည်ရန် မလိုအပ်ပါ။

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ လက်မှတ်ထိုးသူ အလိုက် လမ်းညွှန်ချက်များ
 
- {{<text-name-with-logo>}} တွင် လူကြီးမင်းကို လက်မှတ်ထိုးသူ တစ်ခုချင်းစီအတွက် အဆင့်ဆင့် screenshot လမ်းညွှန်ချက်များကို ပေးထားသည် 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-hardware-signer-screenshots >}}
    </div>

   
---



## 🤝 အဖော်ယုတ် Multisig ကို အလွယ်တကူ ပြုလုပ်နိုင်သည်

Bitcoin Safe သည် multisig ကို အသုံးသူ လက်လှမ်းမီ၍ အဖွဲ့လိုက် အသုံးပြုနိုင်အောင် လွယ်ကူစေသည်။

- 🔐 အင်းခရစ်ထားသော Nostr chat  
- 🔁 ၁-ချက် PSBT ဝေမျှမှု  
- 🔌 USB, 📷 QR, နှင့် 💾 SD ကဒ်

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ အသုံးပြုသူအားလုံးအတွက် အင်အားကြီးသော လက္ခဏာများ

- 🟧 Singlesig wallet များအတွက် ဗစ်ဇာတ်လမ်းအကူအညီ  
- 🟨 2-of-3 multisig စနစ် စတင်ခြင်း  
- 🟩 မည်သည့် n-of-m အပြင်အဆင်မျှ လက်ခံနိုင်မှု  
- 🖨️ မိမိကြိုက် Printable PDF backup sheet များ  
- 🔁 Nostr ဖြင့် label အချက်အလက် đồngစင် ချိန့်လုပ်မှု  
- 🔍 လုံးဝ ငွေကြေးလည်ပတ်မှု ဇယားနှင့် ရှာဖွေရေးရမည့် အမှုအရာများပါသော transaction မှတ်တမ်း

![Transaction diagram in Bitcoin Safe](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 ကမ္ဘာလုံးဆိုင်ရာနှင့် လူမည်းလက်လှမ်းမီ

- ဘာသာစကားစုံ အထောက်အပံ့: {{< flags-short >}}
- အလုပ်လုပ်နိုင်သောစနစ်များ: Windows, macOS & Linux  
- Drag-and-drop PSBT / CSV  
- transaction, UTXO, ပမာဏများနှင့် အခြား filter အဆင့်မြင့်များ

---

## 💡 အကျဉ်းချုပ်

Bitcoin Safe = အမှန်တကယ်သော Bitcoin စုဆောင်းမှု:

✅ Mainnet တွင် ဟာ့ဒ်ဝဲပဲသာ အသုံးပြုနိုင်  
✅ ဆော့ဖ်ဝဲ seed exposure မရှိခြင်း  
✅ စတင်သူများအတွက် မူလတည်းက အဆင်ပြေသော multisig  
✅ developer များအတြက္ စမ်းသပ်ရန် သက်သာသော ပတ်ဝန်းကျင်များ  
✅ မိသားစုနှင့် အဖွဲ့လိုက် အသုံးပြုရန် အသင့်တော်သော လက္ခဏာများ  

🔗 [Bitcoin-Safe.org]({{< ref "/" >}})  
🎥 YouTube ချန်နယ် →: https://youtube.com/@BitcoinSafeOrg