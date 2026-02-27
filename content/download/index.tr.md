---
title: "İndir"
description: "Bitcoin Safe'i indirin"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}

✅ **Bitcoin Safe sizi daha yeni bir sürüm olduğunda bilgilendirir ve özgünlüğünü otomatik olarak doğrular.**


Windows ikili dosyaları imzalanmıştır, [Code signing policy]({{< ref "code-signing-policy" >}}) belgesine göz atın. Burada ayrıca [Bitcoin Safe gizlilik politikası]({{< ref "code-signing-policy" >}}) bulunmaktadır. macOS ikili dosyaları imzalanmamıştır, bu yüzden lütfen uyarı mesajını görmezden gelin.

<br>
<br>

###  macOS 

Bitcoin Safe'i macOS'ta çalıştırmak için şu adımları izleyin:
- Uygulama klasörünüze kopyalayın
- Açmayı denediğinizde bir uyarı alacaksınız
- *Sistem Ayarları* --> *Gizlilik & Güvenlik* --> *Yine de Aç* kısmına gidin
- Şimdi açabilirsiniz


<img src="/images/mac/copy-app.png" alt="macOS uygulamayı kopyala"   /> 
<img src="/images/mac/warning.png" alt="macOS uyarı"   /> 
<img src="/images/mac/disable.png" alt="macOS Bitcoin Safe'i aç"   /> 



<br>
<br>

### Debian/Ubuntu (APT deposu) ile kurulum

{{< apt_repo_install >}}

<br>
<br>

###  İmzayı doğrulayın

Tüm yazılımlar özel anahtarımla imzalanmıştır. İndirmenin orijinal olduğunu doğrulamak için şu adımları izleyin:

Benim [açık anahtarımı]({{< gpg_key_link >}}) içe aktarın ve imzayı şu komutla doğrulayın:

{{< gpg_verify_tabs >}}



<br> 
<br>


<!-- ### Alternative install  via pip  on Mac, Linux, or Windows 
PyPi: https://pypi.org/project/bitcoin-safe/
python -m pip install bitcoin-safe
python -m bitcoin_safe
-->
