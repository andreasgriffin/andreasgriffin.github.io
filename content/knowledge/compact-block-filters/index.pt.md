---
title: "Filtros Compactos de Bloco"
description: "Compreenda o que são filtros compactos de bloco e como melhoram a privacidade em relação aos servidores Electrum."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "filtros compactos de bloco"
  - "CBF"
  - "privacidade"
  - "carteira Bitcoin"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**Os filtros compactos de bloco (CBF)** permitem ao [Bitcoin Safe]({{< ref "/" >}}) analisar a blockchain sem perguntar a um servidor Electrum quais endereços são seus.

![O Bitcoin Safe descarrega filtros compactos de bloco de vários pares aleatórios do Bitcoin Core.](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

Em vez de consultar um servidor central, o Bitcoin Safe descarrega um filtro pequeno para cada bloco de pares aleatórios do Bitcoin Core. A sua carteira verifica esses filtros localmente e só descarrega blocos completos quando é necessário.

### CBF vs Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">Aspeto</th>
        <th scope="col">Filtros compactos de bloco</th>
        <th scope="col">Servidor Electrum</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Privacidade</th>
        <td><span class="text-success fw-semibold">Bom</span> - Os dados da carteira permanecem locais</td>
        <td><span class="text-danger fw-semibold">Mau</span> - O servidor pode ver os seus endereços e histórico</td>
      </tr>
      <tr>
        <th scope="row">Fonte de dados</th>
        <td><span class="text-success fw-semibold">Bom</span> - Pares aleatórios do Bitcoin Core</td>
        <td><span class="text-warning fw-semibold">Neutro</span> - Um único servidor escolhido</td>
      </tr>
      <tr>
        <th scope="row">Sincronização inicial</th>
        <td><span class="text-warning fw-semibold">Neutro</span> - Normalmente mais lenta</td>
        <td><span class="text-success fw-semibold">Bom</span> - Normalmente mais rápida</td>
      </tr>
      <tr>
        <th scope="row">Sincronização contínua</th>
        <td><span class="text-success fw-semibold">Bom</span> - Muito rápida depois da primeira sincronização</td>
        <td><span class="text-success fw-semibold">Bom</span> - Normalmente rápida</td>
      </tr>
      <tr>
        <th scope="row">Ideal para</th>
        <td><span class="text-success fw-semibold">Bom</span> - Utilizadores focados na privacidade</td>
        <td><span class="text-success fw-semibold">Bom</span> - A configuração e recuperação mais rápidas</td>
      </tr>
    </tbody>
  </table>
</div>

### Por que usar CBF

- Mais privacidade: a sua carteira nunca pergunta a um servidor quais endereços são seus.
- Sem indexador de confiança: o Bitcoin Safe fala diretamente com a rede Bitcoin.
- Sincronização leve: os filtros são pequenos, por isso não precisa de toda a blockchain.

### O que esperar

- Carteira nova ou recuperação: normalmente **5 a 30 minutos** para a primeira sincronização.
- Carteira já sincronizada: normalmente recupera **muito rápido**, muitas vezes em **menos de 30 segundos**.
- Mudança de Electrum para CBF: normalmente também **menos de 30 segundos**.

Pode escolher com quantos pares o Bitcoin Safe se liga. Mais pares melhoram a redundância, mas normalmente aumentam a largura de banda e o tempo de sincronização. O predefinido é **2** pares.

### Transações não confirmadas

CBF cobre apenas **blocos confirmados**. Para também receber alertas de pagamentos não confirmados, deixe [Notificações instantâneas de transações]({{< ref "knowledge/instant-transactions-notifications/" >}}) ativadas, que é o comportamento padrão.

### Nota técnica

Os filtros compactos de bloco estão definidos no [BIP158](https://bips.dev/158/). O Bitcoin Safe usa o módulo de código aberto [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto).

Também pode usar o seu próprio nó Bitcoin Core como peer inicial nas definições de _Bitcoin network monitoring_.

![Definição do nó inicial](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
