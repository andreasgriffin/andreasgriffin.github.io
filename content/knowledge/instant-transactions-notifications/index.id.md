---
title: "Notifikasi transaksi instan"
description: "Bagaimana Bitcoin Safe Menerima Notifikasi Transaksi Instan"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [
  "dompet Bitcoin aman untuk keluarga",
  "bitcoin",
  "tabungan bitcoin",
  "penandatangan perangkat keras",
  "kustodian Bitcoin",
  "penasihat keuangan",
  "dompet bitcoin",
  "trezor",
  "usa bitcoin",
  "BTC",
  "HODL",
  "KeamananBitcoin",
  "Notifikasi transaksi instan"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---



![Bitcoin Safe logo](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }


### {{< page-title >}}  
 
  


**Bitcoin Safe** (mulai dari versi **1.5.0**) mendukung notifikasi instan untuk transaksi Bitcoin masuk yang relevan dengan dompet Anda. Berikut cara kerjanya di balik layar:




##### 1. 📡 Mendengarkan Jaringan P2P Bitcoin

Bitcoin Safe terhubung langsung ke satu atau beberapa **node Bitcoin Core**, yang berpartisipasi dalam jaringan **peer-to-peer (P2P)** global. Node-node ini terus bertukar transaksi yang baru disiarkan yang dimaksudkan untuk dimasukkan ke dalam **mempool**.

Bitcoin Safe mendengarkan secara pasif pesan-pesan siaran ini dan memeriksa apakah:

* ada transaksi yang melibatkan **alamat** atau **UTXO** dari dompet Anda.

✅ **Menjaga Privasi**
Metode ini **sepenuhnya privat**. Ini **tidak mengungkapkan apa pun** tentang dompet Anda ke dunia luar.
Bitcoin Safe berperilaku sama seperti node Bitcoin Core biasa: hanya mendengarkan lalu lintas P2P publik — tidak pernah mengumumkan atau meminta sesuatu yang spesifik untuk dompet Anda.



##### 2. 🧠 Kecocokan Ditemukan — Apa yang Terjadi Selanjutnya?

Jika ditemukan transaksi yang cocok, Bitcoin Safe akan bereaksi berbeda tergantung pada backend yang Anda gunakan:

###### Opsi A: ⚡ Backend Electrum atau Esplora

* Bitcoin Safe akan **memicu sinkronisasi latar belakang** untuk mengambil transaksi lengkap dan status dompet dari server.

###### Opsi B: 🔍 Compact Block Filters (Mode Neutrino)

* Dompet akan **langsung menambahkan transaksi yang belum dikonfirmasi** ke data dompet lokal Anda — tidak perlu pencarian lebih lanjut.



#### ⚙️ Perilaku Opt-In / Opt-Out

Untuk menghormati preferensi pengguna dan pengaturan privasi:

* 🔒 **Untuk pengguna lama** yang meng-upgrade ke versi 1.5.0 atau lebih baru, fitur ini **bersifat opt-in secara default** — Anda dapat mengaktifkannya secara manual di pengaturan jaringan.
* 🚀 **Untuk pengguna baru**, fitur ini **diaktifkan (opt-out)** secara default, karena fitur ini **menjaga privasi** dan **sangat berguna** untuk melacak aktivitas dompet secara real-time.

Anda tetap memiliki kendali penuh dan dapat mengubah pengaturan ini kapan saja.
 
 

![Notification settings screenshot](config.png)
{ .img-fluid .mb-5 }


#### ⚠️  Hanya transaksi yang terkonfirmasi yang dapat dipercaya

Bitcoin Safe tidak dapat memvalidasi bahwa sebuah transaksi yang disiarkan itu valid. Seorang penyerang — terutama yang mengendalikan baik server Electrum Anda maupun node Bitcoin yang terhubung ke Anda — dapat:

* Membuat transaksi palsu yang melibatkan alamat Anda
* Menyiarkannya untuk memicu notifikasi dompet
* Memastikan transaksi itu tidak pernah terkonfirmasi, karena transaksi tersebut **tidak valid** atau **bertentangan dengan aturan konsensus**


  


#### ✅ Ringkasan

Mulai dari versi **1.5.0**, Bitcoin Safe mendukung notifikasi transaksi instan dengan:

* Mendengarkan secara pasif jaringan P2P Bitcoin (seperti Bitcoin Core)
* Mencocokkan transaksi yang melibatkan **alamat** atau **UTXO** dompet Anda
* Mengambil detail lengkap melalui Electrum/Esplora atau menambahkan langsung melalui Compact Block Filters
* Tidak pernah mengungkapkan data dompet apa pun ke dunia luar