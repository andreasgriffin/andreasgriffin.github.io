---
title: "Descarrega"
description: "Descarrega Bitcoin Safe"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}

✅ **Bitcoin Safe et notifica quan hi ha una nova versió i en verifica l'autenticitat automàticament.**


Els fitxers binaris per a Windows estan signats; comprova la [política de firma de codi]({{< ref "code-signing-policy" >}}). Consulta aquí la [política de privadesa de Bitcoin Safe]({{< ref "code-signing-policy" >}}). Els binaris per a macOS no estan signats, així que ignora el missatge d'advertència.

<br>
<br>

###  macOS 

Segueix aquests passos per executar Bitcoin Safe a macOS:
- Copia'l a la carpeta d'aplicacions
- Intenta obrir-lo; rebràs un missatge d'advertència
- Ves a *Configuració del sistema* --> *Privacitat i seguretat* --> *Obre igualment*
- Ara el pots obrir


<img src="/images/mac/copy-app.png" alt="Copia l'aplicació (macOS)"   /> 
<img src="/images/mac/warning.png" alt="Avís macOS"   /> 
<img src="/images/mac/disable.png" alt="Obre Bitcoin Safe a macOS"   /> 



<br>
<br>

### Debian/Ubuntu (repositori APT)

{{< apt_repo_install >}}

<br>
<br>

###  Verificar la signatura

Tot el programari està signat amb la meva clau privada. Verifica que la descàrrega és autèntica seguint aquests passos:

Importa la meva [clau pública]({{< gpg_key_link >}}) i verifica la signatura amb:
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