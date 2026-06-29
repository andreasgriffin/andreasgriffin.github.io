---
aliases:
  - "/fr/features/readme/"
title: "Toutes les fonctionnalités"
description: "Aperçu complet de la plupart des fonctionnalités de Bitcoin Safe"
draft: false
bucket: features
images: ["logo.png"]
keywords: [
  "Bitcoin Safe",
  "portefeuille d'épargne Bitcoin",
  "portefeuille MultiSig",
  "assistant de configuration Multisig",
  "signataires matériels",
  "stockage sécurisé de la seed",
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
  "prise en charge multilingue",
  "étiquetage d'adresses",
  "diagrammes de flux de transaction",
  "PSBT",
  "sélection des frais",
  "mempool",
  "serveur Electrum",
  "Compact Block Filters",
  "export CSV",
  "import CSV",
  "BIP329",
  "glisser-déposer",
  "Replace-by-Fee",
  "PDF de sauvegarde",
  "signature de message",
  "MicroSD",
  "USB",
  "codes QR",
  "codes QR animés",
  "recherche et filtrage",
  "chat de portefeuille",
  "synchronisation des étiquettes",
  "regtest",
  "Docker",
  "Nigiri",
  "multi-plateforme",
  "installation",
  "développement"
]
weight: -10
---
<!-- header-end -->
# Bitcoin Safe

#### Un portefeuille d'épargne Bitcoin pour toute la famille

- **Configuration Multisig simple**
  - Instructions étape par étape pour une configuration MultiSig sécurisée avec feuilles de sauvegarde PDF
  - Des transactions de test garantissent que tous les signataires matériels sont prêts
  - Prise en charge complète de [Coldcard](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Coldcard Q](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Bitbox02](https://shop.bitbox.swiss/?ref=MOB4dk7gpm), [Blockstream Jade](https://store.blockstream.com/?code=XEocg5boS77D), [Trezor](https://affil.trezor.io/SHtN), [Foundation Passport Core](https://foundation.xyz/?ref=cbyqjjxumy), [Keystone](https://keyst.one), [Ledger](https://shop.ledger.com/?r=400f1fff75b5), [Specter DIY](https://clavastack.com/en/?coupon=bitcoin-safe), [SeedSigner](https://seedsigner.com), [Krux](https://selfcustody.github.io/krux), via *QR*, *USB* et *carte SD*
- **Sécurisé** : uniquement des signataires matériels
  - Tous les portefeuilles requièrent des signataires/portefeuilles matériels pour un stockage sûr de la seed
  - Propulsé par **[BDK](https://github.com/bitcoindevkit/bdk)**
- **Multilingue** :
  - 🇺🇸 Anglais, 🇨🇳 Chinois - 简体中文, 🇪🇸 Espagnol - español de España, 🇯🇵 Japonais - 日本語, 🇷🇺 Russe - русский, 🇵🇹 Portugais - português europeu, 🇮🇳 Hindi - हिन्दी, Arabe - العربية, 🇮🇹 Italien - italiano, 🇫🇷 Français - Français, 🇩🇪 Allemand - Deutsch, 🇲🇲 Birman - မြန်မာ, 🇰🇷 Coréen - 한국어, 🇹🇭 Thaï - ภาษาไทย, 🇮🇷 Persan (Farsi) - فارسی, 🇵🇱 Polonais - Polski, 🇪🇸 Catalan - Català, (plus sur demande)
- **Simplification** des étiquettes d'adresses grâce aux catégories (par ex. "KYC", "Non-KYC", "Travail", "Amis", ...)
  - Sélection automatique des pièces (coin selection) au sein des catégories
  - Diagrammes de flux de transaction, visualisant les entrées et sorties ; cliquez sur les entrées et les sorties pour suivre le flux d'argent
- **Envoi** pour les utilisateurs non techniques
  - Sélection des frais en 1 clic via mempool-blocks
  - Fusion automatique des UTXO lorsque les frais sont bas
- **Synchronisation & Chat** :
  - Sauvegarde chiffrée dans le cloud (via nostr) des étiquettes
  - Synchronisation des étiquettes entre différents ordinateurs
  - Chat de portefeuille et partage de PSBT entre différents ordinateurs
- **Rapide** :
  - Synchronisation via un serveur Electrum
  - mise à niveau prévue vers **Compact Block Filters** pour la version Bitcoin Safe 2.0




### Fonctionnalités complètes — Simple et puissant

| **Assistant de configuration Multisig**          | **Créer une PSBT, signer et diffuser (broadcast)**                     |
|--------------------------------|----------------------------|
| ![Multisig setup](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/multisig-setup.gif) |  ![Send transaction](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/send.gif) |
| **Exploration des transactions via un diagramme**          | **Recherche à la frappe dans tous les portefeuilles**                    |
| ![Explorer](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/explorer.gif) |  ![Global search](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/global-search.gif) |
|   **Synchronisation automatique des étiquettes**      | **Collaboration multiacteurs pour Multisig**                  |
| ![Label sync](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/label-sync.gif)  |   ![PSBT share](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/psbt-share.gif) |
|   **Catégories de pièces (Coin Categories)**      |                 |
| ![Category drag and drop](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/category-drag-and-drop.gif)  |   |



### Disponible sur toutes les plateformes
| ![Windows](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-win.png) | ![Mac OS X](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-mac.png) | ![Linux](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-linux.png) |
|-----------------------------|-----------------------------|----------------------------|
| Windows                    | Mac OS X                   | Linux                     |


## Liste complète des fonctionnalités

- **Capacités d'import et d'export**
  
  - Export CSV pour toutes les listes
  - Import CSV pour les transactions en lot
  - Import et export d'étiquettes en utilisant [BIP329](https://bip329.org/)
  - Import d'étiquettes depuis le portefeuille Electrum
  - Export du diagramme de flux d'argent en SVG
  - Glisser-déposer pour Transactions, PSBT et fichiers CSV

- **Fonctionnalités du portefeuille**
  
  - Étiquetage d'adresses simplifié en utilisant des catégories comme KYC, Non-KYC, Travail, Amis
  - Augmentation des frais sur les transactions (via Replace-by-Fee)
  - Recevoir plus rapidement (via Child Pays For Parents)
  - Stockage du portefeuille chiffré
  - PDF de sauvegarde avec Descriptor (texte et code QR)
  - Signature de messages via USB et QR

- **Connectivité des signataires matériels**
  
  - MicroSD (fichiers)
  - USB
  - Codes QR (détection améliorée des QR pour les caméras d'ordinateur portable)
  - Codes QR animés incluant [Coldcard/BBQr](https://bbqr.org/) et le format [UR](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md)

- **Options de recherche et de filtrage**
  
  - Filtrage rapide sur txids, utxos, étiquettes, dates, montants, catégories
  - Recherche à travers tous les portefeuilles ouverts, txids, utxos, étiquettes, dates, montants, catégories

- **Langues**
  
  - 🇺🇸 Anglais, 🇨🇳 Chinois - 简体中文, 🇪🇸 Espagnol - español de España, 🇯🇵 Japonais - 日本語, 🇷🇺 Russe - русский, 🇵🇹 Portugais - português europeu, 🇮🇳 Hindi - हिन्दी, Arabe - العربية, 🇮🇹 Italien - italiano, 🇫🇷 Français - Français, 🇩🇪 Allemand - Deutsch, 🇲🇲 Birman - မြန်မာ, 🇰🇷 Coréen - 한국어, 🇹🇭 Thaï - ภาษาไทย, 🇮🇷 Persan (Farsi) - فارسی, 🇵🇱 Polonais - Polski, 🇪🇸 Catalan - Català, (plus sur demande)

- **Création de transaction / PSBT**
  
  - Sélection des frais en 1 clic et aperçu des blocs mempool
  - Fusion automatique des UTXO lorsque les frais sont bas
  - Mise en évidence des adresses propres (possédées)

- **Sécurité et fiabilité**
  
  - Aucune génération ou stockage de seed sur le mainnet
  - Le stockage de la seed nécessite un signataire matériel séparé  
  - Notifications de mise à jour et vérification des signatures
  - Propulsé par [Bitcoin Development Kit (BDK)](https://github.com/bitcoindevkit/bdk)

- **Facilité d'utilisation pour les portefeuilles Multisig**
  
  - Configuration simplifiée des portefeuilles multisig, incluant des instructions pas-à-pas et une feuille de sauvegarde PDF
  - Test de signature avec tous les signataires matériels
  - Gestion collaborative des portefeuilles incluant chat et partage de PSBT via nostr et synchronisation des étiquettes entre appareils de confiance
  - Serveur nostr personnalisé optionnel

- **Fonctionnalités à venir**
  
  - Pour la version 2.0
    - **Compact Block Filters** par défaut
      - Les Compact Block Filters sont **rapides** et **privés**
      - Les Compact Block Filters (bdk) sont en cours de développement ([work in progress](https://github.com/bitcoindevkit/bdk/issues/679)), et seront inclus dans bdk 1.1. Pour l'instant RPC, Electrum et Esplora sont disponibles, mais seront entièrement remplacés par les Compact Block Filters.


## Installation depuis le dépôt Git


### Ubuntu, Debian

- Installer les dépendances : 
sudo apt-get install qt6-tools-dev-tools libzbar-dev libxcb-cursor0 '^libqt6.*$'
- Installer `poetry` et lancer `bitcoin_safe`
git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
  pip install poetry  && poetry install && poetry run python -m bitcoin_safe
### Mac

- Cloner `bitcoin_safe`
open "/Applications/Python 3.12/Install Certificates.command"
  export SSL_CERT_FILE=$(python3 -m certifi) # to fix ssl errors
  git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
- *Optionnel* : dépendance `zbar`
brew install zbar
- Lancer `bitcoin_safe`
python3 -m pip install poetry && python3 -m poetry install && python3 -m poetry run python3 -m bitcoin_safe
## Développement

* Exécuter manuellement le precommit pour le débogage
poetry run pre-commit run --all-files
#### Environnement regtest Docker avec electrs et mempool

* installer docker
# see https://docs.docker.com/engine/install/ubuntu/
* mise en place d'un environnement regtest dans Docker + instance mempool
curl https://getnigiri.vulpem.com | sudo bash # see https://nigiri.vulpem.com/#install
sudo nigiri start
xdg-open http://localhost:5000/
* Cela crée
  * esplora localhost:3000
    electrs localhost:50000 
  * et un explorateur de blocs GUI à http://localhost:5000
* Configuration de l'instance mempool
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
* cela ouvre un mempool à http://localhost:8080/

#### Contrôler l'environnement Regtest

* obtenir des coins vers une adresse
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

Les composants Qt peuvent être explorés avec le Qt Designer :
virtualenv .env-qt-designer
source .env-qt-designer/bin/activate
pip install pyqt6-tools 
pyqt6-tools designer
## Politique de signature du code


Signature de code gratuite fournie par [SignPath.io](https://about.signpath.io/), certificat par [SignPath Foundation](https://signpath.org/)


## Politique de confidentialité
Ce programme utilise par défaut
- le serveur electrum/esplora de [blockstream.com](https://blockstream.com/) pour récupérer les données de la blockchain
- récupère les informations de frais du mempool depuis [mempool.space](https://mempool.space/)

Vous pouvez spécifier votre propre serveur (personnel) pour les deux dans les "Network settings".

Lors de l'activation de la fonctionnalité Synchronisation & Chat, des [relais par défaut](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py) sont utilisés pour transmettre des données chiffrées vers vos appareils approuvés et de confiance. Vous pouvez spécifier votre(s) propre(s) relais dans les paramètres Sync&Chat.

Ce programme ne transférera aucune autre information vers d'autres systèmes réseau sauf si cela est spécifiquement demandé par l'utilisateur ou la personne l'installant ou l'exploitant.