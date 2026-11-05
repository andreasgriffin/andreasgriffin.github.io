---
title: "Sync & Chat"
description: "Temukan rekan di dompet Anda, sinkronkan label dan kategori, chat dengan aman, dan bagikan PSBT dengan satu klik."
draft: false
tags: ["Plugins", "sync-chat-mainpage"]
images: ["logo.png"]
weight: 30
faq:
  title: "Pertanyaan tentang Sync & Chat"
  items:
    - question: "Bagaimana perangkat saling menemukan?"
      answer: "Sync & Chat mencari perangkat lain yang menggunakan deskriptor dompet yang sama. Deskriptor di-hash sebelum digunakan untuk pencarian, sehingga tidak terekspos dalam bentuk teks biasa. Selain itu, setiap perangkat yang ditemukan harus ditambahkan dan ditandai sebagai tepercaya secara manual sebelum dapat ikut serta dalam chat. Dengan cara ini, chat tetap aman meskipun deskriptornya tidak rahasia."
    - question: "Bagaimana kolaborasi berjalan dalam praktik?"
      answer: "1. Pengaturan (sekali): tambahkan perangkat setiap peserta dan tandai sebagai tepercaya.\n2. Buat: salah satu peserta membuat PSBT dan menambahkan tanda tangannya.\n3. Bagikan: PSBT dikirim ke semua peserta, atau hanya ke peserta tertentu.\n4. Tanda tangan: setiap peserta menambahkan tanda tangannya hingga transaksi sepenuhnya ditandatangani.\n5. Siarkan: penandatangan terakhir menyiarkan transaksi, dan transaksi tersebut kemudian muncul di dompet semua peserta."
    - question: "Apa saja yang disinkronkan?"
      answer: "Sync & Chat menangani:\n- Kategori koin dan label, yang disinkronkan antar penandatangan, bahkan di sistem operasi yang berbeda\n- Berbagi PSBT dengan satu klik"
    - question: "Apakah chat bersifat privat?"
      answer: "Ya. Chat dompet terenkripsi dan berjalan melalui Nostr; cadangan label juga disimpan terenkripsi melalui Nostr."
---

### {{< page-title >}}

<p class="lead">Koordinasikan penandatangan multisig dan jaga konteks dompet tetap tersinkronisasi langsung dari Bitcoin-Safe.</p>

<ul class="plugin-features">
<li>Temukan perangkat lain yang menggunakan deskriptor dompet yang sama</li>
<li>Sinkronkan label dan kategori antar penandatangan</li>
<li>Chat dengan aman dan bagikan PSBT dengan satu klik</li>
</ul>

### Sinkronisasi label

{{< video src="../../library/label-sync/label-sync.mp4" controls="true" >}}

### Penandatanganan kolaboratif

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

Untuk panduan lengkap penandatanganan kolaboratif multisig, lihat [Kolaborasi dalam Multisig]({{< ref "library/collaboration/" >}}).

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
<summary>Bagaimana perangkat saling menemukan?</summary>

Sync & Chat mencari perangkat lain yang menggunakan deskriptor dompet yang sama. Deskriptor di-hash sebelum digunakan untuk pencarian, sehingga tidak terekspos dalam bentuk teks biasa. Selain itu, setiap perangkat yang ditemukan harus ditambahkan dan ditandai sebagai tepercaya secara manual sebelum dapat ikut serta dalam chat. Dengan cara ini, chat tetap aman meskipun deskriptornya tidak rahasia.

</details>

<details>
<summary>Bagaimana kolaborasi berjalan dalam praktik?</summary>

1. **Pengaturan (sekali):** tambahkan perangkat setiap peserta dan tandai sebagai tepercaya.
2. **Buat:** salah satu peserta membuat PSBT dan menambahkan tanda tangannya.
3. **Bagikan:** PSBT dikirim ke semua peserta, atau hanya ke peserta tertentu.
4. **Tanda tangan:** setiap peserta menambahkan tanda tangannya hingga transaksi sepenuhnya ditandatangani.
5. **Siarkan:** penandatangan terakhir menyiarkan transaksi, dan transaksi tersebut kemudian muncul di dompet semua peserta.

</details>

<details>
<summary>Apa saja yang disinkronkan?</summary>

Sync & Chat menangani:

- Kategori koin dan label, yang disinkronkan antar penandatangan, bahkan di sistem operasi yang berbeda
- Berbagi PSBT dengan satu klik

</details>

<details>
<summary>Apakah chat bersifat privat?</summary>

Ya. Chat dompet terenkripsi dan berjalan melalui Nostr; cadangan label juga disimpan terenkripsi melalui Nostr.

</details>

{{< sync-page-box >}}
</content>
