---
title: "مرشحات الكتل المدمجة"
description: "تعرّف على ما هي مرشحات الكتل المدمجة وكيف تحسن الخصوصية مقارنة بخوادم Electrum."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "مرشحات الكتل المدمجة"
  - "CBF"
  - "الخصوصية"
  - "محفظة بيتكوين"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**مرشحات الكتل المدمجة (CBF)** تُمكّن [Bitcoin Safe]({{< ref "/" >}}) من فحص سلسلة الكتل دون سؤال خادم Electrum عن العناوين التي تخصك.

![يقوم Bitcoin Safe بتنزيل مرشحات الكتل المدمجة من عدة أقران عشوائيين لـ Bitcoin Core.](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

بدلاً من الاستعلام من خادم مركزي، يحمّل Bitcoin Safe مرشحًا صغيرًا لكل كتلة من أقران Bitcoin Core عشوائيين. تتحقق محفظتك منها محليًا وتحمّل الكتل الكاملة فقط عند الحاجة.

### CBF مقابل Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">البند</th>
        <th scope="col">مرشحات الكتل المدمجة</th>
        <th scope="col">خادم Electrum</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">الخصوصية</th>
        <td><span class="text-success fw-semibold">جيد</span> - تبقى بيانات المحفظة محليًا</td>
        <td><span class="text-danger fw-semibold">سيئ</span> - يمكن للخادم رؤية عناوينك وسجلّك</td>
      </tr>
      <tr>
        <th scope="row">مصدر البيانات</th>
        <td><span class="text-success fw-semibold">جيد</span> - أقران Bitcoin Core عشوائيون</td>
        <td><span class="text-warning fw-semibold">محايد</span> - خادم واحد تختاره</td>
      </tr>
      <tr>
        <th scope="row">المزامنة الأولى</th>
        <td><span class="text-warning fw-semibold">محايد</span> - عادة أبطأ</td>
        <td><span class="text-success fw-semibold">جيد</span> - عادة أسرع</td>
      </tr>
      <tr>
        <th scope="row">المزامنة المستمرة</th>
        <td><span class="text-success fw-semibold">جيد</span> - سريعة جدًا بعد المزامنة الأولى</td>
        <td><span class="text-success fw-semibold">جيد</span> - عادة سريعة</td>
      </tr>
      <tr>
        <th scope="row">مناسب لـ</th>
        <td><span class="text-success fw-semibold">جيد</span> - المستخدمين المهتمين بالخصوصية</td>
        <td><span class="text-success fw-semibold">جيد</span> - أسرع إعداد واستعادة</td>
      </tr>
    </tbody>
  </table>
</div>

### لماذا تستخدم CBF

- خصوصية أفضل: محفظتك لا تسأل خادمًا أبدًا عن عناوينك.
- بدون فهرس موثوق: يتواصل Bitcoin Safe مباشرة مع شبكة Bitcoin.
- مزامنة خفيفة: المرشحات صغيرة، لذلك لا تحتاج إلى سلسلة الكتل كاملة.

### ما الذي تتوقعه

- محفظة جديدة أو استعادة: عادة **5 إلى 30 دقيقة** للمزامنة الأولى.
- محفظة متزامنة بالفعل: عادة تلحق **بسرعة كبيرة**، وغالبًا في **أقل من 30 ثانية**.
- الانتقال من Electrum إلى CBF: عادة أيضًا **أقل من 30 ثانية**.

يمكنك اختيار عدد الأقران الذين يتصل بهم Bitcoin Safe. كلما زاد العدد تحسنت الموثوقية، لكن ذلك يزيد عادة عرض النطاق وزمن المزامنة. القيمة الافتراضية هي **2** من الأقران.

### المعاملات غير المؤكدة

يغطي CBF فقط **الكتل المؤكدة**. وللحصول أيضًا على تنبيهات بشأن المدفوعات الواردة غير المؤكدة، اترك [Instant transaction notifications]({{< ref "knowledge/instant-transactions-notifications/" >}}) مفعلة، فهذا هو الإعداد الافتراضي.

### ملاحظة تقنية

تم تعريف مرشحات الكتل المدمجة في [BIP158](https://bips.dev/158/). يستخدم Bitcoin Safe وحدة مفتوحة المصدر [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto).

يمكنك أيضًا استخدام عقدة Bitcoin Core الخاصة بك كقرين ابتدائي في إعدادات _Bitcoin network monitoring_.

![إعداد العقدة الابتدائية](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
