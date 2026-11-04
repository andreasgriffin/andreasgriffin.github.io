---
title: "Seed ของ COLDCARD ที่ไม่ปลอดภัย"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "คำแนะนำสั้น ๆ สำหรับย้ายเงินออกจาก seed ที่สร้างบนอุปกรณ์ Coinkite"
---

[Coinkite ได้เปิดเผยจุดอ่อนในการสร้าง seed บน firmware ของ COLDCARD ที่ได้รับผลกระทบ](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/) โปรดดู [การวิเคราะห์ทางเทคนิคของ Block เกี่ยวกับ fallback ของ RNG ที่คาดเดาได้และการ reseed แบบ 32 บิต](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware) ด้วย การอัปเดต firmware ไม่สามารถแก้ไข seed ที่มีอยู่แล้วได้

**หากคุณสร้าง seed ด้วยผลิตภัณฑ์ Coinkite ใด ๆ ให้ย้ายเงินโดยเร็ว!**

## รายการตรวจสอบการย้าย

1. สร้าง seed ใหม่ทั้งหมดบน **อุปกรณ์ลงนามที่ไม่ใช่ COLDCARD** ([ดูอุปกรณ์ที่รองรับ]({{< ref "library/supported-hardware-signers" >}})) ห้ามใช้ seed เก่าซ้ำ จากนั้นใช้อุปกรณ์ลงนามนั้นกับตัวช่วยการตั้งค่า Bitcoin-Safe เพื่อสร้าง [wallet แบบลายเซ็นเดียว]({{< ref "library/setup-singlesig-wallet" >}}) หรือ [wallet แบบหลายลายเซ็น]({{< ref "library/setup-multisig-wallet" >}}) ใหม่
   - หากไม่มี hardware signer ที่ไม่ใช่ COLDCARD สามารถใช้ [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}}) บนอุปกรณ์ Android เฉพาะที่รีเซ็ตเป็นค่าโรงงานแล้ว เก็บไว้แบบออฟไลน์ และใช้สำหรับลงนามเท่านั้น
   - ทำการทดสอบรับและส่งในตัวช่วยให้เสร็จเพื่อให้แน่ใจว่า wallet ใหม่ตั้งค่าอย่างถูกต้อง: ตรวจสอบข้อมูลสำรองและที่อยู่รับบน signer ใหม่ รับเงินทดสอบจำนวนเล็กน้อย แล้วทำ self-send ไปยังที่อยู่อื่นใน wallet ใหม่ที่ตรวจสอบแล้วให้สำเร็จ
2. ลงนาม transaction สำหรับการย้าย:
   - **หาก wallet ที่ได้รับผลกระทบเป็นแบบลายเซ็นเดียว:** broadcast ตามปกติด้วย fee สูงเพื่อให้ได้รับการยืนยันอย่างรวดเร็ว
   - **หาก wallet ที่ได้รับผลกระทบเป็นแบบหลายลายเซ็น:** อย่า broadcast ตามปกติ เพราะจะเปิดเผย public keys ใน public mempool ให้คัดลอก raw transaction ที่ลงนามแล้วและส่งโดยตรงผ่าน [MARA Slipstream](https://slipstream.mara.com/)
3. เก็บ COLDCARD เครื่องเก่าไว้จนกว่ายอดเงินทั้งหมดจะมาถึงและได้รับการยืนยันใน wallet ใหม่ จากนั้นอัปเดตเป็น firmware ล่าสุด

หากคุณกำลังช่วยผู้อื่นย้ายเงิน ห้ามขอให้พวกเขาแชร์ ถ่ายรูป หรือพิมพ์คำ seed โดยเด็ดขาด Seed ต้องเป็นความลับและป้อนบนอุปกรณ์ลงนามเท่านั้น
