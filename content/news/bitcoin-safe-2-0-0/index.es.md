---
title: "Bitcoin-Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "Notas de la version de Bitcoin-Safe 2.0.0, con un asistente de configuracion reconstruido, sincronizacion privada con Compact Block Filters y soporte ampliado para hardware wallets."
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">Anuncio de lanzamiento</p>
    <h2 class="display-6 mb-3">Bitcoin-Safe 2.0 - configuracion guiada de wallets, sincronizacion privada de la cadena y firma centrada en dispositivos</h2>
    <p class="lead mb-4">Esta version trae un asistente de configuracion reconstruido, sincronizacion privada de la cadena con Compact Block Filters y un flujo de firma organizado alrededor de cada dispositivo de hardware. Si tenias curiosidad por el cold storage pero no estabas seguro, esta es la version para probar.</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Descargar Bitcoin-Safe 2.0</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">Ver que hay de nuevo</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Configuracion de wallet paso a paso</h2>
          <p class="mb-0">El nuevo asistente explica cada paso, reduce la ambiguedad y ayuda a las personas nuevas a elegir el camino correcto sin perder la potencia de multisig.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Sincronizacion privada de la wallet</h2>
          <p class="mb-0">Las nuevas wallets ahora se sincronizan con Compact Block Filters desde el primer momento, para que puedas escanear la cadena en privado sin depender de un indexador Electrum de terceros.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Firma centrada en dispositivos</h2>
          <p class="mb-0">Los flujos de firma ahora se mantienen centrados en el dispositivo que tienes delante, con pasos siguientes mas claros para QR, USB, Bluetooth, archivos y coordinacion multisig.</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## Un camino guiado hacia la autocustodia {#setup-flow}

La experiencia del primer uso se ha reconstruido desde cero. Bitcoin-Safe sigue orientado a la autocustodia seria, incluida la multisig respaldada por hardware, y ahora 2.0 ofrece a las personas nuevas un camino guiado por esa configuracion. El nuevo asistente explica que esta ocurriendo, en que parte del flujo te encuentras y que necesita cada signer antes de que continues.

<p class="small text-muted">Para detalles de implementacion, consulta el <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a>.</p>

Aspectos destacados del rediseño:

- Una nueva pantalla de bienvenida que ayuda a quienes llegan por primera vez a elegir el punto de partida correcto
- Un flujo de progreso paso a paso durante la creacion de la wallet
- Pantallas de firma especificas para cada dispositivo con instrucciones centradas y ayuda contextual
- PDFs de recuperacion con nombres e iconos de dispositivos para que las copias de seguridad sigan siendo claras

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## Sincronizacion privada y robusta de la cadena con Compact Block Filters {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) ahora impulsan la sincronizacion de wallets nuevas en Bitcoin-Safe 2.0. En lugar de preguntarle a un servidor Electrum que direcciones te pertenecen, Bitcoin-Safe ahora puede escanear la cadena de forma privada descargando filtros compactos desde nodos aleatorios de Bitcoin Core y comprobando todo localmente.

<p class="small text-muted">Para detalles de implementacion, consulta el <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a>.</p>


- La sincronizacion de la wallet se mantiene privada desde el primer inicio
- Sin dependencia de servidores Electrum de terceros
- Electrum sigue disponible para quienes lo prefieran
- [Sincronizacion instantanea despues del escaneo inicial de la wallet]({{< ref "library/compact-block-filters" >}})
- [Notificaciones instantaneas de transacciones retransmitidas]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## Un flujo de firma centrado en el dispositivo para cada equipo {#device-focused-signing}

El rediseño tambien reorganiza el flujo de firma despues de la creacion de la wallet. En lugar de una pantalla generica para todos los signers, Bitcoin-Safe ahora centra las acciones alrededor del dispositivo concreto que estas usando.

<p class="small text-muted">Para detalles de implementacion, consulta el <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a>.</p>

- Las acciones de QR, USB, Bluetooth, exportacion/importacion de archivos y Sync & Chat se muestran directamente en la tarjeta del signer activo
- Los signers restantes, los dispositivos ya firmados y la siguiente accion necesaria siguen visibles de un vistazo
- Los flujos multisig con dispositivos mixtos siguen siendo legibles porque la identidad de cada signer permanece visible durante todo el PSBT
- Las transacciones complejas con una mezcla de entradas single-sig y multisig se gestionan correctamente, de modo que cada paso de firma queda claro

![Tarjeta de signer con acciones especificas para QR, USB, Bluetooth, exportacion de archivos y Chat & Sync](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Arquitectura de plugins para flujos de trabajo empresariales y usuarios avanzados

Bitcoin-Safe 2.0 tambien sienta las bases para futuros plugins adicionales dirigidos a empresas de Bitcoin y a usuarios avanzados. Asi que vale la pena estar atentos a lo que viene :-)

<p class="small text-muted">Para detalles de implementacion, consulta el <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a>.</p>

- Distribucion de plugins mediante un repositorio externo de *sources*
- Cada plugin esta *firmado con GPG* por [andreasgriffin]({{< gpg_key_link >}}) para garantizar la seguridad, integridad y distribucion del plugin
- El versionado individual de plugins y las actualizaciones permiten un desarrollo mas rapido e independiente

![Tarjeta de signer con acciones especificas para QR, USB, Bluetooth, exportacion de archivos y Chat & Sync](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Mas soporte para dispositivos y mas pulido {#hardware-support}

- Codigos QR animados **30%** mas rapidos para escanear mas rapido
- Ahora se admite [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) por USB
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) ahora admite **Bluetooth**, ademas de USB y QR
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) y [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) se añaden como dispositivos compatibles
- Consulta la [lista completa de dispositivos compatibles]({{< ref "library/supported-hardware-signers" >}})
- Se añadieron comprobaciones automatizadas para la [reproducibilidad]({{< ref "library/reproducibility-and-security" >}})
- Consulta aqui la [lista completa](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0) de mejoras


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## Las fortalezas de siempre siguen aqui

La version 2.0 no es un reinicio. Debajo del nuevo flujo de incorporacion y firma, Bitcoin-Safe sigue manteniendo las funciones que lo hacian util cada dia: multisig colaborativo, copias de seguridad en PDF, historial de wallet con busqueda, visualizaciones de flujo de dinero, sincronizacion de etiquetas y mas.

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">Listo para probar Bitcoin-Safe 2.0?</h2>
  <p class="mb-3">Descarga la ultima version y explora por ti mismo la nueva incorporacion, la sincronizacion privada y las mejoras para hardware wallets.</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Descargar Bitcoin-Safe</a>
</div>


<br><br>

## Gracias

Esta version se apoya en mucho trabajo de colaboradores, testers y [personas que apoyan el proyecto]({{< ref "donate" >}}):

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r)) por el rediseño del asistente, el trabajo de interfaz para plugins y un apoyo de UI/UX **increible e incansable**
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) por el cliente de Compact Block Filters que ahora impulsa la sincronizacion privada de wallets nuevas
- El [equipo de Bitcoin Dev Kit](https://github.com/bitcoindevkit/) por las bibliotecas en el nucleo de Bitcoin-Safe
- El [equipo de ndk](https://github.com/nostr-dev-kit/ndk) por las bibliotecas que impulsan la funcionalidad de nostr
- Toda la comunidad de Bitcoin-Safe que probo versiones candidatas, reporto errores, tradujo paginas, envio sats y siguio empujando el proyecto hacia adelante
- [Traductores]({{< ref "donate/#translators" >}}), entre ellos <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (Vietnamita)" title="qdyg-vn 🇻🇳 (Vietnamita)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (Aleman)" title="bsn21m 🇩🇪 (Aleman)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (Espanol)" title="cyphra 🇪🇸 (Espanol)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (Chino)" title="DaGrindDontStop 🇨🇳 (Chino)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


Si quieres ayudar a financiar la proxima version, tambien puedes donar aqui: {{< donation_btc >}}
