---
title: "Filtres de blocs compactes"
description: "Entén què són els filtres de blocs compactes i com milloren la privadesa respecte als servidors Electrum."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "filtres de blocs compactes"
  - "CBF"
  - "privadesa"
  - "cartera Bitcoin"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**Els filtres de blocs compactes (CBF)** permeten que [Bitcoin Safe]({{< ref "/" >}}) escanegi la blockchain sense preguntar a un servidor Electrum quines adreces són teves.

![Bitcoin Safe descarrega filtres de blocs compactes de diversos peers aleatoris de Bitcoin Core.](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

En lloc de consultar un servidor central, Bitcoin Safe descarrega un filtre petit per a cada bloc des de peers aleatoris de Bitcoin Core. La teva cartera els comprova localment i només descarrega els blocs complets quan cal.

### CBF vs Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">Aspecte</th>
        <th scope="col">Filtres de blocs compactes</th>
        <th scope="col">Servidor Electrum</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Privadesa</th>
        <td><span class="text-success fw-semibold">Bo</span> - Les dades de la cartera es mantenen locals</td>
        <td><span class="text-danger fw-semibold">Dolent</span> - El servidor pot veure les teves adreces i historial</td>
      </tr>
      <tr>
        <th scope="row">Font de dades</th>
        <td><span class="text-success fw-semibold">Bo</span> - Peers aleatoris de Bitcoin Core</td>
        <td><span class="text-warning fw-semibold">Neutral</span> - Un únic servidor escollit</td>
      </tr>
      <tr>
        <th scope="row">Sincronització inicial</th>
        <td><span class="text-warning fw-semibold">Neutral</span> - Normalment més lenta</td>
        <td><span class="text-success fw-semibold">Bo</span> - Normalment més ràpida</td>
      </tr>
      <tr>
        <th scope="row">Sincronització contínua</th>
        <td><span class="text-success fw-semibold">Bo</span> - Molt ràpida després de la primera sincronització</td>
        <td><span class="text-success fw-semibold">Bo</span> - Normalment ràpida</td>
      </tr>
      <tr>
        <th scope="row">Ideal per a</th>
        <td><span class="text-success fw-semibold">Bo</span> - Usuaris que prioritzen la privadesa</td>
        <td><span class="text-success fw-semibold">Bo</span> - La configuració i recuperació més ràpides</td>
      </tr>
    </tbody>
  </table>
</div>

### Per què usar CBF

- Més privadesa: la teva cartera no pregunta mai a cap servidor quines adreces són teves.
- Sense indexador de confiança: Bitcoin Safe parla directament amb la xarxa Bitcoin.
- Sincronització lleugera: els filtres són petits, així que no necessites tota la blockchain.

### Què esperar

- Cartera nova o recuperació: normalment **5 a 30 minuts** per a la primera sincronització.
- Cartera ja sincronitzada: normalment es posa al dia **molt ràpid**, sovint en **menys de 30 segons**.
- Canvi d'Electrum a CBF: normalment també **menys de 30 segons**.

Pots triar amb quants peers es connecta Bitcoin Safe. Més peers milloren la redundància, però normalment també augmenten l'ús de banda i el temps de sincronització. El valor per defecte és **2** peers.

### Transaccions no confirmades

CBF només cobreix **blocs confirmats**. Per rebre també alertes de pagaments no confirmats, deixa [Notificacions instantànies de transaccions]({{< ref "knowledge/instant-transactions-notifications/" >}}) activades, que és el comportament per defecte.

### Nota tècnica

Els filtres de blocs compactes es defineixen a [BIP158](https://bips.dev/158/). Bitcoin Safe usa el mòdul de codi obert [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto).

També pots usar el teu propi node de Bitcoin Core com a peer inicial a la configuració de _Bitcoin network monitoring_.

![Configuració del node inicial](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
