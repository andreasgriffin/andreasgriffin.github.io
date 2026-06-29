---
aliases:
  - "/de/features/readme/"
title: "Alle Funktionen"
description: "Umfassender Überblick über die meisten Funktionen von Bitcoin Safe"
draft: false
bucket: features
images: ["logo.png"]
keywords: [
  "Bitcoin Safe",
  "Bitcoin-Spar-Wallet",
  "MultiSig-Wallet",
  "Multisig‑Einrichtungsassistent",
  "Hardware‑Signer",
  "sichere Seed‑Speicherung",
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
  "Mehrsprachige Unterstützung",
  "Adressbeschriftung",
  "Transaktionsflussdiagramme",
  "PSBT",
  "Gebührenauswahl",
  "mempool",
  "Electrum-Server",
  "Compact Block Filters",
  "CSV‑Export",
  "CSV‑Import",
  "BIP329",
  "Ziehen und Ablegen",
  "Replace-by-Fee",
  "Backup-PDF",
  "Nachrichtenunterzeichnung",
  "MicroSD",
  "USB",
  "QR-Codes",
  "animierte QR-Codes",
  "Suche und Filterung",
  "Wallet-Chat",
  "Label‑Synchronisation",
  "regtest",
  "Docker",
  "Nigiri",
  "plattformübergreifend",
  "Installation",
  "Entwicklung"
]
weight: -10
---
<!-- header-end -->
# Bitcoin Safe

#### Eine Bitcoin‑Spar‑Wallet für die ganze Familie

- **Einfach** Multisig‑Wallet-Setup
  - Schritt‑für‑Schritt‑Anleitungen für ein sicheres MultiSig-Setup mit PDF‑Backup‑Blättern
  - Testtransaktionen stellen sicher, dass alle Hardware‑Signer bereit sind
  - Vollständige Unterstützung für [Coldcard](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Coldcard Q](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Bitbox02](https://shop.bitbox.swiss/?ref=MOB4dk7gpm), [Blockstream Jade](https://store.blockstream.com/?code=XEocg5boS77D), [Trezor](https://affil.trezor.io/SHtN), [Foundation Passport Core](https://foundation.xyz/?ref=cbyqjjxumy), [Keystone](https://keyst.one), [Ledger](https://shop.ledger.com/?r=400f1fff75b5), [Specter DIY](https://clavastack.com/en/?coupon=bitcoin-safe), [SeedSigner](https://seedsigner.com), [Krux](https://selfcustody.github.io/krux), unter Verwendung von *QR*, *USB* und *SD‑Karte*
- **Sicher**: Nur Hardware‑Signer
  - Alle Wallets benötigen Hardware‑Signer/Wallets für sichere Seed‑Speicherung
  - Angetrieben von **[BDK](https://github.com/bitcoindevkit/bdk)**
- **Mehrsprachig**:
  - 🇺🇸 Englisch, 🇨🇳 Chinesisch - 简体中文, 🇪🇸 Spanisch - español de España, 🇯🇵 Japanisch - 日本語, 🇷🇺 Russisch - русский, 🇵🇹 Portugiesisch - português europeu, 🇮🇳 Hindi - हिन्दी, Arabisch -,atalanisch - Català, (mehr auf Anfrage)
- **Einfachere** Adress‑Beschriftungen durch Kategorien (z. B. „KYC“, „Non‑KYC“, „Arbeit“, „Freunde“, …)
  - Automatische Münzauswahl innerhalb von Kategorien
  - Transaktionsflussdiagramme, die Eingaben und Ausgaben visualisieren; klicken Sie auf Eingaben und Ausgaben, um den Geldfluss nachzuverfolgen
- **Senden** für nicht‑technische Benutzer
  - Ein‑Klick‑Gebührenauswahl über Mempool‑Blöcke
  - Automatisches Zusammenführen von UTXOs bei niedrigen Gebühren
- **Sync & Chat**:
  - Verschlüsseltes Cloud‑Backup (via nostr) von Labels
  - Label‑Synchronisation zwischen verschiedenen Computern
  - Wallet‑Chat und PSBT‑Teilen zwischen verschiedenen Computern
- **Schnell**: 
  - Synchronisation mit Electrum‑Server
  - geplantes Upgrade zu **Compact Block Filters** für die Bitcoin Safe 2.0‑Version




### Vollständig ausgestattet – Einfach und Leistungsstark

| **Multisig‑Einrichtungsassistent**          | **Erstelle ein PSBT, signiere und sende**                     |
|--------------------------------|----------------------------|
| ![Multisig setup](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/multisig-setup.gif) |  ![Send transaction](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/send.gif) |
| **Transaktionsexploration via Diagramm**          | **Während der Eingabe suchen in allen Wallets**                    |
| ![Explorer](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/explorer.gif) |  ![Global search](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/global-search.gif) |
|   **Automatische Label‑Synchronisation**      | **Mehrparteien‑Multisig‑Zusammenarbeit**                  |
| ![Label sync](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/label-sync.gif)  |   ![PSBT share](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/psbt-share.gif) |
|   **Münz‑Kategorien**      |                 |
| ![Category drag and drop](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/category-drag-and-drop.gif)  |   |



### Auf allen Plattformen verfügbar
| ![Windows](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-win.png) | ![Mac OS X](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-mac.png) | ![Linux](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-linux.png) |
|-----------------------------|-----------------------------|----------------------------|
| Windows                    | Mac OS X                   | Linux                     |


## Umfassende Funktionsliste

- **Import- und Exportfähigkeiten**
  
  - CSV‑Export für alle Listen
  - CSV‑Import für Stapeltransaktionen
  - Label‑Import und -Export mit [BIP329](https://bip329.org/)
  - Label‑Import aus Electrum‑Wallet
  - Export des Geldflussdiagramms als SVG
  - Ziehen und Ablegen für Transaktionen, PSBTs und CSV‑Dateien

- **Wallet‑Funktionen**
  
  - Vereinfachte Adressbeschriftung mittels Kategorien wie KYC, Non‑KYC, Arbeit, Freunde
  - Gebühr erhöhen bei Transaktionen (via Replace‑by‑Fee)
  - Schneller empfangen (via Child Pays For Parents)
  - Verschlüsselter Wallet‑Speicher
  - Backup‑PDF mit Descriptor (Text und QR‑Code)
  - Nachrichtenunterzeichnung via USB und QR

- **Hardware‑Signer‑Konnektivität**
  
  - MicroSD (Dateien)
  - USB
  - QR‑Codes (verbesserte QR‑Code‑Erkennung für Laptop‑Kameras)
  - Animierte QR‑Codes inklusive [Coldcard/BBQr](https://bbqr.org/) und [UR](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md) Format

- **‑ und Filter Spanisch - español de España, 🇯🇵 Japanisch - 日本語, 🇷🇺 Russisch - русский, 🇵🇹 Portugiesisch - português europeu, 🇮🇳 Hindi - हिन्दी, Arabisch - العربية, 🇮🇹 Italienisch - italiano, 🇫🇷 Französisch - Français, 🇩🇪 Deutsch, 🇲🇲 Birmanisch - မြန်မာ, 🇰🇷 Koreanisch - 한국어, 🇹🇭 Thailändisch - ภาษาไทย, 🇮🇷 Persisch (Farsi) - فارسی, 🇵🇱 Polnisch - Polski, 🇪🇸 Katalanisch - Català, (mehr auf Anfrage)

- **Transaktion / PSBT‑Erstellung**
  
  - Ein‑Klick‑Gebührenauswahl und Mempool‑Block‑Vorschau
  - Automatisches Zusammenführen von UTXOs bei niedrigen Gebühren
  - Hervorhebung eigener Adressen 

- **Sicherheit und Zuverlässigkeit**
  
  - Keine Seed‑Erzeugung oder -Speicherung im Mainnet
  - Seed‑Speicherung erfordert einen separaten Hardware‑Signer  
  - Update‑Benachrichtigungen und Signatur‑Verifizierung
  - Angetrieben von [Bitcoin Development Kit (BDK)](https://github.com/bitcoindevkit/bdk)

- **Benutzerfreundlichkeit für Multisig‑Wallets**
  
  - Vereinfachte Einrichtung für Multisig‑Wallets, inkl. Schritt‑für‑Schritt‑Anleitungen und PDF‑Backup‑Blatt
  - Test‑Signierung mit allen Hardware‑Signern
  - Kollaboratives Wallet‑Management inkl. Chat und PSBT‑Teilen via nostr sowie Label‑Synchronisation zwischen vertrauenswürdigen Geräten
  - Optionaler benutzerdefinierter nostr‑Server 

- **Zukünftige Features**
  
  - Für das 2.0‑Release
    - **Compact Block Filters** standardmäßig
      - Compact Block Filters sind **schnell** und **privat**
      - Compact Block Filters (bdk) werden derzeit [bearbeitet](https://github.com/bitcoindevkit/bdk/issues/679) und sollen in bdk 1.1 enthalten sein. Derzeit stehen RPC, Electrum und Esplora zur Verfügung, werden aber vollständig durch Compact Block Filters ersetzt werden.



## Installation vom Git‑Repository


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
## Entwicklung

* Pre‑Commit manuell zum Debuggen ausführen
poetry run pre-commit run --all-files
#### Regtest‑Docker‑Umgebung mit electrs und mempool

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

#### Regtest‑Umgebung steuern

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
## Code‑Signatur‑Richtlinie


Free code signing provided by [SignPath.io](https://about.signpath.io/), certificate by [SignPath Foundation](https://signpath.org/)


## Datenschutz‑Richtlinie
Dieses Programm verwendet standardmäßig
- den Electrum/Esplora‑Server von [blockstream.com](https://blockstream.com/), um Blockchain‑Daten abzurufen
- ruft Gebühreninformationen des Mempools von [mempool.space](https://mempool.space/) ab

Sie können in den „Netzwerkeinstellungen“ eigene (private) Server für beides angeben.

Beim Aktivieren der Sync&Chat‑Funktion werden die [Standard‑Relays](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py) verwendet, um verschlüsselte Daten an Ihre freigegebenen, vertrauenswürdigen Geräte zu übertragen. Sie können eigene Relays in den Sync&Chat‑Einstellungen festlegen.

Dieses Programm überträgt keine weiteren Informationen an andere Netzwerk‑Systeme, es sei denn, der Nutzer oder die Person, die das Programm installiert oder betreibt, fordert dies ausdrücklich an.