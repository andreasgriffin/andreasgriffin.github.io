---
aliases:
- /id/knowledge/supported-hardware-signers/metrovault/
title: MetroVault
signer: metrovault
bucket: knowledge
---

MetroVault dapat mengubah perangkat Android lama menjadi perangkat penandatangan Bitcoin offline khusus untuk Bitcoin Safe. Jangan memasangnya di ponsel harian Anda. Reset perangkat terlebih dahulu, jaga tetap **OFFLINE** dan terputus dari internet, lalu gunakan hanya untuk menandatangani.

## Yang perlu diharapkan

- Reset perangkat Android lama sebelum instalasi dan gunakan hanya sebagai penanda tangan.
- Jangan instal aplikasi lain, jangan masuk ke akun apa pun, jangan masukkan kartu SIM, dan jangan sambungkan kembali perangkat ke internet.
- Tukarkan data dompet, descriptor, dan PSBT dengan Bitcoin Safe menggunakan kode QR.
- Daftarkan descriptor multisig dan ekspor data penanda tangan untuk Bitcoin Safe.
- Verifikasi semua detail di layar MetroVault sebelum menandatangani.

## Reset perangkat Android dan gunakan hanya sebagai penanda tangan offline

Dokumentasi upstream MetroVault memiliki [pengaturan perangkat yang direkomendasikan](https://github.com/gorunjinian/MetroVault/#recommended-device-setup). Anggap ini sebagai persyaratan: gunakan ponsel khusus yang sudah di-reset ke setelan pabrik, **OFFLINE**, tetap terputus dari internet setelah penyiapan, dan dipakai hanya untuk menandatangani.

1. Reset ponsel ke setelan pabrik sebelum instalasi.
2. Lewati penyiapan akun Google dan biarkan perangkat tetap offline.
3. Biarkan mode pesawat selalu aktif.
4. Nonaktifkan Wi-Fi, Bluetooth, NFC, dan data seluler.
5. Lepaskan kartu SIM.
6. Nonaktifkan USB debugging.
7. Jangan instal aplikasi lain dan jangan gunakan ponsel untuk hal lain selain menandatangani.

Untuk penggunaan produksi, bangun dari kode sumber jika memungkinkan. Jika Anda tidak dapat menjaga perangkat tetap offline dan khusus untuk menandatangani, jangan gunakan untuk dana produksi MetroVault.
