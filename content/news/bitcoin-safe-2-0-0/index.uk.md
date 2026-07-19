---
title: "Bitcoin-Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "Нотатки до випуску Bitcoin-Safe 2.0.0: оновлений майстер налаштування, приватна синхронізація через Compact Block Filters і ширша підтримка апаратних гаманців."
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">Оголошення про випуск</p>
    <h2 class="display-6 mb-3">Bitcoin-Safe 2.0 - покрокове налаштування гаманця, приватна синхронізація ланцюга і підписання з фокусом на пристрої</h2>
    <p class="lead mb-4">Цей випуск приносить повністю перебудований майстер налаштування, приватну синхронізацію ланцюга за допомогою Compact Block Filters і процес підписання, організований навколо кожного апаратного пристрою. Якщо вам було цікаво спробувати cold storage, але ви не були впевнені, це саме той випуск, який варто протестувати.</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Завантажити Bitcoin-Safe 2.0</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">Подивитися, що нового</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Покрокове налаштування гаманця</h2>
          <p class="mb-0">Новий майстер пояснює кожен крок, зменшує неоднозначність і допомагає новим користувачам вибрати правильний шлях, не втрачаючи переваг multisig.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Приватна синхронізація гаманця</h2>
          <p class="mb-0">Нові гаманці тепер синхронізуються через Compact Block Filters одразу, тож ви можете приватно сканувати ланцюг без залежності від стороннього Electrum indexer.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Підписання з фокусом на пристрої</h2>
          <p class="mb-0">Тепер процеси підписання залишаються зосередженими на пристрої перед вами, а наступні кроки для QR, USB, Bluetooth, файлів і координації multisig стали зрозумілішими.</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## Керований шлях до self-custody {#setup-flow}

Досвід першого запуску було повністю перебудовано. Bitcoin-Safe і надалі орієнтується на серйозну self-custody, включно з hardware-backed multisig, а версія 2.0 тепер дає новим користувачам зрозумілий шлях через це налаштування. Новий майстер пояснює, що відбувається, де ви перебуваєте в процесі та що потрібно від кожного signer перед переходом далі.

<p class="small text-muted">Деталі реалізації дивіться в <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a>.</p>

Основні моменти редизайну:

- Новий екран привітання, який допомагає тим, хто запускає застосунок уперше, вибрати правильну відправну точку
- Покроковий індикатор прогресу під час створення гаманця
- Екрани підписання для конкретних пристроїв із чіткими інструкціями та контекстною допомогою
- Recovery PDF з назвами та іконками пристроїв, щоб резервні копії залишалися однозначними

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## Приватна і надійна синхронізація ланцюга з Compact Block Filters {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) тепер забезпечують синхронізацію нових гаманців у Bitcoin-Safe 2.0. Замість того щоб питати Electrum server, які адреси належать вам, Bitcoin-Safe тепер може приватно сканувати ланцюг, завантажуючи compact filters від випадкових Bitcoin Core peers і перевіряючи їх локально.

<p class="small text-muted">Деталі реалізації дивіться в <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a>.</p>


- Синхронізація гаманця залишається приватною з першого запуску
- Немає залежності від сторонніх Electrum servers
- Electrum і далі доступний для тих, хто його віддає перевагу
- [Миттєва синхронізація після початкового сканування гаманця]({{< ref "library/compact-block-filters" >}})
- [Миттєві сповіщення про ретрансльовані транзакції]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## Процес підписання, зосереджений на пристрої, для кожного пристрою {#device-focused-signing}

Редизайн також змінює процес підписання після створення гаманця. Замість одного загального екрана для всіх signer'ів, Bitcoin-Safe тепер вибудовує дії навколо конкретного пристрою, який ви використовуєте.

<p class="small text-muted">Деталі реалізації дивіться в <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a>.</p>

- Дії для QR, USB, Bluetooth, експорту/імпорту файлів і Sync & Chat відображаються прямо на картці активного signer'а
- Signer'и, що залишилися, пристрої, які вже підписали, та наступний потрібний крок видно з першого погляду
- Multisig-процеси зі змішаними пристроями залишаються читабельними, тому що ідентичність signer'а видно протягом усього PSBT
- Складні транзакції зі змішаними single-sig і multisig входами обробляються коректно, тож кожен крок підписання залишається зрозумілим

![Картка signer'а з діями для QR, USB, Bluetooth, експорту файлів і Chat & Sync](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Архітектура плагінів для бізнес-процесів і power users

Bitcoin-Safe 2.0 також закладає основу для майбутніх додаткових плагінів, орієнтованих на Bitcoin-бізнес і power users. Тож стежте за тим, що з'явиться далі :-)

<p class="small text-muted">Деталі реалізації дивіться в <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a>.</p>

- Поширення плагінів через зовнішній репозиторій *sources*
- Кожен плагін *підписаний GPG* від [andreasgriffin]({{< gpg_key_link >}}), щоб гарантувати безпеку, цілісність і доставку плагінів
- Окреме версіонування плагінів і оновлення дають змогу розвивати їх швидше та незалежно

![Картка signer'а з діями для QR, USB, Bluetooth, експорту файлів і Chat & Sync](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Ширша підтримка пристроїв і полірування {#hardware-support}

- Анімовані QR-коди стали на **30%** швидшими для швидшого сканування
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) тепер підтримується через USB
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) тепер підтримує **Bluetooth** на додачу до USB і QR
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) та [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) додані до списку підтримуваних пристроїв
- Перегляньте [повний список підтримуваних пристроїв]({{< ref "library/supported-hardware-signers" >}})
- Додано автоматичні перевірки [відтворюваності]({{< ref "library/reproducibility-and-security" >}})
- Тут можна переглянути [повний список](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0) покращень


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## Попередні сильні сторони нікуди не зникли

Реліз 2.0 не є перезапуском з нуля. Під новим onboarding і процесом підписання Bitcoin-Safe зберігає ті функції, які робили його корисним щодня: collaborative multisig, PDF-резервні копії, історію гаманця з пошуком, візуалізацію руху коштів, label sync та багато іншого.

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">Готові спробувати Bitcoin-Safe 2.0?</h2>
  <p class="mb-3">Завантажте останній реліз і самі дослідіть новий onboarding, приватну синхронізацію та покращення для апаратних гаманців.</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Завантажити Bitcoin-Safe</a>
</div>


<br><br>

## Дякуємо

Цей випуск спирається на велику працю контриб'юторів, тестувальників і [підтримувачів усього проєкту]({{< ref "donate" >}}):

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r)) за редизайн майстра, роботу над UI плагінів і **неймовірну та невтомну** UI/UX підтримку
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) за Compact Block Filter client, який тепер забезпечує приватну синхронізацію нових гаманців
- Команді [Bitcoin Dev Kit](https://github.com/bitcoindevkit/) за бібліотеки в основі Bitcoin-Safe
- Команді [ndk](https://github.com/nostr-dev-kit/ndk) за бібліотеки, які забезпечують функціональність nostr
- Усім у спільноті Bitcoin-Safe, хто тестував release candidate, повідомляв про баги, перекладав сторінки, надсилав sats і рухав проєкт уперед
- [Перекладачі]({{< ref "donate/#translators" >}}), зокрема <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (В'єтнамська)" title="qdyg-vn 🇻🇳 (В'єтнамська)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (Німецька)" title="bsn21m 🇩🇪 (Німецька)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (Іспанська)" title="cyphra 🇪🇸 (Іспанська)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (Китайська)" title="DaGrindDontStop 🇨🇳 (Китайська)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


Якщо ви хочете допомогти профінансувати наступний реліз, ви також можете зробити пожертву тут: {{< donation_btc >}}
