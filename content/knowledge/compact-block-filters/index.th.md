---
title: "ตัวกรองบล็อกแบบกะทัดรัด"
description: "ทำความเข้าใจว่าตัวกรองบล็อกแบบกะทัดรัดคืออะไร และช่วยเพิ่มความเป็นส่วนตัวได้อย่างไรเมื่อเทียบกับเซิร์ฟเวอร์ Electrum"
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "ตัวกรองบล็อกแบบกะทัดรัด"
  - "CBF"
  - "ความเป็นส่วนตัว"
  - "กระเป๋าเงิน Bitcoin"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**ตัวกรองบล็อกแบบกะทัดรัด (CBF)** ช่วยให้ [Bitcoin Safe]({{< ref "/" >}}) สแกนบล็อกเชนได้โดยไม่ต้องถามเซิร์ฟเวอร์ Electrum ว่าที่อยู่ใดเป็นของคุณ

![Bitcoin Safe ดาวน์โหลดตัวกรองบล็อกแบบกะทัดรัดจาก peer ของ Bitcoin Core แบบสุ่มหลายตัว](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

แทนที่จะสอบถามเซิร์ฟเวอร์กลาง Bitcoin Safe จะดาวน์โหลดตัวกรองขนาดเล็กสำหรับแต่ละบล็อกจาก peer ของ Bitcoin Core แบบสุ่ม กระเป๋าเงินของคุณตรวจสอบตัวกรองเหล่านี้แบบโลคัล และจะดาวน์โหลดบล็อกเต็มเมื่อจำเป็นเท่านั้น

### CBF เทียบกับ Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">ด้าน</th>
        <th scope="col">ตัวกรองบล็อกแบบกะทัดรัด</th>
        <th scope="col">เซิร์ฟเวอร์ Electrum</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">ความเป็นส่วนตัว</th>
        <td><span class="text-success fw-semibold">ดี</span> - ข้อมูลกระเป๋าเงินยังคงอยู่ในเครื่อง</td>
        <td><span class="text-danger fw-semibold">แย่</span> - เซิร์ฟเวอร์สามารถเห็นที่อยู่และประวัติของคุณ</td>
      </tr>
      <tr>
        <th scope="row">แหล่งข้อมูล</th>
        <td><span class="text-success fw-semibold">ดี</span> - peer ของ Bitcoin Core แบบสุ่ม</td>
        <td><span class="text-warning fw-semibold">กลาง</span> - เซิร์ฟเวอร์ที่คุณเลือกเพียงตัวเดียว</td>
      </tr>
      <tr>
        <th scope="row">การซิงก์ครั้งแรก</th>
        <td><span class="text-warning fw-semibold">กลาง</span> - มักจะช้ากว่า</td>
        <td><span class="text-success fw-semibold">ดี</span> - มักจะเร็วกว่า</td>
      </tr>
      <tr>
        <th scope="row">การซิงก์ต่อเนื่อง</th>
        <td><span class="text-success fw-semibold">ดี</span> - เร็วมากหลังการซิงก์ครั้งแรก</td>
        <td><span class="text-success fw-semibold">ดี</span> - โดยทั่วไปเร็ว</td>
      </tr>
      <tr>
        <th scope="row">เหมาะสำหรับ</th>
        <td><span class="text-success fw-semibold">ดี</span> - ผู้ใช้ที่ให้ความสำคัญกับความเป็นส่วนตัว</td>
        <td><span class="text-success fw-semibold">ดี</span> - การตั้งค่าและกู้คืนที่เร็วที่สุด</td>
      </tr>
    </tbody>
  </table>
</div>

### ทำไมควรใช้ CBF

- ความเป็นส่วนตัวดีกว่า: กระเป๋าเงินของคุณไม่ต้องถามเซิร์ฟเวอร์ว่าใช้ที่อยู่ใด
- ไม่ต้องพึ่งตัวจัดทำดัชนีที่เชื่อถือได้: Bitcoin Safe สื่อสารกับเครือข่าย Bitcoin โดยตรง
- ซิงก์แบบเบา: ตัวกรองมีขนาดเล็ก จึงไม่จำเป็นต้องใช้บล็อกเชนทั้งหมด

### สิ่งที่คาดหวังได้

- กระเป๋าเงินใหม่หรือการกู้คืน: การซิงก์ครั้งแรกมักใช้เวลา **5 ถึง 30 นาที**
- กระเป๋าเงินที่ซิงก์แล้ว: มักตามทันได้ **เร็วมาก** บ่อยครั้งภายใน **ไม่ถึง 30 วินาที**
- เปลี่ยนจาก Electrum ไป CBF: โดยทั่วไปก็ **ไม่ถึง 30 วินาที** เช่นกัน

คุณสามารถเลือกจำนวน peer ที่ Bitcoin Safe เชื่อมต่อได้ ยิ่งมี peer มาก ความสำรองก็ยิ่งดี แต่โดยปกติก็ใช้แบนด์วิดท์และเวลาในการซิงก์มากขึ้น ค่าเริ่มต้นคือ **2** peer

### ธุรกรรมที่ยังไม่ยืนยัน

CBF ครอบคลุมเฉพาะ **บล็อกที่ยืนยันแล้ว** เท่านั้น หากต้องการรับการแจ้งเตือนเงินเข้าแบบยังไม่ยืนยันด้วย ให้เปิด [Instant transaction notifications]({{< ref "knowledge/instant-transactions-notifications/" >}}) ไว้ ซึ่งเป็นค่าเริ่มต้น

### หมายเหตุทางเทคนิค

ตัวกรองบล็อกแบบกะทัดรัดกำหนดไว้ใน [BIP158](https://bips.dev/158/). Bitcoin Safe ใช้โมดูลโอเพนซอร์ส [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto)

คุณยังสามารถใช้โหนด Bitcoin Core ของคุณเองเป็น peer เริ่มต้นในตั้งค่า _Bitcoin network monitoring_ ได้

![การตั้งค่าโหนดเริ่มต้น](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
