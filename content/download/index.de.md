---
title: "Herunterladen"
description: "Bitcoin Safe herunterladen"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}

✅ **Bitcoin Safe benachrichtigt Sie über neuere Versionen und überprüft automatisch deren Authentizität.**


Windows-Binärdateien sind signiert, prüfen Sie die [Richtlinie zur Code-Signatur]({{< ref "code-signing-policy" >}}). Lesen Sie hier die [Bitcoin Safe Datenschutzerklärung]({{< ref "code-signing-policy" >}}). Die macOS-Binaries sind nicht signiert, daher ignorieren Sie bitte die Warnmeldung.

<br>
<br>

###  macOS 

Bitte führen Sie die folgenden Schritte aus, um Bitcoin Safe unter macOS zu starten:
- Kopieren Sie es in Ihren Anwendungsordner
- Wenn Sie versuchen, es zu öffnen, erhalten Sie eine Warnung
- Gehen Sie zu *Systemeinstellungen* --> *Privatsphäre & Sicherheit* --> *Trotzdem öffnen*
- Jetzt können Sie es öffnen


<img src="/images/mac/copy-app.png" alt="macOS App kopieren"   /> 
<img src="/images/mac/warning.png" alt="macOS Warnung"   /> 
<img src="/images/mac/disable.png" alt="macOS Bitcoin Safe öffnen"   /> 



<br>
<br>

### Debian/Ubuntu (APT-Repository)

{{< apt_repo_install >}}

<br>
<br>

###  Signatur überprüfen

Alle Software ist mit meinem privaten Schlüssel signiert. Überprüfen Sie die Authentizität des Downloads, indem Sie folgende Schritte ausführen:

Importieren Sie meinen [öffentlichen Schlüssel]({{< gpg_key_link >}}) und überprüfen Sie die Signatur mit:

{{< gpg_verify_tabs >}}



<br> 
<br>


<!-- ### Alternative install  via pip  on Mac, Linux, or Windows 
PyPi: https://pypi.org/project/bitcoin-safe/
python -m pip install bitcoin-safe
python -m bitcoin_safe
-->