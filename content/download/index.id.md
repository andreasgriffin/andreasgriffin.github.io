---
title: "Unduh"
description: "Unduh Bitcoin Safe"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}

✅ **Bitcoin Safe memberi tahu Anda tentang versi yang lebih baru dan secara otomatis memverifikasi keasliannya.**


Windows binary files are signed, check the [Kebijakan penandatanganan kode]({{< ref "code-signing-policy" >}}). Lihat juga [Kebijakan privasi Bitcoin Safe]({{< ref "code-signing-policy" >}}). Biner macOS tidak ditandatangani, jadi abaikan pesan peringatan tersebut.

<br>
<br>

###  macOS 

Ikuti langkah-langkah berikut untuk menjalankan Bitcoin Safe di macOS:
- Salin ke folder Aplikasi Anda
- Saat mencoba membukanya, Anda akan menerima peringatan
- Masuk ke *Pengaturan Sistem* --> *Privasi & Keamanan* --> *Buka saja*
- Sekarang Anda dapat membukanya


<img src="/images/mac/copy-app.png" alt="macOS salin aplikasi"   /> 
<img src="/images/mac/warning.png" alt="peringatan macOS"   /> 
<img src="/images/mac/disable.png" alt="membuka Bitcoin Safe di macOS"   /> 



<br>
<br>

### Debian/Ubuntu (repositori APT)

{{< apt_repo_install >}}

<br>
<br>

###  Verifikasi tanda tangan

Semua perangkat lunak ditandatangani dengan kunci privat saya. Verifikasi bahwa unduhan ini otentik dengan mengikuti langkah-langkah berikut:

Impor [kunci publik]({{< gpg_key_link >}}) saya dan verifikasi tanda tangannya dengan:

{{< gpg_verify_tabs >}}



<br> 
<br>


<!-- ### Alternative install  via pip  on Mac, Linux, or Windows 
PyPi: https://pypi.org/project/bitcoin-safe/
python -m pip install bitcoin-safe
python -m bitcoin_safe
-->