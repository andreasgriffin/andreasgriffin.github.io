---
title: "Signateurs matériels requis"
description: "Bitcoin Safe n'autorise que les seeds matériels sur le Mainnet pour maximiser la sécurité et éviter les risques liés au stockage de clés par logiciel. Voici pourquoi cela compte."
draft: false
tags: ["Featured", "Knowledge" ]
keywords: [
  "Bitcoin Safe",
  "portefeuille matériel",
  "seed logiciel",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "multisignature",
  "PSBT",
  "auto-garde",
  "sécurité Bitcoin",
  "empoisonnement d'adresse",
  "outils Bitcoin"
]
images: ["logo.png" ]
# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=dbSmQmt0uDI"
weight: 21
---

 

![Bitcoin Safe logo](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }

## 🚫 Pourquoi Bitcoin Safe bloque-t-il les seeds logiciels sur le Mainnet ?

🤔 N'est-ce pas gênant ?

🔥 En réalité — c'est une **amélioration majeure de sécurité**.

Bitcoin Safe **n'autorise les seeds logiciels que sur Testnet, Signet et Regtest** — jamais sur le Mainnet. Voici pourquoi :

### ✅ Raisons pour lesquelles les seeds logiciels sont bloqués sur le Mainnet

- 🧠 **Les seeds logiciels sont peu sécurisés** 
  - Les ordinateurs regorgent de risques : voleurs de presse-papiers, logiciels malveillants, failles de navigateur.
  - Une seule erreur, et votre seed est compromis — c'est la perte des fonds.
  - Le stockage à froid ne doit jamais être initialisé sur un appareil chaud.

</br>

- 🧊 **Le stockage à froid doit naître froid**
  - Les utilisateurs génèrent souvent des seeds dans des portefeuilles logiciels puis migrent vers du matériel.
  - Mais l'exposition initiale a déjà eu lieu — il n'y a pas de retour en arrière.
  - Véritable stockage à froid = créé sur un signateur matériel dès le départ.

</br>

- 🎣 **Le phishing prospère grâce aux habitudes logicielles**
  - Saisir des seeds dans des applications vous habitue à faire confiance à de mauvaises pratiques UX.
  - L'obligation du matériel force de meilleures habitudes et réduit l'exposition.
  - ✅ Mainnet sans seed logiciel = moins de victimes de phishing.

</br>

- 🧪 **Les développeurs gardent de la flexibilité**
  - Les seeds logiciels *sont* autorisés sur :
    - Testnet
    - Signet
    - Regtest
  - Idéal pour les développeurs. Aucun risque pour des sats réels. 🧡



</br>


- 🔐 **Le Mainnet exige des signateurs matériels — aucune exception**
  - 🔌 USB, 📷 QR, et 💾 carte SD avec tous les principaux appareils
    - [Coldcard]({{< ref "knowledge/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Foundation Passport]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Ledger]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Keystone]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "knowledge/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "knowledge/supported-hardware-signers" >}})
  - [Voir tous les signateurs pris en charge →]({{< ref "knowledge/supported-hardware-signers" >}})


---

## 🛡️ Protection contre l'empoisonnement d'adresses

Bitcoin Safe **code les adresses de réception par couleur** pour rendre l'empoisonnement d'adresses évident :

- 🟢 Vert = adresse de réception vérifiée  
- 🟡 Jaune = adresse de change  

Si quelqu'un tente d'empoisonner votre presse-papiers avec une fausse adresse, vous le verrez instantanément.

![Exemple de détection d'empoisonnement d'adresse](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ Vérification d'adresses via USB ou QR

Vérifiez les adresses de réception directement sur votre signateur matériel — pas besoin de faire confiance à l'écran.

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ Instructions pour chaque signateur matériel
 
- {{<text-name-with-logo>}} inclut des captures d'écran et des instructions pour chaque signateur matériel afin de vous guider à chaque étape 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-images >}}
    </div>

   
---



## 🤝 Multisig collaboratif simplifié

Bitcoin Safe rend le multisig convivial et prêt pour le travail en équipe :

- 🔐 Chat Nostr chiffré  
- 🔁 Partage de PSBT en 1 clic  
- 🔌 USB, 📷 QR, et 💾 carte SD

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ Fonctionnalités puissantes pour tous les utilisateurs

- 🟧 Assistant de portefeuille singlesig  
- 🟨 Configuration multisig 2-sur-3  
- 🟩 Toute configuration n-sur-m  
- 🖨️ Feuilles de sauvegarde PDF imprimables  
- 🔁 Synchronisation des étiquettes via Nostr  
- 🔍 Diagramme complet des flux d'argent & historique des transactions consultable

![Diagramme des transactions dans Bitcoin Safe](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 International et convivial

- Support multilingue : {{< flags-short >}}
- Fonctionne sur : Windows, macOS & Linux  
- Glisser-déposer PSBT / CSV  
- Filtres avancés pour les transactions, UTXO, montants, et plus

---

## 💡 En bref

Bitcoin Safe = Vraies économies en Bitcoin :

✅ Matériel uniquement sur le Mainnet  
✅ Aucune exposition de seed logiciel  
✅ Multisig adapté aux débutants  
✅ Environnements de test adaptés aux développeurs  
✅ Fonctionnalités prêtes pour la famille et les équipes  

🔗 [Bitcoin-Safe.org]({{< ref "/" >}})  
🎥 Chaîne YouTube →: https://youtube.com/@BitcoinSafeOrg