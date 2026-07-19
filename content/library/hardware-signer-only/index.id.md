---
aliases:
  - "/id/knowledge/hardware-signer-only/"
title: "Diperlukan Penanda Perangkat Keras"
description: "Bitcoin-Safe menerapkan hanya seed perangkat keras di Mainnet untuk memaksimalkan keamanan dan menghindari risiko penyimpanan kunci berbasis perangkat lunak. Inilah alasannya."
draft: false
bucket: knowledge
tags: ["Featured"]
keywords: [
  "Bitcoin-Safe",
  "dompet perangkat keras",
  "seed perangkat lunak",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "multisig",
  "PSBT",
  "penyimpanan mandiri",
  "keamanan Bitcoin",
  "pemalsuan alamat",
  "alat Bitcoin"
]
images: ["logo.png" ]
# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=dbSmQmt0uDI"
weight: 21
---

 

![Bitcoin-Safe logo](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }

## 🚫 Mengapa Bitcoin-Safe memblokir seed perangkat lunak di Mainnet?

🤔 Bukankah itu merepotkan?

🔥 Ternyata — ini adalah **peningkatan keamanan besar**.

Bitcoin-Safe **hanya mengizinkan seed perangkat lunak di Testnet, Signet, dan Regtest** — tidak pernah di Mainnet. Begini alasannya:

### ✅ Alasan mengapa seed perangkat lunak diblokir di Mainnet

- 🧠 **Seed perangkat lunak tidak aman**
  - Komputer penuh dengan risiko: peretas clipboard, malware, celah browser.
  - Satu kesalahan, seed Anda terekspos — itu berarti berakhir.
  - Penyimpanan dingin tidak boleh dimulai dalam keadaan 'hot'.

</br>

- 🧊 **Penyimpanan dingin harus lahir dingin**
  - Pengguna sering menghasilkan seed di dompet perangkat lunak lalu memindahkannya ke perangkat keras.
  - Namun paparan awal sudah terjadi — tidak bisa kembali.
  - Penyimpanan dingin sejati = dibuat di penanda perangkat keras sejak awal.

</br>

- 🎣 **Phishing berkembang karena kebiasaan perangkat lunak**
  - Mengetik seed ke aplikasi melatih Anda mempercayai pola UX yang berbahaya.
  - Hanya perangkat keras memaksa kebiasaan yang lebih baik dan membatasi paparan.
  - ✅ Tanpa seed di Mainnet = lebih sedikit korban phishing.

</br>

- 🧪 **Pengembang masih mendapatkan fleksibilitas**
  - Seed perangkat lunak *diizinkan* di:
    - Testnet
    - Signet
    - Regtest
  - Ideal untuk pengembang. Tidak ada risiko terhadap sats nyata. 🧡



</br>


- 🔐 **Mainnet mengharuskan penanda perangkat keras — tanpa pengecualian**
  - 🔌 USB, 📷 QR, dan 💾 kartu SD dengan semua perangkat utama
    - [Coldcard]({{< ref "library/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "library/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "library/supported-hardware-signers" >}})
    - [Foundation Passport Core]({{< ref "library/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "library/supported-hardware-signers" >}})
    - [Ledger]({{< ref "library/supported-hardware-signers" >}})
    - [Keystone]({{< ref "library/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "library/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "library/supported-hardware-signers" >}})
  - [Lihat semua penanda yang didukung →]({{< ref "library/supported-hardware-signers" >}})


---

## 🛡️ Perlindungan terhadap pemalsuan alamat

Bitcoin-Safe **mewarnai alamat penerimaan** untuk membuat pemalsuan alamat terlihat jelas:

- 🟢 Hijau = alamat penerimaan yang terverifikasi  
- 🟡 Kuning = alamat perubahan  

Jika seseorang mencoba meracuni clipboard Anda dengan alamat palsu, Anda akan melihatnya langsung.

![Contoh deteksi pemalsuan alamat](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ Verifikasi alamat melalui USB atau QR

Verifikasi alamat penerimaan langsung di penanda perangkat keras Anda — tidak perlu mempercayai layar.

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ Instruksi untuk setiap penanda perangkat keras
 
- {{<text-name-with-logo>}} menyertakan screenshot petunjuk untuk setiap penanda perangkat keras untuk membimbing Anda melalui setiap langkah 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-images >}}
    </div>

   
---



## 🤝 Multisig kolaboratif jadi mudah

Bitcoin-Safe membuat multisig ramah pengguna dan siap tim:

- 🔐 Obrolan Nostr terenkripsi  
- 🔁 Berbagi PSBT dengan 1-klik  
- 🔌 USB, 📷 QR, dan 💾 kartu SD

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ Fitur kuat untuk semua pengguna

- 🟧 Wizard dompet singlesig  
- 🟨 Pengaturan multisig 2-dari-3  
- 🟩 Konfigurasi n-dari-m apa pun  
- 🖨️ Lembar cadangan PDF yang dapat dicetak  
- 🔁 Sinkronisasi label melalui Nostr  
- 🔍 Diagram aliran uang lengkap & riwayat transaksi yang dapat dicari

![Diagram transaksi di Bitcoin-Safe](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 Global dan ramah pengguna

- Dukungan multibahasa: {{< flags-short >}}
- Berfungsi di: Windows, macOS & Linux  
- Seret-dan-letakkan PSBT / CSV  
- Filter lanjutan untuk transaksi, UTXO, jumlah, dan lainnya

---

## 💡 Singkatnya

Bitcoin-Safe = Tabungan Bitcoin sejati:

✅ Hanya perangkat keras di Mainnet  
✅ Tidak ada paparan seed perangkat lunak  
✅ Multisig ramah pemula  
✅ Lingkungan pengujian ramah pengembang  
✅ Fitur siap keluarga & tim  

🔗 [Bitcoin-Safe.org]({{< ref "/" >}})  
🎥 Channel YouTube →: https://youtube.com/@BitcoinSafeOrg