---
aliases:
  - "/th/features/reproducibility-and-security/"
title: "ความปลอดภัยและความสามารถในการทำซ้ำได้"
description: "Bitcoin Safe ยึดตามมาตรฐานความปลอดภัยของไฟล์ไบนารีในระดับสูง: build ที่ทำซ้ำได้, commit ที่ลงลายเซ็น, release ที่ลงลายเซ็น และการติดตามตรวจสอบจากภายนอกอย่างอิสระ"
draft: false
bucket: features
tags: ["Featured", "Security"]
images: ["logo.png"]
keywords: ["reproducible builds", "verify binaries", "signed commits", "signed releases", "appimage", "flatpak", "windows exe", "binary security"]
weight: 18
---

### {{< page-title >}}
{{< page-description >}}
<br>

![ผลลัพธ์ build ที่ทำซ้ำได้ของ Bitcoin Safe](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 500px;" }

เราได้เพิ่มหลายชั้นของการปกป้องความถูกต้องของไฟล์ดาวน์โหลดบนเว็บไซต์ เพื่อให้แอปที่คุณดาวน์โหลดตรงกับซอร์สโค้ดสาธารณะจริง ๆ:

- **Build ที่ทำซ้ำได้**: Build ของ Linux `deb`, `AppImage`, และ `Flatpak` รวมถึง Windows `portable exe` และ `setup exe` สามารถสร้างซ้ำแบบ byte ต่อ byte ได้ หากไฟล์ที่สร้างใหม่ตรงกันทุกประการ นั่นเป็นหลักฐานที่ชัดเจนว่าไฟล์ไบนารีถูกสร้างมาจากซอร์สโค้ดเดียวกัน
- **ประวัติ repository ที่ลงลายเซ็น**: [GitHub repository ของ Bitcoin Safe](https://github.com/andreasgriffin/bitcoin-safe/commits/main) เผยแพร่ commit ที่ลงลายเซ็นและผ่านการยืนยันแล้ว เพื่อให้ผู้ตรวจสอบสามารถเช็กได้ว่าใครเป็นผู้สร้างโค้ดที่เข้าไปอยู่ใน release
- **ไฟล์ไบนารีที่ลงลายเซ็น**: ไฟล์ release ถูกลงลายเซ็นด้วย [public PGP key]({{< gpg_key_link >}}) ของ Bitcoin Safe และไฟล์ไบนารีบน Windows ยังปฏิบัติตาม [นโยบาย code signing]({{< ref "code-signing-policy" >}}) ด้วย
- **การตรวจสอบความสามารถในการทำซ้ำได้โดยอิสระ**: [WalletScrutiny](https://walletscrutiny.com/desktop/bitcoin.safe/) ติดตาม Bitcoin Safe อย่างอิสระและแสดงสถานะการตรวจสอบ build แบบทำซ้ำได้สำหรับ release บนเดสก์ท็อป
- **การติดตามลายเซ็นอย่างต่อเนื่อง**: [BinaryWatch](https://binarywatch.org/) ตรวจสอบไฟล์ release ของ Bitcoin Safe เป็นประจำ รวมถึงตรวจว่าลายเซ็นยังคงใช้ได้กับ [public PGP key]({{< gpg_key_link >}}) ของ Bitcoin Safe หรือไม่
- **การตรวจสอบอัปเดต**: อัปเดตจะถูกแสดงใน Bitcoin Safe และลายเซ็นของอัปเดตจะถูกตรวจสอบโดยอัตโนมัติ

เมื่อรวมทั้งหมดแล้ว มาตรการเหล่านี้ทำให้ Bitcoin Safe อยู่ในกลุ่มเล็ก ๆ ของโครงการที่ถือว่าความปลอดภัยของไฟล์ไบนารีเป็นส่วนสำคัญของความปลอดภัยของผู้ใช้ ไม่ใช่สิ่งที่ค่อยมาเพิ่มทีหลัง

### ความปลอดภัยคือเกณฑ์สำคัญที่สุดในทุกด้านของ Bitcoin Safe

นอกเหนือจากความถูกต้องของไฟล์ไบนารีแล้ว Bitcoin Safe ยังถูกออกแบบบนพื้นฐานของค่าเริ่มต้นที่ปลอดภัย แนวปฏิบัติการใช้งานที่ดี และคำแนะนำที่ชัดเจนสำหรับผู้ใช้ ตัวอย่างเช่น:

- **การเก็บรักษาที่เน้นฮาร์ดแวร์เป็นหลัก**: Bitcoin Safe ต้องใช้ [hardware signer]({{< ref "library/supported-hardware-signers" >}}) เพื่อให้ seed อยู่บนอุปกรณ์เฉพาะทาง แทนที่จะกลายเป็นความลับแบบ hot บนคอมพิวเตอร์ทั่วไป
- **ขั้นตอนการตั้งค่าที่ปลอดภัยยิ่งขึ้น**: ตัวช่วยตั้งค่าช่วยให้ผู้ใช้สร้าง wallet ที่พร้อมใช้งานจริง โดยรวมถึงการทดสอบ [hardware signer]({{< ref "library/supported-hardware-signers" >}}), [แผ่นสำรองข้อมูล PDF]({{< ref "library/pdf-export/" >}}), และคำแนะนำเกี่ยวกับการเก็บอุปกรณ์และ seed backup อย่างปลอดภัย
- **การยืนยันที่อยู่รับเงิน**: Bitcoin Safe ทำให้ [การยืนยันที่อยู่รับเงิน]({{< ref "library/verify-receive-address/" >}}) บนอุปกรณ์ signer ก่อนแชร์ทำได้ง่าย
- **การตรวจจับ address poisoning**: แอปจะเตือนเมื่อพบ [ที่อยู่ที่น่าสงสัยและคล้ายกัน]({{< ref "library/address-poisoning/" >}})
- **ความปลอดภัยของ multisig**: Bitcoin Safe รองรับ wallet แบบ multisig เพื่อให้เงินจำนวนมากได้รับการปกป้องด้วยหลายอุปกรณ์หรือหลายคน แทนที่จะพึ่งจุดล้มเหลวเพียงจุดเดียว
- **การทำงานร่วมกันที่ทำให้ multisig ง่ายขึ้น**: Bitcoin Safe ทำให้ [การทำงานร่วมกันแบบ multisig]({{< ref "library/collaboration/" >}}) ใช้งานได้จริง จึงประสานการตั้งค่าและการเซ็นธุรกรรมได้ง่ายขึ้นมากในโลกจริง
- **ขั้นตอนการเซ็นที่ชัดเจน**: หน้าจอการเซ็นที่ออกแบบเฉพาะตามอุปกรณ์ช่วยลดความสับสนระหว่างการตรวจสอบ PSBT และช่วยให้ผู้ใช้ทำสิ่งที่ถูกต้องบน signer ที่ถูกต้อง
