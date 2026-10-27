---
title: "Seed COLDCARD non sicuro"
date: "2026-08-02"
draft: false
description: "Coinkite ha reso nota una debolezza critica nella generazione dei seed sui firmware COLDCARD interessati. Se hai creato un seed con un dispositivo Coinkite interessato, sposta i tuoi fondi su un nuovo seed."
images: ["COLDCARD Security Advisory Notice - Migrate ASAP.png"]
---

## Sintesi

[Coinkite ha reso nota una debolezza critica nella generazione dei seed sui firmware COLDCARD interessati](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). [L'analisi tecnica di Block](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware) ha individuato la causa in un generatore di numeri casuali software prevedibile usato al posto dell'RNG hardware del dispositivo e avverte che **è in corso uno sfruttamento attivo**. L'aggiornamento del firmware **non** corregge un seed esistente.

**Se hai creato un seed con un dispositivo Coinkite interessato, sposta i tuoi fondi su un nuovo seed.**

## Il mio dispositivo è interessato?

L'esposizione dipende dalla **versione del firmware installata quando è stato generato il seed**, non da quando il dispositivo è stato fabbricato.

| Dispositivo | Firmware usato per generare il seed | Stato |
|---|---|---|
| Mk1 | Tutto il firmware pubblicato | Non interessato |
| Mk2 / Mk3 | v3.2.2 o precedente | Non interessato (usa RNG hardware) |
| Mk2 / Mk3 | v4.0.0 – v4.1.9 | **Vulnerabile** — nessun reseed sicuro |
| Mk4 | Produzione da v5.0.0 in poi | **Vulnerabile** — limitato a ~72 bit di entropia |
| Q | Tutto il firmware di produzione | **Vulnerabile** — limitato a ~72 bit di entropia |
| Mk5 | Tutto il firmware di produzione | **Vulnerabile** — limitato a ~72 bit di entropia |
| TAPSIGNER, OPENDIME, SATSCARD | — | Non interessato (codice diverso) |

Nota: esportare un seed non sicuro e importarlo in un altro portafoglio **non** lo corregge: il seed stesso rimane interessato.

## Installa il firmware corretto prima di generare un nuovo seed

Il firmware corretto è ora disponibile per ogni modello e canale di rilascio interessato. Non generare un nuovo seed su una COLDCARD finché non è installato.

| Dispositivo | Firmware corretto |
|---|---|
| Mk2 / Mk3 | 4.2.0 o successivo |
| Mk4 / Mk5 (standard) | 5.6.0 o successivo |
| Q (standard) | 1.5.0Q o successivo |
| Mk4 / Mk5 (Edge) | 6.6.0X o successivo |
| Q (Edge) | 6.6.0QX o successivo |

Standard ed Edge sono canali di rilascio separati. Se usi Edge, installa la versione Edge corretta per il tuo modello: non dare per scontato che una versione Edge 6.x più vecchia sia corretta solo perché il suo numero è più alto di quello della versione standard.

## I lanci di dadi o una passphrase mi proteggono?

- **Lanci di dadi:** il bug riguarda solo l'entropia generata dal dispositivo. Se hai inserito almeno **50 lanci di dadi indipendenti e privati** durante la creazione del seed (99 o più per circa 256 bit di entropia), l'input dei dadi da solo ha fornito almeno 128 bit di entropia indipendente e il seed non è considerato a rischio per questo solo problema. Con meno di 50 lanci — o se non sei sicuro di quanti ne siano stati inseriti o se erano privati — **migra**.
- **Passphrase BIP-39:** una passphrase BIP-39 forte e unica (non il PIN della COLDCARD) aggiunge una barriera indipendente, ma **non** corregge il seed interessato. Se la tua passphrase è corta, comune, riusata o prevedibile — o non sei sicuro della sua robustezza — tratta i fondi come a rischio e migra immediatamente. Anche con una passphrase forte, migra verso un seed appena generato appena possibile.

## Checklist per la migrazione

Migra con calma e attenzione. Una migrazione affrettata può creare un rischio più immediato del problema che stai cercando di risolvere.

1. **Installa il firmware corretto** del tuo modello prima di generare un seed sostitutivo. Se preferisci, genera il nuovo seed su un **dispositivo di firma non COLDCARD** ([vedi dispositivi supportati]({{< ref "library/supported-hardware-signers" >}})) — in ogni caso, **non** riutilizzare il vecchio seed.
2. Genera un seed completamente nuovo e **registralo**. Prima di depositare fondi, verifica il backup scritto, l'impronta del portafoglio e un indirizzo di ricezione.
3. Usa la procedura guidata di configurazione di Bitcoin-Safe per creare un nuovo [portafoglio a firma singola]({{< ref "library/setup-singlesig-wallet" >}}) o [portafoglio multisignature]({{< ref "library/setup-multisig-wallet" >}}) con il nuovo seed.
4. Completa il test di ricezione e invio della procedura guidata: verifica il backup e un indirizzo di ricezione sul nuovo firmatario, ricevi un piccolo importo di prova e invialo con successo a un altro indirizzo verificato nel nuovo portafoglio.
5. Firma e trasmetti la transazione di migrazione:
   - **Portafoglio a firma singola:** trasmettilo normalmente con una commissione alta così si conferma rapidamente.
   - **Portafoglio multisignature:** non trasmetterlo normalmente, perché così si rivelano le sue chiavi pubbliche nel mempool pubblico. Copia la transazione grezza firmata e inviala direttamente tramite [MARA Slipstream](https://slipstream.mara.com/).
6. Conserva la vecchia COLDCARD e il suo backup fino a quando il **saldo completo** non è arrivato e confermato nel nuovo portafoglio. Solo allora cancella il vecchio seed.

Se la Mk2/Mk3 è il tuo unico dispositivo di firma, installa prima il firmware 4.2.0 o successivo: genera correttamente i seed sostitutivi, quindi non hai bisogno di una COLDCARD più recente per completare la migrazione. Segui gli stessi passaggi, alternando con attenzione tra il vecchio e il nuovo seed sull'unico dispositivo, e conserva il vecchio backup finché la migrazione non è completamente confermata.

## Se usi la multisignature

Se una configurazione multisignature è composta **esclusivamente** da dispositivi interessati, la vulnerabilità si applica comunque. Proteggi la configurazione con un quorum che includa almeno un dispositivo di firma non interessato.

## Aiutare qualcun altro a migrare

Non chiedere mai di condividere, fotografare o digitare le parole seed. Il seed deve rimanere privato e deve essere inserito solo sul dispositivo di firma stesso.
