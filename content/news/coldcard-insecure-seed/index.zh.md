---
title: "不安全的 COLDCARD Seed"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "将资金从 Coinkite 设备生成的 seed 中迁出的简要指南。"
---

[Coinkite 已披露受影响 COLDCARD firmware 中的 seed 生成弱点](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/)。另请参阅 [Block 对可预测 RNG fallback 和 32 位 reseed 的技术分析](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware)。更新 firmware 无法修复已有的 seed。

**如果你的 seed 是用任何 Coinkite 产品创建的，请尽快迁移！**

## 迁移检查清单

1. 在**非 COLDCARD 签名设备**（[查看支持的设备]({{< ref "library/supported-hardware-signers" >}})）上生成一个全新的 seed。不要重复使用旧 seed。然后在 Bitcoin-Safe 设置向导中使用该签名器，创建新的[单签钱包]({{< ref "library/setup-singlesig-wallet" >}})或[多签钱包]({{< ref "library/setup-multisig-wallet" >}})。
   - 如果没有非 COLDCARD 硬件签名器可用，可以在一台专用、已恢复出厂设置、始终保持离线且仅用于签名的 Android 设备上使用 [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}})。
   - 完成向导中的收款和发送测试，以确保新钱包设置正确：核对备份以及新签名器上显示的收款地址，接收一小笔测试金额，然后成功 self-send 到新钱包中另一个已核对的地址。
2. 签署迁移交易：
   - **如果受影响的钱包是单签钱包：** 使用较高的手续费按常规方式广播，以便尽快确认。
   - **如果受影响的钱包是多签钱包：** 不要按常规方式广播，因为这会在公共 mempool 中暴露其公钥。复制已签名的 raw transaction，并通过 [MARA Slipstream](https://slipstream.mara.com/) 直接提交。
3. 保留旧 COLDCARD，直到全部余额到达新钱包并获得确认，然后将其升级到最新 firmware。

如果你在帮助他人迁移，绝不要让对方分享、拍摄或输入 seed words。Seed 必须保持私密，并且只能在签名设备上输入。
