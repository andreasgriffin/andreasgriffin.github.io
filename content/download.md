---
title: "Download"
description: "Download Bitcoin Safe"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}


✅ **Bitcoin Safe notifies you of a newer version and verifies the authenticity automatically.**


Windows binary files are signed, check the [Code signing policy]({{< ref "code-signing-policy" >}}). See here the   [Bitcoin Safe privacy policy]({{< ref "code-signing-policy" >}}).  The  MacOS binaries are not signed, so please disregard the warning message.

<br>
<br>

###  Verify signature

All software is signed with my private key. Verify the download is authentic by following these steps:

Import my [public key](https://keys.openpgp.org/vks/v1/by-fingerprint/2759AA7148568ECCB03B76301D82124B440F612D) and verify the signature with:
```bash
gpg --import 2759AA7148568ECCB03B76301D82124B440F612D.asc
gpg --verify Bitcoin-Safe-{{< latest_version >}}-x86_64.AppImage.asc
```


<br> 
<br>


<!-- ### Alternative install  via pip  on Mac, Linux, or Windows 
PyPi: https://pypi.org/project/bitcoin-safe/
```bash
python -m pip install bitcoin-safe
python -m bitcoin_safe
``` -->
