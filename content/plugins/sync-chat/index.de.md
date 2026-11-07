---
title: "Sync & Chat"
description: "Finde Peers in deiner Wallet, synchronisiere Labels und Kategorien, chatte sicher und teile PSBTs mit einem Klick."
draft: false
tags: ["Plugins", "sync-chat-mainpage"]
images: ["logo.png"]
weight: 30
faq:
  title: "Fragen zu Sync & Chat"
  items:
    - question: "Wie finden Geräte einander?"
      answer: "Sync & Chat sucht nach anderen Geräten, die denselben Wallet-Deskriptor verwenden. Der Deskriptor wird vor der Suche gehasht, sodass er nicht im Klartext offengelegt wird. Jedes gefundene Gerät muss außerdem manuell hinzugefügt und als vertrauenswürdig markiert werden, bevor es am Chat teilnehmen kann. So bleibt der Chat auch dann sicher, wenn der Deskriptor nicht geheim ist."
    - question: "Wie funktioniert die Zusammenarbeit in der Praxis?"
      answer: "1. Einrichtung (einmalig): Füge jedes Gerät eines Teilnehmers hinzu und markiere es als vertrauenswürdig.\n2. Erstellen: Ein Teilnehmer erstellt eine PSBT und fügt seine Signatur hinzu.\n3. Teilen: Die PSBT geht an alle Teilnehmer oder nur an ausgewählte.\n4. Signieren: Jeder Teilnehmer fügt seine Signatur hinzu, bis die Transaktion vollständig signiert ist.\n5. Senden: Der letzte Unterzeichner sendet die Transaktion, und sie erscheint danach in den Wallets aller Teilnehmer."
    - question: "Was wird synchronisiert?"
      answer: "Sync & Chat übernimmt:\n- Coin-Kategorien und Labels, synchronisiert zwischen den Unterzeichnern, auch über verschiedene Betriebssysteme hinweg\n- Das Teilen von PSBTs mit einem Klick"
    - question: "Ist der Chat privat?"
      answer: "Ja. Der Wallet-Chat ist verschlüsselt und läuft über Nostr; auch Label-Sicherungen werden verschlüsselt über Nostr gespeichert."
---

### {{< page-title >}}

<p class="lead">Koordiniere Multisig-Unterzeichner und halte den Wallet-Kontext direkt in Bitcoin-Safe synchron.</p>

<ul class="plugin-features">
<li>Andere Geräte finden, die denselben Wallet-Deskriptor verwenden</li>
<li>Labels und Kategorien zwischen Unterzeichnern synchronisieren</li>
<li>Sicher chatten und PSBTs mit einem Klick teilen</li>
</ul>

### Label-Synchronisation

{{< video src="../../library/label-sync/label-sync.mp4" controls="true" >}}

### Gemeinsames Signieren

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

Die vollständige Anleitung zum gemeinsamen Signieren einer Multisig-Wallet findest du unter [Zusammenarbeit in einer Multisig]({{< ref "library/collaboration/" >}}).

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
<summary>Wie finden Geräte einander?</summary>

Sync & Chat sucht nach anderen Geräten, die denselben Wallet-Deskriptor verwenden. Der Deskriptor wird vor der Suche gehasht, sodass er nicht im Klartext offengelegt wird. Jedes gefundene Gerät muss außerdem manuell hinzugefügt und als vertrauenswürdig markiert werden, bevor es am Chat teilnehmen kann. So bleibt der Chat auch dann sicher, wenn der Deskriptor nicht geheim ist.

</details>

<details>
<summary>Wie funktioniert die Zusammenarbeit in der Praxis?</summary>

1. **Einrichtung (einmalig):** Füge jedes Gerät eines Teilnehmers hinzu und markiere es als vertrauenswürdig.
2. **Erstellen:** Ein Teilnehmer erstellt eine PSBT und fügt seine Signatur hinzu.
3. **Teilen:** Die PSBT geht an alle Teilnehmer oder nur an ausgewählte.
4. **Signieren:** Jeder Teilnehmer fügt seine Signatur hinzu, bis die Transaktion vollständig signiert ist.
5. **Senden:** Der letzte Unterzeichner sendet die Transaktion, und sie erscheint danach in den Wallets aller Teilnehmer.

</details>

<details>
<summary>Was wird synchronisiert?</summary>

Sync & Chat übernimmt:

- Coin-Kategorien und Labels, synchronisiert zwischen den Unterzeichnern, auch über verschiedene Betriebssysteme hinweg
- Das Teilen von PSBTs mit einem Klick

</details>

<details>
<summary>Ist der Chat privat?</summary>

Ja. Der Wallet-Chat ist verschlüsselt und läuft über Nostr; auch Label-Sicherungen werden verschlüsselt über Nostr gespeichert.

</details>

{{< sync-page-box >}}
</content>
