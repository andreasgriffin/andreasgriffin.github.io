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


Bitcoin Safe 1.6.0 introduce los **Filtros Compactos de Bloques (CBF)** como una forma opcional de sincronizar tu monedero. En lugar de consultar a un servidor Electrum centralizado por el historial de tu monedero, Bitcoin Safe ahora puede descargar un pequeño archivo resumen de cada bloque directamente desde nodos aleatorios de Bitcoin Core. Estos resúmenes actúan como una breve lista de verificación que permite a tu monedero decidir por sí mismo si un bloque podría contener una de tus transacciones.

Como Bitcoin Safe toma la decisión de forma local, ningún servidor tercero llega a saber qué direcciones o transacciones te interesan. Obtienes los mismos datos de confirmación que conservaría un nodo completo, pero en un formato más ligero que cabe en dispositivos cotidianos.

**Por qué resulta mejor:**

- 📦 **Descargas pequeñas:** Cada filtro ocupa solo unos pocos kilobytes, por lo que puedes sincronizarte a través de conexiones domésticas normales sin almacenar toda la cadena de bloques.
- 🔐 **Directo desde la red:** Bitcoin Safe se comunica con varios nodos aleatorios de Bitcoin Core, igual que hacen otros nodos, reduciendo la posibilidad de que un único observador pueda perfilarte.
- 🕵️ **Coincidencia local:** Tu monedero comprueba los filtros de forma local. Si un filtro parece relevante, solo entonces descarga el bloque específico, manteniendo tus direcciones privadas.

Los servidores Electrum, en cambio, buscan en la cadena de bloques en tu nombre. Cada petición comparte direcciones de tu monedero con el operador del servidor, que podría registrar esa información. Con los filtros compactos de bloques, Bitcoin Safe descarga los mismos datos neutrales que comparte cualquier nodo. Nadie puede saber qué direcciones te pertenecen porque tu monedero nunca las revela en primer lugar.

A continuación hay una vista sencilla de cómo se conecta Bitcoin Safe cuando CBF está activado. Observa cómo refleja la manera en que los nodos de Bitcoin Core ya se comunican entre sí:


![Bitcoin Safe descarga filtros compactos de bloques desde varios nodos aleatorios de Bitcoin Core.](logo.jpg)
{ .img-fluid .mb-5   style="max-width: 450px;" }


Puedes elegir a cuántos nodos debe conectarse Bitcoin Safe. Más nodos necesitan más ancho de banda y resultan en un tiempo de sincronización más lento. El valor predeterminado es 2.

 
### Qué esperar al sincronizar

CBF cambia el tiempo de espera dependiendo de lo que estés haciendo:

1. ✨ **Configurar o recuperar un monedero:** Ya sea que crees un monedero nuevo o recuperes uno existente, la sincronización inicial descarga filtros para todo el historial de bloques. Espera que este proceso único tarde **entre 5 y 30 minutos**, según la velocidad de tu conexión a Internet.
2. 🚀 **Abrir un monedero que ya estaba sincronizado:** Bitcoin Safe solo necesita obtener los filtros más recientes desde tu última sesión. Esa puesta al día suele completarse en **menos de 30 segundos**.
3. 🔄 **Cambiar de servidores Electrum a CBF:** Dado que el monedero ya estaba sincronizado con servidores Electrum, Bitcoin Safe solo necesita obtener los filtros más nuevos, lo cual generalmente será **menos de 30 segundos**.

### Mantente informado sobre pagos no confirmados

Los filtros compactos de bloques cubren únicamente los **bloques confirmados**. Para enterarte de transacciones entrantes antes de que se confirmen, asegúrate también de habilitar [Notificaciones instantáneas de transacciones]({{< ref "knowledge/instant-transactions-notifications/" >}}). Esa función escucha los mensajes en vivo peer-to-peer de un nodo Bitcoin aleatorio para que puedas reaccionar a la actividad del mempool sin renunciar a la privacidad.


<br>
<br>



### Detalles técnicos


- *Para desarrolladores que quieran profundizar:* los filtros compactos de bloques siguen la especificación [BIP158](https://bips.dev/158/) y se exploran en el [resumen de Elle Mouton sobre los conjuntos codificados con Golomb](https://ellemouton.com/posts/bip158/). La implementación de Bitcoin Safe se basa en el módulo de filtros compactos Kyoto de código abierto para BDK: [Kyoto compact block filter module for BDK](https://github.com/rustaceanrob/kyoto).
- Puedes añadir tu propio nodo de Bitcoin Core a los pares para la sincronización de Filtros Compactos de Bloques, eligiendo el _Nodo inicial_ de la _Supervisión de la red Bitcoin_.


![](inital-node.png)
{ .img-fluid .mb-5   style="max-width: 414px;" }