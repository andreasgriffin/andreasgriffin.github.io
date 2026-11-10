---
title: "Sync & Chat"
description: "Descubre pares en tu billetera, sincroniza etiquetas y categorías, chatea de forma segura y comparte PSBT con un clic."
draft: false
tags: ["Plugins", "sync-chat-mainpage"]
images: ["logo.png"]
weight: 30
faq:
  title: "Preguntas sobre Sync & Chat"
  items:
    - question: "¿Cómo se encuentran los dispositivos?"
      answer: "Sync & Chat busca otros dispositivos que usen el mismo descriptor de billetera. El descriptor se somete a hash antes de usarse para la búsqueda, por lo que no se expone en texto plano. Además, cada dispositivo encontrado debe añadirse y marcarse como de confianza manualmente antes de poder participar en el chat. Así el chat sigue siendo seguro aunque el descriptor no sea secreto."
    - question: "¿Cómo funciona la colaboración en la práctica?"
      answer: "1. Configuración (una sola vez): añade y marca como de confianza el dispositivo de cada participante.\n2. Crear: un participante crea una PSBT y añade su firma.\n3. Compartir: la PSBT se envía a todos los participantes, o solo a los seleccionados.\n4. Firmar: cada participante añade su firma hasta que la transacción esté completamente firmada.\n5. Emitir: el último firmante emite la transacción, y después aparece en la billetera de todos los participantes."
    - question: "¿Qué se sincroniza?"
      answer: "Sync & Chat gestiona:\n- Categorías y etiquetas de monedas, sincronizadas entre firmantes, incluso entre sistemas operativos distintos\n- Compartir PSBT con un clic"
    - question: "¿Es privado el chat?"
      answer: "Sí. El chat de la billetera está cifrado y funciona a través de Nostr; las copias de seguridad de las etiquetas también se almacenan cifradas mediante Nostr."
---

### {{< page-title >}}

<p class="lead">Coordina a los firmantes de multifirma y mantén sincronizado el contexto de la billetera desde Bitcoin-Safe.</p>

<ul class="plugin-features">
<li>Descubre otros dispositivos que usan el mismo descriptor de billetera</li>
<li>Sincroniza etiquetas y categorías entre firmantes</li>
<li>Chatea de forma segura y comparte PSBT con un clic</li>
</ul>

### Sincronización de etiquetas

{{< video src="../../library/label-sync/label-sync.mp4" controls="true" >}}

### Firma colaborativa

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

Para la guía completa de firma colaborativa multifirma, consulta [Colaboración en una multifirma]({{< ref "library/collaboration/" >}}).

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
<summary>¿Cómo se encuentran los dispositivos?</summary>

Sync & Chat busca otros dispositivos que usen el mismo descriptor de billetera. El descriptor se somete a hash antes de usarse para la búsqueda, por lo que no se expone en texto plano. Además, cada dispositivo encontrado debe añadirse y marcarse como de confianza manualmente antes de poder participar en el chat. Así el chat sigue siendo seguro aunque el descriptor no sea secreto.

</details>

<details>
<summary>¿Cómo funciona la colaboración en la práctica?</summary>

1. **Configuración (una sola vez):** añade y marca como de confianza el dispositivo de cada participante.
2. **Crear:** un participante crea una PSBT y añade su firma.
3. **Compartir:** la PSBT se envía a todos los participantes, o solo a los seleccionados.
4. **Firmar:** cada participante añade su firma hasta que la transacción esté completamente firmada.
5. **Emitir:** el último firmante emite la transacción, y después aparece en la billetera de todos los participantes.

</details>

<details>
<summary>¿Qué se sincroniza?</summary>

Sync & Chat gestiona:

- Categorías y etiquetas de monedas, sincronizadas entre firmantes, incluso entre sistemas operativos distintos
- Compartir PSBT con un clic

</details>

<details>
<summary>¿Es privado el chat?</summary>

Sí. El chat de la billetera está cifrado y funciona a través de Nostr; las copias de seguridad de las etiquetas también se almacenan cifradas mediante Nostr.

</details>

{{< sync-page-box >}}
</content>
