---
title: "Unsicherer COLDCARD-Seed"
date: "2026-08-02"
draft: false
description: "Coinkite hat eine kritische Schwachstelle bei der Seed-Erzeugung in betroffener COLDCARD-Firmware offengelegt. Wenn Sie einen Seed mit einem betroffenen Coinkite-Gerät erstellt haben, transferieren Sie Ihre Gelder zu einem neuen Seed."
images: ["COLDCARD Security Advisory Notice - Migrate ASAP.png"]
---

## Zusammenfassung

[Coinkite hat eine kritische Schwachstelle bei der Seed-Erzeugung in betroffener COLDCARD-Firmware offengelegt](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). [Blocks technische Analyse](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware) führt die Ursache auf einen vorhersagbaren softwarebasierten Zufallszahlengenerator zurück, der anstelle des Hardware-RNG des Geräts verwendet wird, und warnt, dass **eine aktive Ausnutzung im Gange ist**. Ein Firmware-Update **repariert** einen bestehenden Seed **nicht**.

**Wenn Sie einen Seed mit einem betroffenen Coinkite-Gerät erstellt haben, transferieren Sie Ihre Gelder zu einem neuen Seed.**

## Ist mein Gerät betroffen?

Die Betroffenheit hängt von der **Firmware-Version ab, die zum Zeitpunkt der Seed-Erzeugung installiert war** – nicht davon, wann das Gerät hergestellt wurde.

| Gerät | Firmware zur Seed-Erzeugung | Status |
|---|---|---|
| Mk1 | Alle veröffentlichten Firmwares | Nicht betroffen |
| Mk2 / Mk3 | v3.2.2 oder älter | Nicht betroffen (verwendet Hardware-RNG) |
| Mk2 / Mk3 | v4.0.0 – v4.1.9 | **Verwundbar** – kein sicheres Reseeding |
| Mk4 | Produktion ab v5.0.0 | **Verwundbar** – auf ~72 Bit Entropie begrenzt |
| Q | Alle Produktions-Firmwares | **Verwundbar** – auf ~72 Bit Entropie begrenzt |
| Mk5 | Alle Produktions-Firmwares | **Verwundbar** – auf ~72 Bit Entropie begrenzt |
| TAPSIGNER, OPENDIME, SATSCARD | — | Nicht betroffen (anderer Code) |

Beachten Sie: Das Exportieren eines unsicheren Seeds und dessen Import in eine andere Wallet **behebt** das Problem **nicht** – der Seed selbst bleibt betroffen.

## Installieren Sie die korrigierte Firmware, bevor Sie einen neuen Seed erzeugen

Eine korrigierte Firmware ist nun für jedes betroffene Modell und jeden Release-Kanal verfügbar. Erzeugen Sie auf einer COLDCARD keinen neuen Seed, bis sie installiert ist.

| Gerät | Korrigierte Firmware |
|---|---|
| Mk2 / Mk3 | 4.2.0 oder neuer |
| Mk4 / Mk5 (standard) | 5.6.0 oder neuer |
| Q (standard) | 1.5.0Q oder neuer |
| Mk4 / Mk5 (Edge) | 6.6.0X oder neuer |
| Q (Edge) | 6.6.0QX oder neuer |

Standard und Edge sind getrennte Release-Kanäle. Wenn Sie Edge verwenden, installieren Sie die korrigierte Edge-Version für Ihr Modell – gehen Sie nicht davon aus, dass eine ältere Edge-6.x-Version bereits korrigiert ist, nur weil ihre Versionsnummer höher ist als die der Standard-Version.

## Schützen mich Würfelwürfe oder eine Passphrase?

- **Würfelwürfe:** Der Fehler betrifft nur die vom Gerät erzeugte Entropie. Wenn Sie bei der Erstellung des Seeds mindestens **50 unabhängige, private Würfelwürfe** eingegeben haben (99 oder mehr für etwa 256 Bit Entropie), hat allein die Würfeleingabe mindestens 128 Bit unabhängige Entropie beigesteuert, und der Seed gilt durch dieses Problem allein nicht als gefährdet. Bei weniger als 50 Würfen – oder wenn Sie unsicher sind, wie viele eingegeben wurden oder ob sie privat waren – **migrieren Sie**.
- **BIP-39-Passphrase:** Eine starke, einzigartige BIP-39-Passphrase (nicht die COLDCARD-PIN) bietet eine zusätzliche unabhängige Hürde, **repariert** den betroffenen Seed aber **nicht**. Wenn Ihre Passphrase kurz, gebräuchlich, wiederverwendet oder erratbar ist – oder Sie sich ihrer Stärke nicht sicher sind – behandeln Sie die Gelder als gefährdet und migrieren Sie sofort. Selbst mit einer starken Passphrase sollten Sie so bald wie möglich zu einem neu erzeugten Seed migrieren.

## Migrations-Checkliste

Migrieren Sie ruhig und sorgfältig. Eine überstürzte Wallet-Migration kann ein unmittelbareres Risiko schaffen als das Problem, das Sie beheben möchten.

1. **Installieren Sie die korrigierte Firmware** für Ihr Modell, bevor Sie einen Ersatz-Seed erzeugen. Wenn Sie es vorziehen, erzeugen Sie den neuen Seed auf einem **Nicht-COLDCARD-Signiergerät** ([siehe unterstützte Geräte]({{< ref "library/supported-hardware-signers" >}})) – verwenden Sie den alten Seed in jedem Fall **nicht** erneut.
2. Erzeugen Sie einen völlig neuen Seed und **bewahren Sie ihn auf**. Verifizieren Sie vor jeder Einzahlung das schriftliche Backup, den Wallet-Fingerprint und eine Empfangsadresse.
3. Nutzen Sie den Einrichtungsassistenten von Bitcoin-Safe, um mit dem neuen Seed eine neue [Einzel-Signatur-Wallet]({{< ref "library/setup-singlesig-wallet" >}}) oder [Multisignatur-Wallet]({{< ref "library/setup-multisig-wallet" >}}) zu erstellen.
4. Führen Sie den Empfangs-und-Sende-Test des Assistenten durch: Verifizieren Sie das Backup und eine Empfangsadresse auf dem neuen Signiergerät, empfangen Sie einen kleinen Testbetrag und senden Sie ihn erfolgreich an eine weitere verifizierte Adresse in der neuen Wallet.
5. Signieren und senden Sie die Migrationstransaktion:
   - **Einzel-Signatur-Wallet:** Senden Sie sie normal mit einer hohen Gebühr, damit sie schnell bestätigt wird.
   - **Multisignatur-Wallet:** Senden Sie sie nicht normal ab, da dadurch ihre öffentlichen Schlüssel im öffentlichen Mempool sichtbar werden. Kopieren Sie die signierte Roh-Transaktion und übermitteln Sie sie direkt über [MARA Slipstream](https://slipstream.mara.com/).
6. Bewahren Sie die alte COLDCARD und ihr Backup auf, bis der **vollständige Saldo** in der neuen Wallet eingegangen und bestätigt ist. Erst dann löschen Sie den alten Seed.

Wenn die Mk2/Mk3 Ihr einziges Signiergerät ist, installieren Sie zuerst Firmware 4.2.0 oder neuer: Sie erzeugt Ersatz-Seeds korrekt, sodass Sie für die Migration keine neuere COLDCARD benötigen. Befolgen Sie dieselben Schritte, wechseln Sie auf dem einzelnen Gerät sorgfältig zwischen altem und neuem Seed und bewahren Sie das alte Backup auf, bis die Migration vollständig bestätigt ist.

## Wenn Sie Multisignatur verwenden

Wenn eine Multisignatur-Konfiguration **ausschließlich** aus betroffenen Geräten besteht, bleibt die Schwachstelle wirksam. Schützen Sie die Konfiguration mit einem Quorum, das mindestens ein nicht betroffenes Signiergerät enthält.

## Wenn Sie jemand anderem bei der Migration helfen

Bitten Sie diese Person niemals, ihre Seed-Wörter zu teilen, zu fotografieren oder einzutippen. Der Seed muss privat bleiben und darf nur auf dem Signiergerät selbst eingegeben werden.
