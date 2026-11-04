---
title: "Seed COLDCARD Tidak Aman"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "Panduan singkat untuk memindahkan dana dari seed yang dibuat pada perangkat Coinkite."
---

[Coinkite telah mengungkap kelemahan dalam pembuatan seed pada firmware COLDCARD yang terdampak](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). Baca juga [analisis teknis Block tentang fallback RNG yang dapat diprediksi dan reseed 32-bit](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware). Memperbarui firmware tidak memperbaiki seed yang sudah ada.

**Jika Anda membuat seed dengan produk Coinkite apa pun, segera lakukan migrasi!**

## Daftar periksa migrasi

1. Buat seed yang benar-benar baru pada **perangkat penandatangan non-COLDCARD** ([lihat perangkat yang didukung]({{< ref "library/supported-hardware-signers" >}})). Jangan gunakan kembali seed lama. Setelah itu, gunakan penandatangan tersebut dengan panduan pengaturan Bitcoin-Safe untuk membuat [dompet tanda tangan tunggal]({{< ref "library/setup-singlesig-wallet" >}}) atau [dompet multisig]({{< ref "library/setup-multisig-wallet" >}}) yang baru.
   - Jika tidak tersedia penandatangan perangkat keras selain COLDCARD, [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}}) dapat digunakan pada perangkat Android khusus yang sudah direset ke setelan pabrik, selalu offline, dan hanya digunakan untuk menandatangani.
   - Selesaikan pengujian menerima dan mengirim dalam panduan untuk memastikan dompet baru telah disiapkan dengan benar: verifikasi cadangan dan alamat penerimaan pada penandatangan baru, terima sejumlah kecil dana pengujian, lalu lakukan pengiriman mandiri ke alamat lain yang telah diverifikasi dalam dompet baru.
2. Tandatangani transaksi migrasi:
   - **Jika dompet yang terdampak adalah dompet tanda tangan tunggal:** siarkan dengan cara biasa menggunakan biaya tinggi agar cepat dikonfirmasi.
   - **Jika dompet yang terdampak adalah dompet multisig:** jangan siarkan dengan cara biasa karena tindakan tersebut mengungkap kunci publiknya di mempool publik. Salin transaksi mentah yang sudah ditandatangani dan kirim langsung melalui [MARA Slipstream](https://slipstream.mara.com/).
3. Simpan COLDCARD lama sampai seluruh saldo telah tiba dan dikonfirmasi di dompet baru, lalu perbarui ke firmware terbaru.

Jika Anda membantu seseorang melakukan migrasi, jangan pernah meminta mereka membagikan, memotret, atau mengetik kata-kata seed. Seed harus tetap bersifat pribadi dan hanya dimasukkan pada perangkat penandatangan.
