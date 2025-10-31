---
title: "دانلود"
description: "دانلود Bitcoin Safe"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}


✅ **Bitcoin Safe شما را از نسخهٔ جدیدتر مطلع می‌کند و اصالت را به‌صورت خودکار تأیید می‌کند.**


فایل‌های باینری ویندوز امضا شده‌اند، [سیاست امضای کد]({{< ref "code-signing-policy" >}}) را بررسی کنید. همچنین [سیاست حفظ حریم خصوصی Bitcoin Safe]({{< ref "code-signing-policy" >}}) را ببینید. فایل‌های باینری macOS امضا نشده‌اند، بنابراین لطفاً پیام هشدار را نادیده بگیرید.

<br>
<br>

###  macOS 

لطفاً برای اجرای Bitcoin Safe روی macOS مراحل زیر را دنبال کنید:
- آن را در پوشهٔ Applications (پوشهٔ برنامه‌ها) خود کپی کنید
- برای باز کردن آن تلاش کنید؛ یک هشدار دریافت خواهید کرد
- به *تنظیمات سیستم* --> *حریم خصوصی و امنیت* --> *باز کردن به هر حال* بروید
- اکنون می‌توانید آن را باز کنید


<img src="/images/mac/copy-app.png" alt="کپی برنامه در macOS"   /> 
<img src="/images/mac/warning.png" alt="هشدار macOS"   /> 
<img src="/images/mac/disable.png" alt="باز کردن Bitcoin Safe در macOS"   /> 

<br>
<br>

###  تأیید امضا

تمام نرم‌افزارها با کلید خصوصی من امضا شده‌اند. برای بررسی اینکه دانلود اصالت دارد، مراحل زیر را دنبال کنید:

کلید عمومی من را وارد کنید: [کلید عمومی]({{< gpg_key_link >}}) و امضا را با دستور زیر بررسی کنید:
```bash
{{< gpg_import_code >}}
```



<br> 
<br>


<!-- ### Alternative install  via pip  on Mac, Linux, or Windows 
PyPi: https://pypi.org/project/bitcoin-safe/
python -m pip install bitcoin-safe
python -m bitcoin_safe
-->