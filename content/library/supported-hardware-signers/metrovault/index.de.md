---
aliases:
- /de/knowledge/supported-hardware-signers/metrovault/
title: MetroVault
signer: metrovault
bucket: knowledge
---

MetroVault kann ein altes Android-Gerat in ein dediziertes Offline-Bitcoin-Signiergerat fur Bitcoin Safe verwandeln. Installiere es nicht auf deinem Alltagstelefon. Setze das Gerat zuerst auf Werkseinstellungen zuruck, halte es **OFFLINE** und vom Internet getrennt und verwende es nur zum Signieren.

## Was du erwarten solltest

- Setze vor der Installation ein altes Android-Gerat zuruck und verwende es nur als Signiergerat.
- Installiere keine anderen Apps, melde dich in keinen Konten an, lege keine SIM-Karte ein und verbinde das Gerat nicht wieder mit dem Internet.
- Tausche Wallet-Daten, Deskriptoren und PSBTs mit Bitcoin Safe per QR-Code aus.
- Registriere Multisig-Deskriptoren und exportiere Signierdaten fur Bitcoin Safe.
- Prufe alle Details auf dem MetroVault-Bildschirm, bevor du signierst.

## Setze das Android-Gerat zuruck und nutze es nur als Offline-Signiergerat

Die Upstream-Dokumentation von MetroVault enthalt eine [empfohlene Geratekonfiguration](https://github.com/gorunjinian/MetroVault/#recommended-device-setup). Betrachte das als Anforderung: Verwende ein dediziertes, auf Werkseinstellungen zuruckgesetztes **OFFLINE-Telefon**, das nach der Einrichtung vom Internet getrennt bleibt und nur zum Signieren genutzt wird.

1. Setze das Telefon vor der Installation auf Werkseinstellungen zuruck.
2. Uberspringe die Einrichtung eines Google-Kontos und halte das Gerat offline.
3. Lass den Flugmodus dauerhaft aktiviert.
4. Deaktiviere Wi-Fi, Bluetooth, NFC und mobile Daten.
5. Entferne die SIM-Karte.
6. Deaktiviere USB-Debugging.
7. Installiere keine anderen Apps und nutze das Telefon fur nichts anderes als Signieren.

Fur den Produktionseinsatz solltest du nach Moglichkeit aus dem Quellcode bauen. Wenn du das Gerat nicht offline und ausschliesslich als Signiergerat halten kannst, verwende es nicht fur MetroVault-Produktionsgelder.
