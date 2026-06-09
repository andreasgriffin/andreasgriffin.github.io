---
title: "Seguridad y reproducibilidad"
description: "Bitcoin Safe sigue estándares altos de seguridad binaria: compilaciones reproducibles, commits firmados, versiones firmadas y supervisión externa independiente."
draft: false
tags: ["Featured", "Features", "Security"]
images: ["logo.png"]
keywords: ["reproducible builds", "verify binaries", "signed commits", "signed releases", "appimage", "flatpak", "windows exe", "binary security"]
weight: 18
---

### {{< page-title >}}
{{< page-description >}}
<br>

![Resultados de compilación reproducible para Bitcoin Safe](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 500px;" }

Hemos implementado varias capas de protección para la integridad de las descargas en el sitio web, de modo que la aplicación que descargas realmente coincida con el código fuente público:

- **Compilaciones reproducibles**: Las compilaciones de Linux `deb`, `AppImage` y `Flatpak`, además de `portable exe` y `setup exe` para Windows, pueden reproducirse byte por byte. Si un archivo reconstruido coincide exactamente, eso es una señal fuerte de que el binario se generó a partir del mismo código fuente.
- **Historial del repositorio firmado**: El [repositorio de Bitcoin Safe en GitHub](https://github.com/andreasgriffin/bitcoin-safe/commits/main) publica commits firmados y verificados, para que los revisores puedan comprobar quién creó el código que entró en una versión.
- **Binarios firmados**: Los archivos de cada versión se firman con la [clave pública PGP]({{< gpg_key_link >}}) de Bitcoin Safe, y los binarios de Windows también siguen la [política de firma de código]({{< ref "code-signing-policy" >}}).
- **Comprobaciones independientes de reproducibilidad**: [WalletScrutiny](https://walletscrutiny.com/desktop/bitcoin.safe/) sigue Bitcoin Safe de forma independiente y muestra el estado de verificación reproducible de las versiones de escritorio.
- **Supervisión continua de firmas**: [BinaryWatch](https://binarywatch.org/) comprueba regularmente los archivos de versión de Bitcoin Safe y si sus firmas siguen validando contra la [clave pública PGP]({{< gpg_key_link >}}) de Bitcoin Safe.
- **Verificación de actualizaciones**: Las actualizaciones se muestran en Bitcoin Safe y su firma se verifica automáticamente.

En conjunto, estas medidas sitúan a Bitcoin Safe en un grupo pequeño de proyectos que tratan la seguridad binaria como una parte esencial de la seguridad del usuario, y no como algo secundario.

### La seguridad es la consideración principal en cada aspecto de Bitcoin Safe

Más allá de la integridad binaria, Bitcoin Safe está diseñado con valores seguros por defecto, buenas prácticas operativas y una guía clara para el usuario. Algunos ejemplos:

- **Custodia centrada en hardware**: Bitcoin Safe requiere [firmantes de hardware]({{< ref "knowledge/supported-hardware-signers" >}}), para que las semillas permanezcan en dispositivos dedicados en lugar de convertirse en secretos expuestos en un ordenador de uso general.
- **Flujo de configuración más seguro**: El asistente de configuración ayuda a crear wallets realmente listas para el uso real, incluyendo pruebas de [firmantes de hardware]({{< ref "knowledge/supported-hardware-signers" >}}), [hojas PDF de respaldo]({{< ref "features/pdf-export/" >}}) y orientación sobre cómo guardar los firmantes de hardware y las copias de seguridad de las semillas.
- **Verificación de direcciones de recepción**: Bitcoin Safe facilita [verificar las direcciones de recepción]({{< ref "knowledge/verify-receive-address/" >}}) en el propio firmante antes de compartirlas.
- **Detección de envenenamiento de direcciones**: Advierte sobre [direcciones sospechosas y parecidas]({{< ref "features/address-poisoning/" >}}).
- **Seguridad multisig**: Bitcoin Safe admite wallets multifirma, de modo que fondos más grandes puedan protegerse con varios dispositivos o personas en lugar de depender de un único punto de fallo.
- **Colaboración que hace más fácil el multisig**: Bitcoin Safe hace práctica la [colaboración multifirma]({{< ref "features/collaboration/" >}}), por lo que coordinar la configuración y la firma resulta mucho más sencillo en el uso real.
- **Flujos de firma claros**: Las pantallas de firma específicas para cada dispositivo reducen la confusión durante la revisión de PSBT y ayudan a que el usuario realice la acción correcta en el firmante correcto.
