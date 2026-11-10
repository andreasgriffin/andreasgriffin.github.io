---
title: "Powiadomienia portfela"
description: "Przekazuj powiadomienia portfela i aplikacji Bitcoin-Safe do skonfigurowanych miejsc docelowych, z kontrolą dostarczania, prywatności i czasu wysyłki."
draft: false
tags: ["Plugins"]
images: ["notifications.png"]
weight: 35
faq:
  title: "Pytania o powiadomienia portfela"
  items:
    - question: "Dokąd Bitcoin-Safe może wysyłać powiadomienia?"
      answer: "Bitcoin-Safe może wysyłać powiadomienia:\n- Do webhooków: w ogólnym formacie JSON lub w formatach zgodnych ze Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy i Gotify\n- Jako wiadomości prywatne Nostr\n- Do botów Telegram\n- E-mailem przez SMTP\n- Do kalendarzy CalDAV"
    - question: "Czy mogę usunąć wrażliwe szczegóły z powiadomień?"
      answer: "Tak. Włącz ukrywanie wrażliwych szczegółów, a wiadomość będzie zawierać tylko ogólne powiadomienie, że wystąpiło zdarzenie Bitcoin-Safe."
    - question: "Czy mogę kontrolować, które zdarzenia trafiają dokąd?"
      answer: "Każde miejsce docelowe ma własne reguły. Wybierasz, jakie typy zdarzeń otrzymuje:\n- Transakcje portfela\n- Płatności zaplanowane\n- Synchronizacja i czat\n- Ostrzeżenia\n\nMożesz też ustawić opcjonalne losowe opóźnienie dostarczania."
    - question: "Czy aplikacja musi pozostać odblokowana?"
      answer: "Nie. Opcja „Zablokuj i zminimalizuj do zasobnika” pozwala Bitcoin-Safe działać w tle, gdy portfel jest zablokowany."
---

### {{< page-title >}}

<p class="lead">Otrzymuj informacje o aktywności portfela przez kanały, które Ci odpowiadają.</p>

<ul class="plugin-features">
<li>Transakcje przychodzące i wychodzące, wiadomości Sync&Chat, zaplanowane płatności, które nadeszły, ...</li>
<li>Przekazywanie alertów do webhooków, Nostr, Telegram, e-mail, kalendarzy i nie tylko</li>
<li>Wybór zdarzeń dla każdego miejsca docelowego i ukrywanie wrażliwych szczegółów</li>
<li>Utrzymuj Bitcoin-Safe w tle; użyj <strong>Zablokuj i zminimalizuj do zasobnika</strong>, aby aplikacja działała, gdy portfel jest zablokowany</li>
</ul>

### Konfiguracja webhooka

{{< video "webhook.mp4" controls >}}

### Wiadomości prywatne Nostr

{{< video "nostr.mp4" controls >}}

### Powiadomienia w kalendarzu

{{< video "calendar.mp4" controls >}}

### Połącz swoje miejsca docelowe

- Dodaj jedno lub więcej miejsc docelowych. Każde może mieć własnych odbiorców i reguły dostarczania.
- **E-mail:** bezpośrednie połączenie z serwerem SMTP: host, port, dane logowania, nadawca i ustawienia bezpieczeństwa. To nie jest zarządzana integracja z Gmail ani Outlook.
- **Telegram:** wysyłka do czatu przez bota. Rozpocznij rozmowę z botem, aby go sprawdzić i wykryć ostatnie identyfikatory czatów.
- **Nostr DM:** wysyłka zaszyfrowanych wiadomości NIP-17 do odbiorców `npub` przez skonfigurowane przekaźniki z kluczem nadawcy.
- **CalDAV:** dodawanie zdarzeń do istniejącego kalendarza, na przykład skonfigurowanego kalendarza Nextcloud.
- **Webhooki:** wysyłka w ogólnym formacie JSON lub w formatach dla punktów końcowych zgodnych ze Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy i Gotify. Popularne typy punktów końcowych mogą być wykrywane automatycznie.
- Zapisz ustawienia miejsca docelowego i użyj funkcji testowej, jeśli jest dostępna.

### Wybór tego, co jest wysyłane

- Wybierz, jakie typy zdarzeń otrzymuje każde miejsce docelowe:
  - Transakcje portfela
  - Płatności zaplanowane
  - Synchronizacja i czat
  - Ostrzeżenia
- Ukrywaj wrażliwe szczegóły. Wiadomość zawiera wtedy tylko ogólne powiadomienie, że wystąpiło zdarzenie Bitcoin-Safe.
- Ustaw losowe opóźnienie dostarczania do wybranego maksimum.
- Wiadomości o transakcjach portfela mogą zawierać link do eksploratora, jeśli jest dostępny i szczegóły nie są ukryte.

### Sprawdzanie dostarczenia

- Historia pokazuje każde zdarzenie, miejsce docelowe, adapter, czas i wynik: wysłane, częściowo lub niepowodzenie.
- Dostarczenie zależy od skonfigurowanego miejsca docelowego i jego dostępności. Zastanów się, jakie informacje wysyłasz do usług zewnętrznych.

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
<summary>Dokąd Bitcoin-Safe może wysyłać powiadomienia?</summary>

Bitcoin-Safe może wysyłać powiadomienia:

- Do webhooków: w ogólnym formacie JSON lub w formatach zgodnych ze Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy i Gotify
- Jako wiadomości prywatne Nostr
- Do botów Telegram
- E-mailem przez SMTP
- Do kalendarzy CalDAV

</details>

<details>
<summary>Czy mogę usunąć wrażliwe szczegóły z powiadomień?</summary>

Tak. Włącz ukrywanie wrażliwych szczegółów, a wiadomość będzie zawierać tylko ogólne powiadomienie, że wystąpiło zdarzenie Bitcoin-Safe.

</details>

<details>
<summary>Czy mogę kontrolować, które zdarzenia trafiają dokąd?</summary>

Każde miejsce docelowe ma własne reguły. Wybierasz, jakie typy zdarzeń otrzymuje:

- Transakcje portfela
- Płatności zaplanowane
- Synchronizacja i czat
- Ostrzeżenia

Możesz też ustawić opcjonalne losowe opóźnienie dostarczania.

</details>

<details>
<summary>Czy aplikacja musi pozostać odblokowana?</summary>

Nie. Opcja „Zablokuj i zminimalizuj do zasobnika” pozwala Bitcoin-Safe działać w tle, gdy portfel jest zablokowany.

</details>
</content>
