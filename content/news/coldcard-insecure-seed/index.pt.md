---
title: "Seed COLDCARD insegura"
date: "2026-08-02"
draft: false
description: "A Coinkite divulgou uma falha crítica na geração de seeds no firmware COLDCARD afetado. Se criaste uma seed com qualquer dispositivo Coinkite afetado, transfere os teus fundos para uma nova seed."
images: ["COLDCARD Security Advisory Notice - Migrate ASAP.png"]
---

## Resumo

[A Coinkite divulgou uma falha crítica na geração de seeds no firmware COLDCARD afetado](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). [A análise técnica da Block](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware) identificou como causa um gerador de números aleatórios por software previsível usado em vez do RNG de hardware do dispositivo, e alerta que **está em curso uma exploração ativa**. Atualizar o firmware **não** corrige uma seed existente.

**Se criaste uma seed com qualquer dispositivo Coinkite afetado, transfere os teus fundos para uma nova seed.**

## O meu dispositivo está afetado?

A exposição depende da **versão do firmware que estava instalada quando a seed foi gerada**, não de quando o dispositivo foi fabricado.

| Dispositivo | Firmware usado para gerar a seed | Estado |
|---|---|---|
| Mk1 | Todo o firmware lançado | Não afetado |
| Mk2 / Mk3 | v3.2.2 ou anterior | Não afetado (usa RNG de hardware) |
| Mk2 / Mk3 | v4.0.0 – v4.1.9 | **Vulnerável** — sem reseed seguro |
| Mk4 | Produção v5.0.0 em diante | **Vulnerável** — limitado a ~72 bits de entropia |
| Q | Todo o firmware de produção | **Vulnerável** — limitado a ~72 bits de entropia |
| Mk5 | Todo o firmware de produção | **Vulnerável** — limitado a ~72 bits de entropia |
| TAPSIGNER, OPENDIME, SATSCARD | — | Não afetado (código diferente) |

Repara que exportar uma seed insegura e importá-la noutra carteira **não** a corrige: a própria seed continua afetada.

## Instala o firmware corrigido antes de gerar uma nova seed

O firmware corrigido está agora disponível para cada modelo e canal de lançamento afetados. Não geres uma nova seed numa COLDCARD até o instalares.

| Dispositivo | Firmware corrigido |
|---|---|
| Mk2 / Mk3 | 4.2.0 ou posterior |
| Mk4 / Mk5 (standard) | 5.6.0 ou posterior |
| Q (standard) | 1.5.0Q ou posterior |
| Mk4 / Mk5 (Edge) | 6.6.0X ou posterior |
| Q (Edge) | 6.6.0QX ou posterior |

Standard e Edge são canais de lançamento separados. Se usas Edge, instala a versão Edge corrigida para o teu modelo: não assumas que uma versão antiga de Edge 6.x está corrigida apenas porque o seu número é superior ao da versão standard.

## Os lançamentos de dados ou uma frase de acesso protegem-me?

- **Lançamentos de dados:** o bug afeta apenas a entropia gerada pelo dispositivo. Se introduziste pelo menos **50 lançamentos de dados independentes e privados** ao criar a seed (99 ou mais para aproximadamente 256 bits de entropia), a entrada dos dados por si só contribuiu com pelo menos 128 bits de entropia independente e a seed não é considerada em risco por este problema isoladamente. Com menos de 50 lançamentos — ou se não tens a certeza de quantos foram introduzidos ou se eram privados — **migra**.
- **Frase de acesso BIP-39:** uma frase de acesso BIP-39 forte e única (não o PIN da COLDCARD) acrescenta uma barreira independente, mas **não** corrige a seed afetada. Se a tua frase de acesso é curta, comum, reutilizada ou adivinhável — ou se não tens a certeza da sua robustez — trata os fundos como em risco e migra imediatamente. Mesmo com uma frase de acesso forte, migra para uma seed recém-gerada assim que for possível.

## Lista de verificação para a migração

Migra com calma e cuidado. Apressar uma migração de carteira pode criar um risco mais imediato do que o problema que tentas resolver.

1. **Instala o firmware corrigido** do teu modelo antes de gerar uma seed de substituição. Se preferires, gera a nova seed num **dispositivo de assinatura que não seja COLDCARD** ([consulta os dispositivos suportados]({{< ref "library/supported-hardware-signers" >}})) — em qualquer caso, **não** reutilizes a seed antiga.
2. Gera uma seed completamente nova e **regista-a**. Antes de depositar fundos, verifica a cópia de segurança escrita, a impressão digital da carteira e um endereço de receção.
3. Usa o assistente de configuração do Bitcoin-Safe para criar uma nova [carteira de assinatura única]({{< ref "library/setup-singlesig-wallet" >}}) ou [carteira multisignature]({{< ref "library/setup-multisig-wallet" >}}) com a nova seed.
4. Conclui o teste de receção e envio do assistente: verifica a cópia de segurança e um endereço de receção no novo assinante, recebe um pequeno valor de teste e envia-o com sucesso para outro endereço verificado na nova carteira.
5. Assina e transmite a transação de migração:
   - **Carteira de assinatura única:** transmite-a normalmente com uma taxa elevada para confirmar rapidamente.
   - **Carteira multisignature:** não a transmites normalmente, porque isso revela as suas chaves públicas no mempool público. Copia a transação em bruto assinada e submete-a diretamente através do [MARA Slipstream](https://slipstream.mara.com/).
6. Mantém a COLDCARD antiga e a sua cópia de segurança até o **saldo completo** ter chegado e sido confirmado na nova carteira. Só então apaga a seed antiga.

Se a Mk2/Mk3 é o teu único dispositivo de assinatura, instala primeiro o firmware 4.2.0 ou posterior: ele gera corretamente seeds de substituição, por isso não precisas de uma COLDCARD mais recente para concluir a migração. Segue os mesmos passos, alternando com cuidado entre a seed antiga e a nova no único dispositivo, e mantém a cópia de segurança antiga até a migração estar totalmente confirmada.

## Se usas multisignature

Se uma configuração multisignature é composta **exclusivamente** por dispositivos afetados, a vulnerabilidade continua a aplicar-se. Protege a configuração com um quórum que inclua pelo menos um dispositivo de assinatura não afetado.

## Ajudar outra pessoa a migrar

Nunca lhe peças para partilhar, fotografar ou escrever as palavras seed. A seed deve permanecer privada e ser introduzida apenas no próprio dispositivo de assinatura.
