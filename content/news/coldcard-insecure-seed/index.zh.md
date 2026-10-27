---
title: "不安全的 COLDCARD Seed"
date: "2026-08-02"
draft: false
description: "Coinkite 已披露受影响 COLDCARD firmware 中 seed 生成的严重弱点。如果您在任何受影响的 Coinkite 设备上创建了 seed，请将资金迁移到新的 seed。"
images: ["COLDCARD Security Advisory Notice - Migrate ASAP.png"]
---

## 摘要

[Coinkite 已披露受影响 COLDCARD firmware 中 seed 生成的严重弱点](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/)。[Block 的技术分析](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware)确认原因是使用了可预测的软件随机数生成器，而非设备的硬件 RNG，并警告**攻击正在进行中**。更新 firmware **无法**修复已有的 seed。

**如果您在任何受影响的 Coinkite 设备上创建了 seed，请将资金迁移到新的 seed。**

## 我的设备受影响吗？

是否受影响取决于**生成 seed 时安装的 firmware 版本**，而不是设备的制造时间。

| 设备 | 用于生成 seed 的 firmware | 状态 |
|---|---|---|
| Mk1 | 所有已发布的 firmware | 不受影响 |
| Mk2 / Mk3 | v3.2.2 或更早 | 不受影响（使用硬件 RNG） |
| Mk2 / Mk3 | v4.0.0 – v4.1.9 | **易受攻击** — 无安全 reseed |
| Mk4 | 生产版 v5.0.0 及之后 | **易受攻击** — 熵限制在约 72 位 |
| Q | 所有生产版 firmware | **易受攻击** — 熵限制在约 72 位 |
| Mk5 | 所有生产版 firmware | **易受攻击** — 熵限制在约 72 位 |
| TAPSIGNER、OPENDIME、SATSCARD | — | 不受影响（不同的代码库） |

请注意，导出不安全的 seed 并导入另一个钱包**不会**修复它——seed 本身仍然受影响。

## 在生成新 seed 之前安装修复后的 firmware

所有受影响的型号和发布通道现在都有修复后的 firmware。在安装完成之前，不要在 COLDCARD 上生成新的 seed。

| 设备 | 修复后的 firmware |
|---|---|
| Mk2 / Mk3 | 4.2.0 或更高 |
| Mk4 / Mk5（standard） | 5.6.0 或更高 |
| Q（standard） | 1.5.0Q 或更高 |
| Mk4 / Mk5（Edge） | 6.6.0X 或更高 |
| Q（Edge） | 6.6.0QX 或更高 |

Standard 和 Edge 是独立的发布通道。如果您使用 Edge，请为您的型号安装修复后的 Edge 版本——不要因为版本号高于 standard 版本就认为旧版 Edge 6.x 已修复。

## 掷骰子或口令短语能保护我吗？

- **掷骰子：** 该缺陷只影响设备生成的熵。如果您在创建 seed 时输入了至少 **50 次独立、私密的骰子投掷**（99 次或更多可获得约 256 位熵），仅骰子输入就贡献了至少 128 位的独立熵，该 seed 不会因为这一个问题而被视为有风险。如果少于 50 次——或者您不确定输入了多少次或是否私密——请**迁移**。
- **BIP-39 口令短语：** 一个强且唯一的 BIP-39 口令短语（不是 COLDCARD PIN）增加了独立的防护，但**无法**修复受影响的 seed。如果您的口令短语短、常见、重复使用或容易被猜出——或者您不确定其强度——请将资金视为有风险并立即迁移。即使使用强口令短语，也应尽快迁移到新生成的 seed。

## 迁移清单

请冷静、谨慎地迁移。仓促进行钱包迁移可能比您要解决的问题带来更直接的风险。

1. 在生成替代 seed 之前，**安装修复后的 firmware**。如果您愿意，可以在**非 COLDCARD 签名设备**上生成新 seed（[查看支持的设备]({{< ref "library/supported-hardware-signers" >}}））——无论如何，**不要**重复使用旧 seed。
2. 生成一个全新的 seed 并**记录下来**。在存入任何资金之前，验证书面备份、钱包指纹和收款地址。
3. 使用 Bitcoin-Safe 的设置向导，用新 seed 创建新的[单签名钱包]({{< ref "library/setup-singlesig-wallet" >}})或[多签名钱包]({{< ref "library/setup-multisig-wallet" >}}）。
4. 完成向导的收款与发送测试：在新的签名设备上验证备份和收款地址，接收一笔小额测试资金，并将其成功发送到新钱包中另一个已验证的地址。
5. 签署并广播迁移交易：
   - **单签名钱包：** 正常广播，并设置较高的手续费以便快速确认。
   - **多签名钱包：** 不要正常广播，因为这会将其公钥暴露在公开内存池中。复制已签署的原始交易，并通过 [MARA Slipstream](https://slipstream.mara.com/) 直接提交。
6. 在**全部余额**到达新钱包并确认之前，保留旧的 COLDCARD 及其备份。之后才擦除旧 seed。

如果 Mk2/Mk3 是您唯一的签名设备，请先安装 firmware 4.2.0 或更高版本：它能正确生成替代 seed，因此您无需更新的 COLDCARD 即可完成迁移。按照相同的步骤，在单台设备上小心地在旧 seed 和新 seed 之间切换，并在迁移完全确认之前保留旧备份。

## 如果您使用多签名

如果多签名配置**完全**由受影响的设备组成，则漏洞仍然适用。请使用包含至少一个不受影响签名设备的法定人数来保护配置。

## 帮助他人迁移

切勿要求他们分享、拍照或输入 seed 助记词。seed 必须保持私密，并且只能在签名设备本身上输入。
