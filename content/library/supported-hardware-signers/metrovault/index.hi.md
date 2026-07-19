---
aliases:
- /hi/knowledge/supported-hardware-signers/metrovault/
title: MetroVault
signer: metrovault
bucket: knowledge
---

MetroVault किसी पुराने Android डिवाइस को Bitcoin-Safe के लिए एक समर्पित ऑफलाइन Bitcoin signing device में बदल सकता है। इसे अपने रोजमर्रा वाले फोन पर इंस्टॉल न करें। पहले डिवाइस को reset करें, उसे **ऑफलाइन** और इंटरनेट से अलग रखें, और उसका उपयोग केवल signing के लिए करें।

## क्या अपेक्षा करें

- इंस्टॉलेशन से पहले पुराने Android डिवाइस को reset करें और उसे केवल signer की तरह इस्तेमाल करें।
- कोई दूसरी ऐप इंस्टॉल न करें, किसी खाते में sign in न करें, SIM card न डालें, और डिवाइस को फिर से इंटरनेट से न जोड़ें।
- Wallet data, descriptors और PSBT को QR codes के जरिए Bitcoin-Safe के साथ आदान-प्रदान करें।
- Bitcoin-Safe के लिए multisig descriptors register करें और signer data export करें।
- Sign करने से पहले MetroVault की स्क्रीन पर सभी विवरण जांचें।

## Android डिवाइस reset करें और उसे केवल ऑफलाइन signer की तरह इस्तेमाल करें

MetroVault के upstream documentation में अब एक comprehensive [device setup guide](https://github.com/gorunjinian/MetroVault/blob/main/docs/DEVICE_SETUP.md) दिया गया है। हम जोरदार सिफारिश करते हैं कि इसे step by step follow करें और एक अनिवार्य requirement की तरह मानें: ऐसा dedicated, factory-reset **ऑफलाइन फोन** इस्तेमाल करें जो setup के बाद भी इंटरनेट से disconnected रहे और केवल signing के लिए इस्तेमाल हो।

1. इंस्टॉलेशन से पहले फोन को factory reset करें।
2. Google account setup को skip करें और डिवाइस को offline रखें।
3. Airplane mode को हमेशा enabled रखें।
4. Wi-Fi, Bluetooth, NFC और mobile data को disable करें।
5. SIM card निकाल दें।
6. USB debugging को disable करें।
7. दूसरी ऐप्स इंस्टॉल न करें और फोन का इस्तेमाल signing के अलावा किसी और काम के लिए न करें।

Production उपयोग के लिए, जब संभव हो source code से build करें। अगर आप डिवाइस को offline और signer-only नहीं रख सकते, तो MetroVault production funds के लिए इसका उपयोग न करें।
