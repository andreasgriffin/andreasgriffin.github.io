---
title: "कोड साइनिंग नीति और Bitcoin Safe गोपनीयता नीति"
description: "कोड साइनिंग नीति"
draft: false
tags: ["legal"]
menu:
  footer:
    weight: 90
---


## कोड साइनिंग नीति


Free code signing provided by [SignPath.io](https://about.signpath.io/), certificate by [SignPath Foundation](https://signpath.org/)


## गोपनीयता नीति
यह प्रोग्राम डिफ़ॉल्ट रूप से निम्न का उपयोग करता है
- ब्लॉकचेन डेटा प्राप्त करने के लिए [blockstream.com](https://blockstream.com/) के electrum/esplora सर्वर
- [mempool.space](https://mempool.space/) से mempool शुल्क की जानकारी प्राप्त करता है

आप "नेटवर्क सेटिंग्स" में दोनों के लिए अपना (व्यक्तिगत) सर्वर निर्दिष्ट कर सकते हैं।

जब आप "सिंक और चैट" सुविधा सक्षम करते हैं तो आपके अनुमोदित भरोसेमंद उपकरणों को एन्क्रिप्ट किया गया डेटा भेजने के लिए [डिफ़ॉल्ट रिले](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py) उपयोग किए जाते हैं। आप "सिंक और चैट सेटिंग्स" में अपने स्वयं के रिले(ओं) को निर्दिष्ट कर सकते हैं।

यह प्रोग्राम किसी अन्य नेटवर्केड सिस्टम को कोई अन्य जानकारी स्थानांतरित नहीं करेगा, जब तक कि उपयोगकर्ता या इसे स्थापित या संचालित करने वाला व्यक्ति विशेष रूप से अनुरोध न करे।