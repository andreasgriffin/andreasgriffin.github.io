---
title: "Güvenli Olmayan COLDCARD Seed'i"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "Coinkite cihazında oluşturulan bir seed ile korunan fonları taşımak için kısa rehber."
---

[Coinkite, etkilenen COLDCARD aygıt yazılımındaki seed üretiminde bir zayıflık açıkladı](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). Ayrıca [Block'un öngörülebilir RNG yedeği ve 32 bitlik yeniden tohumlama hakkındaki teknik analizine](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware) bakın. Aygıt yazılımını güncellemek mevcut bir seed'i düzeltmez.

**Herhangi bir Coinkite ürünüyle seed oluşturduysanız, YAKINDA taşıyın!**

## Taşıma kontrol listesi

1. **COLDCARD olmayan bir imzalama cihazında** ([desteklenen cihazlara bakın]({{< ref "library/supported-hardware-signers" >}})) tamamen yeni bir seed oluşturun. Eski seed'i yeniden kullanmayın. Ardından bu imzalayıcıyı Bitcoin-Safe kurulum sihirbazıyla kullanarak yeni bir [tek imzalı cüzdan]({{< ref "library/setup-singlesig-wallet" >}}) veya [çoklu imzalı cüzdan]({{< ref "library/setup-multisig-wallet" >}}) oluşturun.
   - COLDCARD dışında bir donanım imzalayıcı yoksa, fabrika ayarlarına sıfırlanmış, çevrimdışı tutulan ve yalnızca imzalama için kullanılan özel bir Android cihazında [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}}) kullanılabilir.
   - Yeni cüzdanın doğru kurulduğundan emin olmak için sihirbazdaki alma ve gönderme testini tamamlayın: yedeği ve yeni imzalayıcıdaki bir alma adresini doğrulayın, küçük bir test tutarı alın ve bu tutarı yeni cüzdandaki doğrulanmış başka bir adrese başarıyla kendinize gönderin.
2. Taşıma işlemini imzalayın:
   - **Etkilenen cüzdan tek imzalıysa:** hızla onaylanması için yüksek bir ücretle normal şekilde yayınlayın.
   - **Etkilenen cüzdan çoklu imzalıysa:** normal şekilde yayınlamayın; çünkü bu, açık anahtarlarını herkese açık mempool'da ortaya çıkarır. İmzalı ham işlemi kopyalayıp doğrudan [MARA Slipstream](https://slipstream.mara.com/) üzerinden gönderin.
3. Bakiyenin tamamı yeni cüzdana ulaşıp onaylanana kadar eski COLDCARD'ı saklayın, ardından en son aygıt yazılımına güncelleyin.

Birinin taşıma yapmasına yardım ediyorsanız seed kelimelerini paylaşmasını, fotoğraflamasını veya yazmasını asla istemeyin. Seed gizli kalmalı ve yalnızca imzalama cihazına girilmelidir.
