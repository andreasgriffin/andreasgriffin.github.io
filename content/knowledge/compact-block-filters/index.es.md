---
title: "Filtros compactos de bloques"
description: "Entender qué son los filtros compactos de bloques y cómo mejoran la privacidad frente a servidores Electrum."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "filtros compactos de bloques"
  - "CBF"
  - "privacidad"
  - "monedero Bitcoin"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**Los filtros compactos de bloques (CBF)** permiten a [Bitcoin Safe]({{< ref "/" >}}) analizar la cadena sin preguntar a un servidor Electrum qué direcciones son tuyas.

![Bitcoin Safe descarga filtros compactos de bloques desde varios pares aleatorios de Bitcoin Core.](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

En lugar de consultar a un servidor central, Bitcoin Safe descarga un filtro pequeño para cada bloque desde pares aleatorios de Bitcoin Core. Tu monedero comprueba esos filtros localmente y solo descarga los bloques completos cuando hace falta.

### CBF frente a Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">Aspecto</th>
        <th scope="col">Filtros compactos de bloques</th>
        <th scope="col">Servidor Electrum</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Privacidad</th>
        <td><span class="text-success fw-semibold">Bien</span> - Los datos del monedero siguen siendo locales</td>
        <td><span class="text-danger fw-semibold">Mal</span> - El servidor puede ver tus direcciones y tu historial</td>
      </tr>
      <tr>
        <th scope="row">Fuente de datos</th>
        <td><span class="text-success fw-semibold">Bien</span> - Pares aleatorios de Bitcoin Core</td>
        <td><span class="text-warning fw-semibold">Neutral</span> - Un solo servidor elegido</td>
      </tr>
      <tr>
        <th scope="row">Sincronización inicial</th>
        <td><span class="text-warning fw-semibold">Neutral</span> - Normalmente más lenta</td>
        <td><span class="text-success fw-semibold">Bien</span> - Normalmente más rápida</td>
      </tr>
      <tr>
        <th scope="row">Sincronización continua</th>
        <td><span class="text-success fw-semibold">Bien</span> - Muy rápida después de la primera sincronización</td>
        <td><span class="text-success fw-semibold">Bien</span> - Normalmente rápida</td>
      </tr>
      <tr>
        <th scope="row">Ideal para</th>
        <td><span class="text-success fw-semibold">Bien</span> - Usuarios que priorizan la privacidad</td>
        <td><span class="text-success fw-semibold">Bien</span> - La configuración y recuperación más rápidas</td>
      </tr>
    </tbody>
  </table>
</div>

### Por qué usar CBF

- Mejor privacidad: tu monedero nunca le pide a un servidor qué direcciones son tuyas.
- Sin indexador de confianza: Bitcoin Safe se comunica directamente con la red Bitcoin.
- Sincronización ligera: los filtros son pequeños, así que no necesitas toda la cadena de bloques.

### Qué esperar

- Monedero nuevo o recuperación: normalmente **5 a 30 minutos** para la primera sincronización.
- Monedero ya sincronizado: normalmente se pone al día **muy rápido**, a menudo en **menos de 30 segundos**.
- Cambio de Electrum a CBF: normalmente también **menos de 30 segundos**.

Puedes elegir a cuántos pares se conecta Bitcoin Safe. Más pares mejoran la redundancia, pero normalmente aumentan el uso de ancho de banda y el tiempo de sincronización. El valor predeterminado es **2** pares.

### Transacciones no confirmadas

CBF cubre solo los **bloques confirmados**. Para recibir también alertas de pagos no confirmados, deja [Notificaciones instantáneas de transacciones]({{< ref "knowledge/instant-transactions-notifications/" >}}) activadas, que es el comportamiento predeterminado.

### Nota técnica

Los filtros compactos de bloques están definidos en [BIP158](https://bips.dev/158/). Bitcoin Safe usa el módulo de código abierto [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto).

También puedes usar tu propio nodo de Bitcoin Core como par inicial en los ajustes de _Supervisión de la red Bitcoin_.

![Ajuste de nodo inicial](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
