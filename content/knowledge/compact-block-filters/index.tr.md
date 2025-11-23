---
title: "Kompakt Blok Filtreleri"
description: "Kompakt blok filtrelerinin ne olduğunu ve Electrum sunucularına kıyasla gizliliği nasıl iyileştirdiğini öğrenin."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "Kompakt blok filtreleri"
  - "CBF"
  - "gizlilik"
  - "Bitcoin cüzdanı"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}


Bitcoin Safe 1.6.0, cüzdanınızı eşitlemenin isteğe bağlı bir yolu olarak **Kompakt Blok Filtreleri (CBF)** sunar. Merkezi bir Electrum sunucusuna cüzdan geçmişinizi sormak yerine, Bitcoin Safe artık her blok için rastgele Bitcoin Core düğümlerinden küçük bir özet dosyası indirebilir. Bu özetler, cüzdanınızın bir bloğun işlemlerinizden birini içerip içermediğine kendi başına karar vermesini sağlayan kısa bir kontrol listesi gibi davranır.

Bitcoin Safe kararı yerel olarak verdiği için, herhangi bir üçüncü taraf sunucu hangi adresleri veya işlemleri önemsediğinizi asla öğrenmez. Tam bir düğümün saklayacağı aynı onay verilerini alırsınız, ancak günlük cihazlara uygun daha hafif bir biçimde.

**Neden daha iyi hissettirir:**

- 📦 **Küçük indirmeler:** Her filtre yalnızca birkaç kilobayt olduğundan, tüm blok zincirini depolamadan normal ev bağlantıları üzerinden eşitleme yapabilirsiniz.
- 🔐 **Doğrudan ağdan:** Bitcoin Safe, diğer düğümlerin yaptığı gibi birden fazla rastgele Bitcoin Core düğümüyle konuşur; bu, tek bir gözlemcinin sizi profilleme olasılığını azaltır.
- 🕵️ **Yerel eşleme:** Cüzdanınız filtreleri yerel olarak kontrol eder. Bir filtre ilgili görünürse, yalnızca o zaman ilgili bloğu indirir; bu da adreslerinizi gizli tutar.

Buna karşılık Electrum sunucuları blok zincirini sizin adınıza arar. Her istek, cüzdanınızdaki adresleri sunucu operatörüyle paylaşır ve operatör bu bilgileri kaydedebilir. Kompakt blok filtreleri ile Bitcoin Safe, her düğümün paylaştığı aynı tarafsız veriyi indirir. Cüzdanınız baştan bu adresleri asla açığa çıkarmadığı için kimse hangi adreslerin size ait olduğunu söyleyemez.

Aşağıda CBF etkinleştirildiğinde Bitcoin Safe'in nasıl bağlandığına dair basit bir görünüm yer alıyor. Bitcoin Core düğümlerinin zaten birbirleriyle konuşma şeklini nasıl yansıttığına dikkat edin:


![Bitcoin Safe downloads compact block filters from several random Bitcoin Core peers.](logo.jpg)
{ .img-fluid .mb-5   style="max-width: 450px;" }


Bitcoin Safe'in kaç eşe bağlanacağını seçebilirsiniz. Daha fazla eş daha fazla bant genişliği gerektirir ve eşitleme süresini uzatabilir. Varsayılan değer 2'dir.

 
### Eşitleme sırasında bekleyebilecekleriniz

CBF, ne yaptığına bağlı olarak bekleme sürenizi değiştirir:

1. ✨ **Cüzdan kurma veya kurtarma:** Yeni bir cüzdan oluşturuyor veya mevcut bir cüzdanı kurtarıyorsanız, ilk eşitleme cüzdanınızın tüm geçmişi için filtreleri çeker. İnternet hızınıza bağlı olarak bu tek seferlik işlemin **5 ila 30 dakika** arasında sürebileceğini bekleyin.
2. 🚀 **Zaten eşitlenmiş bir cüzdanı açmak:** Bitcoin Safe, yalnızca son oturumunuzdan bu yana oluşan en yeni filtreleri alır. Bu yakalama genellikle **30 saniyenin altında** tamamlanır.
3. 🔄 **Electrum sunucularından CBF'ye geçiş:** Cüzdan daha önce Electrum sunucularıyla eşitlenmişse, Bitcoin Safe yalnızca en yeni filtreleri alır; bu genellikle **30 saniyeden az** sürer.

### Onaylanmamış ödemeler hakkında haberdar olun

Kompakt blok filtreleri yalnızca **onaylanmış blokları** kapsar. Onaylanmadan önce gelen işlemler hakkında bilgi almak istiyorsanız, [Anlık işlem bildirimleri]({{< ref "knowledge/instant-transactions-notifications/" >}}) özelliğini de etkinleştirdiğinizden emin olun. Bu özellik, mempool etkinliğine gizliliğinizi riske atmadan tepki verebilmeniz için rastgele bir Bitcoin düğümünden gelen eşler arası canlı mesajları dinler.


<br>
<br>



### Teknik detaylar


- *Daha derine inmek isteyen geliştiriciler için:* kompakt blok filtreleri [BIP158 spesifikasyonunu](https://bips.dev/158/) takip eder ve [Elle Mouton’un Golomb-kodlu kümeler üzerine özeti](https://ellemouton.com/posts/bip158/) bu konuyu açıklar. Bitcoin Safe’in uygulaması açık kaynaklı [BDK için Kyoto kompakt blok filtre modülüne](https://github.com/2140-dev/kyoto) dayanır.
- Kompakt Blok Filtreleri eşitlemesi için kendi Bitcoin Core düğümünüzü eşlere ekleyebilirsiniz; bunun için _Bitcoin ağ izleme_ ayarlarında _Başlangıç düğümü_ seçeneğini belirleyin.


![](inital-node.png)
{ .img-fluid .mb-5   style="max-width: 414px;" }