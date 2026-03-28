---
title: "Filtri compatti dei blocchi"
description: "Scopri cosa sono i filtri compatti dei blocchi e come migliorano la privacy rispetto ai server Electrum."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "filtri compatti dei blocchi"
  - "CBF"
  - "privacy"
  - "portafoglio Bitcoin"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**I filtri compatti dei blocchi (CBF)** permettono a [Bitcoin Safe]({{< ref "/" >}}) di analizzare la blockchain senza chiedere a un server Electrum quali indirizzi sono tuoi.

![Bitcoin Safe scarica filtri compatti dei blocchi da diversi peer casuali di Bitcoin Core.](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

Invece di interrogare un server centrale, Bitcoin Safe scarica un piccolo filtro per ogni blocco da peer casuali di Bitcoin Core. Il tuo portafoglio verifica questi filtri localmente e scarica i blocchi completi solo quando serve.

### CBF vs Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">Aspetto</th>
        <th scope="col">Filtri compatti dei blocchi</th>
        <th scope="col">Server Electrum</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Privacy</th>
        <td><span class="text-success fw-semibold">Buono</span> - I dati del portafoglio restano locali</td>
        <td><span class="text-danger fw-semibold">Cattivo</span> - Il server può vedere i tuoi indirizzi e la cronologia</td>
      </tr>
      <tr>
        <th scope="row">Origine dei dati</th>
        <td><span class="text-success fw-semibold">Buono</span> - Peer casuali di Bitcoin Core</td>
        <td><span class="text-warning fw-semibold">Neutro</span> - Un solo server scelto</td>
      </tr>
      <tr>
        <th scope="row">Sincronizzazione iniziale</th>
        <td><span class="text-warning fw-semibold">Neutro</span> - Di solito più lenta</td>
        <td><span class="text-success fw-semibold">Buono</span> - Di solito più veloce</td>
      </tr>
      <tr>
        <th scope="row">Sincronizzazione continua</th>
        <td><span class="text-success fw-semibold">Buono</span> - Molto rapida dopo la prima sincronizzazione</td>
        <td><span class="text-success fw-semibold">Buono</span> - Di solito rapida</td>
      </tr>
      <tr>
        <th scope="row">Ideale per</th>
        <td><span class="text-success fw-semibold">Buono</span> - Utenti attenti alla privacy</td>
        <td><span class="text-success fw-semibold">Buono</span> - L'installazione e il ripristino più rapidi</td>
      </tr>
    </tbody>
  </table>
</div>

### Perché usare CBF

- Più privacy: il tuo portafoglio non chiede mai a un server quali indirizzi sono tuoi.
- Nessun indexer fidato: Bitcoin Safe parla direttamente con la rete Bitcoin.
- Sincronizzazione leggera: i filtri sono piccoli, quindi non serve tutta la blockchain.

### Cosa aspettarsi

- Portafoglio nuovo o ripristino: di solito **5-30 minuti** per la prima sincronizzazione.
- Portafoglio già sincronizzato: si aggiorna **molto rapidamente**, spesso in **meno di 30 secondi**.
- Passaggio da Electrum a CBF: di solito anche **meno di 30 secondi**.

Puoi scegliere con quanti peer si collega Bitcoin Safe. Più peer migliorano la ridondanza, ma di solito aumentano banda e tempo di sincronizzazione. Il valore predefinito è **2** peer.

### Transazioni non confermate

CBF copre solo i **blocchi confermati**. Per ricevere anche avvisi sui pagamenti non confermati, lascia [Notifiche istantanee sulle transazioni]({{< ref "knowledge/instant-transactions-notifications/" >}}) attive, che è il comportamento predefinito.

### Nota tecnica

I filtri compatti dei blocchi sono definiti nel [BIP158](https://bips.dev/158/). Bitcoin Safe usa il modulo open-source [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto).

Puoi anche usare il tuo nodo Bitcoin Core come peer iniziale nelle impostazioni di _Bitcoin network monitoring_.

![Impostazione del nodo iniziale](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
