---
title: "Компактные фильтры блоков"
description: "Поймите, что такое компактные фильтры блоков и как они повышают приватность по сравнению с серверами Electrum."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "компактные фильтры блоков"
  - "CBF"
  - "приватность"
  - "биткоин-кошелёк"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**Компактные фильтры блоков (CBF)** позволяют [Bitcoin Safe]({{< ref "/" >}}) сканировать блокчейн, не спрашивая у сервера Electrum, какие адреса принадлежат вам.

![Bitcoin Safe загружает компактные фильтры блоков от нескольких случайных пирингов Bitcoin Core.](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

Вместо запроса к центральному серверу Bitcoin Safe загружает маленький фильтр для каждого блока от случайных пирингов Bitcoin Core. Ваш кошелёк проверяет их локально и загружает полные блоки только при необходимости.

### CBF и Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">Параметр</th>
        <th scope="col">Компактные фильтры блоков</th>
        <th scope="col">Сервер Electrum</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Приватность</th>
        <td><span class="text-success fw-semibold">Хорошо</span> - Данные кошелька остаются локально</td>
        <td><span class="text-danger fw-semibold">Плохо</span> - Сервер может видеть ваши адреса и историю</td>
      </tr>
      <tr>
        <th scope="row">Источник данных</th>
        <td><span class="text-success fw-semibold">Хорошо</span> - Случайные пиринги Bitcoin Core</td>
        <td><span class="text-warning fw-semibold">Нейтрально</span> - Один выбранный сервер</td>
      </tr>
      <tr>
        <th scope="row">Первичная синхронизация</th>
        <td><span class="text-warning fw-semibold">Нейтрально</span> - Обычно медленнее</td>
        <td><span class="text-success fw-semibold">Хорошо</span> - Обычно быстрее</td>
      </tr>
      <tr>
        <th scope="row">Постоянная синхронизация</th>
        <td><span class="text-success fw-semibold">Хорошо</span> - Очень быстро после первой синхронизации</td>
        <td><span class="text-success fw-semibold">Хорошо</span> - Обычно быстро</td>
      </tr>
      <tr>
        <th scope="row">Лучше всего для</th>
        <td><span class="text-success fw-semibold">Хорошо</span> - Пользователей, которым важна приватность</td>
        <td><span class="text-success fw-semibold">Хорошо</span> - Самой быстрой настройки и восстановления</td>
      </tr>
    </tbody>
  </table>
</div>

### Зачем использовать CBF

- Больше приватности: ваш кошелёк никогда не спрашивает сервер о ваших адресах.
- Без доверенного индексатора: Bitcoin Safe напрямую общается с сетью Bitcoin.
- Лёгкая синхронизация: фильтры маленькие, поэтому не нужен весь блокчейн.

### Чего ожидать

- Новый кошелёк или восстановление: обычно **5–30 минут** для первой синхронизации.
- Уже синхронизированный кошелёк: обычно догоняет **очень быстро**, часто **менее чем за 30 секунд**.
- Переход с Electrum на CBF: обычно тоже **менее чем за 30 секунд**.

Вы можете выбрать, с каким количеством пирингов подключается Bitcoin Safe. Чем их больше, тем выше надёжность, но обычно больше расходуется трафика и времени на синхронизацию. Значение по умолчанию — **2** пиринга.

### Неподтверждённые транзакции

CBF покрывает только **подтверждённые блоки**. Чтобы также получать уведомления о неподтверждённых входящих платежах, оставьте [Instant transaction notifications]({{< ref "knowledge/instant-transactions-notifications/" >}}) включёнными, это настройка по умолчанию.

### Техническая заметка

Компактные фильтры блоков определены в [BIP158](https://bips.dev/158/). Bitcoin Safe использует открытый модуль [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto).

Вы также можете использовать собственный узел Bitcoin Core как начальный пиринг в настройках _Bitcoin network monitoring_.

![Настройка начального узла](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
