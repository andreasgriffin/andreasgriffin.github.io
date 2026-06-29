---
title: "Bitcoin Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "Bitcoin Safe 2.0.0 के रिलीज नोट्स, जिनमें नया सेटअप विज़ार्ड, Compact Block Filters के साथ निजी सिंक और हार्डवेयर वॉलेट्स के लिए विस्तृत सपोर्ट शामिल है।"
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">रिलीज घोषणा</p>
    <h2 class="display-6 mb-3">Bitcoin Safe 2.0 - गाइडेड वॉलेट सेटअप, निजी चेन सिंक, और डिवाइस-केंद्रित साइनिंग</h2>
    <p class="lead mb-4">इस रिलीज में नया सेटअप विज़ार्ड, Compact Block Filters के साथ निजी चेन सिंक, और हर हार्डवेयर डिवाइस के आसपास व्यवस्थित साइनिंग फ्लो शामिल है। अगर आप cold storage को लेकर उत्सुक थे लेकिन अभी तक आश्वस्त नहीं थे, तो यही रिलीज आजमाने लायक है।</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Bitcoin Safe 2.0 डाउनलोड करें</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">नया क्या है देखें</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">स्टेप-बाय-स्टेप वॉलेट सेटअप</h2>
          <p class="mb-0">नया विज़ार्ड हर चरण समझाता है, भ्रम कम करता है, और नए उपयोगकर्ताओं को multisig की ताकत खोए बिना सही रास्ता चुनने में मदद करता है।</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">निजी वॉलेट सिंक</h2>
          <p class="mb-0">नए वॉलेट अब डिफॉल्ट रूप से Compact Block Filters के साथ सिंक होते हैं, ताकि आप किसी third-party Electrum indexer पर निर्भर हुए बिना निजी तौर पर चेन स्कैन कर सकें।</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">डिवाइस-केंद्रित साइनिंग</h2>
          <p class="mb-0">साइनिंग फ्लो अब आपके सामने मौजूद डिवाइस पर केंद्रित रहता है, और QR, USB, Bluetooth, फाइलों तथा multisig coordination के लिए ज्यादा स्पष्ट अगले कदम दिखाता है।</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## Self-custody की ओर एक गाइडेड रास्ता {#setup-flow}

पहले उपयोग का अनुभव पूरी तरह से दोबारा बनाया गया है। Bitcoin Safe अब भी गंभीर self-custody के लिए है, जिसमें hardware-backed multisig भी शामिल है, और 2.0 अब नए उपयोगकर्ताओं को उस सेटअप तक पहुंचने का एक गाइडेड रास्ता देता है। नया विज़ार्ड बताता है कि अभी क्या हो रहा है, आप फ्लो में कहां हैं, और आगे बढ़ने से पहले हर signer को आपसे क्या चाहिए।

<p class="small text-muted">इम्प्लीमेंटेशन की जानकारी के लिए <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a> देखें।</p>

रीडिज़ाइन की मुख्य बातें:

- नया welcome screen, जो पहली बार उपयोग करने वालों को सही शुरुआती रास्ता चुनने में मदद करता है
- वॉलेट बनाने के दौरान step-by-step progress flow
- device-specific signing screens, जिनमें focused instructions और contextual help है
- recovery PDFs जिनमें device names और icons हैं, ताकि backups साफ और बिना भ्रम के रहें

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## Compact Block Filters के साथ निजी और मजबूत चेन सिंक {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) अब Bitcoin Safe 2.0 में नए वॉलेट्स की सिंकिंग को चलाते हैं। Electrum server से यह पूछने के बजाय कि कौन से addresses आपके हैं, Bitcoin Safe अब random Bitcoin Core peers से compact filters डाउनलोड करके और उन्हें locally जांचकर निजी तौर पर चेन स्कैन कर सकता है।

<p class="small text-muted">इम्प्लीमेंटेशन की जानकारी के लिए <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a> देखें।</p>


- वॉलेट सिंक पहली launch से ही निजी रहती है
- third-party Electrum servers पर निर्भरता नहीं
- जिन उपयोगकर्ताओं को पसंद है, उनके लिए Electrum अभी भी उपलब्ध है
- [पहले वॉलेट स्कैन के बाद तुरंत सिंक]({{< ref "library/compact-block-filters" >}})
- [relay की गई transactions की तुरंत notifications]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## हर डिवाइस के लिए डिवाइस-केंद्रित साइनिंग फ्लो {#device-focused-signing}

यह रीडिज़ाइन वॉलेट बनने के बाद के signing flow को भी नया रूप देता है। हर signer के लिए एक generic screen रखने के बजाय, Bitcoin Safe अब actions को उस खास डिवाइस के आसपास रखता है जिसे आप इस समय उपयोग कर रहे हैं।

<p class="small text-muted">इम्प्लीमेंटेशन की जानकारी के लिए <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a> देखें।</p>

- QR, USB, Bluetooth, file export/import, और Sync & Chat actions सीधे active signer card पर दिखते हैं
- बचे हुए signers, पहले से sign कर चुके devices, और अगला जरूरी कदम एक नजर में दिखता है
- mixed-device multisig flows पढ़ने में आसान रहते हैं क्योंकि पूरे PSBT में signer identity साफ दिखाई देती है
- single-sig और multisig inputs के मिश्रण वाली जटिल transactions सही तरीके से संभाली जाती हैं, ताकि हर signing step स्पष्ट रहे

![QR, USB, Bluetooth, file export और Chat & Sync के लिए device-specific actions वाला signer card](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## बिज़नेस workflows और power users के लिए plugin architecture

Bitcoin Safe 2.0 भविष्य में आने वाले अतिरिक्त plugins के लिए भी नींव रखता है, जो Bitcoin businesses और power users के लिए बनाए जाएंगे। इसलिए आगे क्या आने वाला है, उस पर नजर रखें :-)

<p class="small text-muted">इम्प्लीमेंटेशन की जानकारी के लिए <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a> देखें।</p>

- बाहरी *sources* repository के जरिए plugin distribution
- हर plugin को [andreasgriffin]({{< gpg_key_link >}}) द्वारा *GPG signed* किया जाता है, ताकि plugin security, integrity और delivery सुनिश्चित हो
- अलग plugin versioning और updates, तेज और स्वतंत्र plugin development को संभव बनाते हैं

![QR, USB, Bluetooth, file export और Chat & Sync के लिए device-specific actions वाला signer card](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## ज्यादा डिवाइस सपोर्ट और बेहतर polish {#hardware-support}

- तेज स्कैनिंग के लिए animated QR codes **30%** तेज
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) अब USB के जरिए supported है
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) अब USB और QR के अलावा **Bluetooth** भी support करता है
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) और [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) को supported devices की सूची में जोड़ा गया है
- [supported devices की पूरी सूची]({{< ref "library/supported-hardware-signers" >}}) देखें
- [reproducibility]({{< ref "library/reproducibility-and-security" >}}) के लिए automated checks जोड़े गए हैं
- सुधारों की [पूरी सूची](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0) यहां देखें


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## पुरानी ताकतें अब भी मौजूद हैं

2.0 रिलीज कोई reset नहीं है। नए onboarding और signing flow के नीचे, Bitcoin Safe अब भी वे सुविधाएं रखता है जिन्होंने इसे रोजमर्रा में उपयोगी बनाया: collaborative multisig, PDF backups, searchable wallet history, money-flow visualizations, label sync, और बहुत कुछ।

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">Bitcoin Safe 2.0 आजमाने के लिए तैयार हैं?</h2>
  <p class="mb-3">नवीनतम रिलीज डाउनलोड करें और नया onboarding, निजी सिंक और hardware wallet improvements खुद देखें।</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Bitcoin Safe डाउनलोड करें</a>
</div>


<br><br>

## धन्यवाद

यह रिलीज contributors, testers, और [पूरे प्रोजेक्ट के supporters]({{< ref "donate" >}}) के बहुत से काम पर आधारित है:

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r)) को wizard redesign, plugin UI work, और **शानदार और लगातार** UI/UX support के लिए धन्यवाद
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) को Compact Block Filter client के लिए, जो अब नए वॉलेट्स के निजी सिंक को चलाता है
- [Bitcoin Dev Kit टीम](https://github.com/bitcoindevkit/) को, जिनकी libraries Bitcoin Safe के केंद्र में हैं
- [ndk टीम](https://github.com/nostr-dev-kit/ndk) को, जिनकी libraries nostr functionality को चलाती हैं
- Bitcoin Safe समुदाय के सभी लोगों को, जिन्होंने release candidates टेस्ट किए, bugs report किए, pages translate किए, sats भेजे और प्रोजेक्ट को आगे बढ़ाया
- [अनुवादक]({{< ref "donate/#translators" >}}), जिनमें <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (वियतनामी)" title="qdyg-vn 🇻🇳 (वियतनामी)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (जर्मन)" title="bsn21m 🇩🇪 (जर्मन)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (स्पेनिश)" title="cyphra 🇪🇸 (स्पेनिश)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (चीनी)" title="DaGrindDontStop 🇨🇳 (चीनी)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


अगर आप अगली रिलीज को फंड करने में मदद करना चाहते हैं, तो यहां दान कर सकते हैं: {{< donation_btc >}}
