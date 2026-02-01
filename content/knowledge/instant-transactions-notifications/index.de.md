---
title: "Sofortige Transaktionsbenachrichtigungen"
description: "Wie Bitcoin Safe sofortige Transaktionsbenachrichtigungen empfängt"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [
  "sichere Bitcoin-Wallet für Familien",
  "Bitcoin",
  "Bitcoin-Sparen",
  "Hardware-Signer",
  "Bitcoin-Verwahrer",
  "Finanzberater",
  "Bitcoin-Wallet",
  "Trezor",
  "Bitcoin USA",
  "BTC",
  "HODL",
  "Bitcoin-Sicherheit",
  "Sofortige Transaktionsbenachrichtigungen"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---



![](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }


### {{< page-title >}}  
 
  


**Bitcoin Safe** (ab Version **1.5.0**) unterstützt sofortige Benachrichtigungen über eingehende Bitcoin-Transaktionen, die für Ihre Wallet relevant sind. So funktioniert es unter der Haube:




##### 1. 📡 Abhören des Bitcoin P2P-Netzwerks

Bitcoin Safe verbindet sich direkt mit einem oder mehreren **Bitcoin Core-Knoten**, die am globalen **Peer-to-Peer (P2P)**-Netzwerk teilnehmen. Diese Knoten tauschen kontinuierlich neu verbreitete Transaktionen aus, die für die Aufnahme in den **Mempool** bestimmt sind.

Bitcoin Safe lauscht passiv auf diese Broadcast-Nachrichten und prüft, ob:

* eine Transaktion **Adressen** oder **UTXOs** aus Ihrer Wallet betrifft.

✅ **Datenschutzfreundlich**
Diese Methode ist **vollkommen privat**. Sie **enthüllt nichts** über Ihre Wallet nach außen.
Bitcoin Safe verhält sich wie ein normaler Bitcoin Core-Knoten: Es hört nur den öffentlichen P2P-Verkehr — es gibt niemals spezifische Anfragen oder Ankündigungen, die Ihre Wallet betreffen.



##### 2. 🧠 Treffer — Was passiert als Nächstes?

Falls eine übereinstimmende Transaktion gefunden wird, reagiert Bitcoin Safe unterschiedlich, abhängig vom verwendeten Backend:

###### Option A: ⚡ Electrum- oder Esplora-Backend

* Bitcoin Safe wird einen **Hintergrund-Sync auslösen**, um die vollständige Transaktion und den Wallet-Zustand vom Server abzurufen.

###### Option B: 🔍 Compact Block Filters (Neutrino-Modus)

* Die Wallet wird die **unbestätigte Transaktion direkt** zu Ihren lokalen Wallet-Daten hinzufügen — keine weitere Abfrage erforderlich.



#### ⚙️ Opt-In / Opt-Out-Verhalten

Um Nutzerpräferenzen und Datenschutzeinstellungen zu respektieren:

* 🔒 **Für bestehende Nutzer**, die auf Version 1.5.0 oder neuer aktualisieren, ist diese Funktion **standardmäßig opt-in** — sie kann manuell in den Netzwerkeinstellungen aktiviert werden.
* 🚀 **Für neue Nutzer** ist diese Funktion **standardmäßig aktiviert (opt-out)**, da sie sowohl **datenschutzfreundlich** als auch **sehr nützlich** ist, um Wallet-Aktivitäten in Echtzeit zu verfolgen.

Sie behalten die volle Kontrolle und können diese Funktion jederzeit aktivieren oder deaktivieren.
 
 

![](config.png)
{ .img-fluid .mb-5 }


#### ⚠️ Nur bestätigte Transaktionen sind vertrauenswürdig

Bitcoin Safe kann nicht bestätigen, dass eine übermittelte Transaktion gültig ist. Ein Angreifer — insbesondere einer, der sowohl Ihren Electrum-Server als auch den Bitcoin-Knoten kontrolliert, mit dem Sie verbunden sind — könnte:

* Eine gefälschte Transaktion erstellen, die Ihre Adresse betrifft
* Diese verbreiten, um eine Wallet-Benachrichtigung auszulösen
* Sicherstellen, dass sie niemals bestätigt wird, weil sie ungültig ist oder mit den Konsensregeln in Konflikt steht


  


#### ✅ Zusammenfassung

Ab Version **1.5.0** unterstützt Bitcoin Safe sofortige Transaktionsbenachrichtigungen durch:

* Passives Abhören des P2P-Bitcoin-Netzwerks (wie Bitcoin Core)
* Abgleich von Transaktionen, die die **Adressen** oder **UTXOs** Ihrer Wallet betreffen
* Abruf vollständiger Details über Electrum/Esplora oder direkte Hinzufügung über Compact Block Filters
* Es werden niemals Wallet-Daten nach außen preisgegeben