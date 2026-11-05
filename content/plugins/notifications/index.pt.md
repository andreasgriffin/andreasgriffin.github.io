---
title: "Notificações da carteira"
description: "Encaminhe notificações da carteira e do aplicativo Bitcoin-Safe para os destinos que você configurar, com controles de entrega, privacidade e horário."
draft: false
tags: ["Plugins"]
images: ["notifications.png"]
weight: 35
faq:
  title: "Perguntas sobre notificações da carteira"
  items:
    - question: "Para onde o Bitcoin-Safe pode enviar notificações?"
      answer: "O Bitcoin-Safe pode enviar notificações para:\n- Webhooks: JSON genérico, ou formatos compatíveis com Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy e Gotify\n- Mensagens diretas Nostr\n- Bots do Telegram\n- E-mail via SMTP\n- Calendários CalDAV"
    - question: "Posso impedir que os alertas contenham detalhes sensíveis?"
      answer: "Sim. Ative a opção de ocultar detalhes sensíveis e a mensagem conterá apenas um aviso genérico de que ocorreu um evento de notificação do Bitcoin-Safe."
    - question: "Eu controlo quais eventos vão para cada destino?"
      answer: "Cada destino tem suas próprias regras. Você escolhe quais tipos de evento ele recebe:\n- Transações da carteira\n- Pagamentos agendados\n- Sincronização e chat\n- Avisos\n\nVocê também pode definir um atraso aleatório opcional na entrega."
    - question: "O aplicativo precisa continuar desbloqueado?"
      answer: "Não. Bloquear e minimizar para a bandeja mantém o Bitcoin-Safe em execução em segundo plano enquanto a carteira permanece bloqueada."
---

### {{< page-title >}}

<p class="lead">Receba avisos sobre a atividade da sua carteira pelos canais que funcionam para você.</p>

<ul class="plugin-features">
<li>Transações de entrada e saída, mensagens do Sync&Chat, pagamentos agendados vencidos, ...</li>
<li>Encaminhe alertas para webhooks, Nostr, Telegram, e-mail, calendários e muito mais</li>
<li>Escolha quais eventos cada destino recebe e oculte detalhes sensíveis</li>
<li>Mantenha o Bitcoin-Safe em segundo plano; use <strong>Bloquear e minimizar para a bandeja</strong> para deixá-lo em execução enquanto a carteira está bloqueada</li>
</ul>

### Configurar um webhook

{{< video "webhook.mp4" controls >}}

### Mensagens diretas Nostr

{{< video "nostr.mp4" controls >}}

### Notificações de calendário

{{< video "calendar.mp4" controls >}}

### Conecte seus destinos

- Adicione um ou mais destinos. Cada um pode ter seus próprios destinatários e regras de entrega.
- **E-mail:** conexão direta a um servidor SMTP com host, porta, credenciais, remetente e configurações de segurança. Não é uma integração gerenciada com Gmail ou Outlook.
- **Telegram:** envio para um chat por meio de um bot. Inicie uma conversa com o bot para verificá-lo e detectar IDs de chat recentes.
- **Nostr DM:** envio de mensagens NIP-17 criptografadas para destinatários `npub` por meio de relays configurados, com uma chave de remetente.
- **CalDAV:** adição de eventos a um calendário existente, como um calendário Nextcloud configurado.
- **Webhooks:** envio em JSON genérico ou nos formatos de endpoints compatíveis com Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy e Gotify. Tipos comuns de endpoint podem ser detectados automaticamente.
- Salve as configurações do destino e use a ação de teste quando disponível.

### Escolher o que é enviado

- Escolha quais tipos de evento cada destino recebe:
  - Transações da carteira
  - Pagamentos agendados
  - Sincronização e chat
  - Avisos
- Oculte detalhes sensíveis. A mensagem conterá então apenas um aviso genérico de que ocorreu um evento de notificação do Bitcoin-Safe.
- Defina um atraso aleatório na entrega até o máximo escolhido.
- Mensagens sobre transações da carteira podem incluir um link para o explorador, quando disponível e se os detalhes não estiverem ocultos.

### Revisar as entregas

- O histórico recente mostra cada evento, destino, adaptador, horário e resultado: enviado, parcial ou com falha.
- A entrega depende do destino configurado e de sua disponibilidade. Considere quais informações você envia a serviços externos.

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">Baixar o Bitcoin-Safe</h2>
<p class="text-muted mb-3">Os plugins vêm incluídos no Bitcoin-Safe. Baixe o aplicativo para experimentá-los.</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">Baixar o Bitcoin-Safe</a>
<small class="text-muted">Software livre e de código aberto · Windows, macOS, Linux</small>
</div>
</section>

### Perguntas frequentes

<details>
<summary>Para onde o Bitcoin-Safe pode enviar notificações?</summary>

O Bitcoin-Safe pode enviar notificações para:

- Webhooks: JSON genérico, ou formatos compatíveis com Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy e Gotify
- Mensagens diretas Nostr
- Bots do Telegram
- E-mail via SMTP
- Calendários CalDAV

</details>

<details>
<summary>Posso impedir que os alertas contenham detalhes sensíveis?</summary>

Sim. Ative a opção de ocultar detalhes sensíveis e a mensagem conterá apenas um aviso genérico de que ocorreu um evento de notificação do Bitcoin-Safe.

</details>

<details>
<summary>Eu controlo quais eventos vão para cada destino?</summary>

Cada destino tem suas próprias regras. Você escolhe quais tipos de evento ele recebe:

- Transações da carteira
- Pagamentos agendados
- Sincronização e chat
- Avisos

Você também pode definir um atraso aleatório opcional na entrega.

</details>

<details>
<summary>O aplicativo precisa continuar desbloqueado?</summary>

Não. Bloquear e minimizar para a bandeja mantém o Bitcoin-Safe em execução em segundo plano enquanto a carteira permanece bloqueada.

</details>
</content>
