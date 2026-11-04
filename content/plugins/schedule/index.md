---
aliases:
  - "/plugins/schedule/"
title: "Schedule"
description: "Plan one-time or recurring Bitcoin payments, track when they are due, and prepare transactions for review in Bitcoin-Safe."
draft: false
tags: ["Plugins"]
images: ["schedule.png"]
weight: 40
faq:
  title: "Scheduled Payments questions"
  items:
    - question: "Can I schedule a single payment or only recurring ones?"
      answer: "Both. You can create a one-time payment, a fixed number of repeats, or an ongoing schedule."
    - question: "How often can a schedule repeat?"
      answer: "By minutes, hours, days, weeks, months, or years. Weekly schedules can use selected weekdays; monthly and yearly schedules support calendar dates and weekday patterns."
    - question: "Can I set the amount in fiat?"
      answer: "Yes, in Bitcoin or a supported fiat currency. Fiat amounts can use a live rate or the CoinGecko rate fixed at 00:00 GMT, and an exchange-rate override can be set for the next payment."
    - question: "Are addresses reused?"
      answer: "No. Each recipient address is used only once. When a recipient's addresses run out, you can add more addresses for that recipient."
    - question: "Does Bitcoin-Safe send the payments automatically?"
      answer: "No. When a payment is due, Schedule prepares the transaction in Bitcoin-Safe for your review, and you remain responsible for signing and broadcasting it."
---

### {{< page-title >}}

<p class="lead">Plan Bitcoin payments and let Schedule keep track of what is due.</p>

<ul class="plugin-features">
<li>Pay employees or organize other regular obligations</li>
<li>Set up recurring transfers</li>
<li>Schedule a one-time payment you must not forget</li>
</ul>

When a payment is due, Schedule prepares the transaction in Bitcoin-Safe for your review. You remain responsible for signing and broadcasting it.

{{< video "schedule.mp4" controls >}}

### Flexible payment plans

- Choose a one-time payment, a fixed number of repeats, or an ongoing schedule.
- Set a start date and repeat interval: minutes, hours, days, weeks, months, or years. Weekly schedules can use selected weekdays; monthly and yearly schedules support calendar dates and weekday patterns.
- Set a recipient, category, and amount in Bitcoin or a supported fiat currency.
- For fiat amounts, use a live rate or the CoinGecko rate fixed at 00:00 GMT. An exchange-rate override can be set for the next payment.
- Fixed-count schedules show per-payment and total amount previews.

### Prepare payments in your wallet

- See the next due date and payment progress; due payments are highlighted and can trigger a Bitcoin-Safe notice.
- Prepare one due payment or a batch in the transaction composer, with recipient outputs, labels, and categories filled in.
- Review and customize the transaction before signing and broadcasting it yourself.
- Save reusable recipients with a name and multiple addresses. Schedule can select an unused address for a payout.

### Track and manage schedules

- Find schedules by due status, schedule type, or category. Lists show dates, completed payments, frequency, recipient, amount, category, and total.
- Review completed payouts and upcoming occurrences. Matching wallet transactions can update progress; you can also add a payout manually or rescan wallet transactions.
- Edit a schedule before its first recorded payout, duplicate or delete it, and import/export schedules as a JSON backup.

### Frequently asked questions

<details>
<summary>Can I schedule a single payment or only recurring ones?</summary>

Both. You can create a one-time payment, a fixed number of repeats, or an ongoing schedule.

</details>

<details>
<summary>How often can a schedule repeat?</summary>

By minutes, hours, days, weeks, months, or years. Weekly schedules can use selected weekdays; monthly and yearly schedules support calendar dates and weekday patterns.

</details>

<details>
<summary>Can I set the amount in fiat?</summary>

Yes, in Bitcoin or a supported fiat currency. Fiat amounts can use a live rate or the CoinGecko rate fixed at 00:00 GMT, and an exchange-rate override can be set for the next payment.

</details>

<details>
<summary>Are addresses reused?</summary>

No. Each recipient address is used only once. When a recipient's addresses run out, you can add more addresses for that recipient.

</details>

<details>
<summary>Does Bitcoin-Safe send the payments automatically?</summary>

No. When a payment is due, Schedule prepares the transaction in Bitcoin-Safe for your review, and you remain responsible for signing and broadcasting it.

</details>
