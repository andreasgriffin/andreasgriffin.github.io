---
title: "Bitcoin Safe 1.8.0"
date: "2026-03-31"
description: "Bitcoin Safe 1.8.0 के रिलीज़ नोट्स, जिनमें बैलेंस चार्ट ज़ूम, कस्टम nLocktime, ऐप लॉक मोड और आसान अपडेट शामिल हैं।"
videos:
  - "https://www.youtube.com/watch?v=S0O40-p_w0M"
---

## नई सुविधाएं

#### बैलेंस चार्ट ज़ूम

बैलेंस चार्ट के लिए ज़ूम जोड़ा गया ([#492](https://github.com/andreasgriffin/bitcoin-safe/pull/492)).

{{< video src="zoom.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 बैलेंस चार्ट ज़ूम" description="Bitcoin Safe 1.8.0 में बैलेंस चार्ट ज़ूम का पूर्वावलोकन।" >}}

#### कस्टम nLocktime

कस्टम nLocktime का समर्थन जोड़ा गया, जिससे आप वह शुरुआती ब्लॉक हाइट या समय तय कर सकते हैं जब कोई ट्रांज़ैक्शन पुष्टि की जा सकती है ([#481](https://github.com/andreasgriffin/bitcoin-safe/pull/481)).

{{< video src="nLocktime.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 कस्टम nLocktime" description="Bitcoin Safe 1.8.0 में कस्टम nLocktime समर्थन का पूर्वावलोकन।" >}}

#### Jade के लिए Bluetooth समर्थन

Jade के लिए Bluetooth समर्थन जोड़ा गया ([#517](https://github.com/andreasgriffin/bitcoin-safe/pull/517)).

{{< video src="bluetooth.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 Jade के लिए Bluetooth समर्थन" description="Bitcoin Safe 1.8.0 में Jade के लिए Bluetooth समर्थन का पूर्वावलोकन।" >}}

#### ऐप लॉक मोड

ऐप लॉक मोड जोड़ा गया, जो ऐप को बैकग्राउंड में चलते हुए लॉक करने का एक तरीका है ([#519](https://github.com/andreasgriffin/bitcoin-safe/pull/519)).

{{< video src="app-lock.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 ऐप लॉक मोड" description="Bitcoin Safe 1.8.0 में ऐप लॉक मोड का पूर्वावलोकन।" >}}

इसके साथ Windows पर seamless update functionality और macOS व Linux पर आसान अपडेट भी शामिल हैं ([#513](https://github.com/andreasgriffin/bitcoin-safe/pull/513)).

## सुधार

- नोटिफिकेशन हिस्ट्री अब tray icon से उपलब्ध है ([#493](https://github.com/andreasgriffin/bitcoin-safe/pull/493))
- बग फिक्स और छोटे UI सुधार

## योगदान

- [@bsn21m](https://github.com/bsn21m) ने [#538](https://github.com/andreasgriffin/bitcoin-safe/pull/538) में अपना पहला योगदान दिया
- [bdk](https://github.com/bitcoindevkit/) टीम और [@rustaceanrob](https://github.com/rustaceanrob) को धन्यवाद
- डिजाइन और UX समर्थन के लिए [@design-rrr](https://github.com/design-rrr) को बहुत धन्यवाद
