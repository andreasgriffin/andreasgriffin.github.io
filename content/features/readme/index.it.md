---
title: "Tutte le funzionalità"
description: "Panoramica completa della maggior parte delle funzionalità di Bitcoin Safe"
draft: false
tags: [ "Features" ]
images: ["logo.png"]
keywords: [
  "Bitcoin Safe",
  "portafoglio di risparmio bitcoin",
  "portafoglio MultiSig",
  "procedura guidata di configurazione Multisig",
  "hardware signers",
  "conservazione sicura del seed",
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
  "supporto multilingue",
  "etichettatura degli indirizzi",
  "diagrammi del flusso delle transazioni",
  "PSBT",
  "selezione delle commissioni",
  "mempool",
  "Electrum server",
  "Compact Block Filters",
  "esportazione CSV",
  "importazione CSV",
  "BIP329",
  "drag and drop",
  "Replace-by-Fee",
  "backup PDF",
  "firma di messaggi",
  "MicroSD",
  "USB",
  "codici QR",
  "codici QR animati",
  "ricerca e filtraggio",
  "chat del portafoglio",
  "sincronizzazione delle etichette",
  "regtest",
  "Docker",
  "Nigiri",
  "cross-platform",
  "installazione",
  "sviluppo"
]
weight: -10
---
<!-- header-end -->
# Bitcoin Safe

#### Un portafoglio di risparmio Bitcoin per tutta la famiglia

- **Facile** configurazione del portafoglio Multisig
  - Istruzioni passo-passo per una configurazione MultiSig sicura con fogli di backup in PDF
  - Transazioni di prova per assicurarsi che tutti gli hardware signer siano pronti
  - Supporto completo per [Coldcard](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Coldcard Q](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Bitbox02](https://shop.bitbox.swiss/?ref=MOB4dk7gpm), [Blockstream Jade](https://store.blockstream.com/?code=XEocg5boS77D), [Trezor](https://affil.trezor.io/SHtN), [Foundation Passport](https://foundation.xyz/passport), [Keystone](https://keyst.one), [Ledger](https://shop.ledger.com/?r=400f1fff75b5), [Specter DIY](https://clavastack.com/en/?coupon=bitcoin-safe), [SeedSigner](https://seedsigner.com), [Krux](https://selfcustody.github.io/krux), usando *QR*, *USB* e *SD-card*
- **Sicuro**: solo hardware signer
  - Tutti i portafogli richiedono hardware signer/portafogli per la conservazione sicura del seed
  - Basato su **[BDK](https://github.com/bitcoindevkit/bdk)**
- **Multilingue**:
  - 🇺🇸 Inglese - English, 🇨🇳 Cinese - 简体中文, 🇪🇸 Spagnolo - español de España, 🇯🇵 Giapponese - 日本語, 🇷🇺 Russo - русский, 🇵🇹 Portoghese - português europeu, 🇮🇳 Hindi - हिन्दी, Arabo - العربية, 🇮🇹 Italiano - italiano, 🇫🇷 Francese - Français, 🇩🇪 Tedesco - Deutsch, 🇲🇲 Birmano - မြန်မာ, 🇰🇷 Coreano - 한국어, 🇹🇭 Thai - ภาษาไทย, 🇮🇷 Persiano (Farsi) - فارسی, 🇵🇱 Polacco - Polski, 🇪🇸 Catalano - Català, (altri su richiesta)
- **Semplifica** le etichette degli indirizzi usando categorie (es. "KYC", "Non-KYC", "Lavoro", "Amici", ...)
  - Selezione automatica delle monete all'interno delle categorie
  - Diagrammi del flusso delle transazioni che visualizzano input e output; clicca su input e output per tracciare il flusso dei fondi
- **Invio** per utenti non tecnici
  - Selezione della commissione con 1 clic tramite mempool-blocks
  - Fusione automatica degli utxo quando le commissioni sono basse
- **Sincronizzazione & Chat**:
  - Backup crittografato su cloud (via nostr) delle etichette
  - Sincronizzazione delle etichette tra diversi computer
  - Chat del portafoglio e condivisione di PSBT tra diversi computer
- **Veloce**:
  - Sincronizzazione tramite Electrum server
  - aggiornamento pianificato a **Compact Block Filters** per il rilascio di Bitcoin Safe 2.0




### Completamente funzionale - Semplice e Potente

| **Procedura guidata di configurazione Multisig**          | **Crea una PSBT, firma e broadcast**                     |
|--------------------------------|----------------------------|
| ![Multisig setup](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/multisig-setup.gif) |  ![Send transaction](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/send.gif) |
| **Esplorazione delle transazioni tramite diagramma**          | **Digita per cercare in tutti i portafogli**                    |
| ![Explorer](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/explorer.gif) |  ![Global search](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/global-search.gif) |
|   **Sincronizzazione automatica delle etichette**      | **Collaborazione multiparte Multisig**                  |
| ![Label sync](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/label-sync.gif)  |   ![PSBT share](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/psbt-share.gif) |
|   **Categorie di monete**      |                 |
| ![Category drag and drop](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/category-drag-and-drop.gif)  |   |



### Disponibile su tutte le piattaforme
| ![Windows](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-win.png) | ![Mac OS X](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-mac.png) | ![Linux](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-linux.png) |
|-----------------------------|-----------------------------|----------------------------|
| Windows                    | Mac OS X                   | Linux                     |


## Elenco completo delle funzionalità

- **Capacità di importazione ed esportazione**
  
  - Esportazione CSV per tutte le liste
  - Importazione CSV per transazioni in batch
  - Importazione ed esportazione di etichette tramite [BIP329](https://bip329.org/)
  - Importazione di etichette dal portafoglio Electrum
  - Esportazione del diagramma del flusso dei fondi in svg
  - Drag and drop per Transazioni, PSBT e file CSV

- **Funzionalità del portafoglio**
  
  - Etichettatura semplificata degli indirizzi usando categorie come KYC, Non-KYC, Lavoro, Amici
  - Aumento della commissione su transazioni (tramite Replace-by-Fee)
  - Ricezione più veloce (tramite Child Pays For Parents)
  - Archiviazione del portafoglio crittografata
  - Backup in PDF con Descriptor (Testo e codice QR)
  - Firma di messaggi via USB e QR

- **Connettività con hardware signer**
  
  - MicroSD (file)
  - USB
  - Codici QR (rilevamento migliorato dei codici QR per le fotocamere dei laptop)
  - Codici QR animati incluso [Coldcard/BBQr](https://bbqr.org/) e formato [UR](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md)

- **Opzioni di ricerca e filtraggio**
  
  - Filtraggio veloce su txid, utxo, etichette, date, importi, categorie
  - Ricerca in tutti i portafogli aperti: txid, utxo, etichette, date, importi, categorie

- **Lingue**
  
  - 🇺🇸 Inglese - English, 🇨🇳 Cinese - 简体中文, 🇪🇸 Spagnolo - español de España, 🇯🇵 Giapponese - 日本語, 🇷🇺 Russo - русский, 🇵🇹 Portoghese - português europeu, 🇮🇳 Hindi - हिन्दी, Arabo - العربية, 🇮🇹 Italiano - italiano, 🇫🇷 Francese - Français, 🇩🇪 Tedesco - Deutsch, 🇲🇲 Birmano - မြန်မာ, 🇰🇷 Coreano - 한국어, 🇹🇭 Thai - ภาษาไทย, 🇮🇷 Persiano (Farsi) - فارسی, 🇵🇱 Polacco - Polski, 🇪🇸 Catalano - Català, (altri su richiesta)

- **Creazione di transazioni / PSBT**
  
  - Selezione della commissione con 1 clic e anteprima dei blocchi del mempool
  - Fusione automatica degli utxo quando le commissioni sono basse
  - Evidenziazione dei propri indirizzi

- **Sicurezza e affidabilità**
  
  - Nessuna generazione o memorizzazione del seed su mainnet
  - La conservazione del seed richiede un hardware signer separato
  - Notifiche di aggiornamento e verifica delle firme
  - Basato su [Bitcoin Development Kit (BDK)](https://github.com/bitcoindevkit/bdk)

- **Facilità d'uso per portafogli Multisig**
  
  - Configurazione semplificata per portafogli multisig, comprese istruzioni passo-passo e foglio di backup in PDF
  - Firma di prova con tutti gli hardware signer
  - Gestione collaborativa del portafoglio inclusa chat e condivisione di PSBT via nostr e sincronizzazione delle etichette tra dispositivi attendibili
  - Server nostr personalizzato opzionale

- **Funzionalità future**
  
  - Per la release 2.0
    - **Compact Block Filters** di default
      - I Compact Block Filters sono **veloci** e **privati**
      - I Compact Block Filters (bdk) sono in fase di [sviluppo](https://github.com/bitcoindevkit/bdk/issues/679), e saranno inclusi in bdk 1.1. Per ora sono disponibili RPC, Electrum ed Esplora, ma saranno completamente sostituiti dai Compact Block Filters.


## Installazione dal repository Git


### Ubuntu, Debian

- Installa le dipendenze: 
sudo apt-get install qt6-tools-dev-tools libzbar-dev libxcb-cursor0 '^libqt6.*$'
- Installa `poetry` e avvia `bitcoin_safe`
git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
  pip install poetry  && poetry install && poetry run python -m bitcoin_safe
### Mac

- Clona `bitcoin_safe`
open "/Applications/Python 3.12/Install Certificates.command"
  export SSL_CERT_FILE=$(python3 -m certifi) # to fix ssl errors
  git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
- *Opzionale*: dipendenza `zbar`
brew install zbar
- Avvia `bitcoin_safe`
python3 -m pip install poetry && python3 -m poetry install && python3 -m poetry run python3 -m bitcoin_safe
## Sviluppo

* Esegui il precommit manualmente per il debug
poetry run pre-commit run --all-files
#### Ambiente regtest Docker con electrs e mempool

* installa docker
# see https://docs.docker.com/engine/install/ubuntu/
* configurazione di un ambiente regtest in docker + istanza mempool
curl https://getnigiri.vulpem.com | sudo bash # see https://nigiri.vulpem.com/#install
sudo nigiri start
xdg-open http://localhost:5000/
* Questo crea
  * esplora localhost:3000
    electrs localhost:50000 
  * e un block explorer con interfaccia grafica su http://localhost:5000
* Configura l'istanza mempool
sudo apt install docker-compose
git clone https://github.com/ngutech21/nigiri-mempool.git

pushd nigiri-mempool
sudo docker-compose up -d
sleep 10
# questo è necessario perché il database ha bisogno di tempo per avviarsi 
sudo docker-compose up -d
popd
xdg-open http://localhost:8080/

# se il mempool si carica senza fine, ottieni l'output di debug con
sudo docker-compose logs -f mempool-api
* questo apre un mempool su http://localhost:8080/

#### Controllare l'ambiente Regtest

* ottenere coin su un indirizzo
nigiri rpc generatetoaddress 1 bcrt1qgsnt3d4sny4w4zd5zl9x6jufc5rankqmgphyms9vz0ds73q4xfms655y4c # mina blocchi

# o usa il faucet interno
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

I componenti Qt possono essere esplorati con il Qt Designer:
virtualenv .env-qt-designer
source .env-qt-designer/bin/activate
pip install pyqt6-tools 
pyqt6-tools designer
## Politica di firma del codice


Firma del codice gratuita fornita da [SignPath.io](https://about.signpath.io/), certificato da [SignPath Foundation](https://signpath.org/)


## Informativa sulla privacy
Questo programma utilizza per impostazione predefinita
- il server electrum/esplora di [blockstream.com](https://blockstream.com/) per recuperare i dati della blockchain
- recupera informazioni sulle commissioni del mempool da [mempool.space](https://mempool.space/)

Puoi specificare il tuo server (personale) per entrambi nelle "Impostazioni di rete".

Quando abiliti la funzione Sync&Chat vengono utilizzati i [relay predefiniti](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py) per trasmettere i dati crittografati ai tuoi dispositivi attendibili approvati. Puoi specificare il tuo(i) relay nelle impostazioni di Sync&Chat.

Questo programma non trasferirà altre informazioni ad altri sistemi in rete a meno che non sia espressamente richiesto dall'utente o dalla persona che lo installa o lo gestisce.