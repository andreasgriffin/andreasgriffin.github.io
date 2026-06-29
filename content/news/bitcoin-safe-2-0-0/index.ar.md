---
title: "Bitcoin Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "ملاحظات إصدار Bitcoin Safe 2.0.0، مع معالج إعداد معاد بناؤه، ومزامنة خاصة عبر Compact Block Filters، ودعم أوسع للمحافظ الصلبة."
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">إعلان الإصدار</p>
    <h2 class="display-6 mb-3">Bitcoin Safe 2.0 - إعداد موجّه للمحفظة، ومزامنة خاصة للسلسلة، وتوقيع يركّز على الجهاز</h2>
    <p class="lead mb-4">يأتي هذا الإصدار بمعالج إعداد جديد بالكامل، ومزامنة خاصة للسلسلة باستخدام Compact Block Filters، وتدفّق توقيع منظّم حول كل جهاز عتادي. إذا كنت مهتمًا بـ cold storage لكنك لم تكن واثقًا بعد، فهذا هو الإصدار الذي يستحق التجربة.</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">تنزيل Bitcoin Safe 2.0</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">شاهد ما الجديد</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">إعداد المحفظة خطوة بخطوة</h2>
          <p class="mb-0">يشرح المعالج الجديد كل خطوة، ويقلّل الالتباس، ويساعد المستخدمين الجدد على اختيار المسار الصحيح من دون فقدان قوة multisig.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">مزامنة خاصة للمحفظة</h2>
          <p class="mb-0">تتم مزامنة المحافظ الجديدة الآن مع Compact Block Filters بشكل افتراضي، حتى تتمكن من فحص السلسلة بشكل خاص من دون الاعتماد على Electrum indexer تابع لجهة خارجية.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">توقيع يركّز على الجهاز</h2>
          <p class="mb-0">تظل تدفّقات التوقيع الآن متمركزة حول الجهاز الموجود أمامك، مع خطوات تالية أوضح لـ QR وUSB وBluetooth والملفات وتنسيق multisig.</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## مسار موجّه نحو self-custody {#setup-flow}

تمت إعادة بناء تجربة التشغيل الأول من الصفر. لا يزال Bitcoin Safe موجّهًا إلى self-custody الجاد، بما في ذلك multisig المدعوم بالأجهزة، ويمنح الإصدار 2.0 الآن المستخدمين الجدد مسارًا موجّهًا عبر هذا الإعداد. يشرح المعالج الجديد ما الذي يحدث، وأين أنت داخل التدفق، وما الذي يحتاجه كل signer منك قبل الانتقال إلى الخطوة التالية.

<p class="small text-muted">للتفاصيل التنفيذية، راجع <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a>.</p>

أبرز ما في إعادة التصميم:

- شاشة ترحيب جديدة تساعد المستخدمين لأول مرة على اختيار نقطة البداية المناسبة
- تدفّق تقدّم خطوة بخطوة أثناء إنشاء المحفظة
- شاشات توقيع خاصة بكل جهاز مع تعليمات مركّزة ومساعدة سياقية
- ملفات recovery PDF بأسماء الأجهزة وأيقوناتها حتى تبقى النسخ الاحتياطية واضحة

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## مزامنة خاصة ومتينة للسلسلة باستخدام Compact Block Filters {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) أصبحت الآن تشغّل مزامنة المحافظ الجديدة في Bitcoin Safe 2.0. وبدلًا من سؤال Electrum server عن العناوين التي تخصك، يستطيع Bitcoin Safe الآن فحص السلسلة بشكل خاص عبر تنزيل compact filters من Bitcoin Core peers عشوائيين والتحقق منها محليًا.

<p class="small text-muted">للتفاصيل التنفيذية، راجع <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a>.</p>


- تظل مزامنة المحفظة خاصة منذ أول تشغيل
- لا يوجد اعتماد على Electrum servers من جهات خارجية
- ما زال Electrum متاحًا لمن يفضّله
- [مزامنة فورية بعد الفحص الأولي للمحفظة]({{< ref "library/compact-block-filters" >}})
- [إشعارات فورية للمعاملات المُرحّلة]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## تدفّق توقيع يركّز على الجهاز لكل جهاز {#device-focused-signing}

تعيد هذه الواجهة الجديدة أيضًا تشكيل تدفّق التوقيع بعد إنشاء المحفظة. بدلًا من شاشة عامة واحدة لكل signer، يضع Bitcoin Safe الآن الإجراءات حول الجهاز المحدد الذي تستخدمه.

<p class="small text-muted">للتفاصيل التنفيذية، راجع <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a>.</p>

- تظهر إجراءات QR وUSB وBluetooth وتصدير/استيراد الملفات وSync & Chat مباشرة على بطاقة signer النشط
- يبقى signers المتبقون، والأجهزة التي وقّعت بالفعل، والخطوة التالية المطلوبة مرئية بوضوح
- تظل تدفّقات multisig متعددة الأجهزة قابلة للقراءة لأن هوية signer تبقى ظاهرة طوال PSBT
- تتم معالجة المعاملات المعقدة التي تمزج بين single-sig وmultisig بشكل صحيح، بحيث تبقى كل خطوة توقيع واضحة

![بطاقة signer تعرض إجراءات خاصة بالجهاز لـ QR وUSB وBluetooth وتصدير الملفات وChat & Sync](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## بنية plugins لسير العمل التجاري ولمستخدمي القوة

يضع Bitcoin Safe 2.0 أيضًا الأساس لإضافات مستقبلية موجهة إلى شركات Bitcoin ومستخدمي القوة. لذا ترقّب ما سيأتي لاحقًا :-)

<p class="small text-muted">للتفاصيل التنفيذية، راجع <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a>.</p>

- توزيع plugins عبر مستودع خارجي من نوع *sources*
- كل plugin يكون *موقّعًا عبر GPG* من [andreasgriffin]({{< gpg_key_link >}}) لضمان الأمان والسلامة والتوزيع
- يتيح الإصدار المستقل لكل plugin والتحديثات تطويرًا أسرع وأكثر استقلالية

![بطاقة signer تعرض إجراءات خاصة بالجهاز لـ QR وUSB وBluetooth وتصدير الملفات وChat & Sync](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## دعم أوسع للأجهزة والمزيد من الصقل {#hardware-support}

- رموز QR المتحركة أصبحت أسرع بنسبة **30%** لتسريع المسح
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) أصبح مدعومًا الآن عبر USB
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) يدعم الآن **Bluetooth** إلى جانب USB وQR
- تمت إضافة [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) و[COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) كأجهزة مدعومة
- اطّلع على [القائمة الكاملة للأجهزة المدعومة]({{< ref "library/supported-hardware-signers" >}})
- تمت إضافة فحوصات آلية من أجل [reproducibility]({{< ref "library/reproducibility-and-security" >}})
- شاهد [القائمة الكاملة](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0) للتحسينات هنا


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## نقاط القوة الحالية لا تزال موجودة

إصدار 2.0 ليس إعادة ضبط كاملة. فأسفل تدفّق onboarding والتوقيع الجديدين، لا يزال Bitcoin Safe يحتفظ بالميزات التي جعلته مفيدًا يوميًا: collaborative multisig، ونسخ احتياطية PDF، وسجل محفظة قابل للبحث، وتصوّرات لتدفق الأموال، وlabel sync، وغير ذلك.

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">هل أنت جاهز لتجربة Bitcoin Safe 2.0؟</h2>
  <p class="mb-3">نزّل أحدث إصدار واستكشف بنفسك onboarding الجديد والمزامنة الخاصة وتحسينات المحافظ الصلبة.</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">تنزيل Bitcoin Safe</a>
</div>


<br><br>

## شكرًا

يعتمد هذا الإصدار على الكثير من العمل من المساهمين والمختبرين و[الداعمين عبر المشروع]({{< ref "donate" >}}):

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r)) على إعادة تصميم المعالج، والعمل على واجهة plugins، والدعم **الرائع والمتواصل** في UI/UX
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) على عميل Compact Block Filter الذي يشغّل الآن مزامنة المحافظ الجديدة بشكل خاص
- فريق [Bitcoin Dev Kit](https://github.com/bitcoindevkit/) على المكتبات الموجودة في قلب Bitcoin Safe
- فريق [ndk](https://github.com/nostr-dev-kit/ndk) على المكتبات التي تشغّل وظائف nostr
- كل من في مجتمع Bitcoin Safe ممن اختبروا release candidates، وأبلغوا عن الأخطاء، وترجموا الصفحات، وأرسلوا sats، واستمروا في دفع المشروع إلى الأمام
- [المترجمون]({{< ref "donate/#translators" >}})، ومنهم <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (الفيتنامية)" title="qdyg-vn 🇻🇳 (الفيتنامية)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (الألمانية)" title="bsn21m 🇩🇪 (الألمانية)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (الإسبانية)" title="cyphra 🇪🇸 (الإسبانية)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (الصينية)" title="DaGrindDontStop 🇨🇳 (الصينية)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


إذا أردت المساعدة في تمويل الإصدار القادم، يمكنك أيضًا التبرع هنا: {{< donation_btc >}}
