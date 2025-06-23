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

Sigue estos pasos para ejecutar **Bitcoin Safe** en macOS:

* Copia la aplicación a tu carpeta de Aplicaciones
* Intenta abrirla; aparecerá una advertencia
* Ve a *Configuración del sistema* --> *Privacidad y seguridad* --> *Abrir de todos modos*
* Ahora podrás abrirla

<img src="/images/mac/copy-app.png" alt="macOS copiar app"   />  
<img src="/images/mac/warning.png" alt="macOS advertencia"   />  
<img src="/images/mac/disable.png" alt="macOS abrir Bitcoin Safe"   />  
 

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


