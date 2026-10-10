---
title: "Güvenli Olmayan COLDCARD Seed'i"
date: "2026-08-02"
draft: false
description: "Coinkite, etkilenen COLDCARD aygıt yazılımındaki seed üretiminde kritik bir zayıflık açıkladı. Etkilenen herhangi bir Coinkite cihazında seed oluşturduysanız, fonlarınızı yeni bir seed'e taşıyın."
images: ["COLDCARD Security Advisory Notice - Migrate ASAP.png"]
---

## Özet

[Coinkite, etkilenen COLDCARD aygıt yazılımındaki seed üretiminde kritik bir zayıflık açıkladı](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). [Block'un teknik analizi](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware), cihazın donanım RNG'si yerine kullanılan öngörülebilir yazılımsal rastgele sayı üreticisini sorunun kaynağı olarak belirledi ve **aktif bir istismarın sürdüğü** konusunda uyarıyor. Aygıt yazılımını güncellemek mevcut bir seed'i **onarmaz**.

**Etkilenen herhangi bir Coinkite cihazında seed oluşturduysanız, fonlarınızı yeni bir seed'e taşıyın.**

## Cihazım etkileniyor mu?

Etkilenme, cihazın ne zaman üretildiğine değil, **seed'in oluşturulduğu sırada kurulu olan aygıt yazılımı sürümüne** bağlıdır.

| Cihaz | Seed'i oluşturmak için kullanılan aygıt yazılımı | Durum |
|---|---|---|
| Mk1 | Yayınlanan tüm aygıt yazılımları | Etkilenmez |
| Mk2 / Mk3 | v3.2.2 veya daha eski | Etkilenmez (donanım RNG'sini kullanır) |
| Mk2 / Mk3 | v4.0.0 – v4.1.9 | **Savunmasız** — güvenli reseed yok |
| Mk4 | v5.0.0 ve sonrası üretim | **Savunmasız** — ~72 bit entropiyle sınırlı |
| Q | Tüm üretim aygıt yazılımları | **Savunmasız** — ~72 bit entropiyle sınırlı |
| Mk5 | Tüm üretim aygıt yazılımları | **Savunmasız** — ~72 bit entropiyle sınırlı |
| TAPSIGNER, OPENDIME, SATSCARD | — | Etkilenmez (farklı kod tabanı) |

Güvenli olmayan bir seed'i dışa aktarıp başka bir cüzdana aktarmanın **onarmadığını** unutmayın: seed'in kendisi etkilenmeye devam eder.

## Yeni bir seed oluşturmadan önce düzeltilmiş aygıt yazılımını kurun

Düzeltilmiş aygıt yazılımı artık etkilenen her model ve sürüm kanalı için mevcuttur. Kurulana kadar bir COLDCARD'da yeni seed oluşturmayın.

| Cihaz | Düzeltilmiş aygıt yazılımı |
|---|---|
| Mk2 / Mk3 | 4.2.0 veya sonrası |
| Mk4 / Mk5 (standard) | 5.6.0 veya sonrası |
| Q (standard) | 1.5.0Q veya sonrası |
| Mk4 / Mk5 (Edge) | 6.6.0X veya sonrası |
| Q (Edge) | 6.6.0QX veya sonrası |

Standard ve Edge ayrı sürüm kanallarıdır. Edge kullanıyorsanız, modeliniz için düzeltilmiş Edge sürümünü kurun; yalnızca sürüm numarası standard sürümden yüksek diye eski bir Edge 6.x sürümünün düzeltildiğini varsaymayın.

## Zar atışları veya bir parola ifadesi beni korur mu?

- **Zar atışları:** hata yalnızca cihaz tarafından üretilen entropiyi etkiler. Seed'i oluştururken en az **50 bağımsız, gizli zar atışı** girdiyseniz (yaklaşık 256 bit entropi için 99 veya daha fazlası), zar girdisi tek başına en az 128 bit bağımsız entropi sağlamıştır ve seed yalnızca bu sorun nedeniyle risk altında sayılmaz. 50 atıştan az — veya kaç atış girildiğinden ya da gizli olup olmadığından emin değilseniz — **taşıyın**.
- **BIP-39 parola ifadesi:** güçlü, benzersiz bir BIP-39 parola ifadesi (COLDCARD PIN'i değil) bağımsız bir engel ekler, ancak etkilenen seed'i **onarmaz**. Parola ifadeniz kısa, yaygın, yeniden kullanılmış veya tahmin edilebilir ise — ya da gücünden emin değilseniz — fonları risk altında kabul edin ve hemen taşıyın. Güçlü bir parola ifadesi olsa bile, mümkün olan en kısa sürede yeni oluşturulmuş bir seed'e geçin.

## Taşıma kontrol listesi

Sakin ve dikkatli bir şekilde taşıyın. Cüzdan taşımayı aceleye getirmek, çözmeye çalıştığınız sorundan daha acil bir risk oluşturabilir.

1. Yedek bir seed oluşturmadan önce modeliniz için **düzeltilmiş aygıt yazılımını kurun**. İsterseniz yeni seed'i **COLDCARD olmayan bir imzalama cihazında** oluşturun ([desteklenen cihazlara bakın]({{< ref "library/supported-hardware-signers" >}})) — her iki durumda da eski seed'i **yeniden kullanmayın**.
2. Tamamen yeni bir seed oluşturun ve **kaydedin**. Herhangi bir fon yatırmadan önce yazılı yedeği, cüzdan parmak izini ve bir alım adresini doğrulayın.
3. Bitcoin-Safe'in kurulum sihirbazını kullanarak yeni seed ile yeni bir [tek imzalı cüzdan]({{< ref "library/setup-singlesig-wallet" >}}) veya [çoklu imza cüzdanı]({{< ref "library/setup-multisig-wallet" >}}) oluşturun.
4. Sihirbazın alım-gönderim testini tamamlayın: yeni imzalayıcıda yedeği ve bir alım adresini doğrulayın, küçük bir test tutarı alın ve bunu yeni cüzdandaki doğrulanmış başka bir adrese başarıyla gönderin.
5. Taşıma işlemini imzalayın ve yayınlayın:
   - **Tek imzalı cüzdan:** hızlı onaylanması için yüksek ücretle normal şekilde yayınlayın.
   - **Çoklu imza cüzdanı:** normal şekilde yayınlamayın, çünkü bu, açık anahtarlarını herkese açık mempool'da ortaya çıkarır. İmzalanmış ham işlemi kopyalayın ve doğrudan [MARA Slipstream](https://slipstream.mara.com/) üzerinden gönderin.
6. **Tüm bakiye** yeni cüzdana ulaşıp onaylanana kadar eski COLDCARD'ı ve yedeğini saklayın. Ancak o zaman eski seed'i silin.

Mk2/Mk3 tek imzalama cihazınızsa, önce 4.2.0 veya sonrası aygıt yazılımını kurun: yedek seed'leri doğru şekilde üretir, bu nedenle taşımayı tamamlamak için daha yeni bir COLDCARD'a ihtiyacınız yoktur. Aynı adımları izleyin, tek cihazda eski ve yeni seed arasında dikkatlice geçiş yapın ve taşıma tamamen onaylanana kadar eski yedeği saklayın.

## Çoklu imza kullanıyorsanız

Bir çoklu imza yapılandırması **yalnızca** etkilenen cihazlardan oluşuyorsa, güvenlik açığı geçerli olmaya devam eder. En az bir etkilenmeyen imzalama cihazı içeren bir çoğunluk ile yapılandırmayı koruyun.

## Başka birinin taşımasına yardım ederken

Onlardan asla seed kelimelerini paylaşmasını, fotoğraflamasını veya yazmasını istemeyin. Seed gizli kalmalı ve yalnızca imzalama cihazının kendisine girilmelidir.
