---
aliases:
  - "/plugins/notifications/"
title: "Notifications"
description: "Forward Bitcoin-Safe wallet and app notifications to destinations you configure, with per-destination delivery, privacy, and timing controls."
draft: false
tags: ["Plugins"]
images: ["notifications.png"]
weight: 35
---

### {{< page-title >}}

<p class="lead">Get notified about wallet activity through the channels that work for you.</p>

- Incoming and outgoing transactions, Chat&Sync messages, due scheduled payments, ...
- Forward alerts to webhooks, Nostr, Telegram, email, calendars, and more
- Choose which events each destination receives and hide sensitive details
- Keep Bitcoin-Safe running in the background; use <strong>Lock and Minimize to Tray</strong> to leave it running while your wallet is locked


### Webhook setup

{{< video "webhook.mp4" controls >}}

### Nostr direct messages

{{< video "nostr.mp4" controls >}}

### Calendar notifications

{{< video "calendar.mp4" controls >}}

### Connect your destinations

- Add one or more destinations. Each can have its own recipients and delivery rules.
- **Email:** Connect directly to an SMTP server with your host, port, credentials, sender, and security settings. This is not a managed Gmail or Outlook integration.
- **Telegram:** Send to a chat using a bot. Start a conversation with the bot to check it and detect recent chat IDs.
- **Nostr DM:** Send encrypted NIP-17 messages to `npub` recipients through configured relays with a sender key.
- **CalDAV:** Add events to an existing calendar, such as a configured Nextcloud calendar.
- **Webhooks:** Send Generic JSON or formats for Slack-compatible endpoints, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy, and Gotify. Common endpoint types may be detected automatically.
- Save the destination settings and use the test action where supported.

### Choose what gets sent

- Choose which event types each destination receives:
  - Wallet transactions
  - Scheduled payments
  - Sync and chat
  - Warnings
- Hide sensitive details. The message then contains only a generic notice that a Bitcoin-Safe notification event occurred.
- Set a randomized delivery delay up to your chosen maximum.
- Wallet transaction messages may include an explorer link when available and details are not hidden.

### Review delivery

- Recent history shows each event, destination, adapter, time, and result: sent, partial, or failed.
- Delivery depends on your configured destination and its availability. Consider what information you send to external services.

