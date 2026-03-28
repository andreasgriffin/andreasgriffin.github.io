---
title: "Kompakt blok filtreleri"
description: "Kompakt blok filtrelerinin ne olduğunu ve Electrum sunucularına göre gizliliği nasıl artırdığını anlayın."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "kompakt blok filtreleri"
  - "CBF"
  - "gizlilik"
  - "Bitcoin cüzdanı"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**Kompakt blok filtreleri (CBF)**, [Bitcoin Safe]({{< ref "/" >}}) uygulamasının bir Electrum sunucusuna hangi adreslerin size ait olduğunu sormadan blok zincirini taramasını sağlar.

![Bitcoin Safe, birkaç rastgele Bitcoin Core peer'inden kompakt blok filtreleri indirir.](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

Bitcoin Safe, merkezi bir sunucuyu sorgulamak yerine her blok için küçük bir filtreyi rastgele Bitcoin Core peer'lerinden indirir. Cüzdanınız bunları yerel olarak kontrol eder ve yalnızca gerektiğinde tam blokları indirir.

### CBF ve Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">Özellik</th>
        <th scope="col">Kompakt blok filtreleri</th>
        <th scope="col">Electrum sunucusu</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Gizlilik</th>
        <td><span class="text-success fw-semibold">İyi</span> - Cüzdan verileri yerelde kalır</td>
        <td><span class="text-danger fw-semibold">Kötü</span> - Sunucu adreslerinizi ve geçmişinizi görebilir</td>
      </tr>
      <tr>
        <th scope="row">Veri kaynağı</th>
        <td><span class="text-success fw-semibold">İyi</span> - Rastgele Bitcoin Core peer'leri</td>
        <td><span class="text-warning fw-semibold">Nötr</span> - Seçilmiş tek bir sunucu</td>
      </tr>
      <tr>
        <th scope="row">İlk senkronizasyon</th>
        <td><span class="text-warning fw-semibold">Nötr</span> - Genelde daha yavaş</td>
        <td><span class="text-success fw-semibold">İyi</span> - Genelde daha hızlı</td>
      </tr>
      <tr>
        <th scope="row">Sürekli senkronizasyon</th>
        <td><span class="text-success fw-semibold">İyi</span> - İlk senkronizasyondan sonra çok hızlı</td>
        <td><span class="text-success fw-semibold">İyi</span> - Genelde hızlı</td>
      </tr>
      <tr>
        <th scope="row">Kimin için uygun</th>
        <td><span class="text-success fw-semibold">İyi</span> - Gizliliği önemseyen kullanıcılar</td>
        <td><span class="text-success fw-semibold">İyi</span> - En hızlı kurulum ve kurtarma isteyenler</td>
      </tr>
    </tbody>
  </table>
</div>

### Neden CBF kullanılır

- Daha fazla gizlilik: cüzdanınız hiçbir zaman sunucuya adreslerinizi sormaz.
- Güvenilen indeksleyici yok: Bitcoin Safe doğrudan Bitcoin ağıyla konuşur.
- Hafif senkronizasyon: filtreler küçüktür, bu yüzden tüm blok zinciri gerekmez.

### Ne beklemeli

- Yeni cüzdan veya kurtarma: ilk senkronizasyon genelde **5 ila 30 dakika** sürer.
- Zaten senkronize edilmiş cüzdan: genelde **çok hızlı** yetişir, çoğu zaman **30 saniyeden kısa** sürer.
- Electrum'dan CBF'ye geçiş: genelde o da **30 saniyeden kısa** sürer.

Bitcoin Safe'in kaç peer'e bağlanacağını seçebilirsiniz. Peer sayısı arttıkça yedeklilik artar, ancak genelde bant genişliği ve senkronizasyon süresi de artar. Varsayılan **2** peer'dir.

### Onaylanmamış işlemler

CBF yalnızca **onaylı blokları** kapsar. Onaylanmamış gelen ödemeler için de bildirim almak istiyorsanız, [Instant transaction notifications]({{< ref "knowledge/instant-transactions-notifications/" >}}) özelliğini açık bırakın. Bu varsayılan ayardır.

### Teknik not

Kompakt blok filtreleri [BIP158](https://bips.dev/158/) içinde tanımlanmıştır. Bitcoin Safe, açık kaynaklı [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto) kullanır.

Kendi Bitcoin Core düğümünüzü _Bitcoin network monitoring_ ayarlarında başlangıç peer'i olarak da kullanabilirsiniz.

![Başlangıç düğümü ayarı](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
