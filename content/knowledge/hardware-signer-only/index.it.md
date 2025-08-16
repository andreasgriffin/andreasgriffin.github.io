---
aliases:
  - "/conoscenza/firmatari-hardware-obbligatori/"
title: "Firmatari hardware obbligatori"
description: "Bitcoin Safe impone semi generati solo su hardware nel Mainnet per massimizzare la sicurezza ed evitare i rischi dello storage software delle chiavi. Ecco perché è importante."
draft: false
tags: ["Featured", "Knowledge" ]
keywords: [
  "Bitcoin Safe",
  "wallet hardware",
  "seed software",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "multisig",
  "PSBT",
  "autocustodia",
  "sicurezza Bitcoin",
  "avvelenamento degli indirizzi",
  "strumenti Bitcoin"
]
images: ["logo.png" ]
# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=dbSmQmt0uDI"
weight: 21
---

 

![](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }

## 🚫 Perché Bitcoin Safe blocca i seed software sul Mainnet?

🤔 Non è scomodo?

🔥 In realtà — è un **grande upgrade di sicurezza**.

Bitcoin Safe **consente i seed software solo su Testnet, Signet e Regtest** — mai su Mainnet. Ecco perché:

### ✅ Motivi per cui i seed software sono bloccati su Mainnet

- 🧠 **I seed software sono insicuri** 
  - I computer sono pieni di rischi: hijacker degli appunti, malware, exploit del browser.
  - Un attimo di distrazione e il tuo seed è compromesso — partita finita.
  - Il cold storage non dovrebbe mai nascere “caldo”.

</br>

- 🧊 **Il cold storage deve nascere freddo**
  - Spesso si generano seed in wallet software e poi si migra su hardware.
  - Ma l’esposizione iniziale è già avvenuta — non si torna indietro.
  - Vero cold storage = creato fin dall’inizio su un firmatario hardware.

</br>

- 🎣 **Il phishing prospera sulle abitudini software**
  - Digitare i seed nelle app ti abitua a fidarti di pessimi pattern di UX.
  - L’hardware-only impone abitudini migliori e limita l’esposizione.
  - ✅ Mainnet senza digitare la seed = meno vittime di phishing.

</br>

- 🧪 **Gli sviluppatori mantengono flessibilità**
  - I seed software *sono* permessi su:
    - Testnet
    - Signet
    - Regtest
  - Ideale per i dev. Nessun rischio per i sat reali. 🧡



</br>

- 🔐 **Su Mainnet servono firmatari hardware — senza eccezioni**
  - 🔌 USB, 📷 QR e 💾 SD card con tutti i principali dispositivi
    - [Coldcard]({{< ref "knowledge/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Foundation Passport]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Ledger]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Keystone]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "knowledge/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "knowledge/supported-hardware-signers" >}})
  - [Vedi tutti i firmatari supportati →]({{< ref "knowledge/supported-hardware-signers" >}})


---

## 🛡️ Protezione contro l’avvelenamento degli indirizzi

Bitcoin Safe **colora gli indirizzi di ricezione** per rendere evidente l’avvelenamento degli indirizzi:

- 🟢 Verde = indirizzo di ricezione verificato  
- 🟡 Giallo = indirizzo di resto (change)  

Se qualcuno prova ad avvelenare gli appunti con un indirizzo falso, lo vedrai subito.

![Esempio di rilevamento dell’avvelenamento degli indirizzi](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ Verifica degli indirizzi via USB o QR

Verifica gli indirizzi di ricezione direttamente sul tuo firmatario hardware — senza dover fidarti dello schermo.

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ Istruzioni per ogni firmatario hardware
 
- {{<text-name-with-logo>}} include istruzioni con schermate per ciascun firmatario hardware per guidarti passo dopo passo. 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-hardware-signer-screenshots >}}
    </div>

   
---



## 🤝 Multisig collaborativo semplificato

Bitcoin Safe rende il multisig facile e pronto per i team:

- 🔐 Chat Nostr crittografata  
- 🔁 Condivisione PSBT con 1 clic  
- 🔌 USB, 📷 QR e 💾 SD card

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ Funzioni potenti per tutti

- 🟧 Procedura guidata per wallet a firma singola  
- 🟨 Configurazione multisig 2-di-3  
- 🟩 Qualsiasi configurazione n-di-m  
- 🖨️ Schede di backup PDF stampabili  
- 🔁 Sincronizzazione delle etichette via Nostr  
- 🔍 Diagramma completo dei flussi di denaro e cronologia delle transazioni ricercabile

![Diagramma delle transazioni in Bitcoin Safe](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 Globale e facile da usare

- Supporto multilingue: {{< flags-short >}}
- Funziona su: Windows, macOS & Linux  
- Trascina e rilascia PSBT / CSV  
- Filtri avanzati per transazioni, UTXO, importi e altro

---

## 💡 TL;DR

Bitcoin Safe = veri risparmi in Bitcoin:

✅ Solo hardware su Mainnet  
✅ Nessuna esposizione dei seed software  
✅ Multisig adatto ai principianti  
✅ Ambienti di test adatti agli sviluppatori  
✅ Funzioni per famiglie e team  

🔗 [Bitcoin-Safe.org](https://Bitcoin-Safe.org)  
🎥 Canale YouTube →: https://youtube.com/@BitcoinSafeOrg
