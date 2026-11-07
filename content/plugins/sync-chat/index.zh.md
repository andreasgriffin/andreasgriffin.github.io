---
title: "Sync & Chat"
description: "发现钱包中的其他参与方，同步标签和类别，安全聊天，并一键共享 PSBT。"
draft: false
tags: ["Plugins", "sync-chat-mainpage"]
images: ["logo.png"]
weight: 30
faq:
  title: "Sync & Chat 相关问题"
  items:
    - question: "设备之间如何相互发现？"
      answer: "Sync & Chat 会查找使用相同钱包描述符的其他设备。描述符在用于发现之前会先进行哈希处理，因此不会以明文形式暴露。此外，每个被发现的设备都必须手动添加并标记为受信任，才能参与聊天。因此，即使描述符不是秘密，聊天依然是安全的。"
    - question: "协作在实际中如何运作？"
      answer: "1. 设置（只需一次）：添加每位参与者的设备，并将其标记为受信任。\n2. 创建：一位参与者创建 PSBT 并添加自己的签名。\n3. 共享：将 PSBT 发送给所有参与者，或只发送给选定的参与者。\n4. 签名：每位参与者依次添加签名，直到交易完全签名。\n5. 广播：最后一位签名者广播交易，交易随后会出现在所有参与者的钱包中。"
    - question: "会同步哪些内容？"
      answer: "Sync & Chat 会同步：\n- 币的类别和标签，在签名者之间同步，即使操作系统不同也可以\n- 一键共享 PSBT"
    - question: "聊天是私密的吗？"
      answer: "是的。钱包聊天经过加密，并通过 Nostr 传输；标签备份也会通过 Nostr 加密存储。"
---

### {{< page-title >}}

<p class="lead">在 Bitcoin-Safe 中协调多签签名者，并让钱包信息保持同步。</p>

<ul class="plugin-features">
<li>发现使用相同钱包描述符的其他设备</li>
<li>在签名者之间同步标签和类别</li>
<li>安全聊天，并一键共享 PSBT</li>
</ul>

### 标签同步

{{< video src="../../library/label-sync/label-sync.mp4" controls="true" >}}

### 协作签名

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

有关多签协作签名的完整教程，请参阅[多签中的协作]({{< ref "library/collaboration/" >}})。

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
<summary>设备之间如何相互发现？</summary>

Sync & Chat 会查找使用相同钱包描述符的其他设备。描述符在用于发现之前会先进行哈希处理，因此不会以明文形式暴露。此外，每个被发现的设备都必须手动添加并标记为受信任，才能参与聊天。因此，即使描述符不是秘密，聊天依然是安全的。

</details>

<details>
<summary>协作在实际中如何运作？</summary>

1. **设置（只需一次）：** 添加每位参与者的设备，并将其标记为受信任。
2. **创建：** 一位参与者创建 PSBT 并添加自己的签名。
3. **共享：** 将 PSBT 发送给所有参与者，或只发送给选定的参与者。
4. **签名：** 每位参与者依次添加签名，直到交易完全签名。
5. **广播：** 最后一位签名者广播交易，交易随后会出现在所有参与者的钱包中。

</details>

<details>
<summary>会同步哪些内容？</summary>

Sync & Chat 会同步：

- 币的类别和标签，在签名者之间同步，即使操作系统不同也可以
- 一键共享 PSBT

</details>

<details>
<summary>聊天是私密的吗？</summary>

是的。钱包聊天经过加密，并通过 Nostr 传输；标签备份也会通过 Nostr 加密存储。

</details>

{{< sync-page-box >}}
</content>
