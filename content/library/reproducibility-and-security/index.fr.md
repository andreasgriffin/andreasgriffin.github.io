---
aliases:
  - "/fr/features/reproducibility-and-security/"
title: "Securite et reproductibilite"
description: "Bitcoin Safe applique un niveau eleve de securite binaire: builds reproductibles, commits signes, versions signees et surveillance externe independante."
draft: false
bucket: features
tags: ["Featured", "Security"]
images: ["logo.png"]
keywords: ["reproducible builds", "verify binaries", "signed commits", "signed releases", "appimage", "flatpak", "windows exe", "binary security"]
weight: 18
---

### {{< page-title >}}
{{< page-description >}}
<br>

![Resultats de builds reproductibles pour Bitcoin Safe](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 500px;" }

Nous avons mis en place plusieurs protections pour garantir l'integrite des telechargements sur le site, afin que l'application que vous telechargez corresponde vraiment au code source public:

- **Builds reproductibles**: Les builds Linux `deb`, `AppImage` et `Flatpak`, ainsi que `portable exe` et `setup exe` sous Windows, peuvent etre reproduits octet par octet. Si un fichier reconstruit correspond exactement, c'est un indice fort que le binaire a ete genere a partir du meme code source.
- **Historique du depot signe**: Le [depot GitHub de Bitcoin Safe](https://github.com/andreasgriffin/bitcoin-safe/commits/main) publie des commits signes et verifies, afin que les relecteurs puissent verifier qui a produit le code inclus dans une version.
- **Binaires signes**: Les fichiers de publication sont signes avec la [cle publique PGP]({{< gpg_key_link >}}) de Bitcoin Safe, et les binaires Windows suivent egalement la [politique de signature de code]({{< ref "code-signing-policy" >}}).
- **Verifications independantes de reproductibilite**: [WalletScrutiny](https://walletscrutiny.com/desktop/bitcoin.safe/) suit Bitcoin Safe de maniere independante et affiche l'etat de verification reproductible des versions desktop.
- **Surveillance continue des signatures**: [BinaryWatch](https://binarywatch.org/) verifie regulierement les fichiers de version de Bitcoin Safe et si leurs signatures sont toujours valides par rapport a la [cle publique PGP]({{< gpg_key_link >}}) de Bitcoin Safe.
- **Verification des mises a jour**: Les mises a jour sont affichees dans Bitcoin Safe, et leur signature est verifiee automatiquement.

Dans leur ensemble, ces mesures placent Bitcoin Safe dans un petit groupe de projets qui traitent la securite binaire comme un element central de la securite des utilisateurs, et non comme un detail ajoute apres coup.

### La securite est le critere central dans chaque aspect de Bitcoin Safe

Au-dela de l'integrite des binaires, Bitcoin Safe est concu autour de valeurs par defaut sures, de bonnes pratiques operationnelles et d'une guidance claire pour l'utilisateur. Quelques exemples:

- **Conservation centree sur le hardware**: Bitcoin Safe exige des [signataires hardware]({{< ref "library/supported-hardware-signers" >}}), afin que les seeds restent sur des appareils dedies au lieu de devenir des secrets chauds sur un ordinateur generaliste.
- **Parcours de configuration plus sur**: L'assistant de configuration aide les utilisateurs a creer des wallets vraiment prets a l'usage reel, avec notamment des tests de [signataires hardware]({{< ref "library/supported-hardware-signers" >}}), des [fiches PDF de sauvegarde]({{< ref "library/pdf-export/" >}}) et des conseils sur la maniere de stocker les signataires hardware et les sauvegardes de seed.
- **Verification des adresses de reception**: Bitcoin Safe permet de [verifier facilement les adresses de reception]({{< ref "library/verify-receive-address/" >}}) sur le signataire lui-meme avant de les partager.
- **Detection de l'empoisonnement d'adresse**: L'application avertit en cas [d'adresses suspectes et ressemblantes]({{< ref "library/address-poisoning/" >}}).
- **Securite multisig**: Bitcoin Safe prend en charge les wallets multisignatures, afin que des montants plus importants puissent etre proteges par plusieurs appareils ou plusieurs personnes au lieu d'un point de defaillance unique.
- **Une collaboration qui facilite le multisig**: Bitcoin Safe rend la [collaboration multisignature]({{< ref "library/collaboration/" >}}) pratique, ce qui facilite nettement la coordination de la configuration et de la signature au quotidien.
- **Flux de signature clairs**: Des ecrans de signature specifiques a chaque appareil reduisent la confusion pendant la revision des PSBT et aident les utilisateurs a effectuer la bonne action sur le bon signataire.
