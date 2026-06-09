---
title: "ทำไมต้องเลือก Bitcoin Safe?"
description: "มีกระเป๋าเงิน Bitcoin บนเดสก์ท็อปหลายตัวให้เลือก ดูว่าทำไม Bitcoin Safe จึงโดดเด่น"
draft: false
tags: ["Features"]
images: ["logo.png"]
keywords: ["Bitcoin ปลอดภัย", "คุณสมบัติที่เป็นเอกลักษณ์", "กระเป๋าเงินที่ปลอดภัย", "เป็นมิตรกับผู้ใช้"]
weight: 1000
---



## {{< page-title >}} 
<!-- {{< page-description >}}  -->

<br>
<!-- <br> -->

### ✔ การจัดเก็บ Bitcoin ที่ปลอดภัยและใช้งานง่าย 
<!-- - ❌ 2-of-3 Multisignature is complex to use in other wallets -->
<!-- - 2-of-3 Multi-signature is a good choice  
    - Robust against loss or leak of 1 seed  -->
- The {{<text-name-with-logo>}} <a  href={{< ref "knowledge/setup-singlesig-wallet" >}} role="button">ตัวช่วยตั้งค่า</a> ทำให้การใช้งาน Single และ Multi-signature เป็นเรื่อง **ง่าย** สำหรับผู้ที่ไม่ได้เชี่ยวชาญด้านเทคนิค
    --> เพียงทำตามแต่ละขั้นตอนเพื่อสร้างกระเป๋าเงินที่ปลอดภัย   
    <img  src="/images/multisig-steps.png" style="max-width: 600px; width: 100%;" alt="Multisig setup steps">
    - The <a  href={{< ref "features/pdf-export" >}}   role="button"> <img  src="pdf-export.png" width="100" alt="PDF export">  PDF Export</a> ช่วยให้คุณสำรอง descriptor ของกระเป๋าเงินที่สำคัญพร้อมกับแต่ละ seed ได้
    - ลงทะเบียน Multi-signature กับแต่ละ hardware signer
    - รวมการทดสอบการรับและการใช้จ่ายจากกระเป๋าเงิน เพื่อให้แน่ใจว่า hardware signer หลักๆ ทุกตัวทำงานได้
<br>


<br>

#### ✔ การซิงค์ป้ายกำกับและการสำรองข้อมูล

{{<text-name-with-logo>}} จะทำให้เป็นไปอย่างวิเศษ (ผ่านพลังของข้อความ <a href="https://nostr.com/ ">nostr</a> ที่เข้ารหัส)
- <a  href="{{< ref "features/label-sync" >}}" role="button">ซิงค์</a> หมวดหมู่เหรียญและป้ายกำกับของคุณระหว่างคอมพิวเตอร์
- สำรองหมวดหมู่เหรียญและป้ายกำกับของคุณ สิ่งที่คุณต้องทำก็แค่สำรองคีย์สำรองสั้นๆ เท่านั้น
 

<br>

####  ✔ การร่วมมือแบบหลายฝ่ายใน Multi-sig

ต้องการเข้าร่วมกระเป๋า Multi-sig แบบ 3 ใน 5 หรือไม่?

- หลังจากสร้างกระเป๋าแล้ว {{<text-name-with-logo>}} จะสร้างแชทกลุ่มที่เข้ารหัสบน <a href="https://nostr.com/ ">nostr</a> เพื่อร่วมมือกันและ <a  href="{{< ref "features/collaboration" >}}" role="button">ส่ง PSBTs</a> เพื่อเซ็นกัน
-  <a  href="{{< ref "features/label-sync" >}}" role="button">การซิงค์ป้ายกำกับ</a> ก็ใช้งานได้เช่นกัน
- เพื่อความปลอดภัย ผู้เข้าร่วมแต่ละคนต้องยืนยันตัวตนของผู้ใช้คนอื่น ๆ (เพียงคลิกเดียว)


<br>


#### ✔ จัดระเบียบที่อยู่ด้วยหมวดหมู่เหรียญ

 <img  src="coin-categories.png" width="150" alt="Coin categories"> 
 
- คุณสามารถจัดกลุ่มที่อยู่เป็น **หมวดหมู่เหรียญ** ซึ่งง่ายกว่าการติดป้ายกำกับที่อยู่แต่ละรายการ
- สำหรับแต่ละ PSBT ที่คุณสร้าง คุณเลือกหมวดหมู่เหรียญที่ตรงกันและ {{<text-name-with-logo>}} จะเลือกอินพุตจากหมวดหมู่นั้นเท่านั้น  
- {{<text-name-with-logo>}} จะแจ้งเตือนหาก PSBT หรือธุรกรรมผสมหมวดหมู่เหรียญ


<br>


#### ✔ ลดโอกาสเกิดความผิดพลาด

ผู้คนเคยทำความผิดพลาดที่มีค่าใช้จ่ายสูงมากในอดีต ส่วนใหญ่สามารถป้องกันได้หากผู้ใช้ **ไม่เคย** พิมพ์ seed ลงในคอมพิวเตอร์ {{<text-name-with-logo>}} ป้องกันไม่ให้คุณใช้ seed บนคอมพิวเตอร์ และสนับสนุนให้คุณใช้ hardware signer

- {{<text-name-with-logo>}} รองรับ hardware signer ที่นิยมทั้งหมดอย่างเต็มรูปแบบ (เช่น  <a href="https://store.coinkite.com/promo/8BFF877000C34A86F410">Coldcard</a>, 
            <a href="https://store.coinkite.com/promo/8BFF877000C34A86F410">Coldcard Q</a>, 
            <a href="https://shop.bitbox.swiss/?ref=MOB4dk7gpm">Bitbox02</a>, 
            <a href="https://store.blockstream.com/?code=XEocg5boS77D">Blockstream Jade</a>,    
            <a href="https://affil.trezor.io/SHtN">Trezor Safe</a>,
            <a href="https://foundation.xyz/passport">Foundation Passport</a>,
            <a href="https://keyst.one/?rfsn=8630473.c25550a&utm_source=refersion&utm_medium=affiliate&utm_campaign=8630473.c25550a">Keystone</a>,
            <a href="https://shop.ledger.com/?r=400f1fff75b5">Ledger</a>,
            <a href="https://clavastack.com/en/?coupon=bitcoin-safe">Specter DIY</a>)  
- {{<text-name-with-logo>}} มีภาพหน้าจอและคำแนะนำสำหรับแต่ละ hardware signer เพื่อแนะนำคุณในทุกขั้นตอน 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-images "hardware-signer-screenshots" >}}
    </div>

   

<br>




#### ✔ 🔋 ฟีเจอร์ครบครัน 🔋 


{{<text-name-with-logo>}} ถูกออกแบบให้ใช้งานง่าย แต่ยังรวมทุกฟีเจอร์สำคัญสำหรับผู้ใช้ขั้นสูงไว้ครบถ้วน
- เลือกเซิร์ฟเวอร์ electrum/esplora ของคุณเอง, อินสแตนซ์ mempool, และรีเลย์ nostr
- นำเข้าและส่งออกไฟล์ CSV ได้ทุกที่
- RBF, การยกเลิกธุรกรรม, และการแก้ไข PSBT ที่เสร็จสมบูรณ์
- และอีกมากมาย: ดู <a href="https://github.com/andreasgriffin/bitcoin-safe?tab=readme-ov-file#comprehensive-feature-list">รายการฟีเจอร์ทั้งหมด</a>


<br>
