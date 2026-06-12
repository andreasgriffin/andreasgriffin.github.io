---
title: "مطلوب أجهزة توقيع مادية"
description: "تفرض Bitcoin Safe استخدام بذور على أجهزة مادية فقط على الشبكة الرئيسية لتعزيز الأمان وتجنب مخاطر تخزين المفاتيح في برامج. إليك لماذا هذا مهم."
draft: false
tags: ["Featured", "Knowledge" ]
keywords: [
  "Bitcoin Safe",
  "محفظة أجهزة",
  "بذرة برمجية",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "متعدد التواقيع",
  "PSBT",
  "الحفظ الذاتي",
  "أمن البيتكوين",
  "تسميم العناوين",
  "أدوات البيتكوين"
]
images: ["logo.png" ]
# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=dbSmQmt0uDI"
weight: 21
---


![Bitcoin Safe logo](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }

## 🚫 لماذا تمنع Bitcoin Safe البذور البرمجية على الشبكة الرئيسية؟

🤔 ألا يكون ذلك غير مريح؟

🔥 تبين — أنه تحسين أمني كبير.

تسمح Bitcoin Safe **بالبذور البرمجية فقط على Testnet و Signet و Regtest** — ولا تسمح بها أبدًا على الشبكة الرئيسية. إليك السبب:

### ✅ أسباب منع البذور البرمجية على الشبكة الرئيسية

- 🧠 **البذور البرمجية غير آمنة**
  - الحواسيب مليئة بالمخاطر: برامج سرقة الحافظة، البرمجيات الخبيثة، ثغرات المتصفح.
  - زلة واحدة، وتتعرض بذرتك للاختراق — الأمر قد ينتهي بخسارتك لكل شيء.
  - لا يجب أن تبدأ الحفظ البارد بطريقة ساخنة.

</br>

- 🧊 **يجب أن يولد التخزين البارد باردًا**
  - غالبًا ما يُنشئ المستخدمون البذور في محافظ برمجية ثم ينقلونها إلى أجهزة مادية.
  - لكن التعرض الأولي حدث بالفعل — ولا يمكن التراجع عنه.
  - التخزين البارد الحقيقي = إنشاء البذرة على جهاز توقيع مادي من البداية.

</br>

- 🎣 **التصيد يزدهر بسبب العادات البرمجية**
  - إدخال البذور في التطبيقات يعلّمك الثقة بأنماط تجربة مستخدم سيئة.
  - الإلزام بالأجهزة المادية يجبر على عادات أفضل ويقلل التعرض.
  - ✅ بلا بذرة برمجية على الشبكة الرئيسية = عدد أقل من ضحايا التصيد.

</br>

- 🧪 **لا يزال لدى المطورين مرونة**
  - البذور البرمجية *مسموح بها* على:
    - Testnet
    - Signet
    - Regtest
  - مثالية للمطورين. ولا خطر على الساتوشي الحقيقية. 🧡



</br>


- 🔐 **الشبكة الرئيسية تتطلب أجهزة توقيع — بلا استثناءات**
  - 🔌 USB، 📷 QR، و 💾 بطاقة SD مع كل الأجهزة الرئيسية
    - [Coldcard]({{< ref "knowledge/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Foundation Passport Core]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Ledger]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Keystone]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "knowledge/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "knowledge/supported-hardware-signers" >}})
  - [عرض جميع أجهزة التوقيع المدعومة →]({{< ref "knowledge/supported-hardware-signers" >}})


---

## 🛡️ حماية من تسميم العناوين

تقوم Bitcoin Safe **بتلوين عناوين الاستلام** لتجعل تسميم العنوان واضحًا:

- 🟢 أخضر = عنوان استلام مُحقق  
- 🟡 أصفر = عنوان تغيير  

إذا حاول شخص ما تسميم الحافظة (الـ clipboard) بعنوان مزيف، ستراه فورًا.

![مثال على اكتشاف تسميم العنوان](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ التحقق من العنوان عبر USB أو QR

تحقق من عناوين الاستلام مباشرة على جهاز التوقيع المادي — لا حاجة للثقة في شاشة التطبيق.

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ تعليمات لكل جهاز توقيع مادي
 
- {{<text-name-with-logo>}} يتضمن لقطات شاشة وتعليمات لكل جهاز توقيع مادي لتوجيهك خلال كل خطوة 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-images >}}
    </div>

   
---



## 🤝 تسهيل التوقيع المتعدد التعاوني

تجعل Bitcoin Safe التوقيع المتعدد سهل الاستخدام وجاهزًا للعمل الجماعي:

- 🔐 دردشة Nostr مشفّرة  
- 🔁 مشاركة PSBT بنقرة واحدة  
- 🔌 USB، 📷 QR، و 💾 بطاقة SD

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ ميزات قوية لجميع المستخدمين

- 🟧 معالج محفظة أحادية التوقيع  
- 🟨 إعداد توقيع متعدد 2 من 3  
- 🟩 أي تكوين n من m  
- 🖨️ أوراق نسخ احتياطي PDF قابلة للطباعة  
- 🔁 مزامنة العلامات عبر Nostr  
- 🔍 مخطط تدفق الأموال الكامل وسجل معاملات قابل للبحث

![رسم بياني للمعاملات في Bitcoin Safe](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 عالمي وسهل الاستخدام

- دعم متعدد اللغات: {{< flags-short >}}
- يعمل على: Windows و macOS و Linux  
- سحب وإفلات PSBT / CSV  
- مرشحات متقدمة للمعاملات، UTXOs، المبالغ، والمزيد

---

## 💡 ملخص سريع

Bitcoin Safe = مدخرات بيتكوين حقيقية:

✅ أجهزة توقيع فقط على الشبكة الرئيسية  
✅ لا تعريض للبذور البرمجية  
✅ توقيع متعدد سهل للمبتدئين  
✅ بيئات اختبار مناسبة للمطورين  
✅ ميزات مناسبة للعائلة والفريق  

🔗 [Bitcoin-Safe.org]({{< ref "/" >}})  
🎥 قناة YouTube →: https://youtube.com/@BitcoinSafeOrg