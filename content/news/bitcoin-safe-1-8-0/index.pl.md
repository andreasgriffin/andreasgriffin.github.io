---
title: "Bitcoin Safe 1.8.0"
date: "2026-03-31"
description: "Informacje o wydaniu Bitcoin Safe 1.8.0, obejmujace powiekszanie wykresu salda, niestandardowy nLocktime, tryb blokady aplikacji i latwiejsze aktualizacje."
videos:
  - "https://www.youtube.com/watch?v=S0O40-p_w0M"
---

## Nowe funkcje

#### Powiekszanie wykresu salda

Dodano powiekszanie wykresu salda ([#492](https://github.com/andreasgriffin/bitcoin-safe/pull/492)).

{{< video src="zoom.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 powiekszanie wykresu salda" description="Podglad powiekszania wykresu salda w Bitcoin Safe 1.8.0." >}}

#### Niestandardowy nLocktime

Dodano obsluge niestandardowego nLocktime, ktory pozwala ustawic najwczesniejsza wysokosc bloku lub czas, w ktorym transakcja moze zostac potwierdzona ([#481](https://github.com/andreasgriffin/bitcoin-safe/pull/481)).

{{< video src="nLocktime.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 niestandardowy nLocktime" description="Podglad obslugi niestandardowego nLocktime w Bitcoin Safe 1.8.0." >}}

#### Obsluga Bluetooth dla Jade

Dodano obsluge Bluetooth dla Jade ([#517](https://github.com/andreasgriffin/bitcoin-safe/pull/517)).

{{< video src="bluetooth.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 obsluga Bluetooth dla Jade" description="Podglad obslugi Bluetooth dla Jade w Bitcoin Safe 1.8.0." >}}

#### Tryb blokady aplikacji

Dodano tryb blokady aplikacji, czyli sposob na zablokowanie aplikacji, gdy nadal dziala w tle ([#519](https://github.com/andreasgriffin/bitcoin-safe/pull/519)).

{{< video src="app-lock.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 tryb blokady aplikacji" description="Podglad trybu blokady aplikacji w Bitcoin Safe 1.8.0." >}}

Dodano takze plynna funkcje aktualizacji w Windows oraz latwiejsze aktualizacje na macOS i Linux ([#513](https://github.com/andreasgriffin/bitcoin-safe/pull/513)).

## Ulepszenia

- Historia powiadomien jest teraz dostepna z ikony zasobnika ([#493](https://github.com/andreasgriffin/bitcoin-safe/pull/493))
- Poprawki bledow i drobne ulepszenia interfejsu

## Wklad

- [@bsn21m](https://github.com/bsn21m) wniósł swoj pierwszy wkład w [#538](https://github.com/andreasgriffin/bitcoin-safe/pull/538)
- Dzieki dla zespolu [bdk](https://github.com/bitcoindevkit/) i [@rustaceanrob](https://github.com/rustaceanrob)
- Wielkie dzieki dla [@design-rrr](https://github.com/design-rrr) za wsparcie w projektowaniu i UX
