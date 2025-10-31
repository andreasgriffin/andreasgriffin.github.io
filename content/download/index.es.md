---
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


✅ **Bitcoin Safe le notifica cuando hay una versión más reciente y verifica automáticamente la autenticidad.**


Los binarios de Windows están firmados; consulte la [política de firma de código]({{< ref "code-signing-policy" >}}). Vea aquí la [política de privacidad de Bitcoin Safe]({{< ref "code-signing-policy" >}}). Los binarios de macOS no están firmados, por lo que puede ignorar el mensaje de advertencia.

<br>
<br>

###  macOS 

Por favor, siga los pasos para ejecutar Bitcoin Safe en macOS:
- Copie la aplicación en la carpeta de aplicaciones
- Al intentar abrirla recibirá una advertencia
- Vaya a *Ajustes del Sistema* --> *Privacidad y Seguridad* --> *Abrir de todos modos*
- Ahora podrá abrirla


<img src="/images/mac/copy-app.png" alt="macOS copiar la aplicación"   /> 
<img src="/images/mac/warning.png" alt="macOS advertencia"   /> 
<img src="/images/mac/disable.png" alt="macOS abrir Bitcoin Safe"   /> 

<br>
<br>

###  Verificar la firma

Todo el software está firmado con mi clave privada. Verifique que la descarga es auténtica siguiendo estos pasos:

Importe mi [clave pública]({{< gpg_key_link >}}) y verifique la firma con:
```bash
{{< gpg_import_code >}}
```



<br> 
<br>


<!-- ### Alternative install  via pip  on Mac, Linux, or Windows 
PyPi: https://pypi.org/project/bitcoin-safe/
python -m pip install bitcoin-safe
python -m bitcoin_safe
-->