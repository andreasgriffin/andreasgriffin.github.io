---
aliases:
- /th/knowledge/supported-hardware-signers/keycard-shell/
title: Keycard Shell
signer: keycard-shell
bucket: knowledge
---

## สิ่งที่ควรคาดหวัง

- ใช้ Keycard Shell กับ Bitcoin-Safe ผ่าน QR ไม่จำเป็นต้องใช้แอปของผู้ผลิต
- คีย์ถูกสร้างและเก็บไว้ในชิป secure element ของ Keycard Shell อ่าน PSBT แสดงธุรกรรมบนหน้าจอของตัวเอง และลงนามหลังจากคุณยืนยันบนอุปกรณ์เท่านั้น
- รองรับ multisig (P2WSH) และขั้นตอน PSBT แบบเต็ม ลงทะเบียน descriptor แบบ multisig และส่งออกข้อมูลอุปกรณ์ลงนามสำหรับ Bitcoin-Safe
- ตรวจสอบทุกเอาต์พุตและค่าธรรมเนียมบนหน้าจอ Shell ก่อนลงนาม
