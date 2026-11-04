---
title: "Seed COLDCARD non sécurisée"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "Guide minimal pour déplacer des fonds protégés par une seed générée sur un appareil Coinkite."
---

[Coinkite a révélé une faiblesse dans la génération des seeds sur les firmwares COLDCARD concernés](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). Consultez également [l'analyse technique de Block sur le fallback prévisible du RNG et le reseed sur 32 bits](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware). La mise à jour du firmware ne répare pas une seed existante.

**Si vous avez créé une seed avec un produit Coinkite, migrez RAPIDEMENT !**

## Liste de contrôle pour la migration

1. Générez une seed entièrement nouvelle sur un **appareil de signature autre qu'un COLDCARD** ([voir les appareils pris en charge]({{< ref "library/supported-hardware-signers" >}})). Ne réutilisez pas l'ancienne seed. Utilisez ensuite ce signataire avec l'assistant de configuration de Bitcoin-Safe pour créer un nouveau [wallet à signature unique]({{< ref "library/setup-singlesig-wallet" >}}) ou [wallet multisignature]({{< ref "library/setup-multisig-wallet" >}}).
   - Si aucun signataire matériel autre qu'un COLDCARD n'est disponible, [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}}) est une option sur un appareil Android dédié, réinitialisé aux paramètres d'usine, maintenu hors ligne et utilisé uniquement pour signer.
   - Effectuez le test de réception et d'envoi de l'assistant afin de vérifier que le nouveau wallet est correctement configuré : vérifiez sa sauvegarde et une adresse de réception sur le nouveau signataire, recevez un petit montant de test, puis réalisez un auto-envoi vers une autre adresse vérifiée du nouveau wallet.
2. Signez la transaction de migration :
   - **Si le wallet concerné est à signature unique :** diffusez-la normalement avec des frais élevés afin qu'elle soit confirmée rapidement.
   - **Si le wallet concerné est multisignature :** ne la diffusez pas normalement, car cela révèle ses clés publiques dans le mempool public. Copiez la transaction brute signée et soumettez-la directement via [MARA Slipstream](https://slipstream.mara.com/).
3. Conservez l'ancien COLDCARD jusqu'à ce que le solde complet soit arrivé et confirmé dans le nouveau wallet, puis mettez-le à jour avec le firmware le plus récent.

Si vous aidez quelqu'un à migrer, ne lui demandez jamais de partager, photographier ou saisir ses mots seed. La seed doit rester privée et être saisie uniquement sur l'appareil de signature.
