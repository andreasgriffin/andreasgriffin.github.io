---
title: "Seed COLDCARD insegura"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "Guia mínima per traslladar fons des d'una seed generada en un dispositiu Coinkite."
---

[Coinkite ha revelat una feblesa en la generació de seeds del firmware COLDCARD afectat](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). Consulta també [l'anàlisi tècnica de Block sobre el fallback predictible de l'RNG i el reseed de 32 bits](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware). Actualitzar el firmware no repara una seed existent.

**Si has creat una seed amb qualsevol producte Coinkite, migra AVIAT!**

## Llista de migració

1. Genera una seed completament nova en un **dispositiu de signatura que no sigui COLDCARD** ([consulta els dispositius compatibles]({{< ref "library/supported-hardware-signers" >}})). No reutilitzis la seed antiga. Després, utilitza aquest signador amb l'assistent de configuració de Bitcoin-Safe per crear un [moneder de signatura única]({{< ref "library/setup-singlesig-wallet" >}}) nou o un [moneder multifirma]({{< ref "library/setup-multisig-wallet" >}}) nou.
   - Si no tens disponible cap signador de maquinari que no sigui COLDCARD, [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}}) és una opció en un dispositiu Android dedicat, restablert de fàbrica, mantingut fora de línia i utilitzat només per signar.
   - Completa la prova de recepció i enviament de l'assistent per assegurar-te que el moneder nou està ben configurat: verifica'n la còpia de seguretat i una adreça de recepció al signador nou, rep una petita quantitat de prova i fes correctament un autoenviament a una altra adreça verificada del moneder nou.
2. Signa la transacció de migració:
   - **Si el moneder afectat és de signatura única:** difon-la de la manera habitual amb una comissió alta perquè es confirmi ràpidament.
   - **Si el moneder afectat és multifirma:** no la difonguis de la manera habitual, perquè fer-ho revela les seves claus públiques a la mempool pública. Copia la transacció en brut signada i envia-la directament mitjançant [MARA Slipstream](https://slipstream.mara.com/).
3. Conserva el COLDCARD antic fins que el saldo complet hagi arribat i s'hagi confirmat al moneder nou; després, actualitza'l al firmware més recent.

Si ajudes algú a migrar, no li demanis mai que comparteixi, fotografiï o escrigui les paraules de la seed. La seed ha de romandre privada i introduir-se només al dispositiu de signatura.
