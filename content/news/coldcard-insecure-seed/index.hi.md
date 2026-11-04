---
title: "असुरक्षित COLDCARD सीड"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "Coinkite डिवाइस पर बनाए गए सीड से धन स्थानांतरित करने के लिए संक्षिप्त मार्गदर्शन।"
---

[Coinkite ने प्रभावित COLDCARD firmware में सीड बनाने की कमजोरी का खुलासा किया है](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/)। [अनुमान लगाए जा सकने वाले RNG fallback और 32-bit reseed पर Block का तकनीकी विश्लेषण](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware) भी देखें। Firmware अपडेट करने से मौजूदा सीड ठीक नहीं होता।

**अगर आपने किसी भी Coinkite उत्पाद से सीड बनाया है, तो जल्द से जल्द माइग्रेट करें!**

## माइग्रेशन चेकलिस्ट

1. **COLDCARD के अलावा किसी signing device** ([समर्थित devices देखें]({{< ref "library/supported-hardware-signers" >}})) पर एक बिल्कुल नया सीड बनाएँ। पुराने सीड का दोबारा उपयोग न करें। फिर उस signer को Bitcoin-Safe सेटअप विज़ार्ड के साथ इस्तेमाल करके नया [single-signature wallet]({{< ref "library/setup-singlesig-wallet" >}}) या [multisignature wallet]({{< ref "library/setup-multisig-wallet" >}}) बनाएँ।
   - अगर COLDCARD के अलावा कोई hardware signer उपलब्ध नहीं है, तो [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}}) को factory-reset किए गए समर्पित Android device पर इस्तेमाल किया जा सकता है, जिसे offline रखा जाए और केवल signing के लिए उपयोग किया जाए।
   - यह सुनिश्चित करने के लिए कि नया wallet सही तरह से सेट हुआ है, विज़ार्ड का receive-and-send test पूरा करें: backup और नए signer पर receive address सत्यापित करें, थोड़ी परीक्षण राशि प्राप्त करें और उसे नए wallet के किसी दूसरे सत्यापित address पर सफलतापूर्वक self-send करें।
2. माइग्रेशन transaction पर हस्ताक्षर करें:
   - **अगर प्रभावित wallet single-signature है:** जल्दी confirmation के लिए इसे high fee के साथ सामान्य तरीके से broadcast करें।
   - **अगर प्रभावित wallet multisignature है:** इसे सामान्य तरीके से broadcast न करें, क्योंकि ऐसा करने से इसकी public keys public mempool में उजागर हो जाती हैं। हस्ताक्षरित raw transaction को copy करके सीधे [MARA Slipstream](https://slipstream.mara.com/) के माध्यम से submit करें।
3. पुराने COLDCARD को तब तक रखें जब तक पूरी राशि नए wallet में पहुँचकर confirm न हो जाए, फिर उसे नवीनतम firmware पर अपडेट करें।

अगर आप किसी को माइग्रेट करने में मदद कर रहे हैं, तो उनसे कभी भी सीड शब्द साझा करने, उनकी तस्वीर लेने या उन्हें टाइप करने के लिए न कहें। सीड निजी रहना चाहिए और केवल signing device पर दर्ज किया जाना चाहिए।
