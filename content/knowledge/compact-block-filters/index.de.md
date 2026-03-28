---
title: "Kompakte Block-Filter"
description: "Erklärt, was kompakte Block-Filter sind und wie sie die Privatsphäre im Vergleich zu Electrum-Servern verbessern."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "kompakte Block-Filter"
  - "CBF"
  - "Privatsphäre"
  - "Bitcoin-Wallet"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**Kompakte Block-Filter (CBF)** ermöglichen es [Bitcoin Safe]({{< ref "/" >}}), die Blockchain zu scannen, ohne einen Electrum-Server nach Ihren Adressen zu fragen.

![Bitcoin Safe lädt kompakte Block-Filter von mehreren zufälligen Bitcoin-Core-Peers herunter.](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

Statt einen zentralen Server abzufragen, lädt Bitcoin Safe für jeden Block einen kleinen Filter von zufälligen Bitcoin-Core-Peers herunter. Ihre Wallet prüft diese Filter lokal und lädt vollständige Blöcke nur bei Bedarf.

### CBF gegen Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">Merkmal</th>
        <th scope="col">Kompakte Block-Filter</th>
        <th scope="col">Electrum-Server</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Privatsphäre</th>
        <td><span class="text-success fw-semibold">Gut</span> - Wallet-Daten bleiben lokal</td>
        <td><span class="text-danger fw-semibold">Schlecht</span> - Der Server kann Ihre Adressen und Ihren Verlauf sehen</td>
      </tr>
      <tr>
        <th scope="row">Datenquelle</th>
        <td><span class="text-success fw-semibold">Gut</span> - Zufällige Bitcoin-Core-Peers</td>
        <td><span class="text-warning fw-semibold">Neutral</span> - Ein ausgewählter Server</td>
      </tr>
      <tr>
        <th scope="row">Erstsynchronisierung</th>
        <td><span class="text-warning fw-semibold">Neutral</span> - Meist langsamer</td>
        <td><span class="text-success fw-semibold">Gut</span> - Meist schneller</td>
      </tr>
      <tr>
        <th scope="row">Laufende Synchronisierung</th>
        <td><span class="text-success fw-semibold">Gut</span> - Sehr schnell nach der ersten Synchronisierung</td>
        <td><span class="text-success fw-semibold">Gut</span> - Meist schnell</td>
      </tr>
      <tr>
        <th scope="row">Am besten für</th>
        <td><span class="text-success fw-semibold">Gut</span> - Nutzer mit Fokus auf Privatsphäre</td>
        <td><span class="text-success fw-semibold">Gut</span> - Die schnellste Einrichtung und Wiederherstellung</td>
      </tr>
    </tbody>
  </table>
</div>

### Warum CBF verwenden

- Mehr Privatsphäre: Ihre Wallet fragt nie einen Server nach Ihren Adressen.
- Kein vertrauenswürdiger Indexer: Bitcoin Safe spricht direkt mit dem Bitcoin-Netzwerk.
- Leichte Synchronisierung: Die Filter sind klein, daher brauchen Sie nicht die gesamte Blockchain.

### Was Sie erwarten können

- Neue Wallet oder Wiederherstellung: die erste Synchronisierung dauert meist **5 bis 30 Minuten**.
- Bereits synchronisierte Wallet: holt sehr schnell auf, oft in **unter 30 Sekunden**.
- Wechsel von Electrum zu CBF: ebenfalls meist **unter 30 Sekunden**.

Sie können wählen, mit wie vielen Peers sich Bitcoin Safe verbindet. Mehr Peers verbessern die Redundanz, erhöhen aber meist Bandbreite und Synchronisationszeit. Die Standardeinstellung ist **2** Peers.

### Unbestätigte Transaktionen

CBF deckt nur **bestätigte Blöcke** ab. Damit Sie auch Hinweise auf eingehende unbestätigte Zahlungen erhalten, lassen Sie [Instant transaction notifications]({{< ref "knowledge/instant-transactions-notifications/" >}}) aktiviert. Das ist die Standardeinstellung.

### Technischer Hinweis

Kompakte Block-Filter sind in [BIP158](https://bips.dev/158/) definiert. Bitcoin Safe verwendet das Open-Source-[Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto).

Sie können in den Einstellungen für _Bitcoin network monitoring_ auch Ihren eigenen Bitcoin-Core-Knoten als anfänglichen Peer verwenden.

![Einstellung für den Anfangsknoten](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
