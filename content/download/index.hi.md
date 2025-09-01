---
title: "डाउनलोड"
description: "Bitcoin Safe डाउनलोड करें"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}


✅ **Bitcoin Safe आपको नई रिलीज़ के बारे में सूचित करता है और स्वचालित रूप से प्रामाणिकता सत्यापित करता है।**


Windows binary files are signed, check the [कोड साइनिंग नीति]({{< ref "code-signing-policy" >}}). See here the   [Bitcoin Safe गोपनीयता नीति]({{< ref "code-signing-policy" >}}).  The  MacOS binaries are not signed, so please disregard the warning message.

<br>
<br>

###  macOS 

Please follow the steps to run Bitcoin Safe on macOS:
- इसे अपने ऐप फ़ोल्डर में कॉपी करें
- इसे खोलने का प्रयास करें — आपको एक चेतावनी मिलेगी
- *सिस्टम सेटिंग्स* --> *गोपनीयता और सुरक्षा* --> *फिर भी खोलें*
- अब आप इसे खोल सकते हैं


<img src="/images/mac/copy-app.png" alt="macOS ऐप को कॉपी करें"   /> 
<img src="/images/mac/warning.png" alt="macOS चेतावनी"   /> 
<img src="/images/mac/disable.png" alt="macOS Bitcoin Safe खोलें"   /> 

<br>
<br>

###  सत्यापन करें (Verify signature)

सभी सॉफ़्टवेयर मेरी निजी कुंजी से साइन किए गए हैं। डाउनलोड की प्रामाणिकता सत्यापित करने के लिए निम्न चरणों का पालन करें:

मेरी [सार्वजनिक कुंजी]({{< gpg_key_link >}}) आयात करें और हस्ताक्षर को निम्न के साथ सत्यापित करें:
{{< gpg_import_code >}}


<br> 
<br>


<!-- ### Alternative install  via pip  on Mac, Linux, or Windows 
PyPi: https://pypi.org/project/bitcoin-safe/
python -m pip install bitcoin-safe
python -m bitcoin_safe
-->