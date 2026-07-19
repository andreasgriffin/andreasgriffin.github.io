---
aliases:
- /es/knowledge/supported-hardware-signers/metrovault/
title: MetroVault
signer: metrovault
bucket: knowledge
---

MetroVault puede convertir un dispositivo Android antiguo en un dispositivo dedicado de firma de Bitcoin sin conexion para Bitcoin-Safe. No lo instales en tu telefono de uso diario. Restablece el dispositivo primero, mantenlo **SIN CONEXION** y desconectado de internet, y usalo solo como firmador.

## Que esperar

- Restablece un dispositivo Android antiguo antes de la instalacion y usalo solo como firmador.
- No instales otras apps, no inicies sesion en cuentas, no insertes una tarjeta SIM ni vuelvas a conectar el dispositivo a internet.
- Intercambia datos de cartera, descriptores y PSBT con Bitcoin-Safe mediante codigos QR.
- Registra descriptores multifirma y exporta datos del firmador para Bitcoin-Safe.
- Verifica todos los detalles en la pantalla de MetroVault antes de firmar.

## Restablece el dispositivo Android y usalo solo como firmador sin conexion

La documentacion original de MetroVault ahora tiene una [guia completa de configuracion del dispositivo](https://github.com/gorunjinian/MetroVault/blob/main/docs/DEVICE_SETUP.md). Recomendamos encarecidamente seguirla paso a paso y tratarla como un requisito: usa un telefono dedicado, restablecido de fabrica y **SIN CONEXION** que siga desconectado de internet despues de la configuracion y se use solo para firmar.

1. Restablece de fabrica el telefono antes de la instalacion.
2. Omite la configuracion de la cuenta de Google y manten el dispositivo sin conexion.
3. Deja el modo avion activado permanentemente.
4. Desactiva Wi-Fi, Bluetooth, NFC y los datos moviles.
5. Retira la tarjeta SIM.
6. Desactiva la depuracion USB.
7. No instales otras apps ni uses el telefono para nada excepto firmar.

Para uso en produccion, compila desde el codigo fuente siempre que sea posible. Si no puedes mantener el dispositivo sin conexion y dedicado solo a firmar, no lo uses para fondos de produccion con MetroVault.
