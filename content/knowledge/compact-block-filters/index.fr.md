---
title: "Filtres de blocs compacts"
description: "Comprenez ce que sont les filtres de blocs compacts et comment ils améliorent la confidentialité par rapport aux serveurs Electrum."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "filtres de blocs compacts"
  - "CBF"
  - "confidentialité"
  - "portefeuille Bitcoin"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**Les filtres de blocs compacts (CBF)** permettent à [Bitcoin Safe]({{< ref "/" >}}) de parcourir la blockchain sans demander à un serveur Electrum quelles adresses vous appartiennent.

![Bitcoin Safe télécharge des filtres de blocs compacts depuis plusieurs pairs Bitcoin Core aléatoires.](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

Au lieu d'interroger un serveur central, Bitcoin Safe télécharge un petit filtre pour chaque bloc depuis des pairs Bitcoin Core aléatoires. Votre portefeuille vérifie ces filtres localement et ne télécharge les blocs complets qu'en cas de besoin.

### CBF contre Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">Critère</th>
        <th scope="col">Filtres de blocs compacts</th>
        <th scope="col">Serveur Electrum</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Confidentialité</th>
        <td><span class="text-success fw-semibold">Bien</span> - Les données restent locales</td>
        <td><span class="text-danger fw-semibold">Mal</span> - Le serveur peut voir vos adresses et votre historique</td>
      </tr>
      <tr>
        <th scope="row">Source des données</th>
        <td><span class="text-success fw-semibold">Bien</span> - Des pairs Bitcoin Core aléatoires</td>
        <td><span class="text-warning fw-semibold">Neutre</span> - Un seul serveur choisi</td>
      </tr>
      <tr>
        <th scope="row">Synchronisation initiale</th>
        <td><span class="text-warning fw-semibold">Neutre</span> - Généralement plus lente</td>
        <td><span class="text-success fw-semibold">Bien</span> - Généralement plus rapide</td>
      </tr>
      <tr>
        <th scope="row">Synchronisation continue</th>
        <td><span class="text-success fw-semibold">Bien</span> - Très rapide après la première synchro</td>
        <td><span class="text-success fw-semibold">Bien</span> - Généralement rapide</td>
      </tr>
      <tr>
        <th scope="row">Idéal pour</th>
        <td><span class="text-success fw-semibold">Bien</span> - Les utilisateurs soucieux de la confidentialité</td>
        <td><span class="text-success fw-semibold">Bien</span> - La configuration et la récupération les plus rapides</td>
      </tr>
    </tbody>
  </table>
</div>

### Pourquoi utiliser CBF

- Meilleure confidentialité : votre portefeuille ne demande jamais à un serveur quelles adresses vous appartiennent.
- Pas d'indexeur de confiance : Bitcoin Safe communique directement avec le réseau Bitcoin.
- Synchronisation légère : les filtres sont petits, donc pas besoin de télécharger toute la blockchain.

### À quoi s'attendre

- Nouveau portefeuille ou restauration : généralement **5 à 30 minutes** pour la première synchronisation.
- Portefeuille déjà synchronisé : rattrapage **très rapide**, souvent en **moins de 30 secondes**.
- Passage d'Electrum à CBF : généralement aussi **moins de 30 secondes**.

Vous pouvez choisir le nombre de pairs auxquels Bitcoin Safe se connecte. Plus de pairs améliorent la redondance, mais augmentent généralement la bande passante et le temps de synchronisation. La valeur par défaut est **2** pairs.

### Transactions non confirmées

CBF couvre uniquement les **blocs confirmés**. Pour recevoir aussi les alertes des paiements non confirmés, laissez [Notifications de transaction instantanées]({{< ref "knowledge/instant-transactions-notifications/" >}}) activées, ce qui est le comportement par défaut.

### Note technique

Les filtres de blocs compacts sont définis dans [BIP158](https://bips.dev/158/). Bitcoin Safe utilise le module open source [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto).

Vous pouvez aussi utiliser votre propre nœud Bitcoin Core comme pair initial dans les réglages de _Surveillance du réseau Bitcoin_.

![Paramètre de nœud initial](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
