---
title: "모든 기능"
description: "Bitcoin Safe의 대부분 기능에 대한 포괄적인 개요"
draft: false
tags: [ "Features" ]
images: ["logo.png"]
keywords: [
  "Bitcoin Safe",
  "비트코인 저축 지갑",
  "멀티시그 지갑",
  "멀티시그 설정 마법사",
  "하드웨어 서명기",
  "보안 시드 저장",
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
  "다국어 지원",
  "주소 라벨링",
  "거래 흐름 다이어그램",
  "PSBT",
  "수수료 선택",
  "mempool",
  "Electrum server",
  "Compact Block Filters",
  "CSV export",
  "CSV import",
  "BIP329",
  "드래그 앤 드롭",
  "Replace-by-Fee",
  "백업 PDF",
  "메시지 서명",
  "MicroSD",
  "USB",
  "QR codes",
  "animated QR codes",
  "검색 및 필터링",
  "지갑 채팅",
  "라벨 동기화",
  "regtest",
  "Docker",
  "Nigiri",
  "크로스 플랫폼",
  "설치",
  "개발"
]
weight: -10
---
<!-- header-end -->
# Bitcoin Safe

#### 전체 가족을 위한 비트코인 저축 지갑

- **쉬움** Multisig-Wallet Setup
  - 보안 멀티시그 설정을 위한 단계별 안내와 PDF 백업 시트
  - 테스트 거래를 통해 모든 하드웨어 서명기가 준비되었는지 확인
  - Full support for [Coldcard](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Coldcard Q](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Bitbox02](https://shop.bitbox.swiss/?ref=MOB4dk7gpm), [Blockstream Jade](https://store.blockstream.com/?code=XEocg5boS77D), [Trezor](https://affil.trezor.io/SHtN), [Foundation Passport](https://foundation.xyz/passport), [Keystone](https://keyst.one), [Ledger](https://shop.ledger.com/?r=400f1fff75b5), [Specter DIY](https://clavastack.com/en/?coupon=bitcoin-safe), [SeedSigner](https://seedsigner.com), [Krux](https://selfcustody.github.io/krux), using  *QR*, *USB*, and *SD-card* 
- **보안**: Hardware signers only
  - All wallets require hardware signers/wallets for safe seed storage 
  - Powered by **[BDK](https://github.com/bitcoindevkit/bdk)**
- **다국어 지원**:
  - 🇺🇸 English, 🇨🇳 Chinese - 简体中文, 🇪🇸 Spanish - español de España, 🇯🇵 Japanese - 日本語, 🇷🇺 Russian - русский, 🇵🇹 Portuguese - português europeu, 🇮🇳 Hindi - हिन्दी, Arabic - العربية, 🇮🇹 Italian - italiano, 🇫🇷 French - Français, 🇩🇪 German - Deutsch, 🇲🇲 Burmese - မြန်မာ, 🇰🇷 Korean - 한국어, 🇹🇭 Thai - ภาษาไทย,  🇮🇷 Persian (Farsi) - فارسی, 🇵🇱 Polish - Polski, 🇪🇸 Catalan - Català, (more upon request)
- **간단한** address labels by using categories (e.g. "KYC", "Non-KYC", "Work", "Friends", ...)
  - Automatic coin selection within categories
  - Transaction flow diagrams, visualizing inputs and outputs, click on inputs and output to trace the money flow
- **보내기** for non-technical users
  - 1-click fee selection via mempool-blocks
  - Automatic merging of utxos when fees are low
- **동기화 및 채팅**:
  - Encrypted cloud backup (via nostr) of labels
  - Label synchronization between different computers
  - Wallet chat and PSBTs sharing between different computers
- **빠름**: 
  - Electrum server syncing
  - planned upgrade to **Compact Block Filters** for the Bitcoin Safe 2.0 release




### 완전 기능 - 쉬우면서 강력함

| **멀티시그 설정 마법사**          | **PSBT 생성, 서명 및 전송**                     |
|--------------------------------|----------------------------|
| ![Multisig setup](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/multisig-setup.gif) |  ![Send transaction](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/send.gif) |
| **다이어그램을 통한 거래 탐색**          | **전체 지갑에서 타이프-검색**                    |
| ![Explorer](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/explorer.gif) |  ![Global search](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/global-search.gif) |
|   **자동 라벨 동기화**      | **다중 파티 멀티시그 협업**                  |
| ![Label sync](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/label-sync.gif)  |   ![PSBT share](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/psbt-share.gif) |
|   **코인 카테고리**      |                 |
| ![Category drag and drop](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/category-drag-and-drop.gif)  |   |



### Available on all platforms
| ![Windows](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-win.png) | ![Mac OS X](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-mac.png) | ![Linux](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-linux.png) |
|-----------------------------|-----------------------------|----------------------------|
| Windows                    | Mac OS X                   | Linux                     |


## 포괄적인 기능 목록

- **가져오기 및 내보내기 기능**
  
  - CSV export for all lists
  - CSV import for batch transactions
  - Label import and export using [BIP329](https://bip329.org/)
  - Label import from Electrum wallet
  - Export of the money flow diagram to svg
  - Drag and drop for Transactions, PSBTs, and CSV files

- **지갑 기능**
  
  - Simplified address labeling using categories like KYC, Non-KYC, Work, Friends
  - Bump fee on transactions (via Replace-by-Fee)
  - Receive faster (via Child Pays For Parents)
  - Encrypted wallet storage
  - Backup PDF with Descriptor (Text and QR code)
  - Message signing via USB and QR

- **하드웨어 서명기 연결**
  
  - MicroSD (files)
  - USB
  - QR codes (enhanced QR code detection for Laptop cameras)
  - Animated QR codes including [Coldcard/BBQr](https://bbqr.org/) and [UR](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md) format

- **검색 및 필터링 옵션**
  
  - Fast filtering across txids, utxos, labels, dates, amounts, categories
  - Search across all open wallets, txids, utxos, labels, dates, amounts, categories

- **언어**
  
  - 🇺🇸 English, 🇨🇳 Chinese - 简体中文, 🇪🇸 Spanish - español de España, 🇯🇵 Japanese - 日本語, 🇷🇺 Russian - русский, 🇵🇹 Portuguese - português europeu, 🇮🇳 Hindi - हिन्दी, Arabic - العربية, 🇮🇹 Italian - italiano, 🇫🇷 French - Français, 🇩🇪 German - Deutsch, 🇲🇲 Burmese - မြန်မာ, 🇰🇷 Korean - 한국어, 🇹🇭 Thai - ภาษาไทย, 🇮🇷 Persian (Farsi) - فارسی, 🇵🇱 Polish - Polski, 🇪🇸 Catalan - Català, (more upon request)

- **거래 / PSBT 생성**
  
  - 1-click fee selection and mempool block preview
  - Automatic merging of utxos when fees are low
  - Highlighting of own addresses 

- **보안 및 신뢰성**
  
  - No seed generation or storage on mainnet
  - Seed storage requires a separate hardware signer  
  - Update notifications and signature verification
  - Powered by [Bitcoin Development Kit (BDK)](https://github.com/bitcoindevkit/bdk)

- **멀티시그 지갑 사용 용이성**
  
  - Simplified setup for multisig wallets, including step-by-step instructions and PDF backup sheet
  - Test signing with all hardware signers
  - Collaborative wallet management including chat and PSBT sharing via nostr and label synchronization between trusted devices
  - Optional custom nostr server 

- **예정 기능**
  
  - For the 2.0 Release
    - **Compact Block Filters** by default
      - Compact Block Filters are **fast** and **private**
      - Compact Block Filters (bdk) are being [worked on](https://github.com/bitcoindevkit/bdk/issues/679), and will be included in bdk 1.1. For now RPC, Electrum and Esplora are available, but will be replaced completely with Compact Block Filters.


## Git 저장소에서 설치


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
- *Optional*: dependency `zbar`
brew install zbar
- Run `bitcoin_safe`
python3 -m pip install poetry && python3 -m poetry install && python3 -m poetry run python3 -m bitcoin_safe
## Development

* Run the precommit manually for debugging
poetry run pre-commit run --all-files
#### Regtest docker environement with electrs and mempool

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

#### Control the Regtest environment

* get coins to an address
nigiri rpc generatetoaddress 1 bcrt1qgsnt3d4sny4w4zd5zl9x6jufc5rankqmgphyms9vz0ds73q4xfms655y4c # mine blocks

# or use the internal faucet
nigiri faucet bcrt1qgsnt3d4sny4w4zd5zl9x6jufc5rankqmgphyms9vz0ds73q4xfms655y4c 0.01
<!-- * ## Installation from PyPi

### Ubuntu, Debian, Windows

- Install `poetry` and run `bitcoin_safe`
pip install bitcoin-safe
  python -m bitcoin_safe
### Mac

- Run `bitcoin_safe`
python3 -m pip install bitcoin-safe
  python3 -m bitcoin_safe
-->

### Qt designer

Qt componets can be explored with the qt designer:
virtualenv .env-qt-designer
source .env-qt-designer/bin/activate
pip install pyqt6-tools 
pyqt6-tools designer
## Code signing policy


Free code signing provided by [SignPath.io](https://about.signpath.io/), certificate by [SignPath Foundation](https://signpath.org/)


## 개인정보 보호정책
This program uses by default
- the electrum/esplora server of [blockstream.com](https://blockstream.com/) to fetch blockchain data
- fetches mempool fee information from [mempool.space](https://mempool.space/)

You can specify your own (personal) server for both in "Network settings".

When enabeling the Sync&Chat feature [default relays](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py) are used to transmit encrypted data to your approved trusted devices. You can specify your own relay(s) in the Sync&Chat settings.

This program will not transfer any other information to other networked systems unless specifically requested by the user or the person installing or operating it.