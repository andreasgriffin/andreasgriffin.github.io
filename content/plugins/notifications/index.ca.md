---
title: "Notificacions de la cartera"
description: "Reenvia les notificacions de la cartera i de l'aplicació Bitcoin-Safe a les destinacions que configuris, amb controls de lliurament, privadesa i temporització."
draft: false
tags: ["Plugins"]
images: ["notifications.png"]
weight: 35
faq:
  title: "Preguntes sobre les notificacions de la cartera"
  items:
    - question: "On pot enviar notificacions Bitcoin-Safe?"
      answer: "Bitcoin-Safe pot enviar notificacions a:\n- Webhooks: JSON genèric, o formats compatibles amb Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy i Gotify\n- Missatges directes de Nostr\n- Bots de Telegram\n- Correu electrònic mitjançant SMTP\n- Calendaris CalDAV"
    - question: "Puc evitar que les alertes incloguin detalls sensibles?"
      answer: "Sí. Activa l'opció d'amagar els detalls sensibles i el missatge només contindrà un avís genèric que s'ha produït un esdeveniment de notificació de Bitcoin-Safe."
    - question: "Controlo quins esdeveniments van a cada destinació?"
      answer: "Cada destinació té les seves pròpies regles. Tries quins tipus d'esdeveniments rep:\n- Transaccions de la cartera\n- Pagaments programats\n- Sincronització i xat\n- Advertiments\n\nTambé pots definir un retard aleatori opcional en el lliurament."
    - question: "Cal que l'aplicació continuï desbloquejada?"
      answer: "No. L'opció «Bloqueja i minimitza a la safata» manté Bitcoin-Safe en execució en segon pla mentre la cartera està bloquejada."
---

### {{< page-title >}}

<p class="lead">Rep notificacions de l'activitat de la cartera pels canals que et convinguin.</p>

<ul class="plugin-features">
<li>Transaccions entrants i sortints, missatges de Sync&Chat, pagaments programats vençuts, ...</li>
<li>Reenvia les alertes a webhooks, Nostr, Telegram, correu electrònic, calendaris i més</li>
<li>Tria quins esdeveniments rep cada destinació i amaga els detalls sensibles</li>
<li>Mantín Bitcoin-Safe en segon pla; fes servir <strong>Bloqueja i minimitza a la safata</strong> per deixar-lo en marxa mentre la cartera està bloquejada</li>
</ul>

### Configuració d'un webhook

{{< video "webhook.mp4" controls >}}

### Missatges directes de Nostr

{{< video "nostr.mp4" controls >}}

### Notificacions al calendari

{{< video "calendar.mp4" controls >}}

### Connecta les teves destinacions

- Afegeix una o més destinacions. Cadascuna pot tenir els seus propis destinataris i regles de lliurament.
- **Correu electrònic:** connexió directa a un servidor SMTP amb el host, el port, les credencials, el remitent i la configuració de seguretat. No és una integració gestionada amb Gmail ni Outlook.
- **Telegram:** enviament a un xat mitjançant un bot. Inicia una conversa amb el bot per comprovar-lo i detectar identificadors de xat recents.
- **Nostr DM:** enviament de missatges NIP-17 xifrats als destinataris `npub` a través de relés configurats amb una clau de remitent.
- **CalDAV:** afegeix esdeveniments a un calendari existent, com ara un calendari de Nextcloud configurat.
- **Webhooks:** enviament en JSON genèric o en formats per a punts finals compatibles amb Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy i Gotify. Els tipus habituals de punt final es poden detectar automàticament.
- Desa la configuració de la destinació i utilitza l'acció de prova quan hi sigui disponible.

### Tria què s'envia

- Tria quins tipus d'esdeveniments rep cada destinació:
  - Transaccions de la cartera
  - Pagaments programats
  - Sincronització i xat
  - Advertiments
- Amaga els detalls sensibles. Aleshores el missatge només contindrà un avís genèric que s'ha produït un esdeveniment de notificació de Bitcoin-Safe.
- Defineix un retard aleatori en el lliurament fins al màxim que triïs.
- Els missatges de transaccions de la cartera poden incloure un enllaç a l'explorador quan estigui disponible i els detalls no siguin amagats.

### Revisa el lliurament

- L'historial recent mostra cada esdeveniment, destinació, adaptador, hora i resultat: enviat, parcial o fallit.
- El lliurament depèn de la destinació configurada i de la seva disponibilitat. Considera quina informació envies a serveis externs.

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">Descarrega Bitcoin-Safe</h2>
<p class="text-muted mb-3">Els plugins estan inclosos a Bitcoin-Safe. Descarrega l'aplicació per provar-los.</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">Descarrega Bitcoin-Safe</a>
<small class="text-muted">Programari lliure i de codi obert · Windows, macOS, Linux</small>
</div>
</section>

### Preguntes freqüents

<details>
<summary>On pot enviar notificacions Bitcoin-Safe?</summary>

Bitcoin-Safe pot enviar notificacions a:

- Webhooks: JSON genèric, o formats compatibles amb Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy i Gotify
- Missatges directes de Nostr
- Bots de Telegram
- Correu electrònic mitjançant SMTP
- Calendaris CalDAV

</details>

<details>
<summary>Puc evitar que les alertes incloguin detalls sensibles?</summary>

Sí. Activa l'opció d'amagar els detalls sensibles i el missatge només contindrà un avís genèric que s'ha produït un esdeveniment de notificació de Bitcoin-Safe.

</details>

<details>
<summary>Controlo quins esdeveniments van a cada destinació?</summary>

Cada destinació té les seves pròpies regles. Tries quins tipus d'esdeveniments rep:

- Transaccions de la cartera
- Pagaments programats
- Sincronització i xat
- Advertiments

També pots definir un retard aleatori opcional en el lliurament.

</details>

<details>
<summary>Cal que l'aplicació continuï desbloquejada?</summary>

No. L'opció «Bloqueja i minimitza a la safata» manté Bitcoin-Safe en execució en segon pla mentre la cartera està bloquejada.

</details>
</content>
