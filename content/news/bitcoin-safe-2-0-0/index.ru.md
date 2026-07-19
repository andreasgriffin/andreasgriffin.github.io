---
title: "Bitcoin-Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "Заметки о выпуске Bitcoin-Safe 2.0.0: переработанный мастер настройки, приватная синхронизация через Compact Block Filters и расширенная поддержка аппаратных кошельков."
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">Анонс релиза</p>
    <h2 class="display-6 mb-3">Bitcoin-Safe 2.0 - пошаговая настройка кошелька, приватная синхронизация цепочки и подписание с фокусом на устройстве</h2>
    <p class="lead mb-4">Этот релиз приносит полностью переработанный мастер настройки, приватную синхронизацию цепочки с Compact Block Filters и процесс подписи, организованный вокруг каждого аппаратного устройства. Если вам было интересно попробовать cold storage, но вы сомневались, это именно тот релиз, который стоит проверить.</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Скачать Bitcoin-Safe 2.0</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">Посмотреть, что нового</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Пошаговая настройка кошелька</h2>
          <p class="mb-0">Новый мастер объясняет каждый шаг, убирает неоднозначность и помогает новым пользователям выбрать правильный путь, не теряя преимуществ multisig.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Приватная синхронизация кошелька</h2>
          <p class="mb-0">Новые кошельки теперь синхронизируются через Compact Block Filters сразу после создания, так что вы можете сканировать цепочку приватно, не полагаясь на сторонний индексатор Electrum.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Подписание с фокусом на устройстве</h2>
          <p class="mb-0">Теперь процессы подписи сосредоточены на устройстве перед вами, с более понятными следующими шагами для QR, USB, Bluetooth, файлов и координации multisig.</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## Пошаговый путь к самостоятельному хранению {#setup-flow}

Первый запуск был полностью переработан. Bitcoin-Safe по-прежнему нацелен на серьезное самостоятельное хранение, включая multisig с аппаратной защитой, а версия 2.0 теперь дает новым пользователям понятный путь через эту настройку. Новый мастер объясняет, что происходит, где вы находитесь в процессе и что требуется от каждого signer, прежде чем вы перейдете дальше.

<p class="small text-muted">Подробности реализации смотрите в <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a>.</p>

Главные изменения в редизайне:

- Новый экран приветствия помогает новичкам выбрать правильную отправную точку
- Пошаговый индикатор прогресса при создании кошелька
- Экраны подписи для конкретных устройств с понятными инструкциями и контекстной помощью
- PDF для восстановления с именами и иконками устройств, чтобы резервные копии оставались однозначными

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## Приватная и надежная синхронизация цепочки с Compact Block Filters {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) теперь используются для синхронизации новых кошельков в Bitcoin-Safe 2.0. Вместо того чтобы спрашивать у сервера Electrum, какие адреса принадлежат вам, Bitcoin-Safe теперь может приватно сканировать цепочку, загружая компактные фильтры от случайных узлов Bitcoin Core и проверяя их локально.

<p class="small text-muted">Подробности реализации смотрите в <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a>.</p>


- Синхронизация кошелька остается приватной с первого запуска
- Нет зависимости от сторонних серверов Electrum
- Electrum по-прежнему доступен для тех, кто его предпочитает
- [Мгновенная синхронизация после начального сканирования кошелька]({{< ref "library/compact-block-filters" >}})
- [Мгновенные уведомления о ретранслированных транзакциях]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## Процесс подписи с фокусом на устройстве для каждого устройства {#device-focused-signing}

Редизайн также меняет процесс подписи после создания кошелька. Вместо одного общего экрана для всех signer'ов Bitcoin-Safe теперь строит действия вокруг конкретного устройства, которое вы используете.

<p class="small text-muted">Подробности реализации смотрите в <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a>.</p>

- Действия для QR, USB, Bluetooth, экспорта/импорта файлов и Sync & Chat показываются прямо на карточке активного signer'а
- Оставшиеся signer'ы, уже подписавшие устройства и следующий обязательный шаг видны с первого взгляда
- Смешанные multisig-процессы с разными устройствами остаются читаемыми, потому что личность signer'а видна на протяжении всего PSBT
- Сложные транзакции со смесью single-sig и multisig входов обрабатываются корректно, поэтому каждый шаг подписи остается понятным

![Карточка signer'а с действиями для QR, USB, Bluetooth, экспорта файлов и Chat & Sync](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Архитектура плагинов для бизнес-процессов и продвинутых пользователей

Bitcoin-Safe 2.0 также закладывает основу для будущих дополнительных плагинов, ориентированных на Bitcoin-бизнес и продвинутых пользователей. Так что стоит следить за тем, что будет дальше :-)

<p class="small text-muted">Подробности реализации смотрите в <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a>.</p>

- Распространение плагинов через внешний репозиторий *sources*
- Каждый плагин *подписан GPG* от [andreasgriffin]({{< gpg_key_link >}}), чтобы обеспечить безопасность, целостность и доставку плагинов
- Отдельное версионирование и обновления плагинов позволяют развивать их быстрее и независимо

![Карточка signer'а с действиями для QR, USB, Bluetooth, экспорта файлов и Chat & Sync](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Более широкая поддержка устройств и полировка {#hardware-support}

- Анимированные QR-коды стали на **30%** быстрее для более быстрого сканирования
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) теперь поддерживается через USB
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) теперь поддерживает **Bluetooth** наряду с USB и QR
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) и [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) добавлены в список поддерживаемых устройств
- Посмотрите [полный список поддерживаемых устройств]({{< ref "library/supported-hardware-signers" >}})
- Добавлены автоматические проверки [воспроизводимости]({{< ref "library/reproducibility-and-security" >}})
- Здесь можно посмотреть [полный список](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0) улучшений


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## Прежние сильные стороны никуда не делись

Релиз 2.0 не является перезапуском с нуля. Под новым процессом онбординга и подписи Bitcoin-Safe по-прежнему сохраняет функции, которые делали его полезным каждый день: совместный multisig, PDF-резервные копии, поиск по истории кошелька, визуализации движения средств, синхронизацию меток и многое другое.

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">Готовы попробовать Bitcoin-Safe 2.0?</h2>
  <p class="mb-3">Скачайте последнюю версию и сами изучите новый онбординг, приватную синхронизацию и улучшения для аппаратных кошельков.</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Скачать Bitcoin-Safe</a>
</div>


<br><br>

## Спасибо

Этот релиз основан на большой работе участников, тестировщиков и [сторонников проекта]({{< ref "donate" >}}):

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r)) за редизайн мастера, работу над UI плагинов и **потрясающую и неутомимую** поддержку UI/UX
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) за клиент Compact Block Filter, который теперь обеспечивает приватную синхронизацию новых кошельков
- Команде [Bitcoin Dev Kit](https://github.com/bitcoindevkit/) за библиотеки в основе Bitcoin-Safe
- Команде [ndk](https://github.com/nostr-dev-kit/ndk) за библиотеки, которые обеспечивают функциональность nostr
- Всем в сообществе Bitcoin-Safe, кто тестировал release candidate, сообщал об ошибках, переводил страницы, отправлял sats и продолжал двигать проект вперед
- [Переводчики]({{< ref "donate/#translators" >}}), включая <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (Вьетнамский)" title="qdyg-vn 🇻🇳 (Вьетнамский)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (Немецкий)" title="bsn21m 🇩🇪 (Немецкий)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (Испанский)" title="cyphra 🇪🇸 (Испанский)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (Китайский)" title="DaGrindDontStop 🇨🇳 (Китайский)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


Если вы хотите помочь профинансировать следующий релиз, вы также можете пожертвовать здесь: {{< donation_btc >}}
