---
title: "Bitcoin-Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "Yeniden tasarlanan kurulum sihirbazi, Compact Block Filters ile ozel senkronizasyon ve genisletilmis donanim cuzdan destegiyle Bitcoin-Safe 2.0.0 surum notlari."
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">Surum duyurusu</p>
    <h2 class="display-6 mb-3">Bitcoin-Safe 2.0 - yonlendirmeli cuzdan kurulumu, ozel zincir senkronizasyonu ve cihaz odakli imzalama</h2>
    <p class="lead mb-4">Bu surum, yeniden yapilan bir kurulum sihirbazi, Compact Block Filters ile ozel zincir senkronizasyonu ve her donanim cihazi etrafinda duzenlenen bir imzalama akisi getiriyor. Cold storage ilgini cekiyordu ama emin degilsen, denemek icin dogru surum bu.</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Bitcoin-Safe 2.0'yi indir</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">Yeniliklere goz at</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Adim adim cuzdan kurulumu</h2>
          <p class="mb-0">Yeni sihirbaz her adimi acikliyor, belirsizligi azaltyor ve yeni kullanicilarin multisig gucunden vazgecmeden dogru yolu secmesine yardim ediyor.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Ozel cuzdan senkronizasyonu</h2>
          <p class="mb-0">Yeni cuzdanlar artik varsayilan olarak Compact Block Filters ile senkronize oluyor; boylece ucuncu taraf bir Electrum indeksleyicisine dayanmak zorunda kalmadan zinciri ozel olarak tarayabiliyorsun.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Cihaz odakli imzalama</h2>
          <p class="mb-0">Imzalama akislari artik onundeki cihaza odakli kaliyor; QR, USB, Bluetooth, dosyalar ve multisig koordinasyonu icin daha net sonraki adimlar sunuyor.</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## Oz saklamaya yonlendiren rehberli bir yol {#setup-flow}

Ilk kullanim deneyimi bastan sona yeniden kuruldu. Bitcoin-Safe, donanim destekli multisig dahil ciddi oz saklamayi hedeflemeye devam ediyor ve 2.0 artik yeni kullanicilara bu kurulum boyunca yonlendirmeli bir yol sunuyor. Yeni sihirbaz, ne oldugunu, akisin neresinde oldugunu ve ilerlemeden once her signer'in senden neye ihtiyac duydugunu acikliyor.

<p class="small text-muted">Uygulama ayrintilari icin <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a>'ye bak.</p>

Yeniden tasarimin one cikan yonleri:

- Ilk kez kullananlarin dogru baslangic noktasini secmesine yardim eden yeni bir hos geldin ekrani
- Cuzdan olusturma sirasinda adim adim ilerleme akisi
- Odaklanmis talimatlar ve baglamsal yardim iceren cihaza ozel imzalama ekranlari
- Yedeklerin acik ve anlasilir kalmasi icin cihaz adlari ve simgeleri iceren kurtarma PDF'leri

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## Compact Block Filters ile ozel ve saglam zincir senkronizasyonu {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) artik Bitcoin-Safe 2.0'daki yeni cuzdanlarin senkronizasyonunu sagliyor. Electrum sunucusuna hangi adreslerin sana ait oldugunu sormak yerine Bitcoin-Safe, rastgele Bitcoin Core eslerinden kompakt filtreler indirip bunlari yerel olarak kontrol ederek zinciri ozel bicimde tarayabiliyor.

<p class="small text-muted">Uygulama ayrintilari icin <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a>'a bak.</p>


- Cuzdan senkronizasyonu ilk calistirmadan itibaren ozel kalir
- Ucuncu taraf Electrum sunucularina bagimlilik yoktur
- Electrum, tercih eden kullanicilar icin hala kullanilabilir
- [Ilk cuzdan taramasindan sonra aninda senkronizasyon]({{< ref "library/compact-block-filters" >}})
- [Aktarilan islemler icin aninda bildirimler]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## Her cihaz icin cihaz odakli bir imzalama akisi {#device-focused-signing}

Yeniden tasarim, cuzdan olusturulduktan sonraki imzalama akislarini da yeniden sekillendiriyor. Her signer icin tek bir genel ekran yerine Bitcoin-Safe artik eylemleri kullandigin belirli cihaz etrafinda merkezliyor.

<p class="small text-muted">Uygulama ayrintilari icin <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a>'a bak.</p>

- QR, USB, Bluetooth, dosya disa aktarma/ice aktarma ve Sync & Chat eylemleri dogrudan etkin signer kartinda gosterilir
- Kalan signer'lar, zaten imzalamis cihazlar ve gerekli sonraki adim tek bakista gorunur
- Farkli cihazlarin bulundugu multisig akislari, signer kimligi PSBT boyunca gorunur kaldigi icin okunabilirligini korur
- Single-sig ve multisig girdilerinin karisimi olan karmasik islemler dogru sekilde ele alinir; boylece her imzalama adimi net olur

![QR, USB, Bluetooth, dosya disa aktarma ve Chat & Sync icin cihaza ozel eylemler gosteren signer karti](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Is akisleri ve ileri duzey kullanicilar icin eklenti mimarisi

Bitcoin-Safe 2.0, Bitcoin isletmeleri ve ileri duzey Bitcoin kullanicilari icin hedeflenen gelecekteki ek eklentiler icin de temel atiyor. Bu yuzden yakinda neler gelecegini takip etmeye deger :-)

<p class="small text-muted">Uygulama ayrintilari icin <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a>'ye bak.</p>

- Harici bir *sources* deposu uzerinden eklenti dagitimi
- Her eklenti, eklenti guvenligini, butunlugunu ve dagitimini saglamak icin [andreasgriffin]({{< gpg_key_link >}}) tarafindan *GPG ile imzalanir*
- Ayrik eklenti surumleri ve guncellemeler daha hizli ve bagimsiz eklenti gelistirmeyi mumkun kilar

![QR, USB, Bluetooth, dosya disa aktarma ve Chat & Sync icin cihaza ozel eylemler gosteren signer karti](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Daha genis cihaz destegi ve ince ayarlar {#hardware-support}

- Daha hizli tarama icin **30%** daha hizli animasyonlu QR kodlari
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) artik USB ile destekleniyor
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) artik USB ve QR'ye ek olarak **Bluetooth** destegi sunuyor
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) ve [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) desteklenen cihazlar listesine eklendi
- [Desteklenen tum cihazlarin listesini]({{< ref "library/supported-hardware-signers" >}}) gor
- [Tekrar uretilebilirlik]({{< ref "library/reproducibility-and-security" >}}) icin otomatik kontroller eklendi
- Iyilestirmelerin [tam listesine](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0) buradan bak


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## Hala burada olan mevcut gucler

2.0 surumu bir sifirlama degil. Yeni onboarding ve imzalama akislarinin altinda Bitcoin-Safe, onu gunluk kullanimda yararli kilan ozellikleri tasimaya devam ediyor: ortak multisig, PDF yedekleri, aranabilir cuzdan gecmisi, para akisi gorsellestirmeleri, etiket senkronizasyonu ve daha fazlasi.

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">Bitcoin-Safe 2.0'yi denemeye hazir misin?</h2>
  <p class="mb-3">En son surumu indir ve yeni onboarding'i, ozel senkronizasyonu ve donanim cuzdan iyilestirmelerini kendin kesfet.</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Bitcoin-Safe'i indir</a>
</div>


<br><br>

## Tesekkurler

Bu surum, katki saglayanlarin, test edenlerin ve [projenin her yanindaki destekcilerin]({{< ref "donate" >}}) cok emegine dayaniyor:

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r)) sihirbaz yeniden tasarimi, eklenti arayuzu calismalari ve **harika ve bitmek bilmeyen** UI/UX destegi icin
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) yeni cuzdanlar icin ozel senkronizasyonu saglayan Compact Block Filter istemcisi icin
- Bitcoin-Safe'in cekirdegindeki kutuphaneler icin [Bitcoin Dev Kit ekibine](https://github.com/bitcoindevkit/)
- Nostr islevlerini saglayan kutuphaneler icin [ndk ekibine](https://github.com/nostr-dev-kit/ndk)
- Aday surumleri test eden, hata bildiren, sayfalari ceviren, sats gonderen ve projeyi ileri tasimaya devam eden Bitcoin-Safe toplulugundaki herkese
- [Cevirmenler]({{< ref "donate/#translators" >}}) arasinda <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (Vietnamca)" title="qdyg-vn 🇻🇳 (Vietnamca)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (Almanca)" title="bsn21m 🇩🇪 (Almanca)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (Ispanyolca)" title="cyphra 🇪🇸 (Ispanyolca)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (Cince)" title="DaGrindDontStop 🇨🇳 (Cince)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


Bir sonraki surumu finanse etmeye yardim etmek istersen buradan bagis yapabilirsin: {{< donation_btc >}}
