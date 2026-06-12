---
title: "Все функции"
description: "Полный обзор большинства функций Bitcoin Safe"
draft: false
tags: [ "Features" ]
images: ["logo.png"]
keywords: [
  "Bitcoin Safe",
  "кошелёк для накоплений в биткоинах",
  "мультисиг-кошелёк",
  "мастер установки multisig",
  "аппаратные подписыватели",
  "безопасное хранение сидов",
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
  "поддержка нескольких языков",
  "маркировка адресов",
  "диаграммы потоков транзакций",
  "PSBT",
  "выбор комиссии",
  "mempool",
  "Electrum server",
  "Compact Block Filters",
  "экспорт CSV",
  "импорт CSV",
  "BIP329",
  "перетаскивание",
  "Replace-by-Fee",
  "PDF-резервная копия",
  "подпись сообщений",
  "MicroSD",
  "USB",
  "QR-коды",
  "анимированные QR-коды",
  "поиск и фильтрация",
  "чат кошелька",
  "синхронизация меток",
  "regtest",
  "Docker",
  "Nigiri",
  "кроссплатформенность",
  "установка",
  "разработка"
]
weight: -10
---
<!-- header-end -->
# Bitcoin Safe

#### Кошелёк для накоплений в биткоинах для всей семьи

- **Простая** настройка Multisig-кошелька
  - Пошаговые инструкции для безопасной MultiSig-настройки с PDF-листами для резервного копирования
  - Тестовые транзакции гарантируют, что все аппаратные подписыватели готовы
  - Полная поддержка [Coldcard](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Coldcard Q](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Bitbox02](https://shop.bitbox.swiss/?ref=MOB4dk7gpm), [Blockstream Jade](https://store.blockstream.com/?code=XEocg5boS77D), [Trezor](https://affil.trezor.io/SHtN), [Foundation Passport Core](https://foundation.xyz/?ref=cbyqjjxumy), [Keystone](https://keyst.one), [Ledger](https://shop.ledger.com/?r=400f1fff75b5), [Specter DIY](https://clavastack.com/en/?coupon=bitcoin-safe), [SeedSigner](https://seedsigner.com), [Krux](https://selfcustody.github.io/krux), с использованием *QR*, *USB* и *SD-карты*
- **Безопасно**: только аппаратные подписыватели
  - Все кошельки требуют аппаратных подписывателей/устройств для безопасного хранения сидов
  - Работает на базе **[BDK](https://github.com/bitcoindevkit/bdk)**
- **Многоязычность**:
  - 🇺🇸 English, 🇨🇳 Chinese - 简体中文, 🇪🇸 Spanish - español de España, 🇯🇵 Japanese - 日本語, 🇷🇺 Russian - русский, 🇵🇹 Portuguese - português europeu, 🇮🇳 Hindi - हिन्दी, Arabic - العربية, 🇮🇹 Italian - italiano, 🇫🇷 French - Français, 🇩🇪 German - Deutsch, 🇲🇲 Burmese - မြန်မာ, 🇰🇷 Korean - 한국어, 🇹🇭 Thai - ภาษาไทย,  🇮🇷 Persian (Farsi) - فارسی, 🇵🇱 Polish - Polski, 🇪🇸 Catalan - Català, (еще по запросу)
- **Упрощённая** маркировка адресов с использованием категорий (например: "KYC", "Non-KYC", "Работа", "Друзья", ...)
  - Автоматический выбор монет внутри категорий
  - Диаграммы потоков транзакций, которые визуализируют входы и выходы; щёлкните по входам и выходам, чтобы отследить движение средств
- **Отправка** для нетехнических пользователей
  - Выбор комиссии в один клик с использованием mempool-blocks
  - Автоматическое объединение UTXO, когда комиссии низкие
- **Синхронизация и чат**:
  - Зашифрованное облачное резервное копирование (через nostr) меток
  - Синхронизация меток между разными компьютерами
  - Чат кошелька и обмен PSBT между разными компьютерами
- **Быстро**:
  - Синхронизация через Electrum-сервер
  - Планируемое обновление до **Compact Block Filters** в релизе Bitcoin Safe 2.0




### Полный набор функций — просто и мощно

| **Мастер настройки Multisig**          | **Создать PSBT, подписать и отправить**                     |
|--------------------------------|----------------------------|
| ![Multisig setup](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/multisig-setup.gif) |  ![Send transaction](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/send.gif) |
| **Исследование транзакции через диаграмму**          | **Поиск по набору символов во всех кошельках**                    |
| ![Explorer](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/explorer.gif) |  ![Global search](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/global-search.gif) |
|   **Автоматическая синхронизация меток**      | **Совместная работа над мультиподписными кошельками**                  |
| ![Label sync](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/label-sync.gif)  |   ![PSBT share](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/psbt-share.gif) |
|   **Категории монет**      |                 |
| ![Category drag and drop](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/category-drag-and-drop.gif)  |   |



### Доступно на всех платформах
| ![Windows](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-win.png) | ![Mac OS X](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-mac.png) | ![Linux](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-linux.png) |
|-----------------------------|-----------------------------|----------------------------|
| Windows                    | Mac OS X                   | Linux                     |


## Полный список функций

- **Импорт и экспорт**
  
  - Экспорт в CSV для всех списков
  - Импорт CSV для пакетных транзакций
  - Импорт и экспорт меток через [BIP329](https://bip329.org/)
  - Импорт меток из кошелька Electrum
  - Экспорт диаграммы потока денег в SVG
  - Перетаскивание для транзакций, PSBT и CSV-файлов

- **Функции кошелька**
  
  - Упрощённая маркировка адресов с использованием категорий, таких как KYC, Non-KYC, Работа, Друзья
  - Увеличение комиссии для транзакций (Replace-by-Fee)
  - Ускоренный приём (через Child Pays For Parents)
  - Зашифрованное хранение кошельков
  - Резервный PDF с дескриптором (текст и QR-код)
  - Подпись сообщений через USB и QR

- **Подключение аппаратных подписывателй**
  
  - MicroSD (файлы)
  - USB
  - QR-коды (улучшенное распознавание QR-кодов камерами ноутбуков)
  - Анимированные QR-коды, включая [Coldcard/BBQr](https://bbqr.org/) и формат [UR](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md)

- **Поиск и фильтрация**
  
  - Быстрая фильтрация по txid, utxo, меткам, датам, суммам, категориям
  - Поиск по всем открытым кошелькам: txid, utxo, метки, даты, суммы, категории

- **Языки**
  
  - 🇺🇸 English, 🇨🇳 Chinese - 简体中文, 🇪🇸 Spanish - español de España, 🇯🇵 Japanese - 日本語, 🇷🇺 Russian - русский, 🇵🇹 Portuguese - português europeu, 🇮🇳 Hindi - हिन्दी, Arabic - العربية, 🇮🇹 Italian - italiano, 🇫🇷 French - Français, 🇩🇪 German - Deutsch, 🇲🇲 Burmese - မြန်မာ, 🇰🇷 Korean - 한국어, 🇹🇭 Thai - ภาษาไทย, 🇮🇷 Persian (Farsi) - فارسی, 🇵🇱 Polish - Polski, 🇪🇸 Catalan - Català, (еще по запросу)

- **Создание транзакций / PSBT**
  
  - Выбор комиссии в один клик и предварительный просмотр по блокам mempool
  - Автоматическое объединение UTXO, когда комиссии низкие
  - Подсветка собственных адресов

- **Безопасность и надёжность**
  
  - Нет генерации или хранения сидов в mainnet
  - Хранение сидов требует отдельного аппаратного подписывателя
  - Уведомления об обновлениях и проверка подписей
  - Работает на базе [Bitcoin Development Kit (BDK)](https://github.com/bitcoindevkit/bdk)

- **Удобство использования для Multisig-кошельков**
  
  - Упрощённая настройка multisig-кошельков, включая пошаговые инструкции и PDF-листы для резервного копирования
  - Тестовая подпись со всеми аппаратными подписывателями
  - Совместное управление кошельком: чат и обмен PSBT через nostr и синхронизация меток между доверенными устройствами
  - Опциональный собственный nostr-сервер

- **Будущие функции**
  
  - Для релиза 2.0
    - **Compact Block Filters** по умолчанию
      - Compact Block Filters — **быстрые** и **приватные**
      - Compact Block Filters (bdk) сейчас [разрабатываются](https://github.com/bitcoindevkit/bdk/issues/679) и будут включены в bdk 1.1. Пока доступны RPC, Electrum и Esplora, но они будут полностью заменены Compact Block Filters.


## Установка из Git-репозитория


### Ubuntu, Debian

- Установите зависимости: 
sudo apt-get install qt6-tools-dev-tools libzbar-dev libxcb-cursor0 '^libqt6.*$'
- Установите `poetry` и запустите `bitcoin_safe`
git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
  pip install poetry  && poetry install && poetry run python -m bitcoin_safe
### Mac

- Клонируйте `bitcoin_safe`
open "/Applications/Python 3.12/Install Certificates.command"
  export SSL_CERT_FILE=$(python3 -m certifi) # to fix ssl errors
  git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
- *Опционально*: зависимость `zbar`
brew install zbar
- Запустите `bitcoin_safe`
python3 -m pip install poetry && python3 -m poetry install && python3 -m poetry run python3 -m bitcoin_safe
## Разработка

* Запустите precommit вручную для отладки
poetry run pre-commit run --all-files
#### Regtest Docker окружение с electrs и mempool

* установите Docker
# see https://docs.docker.com/engine/install/ubuntu/
* настройка regtest-окружения в Docker + инстанс mempool
curl https://getnigiri.vulpem.com | sudo bash # see https://nigiri.vulpem.com/#install
sudo nigiri start
xdg-open http://localhost:5000/
* Это создаёт
  * esplora localhost:3000
    electrs localhost:50000 
  * и графический блок-эксплорер на http://localhost:5000
* Настройка инстанса mempool
sudo apt install docker-compose
git clone https://github.com/ngutech21/nigiri-mempool.git

pushd nigiri-mempool
sudo docker-compose up -d
sleep 10
# это нужно, потому что базе данных требуется время на запуск 
sudo docker-compose up -d
popd
xdg-open http://localhost:8080/

# если mempool бесконечно загружается, получите отладочный вывод с помощью
sudo docker-compose logs -f mempool-api
* это откроет mempool на http://localhost:8080/

#### Управление Regtest-окружением

* получить монеты на адрес
nigiri rpc generatetoaddress 1 bcrt1qgsnt3d4sny4w4zd5zl9x6jufc5rankqmgphyms9vz0ds73q4xfms655y4c # mine blocks

# или используйте внутренний кран (faucet)
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

### Qt Designer

Элементы Qt можно исследовать с помощью Qt Designer:
virtualenv .env-qt-designer
source .env-qt-designer/bin/activate
pip install pyqt6-tools 
pyqt6-tools designer
## Политика подписи кода


Бесплатная подпись кода предоставляется [SignPath.io](https://about.signpath.io/), сертификат — от [SignPath Foundation](https://signpath.org/)


## Политика конфиденциальности
По умолчанию эта программа использует:
- electrum/esplora-сервер [blockstream.com](https://blockstream.com/) для получения данных блокчейна
- получение информации о комиссиях mempool с [mempool.space](https://mempool.space/)

Вы можете указать собственный (персональный) сервер для обоих в "Network settings".

При включении функции Синхронизация&Чат используются [relays по умолчанию](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py) для передачи зашифрованных данных на ваши одобренные доверенные устройства. Вы можете указать собственный(е) ретранслятор(ы) в настройках Sync&Chat.

Эта программа не будет передавать какую-либо другую информацию другим сетевым системам, если это специально не запрошено пользователем или лицом, устанавливающим или эксплуатирующим её.