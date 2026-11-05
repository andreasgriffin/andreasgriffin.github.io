---
title: "Pagamentos agendados"
description: "Planeje pagamentos em Bitcoin únicos ou recorrentes, acompanhe quando vencem e prepare transações para revisão no Bitcoin-Safe."
draft: false
tags: ["Plugins"]
images: ["schedule.png"]
weight: 40
faq:
  title: "Perguntas sobre pagamentos agendados"
  items:
    - question: "Posso agendar um pagamento único ou apenas recorrentes?"
      answer: "Ambos. Você pode criar um pagamento único, um número fixo de repetições ou um agendamento contínuo."
    - question: "Com que frequência um agendamento pode se repetir?"
      answer: "Os intervalos de repetição disponíveis são:\n- Minutos, horas ou dias\n- Semanas, opcionalmente em dias da semana selecionados\n- Meses ou anos, em datas do calendário ou com padrões de dia da semana"
    - question: "Posso definir o valor em moeda fiduciária?"
      answer: "Sim. Você pode definir o valor em:\n- Bitcoin\n- Uma moeda fiduciária suportada\n\nValores em moeda fiduciária podem usar:\n- Uma taxa de câmbio em tempo real\n- A taxa da CoinGecko, fixada às 00:00 GMT\n\nTambém é possível definir uma substituição da taxa de câmbio para o próximo pagamento."
    - question: "Os endereços são reutilizados?"
      answer: "Não. Cada endereço de destinatário é usado apenas uma vez. Quando os endereços de um destinatário acabam, você pode adicionar mais para ele."
    - question: "O Bitcoin-Safe envia os pagamentos automaticamente?"
      answer: "Não. Quando um pagamento vence, o Schedule prepara a transação no Bitcoin-Safe para sua revisão, e você continua responsável por assiná-la e transmiti-la."
    - question: "Posso pagar vários destinatários de uma vez?"
      answer: "Sim. Selecione vários pagamentos agendados e clique em **Pagar selecionados**. O Bitcoin-Safe os combina em uma única transação em lote."
    - question: "E se um pagamento foi feito em dinheiro ou de outra forma?"
      answer: "Você pode adicionar um pagamento **fora da carteira**. Ele registra o pagamento no agendamento sem uma transação Bitcoin, para que o progresso continue preciso."
---

### {{< page-title >}}

<p class="lead">Planeje pagamentos em Bitcoin e deixe o Schedule acompanhar o que está para vencer.</p>

<ul class="plugin-features">
<li>Pagar funcionários ou organizar outras obrigações regulares</li>
<li>Configurar transferências recorrentes</li>
<li>Agendar um pagamento único que você não pode esquecer</li>
</ul>

Quando um pagamento vence, o Schedule prepara a transação no Bitcoin-Safe para sua revisão. Você continua responsável por assiná-la e transmiti-la.

{{< video "schedule.mp4" controls >}}

### Planos de pagamento flexíveis

- Escolha um pagamento único, um número fixo de repetições ou um agendamento contínuo.
- Defina uma data de início e um intervalo de repetição: minutos, horas, dias, semanas, meses ou anos. Agendamentos semanais podem usar dias da semana selecionados; mensais e anuais aceitam datas do calendário e padrões de dia da semana.
- Defina destinatário, categoria e valor em bitcoin ou em uma moeda fiduciária suportada.
- Para valores em moeda fiduciária, use uma taxa em tempo real ou a taxa da CoinGecko fixada às 00:00 GMT. Pode-se definir uma substituição da taxa de câmbio para o próximo pagamento.
- Agendamentos de número fixo mostram prévias do valor por pagamento e do total.

### Preparar pagamentos na carteira

- Veja a próxima data de vencimento e o progresso dos pagamentos; pagamentos vencidos ficam destacados e podem disparar um aviso do Bitcoin-Safe.
- Prepare um pagamento vencido ou um lote no compositor de transações, com as saídas dos destinatários, rótulos e categorias preenchidos.
- Revise e personalize a transação antes de assiná-la e transmiti-la você mesmo.
- Salve destinatários reutilizáveis com um nome e vários endereços. O Schedule pode selecionar um endereço não utilizado para um pagamento.

### Acompanhar e gerenciar agendamentos

- Encontre agendamentos por status de vencimento, tipo ou categoria. As listas mostram datas, pagamentos concluídos, frequência, destinatário, valor, categoria e total.
- Revise os pagamentos realizados e as próximas ocorrências. Transações correspondentes na carteira podem atualizar o progresso; você também pode adicionar um pagamento manualmente ou reexaminar as transações.
- Edite um agendamento antes do primeiro pagamento registrado, duplique-o ou exclua-o, e importe/exporte agendamentos como backup em JSON.

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
<summary>Posso agendar um pagamento único ou apenas recorrentes?</summary>

Ambos. Você pode criar um pagamento único, um número fixo de repetições ou um agendamento contínuo.

</details>

<details>
<summary>Com que frequência um agendamento pode se repetir?</summary>

Os intervalos de repetição disponíveis são:

- Minutos, horas ou dias
- Semanas, opcionalmente em dias da semana selecionados
- Meses ou anos, em datas do calendário ou com padrões de dia da semana

</details>

<details>
<summary>Posso definir o valor em moeda fiduciária?</summary>

Sim. Você pode definir o valor em:

- Bitcoin
- Uma moeda fiduciária suportada

Valores em moeda fiduciária podem usar:

- Uma taxa de câmbio em tempo real
- A taxa da CoinGecko, fixada às 00:00 GMT

Também é possível definir uma substituição da taxa de câmbio para o próximo pagamento.

</details>

<details>
<summary>Os endereços são reutilizados?</summary>

Não. Cada endereço de destinatário é usado apenas uma vez. Quando os endereços de um destinatário acabam, você pode adicionar mais para ele.

</details>

<details>
<summary>O Bitcoin-Safe envia os pagamentos automaticamente?</summary>

Não. Quando um pagamento vence, o Schedule prepara a transação no Bitcoin-Safe para sua revisão, e você continua responsável por assiná-la e transmiti-la.

</details>

<details>
<summary>Posso pagar vários destinatários de uma vez?</summary>

Sim. Selecione vários pagamentos agendados e clique em **Pagar selecionados**. O Bitcoin-Safe os combina em uma única transação em lote.

</details>

<details>
<summary>E se um pagamento foi feito em dinheiro ou de outra forma?</summary>

Você pode adicionar um pagamento **fora da carteira**. Ele registra o pagamento no agendamento sem uma transação Bitcoin, para que o progresso continue preciso.

</details>
</content>
