---
aliases:
  - "/ca/knowledge/hardware-signer-only/"
title: "Signants de maquinari obligatoris"
description: "Bitcoin Safe exigeix llavors exclusivament de maquinari a la Mainnet per maximitzar la seguretat i evitar els riscos de l'emmagatzematge de claus en programari. Per això és important."
draft: false
bucket: knowledge
tags: ["Featured"]
keywords: [
  "Bitcoin Safe",
  "cartera de maquinari",
  "llavor de programari",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "multisig",
  "PSBT",
  "autocustòdia",
  "seguretat de Bitcoin",
  "enverinament d'adreces",
  "eines Bitcoin"
]
images: ["logo.png" ]
# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=dbSmQmt0uDI"
weight: 21
---

 

![Bitcoin Safe logo](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }

## 🚫 Per què Bitcoin Safe bloqueja les llavors de programari a la Mainnet?

🤔 No és incòmode?

🔥 Resulta que — és una **millora important de seguretat**.

Bitcoin Safe **només permet llavors de programari a Testnet, Signet i Regtest** — mai a la Mainnet. Així és per què:

### ✅ Raons per les quals les llavors de programari estan bloquejades a la Mainnet

- 🧠 **Les llavors de programari no són segures** 
  - Els ordinadors estan plens de riscos: segrestadors del porta-retalls, malware, vulnerabilitats del navegador.
  - Una única errada i la teva llavor queda compromesa — joc acabat.
  - L'emmagatzematge en fred mai no ha d'arrencar en calent.

</br>

- 🧊 **L'emmagatzematge en fred ha de néixer fred**
  - Els usuaris sovint generen llavors en carteres de programari i després les migren a maquinari.
  - Però l'exposició inicial ja ha passat — no hi ha marxa enrere.
  - Emmagatzematge veritablement en fred = creat en un signant de maquinari des del primer moment.

</br>

- 🎣 **El phishing prospera amb els hàbits de programari**
  - Escriure llavors en aplicacions t'ensenya a confiar en mals patrons d'UX.
  - L'exigència de maquinari obliga a millors hàbits i limita l'exposició.
  - ✅ Mainnet sense llavors = menys víctimes de phishing.

</br>

- 🧪 **Els desenvolupadors encara tenen flexibilitat**
  - Les llavors de programari *sí* estan permeses a:
    - Testnet
    - Signet
    - Regtest
  - Ideal per a desenvolupadors. Cap risc per als sats reals. 🧡



</br>


- 🔐 **La Mainnet requereix signants de maquinari — sense excepcions**
  - 🔌 USB, 📷 QR i 💾 targeta SD amb tots els dispositius principals
    - [Coldcard]({{< ref "library/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "library/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "library/supported-hardware-signers" >}})
    - [Foundation Passport Core]({{< ref "library/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "library/supported-hardware-signers" >}})
    - [Ledger]({{< ref "library/supported-hardware-signers" >}})
    - [Keystone]({{< ref "library/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "library/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "library/supported-hardware-signers" >}})
  - [Veure tots els signants compatibles →]({{< ref "library/supported-hardware-signers" >}})


---

## 🛡️ Protecció contra l'enverinament d'adreces

Bitcoin Safe **codifica amb colors les adreces de recepció** per fer evident l'enverinament d'adreces:

- 🟢 Verd = adreça de recepció verificada  
- 🟡 Groc = adreça de canvi  

Si algú intenta enverinar el teu porta-retalls amb una adreça falsa, ho veuràs al moment.

![Exemple de detecció d'enverinament d'adreces](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ Verificació d'adreces via USB o QR

Verifica les adreces de recepció directament al teu signant de maquinari — no cal confiar en la pantalla.

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ Instruccions per a cada signant de maquinari
 
- {{<text-name-with-logo>}} inclou captures de pantalla i instruccions per a cada signant de maquinari per guiar-te a cada pas 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-images >}}
    </div>

   
---



## 🤝 Multisig col·laboratiu fàcil

Bitcoin Safe fa que el multisig sigui fàcil d'usar i apte per a equips:

- 🔐 Xat Nostr xifrat  
- 🔁 Compartir PSBT amb 1 clic  
- 🔌 USB, 📷 QR i 💾 targeta SD

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ Funcions potents per a tots els usuaris

- 🟧 Assistent per a carteres singlesig  
- 🟨 Configuració multisig 2-de-3  
- 🟩 Qualsevol configuració n-de-m  
- 🖨️ Fulls de còpia de seguretat PDF imprimibles  
- 🔁 Sincronització d'etiquetes via Nostr  
- 🔍 Diagrama complet del flux de diners i historial de transaccions amb cerca

![Diagrama de transaccions a Bitcoin Safe](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 Global i fàcil d'usar

- Suport multilingüe: {{< flags-short >}}
- Funciona a: Windows, macOS i Linux  
- Arrossegar i deixar PSBT / CSV  
- Filtres avançats per a transaccions, UTXOs, importos i més

---

## 💡 Resum

Bitcoin Safe = Estalvis reals en Bitcoin:

✅ Maquinari obligatori a la Mainnet  
✅ Cap exposició de llavors de programari  
✅ Multisig accessible per a principiants  
✅ Entorns de prova aptes per a desenvolupadors  
✅ Funcions preparades per a família i equips  

🔗 [Bitcoin-Safe.org]({{< ref "/" >}})  
🎥 Canal de YouTube →: https://youtube.com/@BitcoinSafeOrg