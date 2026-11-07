---
title: "Sync & Chat"
description: "Trova i peer del tuo portafoglio, sincronizza etichette e categorie, chatta in sicurezza e condividi le PSBT con un clic."
draft: false
tags: ["Plugins", "sync-chat-mainpage"]
images: ["logo.png"]
weight: 30
faq:
  title: "Domande su Sync & Chat"
  items:
    - question: "Come fanno i dispositivi a trovarsi?"
      answer: "Sync & Chat cerca altri dispositivi che usano lo stesso descrittore del portafoglio. Il descrittore viene sottoposto ad hash prima di essere usato per la ricerca, quindi non viene esposto in chiaro. Inoltre, ogni dispositivo trovato deve essere aggiunto e considerato attendibile manualmente prima di poter partecipare alla chat. In questo modo la chat resta sicura anche se il descrittore non è segreto."
    - question: "Come funziona la collaborazione in pratica?"
      answer: "1. Configurazione (una sola volta): aggiungi e considera attendibile il dispositivo di ciascun partecipante.\n2. Creazione: un partecipante crea una PSBT e aggiunge la propria firma.\n3. Condivisione: la PSBT viene inviata a tutti i partecipanti, o solo ad alcuni selezionati.\n4. Firma: ogni partecipante aggiunge la propria firma finché la transazione non è completamente firmata.\n5. Trasmissione: l'ultimo firmatario trasmette la transazione, che poi compare nel portafoglio di tutti i partecipanti."
    - question: "Cosa viene sincronizzato?"
      answer: "Sync & Chat gestisce:\n- Categorie ed etichette delle monete, sincronizzate tra i firmatari, anche tra sistemi operativi diversi\n- La condivisione delle PSBT con un clic"
    - question: "La chat è privata?"
      answer: "Sì. La chat del portafoglio è cifrata e funziona tramite Nostr; anche i backup delle etichette sono memorizzati cifrati tramite Nostr."
---

### {{< page-title >}}

<p class="lead">Coordina i firmatari multisig e mantieni sincronizzato il contesto del portafoglio direttamente da Bitcoin-Safe.</p>

<ul class="plugin-features">
<li>Trova altri dispositivi che usano lo stesso descrittore del portafoglio</li>
<li>Sincronizza etichette e categorie tra i firmatari</li>
<li>Chatta in sicurezza e condividi le PSBT con un clic</li>
</ul>

### Sincronizzazione delle etichette

{{< video src="../../library/label-sync/label-sync.mp4" controls="true" >}}

### Firma collaborativa

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

Per la guida completa alla firma collaborativa multisig, vedi [Collaborazione in un multisig]({{< ref "library/collaboration/" >}}).

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">Scarica Bitcoin-Safe</h2>
<p class="text-muted mb-3">I plugin sono inclusi in Bitcoin-Safe. Scarica l'app per provarli.</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">Scarica Bitcoin-Safe</a>
<small class="text-muted">Software libero e open source · Windows, macOS, Linux</small>
</div>
</section>

### Domande frequenti

<details>
<summary>Come fanno i dispositivi a trovarsi?</summary>

Sync & Chat cerca altri dispositivi che usano lo stesso descrittore del portafoglio. Il descrittore viene sottoposto ad hash prima di essere usato per la ricerca, quindi non viene esposto in chiaro. Inoltre, ogni dispositivo trovato deve essere aggiunto e considerato attendibile manualmente prima di poter partecipare alla chat. In questo modo la chat resta sicura anche se il descrittore non è segreto.

</details>

<details>
<summary>Come funziona la collaborazione in pratica?</summary>

1. **Configurazione (una sola volta):** aggiungi e considera attendibile il dispositivo di ciascun partecipante.
2. **Creazione:** un partecipante crea una PSBT e aggiunge la propria firma.
3. **Condivisione:** la PSBT viene inviata a tutti i partecipanti, o solo ad alcuni selezionati.
4. **Firma:** ogni partecipante aggiunge la propria firma finché la transazione non è completamente firmata.
5. **Trasmissione:** l'ultimo firmatario trasmette la transazione, che poi compare nel portafoglio di tutti i partecipanti.

</details>

<details>
<summary>Cosa viene sincronizzato?</summary>

Sync & Chat gestisce:

- Categorie ed etichette delle monete, sincronizzate tra i firmatari, anche tra sistemi operativi diversi
- La condivisione delle PSBT con un clic

</details>

<details>
<summary>La chat è privata?</summary>

Sì. La chat del portafoglio è cifrata e funziona tramite Nostr; anche i backup delle etichette sono memorizzati cifrati tramite Nostr.

</details>

{{< sync-page-box >}}
</content>
