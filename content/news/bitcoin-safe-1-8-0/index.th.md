---
title: "Bitcoin Safe 1.8.0"
date: "2026-03-31"
description: "บันทึกประจำรุ่นของ Bitcoin Safe 1.8.0 รวมถึงการซูมกราฟยอดคงเหลือ nLocktime แบบกำหนดเอง โหมดล็อกแอป และการอัปเดตที่ง่ายขึ้น"
videos:
  - "https://www.youtube.com/watch?v=S0O40-p_w0M"
---

## ฟีเจอร์ใหม่

#### การซูมกราฟยอดคงเหลือ

เพิ่มการซูมกราฟยอดคงเหลือแล้ว ([#492](https://github.com/andreasgriffin/bitcoin-safe/pull/492))

{{< video src="zoom.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 การซูมกราฟยอดคงเหลือ" description="ตัวอย่างการซูมกราฟยอดคงเหลือใน Bitcoin Safe 1.8.0" >}}

#### nLocktime แบบกำหนดเอง

เพิ่มการรองรับ nLocktime แบบกำหนดเอง ซึ่งช่วยให้คุณกำหนดความสูงบล็อกหรือเวลาที่เร็วที่สุดที่ธุรกรรมจะสามารถยืนยันได้ ([#481](https://github.com/andreasgriffin/bitcoin-safe/pull/481))

{{< video src="nLocktime.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 nLocktime แบบกำหนดเอง" description="ตัวอย่างการรองรับ nLocktime แบบกำหนดเองใน Bitcoin Safe 1.8.0" >}}

#### รองรับ Bluetooth สำหรับ Jade

เพิ่มการรองรับ Bluetooth สำหรับ Jade แล้ว ([#517](https://github.com/andreasgriffin/bitcoin-safe/pull/517))

{{< video src="bluetooth.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 รองรับ Bluetooth สำหรับ Jade" description="ตัวอย่างการรองรับ Bluetooth สำหรับ Jade ใน Bitcoin Safe 1.8.0" >}}

#### โหมดล็อกแอป

เพิ่มโหมดล็อกแอป ซึ่งเป็นวิธีล็อกแอปขณะที่ยังคงทำงานอยู่เบื้องหลัง ([#519](https://github.com/andreasgriffin/bitcoin-safe/pull/519))

{{< video src="app-lock.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 โหมดล็อกแอป" description="ตัวอย่างโหมดล็อกแอปใน Bitcoin Safe 1.8.0" >}}

ยังรวมถึงฟังก์ชันอัปเดตแบบลื่นไหลบน Windows และการอัปเดตที่ง่ายขึ้นบน macOS และ Linux ([#513](https://github.com/andreasgriffin/bitcoin-safe/pull/513))

## การปรับปรุง

- ประวัติการแจ้งเตือนสามารถดูได้จากไอคอนในถาดแล้ว ([#493](https://github.com/andreasgriffin/bitcoin-safe/pull/493))
- การแก้ไขบั๊กและการปรับปรุง UI เล็กน้อย

## การมีส่วนร่วม

- [@bsn21m](https://github.com/bsn21m) ได้มีส่วนร่วมครั้งแรกใน [#538](https://github.com/andreasgriffin/bitcoin-safe/pull/538)
- ขอบคุณทีม [bdk](https://github.com/bitcoindevkit/) และ [@rustaceanrob](https://github.com/rustaceanrob)
- ขอบคุณอย่างมากสำหรับ [@design-rrr](https://github.com/design-rrr) ที่ช่วยด้านการออกแบบและ UX
