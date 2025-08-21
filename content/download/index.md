---
aliases:
  - "/download/"
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

###  macOS 

Please follow the steps to run Bitcoin Safe on macOS:
- Copy it into your app folder
- Try to open it you will get a warning
- Go into the *System Settings* --> *Privacy & Security* --> *Open Anyway*
- Now you can open it


<img src="/images/mac/copy-app.png" alt="macOS copy-app"   /> 
<img src="/images/mac/warning.png" alt="macOS warning"   /> 
<img src="/images/mac/disable.png" alt="macOS open Bitcoin Safe"   /> 

<br>
<br>

###  Verify signature

All software is signed with my private key. Verify the download is authentic by following these steps:

Import my [public key]({{< gpg_key_link >}}) and verify the signature with:
{{< gpg_import_code >}}


<br> 
<br>


<!-- ### Alternative install  via pip  on Mac, Linux, or Windows 
PyPi: https://pypi.org/project/bitcoin-safe/
```bash
python -m pip install bitcoin-safe
python -m bitcoin_safe
``` -->
