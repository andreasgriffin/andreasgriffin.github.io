---
title: "Bitcoin-Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "บันทึกประจำรุ่นของ Bitcoin-Safe 2.0.0 พร้อมตัวช่วยตั้งค่าที่สร้างใหม่ การซิงก์แบบเป็นส่วนตัวด้วย Compact Block Filters และการรองรับฮาร์ดแวร์วอลเล็ตที่กว้างขึ้น"
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">ประกาศการออกรุ่น</p>
    <h2 class="display-6 mb-3">Bitcoin-Safe 2.0 - การตั้งค่าวอลเล็ตแบบมีคำแนะนำ การซิงก์เชนแบบเป็นส่วนตัว และการลงนามที่โฟกัสกับอุปกรณ์</h2>
    <p class="lead mb-4">รุ่นนี้มาพร้อมตัวช่วยตั้งค่าที่สร้างใหม่ทั้งหมด การซิงก์เชนแบบเป็นส่วนตัวด้วย Compact Block Filters และขั้นตอนการลงนามที่จัดวางรอบอุปกรณ์ฮาร์ดแวร์แต่ละตัว หากคุณสนใจ cold storage แต่ยังไม่มั่นใจ นี่คือรุ่นที่น่าลองมากที่สุด</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">ดาวน์โหลด Bitcoin-Safe 2.0</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">ดูว่ามีอะไรใหม่</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">ตั้งค่าวอลเล็ตแบบทีละขั้น</h2>
          <p class="mb-0">ตัวช่วยใหม่อธิบายทุกขั้นตอน ลดความกำกวม และช่วยให้ผู้ใช้ใหม่เลือกเส้นทางที่ถูกต้องได้โดยไม่เสียความสามารถของ multisig</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">ซิงก์วอลเล็ตแบบเป็นส่วนตัว</h2>
          <p class="mb-0">วอลเล็ตใหม่จะซิงก์กับ Compact Block Filters โดยอัตโนมัติ ทำให้คุณสแกนเชนแบบเป็นส่วนตัวได้โดยไม่ต้องพึ่ง third-party Electrum indexer</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">การลงนามที่โฟกัสกับอุปกรณ์</h2>
          <p class="mb-0">ขั้นตอนการลงนามตอนนี้จะยึดอุปกรณ์ตรงหน้าคุณเป็นศูนย์กลาง พร้อมขั้นตอนถัดไปที่ชัดเจนขึ้นสำหรับ QR, USB, Bluetooth, ไฟล์ และการประสานงาน multisig</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## เส้นทางแบบมีคำแนะนำสู่ self-custody {#setup-flow}

ประสบการณ์การใช้งานครั้งแรกถูกสร้างใหม่ทั้งหมด Bitcoin-Safe ยังคงมุ่งไปที่ self-custody อย่างจริงจัง รวมถึง hardware-backed multisig และในเวอร์ชัน 2.0 ก็เพิ่มเส้นทางแบบมีคำแนะนำสำหรับผู้ใช้ใหม่ให้ผ่านการตั้งค่านี้ได้ง่ายขึ้น ตัวช่วยใหม่จะอธิบายว่าเกิดอะไรขึ้น ตอนนี้คุณอยู่ตรงไหนของขั้นตอน และ signer แต่ละคนต้องการอะไรจากคุณก่อนจะไปต่อ

<p class="small text-muted">ดูรายละเอียดการพัฒนาได้ที่ <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a></p>

จุดเด่นของการออกแบบใหม่:

- หน้าต้อนรับใหม่ที่ช่วยให้ผู้ใช้ครั้งแรกเลือกจุดเริ่มต้นได้ถูกต้อง
- ขั้นตอนแสดงความคืบหน้าแบบทีละขั้นระหว่างสร้างวอลเล็ต
- หน้าจอลงนามเฉพาะอุปกรณ์พร้อมคำแนะนำที่ชัดเจนและความช่วยเหลือตามบริบท
- recovery PDF ที่มีชื่อและไอคอนของอุปกรณ์ เพื่อให้การสำรองข้อมูลไม่สับสน

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## การซิงก์เชนแบบเป็นส่วนตัวและแข็งแรงด้วย Compact Block Filters {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) กลายเป็นกลไกหลักของการซิงก์วอลเล็ตใหม่ใน Bitcoin-Safe 2.0 แล้ว แทนที่จะถาม Electrum server ว่าที่อยู่ใดเป็นของคุณ Bitcoin-Safe สามารถสแกนเชนแบบเป็นส่วนตัวได้ด้วยการดาวน์โหลด compact filters จาก Bitcoin Core peers แบบสุ่มแล้วตรวจสอบภายในเครื่อง

<p class="small text-muted">ดูรายละเอียดการพัฒนาได้ที่ <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a></p>


- การซิงก์วอลเล็ตยังคงเป็นส่วนตัวตั้งแต่เปิดใช้งานครั้งแรก
- ไม่ต้องพึ่ง third-party Electrum servers
- Electrum ยังใช้งานได้สำหรับผู้ที่ต้องการใช้
- [ซิงก์ได้ทันทีหลังการสแกนวอลเล็ตครั้งแรก]({{< ref "library/compact-block-filters" >}})
- [แจ้งเตือนทันทีสำหรับธุรกรรมที่ถูก relay]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## ขั้นตอนการลงนามที่โฟกัสกับอุปกรณ์สำหรับทุกอุปกรณ์ {#device-focused-signing}

การออกแบบใหม่นี้ยังปรับรูปแบบขั้นตอนการลงนามหลังจากสร้างวอลเล็ตแล้วด้วย จากเดิมที่ใช้หน้าจอทั่วไปหนึ่งหน้าสำหรับ signer ทุกคน ตอนนี้ Bitcoin-Safe จะวาง actions ต่าง ๆ ไว้รอบอุปกรณ์ที่คุณกำลังใช้งานอยู่โดยตรง

<p class="small text-muted">ดูรายละเอียดการพัฒนาได้ที่ <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a></p>

- actions สำหรับ QR, USB, Bluetooth, การส่งออก/นำเข้าไฟล์ และ Sync & Chat แสดงอยู่บนการ์ดของ active signer โดยตรง
- signer ที่เหลือ อุปกรณ์ที่ลงนามแล้ว และขั้นตอนถัดไปที่ต้องทำ มองเห็นได้ในทันที
- ขั้นตอน multisig ที่มีอุปกรณ์หลายแบบยังคงอ่านเข้าใจง่าย เพราะ signer identity มองเห็นได้ตลอดทั้ง PSBT
- ธุรกรรมที่ซับซ้อนซึ่งมีทั้ง single-sig และ multisig inputs ถูกจัดการอย่างถูกต้อง ทำให้ทุกขั้นตอนการลงนามยังคงชัดเจน

![การ์ด signer ที่มี actions เฉพาะอุปกรณ์สำหรับ QR, USB, Bluetooth, การส่งออกไฟล์ และ Chat & Sync](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## สถาปัตยกรรม plugins สำหรับ workflow ทางธุรกิจและ power users

Bitcoin-Safe 2.0 ยังวางรากฐานสำหรับ plugins เพิ่มเติมในอนาคตที่มุ่งเป้าไปยังธุรกิจ Bitcoin และ power users ด้วย ดังนั้นอย่าลืมติดตามสิ่งที่จะตามมา :-)

<p class="small text-muted">ดูรายละเอียดการพัฒนาได้ที่ <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a></p>

- กระจาย plugins ผ่าน external *sources* repository
- plugins แต่ละตัวจะถูก *GPG signed* โดย [andreasgriffin]({{< gpg_key_link >}}) เพื่อให้มั่นใจในความปลอดภัย ความสมบูรณ์ และการส่งมอบ
- การแยก versioning และ updates ของแต่ละ plugin ช่วยให้พัฒนา plugins ได้เร็วขึ้นและเป็นอิสระมากขึ้น

![การ์ด signer ที่มี actions เฉพาะอุปกรณ์สำหรับ QR, USB, Bluetooth, การส่งออกไฟล์ และ Chat & Sync](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## รองรับอุปกรณ์ได้กว้างขึ้นและเก็บรายละเอียดดีขึ้น {#hardware-support}

- QR codes แบบเคลื่อนไหวเร็วขึ้น **30%** เพื่อการสแกนที่รวดเร็วขึ้น
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) รองรับผ่าน USB แล้ว
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) รองรับ **Bluetooth** เพิ่มเติมจาก USB และ QR
- เพิ่ม [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) และ [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) เข้ามาเป็นอุปกรณ์ที่รองรับ
- ดู[รายการอุปกรณ์ที่รองรับทั้งหมด]({{< ref "library/supported-hardware-signers" >}})
- เพิ่มการตรวจสอบอัตโนมัติสำหรับ [reproducibility]({{< ref "library/reproducibility-and-security" >}})
- ดู[รายการทั้งหมด](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0) ของการปรับปรุงได้ที่นี่


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## จุดแข็งเดิมยังอยู่ครบ

เวอร์ชัน 2.0 ไม่ใช่การเริ่มต้นใหม่ทั้งหมด ภายใต้ onboarding และ signing flow ใหม่ Bitcoin-Safe ยังคงรักษาความสามารถที่ทำให้มันมีประโยชน์ในทุกวันไว้เหมือนเดิม ไม่ว่าจะเป็น collaborative multisig, PDF backups, ประวัติวอลเล็ตที่ค้นหาได้, การแสดงภาพการไหลของเงิน, label sync และอื่น ๆ

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">พร้อมลองใช้ Bitcoin-Safe 2.0 แล้วหรือยัง?</h2>
  <p class="mb-3">ดาวน์โหลดรุ่นล่าสุดและลองสำรวจ onboarding ใหม่ การซิงก์แบบเป็นส่วนตัว และการปรับปรุงฮาร์ดแวร์วอลเล็ตด้วยตัวคุณเอง</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">ดาวน์โหลด Bitcoin-Safe</a>
</div>


<br><br>

## ขอบคุณ

รุ่นนี้เกิดขึ้นได้จากการทำงานอย่างหนักของผู้ร่วมพัฒนา ผู้ทดสอบ และ[ผู้สนับสนุนทั่วทั้งโครงการ]({{< ref "donate" >}}):

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r)) สำหรับการออกแบบ wizard ใหม่ งานด้าน plugin UI และการสนับสนุน UI/UX ที่ **ยอดเยี่ยมและไม่ย่อท้อ**
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) สำหรับ Compact Block Filter client ที่ตอนนี้ขับเคลื่อนการซิงก์แบบเป็นส่วนตัวของวอลเล็ตใหม่
- ทีม [Bitcoin Dev Kit](https://github.com/bitcoindevkit/) สำหรับไลบรารีที่เป็นแกนหลักของ Bitcoin-Safe
- ทีม [ndk](https://github.com/nostr-dev-kit/ndk) สำหรับไลบรารีที่ขับเคลื่อนความสามารถด้าน nostr
- ทุกคนในชุมชน Bitcoin-Safe ที่ช่วยทดสอบ release candidates, รายงาน bugs, แปลหน้าเว็บ, ส่ง sats และผลักดันโครงการต่อไป
- [ผู้แปล]({{< ref "donate/#translators" >}}) ได้แก่ <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (เวียดนาม)" title="qdyg-vn 🇻🇳 (เวียดนาม)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (เยอรมัน)" title="bsn21m 🇩🇪 (เยอรมัน)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (สเปน)" title="cyphra 🇪🇸 (สเปน)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (จีน)" title="DaGrindDontStop 🇨🇳 (จีน)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


หากคุณต้องการช่วยสนับสนุนการเงินสำหรับรุ่นถัดไป คุณสามารถบริจาคได้ที่นี่เช่นกัน: {{< donation_btc >}}
