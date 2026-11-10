---
title: "Płatności zaplanowane"
description: "Planuj jednorazowe lub cykliczne płatności Bitcoin, śledź terminy i przygotowuj transakcje do sprawdzenia w Bitcoin-Safe."
draft: false
tags: ["Plugins"]
images: ["schedule.png"]
weight: 40
faq:
  title: "Pytania o płatności zaplanowane"
  items:
    - question: "Czy mogę zaplanować pojedynczą płatność, a nie tylko cykliczne?"
      answer: "Obie opcje są dostępne. Możesz utworzyć płatność jednorazową, płatność z określoną liczbą powtórzeń lub harmonogram bez końca."
    - question: "Jak często harmonogram może się powtarzać?"
      answer: "Dostępne interwały powtarzania to:\n- Minuty, godziny lub dni\n- Tygodnie, opcjonalnie w wybrane dni tygodnia\n- Miesiące lub lata, w określone daty kalendarza lub według wzorca dnia tygodnia"
    - question: "Czy mogę ustawić kwotę w walucie fiat?"
      answer: "Tak. Kwotę możesz ustawić w:\n- Bitcoinach\n- Obsługiwanej walucie fiat\n\nKwoty w walucie fiat mogą korzystać z:\n- Bieżącego kursu\n- Kursu CoinGecko, ustalonego na 00:00 GMT\n\nDla następnej płatności można też ręcznie nadpisać kurs wymiany."
    - question: "Czy adresy są ponownie używane?"
      answer: "Nie. Każdy adres odbiorcy jest używany tylko raz. Gdy adresy odbiorcy się skończą, możesz dodać dla niego kolejne."
    - question: "Czy Bitcoin-Safe wysyła płatności automatycznie?"
      answer: "Nie. Gdy płatność staje się wymagalna, Schedule przygotowuje transakcję w Bitcoin-Safe do sprawdzenia, a Ty nadal odpowiadasz za jej podpisanie i wysłanie."
    - question: "Czy mogę zapłacić wielu odbiorcom naraz?"
      answer: "Tak. Zaznacz kilka płatności zaplanowanych i kliknij **Zapłać zaznaczone**. Bitcoin-Safe połączy je w jedną transakcję wsadową."
    - question: "Co zrobić, gdy płatność została już dokonana gotówką lub inaczej?"
      answer: "Możesz dodać wypłatę **poza portfelem**. Zapisuje ona płatność w harmonogramie bez transakcji Bitcoin, dzięki czemu postęp pozostaje dokładny."
---

### {{< page-title >}}

<p class="lead">Planuj płatności w Bitcoin, a Schedule pilnuje, co ma termin.</p>

<ul class="plugin-features">
<li>Wypłaty dla pracowników lub organizacja innych regularnych zobowiązań</li>
<li>Konfiguracja cyklicznych przelewów</li>
<li>Zaplanowanie jednorazowej płatności, o której nie chcesz zapomnieć</li>
</ul>

Gdy płatność staje się wymagalna, Schedule przygotowuje transakcję w Bitcoin-Safe do sprawdzenia. Nadal odpowiadasz za jej podpisanie i wysłanie.

{{< video "schedule.mp4" controls >}}

### Elastyczne plany płatności

- Wybierz płatność jednorazową, płatność z określoną liczbą powtórzeń lub harmonogram bez końca.
- Ustaw datę startu i interwał powtarzania: minuty, godziny, dni, tygodnie, miesiące lub lata. Harmonogramy tygodniowe mogą używać wybranych dni tygodnia; miesięczne i roczne obsługują daty kalendarza i wzorce dni tygodnia.
- Ustaw odbiorcę, kategorię i kwotę w bitcoinach lub w obsługiwanej walucie fiat.
- Dla kwot w walucie fiat użyj bieżącego kursu lub kursu CoinGecko ustalonego na 00:00 GMT. Dla następnej płatności można nadpisać kurs wymiany.
- Harmonogramy o określonej liczbie płatności pokazują podgląd kwoty za płatność i sumy.

### Przygotowanie płatności w portfelu

- Zobacz najbliższy termin i postęp płatności; wymagalne płatności są wyróżnione i mogą wywołać powiadomienie Bitcoin-Safe.
- Przygotuj jedną wymagalną płatność lub partię w edytorze transakcji, z wypełnionymi wyjściami dla odbiorców, etykietami i kategoriami.
- Sprawdź i w razie potrzeby zmień transakcję, a następnie sam ją podpisz i wyślij.
- Zapisuj wielokrotnie używanych odbiorców z nazwą i wieloma adresami. Schedule może wybrać nieużywany adres do wypłaty.

### Śledzenie i zarządzanie harmonogramami

- Wyszukuj harmonogramy według statusu terminu, typu lub kategorii. Listy pokazują daty, zrealizowane płatności, częstotliwość, odbiorcę, kwotę, kategorię i sumę.
- Przeglądaj zrealizowane wypłaty i nadchodzące terminy. Pasujące transakcje portfela mogą aktualizować postęp; wypłatę możesz dodać ręcznie lub ponownie przeskanować transakcje.
- Edytuj harmonogram przed pierwszą zapisaną wypłatą, duplikuj go lub usuń, a także importuj i eksportuj harmonogramy jako kopię zapasową w JSON.

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">Pobierz Bitcoin-Safe</h2>
<p class="text-muted mb-3">Wtyczki są dołączone do Bitcoin-Safe. Pobierz aplikację, aby je wypróbować.</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">Pobierz Bitcoin-Safe</a>
<small class="text-muted">Wolne oprogramowanie open source · Windows, macOS, Linux</small>
</div>
</section>

### Często zadawane pytania

<details>
<summary>Czy mogę zaplanować pojedynczą płatność, a nie tylko cykliczne?</summary>

Obie opcje są dostępne. Możesz utworzyć płatność jednorazową, płatność z określoną liczbą powtórzeń lub harmonogram bez końca.

</details>

<details>
<summary>Jak często harmonogram może się powtarzać?</summary>

Dostępne interwały powtarzania to:

- Minuty, godziny lub dni
- Tygodnie, opcjonalnie w wybrane dni tygodnia
- Miesiące lub lata, w określone daty kalendarza lub według wzorca dnia tygodnia

</details>

<details>
<summary>Czy mogę ustawić kwotę w walucie fiat?</summary>

Tak. Kwotę możesz ustawić w:

- Bitcoinach
- Obsługiwanej walucie fiat

Kwoty w walucie fiat mogą korzystać z:

- Bieżącego kursu
- Kursu CoinGecko, ustalonego na 00:00 GMT

Dla następnej płatności można też ręcznie nadpisać kurs wymiany.

</details>

<details>
<summary>Czy adresy są ponownie używane?</summary>

Nie. Każdy adres odbiorcy jest używany tylko raz. Gdy adresy odbiorcy się skończą, możesz dodać dla niego kolejne.

</details>

<details>
<summary>Czy Bitcoin-Safe wysyła płatności automatycznie?</summary>

Nie. Gdy płatność staje się wymagalna, Schedule przygotowuje transakcję w Bitcoin-Safe do sprawdzenia, a Ty nadal odpowiadasz za jej podpisanie i wysłanie.

</details>

<details>
<summary>Czy mogę zapłacić wielu odbiorcom naraz?</summary>

Tak. Zaznacz kilka płatności zaplanowanych i kliknij **Zapłać zaznaczone**. Bitcoin-Safe połączy je w jedną transakcję wsadową.

</details>

<details>
<summary>Co zrobić, gdy płatność została już dokonana gotówką lub inaczej?</summary>

Możesz dodać wypłatę **poza portfelem**. Zapisuje ona płatność w harmonogramie bez transakcji Bitcoin, dzięki czemu postęp pozostaje dokładny.

</details>
</content>
