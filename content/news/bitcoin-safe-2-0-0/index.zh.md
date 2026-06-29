---
title: "Bitcoin Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "Bitcoin Safe 2.0.0 发布说明，包括重建的设置向导、基于 Compact Block Filters 的私密同步，以及更广泛的硬件钱包支持。"
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">发布公告</p>
    <h2 class="display-6 mb-3">Bitcoin Safe 2.0 - 引导式钱包设置、私密链同步，以及以设备为中心的签名流程</h2>
    <p class="lead mb-4">这个版本带来了重新打造的设置向导、使用 Compact Block Filters 的私密链同步，以及围绕每个硬件设备组织的签名流程。如果你一直对 cold storage 感兴趣，但还没有足够把握，这就是值得尝试的版本。</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">下载 Bitcoin Safe 2.0</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">查看新内容</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">逐步式钱包设置</h2>
          <p class="mb-0">新的向导会解释每一步，减少含糊不清的地方，并帮助新用户在不失去 multisig 强大能力的前提下选择正确的路径。</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">私密钱包同步</h2>
          <p class="mb-0">新钱包现在默认使用 Compact Block Filters 进行同步，因此你可以私密地扫描链，而不必依赖第三方 Electrum indexer。</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">以设备为中心的签名</h2>
          <p class="mb-0">签名流程现在始终围绕你面前的设备展开，并且为 QR、USB、Bluetooth、文件和 multisig 协调提供更清晰的下一步提示。</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## 通往 self-custody 的引导路径 {#setup-flow}

首次使用体验已经从头重建。Bitcoin Safe 依然面向严肃的 self-custody，包括基于硬件的 multisig，而 2.0 现在为新用户提供了一个经过引导的设置路径。新的向导会说明当前发生了什么、你在流程中的位置，以及在继续之前每个 signer 需要你完成什么。

<p class="small text-muted">实现细节请参见 <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a>。</p>

这次重设计的亮点：

- 全新的欢迎界面，帮助首次使用者选择正确的起点
- 创建钱包过程中的逐步进度流程
- 面向具体设备的签名界面，提供聚焦的说明和上下文帮助
- 带有设备名称和图标的恢复 PDF，让备份保持清晰且不混淆

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## 借助 Compact Block Filters 实现私密且稳健的链同步 {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) 现在为 Bitcoin Safe 2.0 中的新钱包提供同步能力。Bitcoin Safe 不再需要向 Electrum server 询问哪些地址属于你，而是可以从随机的 Bitcoin Core peers 下载 compact filters 并在本地检查，从而私密地扫描整条链。

<p class="small text-muted">实现细节请参见 <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a>。</p>


- 钱包同步从第一次启动开始就是私密的
- 不依赖第三方 Electrum servers
- 对于更喜欢它的用户，Electrum 仍然可用
- [首次钱包扫描之后即可实现即时同步]({{< ref "library/compact-block-filters" >}})
- [被中继交易的即时通知]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## 面向每种设备的设备中心签名流程 {#device-focused-signing}

这次重设计也重塑了钱包创建之后的签名流程。Bitcoin Safe 不再为所有 signer 提供同一个通用页面，而是把操作聚焦在你当前正在使用的具体设备上。

<p class="small text-muted">实现细节请参见 <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a>。</p>

- QR、USB、Bluetooth、文件导出/导入，以及 Sync & Chat 操作会直接显示在当前 active signer card 上
- 剩余的 signers、已经签过名的设备，以及下一步所需操作都能一眼看到
- 混合设备的 multisig 流程依然清晰，因为 signer identity 会在整个 PSBT 过程中持续可见
- 混合了 single-sig 和 multisig 输入的复杂交易也能被正确处理，因此每一步签名都足够明确

![显示 QR、USB、Bluetooth、文件导出和 Chat & Sync 设备专属操作的 signer 卡片](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## 面向业务流程和 power users 的插件架构

Bitcoin Safe 2.0 还为未来面向 Bitcoin 企业和 power users 的更多插件打下了基础。所以也欢迎继续关注接下来会推出什么 :-)

<p class="small text-muted">实现细节请参见 <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a>。</p>

- 通过外部 *sources* 仓库分发插件
- 每个插件都由 [andreasgriffin]({{< gpg_key_link >}}) 进行 *GPG 签名*，以确保插件的安全性、完整性和分发可信度
- 独立的插件版本管理和更新机制，使插件开发更快也更独立

![显示 QR、USB、Bluetooth、文件导出和 Chat & Sync 设备专属操作的 signer 卡片](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## 更广泛的设备支持与更多打磨 {#hardware-support}

- 动画 QR 码速度提升 **30%**，扫描更快
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) 现在支持通过 USB 使用
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) 现在除了 USB 和 QR 之外，也支持 **Bluetooth**
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) 和 [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) 已加入支持设备列表
- 查看[完整支持设备列表]({{< ref "library/supported-hardware-signers" >}})
- 已添加针对 [reproducibility]({{< ref "library/reproducibility-and-security" >}}) 的自动检查
- 在这里查看改进的[完整列表](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0)


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## 原有优势依然都在

2.0 不是一次推倒重来。新的 onboarding 和签名流程之下，Bitcoin Safe 依然保留了那些让它在日常使用中非常实用的功能：协作式 multisig、PDF 备份、可搜索的钱包历史、资金流可视化、label sync，等等。

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">准备好试试 Bitcoin Safe 2.0 了吗？</h2>
  <p class="mb-3">下载最新版本，亲自体验新的 onboarding、私密同步，以及硬件钱包方面的改进。</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">下载 Bitcoin Safe</a>
</div>


<br><br>

## 致谢

这次发布建立在贡献者、测试者，以及[整个项目的支持者]({{< ref "donate" >}})的大量工作之上：

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r))，感谢你完成向导重设计、插件 UI 工作，以及**出色且不知疲倦的** UI/UX 支持
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/))，感谢你开发了 Compact Block Filter client，它现在驱动着新钱包的私密同步
- 感谢 [Bitcoin Dev Kit 团队](https://github.com/bitcoindevkit/) 提供 Bitcoin Safe 核心所依赖的库
- 感谢 [ndk 团队](https://github.com/nostr-dev-kit/ndk) 提供支持 nostr 功能的库
- 感谢 Bitcoin Safe 社区中的每一个人，你们测试了 release candidates、报告了 bug、翻译了页面、发送了 sats，并持续推动项目向前
- [翻译者]({{< ref "donate/#translators" >}})，包括 <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (越南语)" title="qdyg-vn 🇻🇳 (越南语)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (德语)" title="bsn21m 🇩🇪 (德语)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (西班牙语)" title="cyphra 🇪🇸 (西班牙语)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (中文)" title="DaGrindDontStop 🇨🇳 (中文)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


如果你想帮助资助下一个版本，也可以在这里捐赠: {{< donation_btc >}}
