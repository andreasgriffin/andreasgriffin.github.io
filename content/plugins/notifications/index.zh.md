---
title: "钱包通知"
description: "将 Bitcoin-Safe 的钱包和应用通知转发到您配置的目标，可控制投递方式、隐私保护和发送时间。"
draft: false
tags: ["Plugins"]
images: ["notifications.png"]
weight: 35
faq:
  title: "钱包通知相关问题"
  items:
    - question: "Bitcoin-Safe 可以将通知发送到哪里？"
      answer: "Bitcoin-Safe 可以将通知发送到：\n- Webhook：通用 JSON，或兼容 Slack、Discord、Google Chat、Microsoft Teams、Telegram Bot API、ntfy 和 Gotify 的格式\n- Nostr 私信\n- Telegram 机器人\n- 通过 SMTP 发送的电子邮件\n- CalDAV 日历"
    - question: "可以从提醒中去除敏感信息吗？"
      answer: "可以。开启隐藏敏感详情后，消息中只会包含一条通用提示，说明发生了一个 Bitcoin-Safe 通知事件。"
    - question: "我能控制哪些事件发送到哪里吗？"
      answer: "每个目标都有自己的规则。您可以选择它接收的事件类型：\n- 钱包交易\n- 计划付款\n- 同步与聊天\n- 警告\n\n您还可以设置可选的随机发送延迟。"
    - question: "应用需要保持解锁状态吗？"
      answer: "不需要。使用“锁定并最小化到托盘”，即可在钱包锁定时让 Bitcoin-Safe 继续在后台运行。"
---

### {{< page-title >}}

<p class="lead">通过适合您的渠道，及时了解钱包活动。</p>

<ul class="plugin-features">
<li>收款和付款交易、Sync&Chat 消息、到期的计划付款等……</li>
<li>将提醒转发到 Webhook、Nostr、Telegram、电子邮件、日历等</li>
<li>为每个目标选择接收的事件，并隐藏敏感详情</li>
<li>让 Bitcoin-Safe 在后台运行：使用<strong>锁定并最小化到托盘</strong>，即可在钱包锁定时保持应用运行</li>
</ul>

### 设置 Webhook

{{< video "webhook.mp4" controls >}}

### Nostr 私信

{{< video "nostr.mp4" controls >}}

### 日历通知

{{< video "calendar.mp4" controls >}}

### 连接您的目标

- 添加一个或多个目标。每个目标都可以有自己的接收者和投递规则。
- **电子邮件：** 使用主机、端口、凭据、发件人和安全设置直接连接 SMTP 服务器。这不是托管的 Gmail 或 Outlook 集成。
- **Telegram：** 通过机器人发送到聊天。先与机器人发起对话，即可验证机器人并检测最近的聊天 ID。
- **Nostr 私信：** 通过已配置的中继，使用发件人密钥向 `npub` 接收者发送加密的 NIP-17 消息。
- **CalDAV：** 将事件添加到现有日历，例如已配置的 Nextcloud 日历。
- **Webhook：** 以通用 JSON 或适用于 Slack 兼容端点、Discord、Google Chat、Microsoft Teams、Telegram Bot API、ntfy 和 Gotify 的格式发送。常见端点类型可能会被自动识别。
- 保存目标设置，并在支持的情况下使用测试功能。

### 选择发送内容

- 选择每个目标接收的事件类型：
  - 钱包交易
  - 计划付款
  - 同步与聊天
  - 警告
- 隐藏敏感详情。此时消息中只会包含一条通用提示，说明发生了一个 Bitcoin-Safe 通知事件。
- 设置随机发送延迟，最长不超过您选择的时间。
- 在可用且未隐藏详情的情况下，钱包交易消息可能包含区块浏览器链接。

### 查看投递情况

- 最近记录会显示每个事件、目标、适配器、时间和结果：已发送、部分发送或失败。
- 投递取决于您配置的目标及其可用性。请注意您发送给外部服务的信息。

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">下载 Bitcoin-Safe</h2>
<p class="text-muted mb-3">插件已包含在 Bitcoin-Safe 中。下载应用即可试用。</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">下载 Bitcoin-Safe</a>
<small class="text-muted">免费开源 · Windows、macOS、Linux</small>
</div>
</section>

### 常见问题

<details>
<summary>Bitcoin-Safe 可以将通知发送到哪里？</summary>

Bitcoin-Safe 可以将通知发送到：

- Webhook：通用 JSON，或兼容 Slack、Discord、Google Chat、Microsoft Teams、Telegram Bot API、ntfy 和 Gotify 的格式
- Nostr 私信
- Telegram 机器人
- 通过 SMTP 发送的电子邮件
- CalDAV 日历

</details>

<details>
<summary>可以从提醒中去除敏感信息吗？</summary>

可以。开启隐藏敏感详情后，消息中只会包含一条通用提示，说明发生了一个 Bitcoin-Safe 通知事件。

</details>

<details>
<summary>我能控制哪些事件发送到哪里吗？</summary>

每个目标都有自己的规则。您可以选择它接收的事件类型：

- 钱包交易
- 计划付款
- 同步与聊天
- 警告

您还可以设置可选的随机发送延迟。

</details>

<details>
<summary>应用需要保持解锁状态吗？</summary>

不需要。使用“锁定并最小化到托盘”，即可在钱包锁定时让 Bitcoin-Safe 继续在后台运行。

</details>
</content>
