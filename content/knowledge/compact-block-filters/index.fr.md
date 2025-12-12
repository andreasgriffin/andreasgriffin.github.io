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


Bitcoin Safe 1.6.0 introduit les **Filtres de Blocs Compacts (CBF)** comme méthode optionnelle de synchronisation de votre portefeuille. Au lieu de demander à un serveur Electrum centralisé l'historique de votre portefeuille, [Bitcoin Safe]({{< ref "/" >}}) peut désormais télécharger un petit fichier de résumé pour chaque bloc directement depuis des pairs Bitcoin Core aléatoires. Ces résumés agissent comme une courte checklist qui permet à votre portefeuille de décider lui-même si un bloc pourrait contenir l'une de vos transactions.

Parce que [Bitcoin Safe]({{< ref "/" >}}) prend la décision localement, aucun serveur tiers n'apprend jamais quelles adresses ou transactions vous intéressent. Vous obtenez les mêmes données de confirmation qu'un nœud complet conserverait, mais dans un format plus léger adapté aux appareils du quotidien.

**Pourquoi c'est mieux :**

- 📦 **Téléchargements légers :** Chaque filtre ne fait que quelques kilooctets, vous pouvez donc synchroniser via une connexion domestique classique sans stocker toute la blockchain.
- 🔐 **Directement depuis le réseau :** [Bitcoin Safe]({{< ref "/" >}}) se connecte à plusieurs nœuds Bitcoin Core aléatoires, comme le font les autres nœuds, ce qui réduit la probabilité qu'un observateur unique puisse vous profiler.
- 🕵️ **Correspondance locale :** Votre portefeuille vérifie les filtres localement. Si un filtre semble pertinent, il télécharge alors uniquement le bloc concerné, en gardant vos adresses privées.

Les serveurs Electrum, par contraste, parcourent la blockchain pour vous. Chaque requête partage les adresses de votre portefeuille avec l'opérateur du serveur, qui pourrait enregistrer ces informations. Avec les filtres de blocs compacts, [Bitcoin Safe]({{< ref "/" >}}) télécharge les mêmes données neutres que chaque nœud partage. Personne ne peut dire quelles adresses vous appartiennent parce que votre portefeuille ne les révèle jamais en premier lieu.

Ci‑dessous une vue simple montrant comment [Bitcoin Safe]({{< ref "/" >}}) se connecte lorsque les CBF sont activés. Remarquez comment cela reflète la façon dont les nœuds Bitcoin Core communiquent déjà entre eux :


![Bitcoin Safe downloads compact block filters from several random Bitcoin Core peers.](logo.jpg)
{ .img-fluid .mb-5   style="max-width: 450px;" }


Vous pouvez choisir le nombre de pairs auxquels [Bitcoin Safe]({{< ref "/" >}}) doit se connecter. Plus de pairs nécessitent plus de bande passante et impliquent un temps de synchronisation plus long. La valeur par défaut est 2.

 
### À quoi s'attendre lors de la synchronisation

CBF change la durée d'attente selon ce que vous faites :

1. ✨ **Configuration ou récupération d'un portefeuille :** Que vous créiez un nouveau portefeuille ou récupériez un portefeuille existant, la synchronisation initiale télécharge les filtres pour l'ensemble de l'historique. Attendez-vous à ce que ce processus ponctuel prenne **entre 5 et 30 minutes**, selon la vitesse de votre connexion internet.
2. 🚀 **Ouverture d'un portefeuille déjà synchronisé :** [Bitcoin Safe]({{< ref "/" >}}) n'a besoin de récupérer que les filtres les plus récents depuis votre dernière session. Cette mise à jour se termine généralement en **moins de 30 secondes**.
3. 🔄 **Passage des serveurs Electrum aux CBF :** Si le portefeuille a été précédemment synchronisé via des serveurs Electrum, [Bitcoin Safe]({{< ref "/" >}}) n'aura qu'à récupérer les filtres les plus récents, ce qui prend habituellement **moins de 30 secondes**.

### Restez informé des paiements non confirmés

Les filtres de blocs compacts couvrent uniquement les **blocs confirmés**. Pour être informé des transactions entrantes avant qu'elles ne soient confirmées, assurez‑vous également d'activer les [Notifications de transaction instantanées]({{< ref "knowledge/instant-transactions-notifications/" >}}). Cette fonctionnalité écoute les messages pair-à-pair en direct d'un nœud Bitcoin aléatoire afin que vous puissiez réagir à l'activité du mempool sans compromettre votre confidentialité.


<br>
<br>



### Détails techniques


- *Pour les développeurs qui veulent approfondir :* les filtres de blocs compacts suivent la spécification [BIP158](https://bips.dev/158/) et sont expliqués dans l'[overview de Elle Mouton sur les ensembles codés Golomb](https://ellemouton.com/posts/bip158/). L'implémentation de [Bitcoin Safe]({{< ref "/" >}}) s'appuie sur le module open-source [Kyoto compact block filter pour BDK](https://github.com/2140-dev/kyoto).
- Vous pouvez ajouter votre propre nœud Bitcoin Core aux pairs pour la synchronisation des filtres de blocs compacts, en choisissant le _Nœud initial_ du _Surveillance du réseau Bitcoin_.


![](inital-node.png)
{ .img-fluid .mb-5   style="max-width: 414px;" }