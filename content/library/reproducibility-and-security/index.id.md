---
aliases:
  - "/id/features/reproducibility-and-security/"
title: "Keamanan dan reproduktibilitas"
description: "Bitcoin Safe mengikuti standar tinggi untuk keamanan biner: build yang dapat direproduksi, commit yang ditandatangani, rilis yang ditandatangani, dan pemantauan eksternal independen."
draft: false
bucket: features
tags: ["Featured", "Security"]
images: ["logo.png"]
keywords: ["reproducible builds", "verify binaries", "signed commits", "signed releases", "appimage", "flatpak", "windows exe", "binary security"]
weight: 18
---

### {{< page-title >}}
{{< page-description >}}
<br>

![Hasil build yang dapat direproduksi untuk Bitcoin Safe](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 500px;" }

Kami menerapkan beberapa lapisan perlindungan untuk integritas unduhan di situs web, sehingga aplikasi yang Anda unduh benar-benar cocok dengan kode sumber publik:

- **Build yang dapat direproduksi**: Build Linux `deb`, `AppImage`, dan `Flatpak`, serta Windows `portable exe` dan `setup exe`, dapat direproduksi byte demi byte. Jika file yang dibangun ulang cocok persis, itu adalah bukti kuat bahwa biner dibangun dari kode sumber yang sama.
- **Riwayat repositori yang ditandatangani**: [Repositori GitHub Bitcoin Safe](https://github.com/andreasgriffin/bitcoin-safe/commits/main) menerbitkan commit bertanda tangan yang terverifikasi, sehingga peninjau dapat memeriksa siapa yang membuat kode yang masuk ke dalam rilis.
- **Biner yang ditandatangani**: File rilis ditandatangani dengan [kunci publik PGP]({{< gpg_key_link >}}) milik Bitcoin Safe, dan biner Windows juga mengikuti [kebijakan penandatanganan kode]({{< ref "code-signing-policy" >}}).
- **Pemeriksaan reproduktibilitas independen**: [WalletScrutiny](https://walletscrutiny.com/desktop/bitcoin.safe/) melacak Bitcoin Safe secara independen dan menampilkan status verifikasi reproduktibel untuk rilis desktop.
- **Pemantauan tanda tangan berkelanjutan**: [BinaryWatch](https://binarywatch.org/) secara rutin memeriksa file rilis Bitcoin Safe dan apakah tanda tangannya masih valid terhadap [kunci publik PGP]({{< gpg_key_link >}}) milik Bitcoin Safe.
- **Verifikasi pembaruan**: Pembaruan ditampilkan di Bitcoin Safe, dan tanda tangannya diverifikasi secara otomatis.

Jika digabungkan, langkah-langkah ini menempatkan Bitcoin Safe dalam kelompok kecil proyek yang memperlakukan keamanan biner sebagai bagian inti dari keselamatan pengguna, bukan sesuatu yang ditambahkan belakangan.

### Keamanan adalah pertimbangan utama dalam setiap aspek Bitcoin Safe

Di luar integritas biner, Bitcoin Safe dibangun dengan default yang aman, praktik operasional yang baik, dan panduan pengguna yang jelas. Beberapa contoh:

- **Kustodi yang berfokus pada hardware**: Bitcoin Safe membutuhkan [hardware signer]({{< ref "library/supported-hardware-signers" >}}), sehingga seed tetap berada di perangkat khusus dan tidak menjadi rahasia panas di komputer umum.
- **Alur penyiapan yang lebih aman**: Wizard penyiapan membantu pengguna membuat wallet yang benar-benar siap untuk penggunaan nyata, termasuk pengujian [hardware signer]({{< ref "library/supported-hardware-signers" >}}), [lembar cadangan PDF]({{< ref "library/pdf-export/" >}}), dan panduan tentang cara menyimpan perangkat serta cadangan seed dengan aman.
- **Verifikasi alamat penerimaan**: Bitcoin Safe memudahkan [verifikasi alamat penerimaan]({{< ref "library/verify-receive-address/" >}}) pada signer itu sendiri sebelum dibagikan.
- **Deteksi address poisoning**: Aplikasi ini memperingatkan tentang [alamat yang mencurigakan dan mirip]({{< ref "library/address-poisoning/" >}}).
- **Keamanan multisig**: Bitcoin Safe mendukung wallet multisig, sehingga dana yang lebih besar dapat dilindungi oleh beberapa perangkat atau orang, bukan satu titik kegagalan.
- **Kolaborasi yang membuat multisig lebih mudah**: Bitcoin Safe membuat [kolaborasi multisig]({{< ref "library/collaboration/" >}}) menjadi praktis, sehingga koordinasi penyiapan dan penandatanganan jauh lebih mudah dalam penggunaan nyata.
- **Alur penandatanganan yang jelas**: Layar penandatanganan khusus perangkat mengurangi kebingungan saat meninjau PSBT dan membantu pengguna mengambil tindakan yang tepat pada signer yang tepat.
