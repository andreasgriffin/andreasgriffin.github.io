---
title: "Wallet-Benachrichtigungen"
description: "Leite Wallet- und App-Benachrichtigungen von Bitcoin-Safe an selbst konfigurierte Ziele weiter, mit Steuerung von Zustellung, Datenschutz und Zeitpunkt."
draft: false
tags: ["Plugins"]
images: ["notifications.png"]
weight: 35
faq:
  title: "Fragen zu Wallet-Benachrichtigungen"
  items:
    - question: "Wohin kann Bitcoin-Safe Benachrichtigungen senden?"
      answer: "Bitcoin-Safe kann Benachrichtigungen senden an:\n- Webhooks: generisches JSON oder Formate für Slack-kompatible Dienste, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy und Gotify\n- Nostr-Direktnachrichten\n- Telegram-Bots\n- E-Mail über SMTP\n- CalDAV-Kalender"
    - question: "Kann ich sensible Details aus den Benachrichtigungen heraushalten?"
      answer: "Ja. Aktiviere das Ausblenden sensibler Details, dann enthält die Nachricht nur einen allgemeinen Hinweis, dass ein Bitcoin-Safe-Benachrichtigungsereignis aufgetreten ist."
    - question: "Kann ich steuern, welche Ereignisse wohin gehen?"
      answer: "Jedes Ziel hat eigene Regeln. Du wählst, welche Ereignistypen es erhält:\n- Wallet-Transaktionen\n- Geplante Zahlungen\n- Sync und Chat\n- Warnungen\n\nZusätzlich kannst du eine optionale zufällige Verzögerung der Zustellung festlegen."
    - question: "Muss die App entsperrt bleiben?"
      answer: "Nein. Mit „Sperren und in den Infobereich minimieren“ läuft Bitcoin-Safe im Hintergrund weiter, während deine Wallet gesperrt bleibt."
---

### {{< page-title >}}

<p class="lead">Erhalte Benachrichtigungen über Wallet-Aktivitäten über die Kanäle, die für dich funktionieren.</p>

<ul class="plugin-features">
<li>Eingehende und ausgehende Transaktionen, Sync-&-Chat-Nachrichten, fällige geplante Zahlungen, ...</li>
<li>Warnungen an Webhooks, Nostr, Telegram, E-Mail, Kalender und mehr weiterleiten</li>
<li>Wähle, welche Ereignisse jedes Ziel erhält, und blende sensible Details aus</li>
<li>Halte Bitcoin-Safe im Hintergrund am Laufen; mit <strong>Sperren und in den Infobereich minimieren</strong> bleibt es aktiv, während die Wallet gesperrt ist</li>
</ul>

### Webhook einrichten

{{< video "webhook.mp4" controls >}}

### Nostr-Direktnachrichten

{{< video "nostr.mp4" controls >}}

### Kalenderbenachrichtigungen

{{< video "calendar.mp4" controls >}}

### Ziele verbinden

- Füge ein oder mehrere Ziele hinzu. Jedes kann eigene Empfänger und Zustellregeln haben.
- **E-Mail:** Verbinde dich direkt mit einem SMTP-Server über Host, Port, Zugangsdaten, Absender und Sicherheitseinstellungen. Dies ist keine verwaltete Gmail- oder Outlook-Integration.
- **Telegram:** Sende an einen Chat über einen Bot. Starte eine Unterhaltung mit dem Bot, um ihn zu prüfen und aktuelle Chat-IDs zu erkennen.
- **Nostr-DM:** Sende verschlüsselte NIP-17-Nachrichten an `npub`-Empfänger über konfigurierte Relays mit einem Absenderschlüssel.
- **CalDAV:** Füge Ereignisse einem bestehenden Kalender hinzu, etwa einem konfigurierten Nextcloud-Kalender.
- **Webhooks:** Sende generisches JSON oder Formate für Slack-kompatible Endpunkte, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy und Gotify. Gängige Endpunkttypen werden teilweise automatisch erkannt.
- Speichere die Einstellungen des Ziels und nutze, wo unterstützt, die Testfunktion.

### Auswählen, was gesendet wird

- Wähle, welche Ereignistypen jedes Ziel erhält:
  - Wallet-Transaktionen
  - Geplante Zahlungen
  - Sync und Chat
  - Warnungen
- Sensible Details ausblenden. Die Nachricht enthält dann nur einen allgemeinen Hinweis, dass ein Bitcoin-Safe-Benachrichtigungsereignis aufgetreten ist.
- Lege eine zufällige Zustellverzögerung bis zu deinem gewählten Maximum fest.
- Nachrichten zu Wallet-Transaktionen können einen Explorer-Link enthalten, wenn verfügbar und die Details nicht ausgeblendet sind.

### Zustellung prüfen

- Der Verlauf zeigt jedes Ereignis, Ziel, Adapter, Zeitpunkt und Ergebnis: gesendet, teilweise oder fehlgeschlagen.
- Die Zustellung hängt von deinem konfigurierten Ziel und seiner Verfügbarkeit ab. Bedenke, welche Informationen du an externe Dienste sendest.

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">Bitcoin-Safe herunterladen</h2>
<p class="text-muted mb-3">Plugins sind in Bitcoin-Safe enthalten. Lade die App herunter, um sie auszuprobieren.</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">Bitcoin-Safe herunterladen</a>
<small class="text-muted">Freie &amp; Open-Source-Software · Windows, macOS, Linux</small>
</div>
</section>

### Häufig gestellte Fragen

<details>
<summary>Wohin kann Bitcoin-Safe Benachrichtigungen senden?</summary>

Bitcoin-Safe kann Benachrichtigungen senden an:

- Webhooks: generisches JSON oder Formate für Slack-kompatible Dienste, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy und Gotify
- Nostr-Direktnachrichten
- Telegram-Bots
- E-Mail über SMTP
- CalDAV-Kalender

</details>

<details>
<summary>Kann ich sensible Details aus den Benachrichtigungen heraushalten?</summary>

Ja. Aktiviere das Ausblenden sensibler Details, dann enthält die Nachricht nur einen allgemeinen Hinweis, dass ein Bitcoin-Safe-Benachrichtigungsereignis aufgetreten ist.

</details>

<details>
<summary>Kann ich steuern, welche Ereignisse wohin gehen?</summary>

Jedes Ziel hat eigene Regeln. Du wählst, welche Ereignistypen es erhält:

- Wallet-Transaktionen
- Geplante Zahlungen
- Sync und Chat
- Warnungen

Zusätzlich kannst du eine optionale zufällige Verzögerung der Zustellung festlegen.

</details>

<details>
<summary>Muss die App entsperrt bleiben?</summary>

Nein. Mit „Sperren und in den Infobereich minimieren“ läuft Bitcoin-Safe im Hintergrund weiter, während deine Wallet gesperrt bleibt.

</details>
</content>
