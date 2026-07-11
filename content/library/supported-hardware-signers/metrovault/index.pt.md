---
aliases:
- /pt/knowledge/supported-hardware-signers/metrovault/
title: MetroVault
signer: metrovault
bucket: knowledge
---

MetroVault pode transformar um dispositivo Android antigo num dispositivo dedicado de assinatura Bitcoin offline para o Bitcoin Safe. Nao o instales no teu telefone de uso diario. Reposiciona primeiro o dispositivo, mantem-no **OFFLINE** e desligado da internet, e usa-o apenas para assinar.

## O que esperar

- Reposiciona um dispositivo Android antigo antes da instalacao e usa-o apenas como assinador.
- Nao instales outras aplicacoes, nao inicies sessao em contas, nao coloques um cartao SIM nem voltes a ligar o dispositivo a internet.
- Troca dados da carteira, descritores e PSBT com o Bitcoin Safe atraves de codigos QR.
- Regista descritores multisig e exporta dados do assinador para o Bitcoin Safe.
- Verifica todos os detalhes no ecra do MetroVault antes de assinar.

## Reposiciona o dispositivo Android e usa-o apenas como assinador offline

A documentacao upstream do MetroVault tem agora um [guia completo de configuracao do dispositivo](https://github.com/gorunjinian/MetroVault/blob/main/docs/DEVICE_SETUP.md). Recomendamos fortemente que o sigas passo a passo e o trates como um requisito: usa um telefone dedicado, reposto de fabrica e **OFFLINE** que permaneça desligado da internet apos a configuracao e seja usado apenas para assinar.

1. Reposiciona o telefone para as definicoes de fabrica antes da instalacao.
2. Ignora a configuracao da conta Google e mantem o dispositivo offline.
3. Deixa o modo de aviao ativado permanentemente.
4. Desativa Wi-Fi, Bluetooth, NFC e dados moveis.
5. Remove o cartao SIM.
6. Desativa a depuracao USB.
7. Nao instales outras aplicacoes nem uses o telefone para nada alem de assinar.

Para uso em producao, compila a partir do codigo-fonte sempre que possivel. Se nao conseguires manter o dispositivo offline e dedicado apenas a assinar, nao o uses para fundos de producao no MetroVault.
