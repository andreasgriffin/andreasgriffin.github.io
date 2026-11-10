---
title: "Notificaciones de la billetera"
description: "Reenvía las notificaciones de la billetera y de la aplicación Bitcoin-Safe a los destinos que configures, con controles de entrega, privacidad y tiempos."
draft: false
tags: ["Plugins"]
images: ["notifications.png"]
weight: 35
faq:
  title: "Preguntas sobre las notificaciones de la billetera"
  items:
    - question: "¿A dónde puede enviar notificaciones Bitcoin-Safe?"
      answer: "Bitcoin-Safe puede enviar notificaciones a:\n- Webhooks: JSON genérico, o formatos compatibles con Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy y Gotify\n- Mensajes directos de Nostr\n- Bots de Telegram\n- Correo electrónico mediante SMTP\n- Calendarios CalDAV"
    - question: "¿Puedo evitar que las alertas incluyan detalles sensibles?"
      answer: "Sí. Activa la opción de ocultar detalles sensibles y el mensaje solo contendrá un aviso genérico de que se produjo un evento de notificación de Bitcoin-Safe."
    - question: "¿Controlo qué eventos llegan a cada destino?"
      answer: "Cada destino tiene sus propias reglas. Eliges qué tipos de eventos recibe:\n- Transacciones de la billetera\n- Pagos programados\n- Sincronización y chat\n- Advertencias\n\nTambién puedes configurar un retraso aleatorio opcional en la entrega."
    - question: "¿La aplicación tiene que seguir desbloqueada?"
      answer: "No. Bloquear y minimizar a la bandeja mantiene Bitcoin-Safe en ejecución en segundo plano mientras la billetera permanece bloqueada."
---

### {{< page-title >}}

<p class="lead">Recibe avisos de la actividad de tu billetera a través de los canales que te convengan.</p>

<ul class="plugin-features">
<li>Transacciones entrantes y salientes, mensajes de Sync&Chat, pagos programados vencidos, ...</li>
<li>Envía alertas a webhooks, Nostr, Telegram, correo electrónico, calendarios y más</li>
<li>Elige qué eventos recibe cada destino y oculta los detalles sensibles</li>
<li>Mantén Bitcoin-Safe en segundo plano; usa <strong>Bloquear y minimizar a la bandeja</strong> para dejarlo en ejecución mientras la billetera está bloqueada</li>
</ul>

### Configurar un webhook

{{< video "webhook.mp4" controls >}}

### Mensajes directos de Nostr

{{< video "nostr.mp4" controls >}}

### Notificaciones de calendario

{{< video "calendar.mp4" controls >}}

### Conectar tus destinos

- Añade uno o varios destinos. Cada uno puede tener sus propios destinatarios y reglas de entrega.
- **Correo electrónico:** conexión directa a un servidor SMTP con host, puerto, credenciales, remitente y ajustes de seguridad. No es una integración gestionada de Gmail u Outlook.
- **Telegram:** envío a un chat mediante un bot. Inicia una conversación con el bot para comprobarlo y detectar los IDs de chat recientes.
- **Nostr DM:** envío de mensajes NIP-17 cifrados a destinatarios `npub` a través de relés configurados con una clave de remitente.
- **CalDAV:** añade eventos a un calendario existente, como un calendario de Nextcloud configurado.
- **Webhooks:** envío en JSON genérico o en formatos para endpoints compatibles con Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy y Gotify. Los tipos de endpoint comunes pueden detectarse automáticamente.
- Guarda los ajustes del destino y usa la acción de prueba cuando esté disponible.

### Elegir qué se envía

- Elige qué tipos de eventos recibe cada destino:
  - Transacciones de la billetera
  - Pagos programados
  - Sincronización y chat
  - Advertencias
- Oculta los detalles sensibles. El mensaje contendrá entonces solo un aviso genérico de que se produjo un evento de notificación de Bitcoin-Safe.
- Configura un retraso aleatorio en la entrega hasta el máximo que elijas.
- Los mensajes de transacciones de la billetera pueden incluir un enlace al explorador cuando esté disponible y los detalles no estén ocultos.

### Revisar las entregas

- El historial reciente muestra cada evento, destino, adaptador, hora y resultado: enviado, parcial o fallido.
- La entrega depende del destino configurado y de su disponibilidad. Ten en cuenta qué información envías a servicios externos.

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
<summary>¿A dónde puede enviar notificaciones Bitcoin-Safe?</summary>

Bitcoin-Safe puede enviar notificaciones a:

- Webhooks: JSON genérico, o formatos compatibles con Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy y Gotify
- Mensajes directos de Nostr
- Bots de Telegram
- Correo electrónico mediante SMTP
- Calendarios CalDAV

</details>

<details>
<summary>¿Puedo evitar que las alertas incluyan detalles sensibles?</summary>

Sí. Activa la opción de ocultar detalles sensibles y el mensaje solo contendrá un aviso genérico de que se produjo un evento de notificación de Bitcoin-Safe.

</details>

<details>
<summary>¿Controlo qué eventos llegan a cada destino?</summary>

Cada destino tiene sus propias reglas. Eliges qué tipos de eventos recibe:

- Transacciones de la billetera
- Pagos programados
- Sincronización y chat
- Advertencias

También puedes configurar un retraso aleatorio opcional en la entrega.

</details>

<details>
<summary>¿La aplicación tiene que seguir desbloqueada?</summary>

No. Bloquear y minimizar a la bandeja mantiene Bitcoin-Safe en ejecución en segundo plano mientras la billetera permanece bloqueada.

</details>
</content>
