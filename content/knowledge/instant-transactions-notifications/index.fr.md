---
title: "Notifications instantanées de transactions"
description: "Comment Bitcoin Safe reçoit les notifications instantanées de transactions"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [
  "portefeuille Bitcoin sécurisé pour les familles",
  "bitcoin",
  "épargne en Bitcoin",
  "signataire matériel",
  "Gardiens Bitcoin",
  "Conseillers financiers",
  "portefeuille bitcoin",
  "trezor",
  "bitcoin États-Unis",
  "BTC",
  "HODL",
  "Sécurité Bitcoin",
  "Notifications instantanées de transactions"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---



![](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }


### {{< page-title >}}  
 
  


**Bitcoin Safe** (à partir de la version **1.5.0**) prend en charge les notifications instantanées des transactions Bitcoin entrantes pertinentes pour votre portefeuille. Voici comment cela fonctionne en coulisses :




##### 1. 📡 Écoute du réseau P2P Bitcoin

Bitcoin Safe se connecte directement à un ou plusieurs **nœuds Bitcoin Core**, qui participent au réseau global **peer-to-peer (P2P)**. Ces nœuds échangent en continu les transactions nouvellement diffusées destinées à être incluses dans le **mempool**.

Bitcoin Safe écoute passivement ces messages diffusés et vérifie si :

* une transaction implique des **adresses** ou des **UTXO** de votre portefeuille.

✅ **Respect de la vie privée**
Cette méthode est **complètement privée**. Elle ne **révèle rien** de votre portefeuille au monde extérieur.
Bitcoin Safe se comporte comme un nœud Bitcoin Core classique : il n’écoute que le trafic P2P public — sans jamais annoncer ni demander quoi que ce soit de spécifique à votre portefeuille.



##### 2. 🧠 Correspondance trouvée — Que se passe-t-il ensuite ?

Si une transaction correspondante est trouvée, Bitcoin Safe réagira différemment selon le backend que vous utilisez :

###### Option A: ⚡ Backend Electrum ou Esplora

* Bitcoin Safe déclenchera une **synchronisation en arrière-plan** pour récupérer la transaction complète et l’état du portefeuille depuis le serveur.

###### Option B: 🔍 Filtres de blocs compacts (mode Neutrino)

* Le portefeuille **ajoutera directement la transaction non confirmée** aux données locales du portefeuille — aucune recherche supplémentaire nécessaire.



#### ⚙️ Comportement d'activation / de désactivation

Pour respecter les préférences et les paramètres de confidentialité des utilisateurs :

* 🔒 **Pour les utilisateurs existants** effectuant la mise à jour vers la version 1.5.0 ou ultérieure, cette fonctionnalité est **activée par option (opt-in)** — vous pouvez l'activer manuellement dans les paramètres réseau.
* 🚀 **Pour les nouveaux utilisateurs**, cette fonctionnalité est **activée par défaut (opt-out possible)**, car elle est à la fois **respectueuse de la vie privée** et **très utile** pour suivre l'activité du portefeuille en temps réel.

Vous gardez le contrôle total et pouvez activer ou désactiver cette fonctionnalité à tout moment.
 
 


#### ⚠️ Seules les transactions confirmées peuvent être considérées comme fiables

Bitcoin Safe ne peut pas garantir qu'une transaction diffusée soit valide. Un attaquant — en particulier s'il contrôle à la fois votre serveur Electrum et le nœud Bitcoin auquel vous êtes connecté — pourrait :

* Créer une fausse transaction impliquant votre adresse
* La diffuser pour déclencher une notification dans le portefeuille
* S'assurer qu'elle ne soit jamais confirmée, car elle est **invalide** ou **en conflit avec les règles de consensus**


  


#### ✅ Résumé

À partir de la version **1.5.0**, Bitcoin Safe prend en charge les notifications instantanées de transactions en :

* Écoutant passivement le réseau P2P Bitcoin (comme Bitcoin Core)
* Identifiant les transactions impliquant les **adresses** ou **UTXO** de votre portefeuille
* Récupérant les détails complets via Electrum/Esplora ou en ajoutant directement via les filtres de blocs compacts
* Ne révélant jamais aucune donnée du portefeuille au monde extérieur