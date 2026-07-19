---
aliases:
  - "/pl/features/reproducibility-and-security/"
title: "Bezpieczenstwo i odtwarzalnosc"
description: "Bitcoin-Safe utrzymuje wysoki standard bezpieczenstwa plikow binarnych: odtwarzalne buildy, podpisane commity, podpisane wydania i niezalezny zewnetrzny monitoring."
draft: false
bucket: features
tags: ["Featured", "Security"]
images: ["logo.png"]
keywords: ["reproducible builds", "verify binaries", "signed commits", "signed releases", "appimage", "flatpak", "windows exe", "binary security"]
weight: 18
---

### {{< page-title >}}
{{< page-description >}}
<br>

![Wyniki odtwarzalnych buildow dla Bitcoin-Safe](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 500px;" }

Wprowadzilismy kilka warstw ochrony integralnosci plikow pobieranych ze strony, aby aplikacja, ktora pobierasz, rzeczywiscie odpowiadala publicznemu kodowi zrodlowemu:

- **Odtwarzalne buildy**: Buildy Linux `deb`, `AppImage` i `Flatpak`, a takze Windows `portable exe` i `setup exe`, mozna odtworzyc bajt w bajt. Jesli przebudowany plik zgadza sie dokladnie, to mocny dowod, ze binarka zostala zbudowana z tego samego kodu zrodlowego.
- **Podpisana historia repozytorium**: [Repozytorium Bitcoin-Safe na GitHubie](https://github.com/andreasgriffin/bitcoin-safe/commits/main) publikuje zweryfikowane podpisane commity, aby osoby przegladajace kod mogly sprawdzic, kto utworzyl kod, ktory trafil do wydania.
- **Podpisane binarki**: Pliki wydan sa podpisywane [publicznym kluczem PGP]({{< gpg_key_link >}}) Bitcoin-Safe, a binarki Windows dodatkowo podlegaja [polityce podpisywania kodu]({{< ref "code-signing-policy" >}}).
- **Niezalezne kontrole odtwarzalnosci**: [WalletScrutiny](https://walletscrutiny.com/desktop/bitcoin.safe/) niezaleznie sledzi Bitcoin-Safe i pokazuje status odtwarzalnej weryfikacji dla wydan desktopowych.
- **Ciagly monitoring podpisow**: [BinaryWatch](https://binarywatch.org/) regularnie sprawdza pliki wydan Bitcoin-Safe oraz to, czy ich podpisy nadal sa prawidlowe wzgledem [publicznego klucza PGP]({{< gpg_key_link >}}) Bitcoin-Safe.
- **Weryfikacja aktualizacji**: Aktualizacje sa pokazywane w Bitcoin-Safe, a ich podpis jest weryfikowany automatycznie.

Lacznie te dzialania stawiaja Bitcoin-Safe w niewielkiej grupie projektow, ktore traktuja bezpieczenstwo binarek jako podstawowy element bezpieczenstwa uzytkownika, a nie jako dodatek po fakcie.

### Bezpieczenstwo jest glownym kryterium w kazdym aspekcie Bitcoin-Safe

Poza integralnoscia binarek Bitcoin-Safe opiera sie na bezpiecznych ustawieniach domyslnych, dobrych praktykach operacyjnych i jasnych wskazowkach dla uzytkownika. Kilka przykladow:

- **Przechowywanie oparte na hardware**: Bitcoin-Safe wymaga [sprzetowych signerow]({{< ref "library/supported-hardware-signers" >}}), aby seed pozostawal na dedykowanych urzadzeniach zamiast stawac sie goracym sekretem na zwyklym komputerze.
- **Bezpieczniejszy proces konfiguracji**: Kreator konfiguracji pomaga tworzyc portfele, ktore sa naprawde gotowe do realnego uzycia, w tym testy [sprzetowych signerow]({{< ref "library/supported-hardware-signers" >}}), [arkusze PDF do backupu]({{< ref "library/pdf-export/" >}}) oraz wskazowki, jak przechowywac signery i kopie zapasowe seeda.
- **Weryfikacja adresu odbiorczego**: Bitcoin-Safe ulatwia [weryfikacje adresow odbiorczych]({{< ref "library/verify-receive-address/" >}}) bezposrednio na signerze przed ich udostepnieniem.
- **Wykrywanie address poisoning**: Ostrzega przed podejrzanymi [podobnymi adresami]({{< ref "library/address-poisoning/" >}}).
- **Bezpieczenstwo multisig**: Bitcoin-Safe obsluguje portfele multisignature, dzieki czemu wieksze srodki moga byc chronione przez wiele urzadzen lub osob zamiast jednego punktu awarii.
- **Wspolpraca, ktora ulatwia multisig**: Bitcoin-Safe sprawia, ze [wspolpraca multisignature]({{< ref "library/collaboration/" >}}) jest praktyczna, wiec koordynacja konfiguracji i podpisywania jest znacznie prostsza w realnym uzyciu.
- **Jasne przeplywy podpisywania**: Ekrany podpisywania dopasowane do urzadzen zmniejszaja zamieszanie podczas przegladu PSBT i pomagaja uzytkownikom wykonac wlasciwe dzialanie na wlasciwym signerze.
