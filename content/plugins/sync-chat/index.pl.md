---
title: "Sync & Chat"
description: "Znajduj uczestników portfela, synchronizuj etykiety i kategorie, rozmawiaj bezpiecznie i udostępniaj PSBT jednym kliknięciem."
draft: false
tags: ["Plugins", "sync-chat-mainpage"]
images: ["logo.png"]
weight: 30
faq:
  title: "Pytania o Sync & Chat"
  items:
    - question: "Jak urządzenia znajdują się nawzajem?"
      answer: "Sync & Chat szuka innych urządzeń, które używają tego samego deskryptora portfela. Deskryptor jest haszowany przed użyciem do wyszukiwania, więc nie jest ujawniany w postaci jawnej. Każde znalezione urządzenie trzeba też ręcznie dodać i oznaczyć jako zaufane, zanim będzie mogło uczestniczyć w czacie. Dzięki temu czat pozostaje bezpieczny, nawet jeśli deskryptor nie jest tajny."
    - question: "Jak wygląda współpraca w praktyce?"
      answer: "1. Konfiguracja (jednorazowo): dodaj urządzenie każdego uczestnika i oznacz je jako zaufane.\n2. Utworzenie: jeden z uczestników tworzy PSBT i dodaje swój podpis.\n3. Udostępnienie: PSBT trafia do wszystkich uczestników lub tylko do wybranych.\n4. Podpisywanie: każdy uczestnik dodaje swój podpis, aż transakcja zostanie w pełni podpisana.\n5. Nadanie: ostatni podpisujący nadaje transakcję, a potem pojawia się ona w portfelu każdego uczestnika."
    - question: "Co jest synchronizowane?"
      answer: "Sync & Chat synchronizuje:\n- Kategorie i etykiety monet między podpisującymi, nawet między różnymi systemami operacyjnymi\n- Udostępnianie PSBT jednym kliknięciem"
    - question: "Czy czat jest prywatny?"
      answer: "Tak. Czat portfela jest szyfrowany i działa przez Nostr; kopie zapasowe etykiet są również przechowywane zaszyfrowane przez Nostr."
---

### {{< page-title >}}

<p class="lead">Koordynuj podpisujących w multisig i utrzymuj kontekst portfela w synchronizacji bezpośrednio z Bitcoin-Safe.</p>

<ul class="plugin-features">
<li>Znajdź inne urządzenia korzystające z tego samego deskryptora portfela</li>
<li>Synchronizuj etykiety i kategorie między podpisującymi</li>
<li>Rozmawiaj bezpiecznie i udostępniaj PSBT jednym kliknięciem</li>
</ul>

### Synchronizacja etykiet

{{< video src="../../library/label-sync/label-sync.mp4" controls="true" >}}

### Wspólne podpisywanie

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

Pełny przewodnik po wspólnym podpisywaniu w multisig znajdziesz w artykule [Współpraca w multisig]({{< ref "library/collaboration/" >}}).

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
<summary>Jak urządzenia znajdują się nawzajem?</summary>

Sync & Chat szuka innych urządzeń, które używają tego samego deskryptora portfela. Deskryptor jest haszowany przed użyciem do wyszukiwania, więc nie jest ujawniany w postaci jawnej. Każde znalezione urządzenie trzeba też ręcznie dodać i oznaczyć jako zaufane, zanim będzie mogło uczestniczyć w czacie. Dzięki temu czat pozostaje bezpieczny, nawet jeśli deskryptor nie jest tajny.

</details>

<details>
<summary>Jak wygląda współpraca w praktyce?</summary>

1. **Konfiguracja (jednorazowo):** dodaj urządzenie każdego uczestnika i oznacz je jako zaufane.
2. **Utworzenie:** jeden z uczestników tworzy PSBT i dodaje swój podpis.
3. **Udostępnienie:** PSBT trafia do wszystkich uczestników lub tylko do wybranych.
4. **Podpisywanie:** każdy uczestnik dodaje swój podpis, aż transakcja zostanie w pełni podpisana.
5. **Nadanie:** ostatni podpisujący nadaje transakcję, a potem pojawia się ona w portfelu każdego uczestnika.

</details>

<details>
<summary>Co jest synchronizowane?</summary>

Sync & Chat synchronizuje:

- Kategorie i etykiety monet między podpisującymi, nawet między różnymi systemami operacyjnymi
- Udostępnianie PSBT jednym kliknięciem

</details>

<details>
<summary>Czy czat jest prywatny?</summary>

Tak. Czat portfela jest szyfrowany i działa przez Nostr; kopie zapasowe etykiet są również przechowywane zaszyfrowane przez Nostr.

</details>

{{< sync-page-box >}}
</content>
