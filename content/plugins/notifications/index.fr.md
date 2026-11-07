---
title: "Notifications du portefeuille"
description: "Transmettez les notifications du portefeuille et de l'application Bitcoin-Safe vers les destinations que vous configurez, avec des contrôles de livraison, de confidentialité et de délai."
draft: false
tags: ["Plugins"]
images: ["notifications.png"]
weight: 35
faq:
  title: "Questions sur les notifications du portefeuille"
  items:
    - question: "Où Bitcoin-Safe peut-il envoyer des notifications ?"
      answer: "Bitcoin-Safe peut envoyer des notifications :\n- Vers des webhooks : JSON générique, ou formats compatibles Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy et Gotify\n- Par messages directs Nostr\n- Vers des bots Telegram\n- Par e-mail via SMTP\n- Vers des calendriers CalDAV"
    - question: "Puis-je exclure les détails sensibles des alertes ?"
      answer: "Oui. Activez l'option masquer les détails sensibles : le message ne contient alors qu'un avis général indiquant qu'un événement de notification Bitcoin-Safe s'est produit."
    - question: "Puis-je contrôler quels événements vont à quel endroit ?"
      answer: "Chaque destination a ses propres règles. Vous choisissez les types d'événements qu'elle reçoit :\n- Transactions du portefeuille\n- Paiements planifiés\n- Sync et chat\n- Avertissements\n\nVous pouvez aussi définir un délai d'envoi aléatoire optionnel."
    - question: "L'application doit-elle rester déverrouillée ?"
      answer: "Non. Verrouiller et réduire dans la zone de notification garde Bitcoin-Safe actif en arrière-plan pendant que votre portefeuille reste verrouillé."
---

### {{< page-title >}}

<p class="lead">Soyez informé de l'activité de votre portefeuille par les canaux qui vous conviennent.</p>

<ul class="plugin-features">
<li>Transactions entrantes et sortantes, messages Sync&Chat, paiements planifiés arrivés à échéance, ...</li>
<li>Transmission des alertes vers des webhooks, Nostr, Telegram, e-mail, calendriers et plus encore</li>
<li>Choisissez les événements reçus par chaque destination et masquez les détails sensibles</li>
<li>Gardez Bitcoin-Safe actif en arrière-plan ; utilisez <strong>Verrouiller et réduire dans la zone de notification</strong> pour le laisser tourner pendant que le portefeuille est verrouillé</li>
</ul>

### Configurer un webhook

{{< video "webhook.mp4" controls >}}

### Messages directs Nostr

{{< video "nostr.mp4" controls >}}

### Notifications par calendrier

{{< video "calendar.mp4" controls >}}

### Connecter vos destinations

- Ajoutez une ou plusieurs destinations. Chacune peut avoir ses propres destinataires et règles de livraison.
- **E-mail :** connexion directe à un serveur SMTP avec l'hôte, le port, les identifiants, l'expéditeur et les paramètres de sécurité. Ce n'est pas une intégration gérée avec Gmail ou Outlook.
- **Telegram :** envoi vers un chat via un bot. Démarrez une conversation avec le bot pour le vérifier et détecter les identifiants de chat récents.
- **Nostr DM :** envoi de messages chiffrés NIP-17 aux destinataires `npub` via les relais configurés, avec une clé d'expéditeur.
- **CalDAV :** ajout d'événements dans un calendrier existant, comme un calendrier Nextcloud configuré.
- **Webhooks :** envoi au format JSON générique ou aux formats des points de terminaison compatibles Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy et Gotify. Les types de points de terminaison courants peuvent être détectés automatiquement.
- Enregistrez les paramètres de la destination et utilisez l'action de test lorsqu'elle est disponible.

### Choisir ce qui est envoyé

- Choisissez les types d'événements reçus par chaque destination :
  - Transactions du portefeuille
  - Paiements planifiés
  - Sync et chat
  - Avertissements
- Masquez les détails sensibles. Le message ne contient alors qu'un avis général indiquant qu'un événement de notification Bitcoin-Safe s'est produit.
- Définissez un délai d'envoi aléatoire jusqu'au maximum choisi.
- Les messages de transaction du portefeuille peuvent inclure un lien vers l'explorateur lorsqu'il est disponible et que les détails ne sont pas masqués.

### Suivre les envois

- L'historique récent affiche chaque événement, la destination, l'adaptateur, l'heure et le résultat : envoyé, partiel ou échoué.
- La livraison dépend de la destination configurée et de sa disponibilité. Tenez compte des informations que vous envoyez à des services externes.

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
<summary>Où Bitcoin-Safe peut-il envoyer des notifications ?</summary>

Bitcoin-Safe peut envoyer des notifications :

- Vers des webhooks : JSON générique, ou formats compatibles Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy et Gotify
- Par messages directs Nostr
- Vers des bots Telegram
- Par e-mail via SMTP
- Vers des calendriers CalDAV

</details>

<details>
<summary>Puis-je exclure les détails sensibles des alertes ?</summary>

Oui. Activez l'option masquer les détails sensibles : le message ne contient alors qu'un avis général indiquant qu'un événement de notification Bitcoin-Safe s'est produit.

</details>

<details>
<summary>Puis-je contrôler quels événements vont à quel endroit ?</summary>

Chaque destination a ses propres règles. Vous choisissez les types d'événements qu'elle reçoit :

- Transactions du portefeuille
- Paiements planifiés
- Sync et chat
- Avertissements

Vous pouvez aussi définir un délai d'envoi aléatoire optionnel.

</details>

<details>
<summary>L'application doit-elle rester déverrouillée ?</summary>

Non. Verrouiller et réduire dans la zone de notification garde Bitcoin-Safe actif en arrière-plan pendant que votre portefeuille reste verrouillé.

</details>
</content>
