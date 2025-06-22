---
title: "Descargar"
description: "Bitcoin Safe seguro de descargar"
draft: false
menu:
  footer:
    weight: 10
---


### {{< page-title >}} 

<br>

{{< latest_release >}}

 

✅ **Bitcoin Safe te informa de una nueva versión y verifica automáticamente la autenticidad.**



Los archivos binarios de Windows están firmados, consulta la [Política de firmado de código]({{< ref "code-signing-policy" >}}). Ver aquí la  [Política de privacidad de Bitcoin Safe]({{< ref "code-signing-policy" >}}).


 
### macOS

Al abrir Bitcoin Safe en macOS, puede aparecer la siguiente advertencia. <br>
Puedes abrirlo de todos modos yendo a *Configuración del sistema* --> *Privacidad y seguridad* --> *Abrir de todos modos*<br>

<img src="/images/mac-warning.png" alt="advertencia de macOS" />  
<img src="/images/mac-disable.png" alt="abrir Bitcoin Safe en macOS" />  
 

<br>
<br>

### **Verificar firma**

Todos los programas están firmados con mi clave privada. Verificar que el descarga es auténtica siguiendo estos pasos:

Importar mi [clave pública](https://keys.openpgp.org/vks/v1/by-fingerprint/2759AA7148568ECCB03B76301D82124B440F612D) y verificar la firma con:
```bash
gpg --import 2759AA7148568ECCB03B76301D82124B440F612D.asc
gpg --verificar Bitcoin-Safe-{{< latest_version >}}-x86_64.AppImage.asc
```

 

<br>

<br>
<!-- 
### **Instalación alternativa mediante pip en Mac, Linux o Windows**
PyPi: https://pypi.org/project/bitcoin-safe/
```bash
python -m pip install bitcoin-safe
python -m bitcoin_safe
```
Spero te sea útil. -->


