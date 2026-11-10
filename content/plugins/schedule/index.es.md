---
title: "Pagos programados"
description: "Planifica pagos de Bitcoin únicos o recurrentes, sigue cuándo vencen y prepara las transacciones para revisarlas en Bitcoin-Safe."
draft: false
tags: ["Plugins"]
images: ["schedule.png"]
weight: 40
faq:
  title: "Preguntas sobre los pagos programados"
  items:
    - question: "¿Puedo programar un pago único o solo recurrentes?"
      answer: "Ambos. Puedes crear un pago único, un número fijo de repeticiones o un calendario continuo."
    - question: "¿Con qué frecuencia puede repetirse un calendario?"
      answer: "Los intervalos de repetición disponibles son:\n- Minutos, horas o días\n- Semanas, opcionalmente en días de la semana seleccionados\n- Meses o años, en fechas del calendario o con patrones de día de la semana"
    - question: "¿Puedo fijar el importe en moneda fiduciaria?"
      answer: "Sí. Puedes fijar el importe en:\n- Bitcoin\n- Una moneda fiduciaria compatible\n\nLos importes en moneda fiduciaria pueden usar:\n- Un tipo de cambio en tiempo real\n- La tasa de CoinGecko, fijada a las 00:00 GMT\n\nTambién puedes sustituir el tipo de cambio para el siguiente pago."
    - question: "¿Se reutilizan las direcciones?"
      answer: "No. Cada dirección de destinatario se usa una sola vez. Cuando se agotan las direcciones de un destinatario, puedes añadir más para ese destinatario."
    - question: "¿Bitcoin-Safe envía los pagos automáticamente?"
      answer: "No. Cuando un pago vence, Schedule prepara la transacción en Bitcoin-Safe para que la revises, y tú sigues siendo responsable de firmarla y emitirla."
    - question: "¿Puedo pagar a varios destinatarios a la vez?"
      answer: "Sí. Selecciona varios pagos programados y haz clic en **Pagar seleccionados**. Bitcoin-Safe los combinará en una única transacción por lotes."
    - question: "¿Qué pasa si un pago se hizo en efectivo o de otra forma?"
      answer: "Puedes añadir un pago **fuera de banda**. Registra el pago en tu calendario sin una transacción de Bitcoin, para que el progreso siga siendo exacto."
---

### {{< page-title >}}

<p class="lead">Planifica pagos en Bitcoin y deja que Schedule controle lo que vence.</p>

<ul class="plugin-features">
<li>Pagar a empleados u organizar otras obligaciones periódicas</li>
<li>Configurar transferencias recurrentes</li>
<li>Programar un pago único que no debes olvidar</li>
</ul>

Cuando un pago vence, Schedule prepara la transacción en Bitcoin-Safe para que la revises. Tú sigues siendo responsable de firmarla y emitirla.

{{< video "schedule.mp4" controls >}}

### Planes de pago flexibles

- Elige un pago único, un número fijo de repeticiones o un calendario continuo.
- Define una fecha de inicio y un intervalo de repetición: minutos, horas, días, semanas, meses o años. Los calendarios semanales pueden usar días de la semana seleccionados; los mensuales y anuales admiten fechas del calendario y patrones de día de la semana.
- Define un destinatario, una categoría y un importe en bitcoin o en una moneda fiduciaria compatible.
- Para importes en moneda fiduciaria, usa un tipo de cambio en tiempo real o la tasa de CoinGecko fijada a las 00:00 GMT. Puedes configurar una sustitución del tipo de cambio para el siguiente pago.
- Los calendarios de número fijo muestran vistas previas del importe por pago y del total.

### Preparar pagos en tu billetera

- Consulta la próxima fecha de vencimiento y el progreso de los pagos; los pagos vencidos se resaltan y pueden activar un aviso de Bitcoin-Safe.
- Prepara un pago vencido o un lote en el compositor de transacciones, con las salidas de los destinatarios, etiquetas y categorías ya rellenadas.
- Revisa y personaliza la transacción antes de firmarla y emitirla tú mismo.
- Guarda destinatarios reutilizables con un nombre y varias direcciones. Schedule puede seleccionar una dirección sin usar para un pago.

### Seguir y gestionar los calendarios

- Busca calendarios por estado de vencimiento, tipo de calendario o categoría. Las listas muestran fechas, pagos completados, frecuencia, destinatario, importe, categoría y total.
- Revisa los pagos realizados y las próximas ocurrencias. Las transacciones coincidentes de la billetera pueden actualizar el progreso; también puedes añadir un pago manualmente o volver a analizar las transacciones.
- Edita un calendario antes de su primer pago registrado, duplícalo o elimínalo, e importa/exporta calendarios como copia de seguridad en JSON.

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">Descargar Bitcoin-Safe</h2>
<p class="text-muted mb-3">Los plugins vienen incluidos con Bitcoin-Safe. Descarga la aplicación para probarlos.</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">Descargar Bitcoin-Safe</a>
<small class="text-muted">Software libre y de código abierto · Windows, macOS, Linux</small>
</div>
</section>

### Preguntas frecuentes

<details>
<summary>¿Puedo programar un pago único o solo recurrentes?</summary>

Ambos. Puedes crear un pago único, un número fijo de repeticiones o un calendario continuo.

</details>

<details>
<summary>¿Con qué frecuencia puede repetirse un calendario?</summary>

Los intervalos de repetición disponibles son:

- Minutos, horas o días
- Semanas, opcionalmente en días de la semana seleccionados
- Meses o años, en fechas del calendario o con patrones de día de la semana

</details>

<details>
<summary>¿Puedo fijar el importe en moneda fiduciaria?</summary>

Sí. Puedes fijar el importe en:

- Bitcoin
- Una moneda fiduciaria compatible

Los importes en moneda fiduciaria pueden usar:

- Un tipo de cambio en tiempo real
- La tasa de CoinGecko, fijada a las 00:00 GMT

También puedes sustituir el tipo de cambio para el siguiente pago.

</details>

<details>
<summary>¿Se reutilizan las direcciones?</summary>

No. Cada dirección de destinatario se usa una sola vez. Cuando se agotan las direcciones de un destinatario, puedes añadir más para ese destinatario.

</details>

<details>
<summary>¿Bitcoin-Safe envía los pagos automáticamente?</summary>

No. Cuando un pago vence, Schedule prepara la transacción en Bitcoin-Safe para que la revises, y tú sigues siendo responsable de firmarla y emitirla.

</details>

<details>
<summary>¿Puedo pagar a varios destinatarios a la vez?</summary>

Sí. Selecciona varios pagos programados y haz clic en **Pagar seleccionados**. Bitcoin-Safe los combinará en una única transacción por lotes.

</details>

<details>
<summary>¿Qué pasa si un pago se hizo en efectivo o de otra forma?</summary>

Puedes añadir un pago **fuera de banda**. Registra el pago en tu calendario sin una transacción de Bitcoin, para que el progreso siga siendo exacto.

</details>
</content>
