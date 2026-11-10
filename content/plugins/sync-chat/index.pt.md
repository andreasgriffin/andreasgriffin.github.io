---
title: "Sync & Chat"
description: "Encontre pares na sua carteira, sincronize rótulos e categorias, converse com segurança e compartilhe PSBTs com um clique."
draft: false
tags: ["Plugins", "sync-chat-mainpage"]
images: ["logo.png"]
weight: 30
faq:
  title: "Perguntas sobre Sync & Chat"
  items:
    - question: "Como os dispositivos se encontram?"
      answer: "O Sync & Chat procura outros dispositivos que usam o mesmo descritor de carteira. O descritor passa por hash antes de ser usado na busca, por isso não é exposto em texto simples. Além disso, cada dispositivo encontrado precisa ser adicionado e marcado como confiável manualmente antes de poder participar do chat. Assim o chat continua seguro mesmo que o descritor não seja secreto."
    - question: "Como funciona a colaboração na prática?"
      answer: "1. Configuração (uma vez): adicione e marque como confiável o dispositivo de cada participante.\n2. Criar: um participante cria uma PSBT e adiciona sua assinatura.\n3. Compartilhar: a PSBT é enviada a todos os participantes, ou apenas a alguns selecionados.\n4. Assinar: cada participante adiciona sua assinatura até a transação estar totalmente assinada.\n5. Transmitir: o último signatário transmite a transação, que então aparece na carteira de todos os participantes."
    - question: "O que é sincronizado?"
      answer: "O Sync & Chat cuida de:\n- Categorias e rótulos de moedas, sincronizados entre os signatários, mesmo entre sistemas operacionais diferentes\n- Compartilhamento de PSBTs com um clique"
    - question: "O chat é privado?"
      answer: "Sim. O chat da carteira é criptografado e funciona via Nostr; os backups dos rótulos também são armazenados criptografados via Nostr."
---

### {{< page-title >}}

<p class="lead">Coordene os signatários multisig e mantenha o contexto da carteira sincronizado diretamente no Bitcoin-Safe.</p>

<ul class="plugin-features">
<li>Descubra outros dispositivos que usam o mesmo descritor de carteira</li>
<li>Sincronize rótulos e categorias entre os signatários</li>
<li>Converse com segurança e compartilhe PSBTs com um clique</li>
</ul>

### Sincronização de rótulos

{{< video src="../../library/label-sync/label-sync.mp4" controls="true" >}}

### Assinatura colaborativa

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

Para o guia completo de assinatura colaborativa multisig, veja [Colaboração em um multisig]({{< ref "library/collaboration/" >}}).

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
<summary>Como os dispositivos se encontram?</summary>

O Sync & Chat procura outros dispositivos que usam o mesmo descritor de carteira. O descritor passa por hash antes de ser usado na busca, por isso não é exposto em texto simples. Além disso, cada dispositivo encontrado precisa ser adicionado e marcado como confiável manualmente antes de poder participar do chat. Assim o chat continua seguro mesmo que o descritor não seja secreto.

</details>

<details>
<summary>Como funciona a colaboração na prática?</summary>

1. **Configuração (uma vez):** adicione e marque como confiável o dispositivo de cada participante.
2. **Criar:** um participante cria uma PSBT e adiciona sua assinatura.
3. **Compartilhar:** a PSBT é enviada a todos os participantes, ou apenas a alguns selecionados.
4. **Assinar:** cada participante adiciona sua assinatura até a transação estar totalmente assinada.
5. **Transmitir:** o último signatário transmite a transação, que então aparece na carteira de todos os participantes.

</details>

<details>
<summary>O que é sincronizado?</summary>

O Sync & Chat cuida de:

- Categorias e rótulos de moedas, sincronizados entre os signatários, mesmo entre sistemas operacionais diferentes
- Compartilhamento de PSBTs com um clique

</details>

<details>
<summary>O chat é privado?</summary>

Sim. O chat da carteira é criptografado e funciona via Nostr; os backups dos rótulos também são armazenados criptografados via Nostr.

</details>

{{< sync-page-box >}}
</content>
