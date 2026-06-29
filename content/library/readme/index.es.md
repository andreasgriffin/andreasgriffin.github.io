---
aliases:
  - "/es/features/readme/"
title: "Todas las funcionalidades"
description: "Visión general completa de la mayoría de las características de Bitcoin Safe"
draft: false
bucket: features
images: ["logo.png"]
keywords: [
  "Bitcoin Safe",
  "cartera de ahorros en bitcoin",
  "cartera MultiFirma",
  "asistente de configuración Multisig",
  "firmantes de hardware",
  "almacenamiento seguro de semillas",
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
  "soporte multilingüe",
  "etiquetado de direcciones",
  "diagramas de flujo de transacciones",
  "PSBT",
  "selección de tarifas",
  "mempool",
  "servidor Electrum",
  "Filtros de Bloques Compactos",
  "exportación CSV",
  "importación CSV",
  "BIP329",
  "arrastrar y soltar",
  "Reemplazar por tarifa",
  "PDF de copia de seguridad",
  "firma de mensajes",
  "MicroSD",
  "USB",
  "códigos QR",
  "códigos QR animados",
  "búsqueda y filtrado",
  "chat de cartera",
  "sincronización de etiquetas",
  "regtest",
  "Docker",
  "Nigiri",
  "multiplataforma",
  "instalación",
  "desarrollo"
]
weight: -10
---
<!-- header-end -->
# Bitcoin Safe

#### Una cartera de ahorros en bitcoin para toda la familia

- **Fácil** Configuración de cartera Multisig
  - Instrucciones paso a paso para una configuración segura de MultiSig con hojas de copia de seguridad PDF
  - Transacciones de prueba garantizan que todos los firmantes de hardware están listos
  - Compatibilidad total con Coldcard, Coldcard Q, Bitbox02, Blockstream Jade, Trezor, Foundation Passport Core, Keystone, Ledger, Specter DIY, SeedSigner, Krux, usando *QR*, *USB* y *tarjeta SD*
- **Seguro**: Solo firmantes de hardware
  - Todas las carteras requieren firmantes/ dispositivos de hardware para un almacenamiento seguro de la semilla
  - Alimentado por **[BDK](https://github.com/bitcoindevkit/bdk)**
- **Multi-Language**:
  - 🇺🇸 English, 🇨🇳 Chinese - 简体中文, 🇪🇸 Spanish - español de España, 🇯🇵 Japanese - 日本語, 🇷🇺 Russian - русский, 🇵🇹 Portuguese - português europeu, 🇮🇳 Hindi - हिन्दी, Arabic - العربية, 🇮🇹 Italian - italiano, 🇫🇷 French - Français, 🇩🇪 German - Deutsch, 🇲🇲 Burmese - မြန်မာ, 🇰🇷 Korean - 한국어, 🇹🇭 Thai - ภาษาไทย,  🇮🇷 Persian (Farsi) - فارسی, 🇵🇱 Polish - Polski, 🇪🇸 Catalan - Català, (more upon request)
- **Más simple** etiquetas de dirección usando categorías (p.ej., "KYC", "Non-KYC", "Trabajo", "Amigos", ...)
  - Selección automática de monedas dentro de categorías
  - Diagramas de flujo de transacciones, visualizando entradas y salidas; haz clic en entradas y salidas para seguir el flujo del dinero
- **Envío** para usuarios no técnicos
  - Selección de tarifa con 1 clic mediante bloques de mempool
  - Fusión automática de utxos cuando las tarifas son bajas
- **Sync & Chat**:
  - Respaldo en la nube cifrado (a través de nostr) de etiquetas
  - Sincronización de etiquetas entre diferentes ordenadores
  - Chat de cartera y compartición de PSBTs entre diferentes ordenadores
- **Rápido**: 
  - Sincronización con servidor Electrum
  - Mejora planificada a **Filtros de Bloques Compactos** para el lanzamiento Bitcoin Safe 2.0




### Totalmente funcional - Fácil y Potente

| **Asistente de configuración Multisig**          | **Crear un PSBT, firmar y difundir**                     |
|--------------------------------|----------------------------|
| ![Multisig setup](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/multisig-setup.gif) |  ![Send transaction](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/send.gif) |
| **Exploración de transacciones mediante un diagrama**          | **Buscar tecleando en todas las carteras**                    |
| ![Explorer](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/explorer.gif) |  ![Global search](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/global-search.gif) |
|   **Sincronización automática de etiquetas**      | **Colaboración Multisig multiparte**                  |
| ![Label sync](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/label-sync.gif)  |   ![PSBT share](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/psbt-share.gif) |
|   **Categorías de monedas**      |                 |
| ![Category drag and drop](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/category-drag-and-drop.gif)  |   |



### Disponible en todas las plataformas
| ![Windows](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-win.png) | ![Mac OS X](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-mac.png) | ![Linux](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-linux.png) |
|-----------------------------|-----------------------------|----------------------------|
| Windows                    | Mac OS X                   | Linux                     |


## Lista completa de características

- **Capacidades de importación y exportación**
  
  - Exportación CSV para todas las listas
  - Importación CSV para transacciones por lotes
  - Importación y exportación de etiquetas usando [BIP329](https://bip329.org/)
  - Importación de etiquetas desde la cartera Electrum
  - Exportación del diagrama de flujo de dinero a SVG
  - Arrastrar y soltar para Transacciones, PSBTs y archivos CSV

- **Características de la cartera**
  
  - Etiquetado simplificado de direcciones usando categorías como KYC, Non-KYC, Trabajo, Amigos
  - Aumento de tarifa en transacciones (mediante Reemplazar por tarifa)
  - Recibir más rápido (mediante Child Pays For Parents)
  - Almacenamiento de cartera encriptado
  - PDF de copia de seguridad con Descriptor (Texto y código QR)
  - Firma de mensajes vía USB y QR

- **Conectividad de firmantes de hardware**
  
  - MicroSD (archivos)
  - USB
  - Códigos QR (detección mejorada de códigos QR para cámaras de portátil)
  - Códigos QR animados incluyendo [Coldcard/BBQr](https://bbqr.org/) y formato [UR](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md)

- **Opciones de búsqueda y filtrado**
  
  - Filtrado rápido a través de txids, utxos, etiquetas, fechas, montos, categorías
  - Búsqueda en todas las carteras abiertas, txids, utxos, etiquetas, fechas, montos, categorías

- **Idiomas**
  
  - 🇺🇸 English, 🇨🇳 Chinese - 简体中文, 🇪🇸 Spanish - español de España, 🇯🇵 Japanese - 日本語, 🇷🇺 Russian - русский, 🇵🇹 Portuguese - português europeu, 🇮🇳 Hindi - हिन्दी, Arabic - العربية, 🇮🇹 Italian - italiano, 🇫🇷 French - Français, 🇩🇪 German - Deutsch, 🇲🇲 Burmese - မြန်မာ, 🇰🇷 Korean - 한국어, 🇹🇭 Thai - ภาษาไทย, 🇮🇷 Persian (Farsi) - فارسی, 🇵🇱 Polish - Polski, 🇪🇸 Catalan - Català, (more upon request)

- **Creación de transacciones / PSBT**
  
  - Selección de tarifa con 1 clic y vista previa de bloque mempool
  - Fusión automática de utxos cuando las tarifas son bajas
  - Resaltado de direcciones propias 

- **Seguridad y fiabilidad**
  
  - No generación ni almacenamiento de semillas en mainnet
  - El almacenamiento de la semilla requiere un firmante de hardware independiente  
  - Notificaciones de actualizaciones y verificación de firmas
  - Alimentado por [Bitcoin Development Kit (BDK)](https://github.com/bitcoindevkit/bdk)

- **Facilidad de uso para carteras Multisig**
  
  - Configuración simplificada para carteras multisig, incluyendo instrucciones paso a paso y hoja de copia de seguridad PDF
  - Firma de prueba con todos los firmantes de hardware
  - Gestión colaborativa de cartera incluyendo chat y compartición de PSBT vía nostr y sincronización de etiquetas entre dispositivos de confianza
  - Servidor nostr personalizado opcional 

- **Características próximas**
  
  - Para la versión 2.0
    - **Filtros de Bloques Compactos** por defecto
      - Los Filtros de Bloques Compactos son **rápidos** y **privados**
      - Los Filtros de Bloques Compactos (bdk) están siendo [trabajados](https://github.com/bitcoindevkit/bdk/issues/679), y se incluirán en bdk 1.1. Por ahora RPC, Electrum y Esplora están disponibles, pero serán reemplazados completamente por Filtros de Bloques Compactos.


## Instalación desde el repositorio Git


### Ubuntu, Debian

- Instalar dependencias: 
sudo apt-get install qt6-tools-dev-tools libzbar-dev libxcb-cursor0 '^libqt6.*$'
- Instalar `poetry` y ejecutar `bitcoin_safe`
git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
  pip install poetry  && poetry install && poetry run python -m bitcoin_safe
### Mac

- Clonar `bitcoin_safe`
open "/Applications/Python 3.12/Install Certificates.command"
  export SSL_CERT_FILE=$(python3 -m certifi) # to fix ssl errors
  git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
- *Opcional*: dependencia `zbar`
brew install zbar
- Ejecutar `bitcoin_safe`
python3 -m pip install poetry && python3 -m poetry install && python3 -m poetry run python3 -m bitcoin_safe
## Desarrollo

* Ejecutar el precommit manualmente para depuración
poetry run pre-commit run --all-files
#### Entorno Regtest Docker con electrs y mempool

* instalar docker
# ver https://docs.docker.com/engine/install/ubuntu/
* configurar un entorno regtest en docker + instancia mempool
curl https://getnigiri.vulpem.com | sudo bash # ver https://nigiri.vulpem.com/#install
sudo nigiri start
xdg-open http://localhost:5000/
* Esto crea
  * esplora localhost:3000
    electrs localhost:30000 
  * y un explorador gráfico en http://localhost:5000
* Configurar instancia mempool
sudo apt install docker-compose
git clone https://github.com/ngutech21/nigiri-mempool.git

pushd nigiri-mempool
sudo docker-compose up -d
sleep 10
# esto es necesario porque la base de datos necesita tiempo para iniciarse 
sudo docker-compose up -d
popd
xdg-open http://localhost:8080/

# si el mempool se carga indefinidamente, obtener la salida de depuración con
sudo docker-compose logs -f mempool-api
* esto abre un mempool en http://localhost:8080/

#### Controlar el entorno Regtest

* obtener monedas a una dirección
nigiri rpc generatetoaddress 1 bcrt1qgsnt3d4sny4w4zd5zl9x6jufc5rankqmgphyms9vz0ds73q4xfms655y4c # minar bloques

# o usar la fuente interna
nigiri faucet bcrt1qgsnt3d4sny4w4zd5zl9x6jufc5rankqmgphyms9vz0ds73q4xfms655y4c 0.01
<!-- * ## Instalación desde PyPi

### Ubuntu, Debian, Windows

- Instalar `poetry` y ejecutar `bitcoin_safe`
pip install bitcoin-safe
  python -m bitcoin_safe
### Mac

- Ejecutar `bitcoin_safe`
python3 -m pip install bitcoin-safe
  python3 -m bitcoin_safe
-->

### Diseñador Qt

Los componentes Qt pueden explorarse con el diseñador Qt:
virtualenv .env-qt-designer
source .env-qt-designer/bin/activate
pip install pyqt6-tools 
pyqt6-tools designer
## Política de firma de código


Firma de código gratuita proporcionada por [SignPath.io](https://about.signpath.io/), certificado por [SignPath Foundation](https://signpath.org/)


## Política de privacidad
Este programa usa por defecto
- el servidor electrum/esplora de [blockstream.com](https://blockstream.com/) para obtener datos de la cadena de bloques
- obtiene información de tarifas del mempool de [mempool.space](https://mempool.space/)

Puedes especificar tu propio servidor (personal) para ambos en "Configuración de red".

Al habilitar la función Sync&Chat se usan los [relays predeterminados](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py) para transmitir datos cifrados a tus dispositivos de confianza aprobados. Puedes especificar tu(s) propio(s) relay(s) en la configuración Sync&Chat.

Este programa no transferirá ninguna otra información a sistemas de red externos a menos que el usuario o la persona que lo instala o lo opera lo solicite expresamente.