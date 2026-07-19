---
title: "Bitcoin-Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "Catatan rilis untuk Bitcoin-Safe 2.0.0, dengan wizard penyiapan yang dibangun ulang, sinkronisasi privat menggunakan Compact Block Filters, dan dukungan dompet perangkat keras yang lebih luas."
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">Pengumuman rilis</p>
    <h2 class="display-6 mb-3">Bitcoin-Safe 2.0 - penyiapan dompet terpandu, sinkronisasi chain privat, dan penandatanganan yang berfokus pada perangkat</h2>
    <p class="lead mb-4">Rilis ini menghadirkan wizard penyiapan yang dibangun ulang, sinkronisasi chain privat dengan Compact Block Filters, dan alur penandatanganan yang diatur di sekitar setiap perangkat keras. Jika Anda penasaran dengan cold storage tetapi masih ragu, inilah rilis yang patut dicoba.</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Unduh Bitcoin-Safe 2.0</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">Lihat yang baru</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Penyiapan dompet langkah demi langkah</h2>
          <p class="mb-0">Wizard baru menjelaskan setiap langkah, mengurangi kebingungan, dan membantu pengguna baru memilih jalur yang tepat tanpa kehilangan kekuatan multisig.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Sinkronisasi dompet privat</h2>
          <p class="mb-0">Dompet baru sekarang tersinkronisasi dengan Compact Block Filters secara bawaan, sehingga Anda bisa memindai chain secara privat tanpa bergantung pada pengindeks Electrum pihak ketiga.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Penandatanganan berfokus pada perangkat</h2>
          <p class="mb-0">Alur penandatanganan sekarang tetap berpusat pada perangkat di depan Anda, dengan langkah berikutnya yang lebih jelas untuk QR, USB, Bluetooth, file, dan koordinasi multisig.</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## Jalur terpandu menuju self-custody {#setup-flow}

Pengalaman penggunaan pertama telah dibangun ulang dari nol. Bitcoin-Safe tetap ditujukan untuk self-custody yang serius, termasuk multisig berbasis perangkat keras, dan versi 2.0 kini memberi pengguna baru jalur terpandu melalui penyiapan tersebut. Wizard baru menjelaskan apa yang sedang terjadi, Anda sedang berada di bagian mana dari alur, dan apa yang dibutuhkan setiap signer sebelum Anda melanjutkan.

<p class="small text-muted">Untuk detail implementasi, lihat <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a>.</p>

Sorotan desain ulang:

- Layar sambutan baru yang membantu pengguna pertama kali memilih titik awal yang tepat
- Alur progres langkah demi langkah selama pembuatan dompet
- Layar penandatanganan spesifik perangkat dengan instruksi yang fokus dan bantuan kontekstual
- PDF pemulihan dengan nama dan ikon perangkat agar cadangan tetap jelas dan tidak ambigu

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## Sinkronisasi chain yang privat dan tangguh dengan Compact Block Filters {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) kini menjadi mesin sinkronisasi dompet baru di Bitcoin-Safe 2.0. Alih-alih bertanya ke server Electrum alamat mana yang milik Anda, Bitcoin-Safe sekarang dapat memindai chain secara privat dengan mengunduh filter ringkas dari peer Bitcoin Core acak dan memeriksanya secara lokal.

<p class="small text-muted">Untuk detail implementasi, lihat <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a>.</p>


- Sinkronisasi dompet tetap privat sejak pertama kali dijalankan
- Tidak bergantung pada server Electrum pihak ketiga
- Electrum tetap tersedia bagi pengguna yang lebih menyukainya
- [Sinkronisasi instan setelah pemindaian dompet awal]({{< ref "library/compact-block-filters" >}})
- [Notifikasi instan untuk transaksi yang direlay]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## Alur penandatanganan yang berfokus pada perangkat untuk setiap perangkat {#device-focused-signing}

Desain ulang ini juga membentuk ulang alur penandatanganan setelah pembuatan dompet. Alih-alih satu layar generik untuk semua signer, Bitcoin-Safe sekarang memusatkan tindakan di sekitar perangkat spesifik yang sedang Anda gunakan.

<p class="small text-muted">Untuk detail implementasi, lihat <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a>.</p>

- Tindakan QR, USB, Bluetooth, ekspor/impor file, dan Sync & Chat ditampilkan langsung pada kartu signer yang aktif
- Signer yang tersisa, perangkat yang sudah menandatangani, dan tindakan berikutnya yang dibutuhkan tetap terlihat sekilas
- Alur multisig dengan campuran perangkat tetap mudah dibaca karena identitas signer tetap terlihat di seluruh PSBT
- Transaksi rumit dengan campuran input single-sig dan multisig ditangani dengan benar, sehingga setiap langkah penandatanganan tetap jelas

![Kartu signer dengan tindakan spesifik perangkat untuk QR, USB, Bluetooth, ekspor file, dan Chat & Sync](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Arsitektur plugin untuk alur kerja bisnis dan power user

Bitcoin-Safe 2.0 juga meletakkan dasar bagi plugin tambahan di masa depan yang ditujukan untuk bisnis Bitcoin dan power user. Jadi pantau terus apa yang akan datang :-)

<p class="small text-muted">Untuk detail implementasi, lihat <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a>.</p>

- Distribusi plugin melalui repositori *sources* eksternal
- Setiap plugin *ditandatangani dengan GPG* oleh [andreasgriffin]({{< gpg_key_link >}}) untuk memastikan keamanan, integritas, dan distribusinya
- Versi plugin yang terpisah dan pembaruan memungkinkan pengembangan plugin yang lebih cepat dan mandiri

![Kartu signer dengan tindakan spesifik perangkat untuk QR, USB, Bluetooth, ekspor file, dan Chat & Sync](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Dukungan perangkat yang lebih luas dan penyempurnaan {#hardware-support}

- Kode QR animasi **30%** lebih cepat untuk pemindaian yang lebih cepat
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) kini didukung melalui USB
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) kini mendukung **Bluetooth**, selain USB dan QR
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) dan [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) ditambahkan sebagai perangkat yang didukung
- Lihat [daftar lengkap perangkat yang didukung]({{< ref "library/supported-hardware-signers" >}})
- Pemeriksaan otomatis untuk [reproducibility]({{< ref "library/reproducibility-and-security" >}}) telah ditambahkan
- Lihat di sini [daftar lengkap](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0) peningkatannya


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## Kekuatan lama yang tetap ada

Rilis 2.0 bukan reset. Di balik alur onboarding dan penandatanganan yang baru, Bitcoin-Safe tetap membawa fitur-fitur yang membuatnya berguna sehari-hari: multisig kolaboratif, cadangan PDF, riwayat dompet yang dapat dicari, visualisasi arus dana, sinkronisasi label, dan banyak lagi.

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">Siap mencoba Bitcoin-Safe 2.0?</h2>
  <p class="mb-3">Unduh rilis terbaru dan jelajahi sendiri onboarding baru, sinkronisasi privat, serta peningkatan hardware wallet.</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Unduh Bitcoin-Safe</a>
</div>


<br><br>

## Terima kasih

Rilis ini berdiri di atas banyak kerja dari para kontributor, penguji, dan [pendukung di seluruh proyek]({{< ref "donate" >}}):

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r)) untuk desain ulang wizard, pekerjaan UI plugin, dan dukungan UI/UX yang **luar biasa dan tanpa lelah**
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) untuk klien Compact Block Filters yang kini mendukung sinkronisasi dompet privat untuk dompet baru
- Tim [Bitcoin Dev Kit](https://github.com/bitcoindevkit/) untuk pustaka yang menjadi inti Bitcoin-Safe
- Tim [ndk](https://github.com/nostr-dev-kit/ndk) untuk pustaka yang mendukung fungsionalitas nostr
- Semua orang di komunitas Bitcoin-Safe yang menguji release candidate, melaporkan bug, menerjemahkan halaman, mengirim sats, dan terus mendorong proyek ini maju
- [Penerjemah]({{< ref "donate/#translators" >}}), termasuk <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (Vietnam)" title="qdyg-vn 🇻🇳 (Vietnam)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (Jerman)" title="bsn21m 🇩🇪 (Jerman)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (Spanyol)" title="cyphra 🇪🇸 (Spanyol)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (Tionghoa)" title="DaGrindDontStop 🇨🇳 (Tionghoa)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


Jika Anda ingin membantu mendanai rilis berikutnya, Anda juga dapat berdonasi di sini: {{< donation_btc >}}
