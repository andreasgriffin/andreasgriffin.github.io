---
aliases:
  - "/fa/knowledge/hardware-signer-only/"
title: "امضاکننده‌های سخت‌افزاری الزامی"
description: "Bitcoin Safe در Mainnet فقط سیدهای سخت‌افزاری را می‌پذیرد تا امنیت را حداکثر کند و از خطرهای ذخیره‌سازی کلید مبتنی بر نرم‌افزار جلوگیری نماید."
draft: false
bucket: knowledge
tags: ["Featured"]
keywords: [
  "Bitcoin Safe",
  "کیف پول سخت‌افزاری",
  "سید نرم‌افزاری",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "چند‌امضایی",
  "PSBT",
  "خودنگهداری",
  "امنیت بیت‌کوین",
  "تسمم آدرس",
  "ابزارهای بیت‌کوین"
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

## 🚫 چرا Bitcoin Safe سیدهای نرم‌افزاری را در Mainnet مسدود می‌کند؟

🤔 آیا این ناراحت‌کننده نیست؟

🔥 در واقع — این یک ارتقای امنیتی بزرگ است.

Bitcoin Safe **فقط سیدهای نرم‌افزاری را روی Testnet، Signet و Regtest می‌پذیرد** — و هرگز روی Mainnet. دلیلش این است:

### ✅ دلایلی که سیدهای نرم‌افزاری روی Mainnet مسدود شده‌اند

- 🧠 **سیدهای نرم‌افزاری ناامن هستند**
  - کامپیوترها پر از خطرند: رباینده‌ی کلیپ‌بورد، بدافزارها، اکسپلویت‌های مرورگر.
  - یک اشتباه کافی است تا سید شما فاش شود — دیگر کار از کار می‌گذرد.
  - ذخیرهٔ سرد نباید از حالت گرم شروع شود.

</br>

- 🧊 **ذخیرهٔ سرد باید از ابتدا سرد متولد شود**
  - کاربران اغلب سیدها را در کیف‌پول‌های نرم‌افزاری تولید کرده و سپس به سخت‌افزار منتقل می‌کنند.
  - اما قرار گرفتن اولیه در معرض خطر قبلاً رخ داده است — دیگر جبران‌پذیر نیست.
  - ذخیرهٔ سرد واقعی = تولد روی یک امضاکنندهٔ سخت‌افزاری از همان ابتدا.

</br>

- 🎣 **فیشینگ از عادت‌های نرم‌افزاری تغذیه می‌کند**
  - وارد کردن سیدها در برنامه‌ها شما را به اعتماد به الگوهای رابط کاربری بد عادت می‌کند.
  - فقط-سخت‌افزاری عادات بهتری تحمیل می‌کند و میزان قرار گرفتن در معرض خطر را محدود می‌کند.
  - ✅ Mainnet بدون سید نرم‌افزاری = قربانیان فیشینگ کمتر.

</br>

- 🧪 **توسعه‌دهندگان همچنان انعطاف‌پذیری دارند**
  - سیدهای نرم‌افزاری *اجازه داده می‌شوند* روی:
    - Testnet
    - Signet
    - Regtest
  - ایده‌آل برای توسعه‌دهندگان. خطری برای سات‌های واقعی وجود ندارد. 🧡



</br>


- 🔐 **Mainnet امضاکننده‌های سخت‌افزاری می‌خواهد — بدون استثنا**
  - 🔌 USB، 📷 QR، و 💾 کارت SD با تمام دستگاه‌های اصلی
    - [Coldcard]({{< ref "library/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "library/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "library/supported-hardware-signers" >}})
    - [Foundation Passport Core]({{< ref "library/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "library/supported-hardware-signers" >}})
    - [Ledger]({{< ref "library/supported-hardware-signers" >}})
    - [Keystone]({{< ref "library/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "library/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "library/supported-hardware-signers" >}})
  - [مشاهدهٔ همهٔ امضاکنندگان پشتیبانی‌شده →]({{< ref "library/supported-hardware-signers" >}})


---

## 🛡️ محافظت در برابر تسمم آدرس

Bitcoin Safe **آدرس‌های دریافت را با رنگ‌بندی نمایش می‌دهد** تا تسمم آدرس واضح باشد:

- 🟢 سبز = آدرس دریافت تاییدشده  
- 🟡 زرد = آدرس تغییر  

اگر کسی سعی کند کلیپ‌بورد شما را با یک آدرس جعلی آلوده کند، فوراً آن را خواهید دید.

![نمونهٔ تشخیص تسمم آدرس](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ تایید آدرس از طریق USB یا QR

آدرس‌های دریافت را مستقیماً روی امضاکنندهٔ سخت‌افزاری خود تایید کنید — نیازی به اعتماد به صفحهٔ نمایش نیست.

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ دستورالعمل برای هر امضاکنندهٔ سخت‌افزاری
 
- {{<text-name-with-logo>}} شامل راهنماهای تصویری برای هر امضاکنندهٔ سخت‌افزاری است تا شما را در هر مرحله همراهی کند 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-images >}}
    </div>

   
---



## 🤝 ساده‌سازی چند‌امضایی مشارکتی

Bitcoin Safe چند‌امضایی را برای تیم‌ها و استفادهٔ گروهی کاربرپسند می‌کند:

- 🔐 چت رمزنگاری‌شدهٔ Nostr  
- 🔁 اشتراک‌گذاری PSBT با یک کلیک  
- 🔌 USB، 📷 QR، و 💾 کارت SD

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ امکانات قدرتمند برای همه کاربران

- 🟧 جادوگر کیف‌پول تک‌امضایی  
- 🟨 تنظیم چند‌امضایی 2 از 3  
- 🟩 هر پیکربندی n از m  
- 🖨️ برگه‌های پشتیبان قابل چاپ PDF  
- 🔁 همگام‌سازی برچسب‌ها از طریق Nostr  
- 🔍 نمودار کامل جریان پول و تاریخچهٔ تراکنش قابل جستجو

![نمودار تراکنش در Bitcoin Safe](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 جهانی و کاربرپسند

- پشتیبانی چندزبانه: {{< flags-short >}}
- سازگار با: Windows، macOS و Linux  
- کشیدن و رها کردن PSBT / CSV  
- فیلترهای پیشرفته برای تراکنش‌ها، UTXOها، مبالغ و موارد بیشتر

---

## 💡 خلاصه

Bitcoin Safe = پس‌انداز واقعی بیت‌کوین:

✅ فقط سخت‌افزاری در Mainnet  
✅ هیچ قرار گرفتن در معرض سید نرم‌افزاری  
✅ چند‌امضایی مناسب برای مبتدیان  
✅ محیط‌های تست‌پسند برای توسعه‌دهندگان  
✅ امکانات مناسب خانواده و تیم  

🔗 [Bitcoin-Safe.org]({{< ref "/" >}})  
🎥 کانال یوتیوب →: https://youtube.com/@BitcoinSafeOrg