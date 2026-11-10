---
title: "Notifiche del portafoglio"
description: "Inoltra le notifiche del portafoglio e dell'app Bitcoin-Safe alle destinazioni che configuri, con controlli su consegna, privacy e tempistiche."
draft: false
tags: ["Plugins"]
images: ["notifications.png"]
weight: 35
faq:
  title: "Domande sulle notifiche del portafoglio"
  items:
    - question: "Dove può inviare notifiche Bitcoin-Safe?"
      answer: "Bitcoin-Safe può inviare notifiche a:\n- Webhook: JSON generico, o formati compatibili con Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy e Gotify\n- Messaggi diretti Nostr\n- Bot Telegram\n- Email tramite SMTP\n- Calendari CalDAV"
    - question: "Posso evitare che gli avvisi contengano dettagli sensibili?"
      answer: "Sì. Attiva l'opzione per nascondere i dettagli sensibili: il messaggio conterrà solo un avviso generico che indica che si è verificato un evento di notifica di Bitcoin-Safe."
    - question: "Posso controllare quali eventi finiscono in quale destinazione?"
      answer: "Ogni destinazione ha regole proprie. Scegli quali tipi di evento riceve:\n- Transazioni del portafoglio\n- Pagamenti programmati\n- Sync e chat\n- Avvisi\n\nPuoi inoltre impostare un ritardo casuale facoltativo nella consegna."
    - question: "L'app deve restare sbloccata?"
      answer: "No. Blocca e riduci a icona nell'area di notifica mantiene Bitcoin-Safe attivo in background mentre il portafoglio resta bloccato."
---

### {{< page-title >}}

<p class="lead">Ricevi aggiornamenti sull'attività del portafoglio attraverso i canali che preferisci.</p>

<ul class="plugin-features">
<li>Transazioni in entrata e in uscita, messaggi di Sync&Chat, pagamenti programmati in scadenza, ...</li>
<li>Inoltra gli avvisi a webhook, Nostr, Telegram, email, calendari e altro ancora</li>
<li>Scegli quali eventi riceve ogni destinazione e nascondi i dettagli sensibili</li>
<li>Tieni Bitcoin-Safe attivo in background; usa <strong>Blocca e riduci a icona</strong> per lasciarlo in esecuzione mentre il portafoglio è bloccato</li>
</ul>

### Configurare un webhook

{{< video "webhook.mp4" controls >}}

### Messaggi diretti Nostr

{{< video "nostr.mp4" controls >}}

### Notifiche sul calendario

{{< video "calendar.mp4" controls >}}

### Collegare le destinazioni

- Aggiungi una o più destinazioni. Ciascuna può avere propri destinatari e regole di consegna.
- **Email:** collegamento diretto a un server SMTP con host, porta, credenziali, mittente e impostazioni di sicurezza. Non si tratta di un'integrazione gestita con Gmail o Outlook.
- **Telegram:** invio a una chat tramite un bot. Avvia una conversazione con il bot per verificarlo e rilevare gli ID delle chat recenti.
- **Nostr DM:** invio di messaggi NIP-17 cifrati ai destinatari `npub` tramite relay configurati, con una chiave del mittente.
- **CalDAV:** aggiunta di eventi a un calendario esistente, ad esempio un calendario Nextcloud configurato.
- **Webhook:** invio in JSON generico o nei formati per endpoint compatibili con Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy e Gotify. I tipi di endpoint più comuni possono essere rilevati automaticamente.
- Salva le impostazioni della destinazione e usa l'azione di test dove disponibile.

### Scegliere cosa inviare

- Scegli quali tipi di evento riceve ogni destinazione:
  - Transazioni del portafoglio
  - Pagamenti programmati
  - Sync e chat
  - Avvisi
- Nascondi i dettagli sensibili. Il messaggio conterrà allora solo un avviso generico che indica che si è verificato un evento di notifica di Bitcoin-Safe.
- Imposta un ritardo casuale nella consegna fino al massimo scelto.
- I messaggi sulle transazioni del portafoglio possono includere un link all'explorer quando disponibile e se i dettagli non sono nascosti.

### Verificare le consegne

- La cronologia recente mostra ogni evento, destinazione, adattatore, orario e risultato: inviato, parziale o non riuscito.
- La consegna dipende dalla destinazione configurata e dalla sua disponibilità. Valuta quali informazioni invii a servizi esterni.

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">Scarica Bitcoin-Safe</h2>
<p class="text-muted mb-3">I plugin sono inclusi in Bitcoin-Safe. Scarica l'app per provarli.</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">Scarica Bitcoin-Safe</a>
<small class="text-muted">Software libero e open source · Windows, macOS, Linux</small>
</div>
</section>

### Domande frequenti

<details>
<summary>Dove può inviare notifiche Bitcoin-Safe?</summary>

Bitcoin-Safe può inviare notifiche a:

- Webhook: JSON generico, o formati compatibili con Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy e Gotify
- Messaggi diretti Nostr
- Bot Telegram
- Email tramite SMTP
- Calendari CalDAV

</details>

<details>
<summary>Posso evitare che gli avvisi contengano dettagli sensibili?</summary>

Sì. Attiva l'opzione per nascondere i dettagli sensibili: il messaggio conterrà solo un avviso generico che indica che si è verificato un evento di notifica di Bitcoin-Safe.

</details>

<details>
<summary>Posso controllare quali eventi finiscono in quale destinazione?</summary>

Ogni destinazione ha regole proprie. Scegli quali tipi di evento riceve:

- Transazioni del portafoglio
- Pagamenti programmati
- Sync e chat
- Avvisi

Puoi inoltre impostare un ritardo casuale facoltativo nella consegna.

</details>

<details>
<summary>L'app deve restare sbloccata?</summary>

No. Blocca e riduci a icona nell'area di notifica mantiene Bitcoin-Safe attivo in background mentre il portafoglio resta bloccato.

</details>
</content>
