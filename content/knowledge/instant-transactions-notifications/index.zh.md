---
title: "即时交易通知"
description: "Bitcoin Safe 如何接收即时交易通知"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [
  "适合家庭的安全比特币钱包",
  "比特币",
  "比特币储蓄",
  "硬件签名器",
  "比特币托管人",
  "财务顾问",
  "比特币钱包",
  "trezor",
  "美国比特币",
  "BTC",
  "HODL",
  "比特币安全",
  "即时交易通知"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---



![Bitcoin Safe logo](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }


### {{< page-title >}}  
 
  


**Bitcoin Safe** (从 **1.5.0** 版本开始) 支持对与你的钱包相关的入站比特币交易进行即时通知。以下是其底层工作原理：




##### 1. 📡 监听比特币 P2P 网络

Bitcoin Safe 直接连接到一个或多个 **Bitcoin Core 节点**，这些节点参与全球的 **点对点 (P2P)** 网络。这些节点会持续交换新广播的、计划进入 **mempool** 的交易。

Bitcoin Safe 被动地监听这些广播消息，并检查是否：

* 任何交易涉及你钱包中的 **地址** 或 **UTXOs**。

✅ **隐私保护**
此方法是**完全私密的**。它不会向外界**泄露**有关你钱包的任何信息。
Bitcoin Safe 的行为就像一个普通的 Bitcoin Core 节点：仅监听公共 P2P 流量——不会为你的钱包单独公告或请求任何信息。



##### 2. 🧠 匹配到交易 — 接下来会发生什么？

如果发现匹配交易，Bitcoin Safe 会根据你使用的后端不同而采取不同的反应：

###### 选项 A：⚡ Electrum 或 Esplora 后端

* Bitcoin Safe 会**触发后台同步**，从服务器获取完整的交易和钱包状态。

###### 选项 B：🔍 紧凑区块过滤器（Neutrino 模式）

* 钱包会**直接将未确认的交易添加**到本地钱包数据中——无需进一步查询。



#### ⚙️ 选择加入/退出行为

为尊重用户偏好和隐私设置：

* 🔒 **对于已存在的用户**，升级到 1.5.0 或更高版本时，此功能默认为**选择加入（opt-in）**——你可以在网络设置中手动启用它。
* 🚀 **对于新用户**，此功能默认**启用（可选择退出）**，因为它既**保护隐私**又**非常有用**，能够实时跟踪钱包活动。

你始终完全掌控此功能，可以随时切换。
 
 

![Notification settings screenshot](config.png)
{ .img-fluid .mb-5 }


#### ⚠️ 仅已确认的交易可被信任

Bitcoin Safe 无法验证广播的交易本身是否有效。攻击者——尤其是同时控制你的 Electrum 服务器和你连接的比特币节点的攻击者——可能会：

* 构造一个涉及你地址的伪造交易
* 广播它以触发钱包通知
* 确保它永远不会被确认，因为它**无效**或**与共识规则冲突**


  


#### ✅ 总结

从 **1.5.0** 版本开始，Bitcoin Safe 通过以下方式支持即时交易通知：

* 被动监听比特币 P2P 网络（像 Bitcoin Core 一样）
* 匹配涉及你钱包 **地址** 或 **UTXOs** 的交易
* 通过 Electrum/Esplora 获取完整细节，或通过紧凑区块过滤器直接添加
* 从不向外界泄露任何钱包数据