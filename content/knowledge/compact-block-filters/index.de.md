---
title: "Kompakte Block-Filter"
description: "Erklärt, was kompakte Block-Filter sind und wie sie die Privatsphäre im Vergleich zu Electrum-Servern verbessern."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "kompakte Block-Filter"
  - "CBF"
  - "Privatsphäre"
  - "Bitcoin-Wallet"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}


Bitcoin Safe 1.6.0 führt **kompakte Block-Filter (CBF)** als optionale Methode zur Synchronisation Ihrer Wallet ein. Anstatt einen zentralisierten Electrum-Server nach Ihrer Wallet-Historie zu fragen, kann Bitcoin Safe jetzt für jeden Block eine kleine Zusammenfassungsdatei direkt von zufälligen Bitcoin Core-Peers herunterladen. Diese Zusammenfassungen funktionieren wie eine kurze Checkliste, mit der Ihre Wallet eigenständig entscheiden kann, ob ein Block möglicherweise eine Ihrer Transaktionen enthält.

Da Bitcoin Safe die Entscheidung lokal trifft, erfährt kein Drittserver jemals, welche Adressen oder Transaktionen für Sie relevant sind. Sie erhalten dieselben Bestätigungsdaten, die ein Full Node speichert, jedoch in einem leichteren Format, das auf Alltagsgeräten passt.

**Warum sich das besser anfühlt:**

- 📦 **Kleine Downloads:** Jeder Filter ist nur wenige Kilobyte groß, sodass Sie über normale Heimverbindungen synchronisieren können, ohne die gesamte Blockchain zu speichern.
- 🔐 **Direkt aus dem Netzwerk:** Bitcoin Safe verbindet sich mit mehreren zufälligen Bitcoin Core-Knoten, genau wie andere Nodes, und verringert so die Wahrscheinlichkeit, dass ein einzelner Beobachter Sie profilieren kann.
- 🕵️ **Lokaler Abgleich:** Ihre Wallet prüft die Filter lokal. Wirkt ein Filter relevant, wird nur dann der entsprechende Block angefordert, wodurch Ihre Adressen privat bleiben.

Im Gegensatz dazu durchsuchen Electrum-Server die Blockchain in Ihrem Auftrag. Jede Anfrage teilt die Adressen Ihrer Wallet mit dem Serverbetreiber, der diese Informationen protokollieren könnte. Mit kompakten Block-Filtern lädt Bitcoin Safe dieselben neutralen Daten herunter, die jeder Node teilt. Niemand kann herausfinden, welche Adressen Ihnen gehören, weil Ihre Wallet sie von vornherein nicht offenlegt.

Below is a simple view of how Bitcoin Safe connects when CBF is enabled. Notice how it mirrors the way Bitcoin Core nodes already talk to each other:


![Bitcoin Safe lädt kompakte Block-Filter von mehreren zufälligen Bitcoin Core-Peers herunter.](logo.jpg)
{ .img-fluid .mb-5   style="max-width: 450px;" }


Sie können wählen, zu wie vielen Peers sich Bitcoin Safe verbinden soll. Mehr Peers benötigen mehr Bandbreite und führen zu einer längeren Synchronisationszeit. Die Standardeinstellung ist 2.

 
### Womit beim Synchronisieren zu rechnen ist

CBF beeinflusst die Wartezeit je nachdem, was Sie gerade tun:

1. ✨ **Einrichten oder Wiederherstellen einer Wallet:** Ob Sie eine neue Wallet erstellen oder eine vorhandene wiederherstellen, die erste Synchronisation lädt Filter für die gesamte Historie Ihrer Wallet. Erwarten Sie, dass dieser einmalige Vorgang **zwischen 5 und 30 Minuten** dauert, abhängig von Ihrer Internetgeschwindigkeit.
2. 🚀 **Öffnen einer bereits synchronisierten Wallet:** Bitcoin Safe muss nur die neuesten Filter seit Ihrer letzten Sitzung herunterladen. Dieses Nachholen ist normalerweise in **unter 30 Sekunden** abgeschlossen.
3. 🔄 **Wechsel von Electrum-Servern zu CBF:** Da die Wallet zuvor mit Electrum-Servern synchronisiert wurde, muss Bitcoin Safe nur die neuesten Filter herunterladen, was in der Regel **weniger als 30 Sekunden** dauert.

### Über unbestätigte Zahlungen informiert bleiben

Kompakte Block-Filter decken nur **bestätigte Blöcke** ab. Um über eingehende Transaktionen vor der Bestätigung informiert zu werden, aktivieren Sie außerdem die [Instant transaction notifications]({{< ref "knowledge/instant-transactions-notifications/" >}}). Dieses Feature lauscht den Peer-to-Peer-Nachrichten eines zufälligen Bitcoin-Knotens in Echtzeit, sodass Sie auf Mempool-Aktivität reagieren können, ohne die Privatsphäre preiszugeben.


<br>
<br>



### Technische Details


- *Für Entwickler, die tiefer einsteigen möchten:* kompakte Block-Filter folgen der [BIP158-Spezifikation](https://bips.dev/158/) und werden in [Elle Moutons Überblick über Golomb-coded sets](https://ellemouton.com/posts/bip158/) beschrieben. Die Implementierung von Bitcoin Safe basiert auf dem Open-Source-[Kyoto Compact Block Filter Modul für BDK](https://github.com/2140-dev/kyoto).
- Sie können Ihren eigenen Bitcoin Core-Knoten zu den Peers für das Synchronisieren von Compact Block Filters hinzufügen, indem Sie den _Initial node_ des _Bitcoin network monitoring_ auswählen.


![](inital-node.png)
{ .img-fluid .mb-5   style="max-width: 414px;" }