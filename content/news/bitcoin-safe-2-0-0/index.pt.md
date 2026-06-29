---
title: "Bitcoin Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "Notas de lancamento do Bitcoin Safe 2.0.0, com um assistente de configuracao reconstruido, sincronizacao privada com Compact Block Filters e suporte ampliado a carteiras de hardware."
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">Anuncio de lancamento</p>
    <h2 class="display-6 mb-3">Bitcoin Safe 2.0 - configuracao guiada de carteira, sincronizacao privada da cadeia e assinatura focada no dispositivo</h2>
    <p class="lead mb-4">Esta versao traz um assistente de configuracao reconstruido, sincronizacao privada da cadeia com Compact Block Filters e um fluxo de assinatura organizado em torno de cada dispositivo de hardware. Se voce tinha curiosidade sobre cold storage, mas ainda estava em duvida, esta e a versao para testar.</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Baixar Bitcoin Safe 2.0</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">Ver o que ha de novo</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Configuracao de carteira passo a passo</h2>
          <p class="mb-0">O novo assistente explica cada etapa, reduz ambiguidades e ajuda novas pessoas usuarias a escolher o caminho certo sem perder o poder do multisig.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Sincronizacao privada da carteira</h2>
          <p class="mb-0">Novas carteiras agora sincronizam com Compact Block Filters desde o inicio, para que voce possa escanear a cadeia em privado sem depender de um indexador Electrum de terceiros.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Assinatura focada no dispositivo</h2>
          <p class="mb-0">Os fluxos de assinatura agora permanecem centrados no dispositivo a sua frente, com proximos passos mais claros para QR, USB, Bluetooth, arquivos e coordenacao multisig.</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## Um caminho guiado para a autocustodia {#setup-flow}

A experiencia de primeiro uso foi reconstruida do zero. Bitcoin Safe continua voltado para uma autocustodia seria, incluindo multisig com suporte de hardware, e a versao 2.0 agora oferece a novas pessoas usuarias um caminho guiado por essa configuracao. O novo assistente explica o que esta acontecendo, em que ponto do fluxo voce esta e o que cada signer precisa de voce antes de prosseguir.

<p class="small text-muted">Para detalhes de implementacao, veja o <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a>.</p>

Destaques do redesign:

- Uma nova tela de boas-vindas que ajuda quem esta usando pela primeira vez a escolher o ponto de partida correto
- Um fluxo de progresso passo a passo durante a criacao da carteira
- Telas de assinatura especificas por dispositivo com instrucoes focadas e ajuda contextual
- PDFs de recuperacao com nomes e icones dos dispositivos para manter os backups sem ambiguidade

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## Sincronizacao privada e robusta da cadeia com Compact Block Filters {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) agora impulsionam a sincronizacao de novas carteiras no Bitcoin Safe 2.0. Em vez de perguntar a um servidor Electrum quais enderecos pertencem a voce, o Bitcoin Safe agora pode escanear a cadeia de forma privada baixando filtros compactos de pares aleatorios do Bitcoin Core e verificando tudo localmente.

<p class="small text-muted">Para detalhes de implementacao, veja o <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a>.</p>


- A sincronizacao da carteira permanece privada desde a primeira execucao
- Sem dependencia de servidores Electrum de terceiros
- O Electrum continua disponivel para quem o preferir
- [Sincronizacao instantanea apos o escaneamento inicial da carteira]({{< ref "library/compact-block-filters" >}})
- [Notificacoes instantaneas de transacoes retransmitidas]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## Um fluxo de assinatura focado no dispositivo para cada dispositivo {#device-focused-signing}

O redesign tambem remodela o fluxo de assinatura depois da criacao da carteira. Em vez de uma tela generica para cada signer, o Bitcoin Safe agora centraliza as acoes em torno do dispositivo especifico que voce esta usando.

<p class="small text-muted">Para detalhes de implementacao, veja o <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a>.</p>

- Acoes de QR, USB, Bluetooth, exportacao/importacao de arquivos e Sync & Chat sao mostradas diretamente no cartao do signer ativo
- Signers restantes, dispositivos que ja assinaram e a proxima acao necessaria permanecem visiveis de relance
- Fluxos multisig com dispositivos mistos permanecem legiveis porque a identidade de cada signer continua visivel em todo o PSBT
- Transacoes complexas com uma mistura de entradas single-sig e multisig sao tratadas corretamente, para que cada etapa de assinatura fique clara

![Cartao do signer com acoes especificas por dispositivo para QR, USB, Bluetooth, exportacao de arquivo e Chat & Sync](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Arquitetura de plugins para fluxos de trabalho empresariais e power users

Bitcoin Safe 2.0 tambem estabelece a base para plugins futuros adicionais voltados a empresas de Bitcoin e power users. Entao vale a pena ficar de olho no que vem por ai :-)

<p class="small text-muted">Para detalhes de implementacao, veja o <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a>.</p>

- Distribuicao de plugins por meio de um repositorio externo de *sources*
- Cada plugin e *assinado com GPG* por [andreasgriffin]({{< gpg_key_link >}}) para garantir seguranca, integridade e entrega
- Versionamento individual de plugins e atualizacoes permitem um desenvolvimento mais rapido e independente

![Cartao do signer com acoes especificas por dispositivo para QR, USB, Bluetooth, exportacao de arquivo e Chat & Sync](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Suporte mais amplo a dispositivos e polimento {#hardware-support}

- Codigos QR animados **30%** mais rapidos para uma leitura mais rapida
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) agora e suportado via USB
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) agora oferece suporte a **Bluetooth**, alem de USB e QR
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) e [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) adicionados como dispositivos suportados
- Veja a [lista completa de dispositivos suportados]({{< ref "library/supported-hardware-signers" >}})
- Foram adicionadas verificacoes automatizadas de [reprodutibilidade]({{< ref "library/reproducibility-and-security" >}})
- Veja aqui a [lista completa](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0) de melhorias


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## Os pontos fortes existentes continuam aqui

A release 2.0 nao e um recomeço. Por baixo do novo onboarding e do fluxo de assinatura, o Bitcoin Safe continua com os recursos que o tornavam util no dia a dia: multisig colaborativo, backups em PDF, historico pesquisavel da carteira, visualizacoes de fluxo de dinheiro, sincronizacao de labels e muito mais.

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">Pronto para experimentar o Bitcoin Safe 2.0?</h2>
  <p class="mb-3">Baixe a versao mais recente e explore por conta propria o novo onboarding, a sincronizacao privada e as melhorias para carteiras de hardware.</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Baixar Bitcoin Safe</a>
</div>


<br><br>

## Obrigado

Esta release se apoia em muito trabalho de contribuidores, testers e [apoiadores do projeto]({{< ref "donate" >}}):

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r)) pelo redesign do assistente, pelo trabalho de UI dos plugins e pelo suporte UI/UX **incrivel e incansavel**
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) pelo cliente de Compact Block Filters que agora impulsiona a sincronizacao privada de novas carteiras
- A equipe do [Bitcoin Dev Kit](https://github.com/bitcoindevkit/) pelas bibliotecas no centro do Bitcoin Safe
- A equipe do [ndk](https://github.com/nostr-dev-kit/ndk) pelas bibliotecas que impulsionam a funcionalidade nostr
- Toda a comunidade do Bitcoin Safe que testou release candidates, relatou bugs, traduziu paginas, enviou sats e continuou levando o projeto adiante
- [Tradutores]({{< ref "donate/#translators" >}}), incluindo <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (Vietnamita)" title="qdyg-vn 🇻🇳 (Vietnamita)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (Alemao)" title="bsn21m 🇩🇪 (Alemao)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (Espanhol)" title="cyphra 🇪🇸 (Espanhol)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (Chines)" title="DaGrindDontStop 🇨🇳 (Chines)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


Se quiser ajudar a financiar a proxima release, voce tambem pode doar aqui: {{< donation_btc >}}
