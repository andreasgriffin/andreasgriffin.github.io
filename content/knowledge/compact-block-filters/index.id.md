---
title: "Filter Blok Kompak"
description: "Pahami apa itu filter blok kompak dan bagaimana mereka meningkatkan privasi dibandingkan server Electrum."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "filter blok kompak"
  - "CBF"
  - "privasi"
  - "dompet Bitcoin"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}


Bitcoin Safe   1.6.0 memperkenalkan **Filter Blok Kompak (CBF)** sebagai cara opsional untuk menyinkronkan dompet Anda. Daripada meminta server Electrum terpusat untuk riwayat dompet Anda, Bitcoin Safe sekarang dapat mengunduh berkas ringkasan kecil untuk setiap blok langsung dari node Bitcoin Core acak. Ringkasan ini berfungsi seperti daftar periksa singkat yang memungkinkan dompet Anda memutuskan sendiri apakah sebuah blok mungkin berisi salah satu transaksi Anda.

Karena Bitcoin Safe membuat keputusan secara lokal, tidak ada server pihak ketiga yang mengetahui alamat atau transaksi mana yang Anda pedulikan. Anda mendapatkan data konfirmasi yang sama seperti yang disimpan oleh node penuh, namun dalam format yang lebih ringan yang cocok untuk perangkat sehari-hari.

**Mengapa terasa lebih baik:**

- 📦 **Unduhan kecil:** Setiap filter hanya beberapa kilobita, sehingga Anda dapat menyinkronkan melalui koneksi rumah biasa tanpa menyimpan seluruh blockchain.
- 🔐 **Langsung dari jaringan:** Bitcoin Safe berbicara dengan beberapa node Bitcoin Core acak, sama seperti node lain, mengurangi peluang bahwa pengamat tunggal dapat memprofil Anda.
- 🕵️ **Pencocokan lokal:** Dompet Anda memeriksa filter secara lokal. Jika sebuah filter tampak relevan, baru kemudian ia mengunduh blok spesifik tersebut, menjaga alamat Anda tetap privat.

Server Electrum, sebaliknya, mencari di blockchain atas nama Anda. Setiap permintaan membagikan alamat dompet Anda kepada operator server, yang bisa mencatat informasi tersebut. Dengan filter blok kompak, Bitcoin Safe mengunduh data netral yang sama yang dibagikan setiap node. Tidak ada yang bisa mengetahui alamat mana yang milik Anda karena dompet Anda tidak pernah mengungkapkannya sejak awal.

Di bawah ini adalah tampilan sederhana bagaimana Bitcoin Safe terhubung saat CBF diaktifkan. Perhatikan bagaimana ini mencerminkan cara node Bitcoin Core saling berkomunikasi:


![Bitcoin Safe mengunduh filter blok kompak dari beberapa node Bitcoin Core acak.](logo.jpg)
{ .img-fluid .mb-5   style="max-width: 450px;" }


Anda dapat memilih berapa banyak peer yang harus dihubungkan Bitcoin Safe. Semakin banyak peer, semakin besar bandwidth yang dibutuhkan dan semakin lambat waktu sinkronisasi. Defaultnya adalah 2.  

 
### Apa yang diharapkan saat menyinkronkan

CBF mengubah lamanya waktu tunggu tergantung pada apa yang Anda lakukan:

1. ✨ **Menyiapkan atau memulihkan dompet:** Baik Anda membuat dompet baru atau memulihkan yang sudah ada, sinkronisasi awal menarik filter untuk seluruh riwayat dompet Anda. Proses satu kali ini biasanya memakan waktu **antara 5 hingga 30 menit**, tergantung kecepatan internet Anda.
2. 🚀 **Membuka dompet yang sudah pernah disinkronkan:** Bitcoin Safe hanya perlu mengambil filter terbaru sejak sesi terakhir Anda. Pengejaran ini biasanya selesai dalam **kurang dari 30 detik**.
3. 🔄 **Beralih dari server Electrum ke CBF:** Karena dompet sebelumnya sudah disinkronkan dengan server Electrum, Bitcoin Safe hanya perlu mengambil filter terbaru, yang biasanya akan **kurang dari 30 detik**.

### Tetap diberitahu tentang pembayaran yang belum dikonfirmasi

Filter blok kompak hanya mencakup **blok yang sudah dikonfirmasi**. Untuk mendapat pemberitahuan tentang transaksi masuk sebelum dikonfirmasi, pastikan Anda juga mengaktifkan [Instant transaction notifications]({{< ref "knowledge/instant-transactions-notifications/" >}}). Fitur itu mendengarkan pesan peer-to-peer langsung dari node Bitcoin acak sehingga Anda bisa bereaksi terhadap aktivitas mempool tanpa mengorbankan privasi.


<br>
<br>



### Rincian teknis


- *Untuk pengembang yang ingin mendalami:* filter blok kompak mengikuti spesifikasi [BIP158](https://bips.dev/158/) dan dibahas dalam [tinjauan Elle Mouton tentang Golomb-coded sets](https://ellemouton.com/posts/bip158/). Implementasi Bitcoin Safe bergantung pada modul open-source [Kyoto compact block filter untuk BDK](https://github.com/2140-dev/kyoto).
- Anda dapat menambahkan node Bitcoin Core Anda sendiri ke peer untuk sinkronisasi Filter Blok Kompak, dengan memilih _Initial node_ dari _Bitcoin network monitoring_.


![](inital-node.png)
{ .img-fluid .mb-5   style="max-width: 414px;" }