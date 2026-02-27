---
title: "ดาวน์โหลด"
description: "ดาวน์โหลด Bitcoin Safe"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}

✅ **Bitcoin Safe จะแจ้งเตือนเมื่อมีเวอร์ชันใหม่กว่าและยืนยันความถูกต้องโดยอัตโนมัติ.**


Windows binary files are signed, check the [Code signing policy]({{< ref "code-signing-policy" >}}). See here the   [Bitcoin Safe privacy policy]({{< ref "code-signing-policy" >}}).  The  MacOS binaries are not signed, so please disregard the warning message.

<br>
<br>

###  macOS 

โปรดทำตามขั้นตอนต่อไปเพื่อเรียกใช้ Bitcoin Safe บน macOS:
- คัดลอกไปยังโฟลเดอร์แอปของคุณ
- ลองเปิดแอป จะมีข้อความเตือนปรากฏ
- ไปที่ *การตั้งค่าระบบ* --> *ความเป็นส่วนตัวและความปลอดภัย* --> *เปิดต่อไป*
- ตอนนี้คุณสามารถเปิดแอปได้


<img src="/images/mac/copy-app.png" alt="คัดลอกแอปบน macOS"   /> 
<img src="/images/mac/warning.png" alt="การเตือนบน macOS"   /> 
<img src="/images/mac/disable.png" alt="เปิด Bitcoin Safe บน macOS"   /> 



<br>
<br>

### Debian/Ubuntu (คลังแพ็กเกจ APT)

{{< apt_repo_install >}}

<br>
<br>

###  ตรวจสอบลายเซ็น

ซอฟต์แวร์ทั้งหมดถูกลงลายมือชื่อด้วยคีย์ส่วนตัวของฉัน ยืนยันว่าการดาวน์โหลดเป็นของแท้โดยทำตามขั้นตอนดังต่อไปนี้:

นำเข้ากุญแจสาธารณะของฉัน [กุญแจสาธารณะ]({{< gpg_key_link >}}) แล้วตรวจสอบลายเซ็นด้วย:
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