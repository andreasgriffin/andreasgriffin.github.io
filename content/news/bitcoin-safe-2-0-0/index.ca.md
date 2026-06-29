---
title: "Bitcoin Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "Notes de la versio de Bitcoin Safe 2.0.0, amb un assistent de configuracio reconstruït, sincronitzacio privada amb Compact Block Filters i suport ampliat per a carteres de maquinari."
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">Anunci de llançament</p>
    <h2 class="display-6 mb-3">Bitcoin Safe 2.0 - configuracio guiada de la cartera, sincronitzacio privada de la cadena i signatures centrades en el dispositiu</h2>
    <p class="lead mb-4">Aquesta versio incorpora un assistent de configuracio reconstruït, sincronitzacio privada de la cadena amb Compact Block Filters i un flux de signatura organitzat al voltant de cada dispositiu de maquinari. Si tenies curiositat pel cold storage pero no ho tenies clar, aquesta es la versio que has de provar.</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Descarrega Bitcoin Safe 2.0</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">Veure les novetats</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Configuracio de la cartera pas a pas</h2>
          <p class="mb-0">El nou assistent explica cada pas, redueix l'ambigüitat i ajuda les persones noves a escollir el cami correcte sense perdre la potencia del multisig.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Sincronitzacio privada de la cartera</h2>
          <p class="mb-0">Les carteres noves ara se sincronitzen amb Compact Block Filters des del primer moment, de manera que pots escanejar la cadena en privat sense dependre d'un indexador Electrum de tercers.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Signatura centrada en el dispositiu</h2>
          <p class="mb-0">Els fluxos de signatura ara es mantenen centrats en el dispositiu que tens davant, amb passos seguents mes clars per a QR, USB, Bluetooth, fitxers i coordinacio multisig.</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## Un cami guiat cap a l'autocustodia {#setup-flow}

L'experiencia del primer inici s'ha reconstruït des de zero. Bitcoin Safe continua pensat per a una autocustodia seriosa, incloent-hi multisig amb suport de maquinari, i ara la versio 2.0 ofereix a les persones noves un cami guiat per aquesta configuracio. El nou assistent explica que esta passant, en quin punt del flux et trobes i que necessita cada signer abans de continuar.

<p class="small text-muted">Per als detalls d'implementacio, consulta la <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a>.</p>

Punts destacats del redisseny:

- Una nova pantalla de benvinguda que ajuda qui comença a escollir el punt de partida correcte
- Un flux de progres pas a pas durant la creacio de la cartera
- Pantalles de signatura especifiques per dispositiu amb instruccions centrades i ajuda contextual
- PDFs de recuperacio amb noms i icones dels dispositius per mantenir les copies de seguretat sense ambigüitats

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## Sincronitzacio privada i robusta de la cadena amb Compact Block Filters {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) ara impulsen la sincronitzacio de carteres noves a Bitcoin Safe 2.0. En lloc de preguntar a un servidor Electrum quines adreces et pertanyen, Bitcoin Safe ara pot escanejar la cadena de manera privada descarregant filtres compactes de nodes aleatoris de Bitcoin Core i comprovant-los localment.

<p class="small text-muted">Per als detalls d'implementacio, consulta la <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a>.</p>


- La sincronitzacio de la cartera es manté privada des del primer inici
- Sense dependencia de servidors Electrum de tercers
- Electrum continua disponible per a qui el prefereixi
- [Sincronitzacio instantania despres de l'escaneig inicial de la cartera]({{< ref "library/compact-block-filters" >}})
- [Notificacions instantanies de transaccions retransmeses]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## Un flux de signatura centrat en el dispositiu per a cada dispositiu {#device-focused-signing}

El redisseny tambe remodela el flux de signatura despres de crear la cartera. En lloc d'una pantalla generica per a tots els signers, Bitcoin Safe ara centra les accions al voltant del dispositiu concret que estas fent servir.

<p class="small text-muted">Per als detalls d'implementacio, consulta la <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a>.</p>

- Les accions de QR, USB, Bluetooth, exportacio/importacio de fitxers i Sync & Chat es mostren directament a la targeta del signer actiu
- Els signers restants, els dispositius que ja han signat i la seguent accio necessaria es mantenen visibles d'un cop d'ull
- Els fluxos multisig amb dispositius barrejats continuen sent llegibles perque la identitat de cada signer es manté visible durant tot el PSBT
- Les transaccions complexes amb una barreja d'entrades single-sig i multisig es gestionen correctament, de manera que cada pas de signatura queda clar

![Targeta del signer amb accions especifiques per al dispositiu per a QR, USB, Bluetooth, exportacio de fitxers i Chat & Sync](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Arquitectura de plugins per a fluxos de treball empresarials i usuaris avançats

Bitcoin Safe 2.0 tambe posa les bases per a futurs plugins addicionals pensats per a empreses de Bitcoin i usuaris avançats. Així que val la pena estar atents al que vindra :-)

<p class="small text-muted">Per als detalls d'implementacio, consulta la <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a>.</p>

- Distribucio de plugins mitjançant un repositori extern de *sources*
- Cada plugin esta *signat amb GPG* per [andreasgriffin]({{< gpg_key_link >}}) per garantir-ne la seguretat, la integritat i la distribucio
- El versionat individual dels plugins i les actualitzacions permeten un desenvolupament mes rapid i independent

![Targeta del signer amb accions especifiques per al dispositiu per a QR, USB, Bluetooth, exportacio de fitxers i Chat & Sync](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Mes suport per a dispositius i mes poliment {#hardware-support}

- Codis QR animats **30%** mes rapid per a una lectura mes rapida
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) ara te suport via USB
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) ara te suport per a **Bluetooth**, a mes d'USB i QR
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) i [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) s'afegeixen com a dispositius compatibles
- Consulta la [llista completa de dispositius compatibles]({{< ref "library/supported-hardware-signers" >}})
- S'han afegit comprovacions automatitzades de [reproduïbilitat]({{< ref "library/reproducibility-and-security" >}})
- Consulta aqui la [llista completa](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0) de millores


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## Els punts forts que ja existien continuen aqui

La versio 2.0 no es un reinici. Sota el nou flux d'onboarding i signatura, Bitcoin Safe continua mantenint les funcionalitats que el feien util cada dia: multisig col·laboratiu, copies de seguretat en PDF, historial de cartera cercable, visualitzacions del flux de diners, sincronitzacio d'etiquetes i mes.

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">Preparat per provar Bitcoin Safe 2.0?</h2>
  <p class="mb-3">Descarrega l'ultima versio i explora per tu mateix el nou onboarding, la sincronitzacio privada i les millores per a wallets de maquinari.</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Descarrega Bitcoin Safe</a>
</div>


<br><br>

## Gracies

Aquesta versio es basa en molta feina de col·laboradors, testers i [persones que donen suport al projecte]({{< ref "donate" >}}):

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r)) pel redisseny de l'assistent, el treball d'UI dels plugins i un suport d'UI/UX **fantastic i incansable**
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) pel client de Compact Block Filters que ara impulsa la sincronitzacio privada de carteres noves
- L'[equip de Bitcoin Dev Kit](https://github.com/bitcoindevkit/) per les biblioteques al cor de Bitcoin Safe
- L'[equip d'ndk](https://github.com/nostr-dev-kit/ndk) per les biblioteques que impulsen la funcionalitat nostr
- Tota la comunitat de Bitcoin Safe que ha provat release candidates, ha informat d'errors, ha traduit pagines, ha enviat sats i ha continuat empenyent el projecte endavant
- [Traductors]({{< ref "donate/#translators" >}}), incloent-hi <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (Vietnamita)" title="qdyg-vn 🇻🇳 (Vietnamita)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (Alemany)" title="bsn21m 🇩🇪 (Alemany)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (Espanyol)" title="cyphra 🇪🇸 (Espanyol)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (Xines)" title="DaGrindDontStop 🇨🇳 (Xines)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


Si vols ajudar a finançar la proxima versio, tambe pots fer una donacio aqui: {{< donation_btc >}}
