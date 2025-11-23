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


Bitcoin Safe   1.6.0 introduce i **Filtri compatti dei blocchi (CBF)** come metodo opzionale per sincronizzare il tuo portafoglio. Invece di interrogare un server Electrum centralizzato per la cronologia del portafoglio, Bitcoin Safe può ora scaricare un piccolo file di riepilogo per ogni blocco direttamente da peer casuali di Bitcoin Core. Questi riepiloghi funzionano come una breve lista di controllo che permette al tuo portafoglio di decidere autonomamente se un blocco potrebbe contenere una delle tue transazioni.

Poiché Bitcoin Safe prende la decisione localmente, nessun server di terze parti viene mai a sapere quali indirizzi o transazioni ti interessano. Ottieni gli stessi dati di conferma che un nodo completo conserverebbe, ma in un formato più leggero adatto ai dispositivi di tutti i giorni.

**Perché è migliore:**

- 📦 **Download ridotti:** Ogni filtro è di soli pochi kilobyte, quindi puoi sincronizzare tramite normali connessioni domestiche senza memorizzare l'intera blockchain.
- 🔐 **Diretto dalla rete:** Bitcoin Safe parla con più nodi Bitcoin Core casuali, proprio come fanno gli altri nodi, riducendo la possibilità che un singolo osservatore possa profilarti.
- 🕵️ **Corrispondenza locale:** Il tuo portafoglio verifica i filtri localmente. Se un filtro sembra rilevante, solo allora scarica il blocco specifico, mantenendo privati i tuoi indirizzi.

I server Electrum, al contrario, cercano nella blockchain per conto tuo. Ogni richiesta condivide con l'operatore del server gli indirizzi del tuo portafoglio, che potrebbe registrarli. Con i filtri compatti dei blocchi, Bitcoin Safe scarica gli stessi dati neutrali che ogni nodo condivide. Nessuno può dire quali indirizzi ti appartengono perché il tuo portafoglio non li rivela in primo luogo.

Qui sotto c'è una vista semplice di come Bitcoin Safe si connette quando CBF è abilitato. Nota come rispecchia il modo in cui i nodi Bitcoin Core già comunicano tra loro:


![Bitcoin Safe scarica filtri compatti dei blocchi da diversi peer casuali di Bitcoin Core.](logo.jpg)
{ .img-fluid .mb-5   style="max-width: 450px;" }


Puoi scegliere a quanti peer Bitcoin Safe deve connettersi. Più peer richiedono maggiore larghezza di banda e comportano un tempo di sincronizzazione più lento. Il valore predefinito è 2.  

 
### Cosa aspettarsi durante la sincronizzazione

I filtri compatti influenzano i tempi di attesa a seconda di quello che stai facendo:

1. ✨ **Creare o recuperare un portafoglio:** Che tu crei un nuovo portafoglio o ne recuperi uno esistente, la sincronizzazione iniziale scarica i filtri per l'intera storia del portafoglio. Aspettati che questo processo una tantum duri **tra i 5 e i 30 minuti**, in base alla velocità della tua connessione internet.
2. 🚀 **Aprire un portafoglio già sincronizzato:** Bitcoin Safe deve scaricare solo i filtri più recenti dall'ultima sessione. Il recupero solitamente termina in **meno di 30 secondi**.
3. 🔄 **Passare dai server Electrum ai CBF:** Poiché il portafoglio era precedentemente sincronizzato con server Electrum, Bitcoin Safe deve scaricare solo i filtri più recenti, il che di solito richiede **meno di 30 secondi**.

### Rimani informato sui pagamenti non confermati

I filtri compatti dei blocchi coprono solo i **blocchi confermati**. Per essere avvisato delle transazioni in arrivo prima che vengano confermate, assicurati di abilitare anche [Notifiche istantanee sulle transazioni]({{< ref "knowledge/instant-transactions-notifications/" >}}). Questa funzione ascolta i messaggi peer-to-peer in tempo reale da un nodo Bitcoin casuale, così puoi reagire all'attività del mempool senza rinunciare alla privacy.


<br>
<br>



### Dettagli tecnici


- *Per gli sviluppatori che vogliono approfondire:* i filtri compatti dei blocchi seguono la [specifica BIP158](https://bips.dev/158/) e sono analizzati nella panoramica di Elle Mouton sugli insiemi codificati con Golomb (Golomb-coded sets) https://ellemouton.com/posts/bip158/. L'implementazione di Bitcoin Safe si basa sul modulo open-source [Kyoto compact block filter per BDK](https://github.com/2140-dev/kyoto).
- Puoi aggiungere il tuo nodo Bitcoin Core ai peer per la sincronizzazione dei Filtri compatti dei blocchi, scegliendo il _nodo iniziale_ del _monitoraggio della rete Bitcoin_.


![](inital-node.png)
{ .img-fluid .mb-5   style="max-width: 414px;" }