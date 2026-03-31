---
title: "Bitcoin Safe 1.8.0"
date: "2026-03-31"
description: "ملاحظات إصدار Bitcoin Safe 1.8.0، بما في ذلك تكبير مخطط الرصيد وميزة nLocktime المخصصة ووضع قفل التطبيق وتحديثات أسهل."
videos:
  - "https://www.youtube.com/watch?v=S0O40-p_w0M"
---

## الميزات الجديدة

#### تكبير مخطط الرصيد

تمت إضافة إمكانية تكبير مخطط الرصيد ([#492](https://github.com/andreasgriffin/bitcoin-safe/pull/492)).

{{< video src="zoom.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 تكبير مخطط الرصيد" description="معاينة لميزة تكبير مخطط الرصيد في Bitcoin Safe 1.8.0." >}}

#### nLocktime مخصص

تمت إضافة دعم nLocktime المخصص، والذي يتيح لك تحديد أول ارتفاع كتلة أو وقت يمكن عنده تأكيد المعاملة ([#481](https://github.com/andreasgriffin/bitcoin-safe/pull/481)).

{{< video src="nLocktime.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 nLocktime مخصص" description="معاينة لدعم nLocktime المخصص في Bitcoin Safe 1.8.0." >}}

#### دعم Bluetooth لـ Jade

تمت إضافة دعم Bluetooth لجهاز Jade ([#517](https://github.com/andreasgriffin/bitcoin-safe/pull/517)).

{{< video src="bluetooth.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 دعم Bluetooth لـ Jade" description="معاينة لدعم Bluetooth لجهاز Jade في Bitcoin Safe 1.8.0." >}}

#### وضع قفل التطبيق

تمت إضافة وضع قفل التطبيق، وهي طريقة لقفل التطبيق أثناء استمراره في العمل في الخلفية ([#519](https://github.com/andreasgriffin/bitcoin-safe/pull/519)).

{{< video src="app-lock.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 وضع قفل التطبيق" description="معاينة لوضع قفل التطبيق في Bitcoin Safe 1.8.0." >}}

يتضمن هذا الإصدار أيضا وظيفة تحديث سلسة على Windows وتحديثات أسهل على macOS وLinux ([#513](https://github.com/andreasgriffin/bitcoin-safe/pull/513)).

## التحسينات

- أصبح سجل الإشعارات متاحا الآن من أيقونة الدرج ([#493](https://github.com/andreasgriffin/bitcoin-safe/pull/493))
- إصلاحات أخطاء وتحسينات صغيرة في الواجهة

## المساهمات

- قدم [@bsn21m](https://github.com/bsn21m) أول مساهمة له في [#538](https://github.com/andreasgriffin/bitcoin-safe/pull/538)
- الشكر لفريق [bdk](https://github.com/bitcoindevkit/) و[@rustaceanrob](https://github.com/rustaceanrob)
- شكر كبير لـ [@design-rrr](https://github.com/design-rrr) على دعم التصميم وتجربة الاستخدام
