---
title: "Sync & Chat"
description: "Descobreix els parells de la teva cartera, sincronitza etiquetes i categories, xateja de manera segura i comparteix PSBT amb un clic."
draft: false
tags: ["Plugins", "sync-chat-mainpage"]
images: ["logo.png"]
weight: 30
faq:
  title: "Preguntes sobre Sync & Chat"
  items:
    - question: "Com es troben els dispositius entre ells?"
      answer: "Sync & Chat busca altres dispositius que utilitzin el mateix descriptor de cartera. El descriptor es fa un hash abans d'utilitzar-lo per a la cerca, de manera que no s'exposa en text pla. A més, cada dispositiu descobert s'ha d'afegir i marcar com a fiable manualment abans de poder participar al xat. Així el xat es manté segur encara que el descriptor no sigui secret."
    - question: "Com funciona la col·laboració a la pràctica?"
      answer: "1. Configuració (una vegada): afegeix el dispositiu de cada participant i marca'l com a fiable.\n2. Crear: un participant crea una PSBT i hi afegeix la seva signatura.\n3. Compartir: la PSBT s'envia a tots els participants, o només als seleccionats.\n4. Signar: cada participant hi afegeix la seva signatura fins que la transacció estigui totalment signada.\n5. Transmetre: l'últim signant transmet la transacció, i després apareix a la cartera de tots els participants."
    - question: "Què es sincronitza?"
      answer: "Sync & Chat gestiona:\n- Categories i etiquetes de monedes, sincronitzades entre els signants, fins i tot entre sistemes operatius diferents\n- Compartir PSBT amb un clic"
    - question: "És privat el xat?"
      answer: "Sí. El xat de la cartera està xifrat i funciona a través de Nostr; les còpies de seguretat de les etiquetes també s'emmagatzemen xifrades mitjançant Nostr."
---

### {{< page-title >}}

<p class="lead">Coordina els signants de multisig i mantén el context de la cartera sincronitzat des de Bitcoin-Safe.</p>

<ul class="plugin-features">
<li>Descobreix altres dispositius que utilitzen el mateix descriptor de cartera</li>
<li>Sincronitza etiquetes i categories entre els signants</li>
<li>Xateja de manera segura i comparteix PSBT amb un clic</li>
</ul>

### Sincronització d'etiquetes

{{< video src="../../library/label-sync/label-sync.mp4" controls="true" >}}

### Signatura col·laborativa

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

Per a la guia completa de signatura col·laborativa multisig, consulta [Col·laboració en un multisig]({{< ref "library/collaboration/" >}}).

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">Descarrega Bitcoin-Safe</h2>
<p class="text-muted mb-3">Els plugins estan inclosos a Bitcoin-Safe. Descarrega l'aplicació per provar-los.</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">Descarrega Bitcoin-Safe</a>
<small class="text-muted">Programari lliure i de codi obert · Windows, macOS, Linux</small>
</div>
</section>

### Preguntes freqüents

<details>
<summary>Com es troben els dispositius entre ells?</summary>

Sync & Chat busca altres dispositius que utilitzin el mateix descriptor de cartera. El descriptor es fa un hash abans d'utilitzar-lo per a la cerca, de manera que no s'exposa en text pla. A més, cada dispositiu descobert s'ha d'afegir i marcar com a fiable manualment abans de poder participar al xat. Així el xat es manté segur encara que el descriptor no sigui secret.

</details>

<details>
<summary>Com funciona la col·laboració a la pràctica?</summary>

1. **Configuració (una vegada):** afegeix el dispositiu de cada participant i marca'l com a fiable.
2. **Crear:** un participant crea una PSBT i hi afegeix la seva signatura.
3. **Compartir:** la PSBT s'envia a tots els participants, o només als seleccionats.
4. **Signar:** cada participant hi afegeix la seva signatura fins que la transacció estigui totalment signada.
5. **Transmetre:** l'últim signant transmet la transacció, i després apareix a la cartera de tots els participants.

</details>

<details>
<summary>Què es sincronitza?</summary>

Sync & Chat gestiona:

- Categories i etiquetes de monedes, sincronitzades entre els signants, fins i tot entre sistemes operatius diferents
- Compartir PSBT amb un clic

</details>

<details>
<summary>És privat el xat?</summary>

Sí. El xat de la cartera està xifrat i funciona a través de Nostr; les còpies de seguretat de les etiquetes també s'emmagatzemen xifrades mitjançant Nostr.

</details>

{{< sync-page-box >}}
</content>
