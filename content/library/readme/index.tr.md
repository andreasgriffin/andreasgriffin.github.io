---
aliases:
  - "/tr/features/readme/"
title: "Tum ozellikler"
description: "Bitcoin-Safe'deki ozelliklerin buyuk bolumu icin kapsamli genel bakis"
draft: false
bucket: features
images: ["logo.png"]
keywords: [
  "Bitcoin-Safe",
  "bitcoin tasarruf cuzdanı",
  "MultiSig cuzdan",
  "multisig kurulum sihirbazi",
  "hardware signer",
  "compact block filters",
  "etiket senkronizasyonu",
  "islem akis diyagramlari",
  "coklu platform",
  "gelistirme"
]
weight: -10
---
<!-- header-end -->
# Bitcoin-Safe

#### Tum aile icin bir bitcoin tasarruf cuzdanı

- **Kolay multisig cüzdan kurulumu**
  - PDF yedek sayfalariyla guvenli MultiSig kurulumu icin adim adim yonlendirme
  - Test islemleri, tum hardware signer'larin hazir oldugunu dogrular
  - Coldcard, BitBox02, Jade, Trezor, Passport, Keystone, Ledger, Specter, SeedSigner, Krux ve daha fazlasi icin *QR*, *USB* ve *SD kart* destegi
- **Guvenli**
  - Mainnet cüzdanlari, seed saklamayi guvenli tutmak icin hardware signer kullanir
  - **[BDK](https://github.com/bitcoindevkit/bdk)** ile guclendirilir
- **Hizli ve ozel**
  - Electrum/Esplora ile senkronizasyon
  - Daha ozel senkronizasyon icin [Compact Block Filters](https://bitcoin-safe.org/tr/library/compact-block-filters/)
- **Gunluk kullanim icin duzenli**
  - Adres kategorileri ve etiketler wallet yonetimini kolaylastirir
  - Islem akis diyagramlari girdileri ve ciktiklari takip etmeyi kolaylastirir
  - Tek tikla ucret secimi gonderimi basitlestirir
- **Is birligine uygun**
  - Guvenilen bilgisayarlar arasinda etiket senkronizasyonu
  - Sync & Chat eklentisi ile wallet sohbeti ve PSBT paylasimi

### Tum platformlarda mevcut
| ![Windows](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-win.png) | ![Mac OS X](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-mac.png) | ![Linux](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-linux.png) |
|-----------------------------|-----------------------------|----------------------------|
| Windows                    | Mac OS X                   | Linux                     |

## Ozellik ozetleri

- **Ice ve disa aktarma**
  - Listeler ve gecmis icin CSV disa aktarma
  - Toplu islemler icin CSV ice aktarma
  - [BIP329](https://bip329.org/) ile etiket ice/disa aktarma
- **Cuzdan ozellikleri**
  - KYC, Non-KYC, Work, Friends gibi kategoriler
  - Replace-by-Fee ve Child Pays For Parents
  - Sifrelenmis cüzdan depolamasi
  - Descriptor iceren PDF yedekleri
- **Hardware signer baglantilari**
  - MicroSD, USB, QR ve animasyonlu QR
- **Arama ve filtreleme**
  - txid, UTXO, etiket, tarih, tutar ve kategorilerde hizli filtreleme
  - Acik tum cüzdanlarda arama
- **Multisig**
  - Basitlestirilmis kurulum, test imzalama ve uzaktan is birligi

## Git deposundan kurulum

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
