---
title: "Компактні блокові фільтри"
description: "Зрозумійте, що таке компактні блокові фільтри і як вони покращують приватність порівняно з серверами Electrum."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "компактні блокові фільтри"
  - "CBF"
  - "приватність"
  - "Bitcoin-гаманець"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**Компактні блокові фільтри (CBF)** дозволяють [Bitcoin Safe]({{< ref "/" >}}) сканувати блокчейн, не питаючи сервер Electrum, які адреси належать вам.

![Bitcoin Safe завантажує компактні блокові фільтри від кількох випадкових peer'ів Bitcoin Core.](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

Замість запиту до центрального сервера Bitcoin Safe завантажує маленький фільтр для кожного блоку від випадкових peer'ів Bitcoin Core. Ваш гаманець перевіряє їх локально і завантажує повні блоки лише за потреби.

### CBF проти Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">Параметр</th>
        <th scope="col">Компактні блокові фільтри</th>
        <th scope="col">Сервер Electrum</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Приватність</th>
        <td><span class="text-success fw-semibold">Добре</span> - Дані гаманця залишаються локально</td>
        <td><span class="text-danger fw-semibold">Погано</span> - Сервер може бачити ваші адреси та історію</td>
      </tr>
      <tr>
        <th scope="row">Джерело даних</th>
        <td><span class="text-success fw-semibold">Добре</span> - Випадкові peer'и Bitcoin Core</td>
        <td><span class="text-warning fw-semibold">Нейтрально</span> - Один вибраний сервер</td>
      </tr>
      <tr>
        <th scope="row">Початкова синхронізація</th>
        <td><span class="text-warning fw-semibold">Нейтрально</span> - Зазвичай повільніше</td>
        <td><span class="text-success fw-semibold">Добре</span> - Зазвичай швидше</td>
      </tr>
      <tr>
        <th scope="row">Постійна синхронізація</th>
        <td><span class="text-success fw-semibold">Добре</span> - Дуже швидко після першої синхронізації</td>
        <td><span class="text-success fw-semibold">Добре</span> - Зазвичай швидко</td>
      </tr>
      <tr>
        <th scope="row">Найкраще для</th>
        <td><span class="text-success fw-semibold">Добре</span> - Користувачів, яким важлива приватність</td>
        <td><span class="text-success fw-semibold">Добре</span> - Найшвидшого налаштування та відновлення</td>
      </tr>
    </tbody>
  </table>
</div>

### Навіщо використовувати CBF

- Більше приватності: ваш гаманець ніколи не питає сервер про ваші адреси.
- Без довіреного індексатора: Bitcoin Safe напряму спілкується з мережею Bitcoin.
- Легка синхронізація: фільтри маленькі, тому весь блокчейн не потрібен.

### Чого очікувати

- Новий гаманець або відновлення: зазвичай **5-30 хвилин** для першої синхронізації.
- Вже синхронізований гаманець: зазвичай наздоганяє **дуже швидко**, часто **менш ніж за 30 секунд**.
- Перехід з Electrum на CBF: зазвичай теж **менш ніж за 30 секунд**.

Ви можете вибрати, з якою кількістю peer'ів підключається Bitcoin Safe. Більше peer'ів підвищують надійність, але зазвичай збільшують витрати трафіку і час синхронізації. Значення за замовчуванням - **2** peer'и.

### Непідтверджені транзакції

CBF покриває лише **підтверджені блоки**. Щоб також отримувати сповіщення про непідтверджені вхідні платежі, залишайте [Instant transaction notifications]({{< ref "knowledge/instant-transactions-notifications/" >}}) увімкненими, це налаштування за замовчуванням.

### Технічна примітка

Компактні блокові фільтри визначені в [BIP158](https://bips.dev/158/). Bitcoin Safe використовує відкритий модуль [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto).

Ви також можете використовувати власний вузол Bitcoin Core як початковий peer у налаштуваннях _Bitcoin network monitoring_.

![Налаштування початкового вузла](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
