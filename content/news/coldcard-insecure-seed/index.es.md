---
title: "Seed insegura de COLDCARD"
date: "2026-08-02"
draft: false
description: "Coinkite ha revelado una debilidad crítica en la generación de seeds del firmware de COLDCARD afectado. Si creaste una seed con cualquier dispositivo Coinkite afectado, traslada tus fondos a una seed nueva."
images: ["COLDCARD Security Advisory Notice - Migrate ASAP.png"]
---

## Resumen

[Coinkite ha revelado una debilidad crítica en la generación de seeds del firmware de COLDCARD afectado](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). [El análisis técnico de Block](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware) determinó que la causa es un generador de números aleatorios por software predecible usado en lugar del RNG de hardware del dispositivo, y advierte que **hay una explotación activa en curso**. Actualizar el firmware **no** repara una seed existente.

**Si creaste una seed con cualquier dispositivo Coinkite afectado, traslada tus fondos a una seed nueva.**

## ¿Mi dispositivo está afectado?

La exposición depende de la **versión de firmware instalada cuando se generó la seed**, no de cuándo se fabricó el dispositivo.

| Dispositivo | Firmware usado para generar la seed | Estado |
|---|---|---|
| Mk1 | Todo el firmware publicado | No afectado |
| Mk2 / Mk3 | v3.2.2 o anterior | No afectado (usa RNG de hardware) |
| Mk2 / Mk3 | v4.0.0 – v4.1.9 | **Vulnerable** — sin reseed seguro |
| Mk4 | Producción v5.0.0 en adelante | **Vulnerable** — limitado a ~72 bits de entropía |
| Q | Todo el firmware de producción | **Vulnerable** — limitado a ~72 bits de entropía |
| Mk5 | Todo el firmware de producción | **Vulnerable** — limitado a ~72 bits de entropía |
| TAPSIGNER, OPENDIME, SATSCARD | — | No afectado (código base diferente) |

Ten en cuenta que exportar una seed insegura e importarla en otra billetera **no** la corrige: la seed en sí sigue afectada.

## Instala el firmware corregido antes de generar una seed nueva

Ya hay firmware corregido disponible para cada modelo y línea de lanzamiento afectados. No generes una seed nueva en una COLDCARD hasta haberlo instalado.

| Dispositivo | Firmware corregido |
|---|---|
| Mk2 / Mk3 | 4.2.0 o posterior |
| Mk4 / Mk5 (standard) | 5.6.0 o posterior |
| Q (standard) | 1.5.0Q o posterior |
| Mk4 / Mk5 (Edge) | 6.6.0X o posterior |
| Q (Edge) | 6.6.0QX o posterior |

Standard y Edge son líneas de lanzamiento separadas. Si usas Edge, instala la versión corregida de Edge para tu modelo: no des por hecho que una versión antigua de Edge 6.x está corregida solo porque su número de versión sea mayor que el de la versión standard.

## ¿Me protegen las tiradas de dados o una frase de contraseña?

- **Tiradas de dados:** el fallo solo afecta a la entropía generada por el dispositivo. Si introdujiste al menos **50 tiradas de dados independientes y privadas** al crear la seed (99 o más para aproximadamente 256 bits de entropía), la entrada de dados por sí sola aportó al menos 128 bits de entropía independiente y no se considera que la seed corra riesgo por esta sola cuestión. Con menos de 50 tiradas — o si no estás seguro de cuántas introdujiste o de si fueron privadas — **migra**.
- **Frase de contraseña BIP-39:** una frase de contraseña BIP-39 fuerte y única (no el PIN de COLDCARD) añade una barrera independiente, pero **no** repara la seed afectada. Si tu frase de contraseña es corta, común, reutilizada o adivinable — o no estás seguro de su fortaleza — trata los fondos como en riesgo y migra de inmediato. Incluso con una frase de contraseña fuerte, migra a una seed recién generada tan pronto como sea posible.

## Lista de verificación para la migración

Migra con calma y cuidado. Apresurar una migración de billetera puede crear un riesgo más inmediato que el problema que intentas resolver.

1. **Instala el firmware corregido** de tu modelo antes de generar una seed de reemplazo. Si lo prefieres, genera la seed nueva en un **dispositivo de firma que no sea COLDCARD** ([consulta los dispositivos compatibles]({{< ref "library/supported-hardware-signers" >}})) — en cualquier caso, **no** reutilices la seed antigua.
2. Genera una seed completamente nueva y **regístrala**. Antes de depositar fondos, verifica la copia de seguridad escrita, la huella de la billetera y una dirección de recepción.
3. Usa el asistente de configuración de Bitcoin-Safe para crear una nueva [billetera de firma única]({{< ref "library/setup-singlesig-wallet" >}}) o [billetera multifirma]({{< ref "library/setup-multisig-wallet" >}}) con la seed nueva.
4. Completa la prueba de recepción y envío del asistente: verifica la copia de seguridad y una dirección de recepción en el nuevo firmante, recibe una pequeña cantidad de prueba y envíala con éxito a otra dirección verificada en la billetera nueva.
5. Firma y transmite la transacción de migración:
   - **Billetera de firma única:** transmítela normalmente con una tarifa alta para que se confirme rápido.
   - **Billetera multifirma:** no la transmitas normalmente, porque eso revela sus claves públicas en el mempool público. Copia la transacción cruda firmada y envíala directamente mediante [MARA Slipstream](https://slipstream.mara.com/).
6. Conserva la COLDCARD antigua y su copia de seguridad hasta que el **saldo completo** haya llegado y se haya confirmado en la billetera nueva. Solo entonces borra la seed antigua.

Si la Mk2/Mk3 es tu único dispositivo de firma, instala primero el firmware 4.2.0 o posterior: genera seeds de reemplazo correctamente, así que no necesitas una COLDCARD más nueva para completar la migración. Sigue los mismos pasos, alternando con cuidado entre la seed antigua y la nueva en el único dispositivo, y conserva la copia de seguridad antigua hasta que la migración esté confirmada por completo.

## Si usas multifirma

Si una configuración multifirma está compuesta **exclusivamente** por dispositivos afectados, la vulnerabilidad sigue aplicándose. Protege la configuración con un quórum que incluya al menos un dispositivo de firma que no esté afectado.

## Si ayudas a otra persona a migrar

Nunca le pidas que comparta, fotografíe o escriba sus palabras seed. La seed debe permanecer privada e introducirse únicamente en el propio dispositivo de firma.
