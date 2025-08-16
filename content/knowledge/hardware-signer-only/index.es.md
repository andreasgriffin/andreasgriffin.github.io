---
aliases:
  - "/conocimiento/firmantes-de-hardware-obligatorios/"
title: "Firmantes de hardware obligatorios"
description: "Bitcoin Safe exige semillas generadas solo en hardware en Mainnet para maximizar la seguridad y evitar los riesgos del almacenamiento de claves basado en software. Aquí te explicamos por qué importa."
draft: false
tags: ["Featured", "Knowledge" ]
keywords: [
  "Bitcoin Safe",
  "monedero hardware",
  "semilla de software",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "multisig",
  "PSBT",
  "autocustodia",
  "seguridad de Bitcoin",
  "envenenamiento de direcciones",
  "herramientas de Bitcoin"
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

## 🚫 ¿Por qué Bitcoin Safe bloquea las semillas de software en Mainnet?

🤔 ¿No es eso incómodo?

🔥 Resulta que es una **gran mejora de seguridad**.

Bitcoin Safe **solo permite semillas de software en Testnet, Signet y Regtest** — nunca en Mainnet. He aquí por qué:

### ✅ Motivos por los que las semillas de software se bloquean en Mainnet

- 🧠 **Las semillas de software son inseguras** 
  - Los ordenadores están llenos de riesgos: secuestradores del portapapeles, malware, exploits del navegador.
  - Un desliz y tu semilla queda comprometida — se acabó el juego.
  - El almacenamiento en frío nunca debería empezar en caliente.

</br>

- 🧊 **El almacenamiento en frío debe nacer frío**
  - A menudo se generan semillas en monederos software y luego se migra a hardware.
  - Pero la exposición inicial ya ocurrió — no hay marcha atrás.
  - Auténtico cold storage = creado desde el principio en un firmante de hardware.

</br>

- 🎣 **El phishing se alimenta de hábitos de software**
  - Escribir semillas en apps te acostumbra a confiar en patrones de UX poco seguros.
  - Solo-hardware impone mejores hábitos y limita la exposición.
  - ✅ Mainnet sin introducir la semilla = menos víctimas de phishing.

</br>

- 🧪 **Los desarrolladores siguen teniendo flexibilidad**
  - Las semillas de software *sí* están permitidas en:
    - Testnet
    - Signet
    - Regtest
  - Ideal para devs. Sin riesgo para sats reales. 🧡



</br>

- 🔐 **En Mainnet se requieren firmantes de hardware — sin excepciones**
  - 🔌 USB, 📷 QR y 💾 tarjeta SD con todos los dispositivos principales
    - [Coldcard]({{< ref "knowledge/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Foundation Passport]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Ledger]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Keystone]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "knowledge/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "knowledge/supported-hardware-signers" >}})
  - [Ver todos los firmantes compatibles →]({{< ref "knowledge/supported-hardware-signers" >}})


---

## 🛡️ Protección contra el envenenamiento de direcciones

Bitcoin Safe **usa colores para las direcciones de recepción** para que el envenenamiento de direcciones sea evidente:

- 🟢 Verde = dirección de recepción verificada  
- 🟡 Amarillo = dirección de cambio  

Si alguien intenta envenenar tu portapapeles con una dirección falsa, lo verás al instante.

![Ejemplo de detección de envenenamiento de direcciones](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ Verificación de direcciones por USB o QR

Verifica las direcciones de recepción directamente en tu firmante de hardware — no necesitas confiar en la pantalla.

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ Instrucciones para cada firmante de hardware
 
- {{<text-name-with-logo>}} incluye instrucciones con capturas para cada firmante de hardware que te guían en cada paso. 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-hardware-signer-screenshots >}}
    </div>

   
---



## 🤝 Multisig colaborativo, más fácil

Bitcoin Safe hace que el multisig sea fácil y listo para equipos:

- 🔐 Chat Nostr cifrado  
- 🔁 Compartir PSBT con 1 clic  
- 🔌 USB, 📷 QR y 💾 tarjeta SD

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ Funciones potentes para todos

- 🟧 Asistente de monedero de una sola firma  
- 🟨 Configuración multisig 2-de-3  
- 🟩 Cualquier configuración n-de-m  
- 🖨️ Hojas de copia de seguridad en PDF imprimibles  
- 🔁 Sincronización de etiquetas vía Nostr  
- 🔍 Diagrama completo del flujo de dinero e historial de transacciones con búsqueda

![Diagrama de transacciones en Bitcoin Safe](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 Global y fácil de usar

- Soporte multilingüe: {{< flags-short >}}
- Funciona en: Windows, macOS y Linux  
- Arrastrar y soltar PSBT / CSV  
- Filtros avanzados para transacciones, UTXO, importes y más

---

## 💡 TL;DR

Bitcoin Safe = ahorro real en Bitcoin:

✅ Solo hardware en Mainnet  
✅ Sin exposición de semillas de software  
✅ Multisig apto para principiantes  
✅ Entornos de prueba pensados para desarrolladores  
✅ Funciones listas para familias y equipos  

🔗 [Bitcoin-Safe.org](https://Bitcoin-Safe.org)  
🎥 Canal de YouTube →: https://youtube.com/@BitcoinSafeOrg
