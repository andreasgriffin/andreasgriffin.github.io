---
title: "Bitcoin Safe 1.8.0"
date: "2026-03-31"
description: "Notes de version de Bitcoin Safe 1.8.0, avec zoom du graphique de solde, nLocktime personnalise, mode de verrouillage de l'application et mises a jour plus simples."
videos:
  - "https://www.youtube.com/watch?v=S0O40-p_w0M"
---

## Nouvelles fonctionnalites

#### Zoom du graphique de solde

Ajout du zoom du graphique de solde ([#492](https://github.com/andreasgriffin/bitcoin-safe/pull/492)).

{{< video src="zoom.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 zoom du graphique de solde" description="Apercu du zoom du graphique de solde dans Bitcoin Safe 1.8.0." >}}

#### nLocktime personnalise

Ajout de la prise en charge de nLocktime personnalise, qui permet de definir la premiere hauteur de bloc ou le moment ou une transaction peut etre confirmee ([#481](https://github.com/andreasgriffin/bitcoin-safe/pull/481)).

{{< video src="nLocktime.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 nLocktime personnalise" description="Apercu de la prise en charge de nLocktime personnalise dans Bitcoin Safe 1.8.0." >}}

#### Prise en charge Bluetooth pour Jade

Ajout de la prise en charge Bluetooth pour Jade ([#517](https://github.com/andreasgriffin/bitcoin-safe/pull/517)).

{{< video src="bluetooth.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 prise en charge Bluetooth pour Jade" description="Apercu de la prise en charge Bluetooth pour Jade dans Bitcoin Safe 1.8.0." >}}

#### Mode de verrouillage de l'application

Ajout du mode de verrouillage de l'application, une facon de verrouiller l'application tout en la laissant s'executer en arriere-plan ([#519](https://github.com/andreasgriffin/bitcoin-safe/pull/519)).

{{< video src="app-lock.mp4" controls=true muted=true playsinline=true loop=true uploadDate="2026-03-31" name="Bitcoin Safe 1.8.0 mode de verrouillage de l'application" description="Apercu du mode de verrouillage de l'application dans Bitcoin Safe 1.8.0." >}}

La version inclut egalement une fonction de mise a jour transparente sur Windows et des mises a jour plus simples sur macOS et Linux ([#513](https://github.com/andreasgriffin/bitcoin-safe/pull/513)).

## Ameliorations

- L'historique des notifications est maintenant disponible depuis l'icone de la zone de notification ([#493](https://github.com/andreasgriffin/bitcoin-safe/pull/493))
- Corrections de bugs et petites ameliorations de l'interface

## Contributions

- [@bsn21m](https://github.com/bsn21m) a realise sa premiere contribution dans [#538](https://github.com/andreasgriffin/bitcoin-safe/pull/538)
- Merci a l'equipe [bdk](https://github.com/bitcoindevkit/) et a [@rustaceanrob](https://github.com/rustaceanrob)
- Un grand merci a [@design-rrr](https://github.com/design-rrr) pour son soutien en design et UX
