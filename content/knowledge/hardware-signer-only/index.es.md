---
title: "Firmantes hardware obligatorios"
description: "Bitcoin Safe requiere semillas solo en hardware en Mainnet para maximizar la seguridad y evitar los riesgos del almacenamiento de claves en software. Aquí explicamos por qué importa."
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

 

![Bitcoin Safe logo](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }

## 🚫 ¿Por qué Bitcoin Safe bloquea las semillas de software en Mainnet?

🤔 ¿No es eso incómodo?

🔥 Resulta que — es una **mejora de seguridad importante**.

Bitcoin Safe **solo permite semillas de software en Testnet, Signet y Regtest** — nunca en Mainnet. He aquí por qué:

### ✅ Razones por las que las semillas de software están bloqueadas en Mainnet

- 🧠 **Las semillas de software son inseguras**
  - Los ordenadores están llenos de riesgos: secuestradores del portapapeles, malware, exploits en el navegador.
  - Un solo fallo y tu semilla queda comprometida — se acabó el juego.
  - El almacenamiento en frío nunca debe empezar estando caliente.

</br>

- 🧊 **El almacenamiento en frío debe nacer frío**
  - Los usuarios a menudo generan semillas en monederos de software y luego las migran a hardware.
  - Pero la exposición inicial ya ocurrió — no hay vuelta atrás.
  - Verdadero almacenamiento en frío = creado en un firmante de hardware desde el principio.

</br>

- 🎣 **El phishing prospera con los hábitos de software**
  - Escribir semillas en aplicaciones te enseña a confiar en patrones de UX peligrosos.
  - Solo hardware fuerza mejores hábitos y limita la exposición.
  - ✅ Semillas fuera de Mainnet = menos víctimas de phishing.

</br>

- 🧪 **Los desarrolladores aún tienen flexibilidad**
  - Las semillas de software *sí* están permitidas en:
    - Testnet
    - Signet
    - Regtest
  - Ideal para desarrolladores. Sin riesgo para sats reales. 🧡



</br>


- 🔐 **Mainnet requiere firmantes hardware — sin excepciones**
  - 🔌 USB, 📷 QR, y 💾 tarjeta SD con todos los dispositivos principales
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

## 🛡️ Protección contra envenenamiento de direcciones

Bitcoin Safe **colorea las direcciones de recepción** para hacer obvio el envenenamiento de direcciones:

- 🟢 Verde = dirección de recepción verificada  
- 🟡 Amarillo = dirección de cambio  

Si alguien intenta envenenar tu portapapeles con una dirección falsa, la verás al instante.

![Ejemplo de detección de envenenamiento de direcciones](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ Verificación de direcciones vía USB o QR

Verifica las direcciones de recepción directamente en tu firmante de hardware — no necesitas confiar en la pantalla.

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ Instrucciones para cada firmante de hardware
 
- {{<text-name-with-logo>}} incluye capturas de pantalla e instrucciones para cada firmante de hardware que te guían en cada paso 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-images >}}
    </div>

   
---



## 🤝 Multisig colaborativo, fácil

Bitcoin Safe hace que el multisig sea fácil de usar y apto para equipos:

- 🔐 Chat Nostr cifrado  
- 🔁 Compartir PSBT con 1 clic  
- 🔌 USB, 📷 QR, y 💾 tarjeta SD

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ Funciones potentes para todos los usuarios

- 🟧 Asistente para monedero singlesig  
- 🟨 Configuración multisig 2-de-3  
- 🟩 Cualquier configuración n-de-m  
- 🖨️ Hojas de respaldo PDF imprimibles  
- 🔁 Sincronización de etiquetas vía Nostr  
- 🔍 Diagrama completo del flujo de dinero y historial de transacciones buscable

![Diagrama de transacciones en Bitcoin Safe](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 Global y fácil de usar

- Soporte multilingüe: {{< flags-short >}}
- Funciona en: Windows, macOS & Linux  
- Arrastrar y soltar PSBT / CSV  
- Filtros avanzados para transacciones, UTXOs, montos y más

---

## 💡 Resumen rápido

Bitcoin Safe = Verdadero ahorro en Bitcoin:

✅ Solo hardware en Mainnet  
✅ Sin exposición de semillas de software  
✅ Multisig apto para principiantes  
✅ Entornos de prueba amigables para desarrolladores  
✅ Funciones listas para familia y equipos  

🔗 [Bitcoin-Safe.org]({{< ref "/" >}})  
🎥 Canal de YouTube →: https://youtube.com/@BitcoinSafeOrg