---
title: "Notificações instantâneas de transações"
description: "Como o Bitcoin Safe recebe notificações instantâneas de transações"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [
  "carteira Bitcoin segura para famílias",
  "bitcoin",
  "poupança de bitcoin",
  "assinador de hardware",
  "Custódios de Bitcoin",
  "Consultores Financeiros",
  "carteira bitcoin",
  "trezor",
  "bitcoin nos EUA",
  "BTC",
  "HODL",
  "Segurança do Bitcoin",
  "Notificações instantâneas de transações"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---



![](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }


### {{< page-title >}}  
 
  


**Bitcoin Safe** (a partir da versão **1.5.0**) suporta notificações instantâneas de transações Bitcoin relevantes para a sua carteira. Eis como funciona nos bastidores:




##### 1. 📡 A escuta da rede P2P do Bitcoin

O Bitcoin Safe liga-se diretamente a um ou mais **nós Bitcoin Core**, que participam na rede global **peer-to-peer (P2P)**. Esses nós trocam continuamente transacções recém-difundidas destinadas a serem incluídas no **mempool**.

O Bitcoin Safe escuta passivamente essas mensagens de difusão e verifica se:

* alguma transacção envolve **endereços** ou **UTXOs** da sua carteira.

✅ **Preservação da privacidade**
Este método é **completamente privado**. Não **revela nada** sobre a sua carteira ao mundo exterior.
O Bitcoin Safe comporta-se exatamente como um nó Bitcoin Core normal: limita-se a ouvir o tráfego público P2P — nunca anunciando ou solicitando algo específico da sua carteira.



##### 2. 🧠 Correspondência encontrada — O que acontece a seguir?

Se for encontrada uma transacção correspondente, o Bitcoin Safe reagirá de forma diferente dependendo do backend que estiver a utilizar:

###### Opção A: ⚡ Backend Electrum ou Esplora

* O Bitcoin Safe irá **disparar uma sincronização em segundo plano** para obter a transacção completa e o estado da carteira a partir do servidor.

###### Opção B: 🔍 Filtros de Blocos Compactos (Modo Neutrino)

* A carteira irá **adicionar directamente a transacção não confirmada** aos dados locais da sua carteira — sem necessidade de pesquisa adicional.



#### ⚙️ Comportamento de Ativação/Desativação

Para respeitar as preferências do utilizador e as definições de privacidade:

* 🔒 **Para utilizadores existentes** que atualizem para a versão 1.5.0 ou posterior, esta funcionalidade é **por opt-in por defeito** — pode ativá‑la manualmente nas definições de rede.
* 🚀 **Para novos utilizadores**, esta funcionalidade vem **ativada (opt-out)** por defeito, dado que é simultaneamente **preservadora da privacidade** e **muito útil** para acompanhar a actividade da carteira em tempo real.

Permanece em controlo total e pode alternar esta funcionalidade a qualquer momento.
 
 


#### ⚠️ Apenas transacções confirmadas são fiáveis

O Bitcoin Safe não consegue validar que uma transacção difundida seja válida. Um atacante — especialmente se controlar tanto o seu servidor Electrum como o nó Bitcoin ao qual está ligado — poderia:

* Forjar uma transacção falsa envolvendo o seu endereço
* Difundi‑la para desencadear uma notificação na carteira
* Garantir que ela nunca é confirmada, porque é **inválida** ou **entra em conflito com as regras de consenso**


  


#### ✅ Resumo

A partir da versão **1.5.0**, o Bitcoin Safe suporta notificações instantâneas de transacções através de:

* Escuta passiva da rede P2P do Bitcoin (como o Bitcoin Core)
* Correspondência de transacções que envolvem os **endereços** ou **UTXOs** da sua carteira
* Obtenção dos detalhes completos via Electrum/Esplora ou adição directa via Filtros de Blocos Compactos
* Nunca revelar quaisquer dados da carteira ao mundo exterior