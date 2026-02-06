---
title: "Notificacions de transaccions instantànies"
description: "Com Bitcoin Safe rep notificacions instantànies de transaccions"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [
  "moneder Bitcoin segur per a famílies",
  "bitcoin",
  "estalvi en bitcoin",
  "signador de maquinari",
  "custodis de Bitcoin",
  "assessors financers",
  "moneder de bitcoin",
  "trezor",
  "bitcoin EUA",
  "BTC",
  "HODL",
  "Seguretat de Bitcoin",
  "Notificacions de transaccions instantànies"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---



![Bitcoin Safe logo](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }


### {{< page-title >}}  
 
  


**Bitcoin Safe** (a partir de la versió **1.5.0**) admet notificacions instantànies de transaccions entrants rellevants per a la teva cartera. Així és com funciona per dins:




##### 1. 📡 Escoltant la xarxa P2P de Bitcoin

Bitcoin Safe es connecta directament a un o més **nodes Bitcoin Core**, que participen a la xarxa global **peer-to-peer (P2P)**. Aquests nodes intercanvien contínuament noves transaccions difoses destinades a ser incloses al **mempool**.

Bitcoin Safe escolta passivament aquests missatges difosos i comprova si:

* alguna transacció implica **adreces** o **UTXOs** de la teva cartera.

✅ **Preservació de la privadesa**
Aquest mètode és **completament privat**. No **revela res** sobre la teva cartera al món exterior.
Bitcoin Safe es comporta com un node Bitcoin Core normal: només escolta el trànsit P2P públic — mai no anuncia ni sol·licita res específic de la teva cartera.



##### 2. 🧠 S'ha trobat una coincidència — Què passa a continuació?

Si es troba una transacció que coincideix, Bitcoin Safe reaccionarà de manera diferent segons el backend que estiguis utilitzant:

###### Opció A: ⚡ Backend Electrum o Esplora

* Bitcoin Safe **iniciarà una sincronització en segon pla** per obtenir la transacció completa i l'estat de la cartera des del servidor.

###### Opció B: 🔍 Filtres de blocs compactes (Mode Neutrino)

* La cartera **afegirà directament la transacció no confirmada** a les dades locals de la teva cartera — no cal cap consulta addicional.



#### ⚙️ Comportament d'activació/desactivació (opt-in/opt-out)

Per respectar les preferències d'usuari i la configuració de privadesa:

* 🔒 **Per als usuaris existents** que actualitzin a la versió 1.5.0 o posterior, aquesta funció **requereix activació (opt-in) per defecte** — la pots activar manualment a la configuració de xarxa.
* 🚀 **Per als nous usuaris**, aquesta funció està **activada (opt-out) per defecte**, ja que **preserva la privadesa** i és **molt útil** per fer el seguiment de l'activitat de la cartera en temps real.

Tu mantens el control total i pots activar o desactivar aquesta funció en qualsevol moment.
 
 

![Notification settings screenshot](config.png)
{ .img-fluid .mb-5 }


#### ⚠️ Només les transaccions confirmades són de confiança

Bitcoin Safe no pot validar que una transacció difosa sigui vàlida. Un atacant — especialment si controla tant el teu servidor Electrum com el node Bitcoin al qual estàs connectat — podria:

* Crear una transacció falsa que impliqui la teva adreça
* Difondre-la per provocar una notificació a la cartera
* Assegurar-se que mai no es confirma, perquè és **invàlida** o **entra en conflicte amb les regles de consens**


  


#### ✅ Resum

A partir de la versió **1.5.0**, Bitcoin Safe admet notificacions instantànies de transaccions mitjançant:

* Escoltar passivament la xarxa P2P de Bitcoin (com Bitcoin Core)
* Cercar transaccions que impliquin les **adreces** o **UTXOs** de la teva cartera
* Obtenció dels detalls complets via Electrum/Esplora o afegint-les directament amb filtres de blocs compactes
* Sense revelar cap dada de la cartera al món exterior