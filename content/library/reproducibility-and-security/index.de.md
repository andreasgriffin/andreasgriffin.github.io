---
aliases:
  - "/de/features/reproducibility-and-security/"
title: "Sicherheit und Reproduzierbarkeit"
description: "Bitcoin-Safe folgt hohen Standards für Binärsicherheit: reproduzierbare Builds, signierte Commits, signierte Releases und unabhängige externe Überwachung."
draft: false
bucket: features
tags: ["Featured", "Security"]
images: ["logo.png"]
keywords: ["reproducible builds", "verify binaries", "signed commits", "signed releases", "appimage", "flatpak", "windows exe", "binary security"]
weight: 18
---

### {{< page-title >}}
{{< page-description >}}
<br>

![Reproduzierbare Build-Ausgaben für Bitcoin-Safe](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 500px;" }

Wir haben mehrere Schutzebenen für die Integrität der Downloads auf der Website umgesetzt, damit die heruntergeladene App wirklich zum öffentlichen Quellcode passt:

- **Reproduzierbare Builds**: Linux-`deb`-, `AppImage`- und `Flatpak`-Builds sowie Windows-`portable exe` und `setup exe` lassen sich Byte für Byte reproduzieren. Wenn eine neu erstellte Datei exakt übereinstimmt, ist das ein starker Hinweis darauf, dass die Binärdatei aus demselben Quellcode gebaut wurde.
- **Signierte Repository-Historie**: Das [Bitcoin-Safe GitHub-Repository](https://github.com/andreasgriffin/bitcoin-safe/commits/main) veröffentlicht verifizierte signierte Commits, sodass Prüfer nachvollziehen können, wer den Code für ein Release eingebracht hat.
- **Signierte Binärdateien**: Release-Dateien sind mit dem Bitcoin-Safe [öffentlichen PGP-Schlüssel]({{< gpg_key_link >}}) signiert, und Windows-Binärdateien folgen zusätzlich der [Code-Signing-Richtlinie]({{< ref "code-signing-policy" >}}).
- **Unabhängige Reproduzierbarkeits-Prüfungen**: [WalletScrutiny](https://walletscrutiny.com/desktop/bitcoin.safe/) verfolgt Bitcoin-Safe unabhängig und zeigt den Status der reproduzierbaren Verifikation für Desktop-Releases an.
- **Laufende Signatur-Überwachung**: [BinaryWatch](https://binarywatch.org/) prüft regelmäßig Bitcoin-Safe-Release-Dateien und ob ihre Signaturen weiterhin gegen den Bitcoin-Safe [öffentlichen PGP-Schlüssel]({{< gpg_key_link >}}) gültig sind.
- **Update-Verifikation**: Updates werden in Bitcoin-Safe angezeigt, und ihre Signatur wird automatisch verifiziert.

Zusammengenommen gehört Bitcoin-Safe damit zu einer kleinen Gruppe von Projekten, die Binärsicherheit als zentralen Bestandteil der Nutzersicherheit behandeln und nicht als nachträglichen Zusatz.

### Sicherheit ist der zentrale Maßstab in jedem Bereich von Bitcoin-Safe

Über die Integrität der Binärdateien hinaus setzt Bitcoin-Safe auf sichere Voreinstellungen, gute betriebliche Praxis und klare Nutzerführung. Ein paar Beispiele:

- **Hardware-zentrierte Verwahrung**: Bitcoin-Safe setzt auf [Hardware-Signer]({{< ref "library/supported-hardware-signers" >}}), damit Seeds auf dedizierten Geräten bleiben und nicht zu Hot Secrets auf einem allgemeinen Computer werden.
- **Sichererer Einrichtungsablauf**: Der Einrichtungsassistent hilft dabei, Wallets zu erstellen, die wirklich für den realen Einsatz bereit sind, einschließlich Tests für [Hardware-Signer]({{< ref "library/supported-hardware-signers" >}}), [PDF-Backup-Blättern]({{< ref "library/pdf-export/" >}}) und Hinweisen zur sicheren Aufbewahrung von Hardware-Signern und Seed-Backups.
- **Verifikation von Empfangsadressen**: Bitcoin-Safe macht es einfach, [Empfangsadressen]({{< ref "library/verify-receive-address/" >}}) direkt auf dem Signer zu prüfen, bevor sie geteilt werden.
- **Erkennung von Address-Poisoning**: Die App warnt vor verdächtigen [ähnlich aussehenden Adressen]({{< ref "library/address-poisoning/" >}}).
- **Multisig-Sicherheit**: Bitcoin-Safe unterstützt Multisignatur-Wallets, sodass größere Bestände durch mehrere Geräte oder Personen statt durch einen einzelnen Fehlerpunkt geschützt werden können.
- **Zusammenarbeit, die Multisig einfacher macht**: Bitcoin-Safe macht [Multisignatur-Zusammenarbeit]({{< ref "library/collaboration/" >}}) praxistauglich, sodass Einrichtung und Signieren in realen Abläufen deutlich einfacher zu koordinieren sind.
- **Klare Signierabläufe**: Gerätespezifische Signierbildschirme verringern Verwirrung bei der PSBT-Prüfung und helfen Nutzern, auf dem richtigen Signer die richtige Aktion auszuführen.
