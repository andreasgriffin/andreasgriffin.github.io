---
aliases:
  - "/it/features/reproducibility-and-security/"
title: "Sicurezza e riproducibilita"
description: "Bitcoin Safe segue standard elevati per la sicurezza dei binari: build riproducibili, commit firmati, release firmate e monitoraggio esterno indipendente."
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

![Output di build riproducibili per Bitcoin Safe](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 500px;" }

Abbiamo implementato diversi livelli di protezione per l'integrita dei download sul sito, in modo che l'app che scarichi corrisponda davvero al codice sorgente pubblico:

- **Build riproducibili**: Le build Linux `deb`, `AppImage` e `Flatpak`, oltre ai file Windows `portable exe` e `setup exe`, possono essere riprodotte byte per byte. Se un file ricostruito coincide esattamente, e una forte evidenza che il binario sia stato creato dallo stesso codice sorgente.
- **Cronologia del repository firmata**: Il [repository GitHub di Bitcoin Safe](https://github.com/andreasgriffin/bitcoin-safe/commits/main) pubblica commit firmati e verificati, cosi i revisori possono controllare chi ha prodotto il codice incluso in una release.
- **Binari firmati**: I file di release sono firmati con la [chiave pubblica PGP]({{< gpg_key_link >}}) di Bitcoin Safe, e i binari Windows seguono anche la [policy di code signing]({{< ref "code-signing-policy" >}}).
- **Verifiche indipendenti di riproducibilita**: [WalletScrutiny](https://walletscrutiny.com/desktop/bitcoin.safe/) segue Bitcoin Safe in modo indipendente e mostra lo stato di verifica riproducibile delle release desktop.
- **Monitoraggio continuo delle firme**: [BinaryWatch](https://binarywatch.org/) controlla regolarmente i file di release di Bitcoin Safe e se le loro firme continuano a validare contro la [chiave pubblica PGP]({{< gpg_key_link >}}) di Bitcoin Safe.
- **Verifica degli aggiornamenti**: Gli aggiornamenti vengono mostrati in Bitcoin Safe e la loro firma viene verificata automaticamente.

Nel complesso, queste misure collocano Bitcoin Safe in un piccolo gruppo di progetti che trattano la sicurezza dei binari come una parte fondamentale della sicurezza dell'utente, non come un'aggiunta secondaria.

### La sicurezza e il criterio centrale in ogni aspetto di Bitcoin Safe

Oltre all'integrita dei binari, Bitcoin Safe e progettato con impostazioni predefinite sicure, buone pratiche operative e una guida chiara per l'utente. Alcuni esempi:

- **Custodia incentrata sull'hardware**: Bitcoin Safe richiede [firmatari hardware]({{< ref "library/supported-hardware-signers" >}}), cosi i seed restano su dispositivi dedicati invece di diventare segreti esposti su un computer generico.
- **Flusso di configurazione piu sicuro**: La procedura guidata di configurazione aiuta a creare wallet davvero pronti all'uso reale, includendo test dei [firmatari hardware]({{< ref "library/supported-hardware-signers" >}}), [schede PDF di backup]({{< ref "library/pdf-export/" >}}) e indicazioni su come conservare firmatari hardware e backup dei seed.
- **Verifica degli indirizzi di ricezione**: Bitcoin Safe rende semplice [verificare gli indirizzi di ricezione]({{< ref "library/verify-receive-address/" >}}) sul firmatario stesso prima di condividerli.
- **Rilevamento dell'address poisoning**: Avvisa in presenza di [indirizzi sospetti simili]({{< ref "library/address-poisoning/" >}}).
- **Sicurezza multisig**: Bitcoin Safe supporta wallet multisignature, cosi importi piu grandi possono essere protetti da piu dispositivi o persone invece che da un unico punto di guasto.
- **Collaborazione che rende il multisig piu semplice**: Bitcoin Safe rende pratica la [collaborazione multisignature]({{< ref "library/collaboration/" >}}), cosi coordinare configurazione e firma diventa molto piu facile nell'uso reale.
- **Flussi di firma chiari**: Schermate di firma specifiche per dispositivo riducono la confusione durante la revisione dei PSBT e aiutano gli utenti a compiere l'azione giusta sul firmatario giusto.
