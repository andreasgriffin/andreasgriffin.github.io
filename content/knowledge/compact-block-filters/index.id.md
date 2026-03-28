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

**Filter Blok Kompak (CBF)** memungkinkan [Bitcoin Safe]({{< ref "/" >}}) memindai blockchain tanpa menanyakan server Electrum alamat mana yang milik Anda.

![Bitcoin Safe mengunduh filter blok kompak dari beberapa peer Bitcoin Core acak.](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

Alih-alih meminta server pusat, Bitcoin Safe mengunduh filter kecil untuk setiap blok dari peer Bitcoin Core acak. Dompet Anda memeriksa filter itu secara lokal dan hanya mengunduh blok penuh saat diperlukan.

### CBF vs Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">Aspek</th>
        <th scope="col">Filter Blok Kompak</th>
        <th scope="col">Server Electrum</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Privasi</th>
        <td><span class="text-success fw-semibold">Baik</span> - Data dompet tetap lokal</td>
        <td><span class="text-danger fw-semibold">Buruk</span> - Server dapat melihat alamat dan riwayat Anda</td>
      </tr>
      <tr>
        <th scope="row">Sumber data</th>
        <td><span class="text-success fw-semibold">Baik</span> - Peer Bitcoin Core acak</td>
        <td><span class="text-warning fw-semibold">Netral</span> - Satu server yang dipilih</td>
      </tr>
      <tr>
        <th scope="row">Sinkronisasi awal</th>
        <td><span class="text-warning fw-semibold">Netral</span> - Biasanya lebih lambat</td>
        <td><span class="text-success fw-semibold">Baik</span> - Biasanya lebih cepat</td>
      </tr>
      <tr>
        <th scope="row">Sinkronisasi berkelanjutan</th>
        <td><span class="text-success fw-semibold">Baik</span> - Sangat cepat setelah sinkronisasi pertama</td>
        <td><span class="text-success fw-semibold">Baik</span> - Biasanya cepat</td>
      </tr>
      <tr>
        <th scope="row">Cocok untuk</th>
        <td><span class="text-success fw-semibold">Baik</span> - Pengguna yang memprioritaskan privasi</td>
        <td><span class="text-success fw-semibold">Baik</span> - Pengaturan dan pemulihan tercepat</td>
      </tr>
    </tbody>
  </table>
</div>

### Mengapa memakai CBF

- Privasi lebih baik: dompet Anda tidak pernah menanyakan alamat Anda ke server.
- Tanpa indexer tepercaya: Bitcoin Safe berbicara langsung dengan jaringan Bitcoin.
- Sinkronisasi ringan: filternya kecil, jadi Anda tidak perlu seluruh blockchain.

### Apa yang diharapkan

- Dompet baru atau pemulihan: biasanya **5 sampai 30 menit** untuk sinkronisasi pertama.
- Dompet yang sudah tersinkron: biasanya mengejar **sangat cepat**, sering kali dalam **kurang dari 30 detik**.
- Pindah dari Electrum ke CBF: biasanya juga **kurang dari 30 detik**.

Anda dapat memilih berapa banyak peer yang dihubungkan Bitcoin Safe. Lebih banyak peer meningkatkan redundansi, tetapi biasanya menambah penggunaan bandwidth dan waktu sinkronisasi. Default-nya adalah **2** peer.

### Transaksi belum dikonfirmasi

CBF hanya mencakup **blok yang dikonfirmasi**. Untuk juga menerima notifikasi pembayaran masuk yang belum dikonfirmasi, biarkan [Notifikasi transaksi instan]({{< ref "knowledge/instant-transactions-notifications/" >}}) tetap aktif, karena itu adalah pengaturan default.

### Catatan teknis

Filter blok kompak didefinisikan dalam [BIP158](https://bips.dev/158/). Bitcoin Safe menggunakan modul sumber terbuka [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto).

Anda juga dapat memakai node Bitcoin Core Anda sendiri sebagai peer awal di pengaturan _Bitcoin network monitoring_.

![Pengaturan node awal](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
