---
aliases:
- /zh/knowledge/supported-hardware-signers/metrovault/
title: MetroVault
signer: metrovault
bucket: knowledge
---

MetroVault 可以把一台旧的 Android 设备变成专门给 Bitcoin Safe 使用的离线 Bitcoin 签名设备。不要把它安装在你的日常手机上。请先重置设备，让它保持**离线**并与互联网断开连接，而且只把它用于签名。

## 你需要预期什么

- 在安装之前先重置一台旧的 Android 设备，并且只把它当作签名设备使用。
- 不要安装其他应用，不要登录任何账户，不要插入 SIM 卡，也不要再把设备连回互联网。
- 通过二维码与 Bitcoin Safe 交换钱包数据、描述符和 PSBT。
- 为 Bitcoin Safe 注册多签描述符并导出签名设备数据。
- 在签名之前先在 MetroVault 屏幕上核对所有细节。

## 重置 Android 设备，并且只把它当作离线签名器使用

MetroVault 的上游文档现在提供了一份完整的[设备设置指南](https://github.com/gorunjinian/MetroVault/blob/main/docs/DEVICE_SETUP.md)。我们强烈建议你逐步照着做，并把它当作硬性要求：使用一台专用、恢复出厂设置后的**离线手机**，在设置完成后继续与互联网断开连接，而且只用于签名。

1. 在安装之前先把手机恢复出厂设置。
2. 跳过 Google 账户设置，并让设备保持离线。
3. 永久保持飞行模式开启。
4. 关闭 Wi-Fi、Bluetooth、NFC 和移动数据。
5. 取出 SIM 卡。
6. 关闭 USB 调试。
7. 不要安装其他应用，也不要把手机用于签名之外的任何用途。

用于生产环境时，请尽可能从源码构建。如果你无法让设备保持离线并且只用于签名，就不要用它来保护 MetroVault 的生产资金。
