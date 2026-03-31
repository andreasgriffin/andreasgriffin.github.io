---
title: "Bitcoin Safe 1.8.0"
date: "2026-03-31"
description: "Примечания к выпуску Bitcoin Safe 1.8.0, включая масштабирование графика баланса, пользовательский nLocktime, режим блокировки приложения и более простые обновления."
videos:
  - "https://www.youtube.com/watch?v=S0O40-p_w0M"
---

## Новые функции

#### Масштабирование графика баланса

Добавлено масштабирование графика баланса ([#492](https://github.com/andreasgriffin/bitcoin-safe/pull/492)).

{{< video src="zoom.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 масштабирование графика баланса" description="Предпросмотр масштабирования графика баланса в Bitcoin Safe 1.8.0." >}}

#### Пользовательский nLocktime

Добавлена поддержка пользовательского nLocktime, позволяющая задать минимальную высоту блока или время, когда транзакция может быть подтверждена ([#481](https://github.com/andreasgriffin/bitcoin-safe/pull/481)).

{{< video src="nLocktime.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 пользовательский nLocktime" description="Предпросмотр поддержки пользовательского nLocktime в Bitcoin Safe 1.8.0." >}}

#### Поддержка Bluetooth для Jade

Добавлена поддержка Bluetooth для Jade ([#517](https://github.com/andreasgriffin/bitcoin-safe/pull/517)).

{{< video src="bluetooth.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 поддержка Bluetooth для Jade" description="Предпросмотр поддержки Bluetooth для Jade в Bitcoin Safe 1.8.0." >}}

#### Режим блокировки приложения

Добавлен режим блокировки приложения, то есть способ заблокировать приложение, пока оно продолжает работать в фоновом режиме ([#519](https://github.com/andreasgriffin/bitcoin-safe/pull/519)).

{{< video src="app-lock.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 режим блокировки приложения" description="Предпросмотр режима блокировки приложения в Bitcoin Safe 1.8.0." >}}

Также включена функция бесшовного обновления в Windows и более простые обновления в macOS и Linux ([#513](https://github.com/andreasgriffin/bitcoin-safe/pull/513)).

## Улучшения

- История уведомлений теперь доступна из значка в системном трее ([#493](https://github.com/andreasgriffin/bitcoin-safe/pull/493))
- Исправления ошибок и небольшие улучшения интерфейса

## Вклад

- [@bsn21m](https://github.com/bsn21m) сделал свой первый вклад в [#538](https://github.com/andreasgriffin/bitcoin-safe/pull/538)
- Спасибо команде [bdk](https://github.com/bitcoindevkit/) и [@rustaceanrob](https://github.com/rustaceanrob)
- Огромное спасибо [@design-rrr](https://github.com/design-rrr) за поддержку в дизайне и UX
