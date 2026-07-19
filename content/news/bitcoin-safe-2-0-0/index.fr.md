---
title: "Bitcoin-Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "Notes de version pour Bitcoin-Safe 2.0.0 avec un assistant de configuration reconstruit, une synchronisation privee via Compact Block Filters et une prise en charge etendue des portefeuilles materiels."
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">Annonce de sortie</p>
    <h2 class="display-6 mb-3">Bitcoin-Safe 2.0 - configuration guidee des portefeuilles, synchronisation privee de la chaine et signatures centrees sur les appareils</h2>
    <p class="lead mb-4">Cette version apporte un assistant de configuration reconstruit, une synchronisation privee de la chaine avec Compact Block Filters et un flux de signature organise autour de chaque appareil materiel. Si le cold storage vous interessait sans que vous soyez tout a fait rassure, c'est la version a essayer.</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Telecharger Bitcoin-Safe 2.0</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">Voir les nouveautes</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Configuration pas a pas du portefeuille</h2>
          <p class="mb-0">Le nouvel assistant explique chaque etape, reduit les zones d'ombre et aide les nouvelles personnes a choisir la bonne voie sans perdre la puissance du multisig.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Synchronisation privee du portefeuille</h2>
          <p class="mb-0">Les nouveaux portefeuilles se synchronisent maintenant avec Compact Block Filters des le depart, afin que vous puissiez scanner la chaine en prive sans vous appuyer sur un indexeur Electrum tiers.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Signature centree sur l'appareil</h2>
          <p class="mb-0">Les flux de signature restent maintenant centres sur l'appareil devant vous, avec des etapes suivantes plus claires pour QR, USB, Bluetooth, les fichiers et la coordination multisig.</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## Un parcours guide vers l'autoconservation {#setup-flow}

L'experience du premier lancement a ete entierement reconstruite. Bitcoin-Safe reste concu pour une autoconservation serieuse, y compris le multisig appuye sur du materiel, et la version 2.0 offre maintenant aux nouvelles personnes un chemin guide a travers cette configuration. Le nouvel assistant explique ce qui se passe, ou vous en etes dans le flux et ce dont chaque signataire a besoin avant que vous passiez a l'etape suivante.

<p class="small text-muted">Pour les details d'implementation, voir la <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a>.</p>

Points forts de la refonte :

- Un nouvel ecran d'accueil qui aide les personnes qui debutent a choisir le bon point de depart
- Un flux de progression etape par etape pendant la creation du portefeuille
- Des ecrans de signature propres a chaque appareil avec des instructions ciblees et une aide contextuelle
- Des PDF de recuperation avec noms et icones des appareils pour que les sauvegardes restent sans ambiguite

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## Synchronisation privee et robuste de la chaine avec Compact Block Filters {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) alimentent desormais la synchronisation des nouveaux portefeuilles dans Bitcoin-Safe 2.0. Au lieu de demander a un serveur Electrum quelles adresses vous appartiennent, Bitcoin-Safe peut maintenant scanner la chaine de maniere privee en telechargeant des filtres compacts depuis des pairs Bitcoin Core aleatoires et en les verifiant localement.

<p class="small text-muted">Pour les details d'implementation, voir la <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a>.</p>


- La synchronisation du portefeuille reste privee des le premier lancement
- Aucune dependance a des serveurs Electrum tiers
- Electrum reste disponible pour les personnes qui le preferent
- [Synchronisation instantanee apres le scan initial du portefeuille]({{< ref "library/compact-block-filters" >}})
- [Notifications instantanees des transactions relayees]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## Un flux de signature centre sur l'appareil pour chaque appareil {#device-focused-signing}

La refonte remanie egalement le flux de signature apres la creation du portefeuille. Au lieu d'un ecran generique pour tous les signataires, Bitcoin-Safe centre maintenant les actions autour de l'appareil precis que vous utilisez.

<p class="small text-muted">Pour les details d'implementation, voir la <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a>.</p>

- Les actions QR, USB, Bluetooth, export/import de fichiers et Sync & Chat sont affichees directement sur la carte du signataire actif
- Les signataires restants, les appareils deja signes et l'action suivante necessaire restent visibles d'un coup d'oeil
- Les flux multisig melangeant plusieurs appareils restent lisibles parce que l'identite du signataire reste visible tout au long du PSBT
- Les transactions complexes avec un melange d'entrees single-sig et multisig sont gerees correctement, afin que chaque etape de signature soit claire

![Carte de signataire avec actions specifiques a l'appareil pour QR, USB, Bluetooth, export de fichier et Chat & Sync](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Architecture de plugins pour les flux de travail professionnels et les power users

Bitcoin-Safe 2.0 pose aussi les bases de futurs plugins supplementaires destines aux entreprises Bitcoin et aux utilisateurs avances. Gardez donc un oeil sur ce qui arrive :-)

<p class="small text-muted">Pour les details d'implementation, voir la <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a>.</p>

- Distribution des plugins via un depot externe de *sources*
- Chaque plugin est *signe avec GPG* par [andreasgriffin]({{< gpg_key_link >}}) pour garantir la securite, l'integrite et la distribution du plugin
- Le versionnement individuel des plugins et les mises a jour permettent un developpement plus rapide et independant

![Carte de signataire avec actions specifiques a l'appareil pour QR, USB, Bluetooth, export de fichier et Chat & Sync](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Prise en charge plus large des appareils et finitions {#hardware-support}

- Des QR codes animes **30%** plus rapides pour un scan plus rapide
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) est maintenant pris en charge via USB
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) prend maintenant en charge le **Bluetooth** en plus de l'USB et du QR
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) et [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) sont ajoutes a la liste des appareils pris en charge
- Voir la [liste complete des appareils pris en charge]({{< ref "library/supported-hardware-signers" >}})
- Ajout de verifications automatisees pour la [reproductibilite]({{< ref "library/reproducibility-and-security" >}})
- Voir ici la [liste complete](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0) des ameliorations


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## Les points forts existants sont toujours la

La version 2.0 n'est pas une remise a zero. Sous le nouveau flux d'onboarding et de signature, Bitcoin-Safe conserve les fonctionnalites qui le rendaient utile au quotidien : multisig collaboratif, sauvegardes PDF, historique de portefeuille consultable, visualisations des flux d'argent, synchronisation des labels, et plus encore.

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">Pret a essayer Bitcoin-Safe 2.0 ?</h2>
  <p class="mb-3">Telechargez la derniere version et decouvrez par vous-meme le nouvel onboarding, la synchronisation privee et les ameliorations des hardware wallets.</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Telecharger Bitcoin-Safe</a>
</div>


<br><br>

## Merci

Cette version repose sur beaucoup de travail de la part des contributrices et contributeurs, des testeurs et [des soutiens du projet]({{< ref "donate" >}}) :

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r)) pour la refonte de l'assistant, le travail d'interface des plugins et un soutien UI/UX **formidable et infatigable**
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) pour le client Compact Block Filter qui alimente maintenant la synchronisation privee des nouveaux portefeuilles
- L'[equipe Bitcoin Dev Kit](https://github.com/bitcoindevkit/) pour les bibliotheques au coeur de Bitcoin-Safe
- L'[equipe ndk](https://github.com/nostr-dev-kit/ndk) pour les bibliotheques qui alimentent les fonctionnalites nostr
- Toute la communaute Bitcoin-Safe qui a teste les versions candidates, signale des bugs, traduit des pages, envoye des sats et continue a faire avancer le projet
- [Traducteurs]({{< ref "donate/#translators" >}}), dont <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (Vietnamien)" title="qdyg-vn 🇻🇳 (Vietnamien)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (Allemand)" title="bsn21m 🇩🇪 (Allemand)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (Espagnol)" title="cyphra 🇪🇸 (Espagnol)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (Chinois)" title="DaGrindDontStop 🇨🇳 (Chinois)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


Si vous voulez aider a financer la prochaine version, vous pouvez aussi faire un don ici : {{< donation_btc >}}
