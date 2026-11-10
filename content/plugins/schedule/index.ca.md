---
title: "Pagaments programats"
description: "Planifica pagaments de Bitcoin d'una sola vegada o recurrents, fes un seguiment de quan venen i prepara les transaccions per revisar-les a Bitcoin-Safe."
draft: false
tags: ["Plugins"]
images: ["schedule.png"]
weight: 40
faq:
  title: "Preguntes sobre els pagaments programats"
  items:
    - question: "Puc programar un sol pagament o només de recurrents?"
      answer: "Les dues coses. Pots crear un pagament únic, un nombre fix de repeticions o un calendari continu."
    - question: "Amb quina freqüència es pot repetir un calendari?"
      answer: "Els intervals de repetició disponibles són:\n- Minuts, hores o dies\n- Setmanes, opcionalment en dies de la setmana seleccionats\n- Mesos o anys, en dates del calendari o amb patrons de dia de la setmana"
    - question: "Puc definir l'import en moneda fiduciària?"
      answer: "Sí. Pots definir l'import en:\n- Bitcoin\n- Una moneda fiduciària compatible\n\nEls imports en moneda fiduciària poden utilitzar:\n- Un tipus de canvi en temps real\n- La tarifa de CoinGecko, fixada a les 00:00 GMT\n\nTambé es pot establir una substitució del tipus de canvi per al següent pagament."
    - question: "Es reutilitzen les adreces?"
      answer: "No. Cada adreça del destinatari s'utilitza només una vegada. Quan s'acaben les adreces d'un destinatari, pots afegir-ne més per a aquest destinatari."
    - question: "Bitcoin-Safe envia els pagaments automàticament?"
      answer: "No. Quan un pagament venç, Schedule prepara la transacció a Bitcoin-Safe perquè la revisis, i continues sent responsable de signar-la i transmetre-la."
    - question: "Puc pagar a diversos destinataris alhora?"
      answer: "Sí. Selecciona diversos pagaments programats i fes clic a **Paga els seleccionats**. Bitcoin-Safe els combinarà en una única transacció per lots."
    - question: "Què passa si un pagament s'ha fet en efectiu o d'una altra manera?"
      answer: "Pots afegir un pagament **fora de banda**. Registra el pagament al calendari sense una transacció de Bitcoin, perquè el progrés es mantingui exacte."
---

### {{< page-title >}}

<p class="lead">Planifica pagaments en Bitcoin i deixa que Schedule controli què ve.</p>

<ul class="plugin-features">
<li>Pagar empleats o organitzar altres obligacions periòdiques</li>
<li>Configurar transferències recurrents</li>
<li>Programar un pagament únic que no vols oblidar</li>
</ul>

Quan un pagament ve, Schedule prepara la transacció a Bitcoin-Safe perquè la revisis. Continues sent responsable de signar-la i transmetre-la.

{{< video "schedule.mp4" controls >}}

### Plans de pagament flexibles

- Tria un pagament únic, un nombre fix de repeticions o un calendari continu.
- Defineix una data d'inici i un interval de repetició: minuts, hores, dies, setmanes, mesos o anys. Els calendaris setmanals poden utilitzar dies de la setmana seleccionats; els mensuals i anuals admeten dates del calendari i patrons de dia de la setmana.
- Defineix el destinatari, la categoria i l'import en bitcoin o en una moneda fiduciària compatible.
- Per als imports en moneda fiduciària, utilitza un tipus de canvi en temps real o la tarifa de CoinGecko fixada a les 00:00 GMT. Es pot definir una substitució del tipus de canvi per al següent pagament.
- Els calendaris de nombre fix mostren vistes prèvies de l'import per pagament i del total.

### Prepara els pagaments a la cartera

- Consulta la següent data de venciment i el progrés dels pagaments; els pagaments vençuts es ressalten i poden activar un avís de Bitcoin-Safe.
- Prepara un pagament vençut o un lot al compositor de transaccions, amb les sortides dels destinataris, les etiquetes i les categories ja omplertes.
- Revisa i personalitza la transacció abans de signar-la i transmetre-la tu mateix.
- Desa destinataris reutilitzables amb un nom i diverses adreces. Schedule pot seleccionar una adreça no utilitzada per a un pagament.

### Segueix i gestiona els calendaris

- Cerca calendaris per estat de venciment, tipus de calendari o categoria. Les llistes mostren dates, pagaments completats, freqüència, destinatari, import, categoria i total.
- Revisa els pagaments completats i les properes ocurrències. Les transaccions coincidents de la cartera poden actualitzar el progrés; també pots afegir un pagament manualment o tornar a escanejar les transaccions de la cartera.
- Edita un calendari abans del primer pagament registrat, duplica'l o elimina'l, i importa i exporta calendaris com a còpia de seguretat en JSON.

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
<summary>Puc programar un sol pagament o només de recurrents?</summary>

Les dues coses. Pots crear un pagament únic, un nombre fix de repeticions o un calendari continu.

</details>

<details>
<summary>Amb quina freqüència es pot repetir un calendari?</summary>

Els intervals de repetició disponibles són:

- Minuts, hores o dies
- Setmanes, opcionalment en dies de la setmana seleccionats
- Mesos o anys, en dates del calendari o amb patrons de dia de la setmana

</details>

<details>
<summary>Puc definir l'import en moneda fiduciària?</summary>

Sí. Pots definir l'import en:

- Bitcoin
- Una moneda fiduciària compatible

Els imports en moneda fiduciària poden utilitzar:

- Un tipus de canvi en temps real
- La tarifa de CoinGecko, fixada a les 00:00 GMT

També es pot establir una substitució del tipus de canvi per al següent pagament.

</details>

<details>
<summary>Es reutilitzen les adreces?</summary>

No. Cada adreça del destinatari s'utilitza només una vegada. Quan s'acaben les adreces d'un destinatari, pots afegir-ne més per a aquest destinatari.

</details>

<details>
<summary>Bitcoin-Safe envia els pagaments automàticament?</summary>

No. Quan un pagament venç, Schedule prepara la transacció a Bitcoin-Safe perquè la revisis, i continues sent responsable de signar-la i transmetre-la.

</details>

<details>
<summary>Puc pagar a diversos destinataris alhora?</summary>

Sí. Selecciona diversos pagaments programats i fes clic a **Paga els seleccionats**. Bitcoin-Safe els combinarà en una única transacció per lots.

</details>

<details>
<summary>Què passa si un pagament s'ha fet en efectiu o d'una altra manera?</summary>

Pots afegir un pagament **fora de banda**. Registra el pagament al calendari sense una transacció de Bitcoin, perquè el progrés es mantingui exacte.

</details>
</content>
