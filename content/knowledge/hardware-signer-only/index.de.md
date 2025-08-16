---
aliases:
  - "/knowledge/nur-hardware-signer/"
title: "Hardware‑Signer erforderlich"
description: "Bitcoin Safe erzwingt auf dem Mainnet ausschließlich Seeds, die auf Hardware erzeugt wurden, um die Sicherheit zu maximieren und die Risiken der softwarebasierten Schlüsselspeicherung zu vermeiden. Warum das wichtig ist."
draft: false
tags: ["Featured", "Knowledge" ]
keywords: [
  "Bitcoin Safe",
  "Hardware‑Wallet",
  "Software‑Seed",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "Multisig",
  "PSBT",
  "Selbstverwahrung",
  "Bitcoin‑Sicherheit",
  "Adressvergiftung",
  "Bitcoin‑Tools"
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

## 🚫 Warum blockiert Bitcoin Safe Software-Seeds im Mainnet?

🤔 Ist das nicht unpraktisch?

🔥 Stellt sich heraus — es ist ein **großes Sicherheits‑Upgrade**.

Bitcoin Safe **erlaubt Software‑Seeds nur auf Testnet, Signet und Regtest** — niemals im Mainnet. Darum:

### ✅ Gründe, warum Software‑Seeds im Mainnet blockiert sind

- 🧠 **Software‑Seeds sind unsicher** 
  - Computer stecken voller Risiken: Zwischenablagen‑Hijacker, Malware, Browser‑Exploits.
  - Ein Fehler, und dein Seed ist kompromittiert — Game over.
  - Cold Storage sollte niemals „heiß“ beginnen.

</br>

- 🧊 **Cold Storage muss kalt geboren werden**
  - Nutzer erzeugen oft Seeds in Software‑Wallets und migrieren später auf Hardware.
  - Aber die anfängliche Offenlegung ist bereits passiert — es gibt kein Zurück.
  - Echte Cold Storage = von Anfang an auf einem Hardware‑Signer erzeugt.

</br>

- 🎣 **Phishing lebt von Software‑Gewohnheiten**
  - Seeds in Apps einzutippen trainiert, schlechten UX‑Mustern zu vertrauen.
  - Nur‑Hardware erzwingt bessere Gewohnheiten und begrenzt die Angriffsfläche.
  - ✅ Seed‑loses Mainnet = weniger Phishing‑Opfer.

</br>

- 🧪 **Entwickler behalten Flexibilität**
  - Software‑Seeds sind *erlaubt* auf:
    - Testnet
    - Signet
    - Regtest
  - Ideal für Devs. Kein Risiko für echte Sats. 🧡



</br>

- 🔐 **Im Mainnet sind Hardware‑Signer Pflicht — ohne Ausnahme**
  - 🔌 USB, 📷 QR und 💾 SD‑Karte mit allen gängigen Geräten
    - [Coldcard]({{< ref "knowledge/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Foundation Passport]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Ledger]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Keystone]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "knowledge/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "knowledge/supported-hardware-signers" >}})
  - [Alle unterstützten Signer →]({{< ref "knowledge/supported-hardware-signers" >}})


---

## 🛡️ Schutz vor Adressvergiftung

Bitcoin Safe **farbmarkiert Empfangsadressen**, um Adressvergiftung sofort sichtbar zu machen:

- 🟢 Grün = verifizierte Empfangsadresse  
- 🟡 Gelb = Wechselgeldadresse  

Wenn jemand versucht, deine Zwischenablage mit einer falschen Adresse zu vergiften, siehst du es sofort.

![Beispiel für Erkennung von Adressvergiftung](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ Adressprüfung per USB oder QR

Prüfe Empfangsadressen direkt auf deinem Hardware‑Signer — du musst dem Bildschirm nicht vertrauen.

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ Anleitungen für jeden Hardware‑Signer
 
- {{<text-name-with-logo>}} enthält bebilderte Schritt‑für‑Schritt‑Anleitungen für jeden Hardware‑Signer und führt dich durch jeden Schritt. 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-hardware-signer-screenshots >}}
    </div>

   
---



## 🤝 Kollaboratives Multisig, ganz einfach

Bitcoin Safe macht Multisig benutzerfreundlich und teamtauglich:

- 🔐 Verschlüsselter Nostr‑Chat  
- 🔁 1‑Klick‑PSBT‑Freigabe  
- 🔌 USB, 📷 QR und 💾 SD‑Karte

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ Leistungsstarke Funktionen für alle

- 🟧 Singlesig‑Wallet‑Assistent  
- 🟨 2‑von‑3‑Multisig‑Setup  
- 🟩 Beliebige n‑von‑m‑Konfiguration  
- 🖨️ Druckbare PDF‑Backup‑Bögen  
- 🔁 Label‑Sync über Nostr  
- 🔍 Vollständiges Geldfluss‑Diagramm & durchsuchbare Transaktionshistorie

![Transaktionsdiagramm in Bitcoin Safe](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 Global und benutzerfreundlich

- Mehrsprachige Unterstützung: {{< flags-short >}}
- Läuft auf: Windows, macOS & Linux  
- Drag‑and‑Drop PSBT / CSV  
- Erweiterte Filter für Transaktionen, UTXOs, Beträge und mehr

---

## 💡 TL;DR

Bitcoin Safe = echte Bitcoin‑Ersparnisse:

✅ Nur Hardware im Mainnet  
✅ Keine Software‑Seed‑Exposition  
✅ Einsteigerfreundliches Multisig  
✅ Entwicklerfreundliche Testumgebungen  
✅ Familien‑ & Team‑taugliche Funktionen  

🔗 [Bitcoin‑Safe.org](https://Bitcoin-Safe.org)  
🎥 YouTube‑Kanal →: https://youtube.com/@BitcoinSafeOrg
