---
title: "Pembayaran terjadwal"
description: "Rencanakan pembayaran Bitcoin sekali atau berulang, pantau jatuh temponya, dan siapkan transaksi untuk ditinjau di Bitcoin-Safe."
draft: false
tags: ["Plugins"]
images: ["schedule.png"]
weight: 40
faq:
  title: "Pertanyaan tentang pembayaran terjadwal"
  items:
    - question: "Bisakah saya menjadwalkan satu pembayaran, atau hanya pembayaran berulang?"
      answer: "Keduanya. Anda dapat membuat pembayaran sekali, sejumlah pengulangan tetap, atau jadwal yang berkelanjutan."
    - question: "Seberapa sering sebuah jadwal dapat diulang?"
      answer: "Interval pengulangan yang tersedia adalah:\n- Menit, jam, atau hari\n- Minggu, opsional pada hari-hari tertentu dalam seminggu\n- Bulan atau tahun, pada tanggal kalender atau pola hari dalam seminggu"
    - question: "Bisakah saya mengatur jumlah dalam mata uang fiat?"
      answer: "Bisa. Anda dapat mengatur jumlah dalam:\n- Bitcoin\n- Mata uang fiat yang didukung\n\nJumlah fiat dapat menggunakan:\n- Kurs langsung\n- Kurs CoinGecko yang ditetapkan pada pukul 00:00 GMT\n\nPenggantian kurs untuk pembayaran berikutnya juga dapat diatur."
    - question: "Apakah alamat digunakan ulang?"
      answer: "Tidak. Setiap alamat penerima hanya digunakan sekali. Jika alamat penerima habis, Anda dapat menambahkan lebih banyak alamat untuk penerima tersebut."
    - question: "Apakah Bitcoin-Safe mengirim pembayaran secara otomatis?"
      answer: "Tidak. Saat pembayaran jatuh tempo, Schedule menyiapkan transaksinya di Bitcoin-Safe untuk Anda tinjau, dan Anda tetap bertanggung jawab untuk menandatangani serta menyiarkannya."
    - question: "Bisakah saya membayar beberapa penerima sekaligus?"
      answer: "Bisa. Pilih beberapa pembayaran terjadwal lalu klik **Bayar yang dipilih**. Bitcoin-Safe akan menggabungkannya menjadi satu transaksi batch."
    - question: "Bagaimana jika sebuah pembayaran sudah dilakukan secara tunai atau cara lain?"
      answer: "Anda dapat menambahkan pembayaran **di luar rantai**. Ini mencatat pembayaran dalam jadwal tanpa transaksi Bitcoin, sehingga kemajuannya tetap akurat."
---

### {{< page-title >}}

<p class="lead">Rencanakan pembayaran Bitcoin dan biarkan Schedule memantau apa yang jatuh tempo.</p>

<ul class="plugin-features">
<li>Membayar karyawan atau mengatur kewajiban rutin lainnya</li>
<li>Mengatur transfer berulang</li>
<li>Menjadwalkan pembayaran sekali yang tidak boleh terlewat</li>
</ul>

Saat pembayaran jatuh tempo, Schedule menyiapkan transaksinya di Bitcoin-Safe untuk Anda tinjau. Anda tetap bertanggung jawab untuk menandatangani dan menyiarkannya.

{{< video "schedule.mp4" controls >}}

### Rencana pembayaran yang fleksibel

- Pilih pembayaran sekali, sejumlah pengulangan tetap, atau jadwal berkelanjutan.
- Atur tanggal mulai dan interval pengulangan: menit, jam, hari, minggu, bulan, atau tahun. Jadwal mingguan dapat menggunakan hari tertentu dalam seminggu; jadwal bulanan dan tahunan mendukung tanggal kalender dan pola hari dalam seminggu.
- Atur penerima, kategori, dan jumlah dalam Bitcoin atau mata uang fiat yang didukung.
- Untuk jumlah fiat, gunakan kurs langsung atau kurs CoinGecko yang ditetapkan pada pukul 00:00 GMT. Penggantian kurs dapat diatur untuk pembayaran berikutnya.
- Jadwal dengan jumlah pengulangan tetap menampilkan pratinjau jumlah per pembayaran dan total.

### Siapkan pembayaran di dompet Anda

- Lihat tanggal jatuh tempo berikutnya dan kemajuan pembayaran; pembayaran yang jatuh tempo disorot dan dapat memicu pemberitahuan Bitcoin-Safe.
- Siapkan satu pembayaran yang jatuh tempo atau sekumpulan pembayaran di penyusun transaksi, dengan output penerima, label, dan kategori yang sudah terisi.
- Tinjau dan sesuaikan transaksi sebelum menandatangani dan menyiarkannya sendiri.
- Simpan penerima yang dapat digunakan kembali dengan nama dan beberapa alamat. Schedule dapat memilih alamat yang belum digunakan untuk sebuah pembayaran.

### Lacak dan kelola jadwal

- Temukan jadwal berdasarkan status jatuh tempo, jenis jadwal, atau kategori. Daftar menampilkan tanggal, pembayaran yang selesai, frekuensi, penerima, jumlah, kategori, dan total.
- Tinjau pembayaran yang sudah selesai dan jadwal mendatang. Transaksi dompet yang cocok dapat memperbarui kemajuan; Anda juga dapat menambahkan pembayaran secara manual atau memindai ulang transaksi dompet.
- Sunting jadwal sebelum pembayaran pertama tercatat, duplikat atau hapus jadwal, dan impor/ekspor jadwal sebagai cadangan JSON.

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">Unduh Bitcoin-Safe</h2>
<p class="text-muted mb-3">Plugin disertakan dengan Bitcoin-Safe. Unduh aplikasinya untuk mencobanya.</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">Unduh Bitcoin-Safe</a>
<small class="text-muted">Gratis & open source · Windows, macOS, Linux</small>
</div>
</section>

### Pertanyaan yang sering diajukan

<details>
<summary>Bisakah saya menjadwalkan satu pembayaran, atau hanya pembayaran berulang?</summary>

Keduanya. Anda dapat membuat pembayaran sekali, sejumlah pengulangan tetap, atau jadwal yang berkelanjutan.

</details>

<details>
<summary>Seberapa sering sebuah jadwal dapat diulang?</summary>

Interval pengulangan yang tersedia adalah:

- Menit, jam, atau hari
- Minggu, opsional pada hari-hari tertentu dalam seminggu
- Bulan atau tahun, pada tanggal kalender atau pola hari dalam seminggu

</details>

<details>
<summary>Bisakah saya mengatur jumlah dalam mata uang fiat?</summary>

Bisa. Anda dapat mengatur jumlah dalam:

- Bitcoin
- Mata uang fiat yang didukung

Jumlah fiat dapat menggunakan:

- Kurs langsung
- Kurs CoinGecko yang ditetapkan pada pukul 00:00 GMT

Penggantian kurs untuk pembayaran berikutnya juga dapat diatur.

</details>

<details>
<summary>Apakah alamat digunakan ulang?</summary>

Tidak. Setiap alamat penerima hanya digunakan sekali. Jika alamat penerima habis, Anda dapat menambahkan lebih banyak alamat untuk penerima tersebut.

</details>

<details>
<summary>Apakah Bitcoin-Safe mengirim pembayaran secara otomatis?</summary>

Tidak. Saat pembayaran jatuh tempo, Schedule menyiapkan transaksinya di Bitcoin-Safe untuk Anda tinjau, dan Anda tetap bertanggung jawab untuk menandatangani serta menyiarkannya.

</details>

<details>
<summary>Bisakah saya membayar beberapa penerima sekaligus?</summary>

Bisa. Pilih beberapa pembayaran terjadwal lalu klik **Bayar yang dipilih**. Bitcoin-Safe akan menggabungkannya menjadi satu transaksi batch.

</details>

<details>
<summary>Bagaimana jika sebuah pembayaran sudah dilakukan secara tunai atau cara lain?</summary>

Anda dapat menambahkan pembayaran **di luar rantai**. Ini mencatat pembayaran dalam jadwal tanpa transaksi Bitcoin, sehingga kemajuannya tetap akurat.

</details>
</content>
