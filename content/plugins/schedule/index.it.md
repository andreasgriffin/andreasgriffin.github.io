---
title: "Pagamenti programmati"
description: "Pianifica pagamenti Bitcoin una tantum o ricorrenti, controlla quando scadono e prepara le transazioni da verificare in Bitcoin-Safe."
draft: false
tags: ["Plugins"]
images: ["schedule.png"]
weight: 40
faq:
  title: "Domande sui pagamenti programmati"
  items:
    - question: "Posso programmare un pagamento singolo o solo ricorrenti?"
      answer: "Entrambi. Puoi creare un pagamento singolo, un numero fisso di ripetizioni o una pianificazione continua."
    - question: "Con quale frequenza può ripetersi una pianificazione?"
      answer: "Gli intervalli di ripetizione disponibili sono:\n- Minuti, ore o giorni\n- Settimane, facoltativamente in giorni della settimana selezionati\n- Mesi o anni, in date del calendario o con schemi di giorni della settimana"
    - question: "Posso impostare l'importo in valuta fiat?"
      answer: "Sì. Puoi impostare l'importo in:\n- Bitcoin\n- Una valuta fiat supportata\n\nGli importi in fiat possono usare:\n- Un tasso di cambio in tempo reale\n- Il tasso CoinGecko, fissato alle 00:00 GMT\n\nPuoi inoltre impostare una sostituzione del tasso di cambio per il pagamento successivo."
    - question: "Gli indirizzi vengono riutilizzati?"
      answer: "No. Ogni indirizzo del destinatario viene usato una sola volta. Quando gli indirizzi di un destinatario sono esauriti, puoi aggiungerne altri per quel destinatario."
    - question: "Bitcoin-Safe invia i pagamenti automaticamente?"
      answer: "No. Quando un pagamento scade, Schedule prepara la transazione in Bitcoin-Safe per la tua verifica, e tu resti responsabile della sua firma e trasmissione."
    - question: "Posso pagare più destinatari insieme?"
      answer: "Sì. Seleziona diversi pagamenti programmati e clicca su **Paga selezionati**. Bitcoin-Safe li unisce in un'unica transazione batch."
    - question: "Cosa succede se un pagamento è stato fatto in contanti o in altro modo?"
      answer: "Puoi aggiungere un pagamento **fuori banda**. Registra il pagamento nella pianificazione senza una transazione Bitcoin, così l'avanzamento resta accurato."
---

### {{< page-title >}}

<p class="lead">Pianifica i pagamenti in Bitcoin e lascia che Schedule tenga traccia di ciò che scade.</p>

<ul class="plugin-features">
<li>Pagare dipendenti o organizzare altri obblighi ricorrenti</li>
<li>Impostare trasferimenti ricorrenti</li>
<li>Programmare un pagamento unico che non vuoi dimenticare</li>
</ul>

Quando un pagamento scade, Schedule prepara la transazione in Bitcoin-Safe per la tua verifica. Resti tu responsabile della sua firma e trasmissione.

{{< video "schedule.mp4" controls >}}

### Piani di pagamento flessibili

- Scegli un pagamento singolo, un numero fisso di ripetizioni o una pianificazione continua.
- Imposta una data di inizio e un intervallo di ripetizione: minuti, ore, giorni, settimane, mesi o anni. Le pianificazioni settimanali possono usare giorni della settimana selezionati; quelle mensili e annuali supportano date del calendario e schemi di giorni della settimana.
- Imposta destinatario, categoria e importo in bitcoin o in una valuta fiat supportata.
- Per gli importi in fiat, usa un tasso in tempo reale o il tasso CoinGecko fissato alle 00:00 GMT. Per il pagamento successivo puoi impostare una sostituzione del tasso di cambio.
- Le pianificazioni a numero fisso mostrano anteprime dell'importo per pagamento e del totale.

### Preparare i pagamenti nel portafoglio

- Consulta la prossima scadenza e l'avanzamento dei pagamenti; i pagamenti in scadenza sono evidenziati e possono attivare un avviso di Bitcoin-Safe.
- Prepara un pagamento in scadenza o un batch nel compositore di transazioni, con uscite per i destinatari, etichette e categorie già compilate.
- Verifica e personalizza la transazione prima di firmarla e trasmetterla tu stesso.
- Salva destinatari riutilizzabili con un nome e più indirizzi. Schedule può selezionare un indirizzo non utilizzato per un pagamento.

### Seguire e gestire le pianificazioni

- Trova le pianificazioni per stato di scadenza, tipo o categoria. Gli elenchi mostrano date, pagamenti completati, frequenza, destinatario, importo, categoria e totale.
- Controlla i pagamenti effettuati e le prossime occorrenze. Le transazioni del portafoglio corrispondenti possono aggiornare l'avanzamento; puoi anche aggiungere manualmente un pagamento o rieseguire la scansione delle transazioni.
- Modifica una pianificazione prima del primo pagamento registrato, duplicala o eliminala, e importa/esporta le pianificazioni come backup JSON.

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
<summary>Posso programmare un pagamento singolo o solo ricorrenti?</summary>

Entrambi. Puoi creare un pagamento singolo, un numero fisso di ripetizioni o una pianificazione continua.

</details>

<details>
<summary>Con quale frequenza può ripetersi una pianificazione?</summary>

Gli intervalli di ripetizione disponibili sono:

- Minuti, ore o giorni
- Settimane, facoltativamente in giorni della settimana selezionati
- Mesi o anni, in date del calendario o con schemi di giorni della settimana

</details>

<details>
<summary>Posso impostare l'importo in valuta fiat?</summary>

Sì. Puoi impostare l'importo in:

- Bitcoin
- Una valuta fiat supportata

Gli importi in fiat possono usare:

- Un tasso di cambio in tempo reale
- Il tasso CoinGecko, fissato alle 00:00 GMT

Puoi inoltre impostare una sostituzione del tasso di cambio per il pagamento successivo.

</details>

<details>
<summary>Gli indirizzi vengono riutilizzati?</summary>

No. Ogni indirizzo del destinatario viene usato una sola volta. Quando gli indirizzi di un destinatario sono esauriti, puoi aggiungerne altri per quel destinatario.

</details>

<details>
<summary>Bitcoin-Safe invia i pagamenti automaticamente?</summary>

No. Quando un pagamento scade, Schedule prepara la transazione in Bitcoin-Safe per la tua verifica, e tu resti responsabile della sua firma e trasmissione.

</details>

<details>
<summary>Posso pagare più destinatari insieme?</summary>

Sì. Seleziona diversi pagamenti programmati e clicca su **Paga selezionati**. Bitcoin-Safe li unisce in un'unica transazione batch.

</details>

<details>
<summary>Cosa succede se un pagamento è stato fatto in contanti o in altro modo?</summary>

Puoi aggiungere un pagamento **fuori banda**. Registra il pagamento nella pianificazione senza una transazione Bitcoin, così l'avanzamento resta accurato.

</details>
</content>
