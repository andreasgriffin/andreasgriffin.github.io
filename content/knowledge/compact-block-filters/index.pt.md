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


O [Bitcoin Safe]({{< ref "/" >}}) 1.6.0 introduz **Filtros Compactos de Bloco (CBF)** como uma forma opcional de sincronizar a sua carteira. Em vez de perguntar a um servidor Electrum centralizado pelo histórico da sua carteira, o [Bitcoin Safe]({{< ref "/" >}}) pode agora descarregar um pequeno ficheiro resumo para cada bloco diretamente de nós aleatórios do Bitcoin Core. Esses resumos funcionam como uma lista de verificação curta que permite à sua carteira decidir por si só se um bloco pode conter uma das suas transacções.

Como o [Bitcoin Safe]({{< ref "/" >}}) toma a decisão localmente, nenhum servidor terceiro alguma vez fica a saber quais endereços ou transacções o interessam. Obtém os mesmos dados de confirmação que um nó completo armazenaria, mas num formato mais leve que se adequa a dispositivos do dia a dia.

**Porque parece melhor:**

- 📦 **Transferências pequenas:** Cada filtro tem apenas alguns kilobytes, pelo que pode sincronizar através de ligações domésticas normais sem armazenar toda a blockchain.
- 🔐 **Direto da rede:** O [Bitcoin Safe]({{< ref "/" >}}) comunica com múltiplos nós aleatórios do Bitcoin Core, tal como outros nós fazem, reduzindo a hipótese de um único observador o poder perfilar.
- 🕵️ **Verificação local:** A sua carteira verifica os filtros localmente. Se um filtro parecer relevante, só então descarrega o bloco específico, mantendo os seus endereços privados.

Os servidores Electrum, em contraste, pesquisam a blockchain em seu nome. Cada pedido partilha endereços da sua carteira com o operador do servidor, que poderia registar essa informação. Com filtros compactos de bloco, o [Bitcoin Safe]({{< ref "/" >}}) descarrega os mesmos dados neutros que todos os nós partilham. Ninguém consegue saber quais endereços lhe pertencem porque a sua carteira nunca os revela em primeiro lugar.

Abaixo está uma visão simples de como o [Bitcoin Safe]({{< ref "/" >}}) se liga quando o CBF está ativado. Repare como espelha a forma como os nós do Bitcoin Core já comunicam entre si:


![O [Bitcoin Safe]({{< ref "/" >}}) descarrega filtros compactos de bloco a partir de vários nós aleatórios do Bitcoin Core.](logo.jpg)
{ .img-fluid .mb-5   style="max-width: 450px;" }


Pode escolher com quantos nós o [Bitcoin Safe]({{< ref "/" >}}) deve ligar-se. Mais nós exigem mais largura de banda e resultam numa sincronização mais lenta. O predefinido é 2.  

 
### O que esperar durante a sincronização

CBF altera o tempo de espera consoante o que estiver a fazer:

1. ✨ **Configuração ou recuperação de uma carteira:** Quer crie uma carteira nova ou recupere uma existente, a sincronização inicial descarrega filtros para todo o histórico da sua carteira. Espere que este processo único demore **entre 5 e 30 minutos**, dependendo da sua velocidade de internet.
2. 🚀 **Abrir uma carteira que já estava sincronizada:** O [Bitcoin Safe]({{< ref "/" >}}) só precisa de obter os filtros mais recentes desde a sua última sessão. Esse ajuste normalmente termina em **menos de 30 segundos**.
3. 🔄 **Mudar de servidores Electrum para CBF:** Como a carteira foi previamente sincronizada com servidores Electrum, o [Bitcoin Safe]({{< ref "/" >}}) só precisa de obter os filtros mais recentes, o que normalmente será **menos de 30 segundos**.

### Mantenha-se informado sobre pagamentos não confirmados

Os filtros compactos de bloco cobrem apenas **blocos confirmados**. Para ser notificado sobre transacções recebidas antes de serem confirmadas, certifique-se de também activar as [Notificações instantâneas de transações]({{< ref "knowledge/instant-transactions-notifications/" >}}). Essa funcionalidade escuta as mensagens peer-to-peer em tempo real de um nó Bitcoin aleatório, para que possa reagir à actividade do mempool sem perder privacidade.


<br>
<br>



### Detalhes técnicos


- *Para desenvolvedores que queiram aprofundar:* os filtros compactos de bloco seguem a especificação [BIP158](https://bips.dev/158/) e são explorados no [resumo de Elle Mouton sobre Golomb-coded sets](https://ellemouton.com/posts/bip158/). A implementação do [Bitcoin Safe]({{< ref "/" >}}) baseia-se no módulo open-source [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto).
- Pode adicionar o seu próprio nó Bitcoin Core aos pares para sincronização de Filtros Compactos de Bloco, escolhendo o _Nó inicial_ do _Monitor de rede Bitcoin_.


![](inital-node.png)
{ .img-fluid .mb-5   style="max-width: 414px;" }