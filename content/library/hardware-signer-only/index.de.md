---
aliases:
  - "/de/knowledge/hardware-signer-only/"
title: "Hardware-Signer erforderlich"
description: "Bitcoin Safe erzwingt hardwarebasierte Seeds auf dem Mainnet, um die Sicherheit zu maximieren und die Risiken softwarebasierter Schlüsselverwaltung zu vermeiden. Daher ist das wichtig."
draft: false
bucket: knowledge
tags: ["Featured"]
keywords: [
  "Bitcoin Safe",
  "Hardware-Wallet",
  "Software-Seed",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "Multisig",
  "PSBT",
  "Selbstverwahrung",
  "Bitcoin-Sicherheit",
  "Adressvergiftung",
  "Bitcoin-Tools"
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

## 🚫 Warum blockiert Bitcoin Safe Software-Seeds auf dem Mainnet?

🤔 Ist das nicht unpraktisch?

🔥 Überraschung — es ist ein **großes Sicherheits-Upgrade**.

Bitcoin Safe **erlaubt Software-Seeds nur auf Testnet, Signet und Regtest** — niemals auf dem Mainnet. Hier ist warum:

### ✅ Gründe, warum Software-Seeds auf dem Mainnet blockiert werden

- 🧠 **Software-Seeds sind unsicher**
  - Computer bergen viele Risiken: Zwischenablage-Hijacker, Malware, Browser-Exploits.
  - Ein Fehler, und dein Seed ist kompromittiert — das Spiel ist vorbei.
  - Cold Storage sollte niemals heiß beginnen.

</br>

- 🧊 **Cold Storage muss kalt entstehen**
  - Benutzer erzeugen oft Seeds in Software-Wallets und migrieren dann zu Hardware.
  - Aber die erste Exposition hat bereits stattgefunden — das lässt sich nicht rückgängig machen.
  - Echte Cold Storage = von Anfang an auf einem Hardware-Signer erstellt.

</br>

- 🎣 **Phishing lebt von Software-Gewohnheiten**
  - Seeds in Apps einzutippen trainiert dich, schlechten UX-Mustern zu vertrauen.
  - Hardware-only erzwingt bessere Gewohnheiten und reduziert die Exposition.
  - ✅ Mainnet ohne Seeds = weniger Phishing-Opfer.

</br>

- 🧪 **Entwickler behalten trotzdem Flexibilität**
  - Software-Seeds *sind* erlaubt auf:
    - Testnet
    - Signet
    - Regtest
  - Ideal für Entwickler. Kein Risiko für echte Sats. 🧡



</br>


- 🔐 **Mainnet verlangt Hardware-Signer — keine Ausnahmen**
  - 🔌 USB, 📷 QR und 💾 SD-Karte mit allen großen Geräten
    - [Coldcard]({{< ref "library/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "library/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "library/supported-hardware-signers" >}})
    - [Foundation Passport Core]({{< ref "library/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "library/supported-hardware-signers" >}})
    - [Ledger]({{< ref "library/supported-hardware-signers" >}})
    - [Keystone]({{< ref "library/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "library/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "library/supported-hardware-signers" >}})
  - [Alle unterstützten Signer anzeigen →]({{< ref "library/supported-hardware-signers" >}})


---

## 🛡️ Schutz vor Adressvergiftung

Bitcoin Safe **färbt Empfangsadressen ein**, damit Adressvergiftung sofort auffällt:

- 🟢 Grün = verifizierte Empfangsadresse  
- 🟡 Gelb = Change-Adresse  

Wenn jemand versucht, deine Zwischenablage mit einer gefälschten Adresse zu vergiften, siehst du es sofort.

![Address poisoning detection example](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ Adressverifikation per USB oder QR

Überprüfe Empfangsadressen direkt auf deinem Hardware-Signer — du musst dem Bildschirm nicht vertrauen.

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ Anleitungen für jeden Hardware-Signer
 
- {{<text-name-with-logo>}} enthält schrittweise Screenshot-Anleitungen für jeden Hardware-Signer, die dich durch jeden Schritt führen 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-images >}}
    </div>

   
---



## 🤝 Gemeinsame Multisig-Nutzung leicht gemacht

Bitcoin Safe macht Multisig benutzerfreundlich und teamtauglich:

- 🔐 Verschlüsselter Nostr-Chat  
- 🔁 PSBT-Teilen mit einem Klick  
- 🔌 USB, 📷 QR und 💾 SD-Karte

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ Leistungsstarke Funktionen für alle Nutzer

- 🟧 Singlesig-Wallet-Assistent  
- 🟨 2-von-3 Multisig-Einrichtung  
- 🟩 Beliebige n-von-m-Konfiguration  
- 🖨️ Druckbare PDF-Sicherungsblätter  
- 🔁 Label-Synchronisation via Nostr  
- 🔍 Vollständiges Geldflussdiagramm & durchsuchbare Transaktionshistorie

![Transaction diagram in Bitcoin Safe](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 Global und benutzerfreundlich

- Mehrsprachige Unterstützung: {{< flags-short >}}
- Funktioniert auf: Windows, macOS & Linux  
- Drag-and-drop für PSBT / CSV  
- Erweiterte Filter für Transaktionen, UTXOs, Beträge und mehr

---

## 💡 Kurzfassung

Bitcoin Safe = echte Bitcoin-Ersparnisse:

✅ Nur Hardware auf dem Mainnet  
✅ Keine Exposition von Software-Seeds  
✅ Einsteigerfreundliches Multisig  
✅ Entwicklerfreundliche Testumgebungen  
✅ Familien- & Team-fähige Funktionen  

🔗 [Bitcoin-Safe.org]({{< ref "/" >}})  
🎥 YouTube-Kanal →: https://youtube.com/@BitcoinSafeOrg