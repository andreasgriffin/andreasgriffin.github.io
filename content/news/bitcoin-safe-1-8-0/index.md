---
aliases:
  - "/news/bitcoin-safe-1-8-0/"
title: "Bitcoin Safe 1.8.0"
date: "2026-03-31"
description: "Release notes for Bitcoin Safe 1.8.0, including chart zooming, custom nLocktime, app lock mode, and smoother updates."
videos:
  - "https://www.youtube.com/watch?v=S0O40-p_w0M"
---

## New features

#### Balance chart zooming

Added zooming for the balance chart ([#492](https://github.com/andreasgriffin/bitcoin-safe/pull/492)).

{{< video src="zoom.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 balance chart zooming" description="Preview of zooming support for the balance chart in Bitcoin Safe 1.8.0." >}}

#### Custom nLocktime

Added support for custom nLocktime, which lets you set the earliest block height or time when a transaction can be confirmed ([#481](https://github.com/andreasgriffin/bitcoin-safe/pull/481)).

{{< video src="nLocktime.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 custom nLocktime" description="Preview of custom nLocktime support in Bitcoin Safe 1.8.0." >}}

#### Bluetooth support for Jade

Added Bluetooth support for Jade ([#517](https://github.com/andreasgriffin/bitcoin-safe/pull/517)).

{{< video src="bluetooth.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 Jade Bluetooth support" description="Preview of Bluetooth support for Jade in Bitcoin Safe 1.8.0." >}}

#### App lock mode

Added app lock mode, a way to lock the app while it continues running in the background ([#519](https://github.com/andreasgriffin/bitcoin-safe/pull/519)).

{{< video src="app-lock.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 app lock mode" description="Preview of app lock mode in Bitcoin Safe 1.8.0." >}}

Also included seamless update functionality on Windows and easier updates on macOS and Linux ([#513](https://github.com/andreasgriffin/bitcoin-safe/pull/513)).

## Improvements

- Notifications history is now available from the tray icon ([#493](https://github.com/andreasgriffin/bitcoin-safe/pull/493))
- Bug fixes and small UI improvements

## Contributions

- [@bsn21m](https://github.com/bsn21m) made their first contribution in [#538](https://github.com/andreasgriffin/bitcoin-safe/pull/538)
- Thanks to the [bdk](https://github.com/bitcoindevkit/) team and [@rustaceanrob](https://github.com/rustaceanrob)
- Huge thanks to [@design-rrr](https://github.com/design-rrr) for design and UX support
