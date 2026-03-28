---
title: "فیلترهای بلوک فشرده"
description: "بفهمید فیلترهای بلوک فشرده چه هستند و چگونه حریم خصوصی را نسبت به سرورهای Electrum بهتر می‌کنند."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "فیلترهای بلوک فشرده"
  - "CBF"
  - "حریم خصوصی"
  - "کیف پول بیت‌کوین"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**فیلترهای بلوک فشرده (CBF)** به [Bitcoin Safe]({{< ref "/" >}}) اجازه می‌دهند بلاک‌چین را بدون پرسیدن از یک سرور Electrum که کدام آدرس‌ها متعلق به شما هستند، اسکن کند.

![Bitcoin Safe فیلترهای بلوک فشرده را از چند peer تصادفی Bitcoin Core دانلود می‌کند.](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

به‌جای پرس‌وجو از یک سرور مرکزی، Bitcoin Safe برای هر بلاک یک فیلتر کوچک را از peerهای تصادفی Bitcoin Core دانلود می‌کند. کیف پول شما آن‌ها را به‌صورت محلی بررسی می‌کند و فقط هنگام نیاز بلاک کامل را دانلود می‌کند.

### CBF در برابر Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">بخش</th>
        <th scope="col">فیلترهای بلوک فشرده</th>
        <th scope="col">سرور Electrum</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">حریم خصوصی</th>
        <td><span class="text-success fw-semibold">خوب</span> - داده‌های کیف پول محلی می‌مانند</td>
        <td><span class="text-danger fw-semibold">بد</span> - سرور می‌تواند آدرس‌ها و تاریخچه شما را ببیند</td>
      </tr>
      <tr>
        <th scope="row">منبع داده</th>
        <td><span class="text-success fw-semibold">خوب</span> - peerهای تصادفی Bitcoin Core</td>
        <td><span class="text-warning fw-semibold">خنثی</span> - یک سرور انتخاب‌شده</td>
      </tr>
      <tr>
        <th scope="row">همگام‌سازی اولیه</th>
        <td><span class="text-warning fw-semibold">خنثی</span> - معمولاً کندتر</td>
        <td><span class="text-success fw-semibold">خوب</span> - معمولاً سریع‌تر</td>
      </tr>
      <tr>
        <th scope="row">همگام‌سازی مداوم</th>
        <td><span class="text-success fw-semibold">خوب</span> - بعد از همگام‌سازی اول بسیار سریع است</td>
        <td><span class="text-success fw-semibold">خوب</span> - معمولاً سریع</td>
      </tr>
      <tr>
        <th scope="row">مناسب برای</th>
        <td><span class="text-success fw-semibold">خوب</span> - کاربرانی که حریم خصوصی برایشان مهم است</td>
        <td><span class="text-success fw-semibold">خوب</span> - سریع‌ترین راه‌اندازی و بازیابی</td>
      </tr>
    </tbody>
  </table>
</div>

### چرا از CBF استفاده کنیم

- حریم خصوصی بهتر: کیف پول شما هیچ‌وقت از سرور درباره آدرس‌هایتان نمی‌پرسد.
- بدون ایندکسر قابل اعتماد: Bitcoin Safe مستقیماً با شبکه Bitcoin صحبت می‌کند.
- همگام‌سازی سبک: فیلترها کوچک هستند، پس به کل بلاک‌چین نیاز ندارید.

### چه انتظاری داشته باشید

- کیف پول جدید یا بازیابی: همگام‌سازی اول معمولاً **5 تا 30 دقیقه** طول می‌کشد.
- کیف پولی که قبلاً همگام شده: معمولاً **خیلی سریع** به‌روز می‌شود، اغلب در **کمتر از 30 ثانیه**.
- تغییر از Electrum به CBF: معمولاً آن هم **کمتر از 30 ثانیه** است.

می‌توانید تعداد peerهایی را که Bitcoin Safe به آن‌ها وصل می‌شود انتخاب کنید. peer بیشتر باعث افزونگی بهتر می‌شود، اما معمولاً پهنای باند و زمان همگام‌سازی را هم افزایش می‌دهد. مقدار پیش‌فرض **2** peer است.

### تراکنش‌های تأییدنشده

CBF فقط **بلاک‌های تأییدشده** را پوشش می‌دهد. برای دریافت هشدار درباره پرداخت‌های ورودی تأییدنشده هم، [Instant transaction notifications]({{< ref "knowledge/instant-transactions-notifications/" >}}) را روشن نگه دارید، چون این تنظیم پیش‌فرض است.

### نکته فنی

فیلترهای بلوک فشرده در [BIP158](https://bips.dev/158/) تعریف شده‌اند. Bitcoin Safe از ماژول متن‌باز [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto) استفاده می‌کند.

همچنین می‌توانید از نود Bitcoin Core خودتان به‌عنوان peer اولیه در تنظیمات _Bitcoin network monitoring_ استفاده کنید.

![تنظیم نود اولیه](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
