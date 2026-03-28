---
title: "Kompaktowe filtry bloków"
description: "Dowiedz się, czym są kompaktowe filtry bloków i jak zwiększają prywatność w porównaniu z serwerami Electrum."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "kompaktowe filtry bloków"
  - "CBF"
  - "prywatność"
  - "portfel Bitcoin"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**Kompaktowe filtry bloków (CBF)** pozwalają [Bitcoin Safe]({{< ref "/" >}}) skanować blockchain bez pytania serwera Electrum, które adresy należą do Ciebie.

![Bitcoin Safe pobiera kompaktowe filtry bloków od kilku losowych peerów Bitcoin Core.](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

Zamiast odpytywać centralny serwer, Bitcoin Safe pobiera mały filtr dla każdego bloku od losowych peerów Bitcoin Core. Twój portfel sprawdza je lokalnie i pobiera pełne bloki tylko wtedy, gdy to potrzebne.

### CBF vs Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">Cecha</th>
        <th scope="col">Kompaktowe filtry bloków</th>
        <th scope="col">Serwer Electrum</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Prywatność</th>
        <td><span class="text-success fw-semibold">Dobrze</span> - Dane portfela pozostają lokalne</td>
        <td><span class="text-danger fw-semibold">Źle</span> - Serwer może widzieć Twoje adresy i historię</td>
      </tr>
      <tr>
        <th scope="row">Źródło danych</th>
        <td><span class="text-success fw-semibold">Dobrze</span> - Losowe peery Bitcoin Core</td>
        <td><span class="text-warning fw-semibold">Neutralnie</span> - Jeden wybrany serwer</td>
      </tr>
      <tr>
        <th scope="row">Pierwsza synchronizacja</th>
        <td><span class="text-warning fw-semibold">Neutralnie</span> - Zwykle wolniejsza</td>
        <td><span class="text-success fw-semibold">Dobrze</span> - Zwykle szybsza</td>
      </tr>
      <tr>
        <th scope="row">Ciągła synchronizacja</th>
        <td><span class="text-success fw-semibold">Dobrze</span> - Bardzo szybka po pierwszej synchronizacji</td>
        <td><span class="text-success fw-semibold">Dobrze</span> - Zwykle szybka</td>
      </tr>
      <tr>
        <th scope="row">Najlepsze dla</th>
        <td><span class="text-success fw-semibold">Dobrze</span> - Użytkowników, dla których ważna jest prywatność</td>
        <td><span class="text-success fw-semibold">Dobrze</span> - Najszybszej konfiguracji i odzyskiwania</td>
      </tr>
    </tbody>
  </table>
</div>

### Dlaczego warto używać CBF

- Większa prywatność: portfel nigdy nie pyta serwera o Twoje adresy.
- Bez zaufanego indeksatora: Bitcoin Safe łączy się bezpośrednio z siecią Bitcoin.
- Lekka synchronizacja: filtry są małe, więc nie potrzebujesz całego blockchaina.

### Czego się spodziewać

- Nowy portfel lub odzyskiwanie: zwykle **5 do 30 minut** na pierwszą synchronizację.
- Już zsynchronizowany portfel: zwykle nadrabia **bardzo szybko**, często w **mniej niż 30 sekund**.
- Przejście z Electrum na CBF: zwykle też **mniej niż 30 sekund**.

Możesz wybrać, z iloma peerami łączy się Bitcoin Safe. Więcej peerów zwiększa redundancję, ale zwykle podnosi zużycie łącza i czas synchronizacji. Domyślnie są to **2** peery.

### Niepotwierdzone transakcje

CBF obejmuje tylko **potwierdzone bloki**. Aby również otrzymywać powiadomienia o niepotwierdzonych wpłatach, pozostaw [Instant transaction notifications]({{< ref "knowledge/instant-transactions-notifications/" >}}) włączone. To ustawienie domyślne.

### Uwaga techniczna

Kompaktowe filtry bloków są zdefiniowane w [BIP158](https://bips.dev/158/). Bitcoin Safe korzysta z otwartego modułu [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto).

Możesz też użyć własnego węzła Bitcoin Core jako początkowego peera w ustawieniach _Bitcoin network monitoring_.

![Ustawienie początkowego węzła](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
