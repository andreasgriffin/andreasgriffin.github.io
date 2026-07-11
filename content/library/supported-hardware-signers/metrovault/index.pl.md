---
aliases:
- /pl/knowledge/supported-hardware-signers/metrovault/
title: MetroVault
signer: metrovault
bucket: knowledge
---

MetroVault moze zamienic stary telefon z Androidem w dedykowane urzadzenie do podpisywania Bitcoina offline dla Bitcoin Safe. Nie instaluj go na swoim codziennym telefonie. Najpierw zresetuj urzadzenie, trzymaj je **OFFLINE** i bez polaczenia z internetem oraz uzywaj go wylacznie do podpisywania.

## Czego sie spodziewac

- Zresetuj stary telefon z Androidem przed instalacja i uzywaj go tylko jako urzadzenia podpisujacego.
- Nie instaluj innych aplikacji, nie loguj sie do zadnych kont, nie wkladaj karty SIM i nie podlaczaj urzadzenia ponownie do internetu.
- Wymieniaj dane portfela, deskryptory i PSBT z Bitcoin Safe za pomoca kodow QR.
- Rejestruj deskryptory multisig i eksportuj dane sygnatariusza dla Bitcoin Safe.
- Sprawdz wszystkie szczegoly na ekranie MetroVault przed podpisaniem.

## Zresetuj urzadzenie z Androidem i uzywaj go tylko jako podpisujacego offline

Dokumentacja MetroVault zawiera teraz kompleksowy [przewodnik konfiguracji urzadzenia](https://github.com/gorunjinian/MetroVault/blob/main/docs/DEVICE_SETUP.md). Zdecydowanie zalecamy postepowanie zgodnie z nim krok po kroku i traktowanie go jako wymogu: uzywaj dedykowanego telefonu po resecie fabrycznym, **OFFLINE**, ktory po konfiguracji pozostaje odlaczony od internetu i sluzy wylacznie do podpisywania.

1. Zresetuj telefon do ustawien fabrycznych przed instalacja.
2. Pomin konfiguracje konta Google i utrzymuj urzadzenie offline.
3. Pozostaw tryb samolotowy wlaczony na stale.
4. Wylacz Wi-Fi, Bluetooth, NFC i dane komorkowe.
5. Wyjmij karte SIM.
6. Wylacz debugowanie USB.
7. Nie instaluj innych aplikacji i nie uzywaj telefonu do niczego poza podpisywaniem.

Do uzycia produkcyjnego kompiluj ze zrodel, gdy tylko to mozliwe. Jesli nie mozesz utrzymac urzadzenia offline i przeznaczonego tylko do podpisywania, nie uzywaj go do produkcyjnych srodkow MetroVault.
