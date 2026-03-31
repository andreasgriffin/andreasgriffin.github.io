---
title: "Bitcoin Safe 1.8.0"
date: "2026-03-31"
description: "Bitcoin Safe 1.8.0 发行说明，包括余额图表缩放、自定义 nLocktime、应用锁定模式以及更简便的更新。"
videos:
  - "https://www.youtube.com/watch?v=S0O40-p_w0M"
---

## 新功能

#### 余额图表缩放

新增余额图表缩放功能 ([#492](https://github.com/andreasgriffin/bitcoin-safe/pull/492))。

{{< video src="zoom.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 余额图表缩放" description="Bitcoin Safe 1.8.0 中余额图表缩放功能的预览。" >}}

#### 自定义 nLocktime

新增自定义 nLocktime 支持，可让你设置交易最早可以被确认的区块高度或时间 ([#481](https://github.com/andreasgriffin/bitcoin-safe/pull/481))。

{{< video src="nLocktime.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 自定义 nLocktime" description="Bitcoin Safe 1.8.0 中自定义 nLocktime 的预览。" >}}

#### Jade 的 Bluetooth 支持

新增对 Jade 的 Bluetooth 支持 ([#517](https://github.com/andreasgriffin/bitcoin-safe/pull/517))。

{{< video src="bluetooth.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 Jade 的 Bluetooth 支持" description="Bitcoin Safe 1.8.0 中 Jade Bluetooth 支持的预览。" >}}

#### 应用锁定模式

新增应用锁定模式，这是一种在应用继续于后台运行时将其锁定的方式 ([#519](https://github.com/andreasgriffin/bitcoin-safe/pull/519))。

{{< video src="app-lock.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 应用锁定模式" description="Bitcoin Safe 1.8.0 中应用锁定模式的预览。" >}}

此外还包括 Windows 上的无缝更新功能，以及 macOS 和 Linux 上更简便的更新 ([#513](https://github.com/andreasgriffin/bitcoin-safe/pull/513))。

## 改进

- 现在可以从托盘图标查看通知历史记录 ([#493](https://github.com/andreasgriffin/bitcoin-safe/pull/493))
- 错误修复和小型界面改进

## 贡献

- [@bsn21m](https://github.com/bsn21m) 在 [#538](https://github.com/andreasgriffin/bitcoin-safe/pull/538) 中完成了首次贡献
- 感谢 [bdk](https://github.com/bitcoindevkit/) 团队以及 [@rustaceanrob](https://github.com/rustaceanrob)
- 特别感谢 [@design-rrr](https://github.com/design-rrr) 在设计和 UX 方面提供的支持
