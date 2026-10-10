---
title: "Seed COLDCARD non sécurisée"
date: "2026-08-02"
draft: false
description: "Coinkite a révélé une faiblesse critique dans la génération des seeds sur les firmwares COLDCARD concernés. Si vous avez créé une seed avec un appareil Coinkite affecté, déplacez vos fonds vers une nouvelle seed."
images: ["COLDCARD Security Advisory Notice - Migrate ASAP.png"]
---

## Résumé

[Coinkite a révélé une faiblesse critique dans la génération des seeds sur les firmwares COLDCARD concernés](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). [L'analyse technique de Block](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware) a identifié la cause : un générateur de nombres aléatoires logiciel prévisible utilisé à la place du RNG matériel du dispositif, et avertit qu'**une exploitation active est en cours**. La mise à jour du firmware **ne** répare **pas** une seed existante.

**Si vous avez créé une seed avec un appareil Coinkite affecté, déplacez vos fonds vers une nouvelle seed.**

## Mon appareil est-il affecté ?

L'exposition dépend de la **version du firmware installée au moment de la génération de la seed**, pas de la date de fabrication de l'appareil.

| Appareil | Firmware utilisé pour générer la seed | Statut |
|---|---|---|
| Mk1 | Tous les firmwares publiés | Non affecté |
| Mk2 / Mk3 | v3.2.2 ou antérieur | Non affecté (utilise le RNG matériel) |
| Mk2 / Mk3 | v4.0.0 – v4.1.9 | **Vulnérable** — pas de reseed sécurisé |
| Mk4 | Production v5.0.0 et ultérieur | **Vulnérable** — limité à ~72 bits d'entropie |
| Q | Tout le firmware de production | **Vulnérable** — limité à ~72 bits d'entropie |
| Mk5 | Tout le firmware de production | **Vulnérable** — limité à ~72 bits d'entropie |
| TAPSIGNER, OPENDIME, SATSCARD | — | Non affecté (code différent) |

Notez qu'exporter une seed non sécurisée et l'importer dans un autre portefeuille **ne** la corrige **pas** : la seed elle-même reste affectée.

## Installez le firmware corrigé avant de générer une nouvelle seed

Un firmware corrigé est maintenant disponible pour chaque modèle et canal de publication affectés. Ne générez pas une nouvelle seed sur une COLDCARD tant qu'il n'est pas installé.

| Appareil | Firmware corrigé |
|---|---|
| Mk2 / Mk3 | 4.2.0 ou ultérieur |
| Mk4 / Mk5 (standard) | 5.6.0 ou ultérieur |
| Q (standard) | 1.5.0Q ou ultérieur |
| Mk4 / Mk5 (Edge) | 6.6.0X ou ultérieur |
| Q (Edge) | 6.6.0QX ou ultérieur |

Standard et Edge sont des canaux de publication séparés. Si vous utilisez Edge, installez la version Edge corrigée pour votre modèle : ne supposez pas qu'une ancienne version Edge 6.x est corrigée simplement parce que son numéro est supérieur à celui de la version standard.

## Les lancers de dés ou une phrase secrète me protègent-ils ?

- **Lancers de dés :** le bug n'affecte que l'entropie générée par l'appareil. Si vous avez saisi au moins **50 lancers de dés indépendants et privés** lors de la création de la seed (99 ou plus pour environ 256 bits d'entropie), la saisie des dés a à elle seule apporté au moins 128 bits d'entropie indépendante et la seed n'est pas considérée à risque de ce seul fait. Moins de 50 lancers — ou si vous ignorez combien en ont été saisis ou s'ils étaient privés — **migrez**.
- **Phrase secrète BIP-39 :** une phrase secrète BIP-39 forte et unique (pas le PIN de la COLDCARD) ajoute une barrière indépendante, mais elle **ne** répare **pas** la seed affectée. Si votre phrase secrète est courte, courante, réutilisée ou devinable — ou si vous n'êtes pas sûr de sa robustesse — considérez les fonds à risque et migrez immédiatement. Même avec une phrase secrète forte, migrez vers une seed nouvellement générée dès que possible.

## Liste de contrôle pour la migration

Migrez calmement et prudemment. Précipiter une migration de portefeuille peut créer un risque plus immédiat que le problème que vous cherchez à résoudre.

1. **Installez le firmware corrigé** de votre modèle avant de générer une seed de remplacement. Si vous préférez, générez la nouvelle seed sur un **appareil de signature non COLDCARD** ([voir les appareils pris en charge]({{< ref "library/supported-hardware-signers" >}})) — dans tous les cas, **ne** réutilisez **pas** l'ancienne seed.
2. Générez une seed entièrement nouvelle et **enregistrez-la**. Avant de déposer des fonds, vérifiez la sauvegarde écrite, l'empreinte du portefeuille et une adresse de réception.
3. Utilisez l'assistant de configuration de Bitcoin-Safe pour créer un nouveau [portefeuille à signature unique]({{< ref "library/setup-singlesig-wallet" >}}) ou [portefeuille multisignature]({{< ref "library/setup-multisig-wallet" >}}) avec la nouvelle seed.
4. Réalisez le test de réception et d'envoi de l'assistant : vérifiez la sauvegarde et une adresse de réception sur le nouveau signataire, recevez un petit montant de test et envoyez-le-vous avec succès vers une autre adresse vérifiée du nouveau portefeuille.
5. Signez et diffusez la transaction de migration :
   - **Portefeuille à signature unique :** diffusez-la normalement avec des frais élevés pour qu'elle se confirme rapidement.
   - **Portefeuille multisignature :** ne la diffusez pas normalement, car cela révèle ses clés publiques dans le mempool public. Copiez la transaction brute signée et soumettez-la directement via [MARA Slipstream](https://slipstream.mara.com/).
6. Conservez l'ancienne COLDCARD et sa sauvegarde jusqu'à ce que le **solde complet** soit arrivé et confirmé dans le nouveau portefeuille. Ce n'est qu'alors que vous effacerez l'ancienne seed.

Si la Mk2/Mk3 est votre seul appareil de signature, installez d'abord le firmware 4.2.0 ou ultérieur : il génère correctement des seeds de remplacement, vous n'avez donc pas besoin d'une COLDCARD plus récente pour terminer la migration. Suivez les mêmes étapes, en alternant soigneusement entre l'ancienne et la nouvelle seed sur le seul appareil, et conservez l'ancienne sauvegarde jusqu'à ce que la migration soit entièrement confirmée.

## Si vous utilisez la multisignature

Si une configuration multisignature est composée **exclusivement** d'appareils affectés, la vulnérabilité s'applique toujours. Protégez la configuration avec un quorum incluant au moins un appareil de signature non affecté.

## Aider quelqu'un d'autre à migrer

Ne lui demandez jamais de partager, photographier ou saisir ses mots de seed. La seed doit rester privée et n'être saisie que sur l'appareil de signature lui-même.
