---
title: "Seed COLDCARD non sicuro"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "Guida minima per spostare i fondi da un seed generato su un dispositivo Coinkite."
---

[Coinkite ha reso nota una debolezza nella generazione dei seed sui firmware COLDCARD interessati](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). Consulta anche [l'analisi tecnica di Block sul fallback prevedibile dell'RNG e sul reseed a 32 bit](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware). L'aggiornamento del firmware non corregge un seed esistente.

**Se hai creato un seed con qualsiasi prodotto Coinkite, migra PRESTO!**

## Lista di controllo per la migrazione

1. Genera un seed completamente nuovo su un **dispositivo di firma diverso da COLDCARD** ([vedi i dispositivi supportati]({{< ref "library/supported-hardware-signers" >}})). Non riutilizzare il vecchio seed. Usa quindi quel signer con la procedura guidata di Bitcoin-Safe per creare un nuovo [wallet a firma singola]({{< ref "library/setup-singlesig-wallet" >}}) o [wallet multifirma]({{< ref "library/setup-multisig-wallet" >}}).
   - Se non è disponibile alcun hardware signer diverso da COLDCARD, [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}}) è un'opzione su un dispositivo Android dedicato, ripristinato alle impostazioni di fabbrica, mantenuto offline e usato esclusivamente per firmare.
   - Completa il test di ricezione e invio della procedura guidata per assicurarti che il nuovo wallet sia configurato correttamente: verifica il backup e un indirizzo di ricezione sul nuovo signer, ricevi un piccolo importo di prova ed esegui con successo un auto-invio verso un altro indirizzo verificato del nuovo wallet.
2. Firma la transazione di migrazione:
   - **Se il wallet interessato è a firma singola:** trasmettila normalmente con una commissione alta affinché venga confermata rapidamente.
   - **Se il wallet interessato è multifirma:** non trasmetterla normalmente, perché ciò rivela le sue chiavi pubbliche nella mempool pubblica. Copia la transazione grezza firmata e inviala direttamente tramite [MARA Slipstream](https://slipstream.mara.com/).
3. Conserva il vecchio COLDCARD finché l'intero saldo non è arrivato ed è stato confermato nel nuovo wallet, quindi aggiornalo al firmware più recente.

Se stai aiutando qualcuno a migrare, non chiedergli mai di condividere, fotografare o digitare le parole del seed. Il seed deve rimanere privato ed essere inserito solo sul dispositivo di firma.
