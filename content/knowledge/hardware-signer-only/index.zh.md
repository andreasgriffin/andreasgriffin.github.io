---
title: "需要硬件签名器"
description: "Bitcoin Safe 在主网强制只允许硬件种子，以最大化安全性并避免基于软件的密钥存储风险。下面说明这为何重要。"
draft: false
tags: ["Featured", "Knowledge" ]
keywords: [
  "Bitcoin Safe",
  "硬件钱包",
  "软件种子",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "多重签名",
  "PSBT",
  "自我托管",
  "比特币安全",
  "地址中毒",
  "比特币工具"
]
images: ["logo.png" ]
# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=dbSmQmt0uDI"
weight: 21
---


![](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }

## 🚫 为什么 Bitcoin Safe 在主网禁止软件种子？

🤔 这是不是很不方便？

🔥 其实——这是一次重大的安全升级。

Bitcoin Safe **仅在 Testnet、Signet 和 Regtest 上允许软件种子**——在主网绝不允许。原因如下：

### ✅ 软件种子在主网被禁止的原因

- 🧠 **软件种子不安全**
  - 计算机充满了风险：剪贴板劫持、恶意软件、浏览器漏洞。
  - 稍有不慎，你的种子就会被泄露——一切都完了。
  - 冷存储绝不应从“热”状态开始。

</br>

- 🧊 **冷存储必须从冷开始**
  - 用户常常在软件钱包中生成种子，然后再迁移到硬件设备。
  - 但最初的暴露已经发生——无法回头。
  - 真正的冷存储 = 从一开始就在硬件签名器上创建。

</br>

- 🎣 **网络钓鱼利用软件习惯滋生**
  - 在应用中输入种子会训练你信任糟糕的交互模式。
  - 强制使用硬件可以养成更好的习惯并限制暴露面。
  - ✅ 主网无软件种子 = 更少的网络钓鱼受害者。

</br>

- 🧪 **开发者仍有灵活性**
  - 软件种子在以下网络是被允许的：
    - Testnet
    - Signet
    - Regtest
  - 非常适合开发人员。对真实聪(sats)没有风险。🧡



</br>


- 🔐 **主网要求使用硬件签名器——没有例外**
  - 🔌 USB、📷 QR、和 💾 SD 卡与所有主流设备兼容
    - [Coldcard]({{< ref "knowledge/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Foundation Passport]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Ledger]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Keystone]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "knowledge/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "knowledge/supported-hardware-signers" >}})
  - [查看所有支持的签名器 →]({{< ref "knowledge/supported-hardware-signers" >}})


---

## 🛡️ 地址中毒防护

Bitcoin Safe **用颜色标记接收地址**，让地址中毒一目了然：

- 🟢 绿色 = 验证过的接收地址  
- 🟡 黄色 = 找零地址  

如果有人试图用假地址污染你的剪贴板，你会立即看到。

![地址中毒检测示例](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ 通过 USB 或 QR 验证地址

直接在你的硬件签名器上验证接收地址——无需信任屏幕。

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ 每种硬件签名器的使用说明
 
- {{<text-name-with-logo>}} 包含每种硬件签名器的截图说明，引导你完成每一步 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-images >}}
    </div>

   
---



## 🤝 协作式多重签名，轻松实现

Bitcoin Safe 使多重签名对团队和用户都很友好：

- 🔐 加密的 Nostr 聊天  
- 🔁 一键 PSBT 共享  
- 🔌 USB、📷 QR、和 💾 SD 卡

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ 适合所有用户的强大功能

- 🟧 单签钱包向导  
- 🟨 2-of-3 多重签名设置  
- 🟩 任意 n-of-m 配置  
- 🖨️ 可打印的 PDF 备份表  
- 🔁 通过 Nostr 同步标签  
- 🔍 完整的资金流向图与可搜索的交易历史

![Bitcoin Safe 中的交易流程图](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 全球化且易用

- 多语言支持： {{< flags-short >}}
- 兼容：Windows、macOS & Linux  
- 拖放 PSBT / CSV  
- 面向交易、UTXO、金额等的高级筛选

---

## 💡 要点速览

Bitcoin Safe = 真正的比特币储蓄：

✅ 主网仅硬件  
✅ 无软件种子暴露  
✅ 面向初学者的多重签名友好体验  
✅ 面向开发者的测试环境友好  
✅ 适合家庭与团队的功能  

🔗 [Bitcoin-Safe.org]({{< ref "/" >}})  
🎥 YouTube 频道 →: https://youtube.com/@BitcoinSafeOrg