---
title: "कम्पैक्ट ब्लॉक फ़िल्टर"
description: "जानें कि कम्पैक्ट ब्लॉक फ़िल्टर क्या हैं और वे Electrum सर्वरों की तुलना में गोपनीयता कैसे बढ़ाते हैं।"
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "कम्पैक्ट ब्लॉक फ़िल्टर"
  - "CBF"
  - "गोपनीयता"
  - "Bitcoin वॉलेट"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**कम्पैक्ट ब्लॉक फ़िल्टर (CBF)** [Bitcoin Safe]({{< ref "/" >}}) को बिना Electrum सर्वर से यह पूछे कि कौन-से पते आपके हैं, ब्लॉकचेन स्कैन करने देते हैं।

![Bitcoin Safe कई यादृच्छिक Bitcoin Core peer से compact block filters डाउनलोड करता है।](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

केंद्रीय सर्वर से पूछने के बजाय, Bitcoin Safe हर ब्लॉक के लिए छोटे फ़िल्टर यादृच्छिक Bitcoin Core peer से डाउनलोड करता है। आपका वॉलेट इन्हें स्थानीय रूप से जांचता है और केवल ज़रूरत पड़ने पर पूरा ब्लॉक डाउनलोड करता है।

### CBF बनाम Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">पहलू</th>
        <th scope="col">कम्पैक्ट ब्लॉक फ़िल्टर</th>
        <th scope="col">Electrum सर्वर</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">गोपनीयता</th>
        <td><span class="text-success fw-semibold">अच्छा</span> - वॉलेट डेटा स्थानीय रहता है</td>
        <td><span class="text-danger fw-semibold">खराब</span> - सर्वर आपके पते और इतिहास देख सकता है</td>
      </tr>
      <tr>
        <th scope="row">डेटा स्रोत</th>
        <td><span class="text-success fw-semibold">अच्छा</span> - यादृच्छिक Bitcoin Core peer</td>
        <td><span class="text-warning fw-semibold">तटस्थ</span> - एक चुना हुआ सर्वर</td>
      </tr>
      <tr>
        <th scope="row">प्रारंभिक सिंक</th>
        <td><span class="text-warning fw-semibold">तटस्थ</span> - आम तौर पर धीमा</td>
        <td><span class="text-success fw-semibold">अच्छा</span> - आम तौर पर तेज़</td>
      </tr>
      <tr>
        <th scope="row">लगातार सिंक</th>
        <td><span class="text-success fw-semibold">अच्छा</span> - पहले सिंक के बाद बहुत तेज़</td>
        <td><span class="text-success fw-semibold">अच्छा</span> - आम तौर पर तेज़</td>
      </tr>
      <tr>
        <th scope="row">किसके लिए बेहतर</th>
        <td><span class="text-success fw-semibold">अच्छा</span> - गोपनीयता को प्राथमिकता देने वाले उपयोगकर्ता</td>
        <td><span class="text-success fw-semibold">अच्छा</span> - सबसे तेज़ सेटअप और रिकवरी</td>
      </tr>
    </tbody>
  </table>
</div>

### CBF क्यों इस्तेमाल करें

- बेहतर गोपनीयता: आपका वॉलेट कभी सर्वर से आपके पते नहीं पूछता।
- भरोसेमंद इंडेक्सर की जरूरत नहीं: Bitcoin Safe सीधे Bitcoin नेटवर्क से बात करता है।
- हल्का सिंक: फ़िल्टर छोटे हैं, इसलिए पूरे ब्लॉकचेन की जरूरत नहीं।

### क्या अपेक्षा करें

- नया वॉलेट या रिकवरी: पहला सिंक आम तौर पर **5 से 30 मिनट** लेता है।
- पहले से सिंक किया हुआ वॉलेट: आम तौर पर **बहुत तेज़** पकड़ लेता है, अक्सर **30 सेकंड से कम** में।
- Electrum से CBF पर जाना: आम तौर पर वह भी **30 सेकंड से कम** में।

आप चुन सकते हैं कि Bitcoin Safe कितने peer से जुड़े। अधिक peer redundancy बढ़ाते हैं, लेकिन आम तौर पर bandwidth और sync समय भी बढ़ता है। डिफ़ॉल्ट **2** peer हैं।

### अपुष्ट लेनदेन

CBF केवल **confirmed blocks** को कवर करता है। अपुष्ट incoming payments की भी सूचना पाने के लिए [Instant transaction notifications]({{< ref "knowledge/instant-transactions-notifications/" >}}) चालू रखें, यह डिफ़ॉल्ट सेटिंग है।

### तकनीकी नोट

कम्पैक्ट ब्लॉक फ़िल्टर [BIP158](https://bips.dev/158/) में परिभाषित हैं। Bitcoin Safe ओपन-सोर्स [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto) का उपयोग करता है।

आप _Bitcoin network monitoring_ सेटिंग्स में अपने Bitcoin Core node को initial peer के रूप में भी उपयोग कर सकते हैं।

![initial node सेटिंग](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
