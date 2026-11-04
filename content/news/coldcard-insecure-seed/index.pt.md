---
title: "Seed COLDCARD insegura"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "Guia mínimo para transferir fundos de uma seed gerada num dispositivo Coinkite."
---

[A Coinkite divulgou uma falha na geração de seeds no firmware COLDCARD afetado](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). Consulta também [a análise técnica da Block sobre o fallback previsível do RNG e o reseed de 32 bits](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware). Atualizar o firmware não corrige uma seed existente.

**Se criaste uma seed com qualquer produto Coinkite, migra RAPIDAMENTE!**

## Lista de verificação da migração

1. Gera uma seed completamente nova num **dispositivo de assinatura que não seja COLDCARD** ([ver dispositivos suportados]({{< ref "library/supported-hardware-signers" >}})). Não reutilizes a seed antiga. Depois, usa esse signer com o assistente de configuração do Bitcoin-Safe para criar uma nova [carteira de assinatura única]({{< ref "library/setup-singlesig-wallet" >}}) ou [carteira multifirma]({{< ref "library/setup-multisig-wallet" >}}).
   - Se não estiver disponível nenhum hardware signer que não seja COLDCARD, o [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}}) é uma opção num dispositivo Android dedicado, reposto de fábrica, mantido offline e utilizado apenas para assinar.
   - Conclui o teste de receção e envio do assistente para garantir que a nova carteira está corretamente configurada: verifica a cópia de segurança e um endereço de receção no novo signer, recebe um pequeno montante de teste e efetua com sucesso um autoenvio para outro endereço verificado da nova carteira.
2. Assina a transação de migração:
   - **Se a carteira afetada for de assinatura única:** transmite-a normalmente com uma taxa elevada para que seja confirmada rapidamente.
   - **Se a carteira afetada for multifirma:** não a transmitas normalmente, porque isso revela as suas chaves públicas na mempool pública. Copia a transação bruta assinada e envia-a diretamente através do [MARA Slipstream](https://slipstream.mara.com/).
3. Mantém o COLDCARD antigo até que o saldo completo tenha chegado e sido confirmado na nova carteira; depois, atualiza-o para o firmware mais recente.

Se estiveres a ajudar alguém a migrar, nunca lhe peças para partilhar, fotografar ou digitar as palavras da seed. A seed deve permanecer privada e ser introduzida apenas no dispositivo de assinatura.
