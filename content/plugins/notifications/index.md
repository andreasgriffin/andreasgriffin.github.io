---
aliases:
  - "/plugins/notifications/"
title: "Notifications"
description: "Forward Bitcoin-Safe wallet and app notifications to destinations you configure, with per-destination delivery, privacy, and timing controls."
draft: false
tags: ["Plugins"]
images: ["notifications.png"]
weight: 35
faq:
  title: "Wallet Notifications questions"
  items:
    - question: "Where can Bitcoin-Safe send notifications?"
      answer: "Bitcoin-Safe can send notifications to:\n- Webhooks: generic JSON, or Slack-compatible, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy, and Gotify formats\n- Nostr direct messages\n- Telegram bots\n- Email over SMTP\n- CalDAV calendars"
    - question: "Can I keep sensitive details out of the alerts?"
      answer: "Yes. Turn on hiding sensitive details and the message contains only a generic notice that a Bitcoin-Safe notification event occurred."
    - question: "Do I control which events go where?"
      answer: "Each destination has its own rules. You choose which event types it receives:\n- Wallet transactions\n- Scheduled payments\n- Sync and chat\n- Warnings\n\nYou can also set an optional randomized delivery delay."
    - question: "Does the app need to stay unlocked?"
      answer: "No. Lock and Minimize to Tray keeps Bitcoin-Safe running in the background while your wallet stays locked."
---

### {{< page-title >}}

<p class="lead">Get notified about wallet activity through the channels that work for you.</p>

<ul class="plugin-features">
<li>Get alerts about wallet transactions, scheduled payments, Sync &amp; Chat messages, and warnings</li>
<li>Forward notifications to webhooks, Nostr, Telegram, email, or calendars</li>
<li>Choose which events each destination receives and hide sensitive details</li>
<li>Keep Bitcoin-Safe running in the background with <strong>Lock and Minimize to Tray</strong>, even while your wallet is locked</li>
</ul>

### Webhook setup

{{< video "webhook.mp4" controls >}}

### Nostr direct messages

{{< video "nostr.mp4" controls >}}

### Calendar notifications

{{< video "calendar.mp4" controls >}}

### Connect your destinations

- 🔗 Add multiple destinations, each with its own recipients and delivery rules.
- ✉️ **Email:** Connect to an SMTP server using your host, port, credentials, sender, and security settings.
- 💬 **Telegram:** Send to a chat through a bot. Start a conversation to check the bot and detect recent chat IDs.
- 🟣 **Nostr:** Send encrypted NIP-17 direct messages to `npub` recipients through configured relays with a sender key.
- 📆 **Calendars:** Add events to an existing CalDAV calendar, such as a configured Nextcloud calendar.
- 🪝 **Webhooks:** Send Generic JSON or formats for Slack-compatible endpoints, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy, and Gotify.
- 🧪 Save destination settings and test the connection where supported.

### Choose what gets sent

- Set per-destination rules for wallet transactions, scheduled payments, Sync & Chat activity, and warnings.
- Hide sensitive details so notifications contain only a generic Bitcoin-Safe event notice.
- Add a randomized delivery delay up to your chosen maximum.
- Wallet transaction notifications can include an explorer link when available, unless details are hidden.

### Review delivery

- Recent history shows the event, destination, adapter, time, and delivery result: sent, partial, or failed.
- Notifications depend on your destination's availability. Consider what information you send to external services.

{{< plugin-pricing plan="notifications" >}}

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">Get Bitcoin-Safe</h2>
<p class="text-muted mb-3">Plugins ship with Bitcoin-Safe. Download the app to try them.</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">Download Bitcoin-Safe</a>
<small class="text-muted">Free &amp; open source · Windows, macOS, Linux</small>
</div>
</section>

### Frequently asked questions

<details>
<summary>Where can Bitcoin-Safe send notifications?</summary>

Bitcoin-Safe can send notifications to:

- Webhooks: generic JSON, or Slack-compatible, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy, and Gotify formats
- Nostr direct messages
- Telegram bots
- Email over SMTP
- CalDAV calendars

</details>

<details>
<summary>Can I keep sensitive details out of the alerts?</summary>

Yes. Turn on hiding sensitive details and the message contains only a generic notice that a Bitcoin-Safe notification event occurred.

</details>

<details>
<summary>Do I control which events go where?</summary>

Each destination has its own rules. You choose which event types it receives:

- Wallet transactions
- Scheduled payments
- Sync and chat
- Warnings

You can also set an optional randomized delivery delay.

</details>

<details>
<summary>Does the app need to stay unlocked?</summary>

No. Lock and Minimize to Tray keeps Bitcoin-Safe running in the background while your wallet stays locked.

</details>
