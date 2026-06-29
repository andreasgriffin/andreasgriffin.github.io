---
aliases:
  - "/uk/features/readme/"
title: "Усі функції"
description: "Розгорнутий огляд більшості функцій Bitcoin Safe"
draft: false
bucket: features
images: ["logo.png"]
keywords: [
  "Bitcoin Safe",
  "bitcoin savings wallet",
  "MultiSig wallet",
  "Multisig setup wizard",
  "hardware signers",
  "secure seed storage",
  "Coldcard",
  "Coldcard Q",
  "Bitbox02",
  "Blockstream Jade",
  "Trezor",
  "Foundation Passport Core",
  "Keystone",
  "Ledger",
  "Specter DIY",
  "BDK",
  "multi-language support",
  "address labeling",
  "transaction flow diagrams",
  "PSBT",
  "fee selection",
  "mempool",
  "Electrum server",
  "Compact Block Filters",
  "CSV export",
  "CSV import",
  "BIP329",
  "drag and drop",
  "Replace-by-Fee",
  "backup PDF",
  "message signing",
  "MicroSD",
  "USB",
  "QR codes",
  "animated QR codes",
  "search and filtering",
  "wallet chat",
  "label synchronization",
  "regtest",
  "Docker",
  "Nigiri",
  "cross-platform",
  "installation",
  "development"
]
weight: -10
---
<!-- header-end -->
# Bitcoin Safe

#### Біткоїн‑гаманець для заощаджень усієї родини

- **Просте** налаштування мультисиг‑гаманця
  - Покрокові інструкції для безпечного налаштування MultiSig з PDF‑аркушами резервного копіювання
  - Тестові транзакції гарантують готовність усіх апаратних підписувачів
  - Повна підтримка [Coldcard](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Coldcard Q](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Bitbox02](https://shop.bitbox.swiss/?ref=MOB4dk7gpm), [Blockstream Jade](https://store.blockstream.com/?code=XEocg5boS77D), [Trezor](https://affil.trezor.io/SHtNo), [Foundation Passport Core](https://foundation.xyz/?ref=cbyqjjxumy), [Keystone](https://keyst.one), [Ledger](https://shop.ledger.com/?r=400f1fff75b5), [Specter DIY](https://clavastack.com/en/?coupon=bitcoin-safe), [SeedSigner](https://seedsigner.com), [Krux](https://selfcustody.github.io/krux), з використанням *QR*, *USB* та *SD‑картки*
- **Безпека**: лише апаратні підписувачі
  - Усі гаманці потребують апаратних підписувачів/гаманців для безпечного зберігання сідів
  - Працює на **[BDK](https://github.com/bitcoindevkit/bdk)**
- **Багатомовність**:
  - 🇺🇸 English, 🇨🇳 Chinese – 简体中文, 🇪🇸 Spanish – español de España, 🇯🇵 Japanese – 日本語, 🇷🇺 Russian – русский, 🇵🇹 Portuguese – português europeo, 🇧🇷 Portuguese (Brazil) – português do Brasil, 🇮🇳 Hindi – हिन्दी, 🇦🇪 Arabic – العربية, 🇮🇹 Italian – italiano, 🇫🇷 French – Français, 🇩🇪 German – Deutsch, 🇲🇲 Burmese – မြန်မာ, 🇰🇷 Korean – 한국어, 🇹🇭 Thai – ภาษาไทย, 🇮🇷 Persian (Farsi) – فارسی, 🇵🇱 Polish – Polski, 🇪🇸 Catalan – Català, 🇮🇩 Indonesian – Bahasa Indonesia, 🇹🇷 Turkish – Türkçe, 🇺🇦 Ukrainian – Українська (more upon request)
- **Простіші** мітки адрес через категорії (наприклад, "KYC", "Non-KYC", "Work", "Friends", ...)
  - Автоматичний вибір монет у межах категорій
  - Діаграми потоку транзакцій, що візуалізують входи й виходи; натисніть на вхід/вихід, щоб простежити рух коштів
- **Надсилання** для нетехнічних користувачів
  - Вибір комісії одним кліком через блоки mempool
  - Автоматичне об’єднання UTXO, коли комісії низькі
- **Sync & Chat**:
  - Зашифроване хмарне резервне копіювання міток (через nostr)
  - Синхронізація міток між різними комп’ютерами
  - Чат гаманця й обмін PSBT між різними комп’ютерами
- **Швидко**: 
  - Electrum/Esplora сервер
  - Compact Block Filters 



### Доступно на всіх платформах
| ![Windows](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-win.png) | ![Mac OS X](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-mac.png) | ![Linux](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-linux.png) |
|-----------------------------|-----------------------------|----------------------------|
| Windows                    | Mac OS X                   | Linux                     |


## Повний список функцій

- **Можливості імпорту та експорту**
  
  - Експорт CSV для всіх списків
  - Імпорт CSV для пакетних транзакцій
  - Імпорт та експорт міток за стандартом [BIP329](https://bip329.org/)
  - Імпорт міток із гаманця Electrum
  - Експорт діаграми руху коштів у SVG
  - Drag & drop для транзакцій, PSBT та CSV‑файлів

- **Функції гаманця**
  
  - Спрощене маркування адрес через категорії на кшталт KYC, Non‑KYC, Work, Friends
  - Підвищення комісії для транзакцій (Replace‑by‑Fee)
  - Швидше отримання (Child Pays For Parents)
  - Зашифроване сховище гаманця
  - Резервний PDF з дескриптором (текст і QR‑код)
  - Підписання повідомлень через USB і QR

- **Підключення апаратних підписувачів**
  
  - MicroSD (файли)
  - USB
  - QR‑коди (покращене розпізнавання QR для камер ноутбуків)
  - Анімовані QR‑коди, включно з [Coldcard/BBQr](https://bbqr.org/) та форматом [UR](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md)

- **Пошук і фільтри**
  
  - Швидке фільтрування за txid, utxo, мітками, датами, сумами, категоріями
  - Пошук у всіх відкритих гаманцях за txid, utxo, мітками, датами, сумами, категоріями

- **Мови**
  
  - 🇺🇸 English, 🇨🇳 Chinese – 简体中文, 🇪🇸 Spanish – español de España, 🇯🇵 Japanese – 日本語, 🇷🇺 Russian – русский, 🇵🇹 Portuguese – português europeo, 🇧🇷 Portuguese (Brazil) – português do Brasil, 🇮🇳 Hindi – हिन्दी, 🇦🇪 Arabic – العربية, 🇮🇹 Italian – italiano, 🇫🇷 French – Français, 🇩🇪 German – Deutsch, 🇲🇲 Burmese – မြန်မာ, 🇰🇷 Korean – 한국어, 🇹🇭 Thai – ภาษาไทย, 🇮🇷 Persian (Farsi) – فارسی, 🇵🇱 Polish – Polski, 🇪🇸 Catalan – Català, 🇮🇩 Indonesian – Bahasa Indonesia, 🇹🇷 Turkish – Türkçe, 🇺🇦 Ukrainian – Українська (more upon request)

- **Створення транзакцій / PSBT**
  
  - Вибір комісії одним кліком і попередній перегляд блоків mempool
  - Автоматичне об’єднання UTXO, коли комісії низькі
  - Підсвічування власних адрес 
  - Виявлення й попередження про отруєння адреси

- **Безпека та надійність**
  
  - Жодного створення чи зберігання сідів у mainnet
  - Зберігання сідів потребує окремого апаратного підписувача  
  - Сповіщення про оновлення та перевірка підписів
  - Працює на [Bitcoin Development Kit (BDK)](https://github.com/bitcoindevkit/bdk)

- **Зручність для мультисиг‑гаманців**
  
  - Спрощене налаштування мультисиг‑гаманців, включно з покроковими інструкціями та PDF‑аркушем резервної копії
  - Тестове підписання з усіма апаратними підписувачами
  - Спільне керування гаманцем, включно з чатом і обміном PSBT через nostr та синхронізацією міток між довіреними пристроями
  - Необов’язковий власний сервер nostr 

- **Швидка синхронізація**: 
  - Electrum/Esplora сервер
  - Compact Block Filters 


## Встановлення з Git‑репозиторію


### Ubuntu, Debian

- Встановіть залежності: 

  ```sh
  sudo apt-get install qt6-tools-dev-tools libzbar-dev libxcb-cursor0 '^libqt6.*$' 
  ```

- Встановіть `poetry` і запустіть `bitcoin_safe`
  
  ```sh
  git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
  pip install poetry  && poetry install && poetry run python -m bitcoin_safe
  ```

### Mac

- Клонуйте `bitcoin_safe`
  
  ```sh
  open "/Applications/Python 3.12/Install Certificates.command"
  export SSL_CERT_FILE=$(python3 -m certifi) # to fix ssl errors
  git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
  ```
 


- *Необов’язково*: залежність `zbar`
  ```sh 
  brew install zbar  
  ``` 
  
- Запустіть `bitcoin_safe`
  
  ```sh 
  python3 -m pip install poetry && python3 -m poetry install && python3 -m poetry run python3 -m bitcoin_safe
  ```

## Розробка

* Запустити pre-commit вручну для налагодження

```shell
poetry run pre-commit run --all-files
```

#### Docker‑середовище regtest з electrs і mempool

* встановіть docker

```shell
# див. https://docs.docker.com/engine/install/ubuntu/
```

* налаштування regtest‑середовища в docker + інстанс mempool

```shell
curl https://getnigiri.vulpem.com | sudo bash # див. https://nigiri.vulpem.com/#install
sudo nigiri start
xdg-open http://localhost:5000/
```

* Це створює
  * esplora localhost:3000
    electrs localhost:50000 
  * а також GUI‑оглядач блоків на http://localhost:5000
* Налаштування інстансу mempool

```shell
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
```

* це відкриє mempool за адресою http://localhost:8080/

#### Керування середовищем regtest

* отримати монети на адресу

```shell
nigiri rpc generatetoaddress 1 bcrt1qgsnt3d4sny4w4zd5zl9x6jufc5rankqmgphyms9vz0ds73q4xfms655y4c # mine blocks

# or use the internal faucet
nigiri faucet bcrt1qgsnt3d4sny4w4zd5zl9x6jufc5rankqmgphyms9vz0ds73q4xfms655y4c 0.01
```

<!-- * ## Installation from PyPi

### Ubuntu, Debian, Windows

- Install `poetry` and run `bitcoin_safe`
  
  ```sh
  pip install bitcoin-safe
  python -m bitcoin_safe
  ```

### Mac

- Run `bitcoin_safe`
  
  ```sh
  python3 -m pip install bitcoin-safe
  python3 -m bitcoin_safe
  ``` -->




### Перевірка бінарних файлів

- У Linux хеші appimage і deb повинні точно збігатися з вашою власною збіркою.
- Файли Windows exe підписані, тому підпис потрібно видалити. 
```sh
osslsigncode remove-signature -in signed-binary.exe -out binary-stripped.exe
```
`binary-stripped.exe` має збігатися за хешем із вашою збіркою.




### Qt designer

Компоненти Qt можна переглядати у qt designer:

```sh
virtualenv .env-qt-designer
source .env-qt-designer/bin/activate
pip install pyqt6-tools 
pyqt6-tools designer 
```



## Політика підпису коду


Безкоштовний підпис коду надається [SignPath.io](https://about.signpath.io/), сертифікат від [SignPath Foundation](https://signpath.org/)


## Політика конфіденційності
Ця програма за замовчуванням
- використовує сервер electrum/esplora від [blockstream.com](https://blockstream.com/) для отримання даних блокчейну
- отримує інформацію про комісії мемпулу з [mempool.space](https://mempool.space/)

Ви можете вказати власний (персональний) сервер для обох у "Налаштуваннях мережі".

Під час увімкнення функції Sync&Chat використовуються [релеи за замовчуванням](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py) для передавання зашифрованих даних на ваші довірені пристрої. Ви можете вказати власні релеї в налаштуваннях Sync&Chat.

Ця програма не передає іншу інформацію в інші мережеві системи, якщо це не запитано користувачем або особою, яка встановлює чи використовує її.
