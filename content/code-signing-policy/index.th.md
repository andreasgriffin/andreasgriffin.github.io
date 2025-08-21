---
title: "นโยบายการลงนามโค้ด และ นโยบายความเป็นส่วนตัวของ Bitcoin Safe"
description: "นโยบายการลงนามโค้ด"
draft: false
tags: ["legal"]
menu:
  footer:
    weight: 90
---


## นโยบายการลงนามโค้ด


การลงนามโค้ดฟรีจัดให้โดย [SignPath.io](https://about.signpath.io/), ใบรับรองโดย [SignPath Foundation](https://signpath.org/)


## นโยบายความเป็นส่วนตัว
โปรแกรมนี้ใช้ค่าเริ่มต้น
- เซิร์ฟเวอร์ electrum/esplora ของ [blockstream.com](https://blockstream.com/) เพื่อดึงข้อมูลบล็อกเชน
- ดึงข้อมูลค่าธรรมเนียม mempool จาก [mempool.space](https://mempool.space/)

คุณสามารถระบุเซิร์ฟเวอร์ของคุณเอง (ส่วนตัว) สำหรับทั้งสองรายการได้ใน "Network settings"

เมื่อเปิดฟีเจอร์ Sync&Chat จะมีการใช้ [รีเลย์เริ่มต้น](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py) เพื่อส่งข้อมูลที่เข้ารหัสไปยังอุปกรณ์ที่คุณอนุมัติและไว้ใจได้ คุณสามารถระบุรีเลย์ของคุณเองในการตั้งค่า Sync&Chat

โปรแกรมนี้จะไม่ส่งข้อมูลอื่นใดไปยังระบบเครือข่ายอื่น ๆ เว้นแต่จะมีการร้องขอโดยเฉพาะจากผู้ใช้หรือจากบุคคลที่ติดตั้งหรือดำเนินการโปรแกรมนั้น