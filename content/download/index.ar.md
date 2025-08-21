---
title: "تحميل"
description: "تحميل Bitcoin Safe"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}


✅ **يُنبهك Bitcoin Safe عند توفر إصدار أحدث ويتحقق من الأصالة تلقائيًا.**


ملفات البايناري لنظام Windows موقعة، راجع [سياسة توقيع الكود]({{< ref "code-signing-policy" >}}). انظر هنا أيضًا [سياسة خصوصية Bitcoin Safe]({{< ref "code-signing-policy" >}}). ملفات بايناري macOS غير موقعة، لذا تجاهل رسالة التحذير.

<br>
<br>

###  macOS 

يرجى اتباع الخطوات لتشغيل Bitcoin Safe على macOS:
- انسخه إلى مجلد التطبيقات
- حاول فتحه وستظهر لك رسالة تحذير
- اذهب إلى *إعدادات النظام* --> *الخصوصية والأمان* --> *افتح على أي حال*
- الآن يمكنك فتحه


<img src="/images/mac/copy-app.png" alt="نسخ التطبيق على macOS"   /> 
<img src="/images/mac/warning.png" alt="تحذير على macOS"   /> 
<img src="/images/mac/disable.png" alt="فتح Bitcoin Safe على macOS"   /> 

<br>
<br>

###  التحقق من التوقيع

جميع البرامج موقعة بمفتاحي الخاص. تحقق من أن التنزيل أصلي باتباع الخطوات التالية:

قم باستيراد [المفتاح العام]({{< gpg_key_link >}}) الخاص بي وتحقق من التوقيع باستخدام:
{{< gpg_import_code >}}


<br> 
<br>


<!-- ### Alternative install  via pip  on Mac, Linux, or Windows 
PyPi: https://pypi.org/project/bitcoin-safe/
python -m pip install bitcoin-safe
python -m bitcoin_safe
-->