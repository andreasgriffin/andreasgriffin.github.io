---
title: "Seed insegura de COLDCARD"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "Guía mínima para trasladar fondos desde una seed generada en un dispositivo de Coinkite."
---

[Coinkite ha revelado una debilidad en la generación de seeds del firmware de COLDCARD afectado](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). Consulta también [el análisis técnico de Block sobre el fallback predecible del RNG y el reseed de 32 bits](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware). Actualizar el firmware no repara una seed existente.

**Si creaste una seed con cualquier producto de Coinkite, ¡MIGRA PRONTO!**

## Lista de migración

1. Genera una seed completamente nueva en un **dispositivo de firma que no sea COLDCARD** ([ver dispositivos compatibles]({{< ref "library/supported-hardware-signers" >}})). No reutilices la seed antigua. Después, usa ese firmante con el asistente de configuración de Bitcoin-Safe para crear una nueva [wallet de firma única]({{< ref "library/setup-singlesig-wallet" >}}) o [wallet multifirma]({{< ref "library/setup-multisig-wallet" >}}).
   - Si no tienes disponible ningún firmante de hardware que no sea COLDCARD, [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}}) es una opción en un dispositivo Android dedicado, restablecido de fábrica, que permanezca sin conexión y se use solo para firmar.
   - Completa la prueba de recepción y envío del asistente para confirmar que la nueva wallet está bien configurada: verifica su copia de seguridad y una dirección de recepción en el nuevo firmante, recibe una pequeña cantidad de prueba y realiza correctamente un autoenvío a otra dirección verificada de la nueva wallet.
2. Firma la transacción de migración:
   - **Si la wallet afectada es de firma única:** difúndela de la forma habitual con una comisión alta para que se confirme rápidamente.
   - **Si la wallet afectada es multifirma:** no la difundas de la forma habitual, porque hacerlo revela sus claves públicas en la mempool pública. Copia la transacción sin procesar ya firmada y envíala directamente mediante [MARA Slipstream](https://slipstream.mara.com/).
3. Conserva el COLDCARD antiguo hasta que el saldo completo haya llegado y se haya confirmado en la nueva wallet; después, actualízalo al firmware más reciente.

Si estás ayudando a alguien a migrar, nunca le pidas que comparta, fotografíe o escriba sus palabras seed. La seed debe permanecer privada e introducirse únicamente en el dispositivo de firma.
