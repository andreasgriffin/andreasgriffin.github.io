---
aliases:
  - "/zh/features/reproducibility-and-security/"
title: "安全性与可复现性"
description: "Bitcoin Safe 遵循高标准的二进制安全实践：可复现构建、已签名提交、已签名发布以及独立的外部监测。"
draft: false
bucket: features
tags: ["Featured", "Security"]
images: ["logo.png"]
keywords: ["reproducible builds", "verify binaries", "signed commits", "signed releases", "appimage", "flatpak", "windows exe", "binary security"]
weight: 18
---

### {{< page-title >}}
{{< page-description >}}
<br>

![Bitcoin Safe 的可复现构建结果](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 500px;" }

我们为网站上的下载完整性实现了多层保护，因此你下载的应用确实能够与公开源代码对应起来：

- **可复现构建**：Linux 的 `deb`、`AppImage`、`Flatpak` 构建，以及 Windows 的 `portable exe` 和 `setup exe`，都可以做到逐字节重现。如果重新构建后的文件完全一致，那就是一个强有力的证据，说明该二进制文件确实来自同一份源代码。
- **已签名的仓库历史**：[Bitcoin Safe 的 GitHub 仓库](https://github.com/andreasgriffin/bitcoin-safe/commits/main) 会发布经过验证的签名提交，因此审查者可以检查进入发布版本的代码是谁编写的。
- **已签名的二进制文件**：发布文件使用 Bitcoin Safe 的[公开 PGP 密钥]({{< gpg_key_link >}})进行签名，Windows 二进制文件还遵循[代码签名策略]({{< ref "code-signing-policy" >}})。
- **独立的可复现性检查**：[WalletScrutiny](https://walletscrutiny.com/desktop/bitcoin.safe/) 会独立跟踪 Bitcoin Safe，并展示桌面版本的可复现验证状态。
- **持续的签名监测**：[BinaryWatch](https://binarywatch.org/) 会定期检查 Bitcoin Safe 的发布文件，以及这些签名是否仍然能对照 Bitcoin Safe 的[公开 PGP 密钥]({{< gpg_key_link >}})通过验证。
- **更新验证**：更新会显示在 Bitcoin Safe 中，其签名也会被自动验证。

综合来看，这些措施让 Bitcoin Safe 成为少数把二进制安全视为用户安全核心组成部分，而不是事后补充项的项目之一。

### 安全性是 Bitcoin Safe 每一个方面的核心考量

除了二进制完整性之外，Bitcoin Safe 还围绕安全默认值、良好的操作实践以及清晰的用户引导来构建。举几个例子：

- **以硬件为核心的托管方式**：Bitcoin Safe 要求使用[硬件签名设备]({{< ref "library/supported-hardware-signers" >}})，这样 seed 就能保留在专用设备上，而不会变成通用电脑中的热秘密。
- **更安全的设置流程**：设置向导帮助用户创建真正适合实际使用的钱包，包括[硬件签名设备]({{< ref "library/supported-hardware-signers" >}})测试、[PDF 备份页]({{< ref "library/pdf-export/" >}})，以及关于如何保存设备和 seed 备份的指导。
- **接收地址验证**：Bitcoin Safe 让你在分享之前，能够直接在签名设备上轻松[验证接收地址]({{< ref "library/verify-receive-address/" >}})。
- **地址投毒检测**：它会对可疑的[相似地址]({{< ref "library/address-poisoning/" >}})发出警告。
- **multisig 安全性**：Bitcoin Safe 支持 multisig 钱包，因此更大的资金可以由多个设备或多人共同保护，而不是依赖单一故障点。
- **让 multisig 更容易使用的协作能力**：Bitcoin Safe 让[multisig 协作]({{< ref "library/collaboration/" >}})变得切实可用，因此在实际使用中协调设置和签名会容易得多。
- **清晰的签名流程**：针对不同设备的签名界面可以减少用户在检查 PSBT 时的困惑，并帮助他们在正确的签名设备上执行正确的操作。
