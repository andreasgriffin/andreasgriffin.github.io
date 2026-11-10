---
title: "Sync & Chat"
description: "Cüzdanınızdaki eşleri bulun, etiketleri ve kategorileri eşitleyin, güvenle sohbet edin ve PSBT'leri tek tıklamayla paylaşın."
draft: false
tags: ["Plugins", "sync-chat-mainpage"]
images: ["logo.png"]
weight: 30
faq:
  title: "Sync & Chat hakkında sorular"
  items:
    - question: "Cihazlar birbirini nasıl bulur?"
      answer: "Sync & Chat, aynı cüzdan tanımlayıcısını (descriptor) kullanan diğer cihazları arar. Tanımlayıcı, arama için kullanılmadan önce karma (hash) işleminden geçirilir, bu yüzden açık metin olarak ifşa edilmez. Ayrıca bulunan her cihazın sohbette yer alabilmesi için elle eklenmesi ve güvenilir olarak işaretlenmesi gerekir. Bu sayede tanımlayıcı gizli olmasa bile sohbet güvenli kalır."
    - question: "İşbirliği pratikte nasıl çalışır?"
      answer: "1. Kurulum (bir kez): Her katılımcının cihazını ekleyin ve güvenilir olarak işaretleyin.\n2. Oluşturma: Katılımcılardan biri bir PSBT oluşturur ve imzasını ekler.\n3. Paylaşım: PSBT tüm katılımcılara veya yalnızca seçilenlere gönderilir.\n4. İmzalama: Her katılımcı, işlem tamamen imzalanana kadar kendi imzasını ekler.\n5. Yayınlama: Son imzalayan işlemi yayınlar ve işlem her katılımcının cüzdanında görünür."
    - question: "Neler eşitleniyor?"
      answer: "Sync & Chat şunları yönetir:\n- Farklı işletim sistemleri arasında bile, imzacılar arasında eşitlenen madeni para kategorileri ve etiketleri\n- Tek tıklamayla PSBT paylaşımı"
    - question: "Sohbet özel mi?"
      answer: "Evet. Cüzdan sohbeti şifrelidir ve Nostr üzerinden çalışır; etiket yedekleri de Nostr üzerinden şifreli olarak saklanır."
---

### {{< page-title >}}

<p class="lead">Çoklu imzalı (multisig) imzacıları koordine edin ve cüzdan bağlamını doğrudan Bitcoin-Safe'ten senkron tutun.</p>

<ul class="plugin-features">
<li>Aynı cüzdan tanımlayıcısını kullanan diğer cihazları bulun</li>
<li>İmzacılar arasında etiketleri ve kategorileri eşitleyin</li>
<li>Güvenle sohbet edin ve PSBT'leri tek tıklamayla paylaşın</li>
</ul>

### Etiket eşitleme

{{< video src="../../library/label-sync/label-sync.mp4" controls="true" >}}

### Ortak imzalama

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

Çoklu imzalı ortak imzalamanın tam rehberi için bkz. [Çoklu imzada işbirliği]({{< ref "library/collaboration/" >}}).

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
<summary>Cihazlar birbirini nasıl bulur?</summary>

Sync & Chat, aynı cüzdan tanımlayıcısını kullanan diğer cihazları arar. Tanımlayıcı, arama için kullanılmadan önce karma (hash) işleminden geçirilir, bu yüzden açık metin olarak ifşa edilmez. Ayrıca bulunan her cihazın sohbette yer alabilmesi için elle eklenmesi ve güvenilir olarak işaretlenmesi gerekir. Bu sayede tanımlayıcı gizli olmasa bile sohbet güvenli kalır.

</details>

<details>
<summary>İşbirliği pratikte nasıl çalışır?</summary>

1. **Kurulum (bir kez):** Her katılımcının cihazını ekleyin ve güvenilir olarak işaretleyin.
2. **Oluşturma:** Katılımcılardan biri bir PSBT oluşturur ve imzasını ekler.
3. **Paylaşım:** PSBT tüm katılımcılara veya yalnızca seçilenlere gönderilir.
4. **İmzalama:** Her katılımcı, işlem tamamen imzalanana kadar kendi imzasını ekler.
5. **Yayınlama:** Son imzalayan işlemi yayınlar ve işlem her katılımcının cüzdanında görünür.

</details>

<details>
<summary>Neler eşitleniyor?</summary>

Sync & Chat şunları yönetir:

- Farklı işletim sistemleri arasında bile, imzacılar arasında eşitlenen madeni para kategorileri ve etiketleri
- Tek tıklamayla PSBT paylaşımı

</details>

<details>
<summary>Sohbet özel mi?</summary>

Evet. Cüzdan sohbeti şifrelidir ve Nostr üzerinden çalışır; etiket yedekleri de Nostr üzerinden şifreli olarak saklanır.

</details>

{{< sync-page-box >}}
</content>
