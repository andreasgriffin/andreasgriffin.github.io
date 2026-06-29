---
title: "Bitcoin Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "Bitcoin Safe 2.0.0 အတွက် ထုတ်ပြန်ချက် မှတ်စုများ။ ပြန်လည်တည်ဆောက်ထားသော setup wizard၊ Compact Block Filters ဖြင့် ကိုယ်ရေးလုံခြုံသော sync နှင့် hardware wallet များအတွက် ပိုကျယ်ပြန့်သော support ပါဝင်သည်။"
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">ထုတ်ပြန်ချက် ကြေညာချက်</p>
    <h2 class="display-6 mb-3">Bitcoin Safe 2.0 - လမ်းညွှန်ပေးသော wallet setup၊ ကိုယ်ရေးလုံခြုံသော chain sync နှင့် device ကိုဗဟိုပြုသော signing</h2>
    <p class="lead mb-4">ဒီ release မှာ ပြန်လည်တည်ဆောက်ထားတဲ့ setup wizard၊ Compact Block Filters နဲ့ ကိုယ်ရေးလုံခြုံသော chain sync၊ နဲ့ hardware device တစ်ခုချင်းစီကို အခြေခံဖွဲ့စည်းထားတဲ့ signing flow ပါလာပါတယ်။ cold storage ကို စမ်းကြည့်ချင်ပေမယ့် မသေချာသေးရင် ဒီ release က စမ်းသင့်တဲ့ release ပါ။</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Bitcoin Safe 2.0 ကို download လုပ်ရန်</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">ဘာအသစ်လဲ ကြည့်ရန်</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">အဆင့်လိုက် wallet setup</h2>
          <p class="mb-0">wizard အသစ်က အဆင့်တိုင်းကို ရှင်းပြပေးပြီး မရှင်းလင်းမှုကို လျှော့ချပေးသလို multisig ရဲ့ အားသာချက်ကိုမပျောက်စေဘဲ အသုံးပြုသူအသစ်တွေကို မှန်ကန်တဲ့လမ်းကြောင်းရွေးနိုင်အောင် ကူညီပေးပါတယ်။</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">ကိုယ်ရေးလုံခြုံသော wallet sync</h2>
          <p class="mb-0">wallet အသစ်တွေဟာ အခုဆို Compact Block Filters နဲ့ default အနေဖြင့် sync လုပ်ပါတယ်။ ဒါကြောင့် third-party Electrum indexer ကို မမှီခိုဘဲ chain ကို ကိုယ်ရေးလုံခြုံစွာ scan လုပ်နိုင်ပါတယ်။</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">device ကိုဗဟိုပြုသော signing</h2>
          <p class="mb-0">signing flow တွေဟာ အခုဆို သင့်ရှေ့က device ကို ဗဟိုပြုထားပြီး QR, USB, Bluetooth, file, နဲ့ multisig coordination အတွက် နောက်တစ်ဆင့်တွေကို ပိုရှင်းရှင်းလင်းလင်း ပြပါတယ်။</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## self-custody ဆီသို့ လမ်းညွှန်ပေးသောလမ်းကြောင်း {#setup-flow}

ပထမဆုံးအသုံးပြုတဲ့အတွေ့အကြုံကို အစမှပြန်တည်ဆောက်ထားပါတယ်။ Bitcoin Safe က hardware-backed multisig အပါအဝင် အလေးအနက်ထားတဲ့ self-custody ကို ဆက်လက်ဦးတည်ထားပြီး 2.0 ကတော့ အသုံးပြုသူအသစ်တွေကို ဒီ setup ကို နားလည်လွယ်အောင် လမ်းညွှန်ပေးတဲ့လမ်းကြောင်းတစ်ခုပေးပါတယ်။ wizard အသစ်က လက်ရှိဘာတွေဖြစ်နေတယ်၊ flow ရဲ့ ဘယ်အဆင့်မှာရောက်နေတယ်၊ နောက်တစ်ဆင့်မသွားခင် signer တစ်ယောက်ချင်းစီက သင့်ဆီက ဘာလိုအပ်တယ်ဆိုတာ ရှင်းပြပေးပါတယ်။

<p class="small text-muted">အကောင်အထည်ဖော်မှု အသေးစိတ်အတွက် <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a> ကို ကြည့်ပါ။</p>

ဒီ redesign ရဲ့ အဓိကအချက်များ:

- ပထမဆုံးအသုံးပြုသူတွေကို မှန်ကန်တဲ့အစပျိုးကို ရွေးပေးနိုင်အောင် ကူညီပေးတဲ့ welcome screen အသစ်
- wallet ဖန်တီးနေစဉ် အဆင့်လိုက် progress flow
- focused instructions နဲ့ contextual help ပါတဲ့ device-specific signing screens
- backup တွေ မရှုပ်ထွေးအောင် device names နဲ့ icons ပါတဲ့ recovery PDFs

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## Compact Block Filters ဖြင့် ကိုယ်ရေးလုံခြုံပြီး အားကောင်းသော chain sync {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) က အခုဆို Bitcoin Safe 2.0 မှာ wallet အသစ်တွေကို sync လုပ်ပေးတဲ့ အခြေခံစနစ်ဖြစ်လာပါတယ်။ Electrum server ကို ဘယ် address တွေက သင့်ပိုင်လဲလို့ မေးနေစရာမလိုတော့ဘဲ၊ Bitcoin Safe က random Bitcoin Core peers တွေဆီက compact filters တွေကို download လုပ်ပြီး local မှာ စစ်ဆေးခြင်းဖြင့် chain ကို ကိုယ်ရေးလုံခြုံစွာ scan လုပ်နိုင်ပါတယ်။

<p class="small text-muted">အကောင်အထည်ဖော်မှု အသေးစိတ်အတွက် <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a> ကို ကြည့်ပါ။</p>


- wallet sync ဟာ ပထမဆုံး launch ကတည်းက ကိုယ်ရေးလုံခြုံနေပါတယ်
- third-party Electrum servers များကို မမှီခိုရပါ
- Electrum ကို နှစ်သက်သူတွေအတွက်တော့ ဆက်လက်အသုံးပြုနိုင်ပါတယ်
- [ပထမဆုံး wallet scan ပြီးတာနဲ့ ချက်ချင်း sync]({{< ref "library/compact-block-filters" >}})
- [relay လုပ်ထားတဲ့ transactions များအတွက် ချက်ချင်း notifications]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## device တိုင်းအတွက် device ကိုဗဟိုပြုသော signing flow {#device-focused-signing}

ဒီ redesign က wallet ဖန်တီးပြီးနောက် signing flow ကိုလည်း ပြန်လည်ပုံဖော်ထားပါတယ်။ signer အားလုံးအတွက် generic screen တစ်ခုတည်းမဟုတ်တော့ဘဲ၊ Bitcoin Safe က လက်ရှိအသုံးပြုနေတဲ့ သီးသန့် device ကို အခြေခံပြီး actions တွေကို စုစည်းပေးပါတယ်။

<p class="small text-muted">အကောင်အထည်ဖော်မှု အသေးစိတ်အတွက် <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a> ကို ကြည့်ပါ။</p>

- QR, USB, Bluetooth, file export/import, နဲ့ Sync & Chat actions တွေကို active signer card ပေါ်မှာ တိုက်ရိုက်ပြသပါတယ်
- ကျန်ရှိနေတဲ့ signers, လက်မှတ်ထိုးပြီးသား devices, နဲ့ နောက်တစ်ဆင့်လိုအပ်တဲ့ action ကို တစ်ချက်ကြည့်ရုံနဲ့ သိနိုင်ပါတယ်
- mixed-device multisig flows တွေဟာ PSBT တစ်လျှောက် signer identity ကို ဆက်မြင်နိုင်လို့ ဖတ်ရှုရလွယ်ကူနေဆဲပါ
- single-sig နဲ့ multisig inputs ပေါင်းစပ်ထားတဲ့ ရှုပ်ထွေးသော transactions များကို မှန်ကန်စွာကိုင်တွယ်ပေးတဲ့အတွက် signing step တစ်ခုချင်းစီက ရှင်းလင်းနေပါတယ်

![QR, USB, Bluetooth, file export, နဲ့ Chat & Sync အတွက် device-specific actions ပါသော signer card](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## business workflows နှင့် power users အတွက် plugin architecture

Bitcoin Safe 2.0 က Bitcoin businesses နဲ့ power users ကိုရည်ရွယ်တဲ့ နောက်လာမယ့် plugins တွေအတွက်လည်း အခြေခံအုတ်မြစ်ချထားပါတယ်။ ဒါကြောင့် ဘာတွေ ဆက်လာမလဲဆိုတာ စောင့်ကြည့်ထားဖို့ကောင်းပါတယ် :-)

<p class="small text-muted">အကောင်အထည်ဖော်မှု အသေးစိတ်အတွက် <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a> ကို ကြည့်ပါ။</p>

- external *sources* repository ကနေ plugin distribution
- plugin တစ်ခုချင်းစီကို [andreasgriffin]({{< gpg_key_link >}}) က *GPG signed* လုပ်ထားပြီး security, integrity နဲ့ delivery ကို အာမခံပေးပါတယ်
- plugin versioning နဲ့ updates ကို သီးခြားထားတာကြောင့် ပိုမြန်ပြီး လွတ်လပ်တဲ့ plugin development ဖြစ်နိုင်ပါတယ်

![QR, USB, Bluetooth, file export, နဲ့ Chat & Sync အတွက် device-specific actions ပါသော signer card](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## ပိုကျယ်ပြန့်သော device support နှင့် ပိုမို polish ဖြစ်ခြင်း {#hardware-support}

- ပိုမြန်မြန် scan လုပ်နိုင်ဖို့ animated QR codes တွေ **30%** ပိုမြန်လာပါတယ်
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) ကို အခု USB မှတစ်ဆင့် support လုပ်ပါတယ်
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) က USB နဲ့ QR အပြင် **Bluetooth** ကိုလည်း support လုပ်လာပါတယ်
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) နဲ့ [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) ကို support လုပ်ထားတဲ့ devices စာရင်းထဲ ထည့်သွင်းထားပါတယ်
- [support လုပ်ထားတဲ့ devices စာရင်းအပြည့်အစုံ]({{< ref "library/supported-hardware-signers" >}}) ကို ကြည့်ပါ
- [reproducibility]({{< ref "library/reproducibility-and-security" >}}) အတွက် automated checks တွေ ထည့်ထားပါတယ်
- တိုးတက်မှုများ၏ [စာရင်းအပြည့်အစုံ](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0) ကို ဒီမှာကြည့်ပါ


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## ယခင်အားသာချက်များကလည်း အခုထိရှိနေဆဲ

2.0 release က reset မဟုတ်ပါ။ onboarding အသစ်နဲ့ signing flow အသစ်အောက်မှာတောင် Bitcoin Safe က နေ့စဉ်အသုံးဝင်စေတဲ့ feature တွေကို ဆက်လက်ထိန်းသိမ်းထားပါတယ်။ collaborative multisig, PDF backups, searchable wallet history, money-flow visualizations, label sync နဲ့ အခြားအရာများ ပါဝင်ပါတယ်။

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">Bitcoin Safe 2.0 ကို စမ်းသုံးဖို့ အဆင်သင့်ဖြစ်ပြီလား?</h2>
  <p class="mb-3">နောက်ဆုံး release ကို download လုပ်ပြီး onboarding အသစ်၊ ကိုယ်ရေးလုံခြုံသော sync နဲ့ hardware wallet တိုးတက်မှုတွေကို ကိုယ်တိုင်လေ့လာကြည့်ပါ။</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Bitcoin Safe ကို download လုပ်ရန်</a>
</div>


<br><br>

## ကျေးဇူးတင်ပါတယ်

ဒီ release ဟာ contributors, testers, နဲ့ [project တစ်လျှောက်လုံးက supporters]({{< ref "donate" >}}) ရဲ့ ကြိုးစားအားထုတ်မှုအများကြီးပေါ်မှာ တည်ရှိပါတယ်။

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r)) ကို wizard redesign, plugin UI work, နဲ့ **အံ့သြဖွယ်ကောင်းပြီး မနားမနေ** UI/UX support အတွက် ကျေးဇူးတင်ပါတယ်
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) ကို wallet အသစ်တွေကို ကိုယ်ရေးလုံခြုံစွာ sync လုပ်ပေးတဲ့ Compact Block Filter client အတွက် ကျေးဇူးတင်ပါတယ်
- Bitcoin Safe ရဲ့ အခြေခံ libraries တွေအတွက် [Bitcoin Dev Kit team](https://github.com/bitcoindevkit/) ကို ကျေးဇူးတင်ပါတယ်
- nostr functionality ကို မောင်းနှင်ပေးတဲ့ libraries တွေအတွက် [ndk team](https://github.com/nostr-dev-kit/ndk) ကိုလည်း ကျေးဇူးတင်ပါတယ်
- release candidates ကို စမ်းသပ်ခဲ့သူ၊ bugs report လုပ်ခဲ့သူ၊ pages translate လုပ်ခဲ့သူ၊ sats ပို့ခဲ့သူ နဲ့ project ကို ဆက်လက်ရှေ့ဆက်စေခဲ့တဲ့ Bitcoin Safe community မှာရှိသူအားလုံးကို ကျေးဇူးတင်ပါတယ်
- [ဘာသာပြန်သူများ]({{< ref "donate/#translators" >}}) ထဲတွင် <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (ဗီယက်နမ်)" title="qdyg-vn 🇻🇳 (ဗီယက်နမ်)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (ဂျာမန်)" title="bsn21m 🇩🇪 (ဂျာမန်)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (စပိန်)" title="cyphra 🇪🇸 (စပိန်)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (တရုတ်)" title="DaGrindDontStop 🇨🇳 (တရုတ်)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


နောက် release ကို ငွေကြေးထောက်ပံ့ကူညီချင်တယ်ဆိုရင် ဒီနေရာမှာလည်း လှူဒါန်းနိုင်ပါတယ်: {{< donation_btc >}}
