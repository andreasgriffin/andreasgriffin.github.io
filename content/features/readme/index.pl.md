---
title: "Wszystkie funkcje"
description: "Kompleksowy przegląd większości funkcji w Bitcoin Safe"
draft: false
tags: [ "Features" ]
images: ["logo.png"]
keywords: [
  "Bitcoin Safe",
  "portfel oszczędnościowy Bitcoin",
  "portfel MultiSig",
  "kreator konfiguracji multisig",
  "hardware signers",
  "bezpieczne przechowywanie seedów",
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
  "wsparcie wielojęzyczne",
  "etykietowanie adresów",
  "diagramy przepływu transakcji",
  "PSBT",
  "wybór opłaty",
  "mempool",
  "serwer Electrum",
  "Compact Block Filters",
  "eksport CSV",
  "import CSV",
  "BIP329",
  "przeciągnij i upuść",
  "Replace-by-Fee",
  "kopia zapasowa PDF",
  "podpisywanie wiadomości",
  "MicroSD",
  "USB",
  "kody QR",
  "animowane kody QR",
  "wyszukiwanie i filtrowanie",
  "czat portfela",
  "synchronizacja etykiet",
  "regtest",
  "Docker",
  "Nigiri",
  "wieloplatformowy",
  "instalacja",
  "rozwój"
]
weight: -10
---
<!-- header-end -->
# Bitcoin Safe

#### Portfel oszczędnościowy Bitcoin dla całej rodziny

- **Łatwa** konfiguracja portfela MultiSig
  - Instrukcje krok po kroku do bezpiecznej konfiguracji MultiSig z arkuszami kopii zapasowej w PDF
  - Testowe transakcje zapewniają, że wszystkie sprzętowe podpisywarki są gotowe
  - Pełne wsparcie dla [Coldcard](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Coldcard Q](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Bitbox02](https://shop.bitbox.swiss/?ref=MOB4dk7gpm), [Blockstream Jade](https://store.blockstream.com/?code=XEocg5boS77D), [Trezor](https://affil.trezor.io/SHtN), [Foundation Passport Core](https://foundation.xyz/?ref=cbyqjjxumy), [Keystone](https://keyst.one), [Ledger](https://shop.ledger.com/?r=400f1fff75b5), [Specter DIY](https://clavastack.com/en/?coupon=bitcoin-safe), [SeedSigner](https://seedsigner.com), [Krux](https://selfcustody.github.io/krux), z użyciem *QR*, *USB* i *karty SD*
- **Bezpieczne**: tylko sprzętowe podpisywarki
  - Wszystkie portfele wymagają sprzętowych podpisywarek/portfeli do bezpiecznego przechowywania seedów
  - Napędzane przez **[BDK](https://github.com/bitcoindevkit/bdk)**
- **Wielojęzyczne**:
  - 🇺🇸 angielski, 🇨🇳 Chiński - 简体中文, 🇪🇸 hiszpański - español de España, 🇯🇵 japoński - 日本語, 🇷🇺 rosyjski - русский, 🇵🇹 portugalski - português europeu, 🇮🇳 hindi - हिन्दी, arabski - العربية, 🇮🇹 włoski - italiano, 🇫🇷 francuski - Français, 🇩🇪 niemiecki - Deutsch, 🇲🇲 birmański - မြန်မာ, 🇰🇷 koreański - 한국어, 🇹🇭 tajski - ภาษาไทย, 🇮🇷 perski (farsi) - فارسی, 🇵🇱 polski - Polski, 🇪🇸 kataloński - Català, (więcej na życzenie)
- **Prostsze** etykietowanie adresów przez użycie kategorii (np. "KYC", "Non-KYC", "Praca", "Znajomi", ...)
  - Automatyczny wybór monet w obrębie kategorii
  - Diagramy przepływu transakcji, wizualizujące wejścia i wyjścia — kliknij na wejścia i wyjścia, aby śledzić przepływ pieniędzy
- **Wysyłanie** dla użytkowników nietechnicznych
  - Jednoklikowy wybór opłaty poprzez mempool-blocks
  - Automatyczne scalanie UTXO, gdy opłaty są niskie
- **Synchronizacja i czat**:
  - Zaszyfrowana kopia zapasowa etykiet w chmurze (przez nostr)
  - Synchronizacja etykiet między różnymi komputerami
  - Czat portfela i udostępnianie PSBT między różnymi komputerami
- **Szybkie**:
  - Synchronizacja przez serwer Electrum
  - planowana aktualizacja do **Compact Block Filters** dla wydania Bitcoin Safe 2.0




### W pełni funkcjonalny — prosty i potężny

| **Kreator konfiguracji MultiSig**          | **Utwórz PSBT, podpisz i wyślij**                     |
|--------------------------------|----------------------------|
| ![Multisig setup](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/multisig-setup.gif) |  ![Send transaction](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/send.gif) |
| **Eksploracja transakcji za pomocą diagramu**          | **Wyszukiwanie wpisywania we wszystkich portfelach**                    |
| ![Explorer](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/explorer.gif) |  ![Global search](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/global-search.gif) |
|   **Automatyczna synchronizacja etykiet**      | **Współpraca wielostronna w multisig**                  |
| ![Label sync](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/label-sync.gif)  |   ![PSBT share](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/psbt-share.gif) |
|   **Kategorie monet**      |                 |
| ![Category drag and drop](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/category-drag-and-drop.gif)  |   |



### Dostępny na wszystkich platformach
| ![Windows](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-win.png) | ![Mac OS X](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-mac.png) | ![Linux](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-linux.png) |
|-----------------------------|-----------------------------|----------------------------|
| Windows                    | Mac OS X                   | Linux                     |


## Kompleksowa lista funkcji

- **Możliwości importu i eksportu**
  
  - Eksport CSV dla wszystkich list
  - Import CSV dla transakcji wsadowych
  - Import i eksport etykiet przy użyciu [BIP329](https://bip329.org/)
  - Import etykiet z portfela Electrum
  - Eksport diagramu przepływu pieniędzy do SVG
  - Przeciągnij i upuść dla transakcji, PSBT i plików CSV

- **Funkcje portfela**
  
  - Uproszczone etykietowanie adresów przy użyciu kategorii takich jak KYC, Non-KYC, Praca, Znajomi
  - Podbijanie opłaty dla transakcji (przez Replace-by-Fee)
  - Szybsze otrzymywanie (przez Child Pays For Parents)
  - Zaszyfrowane przechowywanie portfela
  - Kopia zapasowa PDF z Deskriptorem (tekst i kod QR)
  - Podpisywanie wiadomości przez USB i QR

- **Łączność ze sprzętowymi podpisywarkami**
  
  - MicroSD (pliki)
  - USB
  - Kody QR (udoskonalane wykrywanie kodów QR dla kamer laptopów)
  - Animowane kody QR, w tym [Coldcard/BBQr](https://bbqr.org/) i format [UR](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md)

- **Opcje wyszukiwania i filtrowania**
  
  - Szybkie filtrowanie po txid, UTXO, etykietach, datach, kwotach, kategoriach
  - Wyszukiwanie we wszystkich otwartych portfelach: txid, UTXO, etykiety, daty, kwoty, kategorie

- **Języki**
  
  - 🇺🇸 angielski, 🇨🇳 Chiński - 简体中文, 🇪🇸 hiszpański - español de España, 🇯🇵 japoński - 日本語, 🇷🇺 rosyjski - русский, 🇵🇹 portugalski - português europeu, 🇮🇳 hindi - हिन्दी, arabski - العربية, 🇮🇹 włoski - italiano, 🇫🇷 francuski - Français, 🇩🇪 niemiecki - Deutsch, 🇲🇲 birmański - မြန်မာ, 🇰🇷 koreański - 한국어, 🇹🇭 tajski - ภาษาไทย, 🇮🇷 perski (farsi) - فارسی, 🇵🇱 polski - Polski, 🇪🇸 kataloński - Català, (więcej na życzenie)

- **Tworzenie transakcji / PSBT**
  
  - Jednoklikowy wybór opłaty i podgląd bloków w mempoolu
  - Automatyczne scalanie UTXO, gdy opłaty są niskie
  - Wyróżnianie własnych adresów

- **Bezpieczeństwo i niezawodność**
  
  - Brak generowania lub przechowywania seedów na mainnecie
  - Przechowywanie seedów wymaga oddzielnej sprzętowej podpisywarki
  - Powiadomienia o aktualizacjach i weryfikacja podpisów
  - Napędzane przez [Bitcoin Development Kit (BDK)](https://github.com/bitcoindevkit/bdk)

- **Łatwość użycia dla portfeli multisig**
  
  - Uproszczona konfiguracja portfeli multisig, w tym instrukcje krok po kroku i arkusz kopii zapasowej w PDF
  - Testowe podpisywanie ze wszystkimi sprzętowymi podpisywarkami
  - Współdzielone zarządzanie portfelem, w tym czat i udostępnianie PSBT przez nostr oraz synchronizacja etykiet między zaufanymi urządzeniami
  - Opcjonalny własny serwer nostr

- **Nadchodzące funkcje**
  
  - Dla wydania 2.0
    - **Compact Block Filters** domyślnie
      - Compact Block Filters są **szybkie** i **prywatne**
      - Compact Block Filters (bdk) są [opracowywane](https://github.com/bitcoindevkit/bdk/issues/679) i zostaną uwzględnione w bdk 1.1. Na razie dostępne są RPC, Electrum i Esplora, ale zostaną całkowicie zastąpione przez Compact Block Filters.


## Instalacja z repozytorium Git


### Ubuntu, Debian

- Zainstaluj zależności: 
sudo apt-get install qt6-tools-dev-tools libzbar-dev libxcb-cursor0 '^libqt6.*$'
- Zainstaluj `poetry` i uruchom `bitcoin_safe`
git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
  pip install poetry  && poetry install && poetry run python -m bitcoin_safe
### Mac

- Sklonuj `bitcoin_safe`
open "/Applications/Python 3.12/Install Certificates.command"
  export SSL_CERT_FILE=$(python3 -m certifi) # to fix ssl errors
  git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
- *Opcjonalnie*: zależność `zbar`
brew install zbar
- Uruchom `bitcoin_safe`
python3 -m pip install poetry && python3 -m poetry install && python3 -m poetry run python3 -m bitcoin_safe
## Rozwój

* Uruchom precommit ręcznie w celu debugowania
poetry run pre-commit run --all-files
#### Środowisko regtest w Dockerze z electrs i mempool

* zainstaluj docker
# see https://docs.docker.com/engine/install/ubuntu/
* konfiguracja środowiska regtest w docker + instancja mempool
curl https://getnigiri.vulpem.com | sudo bash # see https://nigiri.vulpem.com/#install
sudo nigiri start
xdg-open http://localhost:5000/
* To tworzy
  * esplora localhost:3000
    electrs localhost:50000 
  * oraz graficzny eksplorator bloków pod adresem http://localhost:5000
* Konfiguracja instancji mempool
sudo apt install docker-compose
git clone https://github.com/ngutech21/nigiri-mempool.git

pushd nigiri-mempool
sudo docker-compose up -d
sleep 10
# to jest potrzebne, ponieważ baza danych potrzebuje czasu, aby się uruchomić 
sudo docker-compose up -d
popd
xdg-open http://localhost:8080/

# jeśli mempool ładuje się w nieskończoność, uzyskaj debugowy output za pomocą
sudo docker-compose logs -f mempool-api
* to otwiera mempool pod adresem http://localhost:8080/

#### Kontrola środowiska Regtest

* zdobycie monet na adres
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

Komponenty Qt można przeglądać za pomocą qt designera:
virtualenv .env-qt-designer
source .env-qt-designer/bin/activate
pip install pyqt6-tools 
pyqt6-tools designer
## Polityka podpisywania kodu


Bezpłatne podpisywanie kodu zapewniane przez [SignPath.io](https://about.signpath.io/), certyfikat przez [SignPath Foundation](https://signpath.org/)


## Polityka prywatności
Ten program używa domyślnie
- serwera electrum/esplora z [blockstream.com](https://blockstream.com/) do pobierania danych z łańcucha bloków
- pobiera informacje o opłatach z mempool z [mempool.space](https://mempool.space/)

Możesz określić własny (osobisty) serwer dla obu w "Network settings".

Po włączeniu funkcji Synchronizacja i Czat używane są [domyślne przekaźniki](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py) do przesyłania zaszyfrowanych danych do zatwierdzonych zaufanych urządzeń. Możesz określić własny(-e) przekaźnik(-i) w ustawieniach Synchronizacji i Czat.

Ten program nie będzie przekazywać żadnych innych informacji do innych systemów sieciowych, chyba że zostanie to wyraźnie zażądane przez użytkownika lub osobę instalującą czy obsługującą program.