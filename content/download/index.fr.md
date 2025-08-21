---
title: "Télécharger"
description: "Télécharger Bitcoin Safe"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}


✅ **Bitcoin Safe vous informe automatiquement d'une nouvelle version et vérifie l'authenticité.**


Les fichiers binaires Windows sont signés : consultez la [politique de signature du code]({{< ref "code-signing-policy" >}}). Consultez également la [politique de confidentialité de Bitcoin Safe]({{< ref "code-signing-policy" >}}). Les binaires macOS ne sont pas signés, veuillez donc ignorer le message d'avertissement.

<br>
<br>

###  macOS 

Veuillez suivre les étapes pour exécuter Bitcoin Safe sur macOS :
- Copiez-le dans votre dossier Applications
- Essayez de l'ouvrir — vous recevrez un avertissement
- Allez dans les *Réglages Système* --> *Confidentialité & Sécurité* --> *Ouvrir quand même*
- Vous pouvez maintenant l'ouvrir


<img src="/images/mac/copy-app.png" alt="macOS copy-app"   /> 
<img src="/images/mac/warning.png" alt="macOS warning"   /> 
<img src="/images/mac/disable.png" alt="macOS open Bitcoin Safe"   /> 

<br>
<br>

###  Vérifier la signature

Tous les logiciels sont signés avec ma clé privée. Vérifiez que le téléchargement est authentique en suivant ces étapes :

Importez ma [clé publique]({{< gpg_key_link >}}) et vérifiez la signature avec :
{{< gpg_import_code >}}


<br> 
<br>


<!-- ### Alternative install  via pip  on Mac, Linux, or Windows 
PyPi: https://pypi.org/project/bitcoin-safe/
python -m pip install bitcoin-safe
python -m bitcoin_safe
-->