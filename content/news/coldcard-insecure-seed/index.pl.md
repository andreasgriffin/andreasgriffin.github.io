---
title: "Niebezpieczny seed COLDCARD"
date: "2026-08-02"
draft: false
description: "Coinkite ujawniło krytyczną słabość generowania seedów w zagrożonym firmware COLDCARD. Jeśli utworzyłeś seed na dowolnym dotkniętym urządzeniu Coinkite, przenieś swoje środki na nowy seed."
images: ["COLDCARD Security Advisory Notice - Migrate ASAP.png"]
---

## Podsumowanie

[Coinkite ujawniło krytyczną słabość generowania seedów w zagrożonym firmware COLDCARD](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). [Analiza techniczna Block](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware) wskazała jako przyczynę przewidywalny programowy generator liczb losowych używany zamiast sprzętowego RNG urządzenia i ostrzega, że **trwa aktywna eksploatacja luki**. Aktualizacja firmware **nie** naprawia istniejącego seeda.

**Jeśli utworzyłeś seed na dowolnym dotkniętym urządzeniu Coinkite, przenieś swoje środki na nowy seed.**

## Czy moje urządzenie jest dotknięte?

Ryzyko zależy od **wersji firmware zainstalowanej w momencie generowania seeda**, a nie od daty produkcji urządzenia.

| Urządzenie | Firmware użyte do wygenerowania seeda | Status |
|---|---|---|
| Mk1 | Całe wydane firmware | Niedotknięte |
| Mk2 / Mk3 | v3.2.2 lub starsze | Niedotknięte (używa sprzętowego RNG) |
| Mk2 / Mk3 | v4.0.0 – v4.1.9 | **Podatne** — brak bezpiecznego reseedu |
| Mk4 | Produkcja od v5.0.0 | **Podatne** — ograniczone do ~72 bitów entropii |
| Q | Całe firmware produkcyjne | **Podatne** — ograniczone do ~72 bitów entropii |
| Mk5 | Całe firmware produkcyjne | **Podatne** — ograniczone do ~72 bitów entropii |
| TAPSIGNER, OPENDIME, SATSCARD | — | Niedotknięte (inny kod) |

Zwróć uwagę, że wyeksportowanie niebezpiecznego seeda i zaimportowanie go do innego portfela **nie** naprawia go — sam seed pozostaje dotknięty.

## Zainstaluj naprawione firmware przed wygenerowaniem nowego seeda

Naprawione firmware jest już dostępne dla każdego dotkniętego modelu i kanału wydań. Nie generuj nowego seeda na COLDCARD, dopóki go nie zainstalujesz.

| Urządzenie | Naprawione firmware |
|---|---|
| Mk2 / Mk3 | 4.2.0 lub nowsze |
| Mk4 / Mk5 (standard) | 5.6.0 lub nowsze |
| Q (standard) | 1.5.0Q lub nowsze |
| Mk4 / Mk5 (Edge) | 6.6.0X lub nowsze |
| Q (Edge) | 6.6.0QX lub nowsze |

Standard i Edge to osobne kanały wydań. Jeśli używasz Edge, zainstaluj naprawioną wersję Edge dla swojego modelu — nie zakładaj, że starsza wersja Edge 6.x jest naprawiona tylko dlatego, że jej numer jest wyższy niż wersji standard.

## Czy chronią mnie rzuty kośćmi lub fraza hasłowa?

- **Rzuty kośćmi:** błąd dotyczy wyłącznie entropii generowanej przez urządzenie. Jeśli podczas tworzenia seeda wprowadziłeś co najmniej **50 niezależnych, prywatnych rzutów kośćmi** (99 lub więcej dla około 256 bitów entropii), sam wkład kości zapewnił co najmniej 128 bitów niezależnej entropii i taki seed nie jest uważany za zagrożony wyłącznie przez ten problem. Przy mniej niż 50 rzutach — lub jeśli nie jesteś pewien, ile ich wprowadzono lub czy były prywatne — **migruj**.
- **Fraza hasłowa BIP-39:** silna, unikalna fraza hasłowa BIP-39 (nie PIN COLDCARD) dodaje niezależną barierę, ale **nie** naprawia dotkniętego seeda. Jeśli twoja fraza hasłowa jest krótka, powszechna, ponownie używana lub łatwa do odgadnięcia — lub nie jesteś pewien jej siły — potraktuj środki jako zagrożone i migruj natychmiast. Nawet przy silnej frazie hasłowej migruj na świeżo wygenerowany seed tak szybko, jak to możliwe.

## Lista kontrolna migracji

Migruj spokojnie i ostrożnie. Pośpiech podczas migracji portfela może stworzyć bardziej bezpośrednie ryzyko niż problem, który próbujesz rozwiązać.

1. **Zainstaluj naprawione firmware** dla swojego modelu przed wygenerowaniem zastępczego seeda. Jeśli wolisz, wygeneruj nowy seed na **urządzeniu podpisującym, które nie jest COLDCARD** ([zobacz obsługiwane urządzenia]({{< ref "library/supported-hardware-signers" >}})) — w każdym razie **nie** używaj ponownie starego seeda.
2. Wygeneruj całkowicie nowy seed i **zapisz go**. Przed wpłatą jakichkolwiek środków zweryfikuj pisemną kopię zapasową, odcisk portfela i adres odbioru.
3. Użyj kreatora konfiguracji Bitcoin-Safe, aby utworzyć nowy [portfel z pojedynczym podpisem]({{< ref "library/setup-singlesig-wallet" >}}) lub [portfel wielopodpisowy]({{< ref "library/setup-multisig-wallet" >}}) z nowym seedem.
4. Wykonaj test odbioru i wysyłki z kreatora: zweryfikuj kopię zapasową i adres odbioru na nowym podpisującym, odbierz niewielką kwotę testową i pomyślnie wyślij ją do siebie na inny zweryfikowany adres w nowym portfelu.
5. Podpisz i wyślij transakcję migracji:
   - **Portfel z pojedynczym podpisem:** wyślij go normalnie z wysoką opłatą, aby potwierdził się szybko.
   - **Portfel wielopodpisowy:** nie wysyłaj go normalnie, ponieważ to ujawnia jego klucze publiczne w publicznym mempoolu. Skopiuj podpisaną surową transakcję i prześlij ją bezpośrednio przez [MARA Slipstream](https://slipstream.mara.com/).
6. Przechowuj starą COLDCARD i jej kopię zapasową, dopóki **pełne saldo** nie dotrze i nie zostanie potwierdzone w nowym portfelu. Dopiero wtedy wymaż stary seed.

Jeśli Mk2/Mk3 to twoje jedyne urządzenie podpisujące, najpierw zainstaluj firmware 4.2.0 lub nowsze: poprawnie generuje ono zastępcze seedy, więc do ukończenia migracji nie potrzebujesz nowszej COLDCARD. Wykonaj te same kroki, ostrożnie przełączając się między starym a nowym seedem na jedynym urządzeniu, i przechowuj starą kopię zapasową do czasu pełnego potwierdzenia migracji.

## Jeśli używasz wielopodpisu

Jeśli konfiguracja wielopodpisowa składa się **wyłącznie** z dotkniętych urządzeń, luka nadal obowiązuje. Zabezpiecz konfigurację kworum, które obejmuje co najmniej jedno niedotknięte urządzenie podpisujące.

## Pomaganie komuś innemu w migracji

Nigdy nie proś ich o udostępnienie, sfotografowanie ani wpisanie słów seeda. Seed musi pozostać prywatny i może być wprowadzany wyłącznie na samym urządzeniu podpisującym.
