---
aliases:
  - "/plugins/notifications/"
title: "Wallet Notifications"
date: "2026-11-04"
description: "Forward Bitcoin-Safe wallet and app notifications to webhooks, Nostr, Telegram, email, or calendars, with per-destination delivery, privacy, and timing controls."
draft: false
tags: ["Plugins"]
images: ["notifications.png"]
weight: 35
lead: "Get notified about wallet activity through the channels that work for you."
features:
  - "Incoming and outgoing transactions, Chat & Sync messages, due scheduled payments"
  - "Forward alerts to webhooks, Nostr, Telegram, email, calendars, and more"
  - "Choose which events each destination receives and hide sensitive details"
  - "Keep Bitcoin-Safe running in the background with Lock and Minimize to Tray"
media:
  - type: video
    src: "webhook.mp4"
    heading: "Webhook setup"
    caption: "Connecting a webhook destination and sending a test notification."
  - type: video
    src: "nostr.mp4"
    heading: "Nostr direct messages"
    caption: "Sending encrypted NIP-17 direct messages to npub recipients."
  - type: video
    src: "calendar.mp4"
    heading: "Calendar notifications"
    caption: "Adding Bitcoin-Safe events to a CalDAV calendar."
faq:
  title: "Wallet Notifications questions"
  items:
    - question: "Where can Bitcoin-Safe send notifications?"
      answer: "To webhooks (generic JSON or Slack-compatible, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy, and Gotify formats), Nostr direct messages, Telegram bots, email over SMTP, and CalDAV calendars."
    - question: "Can I keep sensitive details out of the alerts?"
      answer: "Yes. Turn on hiding sensitive details and the message contains only a generic notice that a Bitcoin-Safe notification event occurred."
    - question: "Do I control which events go where?"
      answer: "Each destination has its own rules for which event types it receives, such as wallet transactions, scheduled payments, sync and chat, or warnings, plus an optional randomized delivery delay."
    - question: "Does the app need to stay unlocked?"
      answer: "No. Lock and Minimize to Tray keeps Bitcoin-Safe running in the background while your wallet stays locked."
---

## Connect your destinations

- Add one or more destinations. Each can have its own recipients and delivery rules.
- **Email:** Connect directly to an SMTP server with your host, port, credentials, sender, and security settings. This is not a managed Gmail or Outlook integration.
- **Telegram:** Send to a chat using a bot. Start a conversation with the bot to check it and detect recent chat IDs.
- **Nostr DM:** Send encrypted NIP-17 messages to `npub` recipients through configured relays with a sender key.
- **CalDAV:** Add events to an existing calendar, such as a configured Nextcloud calendar.
- **Webhooks:** Send Generic JSON or formats for Slack-compatible endpoints, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy, and Gotify. Common endpoint types may be detected automatically.
- Save the destination settings and use the test action where supported.

## Choose what gets sent

- Choose which event types each destination receives:
  - Wallet transactions
  - Scheduled payments
  - Sync and chat
  - Warnings
- Hide sensitive details. The message then contains only a generic notice that a Bitcoin-Safe notification event occurred.
- Set a randomized delivery delay up to your chosen maximum.
- Wallet transaction messages may include an explorer link when available and details are not hidden.

## Review delivery

- Recent history shows each event, destination, adapter, time, and result: sent, partial, or failed.
- Delivery depends on your configured destination and its availability. Consider what information you send to external services.
