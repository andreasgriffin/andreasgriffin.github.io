---
aliases:
  - "/pt/features/reproducibility-and-security/"
title: "Seguranca e reprodutibilidade"
description: "O Bitcoin-Safe segue padroes elevados de seguranca binaria: builds reproduziveis, commits assinados, releases assinadas e monitorizacao externa independente."
draft: false
bucket: features
tags: ["Featured", "Security"]
images: ["logo.png"]
keywords: ["reproducible builds", "verify binaries", "signed commits", "signed releases", "appimage", "flatpak", "windows exe", "binary security"]
weight: 18
---

### {{< page-title >}}
{{< page-description >}}
<br>

![Resultados de builds reproduziveis para Bitcoin-Safe](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 500px;" }

Implementamos varias camadas de protecao para a integridade dos downloads no site, para que a aplicacao que descarrega corresponda realmente ao codigo-fonte publico:

- **Builds reproduziveis**: Os builds Linux `deb`, `AppImage` e `Flatpak`, bem como os ficheiros Windows `portable exe` e `setup exe`, podem ser reproduzidos byte por byte. Se um ficheiro recompilado corresponder exatamente, isso e uma forte evidencia de que o binario foi gerado a partir do mesmo codigo-fonte.
- **Historico assinado do repositorio**: O [repositorio GitHub do Bitcoin-Safe](https://github.com/andreasgriffin/bitcoin-safe/commits/main) publica commits assinados e verificados, para que os revisores possam confirmar quem criou o codigo que entrou numa release.
- **Binarios assinados**: Os ficheiros de release sao assinados com a [chave publica PGP]({{< gpg_key_link >}}) do Bitcoin-Safe, e os binarios Windows seguem tambem a [politica de assinatura de codigo]({{< ref "code-signing-policy" >}}).
- **Verificacoes independentes de reprodutibilidade**: [WalletScrutiny](https://walletscrutiny.com/desktop/bitcoin.safe/) acompanha o Bitcoin-Safe de forma independente e mostra o estado da verificacao reproduzivel para as releases desktop.
- **Monitorizacao continua de assinaturas**: [BinaryWatch](https://binarywatch.org/) verifica regularmente os ficheiros de release do Bitcoin-Safe e se as respetivas assinaturas continuam validas face a [chave publica PGP]({{< gpg_key_link >}}) do Bitcoin-Safe.
- **Verificacao de atualizacoes**: As atualizacoes sao mostradas no Bitcoin-Safe e a respetiva assinatura e verificada automaticamente.

Em conjunto, estas medidas colocam o Bitcoin-Safe num pequeno grupo de projetos que tratam a seguranca dos binarios como uma parte central da seguranca do utilizador, e nao como um detalhe adicionado mais tarde.

### A seguranca e a consideracao principal em todos os aspetos do Bitcoin-Safe

Para alem da integridade binaria, o Bitcoin-Safe foi concebido com predefinicoes seguras, boas praticas operacionais e orientacao clara para o utilizador. Alguns exemplos:

- **Custodia centrada em hardware**: O Bitcoin-Safe exige [assinantes de hardware]({{< ref "library/supported-hardware-signers" >}}), para que as seeds permaneçam em dispositivos dedicados em vez de se tornarem segredos expostos num computador de uso geral.
- **Fluxo de configuracao mais seguro**: O assistente de configuracao ajuda a criar wallets realmente prontas para uso real, incluindo testes de [assinantes de hardware]({{< ref "library/supported-hardware-signers" >}}), [folhas PDF de backup]({{< ref "library/pdf-export/" >}}) e orientacoes sobre como guardar os assinantes de hardware e os backups de seed.
- **Verificacao de enderecos de rececao**: O Bitcoin-Safe facilita [verificar enderecos de rececao]({{< ref "library/verify-receive-address/" >}}) no proprio assinante antes de os partilhar.
- **Detecao de envenenamento de enderecos**: Avisa sobre [enderecos suspeitos e parecidos]({{< ref "library/address-poisoning/" >}}).
- **Seguranca multisig**: O Bitcoin-Safe suporta wallets multisig, para que montantes maiores possam ser protegidos por varios dispositivos ou pessoas em vez de um unico ponto de falha.
- **Colaboracao que torna a multisig mais facil**: O Bitcoin-Safe torna a [colaboracao multisig]({{< ref "library/collaboration/" >}}) pratica, tornando muito mais facil coordenar a configuracao e a assinatura no mundo real.
- **Fluxos de assinatura claros**: Ecras de assinatura especificos por dispositivo reduzem a confusao durante a revisao de PSBTs e ajudam os utilizadores a tomar a acao correta no assinante correto.
