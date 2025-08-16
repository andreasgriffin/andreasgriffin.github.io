---
aliases:
  - "/descargar/"
title: "Descargar"
description: "Descargar Bitcoin Safe"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}

✅ **Bitcoin Safe te notifica de una nueva versión y verifica la autenticidad automáticamente.**

Los archivos binarios de Windows están firmados, revisa la [Política de firma de código]({{< ref "code-signing-policy" >}}). Consulta aquí la [Política de privacidad de Bitcoin Safe]({{< ref "code-signing-policy" >}}).  
Los binarios de MacOS no están firmados, así que por favor ignora el mensaje de advertencia.

<br>
<br>

###  macOS 

Por favor, sigue los pasos para ejecutar Bitcoin Safe en macOS:
- Copia la aplicación en tu carpeta de aplicaciones
- Intenta abrirla, recibirás una advertencia
- Ve a *Configuración del sistema* --> *Privacidad y seguridad* --> *Abrir de todos modos*
- Ahora puedes abrirla

<img src="/images/mac/copy-app.png" alt="macOS copiar-app"   /> 
<img src="/images/mac/warning.png" alt="macOS advertencia"   /> 
<img src="/images/mac/disable.png" alt="macOS abrir Bitcoin Safe"   /> 

<br>
<br>

###  Verificar firma

Todo el software está firmado con mi clave privada. Verifica que la descarga es auténtica siguiendo estos pasos:

Importa mi [clave pública](https://keys.openpgp.org/vks/v1/by-fingerprint/2759AA7148568ECCB03B76301D82124B440F612D) y verifica la firma con:
```bash
gpg --import 2759AA7148568ECCB03B76301D82124B440F612D.asc
gpg --verify Bitcoin-Safe-{{< latest_version >}}-x86_64.AppImage.asc
```

<br> 
<br>
