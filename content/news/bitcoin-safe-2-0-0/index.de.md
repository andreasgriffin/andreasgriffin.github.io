---
title: "Bitcoin Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "Versionshinweise zu Bitcoin Safe 2.0.0 mit einem neu aufgebauten Einrichtungsassistenten, privater Compact-Block-Filter-Synchronisierung und erweiterter Hardware-Wallet-Unterstuetzung."
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">Release-Ankuendigung</p>
    <h2 class="display-6 mb-3">Bitcoin Safe 2.0 - gefuehrte Wallet-Einrichtung, private Chain-Synchronisierung und geraetefokussiertes Signieren</h2>
    <p class="lead mb-4">Dieses Release bringt einen neu aufgebauten Einrichtungsassistenten, private Chain-Synchronisierung mit Compact Block Filters und einen Signierablauf, der um jedes Hardware-Geraet herum organisiert ist. Wenn du neugierig auf Cold Storage warst, aber unsicher, ist das die richtige Version zum Ausprobieren.</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Bitcoin Safe 2.0 herunterladen</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">Neuerungen ansehen</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Schritt-fuer-Schritt-Wallet-Einrichtung</h2>
          <p class="mb-0">Der neue Assistent erklaert jeden Schritt, verringert Unklarheiten und hilft neuen Nutzerinnen und Nutzern, den richtigen Weg zu waehlen, ohne die Staerke von Multisig zu verlieren.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Private Wallet-Synchronisierung</h2>
          <p class="mb-0">Neue Wallets synchronisieren jetzt standardmaessig mit Compact Block Filters, sodass du die Blockchain privat scannen kannst, ohne dich auf einen Electrum-Indexer eines Drittanbieters zu stuetzen.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Geraetefokussiertes Signieren</h2>
          <p class="mb-0">Signierablaeufe bleiben jetzt auf das Geraet vor dir zentriert, mit klareren naechsten Schritten fuer QR, USB, Bluetooth, Dateien und Multisig-Koordination.</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## Ein gefuehrter Weg zur Selbstverwahrung {#setup-flow}

Das erste Nutzungserlebnis wurde von Grund auf neu aufgebaut. Bitcoin Safe richtet sich weiterhin an ernsthafte Selbstverwahrung, einschliesslich hardwaregestuetzter Multisig-Setups, und 2.0 bietet neuen Nutzerinnen und Nutzern nun einen gefuehrten Weg durch diese Einrichtung. Der neue Assistent erklaert, was gerade passiert, wo du dich im Ablauf befindest und was jeder Signer von dir braucht, bevor du weitergehst.

<p class="small text-muted">Details zur Implementierung findest du in <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a>.</p>

Highlights des Redesigns:

- Ein neuer Begruessungsbildschirm hilft Erstnutzerinnen und Erstnutzern, den richtigen Einstieg zu waehlen
- Ein Schritt-fuer-Schritt-Fortschrittsablauf waehrend der Wallet-Erstellung
- Geraetespezifische Signierbildschirme mit fokussierten Anweisungen und kontextbezogener Hilfe
- Wiederherstellungs-PDFs mit Geraetenamen und Symbolen, damit Backups eindeutig bleiben

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## Private und robuste Chain-Synchronisierung mit Compact Block Filters {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) treiben jetzt die Wallet-Synchronisierung fuer neue Wallets in Bitcoin Safe 2.0 an. Anstatt einen Electrum-Server zu fragen, welche Adressen zu dir gehoeren, kann Bitcoin Safe die Blockchain nun privat scannen, indem kompakte Filter von zufaelligen Bitcoin-Core-Peers geladen und lokal geprueft werden.

<p class="small text-muted">Details zur Implementierung findest du in <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a>.</p>


- Die Wallet-Synchronisierung bleibt vom ersten Start an privat
- Keine Abhaengigkeit von Electrum-Servern Dritter
- Electrum bleibt fuer Nutzerinnen und Nutzer verfuegbar, die es bevorzugen
- [Sofortige Synchronisierung nach dem ersten Wallet-Scan]({{< ref "library/compact-block-filters" >}})
- [Sofortige Benachrichtigungen ueber weitergeleitete Transaktionen]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## Ein geraetefokussierter Signierablauf fuer jedes Geraet {#device-focused-signing}

Das Redesign formt auch den Signierablauf nach der Wallet-Erstellung neu. Statt eines generischen Bildschirms fuer alle Signer stellt Bitcoin Safe die Aktionen jetzt rund um das konkrete Geraet in den Mittelpunkt, das du gerade verwendest.

<p class="small text-muted">Details zur Implementierung findest du in <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a>.</p>

- Aktionen fuer QR, USB, Bluetooth, Datei-Export/-Import sowie Sync & Chat werden direkt auf der aktiven Signer-Karte angezeigt
- Verbleibende Signer, bereits signierte Geraete und der naechste noetige Schritt bleiben auf einen Blick sichtbar
- Multisig-Ablaeufe mit gemischten Geraeten bleiben lesbar, weil die Identitaet jedes Signers waehrend des gesamten PSBT sichtbar bleibt
- Komplexe Transaktionen mit einer Mischung aus Single-Sig- und Multisig-Eingaengen werden korrekt verarbeitet, sodass jeder Signierschritt klar bleibt

![Signer-Karte mit geraetespezifischen Aktionen fuer QR, USB, Bluetooth, Datei-Export und Chat & Sync](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Plugin-Architektur fuer Geschaeftsablaeufe und Power-User

Bitcoin Safe 2.0 legt ausserdem die Grundlage fuer zukuenftige zusaetzliche Plugins, die sich an Bitcoin-Unternehmen und Power-Bitcoiner richten. Es lohnt sich also, auf das zu achten, was noch kommt :-)

<p class="small text-muted">Details zur Implementierung findest du in <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a>.</p>

- Plugin-Verteilung ueber ein externes *sources*-Repository
- Jedes Plugin ist mit *GPG* von [andreasgriffin]({{< gpg_key_link >}}) signiert, um Sicherheit, Integritaet und Auslieferung sicherzustellen
- Eigene Plugin-Versionierung und Updates ermoeglichen schnellere und unabhaengige Plugin-Entwicklung

![Signer-Karte mit geraetespezifischen Aktionen fuer QR, USB, Bluetooth, Datei-Export und Chat & Sync](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Breitere Geraeteunterstuetzung und Feinschliff {#hardware-support}

- **30%** schnellere animierte QR-Codes fuer schnelleres Scannen
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) wird jetzt ueber USB unterstuetzt
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) unterstuetzt jetzt zusaetzlich zu USB und QR auch **Bluetooth**
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) und [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) wurden als unterstuetzte Geraete hinzugefuegt
- Sieh dir die [vollstaendige Liste der unterstuetzten Geraete]({{< ref "library/supported-hardware-signers" >}}) an
- Automatisierte Pruefungen fuer die [Reproduzierbarkeit]({{< ref "library/reproducibility-and-security" >}}) wurden hinzugefuegt
- Hier findest du die [vollstaendige Liste](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0) der Verbesserungen


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## Bestehende Staerken sind weiterhin da

Die Version 2.0 ist kein Neustart. Unter dem neuen Onboarding- und Signierablauf bietet Bitcoin Safe weiterhin die Funktionen, die es im Alltag nuetzlich machen: kollaboratives Multisig, PDF-Backups, durchsuchbare Wallet-Historie, Visualisierungen des Geldflusses, Label-Synchronisierung und mehr.

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">Bereit, Bitcoin Safe 2.0 auszuprobieren?</h2>
  <p class="mb-3">Lade die neueste Version herunter und entdecke selbst das neue Onboarding, die private Synchronisierung und die Verbesserungen fuer Hardware-Wallets.</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Bitcoin Safe herunterladen</a>
</div>


<br><br>

## Danke

Dieses Release basiert auf viel Arbeit von Mitwirkenden, Testerinnen und Testern sowie [Unterstuetzern im gesamten Projekt]({{< ref "donate" >}}):

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r)) fuer das Redesign des Assistenten, die Plugin-Oberflaeche und **grossartige und unermuedliche** UI/UX-Unterstuetzung
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) fuer den Compact-Block-Filter-Client, der jetzt die private Wallet-Synchronisierung fuer neue Wallets ermoeglicht
- Das [Bitcoin Dev Kit Team](https://github.com/bitcoindevkit/) fuer die Bibliotheken im Kern von Bitcoin Safe
- Das [ndk Team](https://github.com/nostr-dev-kit/ndk) fuer die Bibliotheken, die die Nostr-Funktionalitaet antreiben
- Alle in der Bitcoin-Safe-Community, die Release-Kandidaten getestet, Fehler gemeldet, Seiten uebersetzt, Sats geschickt und das Projekt weiter vorangetrieben haben
- [Uebersetzer]({{< ref "donate/#translators" >}}) darunter <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (Vietnamesisch)" title="qdyg-vn 🇻🇳 (Vietnamesisch)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (Deutsch)" title="bsn21m 🇩🇪 (Deutsch)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (Spanisch)" title="cyphra 🇪🇸 (Spanisch)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (Chinesisch)" title="DaGrindDontStop 🇨🇳 (Chinesisch)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


Wenn du helfen moechtest, die naechste Version zu finanzieren, kannst du hier spenden: {{< donation_btc >}}
