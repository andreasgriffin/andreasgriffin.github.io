---
title: "Bitcoin Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "Informacje o wydaniu Bitcoin Safe 2.0.0 z przebudowanym kreatorem konfiguracji, prywatna synchronizacja przez Compact Block Filters oraz szersza obsluga portfeli sprzetowych."
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">Ogłoszenie wydania</p>
    <h2 class="display-6 mb-3">Bitcoin Safe 2.0 - prowadzone tworzenie portfela, prywatna synchronizacja lancucha i podpisywanie skupione na urzadzeniu</h2>
    <p class="lead mb-4">To wydanie przynosi przebudowany kreator konfiguracji, prywatna synchronizacje lancucha z Compact Block Filters oraz przeplyw podpisywania zorganizowany wokol kazdego urzadzenia sprzetowego. Jesli interesowala Cie samodzielna piecza nad srodkami, ale miales watpliwosci, to jest wydanie warte wyprobowania.</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Pobierz Bitcoin Safe 2.0</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">Zobacz nowosci</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Konfiguracja portfela krok po kroku</h2>
          <p class="mb-0">Nowy kreator wyjasnia kazdy krok, zmniejsza niejednoznacznosc i pomaga nowym osobom wybrac wlasciwa sciezke bez utraty mocy multisig.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Prywatna synchronizacja portfela</h2>
          <p class="mb-0">Nowe portfele synchronizuja sie teraz z Compact Block Filters od razu, dzieki czemu mozna skanowac lancuch prywatnie bez polegania na zewnetrznym indeksatorze Electrum.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Podpisywanie skupione na urzadzeniu</h2>
          <p class="mb-0">Przeplywy podpisywania sa teraz skupione na urzadzeniu przed Toba, z jasniejszymi kolejnymi krokami dla QR, USB, Bluetooth, plikow i koordynacji multisig.</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## Prowadzona droga do samodzielnej pieczy nad srodkami {#setup-flow}

Doswiadczenie pierwszego uruchomienia zostalo zbudowane od nowa. Bitcoin Safe nadal celuje w powazna samodzielna piecze nad srodkami, w tym multisig oparty na urzadzeniach sprzetowych, a wersja 2.0 daje nowym osobom prowadzona sciezke przez ten proces. Nowy kreator wyjasnia, co sie dzieje, gdzie jestes w przeplywie i czego kazdy signer potrzebuje od Ciebie, zanim przejdziesz dalej.

<p class="small text-muted">Szczegoly implementacji znajdziesz w <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a>.</p>

Najwazniejsze elementy przebudowy:

- Nowy ekran powitalny, ktory pomaga osobom zaczynajacym wybrac wlasciwy punkt startowy
- Przeplyw postepu krok po kroku podczas tworzenia portfela
- Ekrany podpisywania specyficzne dla urzadzenia z konkretnymi instrukcjami i pomoca kontekstowa
- Pliki PDF do odzyskiwania z nazwami i ikonami urzadzen, aby kopie zapasowe pozostawaly jednoznaczne

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## Prywatna i solidna synchronizacja lancucha z Compact Block Filters {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) napedzaja teraz synchronizacje nowych portfeli w Bitcoin Safe 2.0. Zamiast pytac serwer Electrum, ktore adresy naleza do Ciebie, Bitcoin Safe moze teraz skanowac lancuch prywatnie, pobierajac zwarte filtry od losowych wezlow Bitcoin Core i sprawdzajac je lokalnie.

<p class="small text-muted">Szczegoly implementacji znajdziesz w <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a>.</p>


- Synchronizacja portfela pozostaje prywatna od pierwszego uruchomienia
- Brak zaleznosci od zewnetrznych serwerow Electrum
- Electrum nadal pozostaje dostepne dla osob, ktore je preferuja
- [Natychmiastowa synchronizacja po poczatkowym skanowaniu portfela]({{< ref "library/compact-block-filters" >}})
- [Natychmiastowe powiadomienia o przekazanych transakcjach]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## Przeplyw podpisywania skupiony na urzadzeniu dla kazdego urzadzenia {#device-focused-signing}

Przebudowa zmienia takze przeplyw podpisywania po utworzeniu portfela. Zamiast jednego ogolnego ekranu dla wszystkich signerow, Bitcoin Safe skupia teraz akcje wokol konkretnego urzadzenia, ktorego uzywasz.

<p class="small text-muted">Szczegoly implementacji znajdziesz w <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a>.</p>

- Akcje QR, USB, Bluetooth, eksport/import plikow oraz Sync & Chat sa pokazane bezposrednio na karcie aktywnego signera
- Pozostali signerzy, urzadzenia, ktore juz podpisaly, oraz kolejny wymagany krok pozostaja widoczne na pierwszy rzut oka
- Przeplywy multisig z mieszanymi urzadzeniami pozostaja czytelne, poniewaz tozsamosc signera jest widoczna przez caly PSBT
- Zlozone transakcje z mieszanka wejsc single-sig i multisig sa obslugiwane poprawnie, dzieki czemu kazdy krok podpisywania jest jasny

![Karta signera z akcjami specyficznymi dla urzadzenia: QR, USB, Bluetooth, eksport pliku i Chat & Sync](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Architektura pluginow dla procesow biznesowych i zaawansowanych uzytkownikow

Bitcoin Safe 2.0 kladzie tez fundament pod przyszle dodatkowe pluginy kierowane do firm Bitcoinowych i zaawansowanych Bitcoinowcow. Warto wiec obserwowac, co nadejdzie :-)

<p class="small text-muted">Szczegoly implementacji znajdziesz w <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a>.</p>

- Dystrybucja pluginow przez zewnetrzne repozytorium *sources*
- Kazdy plugin jest *podpisany GPG* przez [andreasgriffin]({{< gpg_key_link >}}), aby zapewnic bezpieczenstwo, integralnosc i dostarczanie pluginu
- Niezalezne wersjonowanie pluginow i aktualizacje pozwalaja na szybszy i niezalezny rozwoj pluginow

![Karta signera z akcjami specyficznymi dla urzadzenia: QR, USB, Bluetooth, eksport pliku i Chat & Sync](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Szersza obsluga urzadzen i dopracowanie {#hardware-support}

- Animowane kody QR dzialaja **30%** szybciej, co przyspiesza skanowanie
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) jest teraz obslugiwany przez USB
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) obsluguje teraz **Bluetooth** oprocz USB i QR
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) oraz [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) zostaly dodane jako obslugiwane urzadzenia
- Zobacz [pelna liste obslugiwanych urzadzen]({{< ref "library/supported-hardware-signers" >}})
- Dodano automatyczne kontrole [odtwarzalnosci]({{< ref "library/reproducibility-and-security" >}})
- Tutaj znajdziesz [pelna liste](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0) ulepszen


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## Dotychczasowe mocne strony nadal tu sa

Wersja 2.0 nie jest resetem. Pod nowym onboardingiem i przeplywem podpisywania Bitcoin Safe nadal zachowuje funkcje, ktore sprawialy, ze byl przydatny na co dzien: wspolpracujacy multisig, kopie zapasowe PDF, przeszukiwalna historie portfela, wizualizacje przeplywu pieniedzy, synchronizacje etykiet i wiele wiecej.

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">Gotowy, aby wyprobowac Bitcoin Safe 2.0?</h2>
  <p class="mb-3">Pobierz najnowsze wydanie i samodzielnie sprawdz nowy onboarding, prywatna synchronizacje oraz ulepszenia dla portfeli sprzetowych.</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Pobierz Bitcoin Safe</a>
</div>


<br><br>

## Dziekujemy

To wydanie opiera sie na ogromie pracy wspoltworcow, testerow i [osob wspierajacych caly projekt]({{< ref "donate" >}}):

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r)) za przebudowe kreatora, prace nad UI pluginow i **swietne oraz niestrudzone** wsparcie UI/UX
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) za klienta Compact Block Filter, ktory teraz napedza prywatna synchronizacje nowych portfeli
- Zespol [Bitcoin Dev Kit](https://github.com/bitcoindevkit/) za biblioteki stanowiace rdzen Bitcoin Safe
- Zespol [ndk](https://github.com/nostr-dev-kit/ndk) za biblioteki napedzajace funkcjonalnosc nostr
- Wszystkim w spolecznosci Bitcoin Safe, ktorzy testowali wersje kandydujace, zglaszali bledy, tlumaczyli strony, wysylali saty i popychali projekt do przodu
- [Tlumacze]({{< ref "donate/#translators" >}}), w tym <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (Wietnamski)" title="qdyg-vn 🇻🇳 (Wietnamski)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (Niemiecki)" title="bsn21m 🇩🇪 (Niemiecki)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (Hiszpanski)" title="cyphra 🇪🇸 (Hiszpanski)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (Chinski)" title="DaGrindDontStop 🇨🇳 (Chinski)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


Jesli chcesz pomoc sfinansowac nastepne wydanie, mozesz przekazac datek tutaj: {{< donation_btc >}}
