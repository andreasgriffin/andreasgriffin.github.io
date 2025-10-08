---
title: "ฟีเจอร์ทั้งหมด"
description: "ภาพรวมโดยละเอียดของฟีเจอร์ส่วนใหญ่ใน Bitcoin Safe"
draft: false
tags: [ "Features" ]
images: ["logo.png"]
keywords: [
  "Bitcoin Safe",
  "กระเป๋าออมบิตคอยน์",
  "กระเป๋า MultiSig",
  "ตัวช่วยตั้งค่า Multisig",
  "ผู้ลงนามฮาร์ดแวร์",
  "การจัดเก็บ seed อย่างปลอดภัย",
  "Coldcard",
  "Coldcard Q",
  "Bitbox02",
  "Blockstream Jade",
  "Trezor",
  "Foundation Passport",
  "Keystone",
  "Ledger",
  "Specter DIY",
  "BDK",
  "การสนับสนุนหลายภาษา",
  "การตั้งป้ายที่อยู่",
  "แผนภาพการไหลของธุรกรรม",
  "PSBT",
  "การเลือกค่าธรรมเนียม",
  "mempool",
  "Electrum server",
  "Compact Block Filters",
  "CSV export",
  "CSV import",
  "BIP329",
  "ลากและวาง",
  "Replace-by-Fee",
  "PDF สำรอง",
  "การลงนามข้อความ",
  "MicroSD",
  "USB",
  "QR codes",
  "animated QR codes",
  "การค้นหาและการกรอง",
  "แชทกระเป๋า",
  "การซิงโครไนซ์ป้าย",
  "regtest",
  "Docker",
  "Nigiri",
  "ข้ามแพลตฟอร์ม",
  "การติดตั้ง",
  "การพัฒนา"
]
weight: -10
---
<!-- header-end -->
# Bitcoin Safe

#### กระเป๋าออมบิตคอยน์สำหรับทุกคนในครอบครัว

- **ง่าย** Multisig‑Wallet Setup
  - คำแนะนำขั้นตอนต่อขั้นสำหรับการตั้งค่า MultiSig อย่างปลอดภัยพร้อมแผ่นสำรอง PDF
  - การทดสอบการทำธุรกรรมเพื่อยืนยันว่าผู้ลงนามฮาร์ดแวร์ทั้งหมดพร้อมใช้งาน
  - Full support for [Coldcard](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Coldcard Q](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Bitbox02](https://shop.bitbox.swiss/?ref=MOB4dk7gpm), [Blockstream Jade](https://store.blockstream.com/?code=XEocg5boS77D), [Trezor](https://affil.trezor.io/SHtN), [Foundation Passport](https://foundation.xyz/passport), [Keystone](https://keyst.one), [Ledger](https://shop.ledger.com/?r=400f1fff75b5), [Specter DIY](https://clavastack.com/en/?coupon=bitcoin-safe), [SeedSigner](https://seedsigner.com), [Krux](https://selfcustody.github.io/krux), using  *QR*, *USB*, and *SD-card* 
- **ปลอดภัย**: ผู้ลงนามฮาร์ดแวร์เท่านั้น
  - กระเป๋าทั้งหมดต้องใช้ผู้ลงนามฮาร์ดแวร์/กระเป๋าเพื่อการจัดเก็บ seed อย่างปลอดภัย 
  - Powered by **[BDK](https://github.com/bitcoindevkit/bdk)**
- **หลายภาษา**:
  - 🇺🇸 อังกฤษ, 🇨🇳 Chinese - 简体中文, 🇪🇸 สเปน - español de España, 🇯🇵 Japanese - 日本語, 🇷🇺 Russian - русский, 🇵🇹 โปรตุเกส - português europeu, 🇮🇳 Hindi - हिन्दी, Arabic - العربية, 🇮🇹 Italian - italiano, 🇫🇷 French - Français, 🇩🇪 German - Deutsch, 🇲🇲 Burmese - မြန်မာ, 🇰🇷 Korean - 한국어, 🇹🇭 Thai - ภาษาไทย, 🇮🇷 Persian (Farsi) - فارسی, 🇵🇱 Polish - Polski, 🇪🇸 Catalan - Català, (more upon request)
- **ง่ายขึ้น** address labels by using categories (e.g. "KYC", "Non‑KYC", "Work", "Friends", ...)
  - การเลือกสกุลเงินอัตโนมัติภายในหมวดหมู่
  - แผนภาพการไหลของธุรกรรม, แสดงภาพอินพุตและเอาต์พุต, คลิกที่อินพุตและเอาต์พุตเพื่อสืบค้นการไหลของเงิน
- **การส่ง** for non-technical users
  - การเลือกค่าธรรมเนียม 1‑คลิกผ่าน mempool‑blocks
  - การรวม utxos อัตโนมัติเมื่อค่าธรรมเนียมต่ำ
- **ซิงค์ & แชท**:
  - การสำรองคลาวด์เข้ารหัส (ผ่าน nostr) ของป้าย
  - การซิงโครไนซ์ป้ายระหว่างคอมพิวเตอร์ต่างกัน
  - แชทกระเป๋าและการแชร์ PSBT ระหว่างคอมพิวเตอร์ต่างกัน
- **เร็ว**: 
  - การซิงค์เซิร์ฟเวอร์ Electrum
  - การอัปเกรดที่วางแผนสำหรับ **Compact Block Filters** ในการปล่อย Bitcoin Safe 2.0 release


### ฟีเจอร์ครบถ้วน - ง่ายและทรงพลัง

| **ตัวช่วยตั้งค่า Multisig**          | **สร้าง PSBT, ลงนามและส่งต่อ**                     |
|--------------------------------|----------------------------|
| ![](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/multisig-setup.gif) |  ![](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/send.gif) |
| **สำรวจธุรกรรมผ่านแผนภาพ**          | **ค้นหาด้วยการพิมพ์ในทุกกระเป๋า**                    |
| ![](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/explorer.gif) |  ![](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/global-search.gif) |
|   **การซิงโครไนซ์ป้ายอัตโนมัติ**      | **การทำงานร่วมกันหลายฝ่าย Multisig**                  |
| ![](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/label-sync.gif)  |   ![](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/psbt-share.gif) |
|   **หมวดสกุลเงิน**      |                 |
| ![](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/category-drag-and-drop.gif)  |   |


### มีให้บนทุกแพลตฟอร์ม
| ![Windows](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-win.png) | ![Mac OS X](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-mac.png) | ![Linux](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-linux.png) |
|-----------------------------|-----------------------------|----------------------------|
| Windows                    | Mac OS X                   | Linux                     |


## รายการฟีเจอร์โดยละเอียด

- **ความสามารถในการนำเข้าและส่งออก**
  
  - ส่งออก CSV สำหรับรายการทั้งหมด
  - นำเข้า CSV สำหรับธุรกรรมเป็นกลุ่ม
  - นำเข้าและส่งออกป้ายโดยใช้ [BIP329](https://bip329.org/)
  - นำเข้าป้ายจากกระเป๋า Electrum
  - ส่งออกแผนภาพการไหลของเงินเป็น svg
  - ลากและวางสำหรับธุรกรรม, PSBT, และไฟล์ CSV

- **ฟีเจอร์ของกระเป๋า**
  
  - การตั้งป้ายที่อยู่แบบง่ายโดยใช้หมวดหมู่เช่น KYC, Non‑KYC, Work, Friends
  - เพิ่มค่าธรรมเนียมบนธุรกรรม (ผ่าน Replace‑by‑Fee)
  - รับเร็วขึ้น (ผ่าน Child Pays For Parents)
  - การจัดเก็บกระเป๋าแบบเข้ารหัส
  - PDF สำรองพร้อม Descriptor (ข้อความและ QR code)
  - การลงนามข้อความผ่าน USB และ QR

- **การเชื่อมต่อผู้ลงนามฮาร์ดแวร์**
  
  - MicroSD (ไฟล์)
  - USB
  - QR codes (การตรวจจับ QR code ที่เพิ่มขึ้นสำหรับกล้อง Laptop)
  - QR code แบบเคลื่อนไหวรวมถึง [Coldcard/BBQr](https://bbqr.org/) และ [UR](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md) format

- **ตัวเลือกการค้นหาและการกรอง**
  
  - การกรองอย่างรวดเร็วทั่ว txids, utxos, ป้าย, วันที่, จำนวน, หมวดหมู่
  - การค้นหาทั่วทุกกระเป๋าเปิด, txids, utxos, ป้าย, วันที่, จำนวน, หมวดหมู่

- **ภาษา**
  
  - 🇺🇸 อังกฤษ, 🇨🇳 Chinese - 简体中文, 🇪🇸 สเปน - español de España, 🇯🇵 Japanese - 日本語, 🇷🇺 Russian - русский, 🇵🇹 โปรตุเกส - português europeu, 🇮🇳 Hindi - हिन्दी, Arabic - العربية, 🇮🇹 Italian - italiano, 🇫🇷 French - Français, 🇩🇪 German - Deutsch, 🇲🇲 Burmese - မြန်မာ, 🇰🇷 Korean - 한국어, 🇹🇭 Thai - ภาษาไทย, 🇮🇷 Persian (Farsi) - فارسی, 🇵🇱 Polish - Polski, 🇪🇸 Catalan - Català, (more upon request)

- **การสร้าง Transaction / PSBT**
  
  - การเลือกค่าธรรมเนียม 1‑คลิกและการแสดงตัวอย่าง mempool block
  - การรวม utxos อัตโนมัติเมื่อค่าธรรมเนียมต่ำ
  - การไฮไลท์ที่อยู่ของตนเอง 

- **ความปลอดภัยและความน่าเชื่อถือ**
  
  - ไม่มีการสร้างหรือจัดเก็บ seed บน mainnet
  - การจัดเก็บ seed ต้องใช้ผู้ลงนามฮาร์ดแวร์แยก  
  - การแจ้งเตือนอัปเดตและการตรวจสอบลายเซ็น
  - Powered by [Bitcoin Development Kit (BDK)](https://github.com/bitcoindevkit/bdk)

- **ความง่ายในการใช้สำหรับกระเป๋า Multisig**
  
  - การตั้งค่าง่ายสำหรับกระเป๋า multisig, รวมถึงคำแนะนำขั้นตอนต่อขั้นและแผ่นสำรอง PDF
  - การทดสอบการลงนามกับผู้ลงนามฮาร์ดแวร์ทั้งหมด
  - การจัดการกระเป๋าแบบร่วมมือรวมถึงแชทและการแชร์ PSBT ผ่าน nostr และการซิงโครไนซ์ป้ายระหว่างอุปกรณ์ที่เชื่อถือ
  - เซิร์ฟเวอร์ nostr ที่กำหนดเอง (ออปชัน) 

- **ฟีเจอร์ที่กำลังจะมาถึง**
  
  - สำหรับการปล่อย 2.0
    - **Compact Block Filters** โดยค่าเริ่มต้น
      - Compact Block Filters มี **ความเร็ว**และ **ความเป็นส่วนตัว**
      - Compact Block Filters (bdk) are being [worked on](https://github.com/bitcoindevkit/bdk/issues/679), and will be included in bdk 1.1. For now RPC, Electrum and Esplora are available, but will be replaced completely with Compact Block Filters.


## การติดตั้งจาก Git repository


### Ubuntu, Debian

- Install dependencies: 
sudo apt-get install qt6-tools-dev-tools libzbar-dev libxcb-cursor0 '^libqt6.*$'
- Install `poetry` and run `bitcoin_safe`
git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
  pip install poetry  && poetry install && poetry run python -m bitcoin_safe
### Mac

- Clone `bitcoin_safe`
open "/Applications/Python 3.12/Install Certificates.command"
  export SSL_CERT_FILE=$(python3 -m certifi) # to fix ssl errors
  git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
- *ออปชัน*: dependency `zbar`
brew install zbar
- Run `bitcoin_safe`
python3 -m pip install poetry && python3 -m poetry install && python3 -m poetry run python3 -m bitcoin_safe
## การพัฒนา

* Run the precommit manually for debugging
poetry run pre-commit run --all-files
#### สภาพแวดล้อม Regtest Docker พร้อม electrs และ mempool

* install docker
# see https://docs.docker.com/engine/install/ubuntu/
* setting up a regtest environment in docker + mempool instance
curl https://getnigiri.vulpem.com | sudo bash # see https://nigiri.vulpem.com/#install
sudo nigiri start
xdg-open http://localhost:5000/
* This creates
  * esplora localhost:3000
    electrs localhost:50000 
  * and a gui block explorer at http://localhost:5000
* Setup mempool instance
sudo apt install docker-compose
git clone https://github.com/ngutech21/nigiri-mempool.git

pushd nigiri-mempool
sudo docker-compose up -d
sleep 10
# this is needed because the database needs time to start up 
sudo docker-compose up -d
popd
xdg-open http://localhost:8080/

# if the mempool is endlessly loading, then get the debug output with
sudo docker-compose logs -f mempool-api
* this opens a mempool at http://localhost:8080/

#### ควบคุมสภาพแวดล้อม Regtest

* get coins to an address
nigiri rpc generatetoaddress 1 bcrt1qgsnt3d4sny4w4zd5zl9x6jufc5rankqmgphyms9vz0ds73q4xfms655y4c # mine blocks

# or use the internal faucet
nigiri faucet bcrt1qgsnt3d4sny4w4zd5zl9x6jufc5rankqmgphyms9vz0ds73q4xfms655y4c 0.01
### Qt designer

Qt componets can be explored with the qt designer:
virtualenv .env-qt-designer
source .env-qt-designer/bin/activate
pip install pyqt6-tools 
pyqt6-tools designer
## นโยบายการลงนามโค้ด


Free code signing provided by [SignPath.io](https://about.signpath.io/), certificate by [SignPath Foundation](https://signpath.org/)


## นโยบายความเป็นส่วนตัว
This program uses by default
- the electrum/esplora server of [blockstream.com](https://blockstream.com/) to fetch blockchain data
- fetches mempool fee information from [mempool.space](https://mempool.space/)

You can specify your own (personal) server for both in "Network settings".

When enabeling the Sync&Chat feature [default relays](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py) are used to transmit encrypted data to your approved trusted devices. You can specify your own relay(s) in the Sync&Chat settings.

This program will not transfer any other information to other networked systems unless specifically requested by the user or the person installing or operating it.