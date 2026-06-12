---
title: "Todas as funcionalidades"
description: "Visão geral abrangente da maioria das funcionalidades do Bitcoin Safe"
draft: false
tags: [ "Features" ]
images: ["logo.png"]
keywords: [
  "Bitcoin Safe",
  "carteira de poupança Bitcoin",
  "carteira MultiSig",
  "assistente de configuração Multisig",
  "assinantes de hardware",
  "armazenamento seguro de seed",
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
  "suporte multilíngue",
  "rotulagem de endereços",
  "diagramas de fluxo de transação",
  "PSBT",
  "seleção de taxa",
  "mempool",
  "servidor Electrum",
  "Filtros de Blocos Compactos",
  "exportação CSV",
  "importação CSV",
  "BIP329",
  "arrastar e largar",
  "Replace-by-Fee",
  "PDF de backup",
  "assinatura de mensagens",
  "MicroSD",
  "USB",
  "códigos QR",
  "códigos QR animados",
  "busca e filtragem",
  "chat da carteira",
  "sincronização de rótulos",
  "regtest",
  "Docker",
  "Nigiri",
  "multiplataforma",
  "instalação",
  "desenvolvimento"
]
weight: -10
---
<!-- header-end -->
# Bitcoin Safe

#### Uma carteira de poupança Bitcoin para toda a família

- **Fácil** Configuração de Carteira Multisig
  - Instruções passo‑a‑passo para uma configuração segura de MultiSig com folhas de backup PDF
  - Transações de teste garantem que todos os assinantes de hardware estão prontos
  - Suporte total para [Coldcard](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Coldcard Q](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Bitbox02](https://shop.bitbox.swiss/?ref=MOB4dk7gpm), [Blockstream Jade](https://store.blockstream.com/?code=XEocg5boS77D), [Trezor](https://affil.trezor.io/SHtN), [Foundation Passport Core](https://foundation.xyz/?ref=cbyqjjxumy), [Keystone](https://keyst.one), [Ledger](https://shop.ledger.com/?r=400f1fff75b5), [Specter DIY](https://clavastack.com/en/?coupon=bitcoin-safe), [SeedSigner](https://seedsigner.com), [Krux](https://selfcustody.github.io/krux), usando *QR*, *USB* e *SD‑card*
- **Seguro**: apenas assinantes de hardware
  - Todas as carteiras requerem assinantes/dispositivos de hardware para armazenamento seguro da seed
  - Alimentado por **[BDK](https://github.com/bitcoindevkit/bdk)**
- **Multi‑Linguagem**:
  - 🇺🇸 English, 🇨🇳 Chinese - 简体中文, 🇪🇸 Spanish - español de España, 🇯🇵 Japanese - 日本語, 🇷🇺 Russian - русский, 🇵🇹 Portuguese - português europeu, 🇮🇳 Hindi - हिन्दी, Arabic - العربية, 🇮🇹 Italian - italiano, 🇫🇷 French - Français, 🇩🇪 German - Deutsch, 🇲🇲 Burmese - မြန်မာ, 🇰🇷 Korean - 한국어, 🇹🇭 Thai - ภาษาไทย, ", "Friends",  - Diagramas de fluxo de transação, visualizando inputs e outputs, clique nos inputs e outputs para rastrear o fluxo de dinheiro
- **Envio** para utilizadores não‑técnicos
  - Seleção de taxa com 1 clique via blocos mempool
  - Fusãoótulos entre diferentes computadores
  - Chat da carteira e partilha de PSBTs entre diferentes computadores
- **Rápido**: 
  - Sincronização com servidor Electrum
  - Atualização planejada para **Compact Block Filters** para o lançamento Bitcoin Safe 2.0 




### Totalmente funcional – Fácil e Poderoso

| **Assistente de configuração Multisig**          | **Criar um PSBT, assinar e difundir**                     |
|--------------------------------|----------------------------|
| ![Multisig setup](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/multisig-setup.gif) |  ![Send transaction](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/send.gif) |
| **Exploração de transações via diagrama**          | **Pesquisa por digitação em todas as carteiras**                    |
| ![Explorer](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/explorer.gif) |  ![Global search](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/global-search.gif) |
|   **Sincronização automática de rótulos**      | **Colaboração Multisig multi‑parte**                  |
| ![Label sync](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/label-sync.gif)  |   ![PSBT share](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/psbt-share.gif) |
|   **Categorias de moedas**      |                 |
| ![Category drag and drop](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/category-drag-and-drop.gif)  |   |



### Disponível em todas as plataformas
| ![Windows](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-win.png) | ![Mac OS X](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-mac.png) | ![Linux](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-linux.png) |
|-----------------------------|-----------------------------|----------------------------|
| Windows                    | Mac OS X                   | Linux                     |


## Lista abrangente de funcionalidades

- **Capacidades de Importação e Exportação**
  
  - Exportação CSV para todas as listas
  - Importação CSV para transações em lote
  - Importação e exportação de rótulos usando [BIP329](https://bip329.org/)
  - Importação de rótulos da carteira Electrum
  - Exportação do diagrama de fluxo de dinheiro para SVG
  - Arrastar e largar para Transações, PSBTs e arquivos CSV

- **Funcionalidades da Carteira**
  
  - Rotulagem simplificada de endereços usando categorias como KYC, Non‑KYC, Work, Friends
  - Aumento de taxa nas transações (via Replace‑by‑Fee)
  - Receber mais rápido (via Child Pays For Parents)
  - Armazenamento encriptado da carteira
  - PDF de backup com Descriptor (texto e código QR)
  - Assinatura de mensagens via USB e QR

- **Conectividade de Assinantes de Hardware**
  
  - MicroSD (ficheiros)
  - USB
  - Códigos QR (detecção avançada de QR para câmaras de laptop)
  - Códigos QR animados incluindo [Coldcard/BBQr](https://bbqr.org/) e formato [UR](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md)

- **Opções de Busca e Filtragem**
  
  - Filtragem rápida entre txids, utxos, rótulos, datas, montantes, categorias
  - Busca em todas as carteiras abertas, txids, utxos, rótulos, datas, montantes, categorias

- **Línguas**
  
  - 🇺🇸 English, 🇨🇳 Chinese - 简体中文, 🇪🇸 Spanish - español de España, 🇯🇵 Japanese - 日本語, 🇷🇺 Russian - русский, 🇵🇹 Portuguese - português europeu, 🇮🇳 Hindi - हिन्दी, Arabic - العربية, 🇮🇹 Italian - italiano, 🇫🇷 French - Français, 🇩🇪 German - Deutsch, 🇲🇲 Burmese - မြန်မာ, 🇰🇷 Korean - 한국어, 🇹🇭 Thai - ภาษาไทย, 🇮🇷 Persian (Farsi) - فارسی, 🇵🇱 Polish - Polski, 🇪🇸 Catalan - Català, (more upon request)

- **Criação de Transação / PSBT**
  
  - Seleção de taxa com 1 clique e pré‑visualização de bloco mempool
  - Fusão automática de utxos quando as taxas são baixas
  - Realce dos próprios endereços 

- **Segurança e Fiabilidade**
  
  - Nenhuma geração ou armazenamento de seed na mainnet
  - Armazenamento de seed requer um assinante de hardware separado  
  - Notificações de atualização e verificação de assinatura
  - Alimentado pelo Bitcoin Development Kit (BDK)

- **Facilidade de Uso para Carteiras Multisig**
  
  - Configuração simplificada para carteiras multisig, incluindo instruções passo‑a‑passo e folha de backup PDF
  - Assinatura de teste com todos os assinantes de hardware
  - Gestão colaborativa da carteira incluindo chat e partilha de PSBT via nostr e sincronização de rótulos entre dispositivos de confiança
  - Servidor nostr personalizado opcional 

- **Funcionalidades Futuras**
  
  - Para o Lançamento 2.0
    - **Filtros de Blocos Compactos** por defeito
      - Filtros de Blocos Compactos são **rápidos** e **privados**
      - Filtros de Blocos Compactos (bdk) estão a ser desenvolvidos e serão incluídos no bdk 1.1. Por enquanto, RPC, Electrum e Esplora estão disponíveis, mas serão substituídos completamente por Filtros de Blocos Compactos.


## Instalação a partir do repositório Git


### Ubuntu, Debian

- Instalar dependências: 
sudo apt-get install qt6-tools-dev-tools libzbar-dev libxcb-cursor0 '^libqt6.*$'
- Instalar `poetry` e executar `bitcoin_safe`
git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
  pip install poetry  && poetry install && poetry run python -m bitcoin_safe
### Mac

- Clonar `bitcoin_safe`
open "/Applications/Python 3.12/Install Certificates.command"
  export SSL_CERT_FILE=$(python3 -m certifi) # to fix ssl errors
  git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
- *Opcional*: dependência `zbar`
brew install zbar
- Executar `bitcoin_safe`
python3 -m pip install poetry && python3 -m poetry install && python3 -m poetry run python3 -m bitcoin_safe
## Desenvolvimento

* Executar o pre‑commit manualmente para depuração
poetry run pre-commit run --all-files
#### Ambiente Regtest Docker com electrs e mempool

* instalar docker
# see https://docs.docker.com/engine/install/ubuntu/
* configurar um ambiente regtest em docker + instância mempool
curl https://getnigiri.vulpem.com | sudo bash # see https://nigiri.vulpem.com/#install
sudo nigiri start
xdg-open http://localhost:5000/
* Isto cria
  * esplora localhost:3000
    electrs localhost:50000 
  * e um explorador de blocos GUI em http://localhost:5000
* Configurar instância mempool
sudo apt install docker-compose
git clone https://github.com/ngutech21/nigiri-mempool.git

pushd nigiri-mempool
sudo docker-compose up -d
sleep 10
# isto é necessário porque a base de dados precisa de tempo para iniciar 
sudo docker-compose up -d
popd
xdg-open http://localhost:8080/

# se o mempool ficar a carregar indefinidamente, obtenha o output de depuração com
sudo docker-compose logs -f mempool-api
* isto abre um mempool em http://localhost:8080/

#### Controlar o ambiente Regtest

* obter moedas para um endereço
nigiri rpc generatetoaddress 1 bcrt1qgsnt3d4sny4w4zd5zl9x6jufc5rankqmgphyms9vz0ds73q4xfms655y4c # mine blocks

# ou usar a torneira interna
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

Componentes Qt podem ser explorados com o Qt Designer:
virtualenv .env-qt-designer
source .env-qt-designer/bin/activate
pip install pyqt6-tools 
pyqt6-tools designer
## Política de assinatura de código


Assinatura de código gratuita fornecida por [SignPath.io](https://about.signpath.io/), certificado por [SignPath Foundation](https://signpath.org/)


## Política de privacidade
Este programa usa por defeito
- o servidor electrum/esplora de [blockstream.com](https://blockstream.com/) para obter dados da blockchain
- obtém informações de taxas do mempool a partir de [mempool.space](https://mempool.space/)

Pode especificar o seu próprio servidor (pessoal) para ambos nas "Definições de Rede".

Ao activar a funcionalidade Sync&Chat são usados os [relés padrão](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py) para transmitir dados encriptados aos seus dispositivos de confiança aprovados. Pode especificar o(s) seu(s)