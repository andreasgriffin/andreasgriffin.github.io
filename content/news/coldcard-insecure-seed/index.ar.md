---
title: "Seed غير آمنة في COLDCARD"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "إرشادات مختصرة لنقل الأموال من seed تم إنشاؤها على جهاز Coinkite."
---

[كشفت Coinkite عن ضعف في إنشاء seed ضمن إصدارات firmware المتأثرة من COLDCARD](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). راجع أيضًا [التحليل التقني من Block حول fallback المتوقع لمولد RNG وإعادة البذر بطول 32 بت](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware). تحديث firmware لا يصلح seed موجودة بالفعل.

**إذا أنشأت seed باستخدام أي منتج من Coinkite، فانقل أموالك قريبًا!**

## قائمة التحقق من النقل

1. أنشئ seed جديدة تمامًا على **جهاز توقيع غير COLDCARD** ([راجع الأجهزة المدعومة]({{< ref "library/supported-hardware-signers" >}})). لا تعِد استخدام seed القديمة. بعد ذلك، استخدم جهاز التوقيع هذا مع معالج إعداد Bitcoin-Safe لإنشاء [wallet بتوقيع واحد]({{< ref "library/setup-singlesig-wallet" >}}) أو [wallet متعددة التوقيعات]({{< ref "library/setup-multisig-wallet" >}}) جديدة.
   - إذا لم يتوفر أي جهاز توقيع عتادي غير COLDCARD، فيمكن استخدام [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}}) على جهاز Android مخصص تمت إعادته إلى إعدادات المصنع، ويظل غير متصل بالإنترنت ويُستخدم للتوقيع فقط.
   - أكمل اختبار الاستلام والإرسال في المعالج للتأكد من إعداد wallet الجديدة بصورة صحيحة: تحقق من النسخة الاحتياطية وعنوان استلام على جهاز التوقيع الجديد، واستلم مبلغًا تجريبيًا صغيرًا، ثم نفّذ بنجاح إرسالًا ذاتيًا إلى عنوان آخر تم التحقق منه في wallet الجديدة.
2. وقّع معاملة النقل:
   - **إذا كانت wallet المتأثرة بتوقيع واحد:** ابثها بالطريقة المعتادة مع رسوم مرتفعة لكي يتم تأكيدها بسرعة.
   - **إذا كانت wallet المتأثرة متعددة التوقيعات:** لا تبثها بالطريقة المعتادة، لأن ذلك يكشف مفاتيحها العامة في mempool العامة. انسخ المعاملة الخام الموقعة وقدّمها مباشرة عبر [MARA Slipstream](https://slipstream.mara.com/).
3. احتفظ بجهاز COLDCARD القديم حتى يصل الرصيد كاملًا إلى wallet الجديدة ويتم تأكيده، ثم حدّث الجهاز إلى أحدث firmware.

إذا كنت تساعد شخصًا على النقل، فلا تطلب منه مطلقًا مشاركة كلمات seed أو تصويرها أو كتابتها. يجب أن تبقى seed خاصة وألا تُدخل إلا على جهاز التوقيع.
