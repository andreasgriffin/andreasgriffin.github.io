---
title: "Notifikasi dompet"
description: "Teruskan notifikasi dompet dan aplikasi Bitcoin-Safe ke tujuan yang Anda atur, dengan kontrol pengiriman, privasi, dan waktu."
draft: false
tags: ["Plugins"]
images: ["notifications.png"]
weight: 35
faq:
  title: "Pertanyaan tentang notifikasi dompet"
  items:
    - question: "Ke mana Bitcoin-Safe dapat mengirim notifikasi?"
      answer: "Bitcoin-Safe dapat mengirim notifikasi ke:\n- Webhook: JSON generik, atau format yang kompatibel dengan Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy, dan Gotify\n- Pesan langsung Nostr\n- Bot Telegram\n- Email melalui SMTP\n- Kalender CalDAV"
    - question: "Bisakah saya menjaga detail sensitif agar tidak ada di peringatan?"
      answer: "Bisa. Aktifkan opsi menyembunyikan detail sensitif, maka pesan hanya berisi pemberitahuan umum bahwa sebuah peristiwa notifikasi Bitcoin-Safe telah terjadi."
    - question: "Apakah saya dapat mengatur peristiwa mana yang dikirim ke mana?"
      answer: "Setiap tujuan memiliki aturannya sendiri. Anda memilih jenis peristiwa yang diterimanya:\n- Transaksi dompet\n- Pembayaran terjadwal\n- Sinkronisasi dan chat\n- Peringatan\n\nAnda juga dapat mengatur penundaan pengiriman acak secara opsional."
    - question: "Apakah aplikasi harus tetap terbuka?"
      answer: "Tidak. Opsi \"Kunci dan Minimalkan ke Tray\" membuat Bitcoin-Safe tetap berjalan di latar belakang saat dompet terkunci."
---

### {{< page-title >}}

<p class="lead">Dapatkan notifikasi tentang aktivitas dompet melalui saluran yang sesuai untuk Anda.</p>

<ul class="plugin-features">
<li>Transaksi masuk dan keluar, pesan Sync&Chat, pembayaran terjadwal yang jatuh tempo, ...</li>
<li>Teruskan peringatan ke webhook, Nostr, Telegram, email, kalender, dan lainnya</li>
<li>Pilih peristiwa yang diterima setiap tujuan dan sembunyikan detail sensitif</li>
<li>Biarkan Bitcoin-Safe berjalan di latar belakang; gunakan <strong>Kunci dan Minimalkan ke Tray</strong> agar tetap berjalan saat dompet terkunci</li>
</ul>

### Pengaturan webhook

{{< video "webhook.mp4" controls >}}

### Pesan langsung Nostr

{{< video "nostr.mp4" controls >}}

### Notifikasi kalender

{{< video "calendar.mp4" controls >}}

### Hubungkan tujuan Anda

- Tambahkan satu atau beberapa tujuan. Setiap tujuan dapat memiliki penerima dan aturan pengiriman sendiri.
- **Email:** Terhubung langsung ke server SMTP dengan host, port, kredensial, pengirim, dan pengaturan keamanan. Ini bukan integrasi Gmail atau Outlook yang dikelola.
- **Telegram:** Kirim ke chat menggunakan bot. Mulai percakapan dengan bot untuk memeriksanya dan mendeteksi ID chat terbaru.
- **Nostr DM:** Kirim pesan NIP-17 terenkripsi ke penerima `npub` melalui relay yang dikonfigurasi dengan kunci pengirim.
- **CalDAV:** Tambahkan acara ke kalender yang sudah ada, seperti kalender Nextcloud yang dikonfigurasi.
- **Webhook:** Kirim dalam format JSON generik atau format untuk endpoint yang kompatibel dengan Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy, dan Gotify. Jenis endpoint umum dapat terdeteksi otomatis.
- Simpan pengaturan tujuan dan gunakan fungsi uji jika tersedia.

### Pilih apa yang dikirim

- Pilih jenis peristiwa yang diterima setiap tujuan:
  - Transaksi dompet
  - Pembayaran terjadwal
  - Sinkronisasi dan chat
  - Peringatan
- Sembunyikan detail sensitif. Pesan kemudian hanya berisi pemberitahuan umum bahwa sebuah peristiwa notifikasi Bitcoin-Safe telah terjadi.
- Atur penundaan pengiriman acak hingga batas maksimum yang Anda pilih.
- Pesan transaksi dompet dapat menyertakan tautan ke penjelajah blok jika tersedia dan detailnya tidak disembunyikan.

### Tinjau pengiriman

- Riwayat terbaru menampilkan setiap peristiwa, tujuan, adapter, waktu, dan hasil: terkirim, sebagian, atau gagal.
- Pengiriman bergantung pada tujuan yang dikonfigurasi dan ketersediaannya. Perhatikan informasi apa yang Anda kirim ke layanan eksternal.

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
<summary>Ke mana Bitcoin-Safe dapat mengirim notifikasi?</summary>

Bitcoin-Safe dapat mengirim notifikasi ke:

- Webhook: JSON generik, atau format yang kompatibel dengan Slack, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy, dan Gotify
- Pesan langsung Nostr
- Bot Telegram
- Email melalui SMTP
- Kalender CalDAV

</details>

<details>
<summary>Bisakah saya menjaga detail sensitif agar tidak ada di peringatan?</summary>

Bisa. Aktifkan opsi menyembunyikan detail sensitif, maka pesan hanya berisi pemberitahuan umum bahwa sebuah peristiwa notifikasi Bitcoin-Safe telah terjadi.

</details>

<details>
<summary>Apakah saya dapat mengatur peristiwa mana yang dikirim ke mana?</summary>

Setiap tujuan memiliki aturannya sendiri. Anda memilih jenis peristiwa yang diterimanya:

- Transaksi dompet
- Pembayaran terjadwal
- Sinkronisasi dan chat
- Peringatan

Anda juga dapat mengatur penundaan pengiriman acak secara opsional.

</details>

<details>
<summary>Apakah aplikasi harus tetap terbuka?</summary>

Tidak. Opsi "Kunci dan Minimalkan ke Tray" membuat Bitcoin-Safe tetap berjalan di latar belakang saat dompet terkunci.

</details>
</content>
