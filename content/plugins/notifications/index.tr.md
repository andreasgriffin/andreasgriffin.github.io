---
title: "Cüzdan bildirimleri"
description: "Bitcoin-Safe cüzdan ve uygulama bildirimlerini yapılandırdığınız hedeflere iletin; teslimat, gizlilik ve zamanlama denetimleriyle."
draft: false
tags: ["Plugins"]
images: ["notifications.png"]
weight: 35
faq:
  title: "Cüzdan bildirimleri hakkında sorular"
  items:
    - question: "Bitcoin-Safe bildirimleri nereye gönderebilir?"
      answer: "Bitcoin-Safe bildirimleri şunlara gönderebilir:\n- Webhook'lara: genel JSON veya Slack uyumlu, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy ve Gotify biçimleri\n- Nostr doğrudan mesajlarına\n- Telegram botlarına\n- SMTP üzerinden e-postaya\n- CalDAV takvimlerine"
    - question: "Uyarılardan hassas ayrıntıları çıkarabilir miyim?"
      answer: "Evet. Hassas ayrıntıları gizle seçeneğini açtığınızda mesaj yalnızca bir Bitcoin-Safe bildirim olayının gerçekleştiğini belirten genel bir uyarı içerir."
    - question: "Hangi olayların nereye gideceğini kontrol edebilir miyim?"
      answer: "Her hedefin kendi kuralları vardır. Hangi olay türlerini alacağını seçersiniz:\n- Cüzdan işlemleri\n- Planlanmış ödemeler\n- Eşitleme ve sohbet\n- Uyarılar\n\nİsteğe bağlı olarak rastgele bir teslimat gecikmesi de ayarlayabilirsiniz."
    - question: "Uygulamanın kilidinin açık kalması gerekir mi?"
      answer: "Hayır. Kilitle ve Tepsiye Küçült seçeneği, cüzdan kilitliyken Bitcoin-Safe'in arka planda çalışmasını sağlar."
---

### {{< page-title >}}

<p class="lead">Cüzdan etkinliğiyle ilgili bildirimleri sizin için uygun kanallardan alın.</p>

<ul class="plugin-features">
<li>Gelen ve giden işlemler, Sync&Chat mesajları, vadesi gelen planlanmış ödemeler, ...</li>
<li>Uyarıları webhook'lara, Nostr'a, Telegram'a, e-postaya, takvimlere ve daha fazlasına iletin</li>
<li>Her hedefin hangi olayları alacağını seçin ve hassas ayrıntıları gizleyin</li>
<li>Bitcoin-Safe'i arka planda tutun; cüzdan kilitliyken çalışmaya devam etmesi için <strong>Kilitle ve Tepsiye Küçült</strong> seçeneğini kullanın</li>
</ul>

### Webhook kurulumu

{{< video "webhook.mp4" controls >}}

### Nostr doğrudan mesajları

{{< video "nostr.mp4" controls >}}

### Takvim bildirimleri

{{< video "calendar.mp4" controls >}}

### Hedeflerinizi bağlayın

- Bir veya daha fazla hedef ekleyin. Her birinin kendi alıcıları ve teslimat kuralları olabilir.
- **E-posta:** Ana bilgisayar, port, kimlik bilgileri, gönderici ve güvenlik ayarlarıyla doğrudan bir SMTP sunucusuna bağlanın. Bu, yönetilen bir Gmail veya Outlook entegrasyonu değildir.
- **Telegram:** Bir bot aracılığıyla bir sohbete gönderin. Botu denetlemek ve yakın zamandaki sohbet kimliklerini bulmak için bota mesaj gönderin.
- **Nostr DM:** Bir gönderici anahtarıyla yapılandırılmış röleler üzerinden `npub` alıcılarına şifreli NIP-17 mesajları gönderin.
- **CalDAV:** Yapılandırılmış bir Nextcloud takvimi gibi mevcut bir takvime etkinlik ekleyin.
- **Webhook'lar:** Genel JSON biçiminde veya Slack uyumlu uç noktalar, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy ve Gotify için biçimlerde gönderin. Yaygın uç nokta türleri otomatik algılanabilir.
- Hedef ayarlarını kaydedin ve destekleniyorsa test işlemini kullanın.

### Neyin gönderileceğini seçin

- Her hedefin hangi olay türlerini alacağını seçin:
  - Cüzdan işlemleri
  - Planlanmış ödemeler
  - Eşitleme ve sohbet
  - Uyarılar
- Hassas ayrıntıları gizleyin. Bu durumda mesaj yalnızca bir Bitcoin-Safe bildirim olayının gerçekleştiğini belirten genel bir uyarı içerir.
- Seçtiğiniz en yüksek değere kadar rastgele bir teslimat gecikmesi ayarlayın.
- Cüzdan işlemi mesajları, kullanılabilir olduğunda ve ayrıntılar gizli değilse bir blok gezgini bağlantısı içerebilir.

### Teslimatı inceleyin

- Son geçmiş her olayı, hedefi, bağdaştırıcıyı, zamanı ve sonucu gösterir: gönderildi, kısmen veya başarısız.
- Teslimat, yapılandırılmış hedefinize ve onun kullanılabilirliğine bağlıdır. Harici hizmetlere hangi bilgileri gönderdiğinizi göz önünde bulundurun.

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
<summary>Bitcoin-Safe bildirimleri nereye gönderebilir?</summary>

Bitcoin-Safe bildirimleri şunlara gönderebilir:

- Webhook'lara: genel JSON veya Slack uyumlu, Discord, Google Chat, Microsoft Teams, Telegram Bot API, ntfy ve Gotify biçimleri
- Nostr doğrudan mesajlarına
- Telegram botlarına
- SMTP üzerinden e-postaya
- CalDAV takvimlerine

</details>

<details>
<summary>Uyarılardan hassas ayrıntıları çıkarabilir miyim?</summary>

Evet. Hassas ayrıntıları gizle seçeneğini açtığınızda mesaj yalnızca bir Bitcoin-Safe bildirim olayının gerçekleştiğini belirten genel bir uyarı içerir.

</details>

<details>
<summary>Hangi olayların nereye gideceğini kontrol edebilir miyim?</summary>

Her hedefin kendi kuralları vardır. Hangi olay türlerini alacağını seçersiniz:

- Cüzdan işlemleri
- Planlanmış ödemeler
- Eşitleme ve sohbet
- Uyarılar

İsteğe bağlı olarak rastgele bir teslimat gecikmesi de ayarlayabilirsiniz.

</details>

<details>
<summary>Uygulamanın kilidinin açık kalması gerekir mi?</summary>

Hayır. Kilitle ve Tepsiye Küçült seçeneği, cüzdan kilitliyken Bitcoin-Safe'in arka planda çalışmasını sağlar.

</details>
</content>
