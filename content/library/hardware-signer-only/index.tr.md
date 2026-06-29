---
aliases:
  - "/tr/knowledge/hardware-signer-only/"
title: "Donanım İmzacıları Gereklidir"
description: "Bitcoin Safe, güvenliği en üst düzeye çıkarmak ve yazılım tabanlı anahtar saklama risklerinden kaçınmak için Mainnet'te yalnızca donanım tohumlarını zorunlu kılar. Neden önemli olduğunu burada bulabilirsiniz."
draft: false
bucket: knowledge
tags: ["Featured"]
keywords: [
  "Bitcoin Safe",
  "donanım cüzdanı",
  "yazılım tohumu",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "çoklu imza",
  "PSBT",
  "öz-saklama",
  "Bitcoin güvenliği",
  "adres zehirlenmesi",
  "Bitcoin araçları"
]
images: ["logo.png" ]
# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=dbSmQmt0uDI"
weight: 21
---

 

![Bitcoin Safe logo](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }

## 🚫 Neden Bitcoin Safe Mainnet'te yazılım tohumlarını engelliyor?

🤔 Bu rahatsız edici değil mi?

🔥 Meğerse — bu **büyük bir güvenlik iyileştirmesi**.

Bitcoin Safe **yalnızca Testnet, Signet ve Regtest'te yazılım tohumlarına izin verir** — Mainnet'te asla. İşte nedenleri:

### ✅ Mainnet'te yazılım tohumlarının engellenme nedenleri

- 🧠 **Yazılım tohumları güvensizdir**
  - Bilgisayarlar birçok riske açıktır: pano hırsızları, kötü amaçlı yazılımlar, tarayıcı açıkları.
  - Bir hata, tohumunuzun açığa çıkmasıyla sonuçlanır — bu, oyunun sonudur.
  - Soğuk saklama asla sıcak olarak başlamamalıdır.

</br>

- 🧊 **Soğuk saklama soğuk doğmalıdır**
  - Kullanıcılar genellikle tohumları yazılım cüzdanlarında oluşturup sonra donanıma taşır.
  - Ancak ilk maruziyet zaten gerçekleşmiştir — geri dönüş yoktur.
  - Gerçek soğuk saklama = başlangıçtan itibaren bir donanım imzacısında oluşturulmuş olmasıdır.

</br>

- 🎣 **Phishing (oltalama) yazılım alışkanlıklarıyla beslenir**
  - Tohumları uygulamalara yazmak, kötü UX kalıplarına güvenmeyi öğretir.
  - Yalnızca donanım zorunluluğu daha iyi alışkanlıklar kazandırır ve maruziyeti sınırlar.
  - ✅ Mainnet'te tohum yok = daha az oltalama kurbanı.

</br>

- 🧪 **Geliştiriciler yine esneklik elde ediyor**
  - Yazılım tohumlarına *izin verilir*:
    - Testnet
    - Signet
    - Regtest
  - Geliştiriciler için ideal. Gerçek satoshi'ler için risk yok. 🧡



</br>


- 🔐 **Mainnet için donanım imzacılar gerekli — istisna yok**
  - 🔌 USB, 📷 QR ve 💾 SD kart ile tüm büyük cihazlar
    - [Coldcard]({{< ref "library/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "library/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "library/supported-hardware-signers" >}})
    - [Foundation Passport Core]({{< ref "library/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "library/supported-hardware-signers" >}})
    - [Ledger]({{< ref "library/supported-hardware-signers" >}})
    - [Keystone]({{< ref "library/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "library/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "library/supported-hardware-signers" >}})
  - [Tüm desteklenen imzacılara bak →]({{< ref "library/supported-hardware-signers" >}})


---

## 🛡️ Adres zehirlenmesine karşı koruma

Bitcoin Safe **alım adreslerini renklendirir** ve adres zehirlenmesini belirgin hale getirir:

- 🟢 Yeşil = doğrulanmış alım adresi  
- 🟡 Sarı = değişim (change) adresi  

Birisi panonuzu sahte bir adresle zehirlemeye çalışırsa, bunu anında görürsünüz.

![Adres zehirlenmesi tespiti örneği](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ USB veya QR ile adres doğrulama

Alım adreslerini doğrudan donanım imzacınızda doğrulayın — ekrana güvenmeniz gerekmez.

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ Her donanım imzacısı için talimatlar
 
- {{<text-name-with-logo>}} her donanım imzacısı için adım adım ekran görüntüsü talimatları içerir ve her adımda size rehberlik eder 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-images >}}
    </div>

   
---



## 🤝 İşbirlikçi çoklu imza artık kolay

Bitcoin Safe çoklu imzayı kullanıcı dostu ve ekip hazır hale getirir:

- 🔐 Şifreli Nostr sohbeti  
- 🔁 Tek tıkla PSBT paylaşımı  
- 🔌 USB, 📷 QR ve 💾 SD kart

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ Tüm kullanıcılar için güçlü özellikler

- 🟧 Tek imzalı cüzdan sihirbazı  
- 🟨 2'den 3'e multisig kurulumu  
- 🟩 Her türlü n-of-m yapılandırması  
- 🖨️ Yazdırılabilir PDF yedek sayfaları  
- 🔁 Nostr üzerinden etiket senkronizasyonu  
- 🔍 Tam para akışı diyagramı ve aranabilir işlem geçmişi

![Transaction diagram in Bitcoin Safe](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 Küresel ve kullanıcı dostu

- Çokdilli destek: {{< flags-short >}}
- Şu platformlarda çalışır: Windows, macOS & Linux  
- PSBT / CSV sürükle-bırak  
- İşlemler, UTXO'lar, tutarlar ve daha fazlası için gelişmiş filtreler

---

## 💡 Özet

Bitcoin Safe = Gerçek Bitcoin tasarrufu:

✅ Mainnet'te yalnızca donanım  
✅ Yazılım tohumu maruziyeti yok  
✅ Yeni başlayanlar için dostça çoklu imza  
✅ Geliştiriciler için test ortamları  
✅ Aile ve ekip için hazır özellikler  

🔗 [Bitcoin-Safe.org]({{< ref "/" >}})  
🎥 YouTube kanalı →: https://youtube.com/@BitcoinSafeOrg