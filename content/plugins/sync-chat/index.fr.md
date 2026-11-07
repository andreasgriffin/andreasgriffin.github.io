---
title: "Sync & Chat"
description: "Découvrez les pairs de votre portefeuille, synchronisez les libellés et catégories, discutez en toute sécurité et partagez des PSBT en un clic."
draft: false
tags: ["Plugins", "sync-chat-mainpage"]
images: ["logo.png"]
weight: 30
faq:
  title: "Questions sur Sync & Chat"
  items:
    - question: "Comment les appareils se trouvent-ils ?"
      answer: "Sync & Chat recherche les autres appareils qui utilisent le même descripteur de portefeuille. Le descripteur est haché avant d'être utilisé pour la recherche, il n'est donc pas exposé en clair. Chaque appareil découvert doit en outre être ajouté et approuvé manuellement avant de pouvoir participer au chat. Le chat reste ainsi sûr même si le descripteur n'est pas secret."
    - question: "Comment fonctionne la collaboration en pratique ?"
      answer: "1. Configuration (une seule fois) : ajoutez et approuvez l'appareil de chaque participant.\n2. Création : un participant crée une PSBT et y ajoute sa signature.\n3. Partage : la PSBT est envoyée à tous les participants, ou seulement à certains d'entre eux.\n4. Signature : chaque participant ajoute sa signature jusqu'à ce que la transaction soit entièrement signée.\n5. Diffusion : le dernier signataire diffuse la transaction, qui apparaît ensuite dans le portefeuille de chaque participant."
    - question: "Qu'est-ce qui est synchronisé ?"
      answer: "Sync & Chat gère :\n- Les catégories et libellés des coins, synchronisés entre les signataires, même entre des systèmes d'exploitation différents\n- Le partage de PSBT en un clic"
    - question: "Le chat est-il privé ?"
      answer: "Oui. Le chat du portefeuille est chiffré et passe par Nostr ; les sauvegardes des libellés sont également stockées chiffrées via Nostr."
---

### {{< page-title >}}

<p class="lead">Coordonnez les signataires multisig et gardez le contexte du portefeuille synchronisé directement depuis Bitcoin-Safe.</p>

<ul class="plugin-features">
<li>Découvrez les autres appareils utilisant le même descripteur de portefeuille</li>
<li>Synchronisez les libellés et catégories entre les signataires</li>
<li>Discutez en toute sécurité et partagez des PSBT en un clic</li>
</ul>

### Synchronisation des libellés

{{< video src="../../library/label-sync/label-sync.mp4" controls="true" >}}

### Signature collaborative

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

Pour le guide complet de la signature multisig collaborative, voir [Collaboration dans un multisig]({{< ref "library/collaboration/" >}}).

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">Télécharger Bitcoin-Safe</h2>
<p class="text-muted mb-3">Les plugins sont inclus dans Bitcoin-Safe. Téléchargez l'application pour les essayer.</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">Télécharger Bitcoin-Safe</a>
<small class="text-muted">Logiciel libre et open source · Windows, macOS, Linux</small>
</div>
</section>

### Questions fréquentes

<details>
<summary>Comment les appareils se trouvent-ils ?</summary>

Sync & Chat recherche les autres appareils qui utilisent le même descripteur de portefeuille. Le descripteur est haché avant d'être utilisé pour la recherche, il n'est donc pas exposé en clair. Chaque appareil découvert doit en outre être ajouté et approuvé manuellement avant de pouvoir participer au chat. Le chat reste ainsi sûr même si le descripteur n'est pas secret.

</details>

<details>
<summary>Comment fonctionne la collaboration en pratique ?</summary>

1. **Configuration (une seule fois) :** ajoutez et approuvez l'appareil de chaque participant.
2. **Création :** un participant crée une PSBT et y ajoute sa signature.
3. **Partage :** la PSBT est envoyée à tous les participants, ou seulement à certains d'entre eux.
4. **Signature :** chaque participant ajoute sa signature jusqu'à ce que la transaction soit entièrement signée.
5. **Diffusion :** le dernier signataire diffuse la transaction, qui apparaît ensuite dans le portefeuille de chaque participant.

</details>

<details>
<summary>Qu'est-ce qui est synchronisé ?</summary>

Sync & Chat gère :

- Les catégories et libellés des coins, synchronisés entre les signataires, même entre des systèmes d'exploitation différents
- Le partage de PSBT en un clic

</details>

<details>
<summary>Le chat est-il privé ?</summary>

Oui. Le chat du portefeuille est chiffré et passe par Nostr ; les sauvegardes des libellés sont également stockées chiffrées via Nostr.

</details>

{{< sync-page-box >}}
</content>
