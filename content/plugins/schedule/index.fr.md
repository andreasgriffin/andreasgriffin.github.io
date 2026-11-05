---
title: "Paiements planifiés"
description: "Planifiez des paiements Bitcoin ponctuels ou récurrents, suivez leurs échéances et préparez les transactions à vérifier dans Bitcoin-Safe."
draft: false
tags: ["Plugins"]
images: ["schedule.png"]
weight: 40
faq:
  title: "Questions sur les paiements planifiés"
  items:
    - question: "Puis-je planifier un paiement unique, ou seulement des paiements récurrents ?"
      answer: "Les deux. Vous pouvez créer un paiement unique, un nombre fixe de répétitions ou un calendrier continu."
    - question: "À quelle fréquence un calendrier peut-il se répéter ?"
      answer: "Les intervalles de répétition sont disponibles :\n- En minutes, heures ou jours\n- En semaines, éventuellement sur des jours de la semaine choisis\n- En mois ou années, à des dates du calendrier ou selon des motifs de jours de la semaine"
    - question: "Puis-je définir le montant en monnaie fiduciaire ?"
      answer: "Oui. Vous pouvez définir le montant :\n- En bitcoin\n- Dans une devise fiduciaire prise en charge\n\nLes montants en fiduciaire peuvent utiliser :\n- Un taux de change en direct\n- Le taux CoinGecko, figé à 00:00 GMT\n\nUne substitution du taux de change peut aussi être définie pour le prochain paiement."
    - question: "Les adresses sont-elles réutilisées ?"
      answer: "Non. Chaque adresse de destinataire n'est utilisée qu'une seule fois. Lorsque les adresses d'un destinataire sont épuisées, vous pouvez en ajouter d'autres pour ce destinataire."
    - question: "Bitcoin-Safe envoie-t-il les paiements automatiquement ?"
      answer: "Non. Lorsqu'un paiement arrive à échéance, Schedule prépare la transaction dans Bitcoin-Safe pour votre vérification. Vous restez responsable de la signer et de la diffuser."
    - question: "Puis-je payer plusieurs destinataires à la fois ?"
      answer: "Oui. Sélectionnez plusieurs paiements planifiés et cliquez sur **Payer la sélection**. Bitcoin-Safe les regroupe dans une seule transaction par lot."
    - question: "Que faire si un paiement a été effectué en espèces ou autrement ?"
      answer: "Ajoutez un paiement **hors bande**. Il enregistre le paiement dans votre calendrier sans transaction Bitcoin, afin que la progression reste exacte."
---

### {{< page-title >}}

<p class="lead">Planifiez vos paiements Bitcoin et laissez Schedule suivre ce qui arrive à échéance.</p>

<ul class="plugin-features">
<li>Payer des employés ou organiser d'autres obligations régulières</li>
<li>Mettre en place des virements récurrents</li>
<li>Planifier un paiement ponctuel que vous ne devez pas oublier</li>
</ul>

Lorsqu'un paiement arrive à échéance, Schedule prépare la transaction dans Bitcoin-Safe pour votre vérification. Vous restez responsable de la signer et de la diffuser.

{{< video "schedule.mp4" controls >}}

### Plans de paiement flexibles

- Choisissez un paiement unique, un nombre fixe de répétitions ou un calendrier continu.
- Définissez une date de début et un intervalle de répétition : minutes, heures, jours, semaines, mois ou années. Les calendriers hebdomadaires peuvent utiliser des jours de la semaine choisis ; les calendriers mensuels et annuels prennent en charge les dates du calendrier et les motifs de jours de la semaine.
- Définissez un destinataire, une catégorie et un montant en bitcoin ou dans une devise fiduciaire prise en charge.
- Pour les montants en fiduciaire, utilisez un taux en direct ou le taux CoinGecko figé à 00:00 GMT. Une substitution du taux peut être définie pour le prochain paiement.
- Les calendriers à nombre fixe affichent des aperçus du montant par paiement et du total.

### Préparer les paiements dans votre portefeuille

- Consultez la prochaine échéance et la progression des paiements ; les paiements arrivés à échéance sont mis en évidence et peuvent déclencher un avis Bitcoin-Safe.
- Préparez un paiement arrivé à échéance ou un lot dans le composeur de transactions, avec les sorties des destinataires, les libellés et les catégories déjà renseignés.
- Vérifiez et personnalisez la transaction avant de la signer et de la diffuser vous-même.
- Enregistrez des destinataires réutilisables avec un nom et plusieurs adresses. Schedule peut sélectionner une adresse inutilisée pour un versement.

### Suivre et gérer les calendriers

- Recherchez des calendriers par statut d'échéance, type de calendrier ou catégorie. Les listes affichent les dates, les paiements effectués, la fréquence, le destinataire, le montant, la catégorie et le total.
- Consultez les versements effectués et les occurrences à venir. Les transactions du portefeuille correspondantes peuvent mettre à jour la progression ; vous pouvez aussi ajouter un versement manuellement ou relancer l'analyse des transactions.
- Modifiez un calendrier avant son premier versement enregistré, dupliquez-le ou supprimez-le, et importez/exportez les calendriers sous forme de sauvegarde JSON.

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">Télécharger Bitcoin-Safe</h2>
<p class="text-muted mb-3">Les plugins sont inclus dans Bitcoin-Safe. Téléchargez l'application pour les essayer.</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">Télécharger Bitcoin-Safe</a>
<small class="text-muted">Logiciel libre et open source · Windows, macOS, Linux</small>
</div>
</section>

### Questions fréquentes

<details>
<summary>Puis-je planifier un paiement unique, ou seulement des paiements récurrents ?</summary>

Les deux. Vous pouvez créer un paiement unique, un nombre fixe de répétitions ou un calendrier continu.

</details>

<details>
<summary>À quelle fréquence un calendrier peut-il se répéter ?</summary>

Les intervalles de répétition sont disponibles :

- En minutes, heures ou jours
- En semaines, éventuellement sur des jours de la semaine choisis
- En mois ou années, à des dates du calendrier ou selon des motifs de jours de la semaine

</details>

<details>
<summary>Puis-je définir le montant en monnaie fiduciaire ?</summary>

Oui. Vous pouvez définir le montant :

- En bitcoin
- Dans une devise fiduciaire prise en charge

Les montants en fiduciaire peuvent utiliser :

- Un taux de change en direct
- Le taux CoinGecko, figé à 00:00 GMT

Une substitution du taux de change peut aussi être définie pour le prochain paiement.

</details>

<details>
<summary>Les adresses sont-elles réutilisées ?</summary>

Non. Chaque adresse de destinataire n'est utilisée qu'une seule fois. Lorsque les adresses d'un destinataire sont épuisées, vous pouvez en ajouter d'autres pour ce destinataire.

</details>

<details>
<summary>Bitcoin-Safe envoie-t-il les paiements automatiquement ?</summary>

Non. Lorsqu'un paiement arrive à échéance, Schedule prépare la transaction dans Bitcoin-Safe pour votre vérification. Vous restez responsable de la signer et de la diffuser.

</details>

<details>
<summary>Puis-je payer plusieurs destinataires à la fois ?</summary>

Oui. Sélectionnez plusieurs paiements planifiés et cliquez sur **Payer la sélection**. Bitcoin-Safe les regroupe dans une seule transaction par lot.

</details>

<details>
<summary>Que faire si un paiement a été effectué en espèces ou autrement ?</summary>

Ajoutez un paiement **hors bande**. Il enregistre le paiement dans votre calendrier sans transaction Bitcoin, afin que la progression reste exacte.

</details>
</content>
