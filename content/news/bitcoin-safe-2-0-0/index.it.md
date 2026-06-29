---
title: "Bitcoin Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "Note di rilascio di Bitcoin Safe 2.0.0, con una procedura guidata di configurazione ricostruita, sincronizzazione privata con Compact Block Filters e supporto ampliato per i wallet hardware."
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">Annuncio della release</p>
    <h2 class="display-6 mb-3">Bitcoin Safe 2.0 - configurazione guidata del wallet, sincronizzazione privata della chain e firma focalizzata sul dispositivo</h2>
    <p class="lead mb-4">Questa release porta una procedura guidata di configurazione ricostruita, sincronizzazione privata della chain con Compact Block Filters e un flusso di firma organizzato intorno a ogni dispositivo hardware. Se eri curioso del cold storage ma non eri sicuro, questa e la release da provare.</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Scarica Bitcoin Safe 2.0</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">Scopri cosa c'e di nuovo</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Configurazione del wallet passo dopo passo</h2>
          <p class="mb-0">La nuova procedura guidata spiega ogni passaggio, riduce l'ambiguita e aiuta i nuovi utenti a scegliere il percorso giusto senza perdere la potenza del multisig.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Sincronizzazione privata del wallet</h2>
          <p class="mb-0">I nuovi wallet ora si sincronizzano con Compact Block Filters fin da subito, cosi puoi scansionare la chain in privato senza affidarti a un indicizzatore Electrum di terze parti.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Firma focalizzata sul dispositivo</h2>
          <p class="mb-0">I flussi di firma ora restano centrati sul dispositivo che hai davanti, con passaggi successivi piu chiari per QR, USB, Bluetooth, file e coordinamento multisig.</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## Un percorso guidato verso l'auto-custodia {#setup-flow}

L'esperienza del primo avvio e stata ricostruita da zero. Bitcoin Safe continua a puntare su un'auto-custodia seria, compresi i setup multisig supportati da hardware, e la versione 2.0 ora offre ai nuovi utenti un percorso guidato attraverso questa configurazione. La nuova procedura guidata spiega cosa sta succedendo, dove ti trovi nel flusso e di cosa ha bisogno ogni signer prima che tu possa andare avanti.

<p class="small text-muted">Per i dettagli di implementazione, vedi la <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a>.</p>

Punti salienti del redesign:

- Una nuova schermata di benvenuto che aiuta chi usa l'app per la prima volta a scegliere il punto di partenza giusto
- Un flusso di avanzamento passo dopo passo durante la creazione del wallet
- Schermate di firma specifiche per dispositivo con istruzioni mirate e aiuto contestuale
- PDF di recupero con nomi e icone dei dispositivi cosi i backup restano chiari

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## Sincronizzazione privata e robusta della chain con Compact Block Filters {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) ora alimentano la sincronizzazione dei nuovi wallet in Bitcoin Safe 2.0. Invece di chiedere a un server Electrum quali indirizzi ti appartengono, Bitcoin Safe puo ora scansionare la chain in privato scaricando filtri compatti da peer Bitcoin Core casuali e verificandoli in locale.

<p class="small text-muted">Per i dettagli di implementazione, vedi la <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a>.</p>


- La sincronizzazione del wallet resta privata fin dal primo avvio
- Nessuna dipendenza da server Electrum di terze parti
- Electrum resta comunque disponibile per chi lo preferisce
- [Sincronizzazione istantanea dopo la scansione iniziale del wallet]({{< ref "library/compact-block-filters" >}})
- [Notifiche istantanee delle transazioni inoltrate]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## Un flusso di firma focalizzato sul dispositivo per ogni dispositivo {#device-focused-signing}

Il redesign rimodella anche il flusso di firma dopo la creazione del wallet. Invece di una schermata generica per ogni signer, Bitcoin Safe ora centra le azioni sul dispositivo specifico che stai usando.

<p class="small text-muted">Per i dettagli di implementazione, vedi la <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a>.</p>

- Le azioni per QR, USB, Bluetooth, esportazione/importazione di file e Sync & Chat sono mostrate direttamente sulla card del signer attivo
- I signer rimanenti, i dispositivi che hanno gia firmato e il prossimo passaggio richiesto restano visibili a colpo d'occhio
- I flussi multisig con dispositivi misti restano leggibili perche l'identita di ogni signer rimane visibile per tutto il PSBT
- Le transazioni complesse con un mix di input single-sig e multisig vengono gestite correttamente, cosi ogni passaggio di firma resta chiaro

![Card del signer con azioni specifiche per il dispositivo per QR, USB, Bluetooth, esportazione file e Chat & Sync](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Architettura plugin per flussi di lavoro aziendali e power user

Bitcoin Safe 2.0 getta anche le basi per futuri plugin aggiuntivi pensati per aziende Bitcoin e power user. Quindi tieni d'occhio quello che arrivera :-)

<p class="small text-muted">Per i dettagli di implementazione, vedi la <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a>.</p>

- Distribuzione dei plugin tramite un repository esterno di *sources*
- Ogni plugin e *firmato con GPG* da [andreasgriffin]({{< gpg_key_link >}}) per garantirne sicurezza, integrita e distribuzione
- Versionamento individuale dei plugin e aggiornamenti permettono uno sviluppo piu rapido e indipendente

![Card del signer con azioni specifiche per il dispositivo per QR, USB, Bluetooth, esportazione file e Chat & Sync](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Supporto piu ampio ai dispositivi e rifiniture {#hardware-support}

- Codici QR animati **30%** piu veloci per una scansione piu rapida
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) ora e supportato via USB
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) ora supporta anche il **Bluetooth**, oltre a USB e QR
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) e [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) aggiunti come dispositivi supportati
- Vedi l'[elenco completo dei dispositivi supportati]({{< ref "library/supported-hardware-signers" >}})
- Aggiunti controlli automatici per la [riproducibilita]({{< ref "library/reproducibility-and-security" >}})
- Vedi qui l'[elenco completo](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0) dei miglioramenti


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## I punti di forza gia esistenti sono ancora qui

La release 2.0 non e un reset. Sotto il nuovo onboarding e il nuovo flusso di firma, Bitcoin Safe conserva ancora le funzionalita che lo rendevano utile ogni giorno: multisig collaborativo, backup PDF, cronologia del wallet ricercabile, visualizzazioni del flusso di denaro, sincronizzazione delle etichette e altro ancora.

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">Pronto a provare Bitcoin Safe 2.0?</h2>
  <p class="mb-3">Scarica l'ultima release ed esplora di persona il nuovo onboarding, la sincronizzazione privata e i miglioramenti per gli hardware wallet.</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Scarica Bitcoin Safe</a>
</div>


<br><br>

## Grazie

Questa release si basa sul grande lavoro di contributori, tester e [sostenitori di tutto il progetto]({{< ref "donate" >}}):

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r)) per il redesign della procedura guidata, il lavoro UI sui plugin e un supporto UI/UX **fantastico e instancabile**
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) per il client Compact Block Filter che ora alimenta la sincronizzazione privata dei nuovi wallet
- Il [team di Bitcoin Dev Kit](https://github.com/bitcoindevkit/) per le librerie al centro di Bitcoin Safe
- Il [team ndk](https://github.com/nostr-dev-kit/ndk) per le librerie che alimentano le funzionalita nostr
- Tutta la comunita di Bitcoin Safe che ha testato release candidate, segnalato bug, tradotto pagine, inviato sats e continuato a spingere il progetto in avanti
- [Traduttori]({{< ref "donate/#translators" >}}), tra cui <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (Vietnamita)" title="qdyg-vn 🇻🇳 (Vietnamita)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (Tedesco)" title="bsn21m 🇩🇪 (Tedesco)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (Spagnolo)" title="cyphra 🇪🇸 (Spagnolo)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (Cinese)" title="DaGrindDontStop 🇨🇳 (Cinese)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


Se vuoi aiutare a finanziare la prossima release, puoi anche donare qui: {{< donation_btc >}}
