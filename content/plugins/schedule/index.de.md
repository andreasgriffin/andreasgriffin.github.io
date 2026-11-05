---
title: "Geplante Zahlungen"
description: "Plane einmalige oder wiederkehrende Bitcoin-Zahlungen, verfolge, wann sie fällig sind, und bereite Transaktionen in Bitcoin-Safe zur Prüfung vor."
draft: false
tags: ["Plugins"]
images: ["schedule.png"]
weight: 40
faq:
  title: "Fragen zu geplanten Zahlungen"
  items:
    - question: "Kann ich eine einzelne Zahlung planen oder nur wiederkehrende?"
      answer: "Beides. Du kannst eine einmalige Zahlung, eine feste Anzahl von Wiederholungen oder einen fortlaufenden Plan erstellen."
    - question: "Wie oft kann sich ein Plan wiederholen?"
      answer: "Wiederholungsintervalle sind verfügbar als:\n- Minuten, Stunden oder Tage\n- Wochen, optional an ausgewählten Wochentagen\n- Monate oder Jahre, an Kalenderdaten oder Wochentagsmustern"
    - question: "Kann ich den Betrag in Fiat festlegen?"
      answer: "Ja. Du kannst den Betrag festlegen in:\n- Bitcoin\n- Einer unterstützten Fiat-Währung\n\nFiat-Beträge können einen von zwei Kursen verwenden:\n- Einen aktuellen Wechselkurs\n- Den CoinGecko-Kurs, festgelegt auf 00:00 GMT\n\nFür die nächste Zahlung kann außerdem ein Wechselkurs manuell überschrieben werden."
    - question: "Werden Adressen wiederverwendet?"
      answer: "Nein. Jede Empfängeradresse wird nur einmal verwendet. Wenn die Adressen eines Empfängers aufgebraucht sind, kannst du für diesen Empfänger weitere Adressen hinzufügen."
    - question: "Sendet Bitcoin-Safe die Zahlungen automatisch?"
      answer: "Nein. Wenn eine Zahlung fällig ist, bereitet Schedule die Transaktion in Bitcoin-Safe zur Prüfung vor. Du bist weiterhin dafür verantwortlich, sie zu signieren und zu senden."
    - question: "Kann ich mehrere Empfänger gleichzeitig bezahlen?"
      answer: "Ja. Wähle mehrere geplante Zahlungen aus und klicke auf **Ausgewählte bezahlen**. Bitcoin-Safe fasst sie zu einer Batch-Transaktion zusammen."
    - question: "Was, wenn eine Zahlung bereits bar oder auf anderem Weg erfolgt ist?"
      answer: "Füge eine **Out-of-Band**-Auszahlung hinzu. Sie erfasst die Zahlung im Plan, ohne eine Bitcoin-Transaktion, damit der Fortschritt korrekt bleibt."
---

### {{< page-title >}}

<p class="lead">Plane Bitcoin-Zahlungen und lass Schedule im Blick behalten, was fällig ist.</p>

<ul class="plugin-features">
<li>Mitarbeiter bezahlen oder andere regelmäßige Verpflichtungen organisieren</li>
<li>Regelmäßige Überweisungen einrichten</li>
<li>Eine einmalige Zahlung planen, die du nicht vergessen darfst</li>
</ul>

Wenn eine Zahlung fällig ist, bereitet Schedule die Transaktion in Bitcoin-Safe zur Prüfung vor. Du bist weiterhin dafür verantwortlich, sie zu signieren und zu senden.

{{< video "schedule.mp4" controls >}}

### Flexible Zahlungspläne

- Wähle eine einmalige Zahlung, eine feste Anzahl von Wiederholungen oder einen fortlaufenden Plan.
- Lege ein Startdatum und ein Wiederholungsintervall fest: Minuten, Stunden, Tage, Wochen, Monate oder Jahre. Wöchentliche Pläne können ausgewählte Wochentage nutzen; monatliche und jährliche Pläne unterstützen Kalenderdaten und Wochentagsmuster.
- Lege Empfänger, Kategorie und Betrag in Bitcoin oder einer unterstützten Fiat-Währung fest.
- Bei Fiat-Beträgen nutze einen aktuellen Kurs oder den CoinGecko-Kurs, festgelegt auf 00:00 GMT. Für die nächste Zahlung kann ein Kurs manuell überschrieben werden.
- Pläne mit fester Anzahl zeigen Vorschauen für den Betrag pro Zahlung und insgesamt.

### Zahlungen in deiner Wallet vorbereiten

- Sieh das nächste Fälligkeitsdatum und den Fortschritt; fällige Zahlungen sind hervorgehoben und können einen Hinweis von Bitcoin-Safe auslösen.
- Bereite eine fällige Zahlung oder einen Batch im Transaktionseditor vor, mit ausgefüllten Empfängerausgängen, Labels und Kategorien.
- Prüfe und passe die Transaktion an, bevor du sie selbst signierst und sendest.
- Speichere wiederverwendbare Empfänger mit Name und mehreren Adressen. Schedule kann für eine Auszahlung eine unbenutzte Adresse auswählen.

### Pläne verfolgen und verwalten

- Finde Pläne nach Fälligkeitsstatus, Plantyp oder Kategorie. Listen zeigen Termine, abgeschlossene Zahlungen, Häufigkeit, Empfänger, Betrag, Kategorie und Summe.
- Prüfe abgeschlossene Auszahlungen und kommende Termine. Passende Wallet-Transaktionen können den Fortschritt aktualisieren; du kannst eine Auszahlung auch manuell hinzufügen oder die Wallet-Transaktionen neu prüfen.
- Bearbeite einen Plan vor seiner ersten erfassten Auszahlung, dupliziere oder lösche ihn und importiere/exportiere Pläne als JSON-Sicherung.

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">Bitcoin-Safe herunterladen</h2>
<p class="text-muted mb-3">Plugins sind in Bitcoin-Safe enthalten. Lade die App herunter, um sie auszuprobieren.</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">Bitcoin-Safe herunterladen</a>
<small class="text-muted">Freie &amp; Open-Source-Software · Windows, macOS, Linux</small>
</div>
</section>

### Häufig gestellte Fragen

<details>
<summary>Kann ich eine einzelne Zahlung planen oder nur wiederkehrende?</summary>

Beides. Du kannst eine einmalige Zahlung, eine feste Anzahl von Wiederholungen oder einen fortlaufenden Plan erstellen.

</details>

<details>
<summary>Wie oft kann sich ein Plan wiederholen?</summary>

Wiederholungsintervalle sind verfügbar als:

- Minuten, Stunden oder Tage
- Wochen, optional an ausgewählten Wochentagen
- Monate oder Jahre, an Kalenderdaten oder Wochentagsmustern

</details>

<details>
<summary>Kann ich den Betrag in Fiat festlegen?</summary>

Ja. Du kannst den Betrag festlegen in:

- Bitcoin
- Einer unterstützten Fiat-Währung

Fiat-Beträge können einen von zwei Kursen verwenden:

- Einen aktuellen Wechselkurs
- Den CoinGecko-Kurs, festgelegt auf 00:00 GMT

Für die nächste Zahlung kann außerdem ein Wechselkurs manuell überschrieben werden.

</details>

<details>
<summary>Werden Adressen wiederverwendet?</summary>

Nein. Jede Empfängeradresse wird nur einmal verwendet. Wenn die Adressen eines Empfängers aufgebraucht sind, kannst du für diesen Empfänger weitere Adressen hinzufügen.

</details>

<details>
<summary>Sendet Bitcoin-Safe die Zahlungen automatisch?</summary>

Nein. Wenn eine Zahlung fällig ist, bereitet Schedule die Transaktion in Bitcoin-Safe zur Prüfung vor. Du bist weiterhin dafür verantwortlich, sie zu signieren und zu senden.

</details>

<details>
<summary>Kann ich mehrere Empfänger gleichzeitig bezahlen?</summary>

Ja. Wähle mehrere geplante Zahlungen aus und klicke auf **Ausgewählte bezahlen**. Bitcoin-Safe fasst sie zu einer Batch-Transaktion zusammen.

</details>

<details>
<summary>Was, wenn eine Zahlung bereits bar oder auf anderem Weg erfolgt ist?</summary>

Füge eine **Out-of-Band**-Auszahlung hinzu. Sie erfasst die Zahlung im Plan, ohne eine Bitcoin-Transaktion, damit der Fortschritt korrekt bleibt.

</details>
</content>
