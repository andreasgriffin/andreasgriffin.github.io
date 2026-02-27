---
title: "Transferir"
description: "Transferir Bitcoin Safe"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}

✅ **O Bitcoin Safe notifica-o de uma nova versão e verifica automaticamente a autenticidade.**


Os ficheiros binários do Windows estão assinados, consulte a [Política de assinatura de código]({{< ref "code-signing-policy" >}}). Veja aqui a [política de privacidade do Bitcoin Safe]({{< ref "code-signing-policy" >}}). Os binários para macOS não estão assinados, por isso desconsidere a mensagem de aviso.

<br>
<br>

###  macOS 

Siga os passos para executar o Bitcoin Safe no macOS:
- Copie-o para a pasta de aplicações
- Ao tentar abri-lo, receberá um aviso
- Vá a *Definições do Sistema* --> *Privacidade & Segurança* --> *Abrir Mesmo Assim*
- Agora pode abri-lo


<img src="/images/mac/copy-app.png" alt="macOS copiar aplicação"   /> 
<img src="/images/mac/warning.png" alt="aviso macOS"   /> 
<img src="/images/mac/disable.png" alt="abrir Bitcoin Safe no macOS"   /> 



<br>
<br>

### Debian/Ubuntu (repositório APT)

{{< apt_repo_install >}}

<br>
<br>

###  Verificar assinatura

Todo o software está assinado com a minha chave privada. Verifique que o download é autêntico seguindo estes passos:

Importe a minha [chave pública]({{< gpg_key_link >}}) e verifique a assinatura com:

{{< gpg_verify_tabs >}}



<br> 
<br>


<!-- ### Alternative install  via pip  on Mac, Linux, or Windows 
PyPi: https://pypi.org/project/bitcoin-safe/
python -m pip install bitcoin-safe
python -m bitcoin_safe
-->