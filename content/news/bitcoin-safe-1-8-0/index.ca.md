---
title: "Bitcoin Safe 1.8.0"
date: "2026-03-31"
description: "Notes de llançament de Bitcoin Safe 1.8.0, incloent el zoom del gràfic de saldo, nLocktime personalitzat, mode de bloqueig de l'aplicació i actualitzacions més fàcils."
videos:
  - "https://www.youtube.com/watch?v=S0O40-p_w0M"
---

## Noves funcions

#### Zoom del gràfic de saldo

S'ha afegit el zoom del gràfic de saldo ([#492](https://github.com/andreasgriffin/bitcoin-safe/pull/492)).

{{< video src="zoom.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 zoom del gràfic de saldo" description="Previsualització del zoom del gràfic de saldo a Bitcoin Safe 1.8.0." >}}

#### nLocktime personalitzat

S'ha afegit suport per a nLocktime personalitzat, que permet definir la primera alçada de bloc o hora en què una transacció es pot confirmar ([#481](https://github.com/andreasgriffin/bitcoin-safe/pull/481)).

{{< video src="nLocktime.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 nLocktime personalitzat" description="Previsualització del suport per a nLocktime personalitzat a Bitcoin Safe 1.8.0." >}}

#### Suport Bluetooth per a Jade

S'ha afegit suport Bluetooth per a Jade ([#517](https://github.com/andreasgriffin/bitcoin-safe/pull/517)).

{{< video src="bluetooth.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 suport Bluetooth per a Jade" description="Previsualització del suport Bluetooth per a Jade a Bitcoin Safe 1.8.0." >}}

#### Mode de bloqueig de l'aplicació

S'ha afegit el mode de bloqueig de l'aplicació, una manera de bloquejar l'aplicació mentre continua executant-se en segon pla ([#519](https://github.com/andreasgriffin/bitcoin-safe/pull/519)).

{{< video src="app-lock.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 mode de bloqueig de l'aplicació" description="Previsualització del mode de bloqueig de l'aplicació a Bitcoin Safe 1.8.0." >}}

També s'hi inclou funcionalitat d'actualització transparent a Windows i actualitzacions més senzilles a macOS i Linux ([#513](https://github.com/andreasgriffin/bitcoin-safe/pull/513)).

## Millores

- L'historial de notificacions ara està disponible des de la icona de la safata ([#493](https://github.com/andreasgriffin/bitcoin-safe/pull/493))
- Correccions d'errors i petites millores d'interfície

## Contribucions

- [@bsn21m](https://github.com/bsn21m) va fer la seva primera contribució a [#538](https://github.com/andreasgriffin/bitcoin-safe/pull/538)
- Gràcies a l'equip de [bdk](https://github.com/bitcoindevkit/) i a [@rustaceanrob](https://github.com/rustaceanrob)
- Moltes gràcies a [@design-rrr](https://github.com/design-rrr) pel suport en disseny i UX
