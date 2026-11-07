---
title: "Planlanmış ödemeler"
description: "Tek seferlik veya tekrarlayan Bitcoin ödemeleri planlayın, vade tarihlerini takip edin ve işlemleri Bitcoin-Safe'te inceleme için hazırlayın."
draft: false
tags: ["Plugins"]
images: ["schedule.png"]
weight: 40
faq:
  title: "Planlanmış ödemeler hakkında sorular"
  items:
    - question: "Tek bir ödeme mi planlayabilirim, yoksa yalnızca tekrarlayan ödemeler mi?"
      answer: "İkisi de. Tek seferlik bir ödeme, sabit sayıda tekrar veya sürekli bir plan oluşturabilirsiniz."
    - question: "Bir plan ne sıklıkla tekrarlanabilir?"
      answer: "Tekrar aralıkları şunlar olabilir:\n- Dakika, saat veya gün\n- Hafta, isteğe bağlı olarak seçilen haftanın günlerinde\n- Ay veya yıl, takvim tarihlerinde ya da haftanın günü kalıplarında"
    - question: "Tutarı fiat para biriminde belirleyebilir miyim?"
      answer: "Evet. Tutarı şu birimlerde belirleyebilirsiniz:\n- Bitcoin\n- Desteklenen bir fiat para birimi\n\nFiat tutarları şunlardan birini kullanabilir:\n- Anlık bir kur\n- 00:00 GMT'de sabitlenen CoinGecko kuru\n\nBir sonraki ödeme için kur geçersiz kılma da ayarlanabilir."
    - question: "Adresler yeniden kullanılıyor mu?"
      answer: "Hayır. Her alıcı adresi yalnızca bir kez kullanılır. Bir alıcının adresleri tükendiğinde, o alıcı için yeni adresler ekleyebilirsiniz."
    - question: "Bitcoin-Safe ödemeleri otomatik olarak gönderiyor mu?"
      answer: "Hayır. Bir ödeme vadesi geldiğinde Schedule, işlemi incelemeniz için Bitcoin-Safe'te hazırlar; imzalama ve yayınlamadan siz sorumlu olmaya devam edersiniz."
    - question: "Birden fazla alıcıya aynı anda ödeme yapabilir miyim?"
      answer: "Evet. Birkaç planlanmış ödeme seçin ve **Seçilenleri öde** düğmesine tıklayın. Bitcoin-Safe bunları tek bir toplu işlemde birleştirir."
    - question: "Bir ödeme nakit veya başka bir yolla yapıldıysa ne olur?"
      answer: "**Bant dışı** bir ödeme ekleyebilirsiniz. Bu, Bitcoin işlemi olmadan ödemeyi planınıza kaydeder ve ilerlemenin doğru kalmasını sağlar."
---

### {{< page-title >}}

<p class="lead">Bitcoin ödemelerinizi planlayın; Schedule neyin vadesinin geldiğini takip etsin.</p>

<ul class="plugin-features">
<li>Çalışanlara ödeme yapın veya diğer düzenli yükümlülükleri yönetin</li>
<li>Tekrarlayan transferler kurun</li>
<li>Unutmak istemediğiniz tek seferlik bir ödemeyi planlayın</li>
</ul>

Bir ödemenin vadesi geldiğinde Schedule, işlemi incelemeniz için Bitcoin-Safe'te hazırlar. İmzalama ve yayınlamadan siz sorumlu olmaya devam edersiniz.

{{< video "schedule.mp4" controls >}}

### Esnek ödeme planları

- Tek seferlik bir ödeme, sabit sayıda tekrar veya sürekli bir plan seçin.
- Bir başlangıç tarihi ve tekrar aralığı belirleyin: dakika, saat, gün, hafta, ay veya yıl. Haftalık planlar seçilen haftanın günlerini kullanabilir; aylık ve yıllık planlar takvim tarihlerini ve haftanın günü kalıplarını destekler.
- Bitcoin veya desteklenen bir fiat para biriminde alıcı, kategori ve tutar belirleyin.
- Fiat tutarları için anlık kuru ya da 00:00 GMT'de sabitlenen CoinGecko kurunu kullanın. Bir sonraki ödeme için kur geçersiz kılma ayarlanabilir.
- Sabit sayıda ödemeli planlar, ödeme başına ve toplam tutar önizlemelerini gösterir.

### Cüzdanınızda ödemeleri hazırlayın

- Bir sonraki vade tarihini ve ödeme ilerlemesini görün; vadesi gelen ödemeler vurgulanır ve bir Bitcoin-Safe bildirimini tetikleyebilir.
- İşlem oluşturucuda tek bir vadesi gelen ödemeyi veya bir toplu ödemeyi, alıcı çıktıları, etiketler ve kategorilerle birlikte hazırlayın.
- İşlemi imzalamadan ve yayınlamadan önce gözden geçirin ve özelleştirin.
- Ad ve birden fazla adresle yeniden kullanılabilir alıcılar kaydedin. Schedule, bir ödeme için kullanılmamış bir adres seçebilir.

### Planları takip edin ve yönetin

- Planları vade durumuna, plan türüne veya kategoriye göre bulun. Listeler tarihleri, tamamlanan ödemeleri, sıklığı, alıcıyı, tutarı, kategoriyi ve toplamı gösterir.
- Tamamlanan ödemeleri ve yaklaşan tarihleri inceleyin. Eşleşen cüzdan işlemleri ilerlemeyi güncelleyebilir; ayrıca bir ödemeyi elle ekleyebilir veya cüzdan işlemlerini yeniden tarayabilirsiniz.
- İlk kaydedilen ödemeden önce bir planı düzenleyin, çoğaltın veya silin; planları JSON yedeği olarak içe ve dışa aktarın.

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">Bitcoin-Safe'i indirin</h2>
<p class="text-muted mb-3">Eklentiler Bitcoin-Safe ile birlikte gelir. Denemek için uygulamayı indirin.</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">Bitcoin-Safe'i indirin</a>
<small class="text-muted">Özgür ve açık kaynaklı yazılım · Windows, macOS, Linux</small>
</div>
</section>

### Sıkça sorulan sorular

<details>
<summary>Tek bir ödeme mi planlayabilirim, yoksa yalnızca tekrarlayan ödemeler mi?</summary>

İkisi de. Tek seferlik bir ödeme, sabit sayıda tekrar veya sürekli bir plan oluşturabilirsiniz.

</details>

<details>
<summary>Bir plan ne sıklıkla tekrarlanabilir?</summary>

Tekrar aralıkları şunlar olabilir:

- Dakika, saat veya gün
- Hafta, isteğe bağlı olarak seçilen haftanın günlerinde
- Ay veya yıl, takvim tarihlerinde ya da haftanın günü kalıplarında

</details>

<details>
<summary>Tutarı fiat para biriminde belirleyebilir miyim?</summary>

Evet. Tutarı şu birimlerde belirleyebilirsiniz:

- Bitcoin
- Desteklenen bir fiat para birimi

Fiat tutarları şunlardan birini kullanabilir:

- Anlık bir kur
- 00:00 GMT'de sabitlenen CoinGecko kuru

Bir sonraki ödeme için kur geçersiz kılma da ayarlanabilir.

</details>

<details>
<summary>Adresler yeniden kullanılıyor mu?</summary>

Hayır. Her alıcı adresi yalnızca bir kez kullanılır. Bir alıcının adresleri tükendiğinde, o alıcı için yeni adresler ekleyebilirsiniz.

</details>

<details>
<summary>Bitcoin-Safe ödemeleri otomatik olarak gönderiyor mu?</summary>

Hayır. Bir ödeme vadesi geldiğinde Schedule, işlemi incelemeniz için Bitcoin-Safe'te hazırlar; imzalama ve yayınlamadan siz sorumlu olmaya devam edersiniz.

</details>

<details>
<summary>Birden fazla alıcıya aynı anda ödeme yapabilir miyim?</summary>

Evet. Birkaç planlanmış ödeme seçin ve **Seçilenleri öde** düğmesine tıklayın. Bitcoin-Safe bunları tek bir toplu işlemde birleştirir.

</details>

<details>
<summary>Bir ödeme nakit veya başka bir yolla yapıldıysa ne olur?</summary>

**Bant dışı** bir ödeme ekleyebilirsiniz. Bu, Bitcoin işlemi olmadan ödemeyi planınıza kaydeder ve ilerlemenin doğru kalmasını sağlar.

</details>
</content>
