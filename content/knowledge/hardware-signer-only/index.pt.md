---
title: "Assinadores de Hardware Obrigatórios"
description: "O Bitcoin Safe impõe seeds apenas em hardware na Mainnet para maximizar a segurança e evitar os riscos do armazenamento de chaves por software. Aqui está o porquê."
draft: false
tags: ["Featured", "Knowledge" ]
keywords: [
  "Bitcoin Safe",
  "carteira de hardware",
  "semente de software",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "multisig",
  "PSBT",
  "autocustódia",
  "segurança do Bitcoin",
  "envenenamento de endereços",
  "ferramentas Bitcoin"
]
images: ["logo.png" ]
# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=dbSmQmt0uDI"
weight: 21
---

 

![](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }

## 🚫 Porque é que o Bitcoin Safe bloqueia seeds de software na Mainnet?

🤔 Não é isso inconveniente?

🔥 A verdade é — é uma **grande melhoria de segurança**.

O Bitcoin Safe **permite seeds de software apenas em Testnet, Signet e Regtest** — nunca na Mainnet. Eis porquê:

### ✅ Razões pelas quais as seeds de software são bloqueadas na Mainnet

- 🧠 **As seeds de software são inseguras** 
  - Os computadores estão cheios de riscos: sequestradores de área de transferência, malware, exploits de navegador.
  - Um único deslize e a sua seed fica comprometida — é o fim do jogo.
  - O cold storage nunca deve começar quente.

</br>

- 🧊 **O cold storage tem de nascer frio**
  - Os utilizadores frequentemente geram seeds em carteiras de software e depois migram para hardware.
  - Mas a exposição inicial já aconteceu — não há volta a dar.
  - Cold storage verdadeiro = criado num assinador de hardware desde o início.

</br>

- 🎣 **O phishing prospera com hábitos de software**
  - Escrever seeds em apps treina-o a confiar em padrões de UX maus.
  - A política apenas-hardware força melhores hábitos e limita a exposição.
  - ✅ Mainnet sem seeds = menos vítimas de phishing.

</br>

- 🧪 **Os desenvolvedores continuam a ter flexibilidade**
  - Seeds de software *são* permitidas em:
    - Testnet
    - Signet
    - Regtest
  - Ideal para desenvolvedores. Sem risco para sats reais. 🧡



</br>


- 🔐 **A Mainnet exige assinadores de hardware — sem exceções**
  - 🔌 USB, 📷 QR, e 💾 cartão SD com todos os dispositivos principais
    - [Coldcard]({{< ref "knowledge/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Foundation Passport]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Ledger]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Keystone]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "knowledge/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "knowledge/supported-hardware-signers" >}})
  - [Ver todos os assinadores suportados →]({{< ref "knowledge/supported-hardware-signers" >}})


---

## 🛡️ Proteção contra envenenamento de endereços

O Bitcoin Safe **codifica a cores os endereços de receção** para tornar o envenenamento de endereços óbvio:

- 🟢 Verde = endereço de receção verificado  
- 🟡 Amarelo = endereço de troco  

Se alguém tentar envenenar a sua área de transferência com um endereço falso, voi-lo-á ver instantaneamente.

![Address poisoning detection example](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ Verificação de endereços via USB ou QR

Verifique endereços de receção diretamente no seu assinador de hardware — não precisa confiar no ecrã.

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ Instruções para cada assinador de hardware
 
- {{<text-name-with-logo>}} inclui instruções com capturas de ecrã para cada assinador de hardware para o guiar em cada passo 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-hardware-signer-screenshots >}}
    </div>

   
---



## 🤝 Multisig colaborativo facilitado

O Bitcoin Safe torna o multisig fácil de usar e pronto para equipas:

- 🔐 Chat Nostr encriptado  
- 🔁 Partilha de PSBT com 1 clique  
- 🔌 USB, 📷 QR, e 💾 cartão SD

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ Funcionalidades poderosas para todos os utilizadores

- 🟧 Assistente para wallet singlesig  
- 🟨 Configuração multisig 2-de-3  
- 🟩 Qualquer configuração n-de-m  
- 🖨️ Folhas de backup em PDF imprimíveis  
- 🔁 Sincronização de etiquetas via Nostr  
- 🔍 Diagrama completo de fluxo de fundos e histórico de transações pesquisável

![Transaction diagram in Bitcoin Safe](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 Global e fácil de usar

- Suporte multilingue: {{< flags-short >}}
- Funciona em: Windows, macOS & Linux  
- Arrastar e largar PSBT / CSV  
- Filtros avançados para transações, UTXOs, montantes e mais

---

## 💡 Resumo rápido

Bitcoin Safe = poupanças reais em Bitcoin:

✅ Apenas hardware na Mainnet  
✅ Sem exposição da seed por software  
✅ Multisig fácil para principiantes  
✅ Ambientes de teste amigáveis para desenvolvedores  
✅ Funcionalidades prontas para família e equipas  

🔗 [Bitcoin-Safe.org](https://Bitcoin-Safe.org)  
🎥 Canal YouTube →: https://youtube.com/@BitcoinSafeOrg