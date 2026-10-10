---
title: "Seed COLDCARD Tidak Aman"
date: "2026-08-02"
draft: false
description: "Coinkite telah mengungkap kelemahan kritis dalam pembuatan seed pada firmware COLDCARD yang terdampak. Jika Anda membuat seed di perangkat Coinkite yang terdampak, pindahkan dana Anda ke seed baru."
images: ["COLDCARD Security Advisory Notice - Migrate ASAP.png"]
---

## Ringkasan

[Coinkite telah mengungkap kelemahan kritis dalam pembuatan seed pada firmware COLDCARD yang terdampak](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). [Analisis teknis Block](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware) mengidentifikasi penyebabnya sebagai generator angka acak perangkat lunak yang dapat diprediksi, yang digunakan sebagai pengganti RNG perangkat keras perangkat, dan memperingatkan bahwa **eksploitasi aktif sedang berlangsung**. Memperbarui firmware **tidak** memperbaiki seed yang sudah ada.

**Jika Anda membuat seed di perangkat Coinkite yang terdampak, pindahkan dana Anda ke seed baru.**

## Apakah perangkat saya terdampak?

Tingkat risiko bergantung pada **versi firmware yang terpasang saat seed dibuat** — bukan pada kapan perangkat diproduksi.

| Perangkat | Firmware yang digunakan untuk membuat seed | Status |
|---|---|---|
| Mk1 | Semua firmware yang dirilis | Tidak terdampak |
| Mk2 / Mk3 | v3.2.2 atau lebih lama | Tidak terdampak (menggunakan RNG perangkat keras) |
| Mk2 / Mk3 | v4.0.0 – v4.1.9 | **Rentan** — tanpa reseed yang aman |
| Mk4 | Produksi v5.0.0 dan seterusnya | **Rentan** — terbatas pada sekitar 72 bit entropi |
| Q | Semua firmware produksi | **Rentan** — terbatas pada sekitar 72 bit entropi |
| Mk5 | Semua firmware produksi | **Rentan** — terbatas pada sekitar 72 bit entropi |
| TAPSIGNER, OPENDIME, SATSCARD | — | Tidak terdampak (kode yang berbeda) |

Perhatikan bahwa mengekspor seed yang tidak aman dan mengimpornya ke dompet lain **tidak** memperbaikinya — seed itu sendiri tetap terdampak.

## Pasang firmware yang diperbaiki sebelum membuat seed baru

Firmware yang diperbaiki kini tersedia untuk setiap model dan jalur rilis yang terdampak. Jangan membuat seed baru di COLDCARD hingga firmware tersebut terpasang.

| Perangkat | Firmware yang diperbaiki |
|---|---|
| Mk2 / Mk3 | 4.2.0 atau lebih baru |
| Mk4 / Mk5 (standard) | 5.6.0 atau lebih baru |
| Q (standard) | 1.5.0Q atau lebih baru |
| Mk4 / Mk5 (Edge) | 6.6.0X atau lebih baru |
| Q (Edge) | 6.6.0QX atau lebih baru |

Standard dan Edge adalah jalur rilis yang terpisah. Jika Anda menggunakan Edge, pasang rilis Edge yang diperbaiki untuk model Anda — jangan berasumsi bahwa rilis Edge 6.x yang lebih lama sudah diperbaiki hanya karena nomor versinya lebih tinggi daripada rilis standard.

## Apakah lemparan dadu atau frasa sandi melindungi saya?

- **Lemparan dadu:** bug ini hanya memengaruhi entropi yang dihasilkan perangkat. Jika Anda memasukkan setidaknya **50 lemparan dadu yang independen dan privat** saat membuat seed (99 atau lebih untuk sekitar 256 bit entropi), masukan dadu saja telah menyumbang setidaknya 128 bit entropi independen, dan seed tersebut tidak dianggap berisiko karena masalah ini saja. Jika lemparannya kurang dari 50 — atau Anda tidak yakin berapa banyak yang dimasukkan atau apakah lemparan tersebut privat — **pindahkan**.
- **Frasa sandi BIP-39:** frasa sandi BIP-39 yang kuat dan unik (bukan PIN COLDCARD) menambah penghalang independen, tetapi **tidak** memperbaiki seed yang terdampak. Jika frasa sandi Anda pendek, umum, dipakai ulang, atau mudah ditebak — atau Anda tidak yakin akan kekuatannya — anggap dana berisiko dan segera pindahkan. Bahkan dengan frasa sandi yang kuat, pindahlah ke seed yang baru dibuat sesegera mungkin.

## Daftar periksa migrasi

Pindahkan dengan tenang dan hati-hati. Terburu-buru dalam migrasi dompet dapat menciptakan risiko yang lebih langsung daripada masalah yang ingin Anda atasi.

1. **Pasang firmware yang diperbaiki** untuk model Anda sebelum membuat seed pengganti. Jika Anda lebih suka, buat seed baru di **perangkat penandatangan yang bukan COLDCARD** ([lihat perangkat yang didukung]({{< ref "library/supported-hardware-signers" >}})) — apa pun pilihannya, **jangan** gunakan ulang seed lama.
2. Buat seed yang benar-benar baru dan **catat**. Sebelum menyetor dana apa pun, verifikasi cadangan tertulis, sidik jari dompet, dan alamat penerima.
3. Gunakan wizard penyiapan Bitcoin-Safe untuk membuat [dompet tanda tangan tunggal]({{< ref "library/setup-singlesig-wallet" >}}) atau [dompet multi-tanda tangan]({{< ref "library/setup-multisig-wallet" >}}) baru dengan seed yang baru.
4. Selesaikan uji terima-dan-kirim wizard: verifikasi cadangan dan alamat penerima di penandatangan baru, terima sejumlah kecil uang uji, dan berhasil kirim ke alamat lain yang telah diverifikasi di dompet baru.
5. Tandatangani dan siarkan transaksi migrasi:
   - **Dompet tanda tangan tunggal:** siarkan secara normal dengan biaya tinggi agar segera terkonfirmasi.
   - **Dompet multi-tanda tangan:** jangan siarkan secara normal, karena hal itu akan memperlihatkan kunci publiknya di mempool publik. Salin transaksi mentah yang sudah ditandatangani dan kirimkan langsung melalui [MARA Slipstream](https://slipstream.mara.com/).
6. Simpan COLDCARD lama dan cadangannya hingga **seluruh saldo** telah tiba dan terkonfirmasi di dompet baru. Baru setelah itu hapus seed lama.

Jika Mk2/Mk3 adalah satu-satunya perangkat penandatangan Anda, pasang dulu firmware 4.2.0 atau lebih baru: firmware tersebut membuat seed pengganti dengan benar, jadi Anda tidak memerlukan COLDCARD yang lebih baru untuk menyelesaikan migrasi. Ikuti langkah yang sama, berganti-ganti dengan hati-hati antara seed lama dan seed baru di perangkat tunggal itu, dan simpan cadangan lama hingga migrasi terkonfirmasi sepenuhnya.

## Jika Anda menggunakan multi-tanda tangan

Jika konfigurasi multi-tanda tangan tersusun **hanya** dari perangkat yang terdampak, kerentanan tetap berlaku. Lindungi konfigurasi dengan kuorum yang mencakup setidaknya satu perangkat penandatangan yang tidak terdampak.

## Membantu orang lain bermigrasi

Jangan pernah meminta mereka membagikan, memotret, atau mengetik kata-kata seed. Seed harus tetap privat dan hanya dimasukkan pada perangkat penandatangan itu sendiri.
