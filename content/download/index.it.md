---
aliases:
  - "/scaricare/"
title: "Scaricare"
description: "Scaricare Bitcoin Safe"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}

✅ **Bitcoin Safe ti notifica di una nuova versione e verifica automaticamente l'autenticità.**

I file binari di Windows sono firmati, controlla la [Politica di firma del codice]({{< ref "code-signing-policy" >}}). Consulta qui l’[Informativa sulla privacy di Bitcoin Safe]({{< ref "code-signing-policy" >}}).  
I binari di MacOS non sono firmati, quindi ignora il messaggio di avviso.

<br>
<br>

###  macOS 

Per favore, segui i passaggi per eseguire Bitcoin Safe su macOS:
- Copialo nella tua cartella Applicazioni
- Prova ad aprirlo, riceverai un avviso
- Vai in *Impostazioni di sistema* --> *Privacy e sicurezza* --> *Apri comunque*
- Ora puoi aprirlo

<img src="/images/mac/copy-app.png" alt="macOS copia-app"   /> 
<img src="/images/mac/warning.png" alt="macOS avviso"   /> 
<img src="/images/mac/disable.png" alt="macOS apri Bitcoin Safe"   /> 

<br>
<br>

###  Verifica firma

Tutto il software è firmato con la mia chiave privata. Verifica che il download sia autentico seguendo questi passaggi:

Importa la mia [chiave pubblica](https://keys.openpgp.org/vks/v1/by-fingerprint/2759AA7148568ECCB03B76301D82124B440F612D) e verifica la firma con:
```bash
gpg --import 2759AA7148568ECCB03B76301D82124B440F612D.asc
gpg --verify Bitcoin-Safe-{{< latest_version >}}-x86_64.AppImage.asc
```

<br> 
<br>
