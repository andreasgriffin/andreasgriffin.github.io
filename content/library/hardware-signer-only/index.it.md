---
aliases:
  - "/it/knowledge/hardware-signer-only/"
title: "Firmatori hardware obbligatori"
description: "Bitcoin-Safe impone seed esclusivamente su hardware su Mainnet per massimizzare la sicurezza ed evitare i rischi dell'archiviazione delle chiavi via software. Ecco perché questo è importante."
draft: false
bucket: knowledge
tags: ["Featured"]
keywords: [
  "Bitcoin-Safe",
  "portafoglio hardware",
  "seed software",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "multisig",
  "PSBT",
  "custodia autonoma",
  "sicurezza di Bitcoin",
  "avvelenamento degli indirizzi",
  "strumenti per Bitcoin"
]
images: ["logo.png" ]
# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=dbSmQmt0uDI"
weight: 21
---


![Bitcoin-Safe logo](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }

## 🚫 Perché Bitcoin-Safe blocca i seed software su Mainnet?

🤔 Non è scomodo?

🔥 In realtà — è un **importante aggiornamento di sicurezza**.

Bitcoin-Safe **consente seed software solo su Testnet, Signet e Regtest** — mai su Mainnet. Ecco perché:

### ✅ Motivi per cui i seed software sono bloccati su Mainnet

- 🧠 **I seed software non sono sicuri**
  - I computer sono pieni di rischi: hijacker degli appunti, malware, exploit del browser.
  - Un solo errore e il tuo seed è compromesso — è la fine.
  - Lo storage freddo non dovrebbe mai iniziare da una condizione “calda”.

</br>

- 🧊 **Lo storage freddo deve nascere freddo**
  - Spesso gli utenti generano seed in portafogli software e poi migrano su hardware.
  - Ma l'esposizione iniziale è già avvenuta — non si può tornare indietro.
  - Vero cold storage = creato su un firmatore hardware fin dall'inizio.

</br>

- 🎣 **Il phishing prospera sulle abitudini software**
  - Digitare i seed nelle app ti abitua a fidarti di pattern di UX pericolosi.
  - L'obbligo hardware favorisce abitudini migliori e limita l'esposizione.
  - ✅ Mainnet senza seed = meno vittime di phishing.

</br>

- 🧪 **Gli sviluppatori mantengono flessibilità**
  - I seed software *sono* consentiti su:
    - Testnet
    - Signet
    - Regtest
  - Ideale per gli sviluppatori. Nessun rischio per i sats reali. 🧡



</br>


- 🔐 **Mainnet richiede firmatori hardware — nessuna eccezione**
  - 🔌 USB, 📷 QR e 💾 scheda SD con tutti i principali dispositivi
    - [Coldcard]({{< ref "library/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "library/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "library/supported-hardware-signers" >}})
    - [Foundation Passport Core]({{< ref "library/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "library/supported-hardware-signers" >}})
    - [Ledger]({{< ref "library/supported-hardware-signers" >}})
    - [Keystone]({{< ref "library/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "library/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "library/supported-hardware-signers" >}})
  - [Visualizza tutti i firmatori supportati →]({{< ref "library/supported-hardware-signers" >}})


---

## 🛡️ Protezione contro l'avvelenamento degli indirizzi

Bitcoin-Safe **colora gli indirizzi di ricezione** per rendere evidente l'avvelenamento degli indirizzi:

- 🟢 Verde = indirizzo di ricezione verificato  
- 🟡 Giallo = indirizzo di cambio  

Se qualcuno prova a infettare i tuoi appunti con un indirizzo falso, lo vedrai all'istante.

![Address poisoning detection example](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ Verifica degli indirizzi via USB o QR

Verifica gli indirizzi di ricezione direttamente sul tuo firmatore hardware — non c'è bisogno di fidarsi dello schermo dell'app.

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ Istruzioni per ogni firmatore hardware
 
- {{<text-name-with-logo>}} include istruzioni con screenshot per ogni firmatore hardware per guidarti in ogni passaggio 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-images >}}
    </div>

   
---



## 🤝 Multisig collaborativo semplificato

Bitcoin-Safe rende il multisig facile da usare e adatto al lavoro di squadra:

- 🔐 Chat Nostr cifrata  
- 🔁 Condivisione PSBT con un clic  
- 🔌 USB, 📷 QR e 💾 scheda SD

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ Funzionalità potenti per tutti gli utenti

- 🟧 Procedura guidata per portafogli singlesig  
- 🟨 Configurazione multisig 2-su-3  
- 🟩 Qualsiasi configurazione n-su-m  
- 🖨️ Fogli di backup PDF stampabili  
- 🔁 Sincronizzazione etichette via Nostr  
- 🔍 Diagramma completo dei flussi di denaro e cronologia transazioni ricercabile

![Transaction diagram in Bitcoin-Safe](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 Globale e facile da usare

- Supporto multilingue: {{< flags-short >}}
- Funziona su: Windows, macOS & Linux  
- Trascina e rilascia PSBT / CSV  
- Filtri avanzati per transazioni, UTXO, importi e altro

---

## 💡 In sintesi

Bitcoin-Safe = vero risparmio in Bitcoin:

✅ Solo hardware su Mainnet  
✅ Nessuna esposizione del seed software  
✅ Multisig adatto ai principianti  
✅ Ambienti di test per sviluppatori  
✅ Funzionalità pronte per famiglia e team  

🔗 [Bitcoin-Safe.org]({{< ref "/" >}})  
🎥 Canale YouTube →: https://youtube.com/@BitcoinSafeOrg