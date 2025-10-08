---
title: "Totes les funcionalitats"
description: "Visió general exhaustiva de la majoria de les funcionalitats de Bitcoin Safe"
draft: false
tags: [ "Features" ]
images: ["logo.png"]
keywords: [
  "Bitcoin Safe",
  "cartera d'estalvi bitcoin",
  "cartera MultiSig",
  "Assistent de configuració Multisig",
  "signadors de maquinari",
  "emmagatzematge segur de llavor",
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
  "suport multilingüe",
  "etiquetatge d'adreces",
  "diagrames de flux de transaccions",
  "PSBT",
  "selecció de comissions",
  "mempool",
  "Electrum server",
  "Compact Block Filters",
  "CSV export",
  "CSV import",
  "BIP329",
  "arrossega i deixa anar",
  "Replace-by-Fee",
  "PDF de còpia de seguretat",
  "signatura de missatges",
  "MicroSD",
  "USB",
  "codi QR",
  "codi QR animat",
  "cerca i filtrat",
  "xat de cartera",
  "sincronització d'etiquetes",
  "regtest",
  "Docker",
  "Nigiri",
  "multiplataforma",
  "instal·lació",
  "desenvolupament"
]
weight: -10
---
<!-- header-end -->
# Bitcoin Safe

#### Una'estalvi bitcoin per a tota la família

- **Fàcil** Configuració de cartera MultiSig
  - Instruccions pas a pas per a una configuració segura de MultiSig amb fulls de còpia de seguretat PDF
  - Transaccions de prova asseguren que tots els signadors de maquinari estan llestos
  - Suport complet per a [Coldcard](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Coldcard Q](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Bitbox02](https://shop.bitbox.swiss/?ref=MOB4dk7gpm), [Blockstream Jade](https://store.blockstream.com/?code=XEocg5boS77D), [Trezor](https://affil.trezor.io/SHtN), [Foundation Passport](https://foundation.xyz/passport), [Keystone](https://keyst.one), [Ledger](https://shop.ledger.com/?r=400f1fff75b5), [Specter DIY](https://clavastack.com/en/?coupon=bitcoin-safe), [SeedSigner](https://seedsigner.com), [Krux](https://selfcustody.github.io/krux), utilitzant *QR*, *USB* i *SD-card* 
- **Segura**: Només signadors de maquinari
  - Totes les carteres requereixen signadors de maquinari/carretilles per a l'emmagatzematge segur de la llavor 
  - Impulsat per **[BDK](https://github.com/bitcoindevkit/bdk)**
- **Multilingüe**:
  - 🇺🇸 English, 🇨🇳 Chinese - 简体中文, 🇪🇸 Spanish - español de España, 🇯🇵 Japanese - 日本語, 🇷🇺 Russian - русский, 🇵🇹 Portuguese - português europeu, 🇮🇳 Hindi - हिन्दी, Arabic - العربية, 🇮🇹 Italian - italiano, 🇫🇷 French - Français, 🇩🇪 German - Deutsch, 🇲🇲 Burmese - မြန်မာ, 🇰🇷 Korean - 한국어, 🇹🇭 Thai - ภาษาไทย,  🇮🇷 Persian (Farsi) - فارسی, 🇵🇱 Polish - Polski, 🇪🇸 Catalan - Català, (more upon request)
- **Més senzill** etiquetatge d'adreces utilitzant categories (p. ex., "KYC", "Non-KYC", "Treball", "Amics", ...)
  - Selecció automàtica de monedes dins de les categories
  - Diagrames de flux de transaccions, visualitzant entrades i sortides; fes clic a les entrades i sortides per traçar el flux de diners
- **Enviament** per a usuaris no tècnics
  - Selecció de comissió amb 1 clic via blocs del mempool
  - Fusió automàtica d'UTXO quan les comissions són baixes
- **Sincronització i Xat**:
  - Còpia de seguretat en el núvol encriptada (via nostr) d'etiquetes
  - Sincronització d'etiquetes entre diferents ordinadors
  - Xat de cartera i compartició de PSBTs entre diferents ordinadors
- **Ràpid**: 
  - Sincronització amb servidor Electrum
  - actualització planificada a **Compact Block Filters** per al llançament de Bitcoin Safe 2.0 




### Totalment funcional - Fàcil i potent

| **Assistent de configuració Multisig**          | **Crea un PSBT, signa i difon**                     |
|--------------------------------|----------------------------|
| ![](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/multisig-setup.gif) |  ![](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/send.gif) |
| **Exploració de transaccions via diagrama**          | **Cerca per escriure en totes les carteres**                    |
| ![](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/explorer.gif) |  ![](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/global-search.gif) |
|   **Sincronització automàtica d'etiquetes**      | **Col·laboració Multisig multipartidaria**                  |
| ![](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/label-sync.gif)  |   ![](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/psbt-share.gif) |
|   **Categories de monedes**      |                 |
| ![](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/category-drag-and-drop.gif)  |   |



### Available on all platforms
| ![Windows](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-win.png) | ![Mac OS X](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-mac.png) | ![Linux](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-linux.png) |
|-----------------------------|-----------------------------|----------------------------|
| Windows                    | Mac OS X                   | Linux                     |


## Llista completa de funcionalitats

- **Capacitats d'importació i exportació**
  
  - Exportació CSV per a totes les llistes
  - Importació CSV per a transaccions per lots
  - Importació i exportació d'etiquetes usant [BIP329](https://bip329.org/)
  - Importació d'etiquetes des de cartera Electrum
  - Exportació del diagrama de flux de diners a SVG
  - Arrossega i deixa anar per a Transaccions, PSBTs i fitxers CSV

- **Funcionalitats de la cartera**
  
  - Etiquetatge d'adreces simplificat utilitzant categories com KYC, Non-KYC, Treball, Amics
  - Incrementa la comissió en transaccions (via Replace-by-Fee)
  - Rep més ràpid (via Child Pays For Parents)
  - Emmagatzematge de cartera encriptat
  - PDF de còpia de seguretat amb Descriptor (Text i codi QR)
  - Signatura de missatges via USB i QR

- **Connectivitat de Signadors de Maquinari**
  
  - MicroSD (fitxers)
  - USB
  - Codis QR (detecció millorada de codis QR per a càmeres d'ordinador portàtil)
  - Codis QR animats incloent [Coldcard/BBQr](https://bbqr.org/) i format [UR](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md)

- **Opcions de cerca i filtratge**
  
  - Filtrat ràpid a través de txids, utxos, etiquetes, dates, quantitats, categories
  - Cerca a través de totes les carteres obertes, txids, utxos, etiquetes, dates, quantitats, categories

- **Idiomes**
  
  - 🇺🇸 English, 🇨🇳 Chinese - 简体中文, 🇪🇸 Spanish - español de España, 🇯🇵 Japanese - 日本語, 🇷🇺 Russian - русский, 🇵🇹 Portuguese - português europeu, 🇮🇳 Hindi - हिन्दी, Arabic - العربية, 🇮🇹 Italian - italiano, 🇫🇷 French - Français, 🇩🇪 German - Deutsch, 🇲🇲 Burmese - မြန်မာ, 🇰🇷 Korean - 한국어, 🇹🇭 Thai - ภาษาไทย, 🇮🇷 Persian (Farsi) - فارسی, 🇵🇱 Polish - Polski, 🇪🇸 Catalan - Català, (more upon request)

- **Creació de transacció / PSBT**
  
  - Selecció de comissió amb 1 clic i vista prèvia del bloc del mempool
  - Fusió automàtica d'UTXOs quan les comissions són baixes
  - Destacament d'adreces pròpies 

- **Seguretat i fiabilitat**
  
  - Cap generació o emmagatzematge de llavor a mainnet
  - L'emmagatzematge de la llavor requereix un signador de maquinari separat  
  - Notificacions d'actualitzacions i verificació de signatures
  - Impulsat per [Bitcoin Development Kit (BDK)](https://github.com/bitcoindevkit/bdk)

- **Facilitat d'ús per a carteres Multisig**
  
  - Configuració simplificada per a carteres multisig, incloent instruccions pas a pas i full de còpia de seguretat PDF
  - Signatura de prova amb tots els signadors de maquinari
  - Gestió col·laborativa de cartera incloent xat i compartició de PSBT via nostr i sincronització d'etiquetes entre dispositius de confiança
  - Servidor nostr personalitzable opcional 

- **Funcionalitats pròximes**
  
  - Per al llançament 2.0
    - **Compact Block Filters** per defecte
      - Compact Block Filters són **ràpids** i **privats**
      - Compact Block Filters (bdk) s'estan [working on](https://github.com/bitcoindevkit/bdk/issues/679), i s'inclouran en bdk 1.1. De moment RPC, Electrum i Esplora estan disponibles, però s'eliminaran completament a favor de Compact Block Filters.


## Instal·lació des del repositori Git


### Ubuntu, Debian

- Instal·la dependències: 
sudo apt-get install qt6-tools-dev-tools libzbar-dev libxcb-cursor0 '^libqt6.*$'
- Instal·la `poetry` i executa `bitcoin_safe`
git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
  pip install poetry  && poetry install && poetry run python -m bitcoin_safe
### Mac

- Clona `bitcoin_safe`
open "/Applications/Python 3.12/Install Certificates.command"
  export SSL_CERT_FILE=$(python3 -m certifi) # to fix ssl errors
  git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
- *Opcional*: dependència `zbar`
brew install zbar
- Executa `bitcoin_safe`
python3 -m pip install poetry && python3 -m poetry install && python3 -m poetry run python3 -m bitcoin_safe
## Desenvolupament

* Executa el precommit manualment per depurar
poetry run pre-commit run --all-files
#### Entorn Regtest Docker amb electrs i mempool

* instal·la docker
# see https://docs.docker.com/engine/install/ubuntu/
* configuració d'un entorn regtest en docker + instància mempool
curl https://getnigiri.vulpem.com | sudo bash # see https://nigiri.vulpem.com/#install
sudo nigiri start
xdg-open http://localhost:5000/
* Això crea
  * esplora localhost:3000
    electrs localhost:50000 
  * i una interfície web d'explorador de blocs a http://localhost:5000
* Configura una instància mempool
sudo apt install docker-compose
git clone httpsigiri-mempool.git

pushd nigiri-mempool
sudo docker-compose up -d
sleep 10
# això és necessari perquè la base de dades necesse iniciar-se 
sudo docker-compose up -d
popd
xdg-open http://localhost:8080/

# si el mempool carrega indefinidament, obtén la sortida de depuració amb
sudo docker-compose logs -f mempool-api
* això obre un mempool a http://localhost:8080/

#### Control de l'entorn Regtest

* obtén monedes a una adreça
nigiri rpc generatetoaddress 1 bcrt1qgsnt3d4sny4w4zd5zl9x6jufc5rankqmgphyms9vz0ds73q4xfms655y4c # mine blocks

# o usa la goteig interna
nigiri faucet bcrt1qgsnt3d4sny4w4zd5zl9x6jufc5rankqmgphyms9vz0ds73q4xfms655y4c 0.01
<!-- * ## Instal·lació des de PyPi

### Ubuntu, Debian, Windows

- Instal·la `poetry` i executa `bitcoin_safe`
pip install bitcoin-safe
  python -m bitcoin_safe
### Mac

- Executa `bitcoin_safe`
python3 -m pip install bitcoin-safe
  python3 -m bitcoin_safe
-->

### Qt designer

Els components Qt es poden explorar amb el Qt designer:
virtualenv .env-qt-designer
source .env-qt-designer/bin/activate
pip install pyqt6-tools 
pyqt6-tools designer
## Política de signatura de codi


Signatura de codi gratuïta proporcionada per [SignPath.io](https://about.signpath.io/), certificat per [SignPath Foundation](https://signpath.org/)


## Política de privacitat
Aquest programa utilitza per defecte
- el servidor electrum/esplora de [blockstream.com](https://blockstream.com/) per obtenir dades de la cadena de blocs
- obté informació de comissions de mempool de [mempool.space](https://mempool.space/)

Pots especificar el teu propi servidor (personal) per a ambdós a “Configuració de xarxa”.

Quan s’activa la funcionalitat Sync&Chat s’utilitzen [relays predeterminats](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py) per transmetre dades encriptades als teus dispositius de confiança aprovats. Pots especificar el teu propi(s) relay(s) a la configuració de Sync&Chat.

Aquest programa no transferirà cap altra informació a altres sistemes en xarxa a menys que l’usuari o la persona que l’instal·la o l’opera ho sol·liciti explícitament.