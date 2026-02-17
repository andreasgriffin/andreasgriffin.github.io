---
title: "Scarica"
description: "Scarica Bitcoin Safe"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}


✅ **Bitcoin Safe ti notifica quando è disponibile una versione più recente e ne verifica automaticamente l'autenticità.**


I file binari per Windows sono firmati; controlla la [Politica di firma del codice]({{< ref "code-signing-policy" >}}). Vedi qui anche la [informativa sulla privacy di Bitcoin Safe]({{< ref "code-signing-policy" >}}). I binari per macOS non sono firmati, quindi ignora il messaggio di avviso.

<br>
<br>

###  macOS 

Segui questi passaggi per eseguire Bitcoin Safe su macOS:
- Copia l'app nella cartella Applicazioni
- Prova ad aprirla: riceverai un avviso
- Vai in *Impostazioni di Sistema* --> *Privacy e Sicurezza* --> *Apri comunque*
- Ora puoi aprirla


<img src="/images/mac/copy-app.png" alt="macOS copia dell'app"   /> 
<img src="/images/mac/warning.png" alt="avviso macOS"   /> 
<img src="/images/mac/disable.png" alt="apri Bitcoin Safe su macOS"   /> 

<br>
<br>

###  Verifica della firma

Tutto il software è firmato con la mia chiave privata. Verifica che il download sia autentico seguendo questi passaggi:

Importa la mia [chiave pubblica]({{< gpg_key_link >}}) e verifica la firma con:
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