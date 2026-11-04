---
title: "Unsicherer COLDCARD-Seed"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "Kurzanleitung zum Verschieben von Guthaben aus einem Seed, der auf einem Coinkite-Gerät erzeugt wurde."
---

[Coinkite hat eine Schwachstelle bei der Seed-Erzeugung in betroffener COLDCARD-Firmware offengelegt](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). Siehe auch [Blocks technische Analyse des vorhersagbaren RNG-Fallbacks und des 32-Bit-Reseedings](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware). Ein Firmware-Update repariert einen bestehenden Seed nicht.

**Wenn du einen Seed mit einem Coinkite-Produkt erstellt hast, migriere BALD!**

## Checkliste für die Migration

1. Erzeuge auf einem **Signiergerät, das kein COLDCARD ist** ([unterstützte Geräte ansehen]({{< ref "library/supported-hardware-signers" >}})), einen vollständig neuen Seed. Verwende den alten Seed nicht wieder. Nutze anschließend diesen Signer mit dem Einrichtungsassistenten von Bitcoin-Safe, um entweder eine neue [Single-Signature-Wallet]({{< ref "library/setup-singlesig-wallet" >}}) oder eine [Multisignature-Wallet]({{< ref "library/setup-multisig-wallet" >}}) zu erstellen.
   - Wenn kein Hardware-Signer außer COLDCARD verfügbar ist, kannst du [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}}) auf einem dedizierten, auf Werkseinstellungen zurückgesetzten Android-Gerät verwenden, das offline bleibt und ausschließlich zum Signieren dient.
   - Schließe den Empfangs- und Sendetest des Assistenten ab, um sicherzustellen, dass die neue Wallet korrekt eingerichtet ist: prüfe ihr Backup und eine Empfangsadresse auf dem neuen Signer, empfange einen kleinen Testbetrag und sende ihn erfolgreich an eine andere verifizierte Adresse derselben neuen Wallet.
2. Signiere die Migrationstransaktion:
   - **Wenn die betroffene Wallet eine Single-Signature-Wallet ist:** Übertrage sie auf dem üblichen Weg mit einer hohen Gebühr, damit sie schnell bestätigt wird.
   - **Wenn die betroffene Wallet eine Multisignature-Wallet ist:** Übertrage sie nicht auf dem üblichen Weg, da dadurch ihre öffentlichen Schlüssel im öffentlichen Mempool offengelegt werden. Kopiere die signierte Rohtransaktion und reiche sie direkt über [MARA Slipstream](https://slipstream.mara.com/) ein.
3. Behalte das alte COLDCARD, bis das gesamte Guthaben in der neuen Wallet eingegangen und bestätigt ist, und aktualisiere es anschließend auf die neueste Firmware.

Wenn du jemandem bei der Migration hilfst, bitte die Person niemals, ihre Seed-Wörter zu teilen, zu fotografieren oder einzutippen. Der Seed muss privat bleiben und darf nur auf dem Signiergerät eingegeben werden.
