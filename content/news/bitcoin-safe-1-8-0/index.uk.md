---
title: "Bitcoin Safe 1.8.0"
date: "2026-03-31"
description: "Нотатки до релізу Bitcoin Safe 1.8.0, включно з масштабуванням графіка балансу, користувацьким nLocktime, режимом блокування застосунку та простішими оновленнями."
videos:
  - "https://www.youtube.com/watch?v=S0O40-p_w0M"
---

## Нові функції

#### Масштабування графіка балансу

Додано масштабування графіка балансу ([#492](https://github.com/andreasgriffin/bitcoin-safe/pull/492)).

{{< video src="zoom.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 масштабування графіка балансу" description="Попередній перегляд масштабування графіка балансу в Bitcoin Safe 1.8.0." >}}

#### Користувацький nLocktime

Додано підтримку користувацького nLocktime, що дає змогу задати найранішу висоту блоку або час, коли транзакцію можна підтвердити ([#481](https://github.com/andreasgriffin/bitcoin-safe/pull/481)).

{{< video src="nLocktime.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 користувацький nLocktime" description="Попередній перегляд підтримки користувацького nLocktime в Bitcoin Safe 1.8.0." >}}

#### Підтримка Bluetooth для Jade

Додано підтримку Bluetooth для Jade ([#517](https://github.com/andreasgriffin/bitcoin-safe/pull/517)).

{{< video src="bluetooth.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 підтримка Bluetooth для Jade" description="Попередній перегляд підтримки Bluetooth для Jade в Bitcoin Safe 1.8.0." >}}

#### Режим блокування застосунку

Додано режим блокування застосунку, тобто спосіб заблокувати застосунок, поки він продовжує працювати у фоновому режимі ([#519](https://github.com/andreasgriffin/bitcoin-safe/pull/519)).

{{< video src="app-lock.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 режим блокування застосунку" description="Попередній перегляд режиму блокування застосунку в Bitcoin Safe 1.8.0." >}}

Також додано функцію безшовного оновлення у Windows і простіші оновлення у macOS та Linux ([#513](https://github.com/andreasgriffin/bitcoin-safe/pull/513)).

## Покращення

- Історія сповіщень тепер доступна з іконки в треї ([#493](https://github.com/andreasgriffin/bitcoin-safe/pull/493))
- Виправлення помилок і невеликі покращення інтерфейсу

## Внесок

- [@bsn21m](https://github.com/bsn21m) зробив свій перший внесок у [#538](https://github.com/andreasgriffin/bitcoin-safe/pull/538)
- Дякуємо команді [bdk](https://github.com/bitcoindevkit/) і [@rustaceanrob](https://github.com/rustaceanrob)
- Велика подяка [@design-rrr](https://github.com/design-rrr) за підтримку дизайну та UX
