---
aliases:
  - "/id/features/readme/"
title: "Semua fitur"
description: "Gambaran menyeluruh tentang sebagian besar fitur di Bitcoin-Safe"
draft: false
bucket: features
images: ["logo.png"]
keywords: [
  "Bitcoin-Safe",
  "dompet tabungan bitcoin",
  "wallet MultiSig",
  "panduan setup multisig",
  "hardware signer",
  "compact block filters",
  "sinkronisasi label",
  "diagram aliran transaksi",
  "lintas platform",
  "pengembangan"
]
weight: -10
---
<!-- header-end -->
# Bitcoin-Safe

#### Dompet tabungan bitcoin untuk seluruh keluarga

- **Setup wallet multisig yang mudah**
  - Panduan langkah demi langkah untuk setup MultiSig yang aman dengan lembar cadangan PDF
  - Transaksi uji membantu memastikan semua hardware signer siap digunakan
  - Dukungan luas untuk Coldcard, BitBox02, Jade, Trezor, Passport, Keystone, Ledger, Specter, SeedSigner, Krux, dan lainnya melalui *QR*, *USB*, dan *SD-card*
- **Aman**
  - Wallet di mainnet bergantung pada hardware signer untuk penyimpanan seed yang aman
  - Dibangun di atas **[BDK](https://github.com/bitcoindevkit/bdk)**
- **Cepat dan privat**
  - Sinkronisasi melalui Electrum/Esplora
  - [Compact Block Filters](https://bitcoin-safe.org/id/library/compact-block-filters/) untuk sinkronisasi yang lebih privat
- **Rapi untuk penggunaan sehari-hari**
  - Kategori alamat dan label memudahkan pengelolaan wallet
  - Diagram aliran transaksi membantu menelusuri input dan output
  - Pemilihan biaya satu klik mempermudah pengiriman
- **Kolaboratif**
  - Sinkronisasi label antar komputer tepercaya
  - Chat wallet dan berbagi PSBT melalui plugin Sync & Chat

### Tersedia di semua platform
| ![Windows](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-win.png) | ![Mac OS X](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-mac.png) | ![Linux](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-linux.png) |
|-----------------------------|-----------------------------|----------------------------|
| Windows                    | Mac OS X                   | Linux                     |

## Sorotan fitur

- **Impor dan ekspor**
  - Ekspor CSV untuk daftar dan riwayat
  - Impor CSV untuk transaksi batch
  - Impor dan ekspor label dengan [BIP329](https://bip329.org/)
- **Fitur wallet**
  - Kategori seperti KYC, Non-KYC, Work, Friends
  - Replace-by-Fee dan Child Pays For Parents
  - Penyimpanan wallet terenkripsi
  - Cadangan PDF dengan descriptor
- **Konektivitas hardware signer**
  - MicroSD, USB, QR, dan animated QR
- **Pencarian dan filter**
  - Filter cepat untuk txid, UTXO, label, tanggal, jumlah, dan kategori
  - Pencarian di semua wallet yang sedang terbuka
- **Multisig**
  - Setup yang disederhanakan, pengujian penandatanganan, dan kolaborasi jarak jauh

## Instalasi dari repositori Git

### Ubuntu, Debian

```sh
sudo apt-get install qt6-tools-dev-tools libzbar-dev libxcb-cursor0 '^libqt6.*$'
git clone https://github.com/andreasgriffin/bitcoin-safe.git
cd bitcoin-safe
pip install poetry && poetry install && poetry run python -m bitcoin_safe
```

### macOS

```sh
open "/Applications/Python 3.12/Install Certificates.command"
export SSL_CERT_FILE=$(python3 -m certifi)
git clone https://github.com/andreasgriffin/bitcoin-safe.git
cd bitcoin-safe
brew install zbar
python3 -m pip install poetry && python3 -m poetry install && python3 -m poetry run python3 -m bitcoin_safe
```
