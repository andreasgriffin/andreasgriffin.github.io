---
title: "紧凑区块过滤器"
description: "了解什么是紧凑区块过滤器，以及它们如何比 Electrum 服务器更好地保护隐私。"
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "紧凑区块过滤器"
  - "CBF"
  - "隐私"
  - "比特币钱包"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**紧凑区块过滤器（CBF）** 让 [Bitcoin Safe]({{< ref "/" >}}) 无需向 Electrum 服务器询问你的地址，也能扫描区块链。

![Bitcoin Safe 从多个随机 Bitcoin Core 对等节点下载紧凑区块过滤器。](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

Bitcoin Safe 不会查询中心服务器，而是从随机的 Bitcoin Core 对等节点为每个区块下载一个很小的过滤器。钱包在本地检查这些过滤器，只在需要时下载完整区块。

### CBF 与 Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">项目</th>
        <th scope="col">紧凑区块过滤器</th>
        <th scope="col">Electrum 服务器</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">隐私</th>
        <td><span class="text-success fw-semibold">好</span> - 钱包数据保持本地</td>
        <td><span class="text-danger fw-semibold">差</span> - 服务器可以看到你的地址和历史</td>
      </tr>
      <tr>
        <th scope="row">数据来源</th>
        <td><span class="text-success fw-semibold">好</span> - 随机的 Bitcoin Core 对等节点</td>
        <td><span class="text-warning fw-semibold">中立</span> - 一个你选择的服务器</td>
      </tr>
      <tr>
        <th scope="row">初次同步</th>
        <td><span class="text-warning fw-semibold">中立</span> - 通常较慢</td>
        <td><span class="text-success fw-semibold">好</span> - 通常较快</td>
      </tr>
      <tr>
        <th scope="row">持续同步</th>
        <td><span class="text-success fw-semibold">好</span> - 首次同步后非常快</td>
        <td><span class="text-success fw-semibold">好</span> - 通常很快</td>
      </tr>
      <tr>
        <th scope="row">适合</th>
        <td><span class="text-success fw-semibold">好</span> - 重视隐私的用户</td>
        <td><span class="text-success fw-semibold">好</span> - 希望最快完成设置和恢复的用户</td>
      </tr>
    </tbody>
  </table>
</div>

### 为什么使用 CBF

- 更好的隐私：你的钱包不会向服务器询问你的地址。
- 不依赖可信索引器：Bitcoin Safe 直接与比特币网络通信。
- 轻量同步：过滤器很小，不需要整条区块链。

### 你可以期待什么

- 新钱包或恢复钱包：首次同步通常需要 **5 到 30 分钟**。
- 已同步的钱包：通常会 **非常快** 赶上，往往在 **30 秒以内**。
- 从 Electrum 切换到 CBF：通常也在 **30 秒以内**。

你可以选择 Bitcoin Safe 连接多少个对等节点。更多对等节点会提高冗余，但通常也会增加带宽和同步时间。默认是 **2** 个对等节点。

### 未确认交易

CBF 只覆盖 **已确认区块**。如果你也想收到未确认入账提醒，请保持 [即时交易通知]({{< ref "knowledge/instant-transactions-notifications/" >}}) 开启，这是默认设置。

### 技术说明

紧凑区块过滤器定义于 [BIP158](https://bips.dev/158/)。Bitcoin Safe 使用开源的 [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto)。

你也可以在 _Bitcoin network monitoring_ 设置中把自己的 Bitcoin Core 节点作为初始对等节点。

![初始节点设置](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
