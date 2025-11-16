---
title: "Filtres compactes de blocs"
description: "Entén què són els filtres compactes de blocs i com milloren la privadesa respecte als servidors Electrum."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "filtres compactes de blocs"
  - "CBF"
  - "privadesa"
  - "cartera Bitcoin"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}


Bitcoin Safe   1.6.0 introdueix **filtres compactes de blocs (CBF)** com una forma opcional de sincronitzar la teva cartera. En lloc de sol·licitar a un servidor Electrum centralitzat l'historial de la teva cartera, Bitcoin Safe ara pot descarregar un petit fitxer resum per a cada bloc directament de peers aleatoris de Bitcoin Core. Aquests resums actuen com una llista de comprovació curta que permet a la teva cartera decidir per si mateixa si un bloc podria contenir alguna de les teves transaccions.

Com que Bitcoin Safe pren la decisió localment, cap servidor de tercers mai no arriba a saber quines adreces o transaccions t'importen. Obtens les mateixes dades de confirmació que un node complet conservaria, però en un format més lleuger que s'adapta a dispositius d'ús quotidià.

**Per què és millor:**

- 📦 **Descarregues petites:** Cada filtre ocupa només uns quants quilobytes, així que pots sincronitzar-te a través de connexions domèstiques normals sense emmagatzemar tota la cadena de blocs.
- 🔐 **Directament des de la xarxa:** Bitcoin Safe parla amb diversos nodes Bitcoin Core aleatoris, igual que fan altres nodes, reduint la possibilitat que un observador individual et pugui perfilar.
- 🕵️ **Comprovació local:** La teva cartera comprova els filtres localment. Si un filtre sembla rellevant, només en aquest cas descarrega el bloc concret, mantenint les teves adreces privades.

Els servidors Electrum, en canvi, cerquen la cadena de blocs en el teu nom. Cada sol·licitud comparteix les adreces de la teva cartera amb l'operador del servidor, que podria registrar aquesta informació. Amb els filtres compactes de blocs, Bitcoin Safe descarrega les mateixes dades neutrals que comparteix cada node. Ningú no pot saber quines adreces són teves perquè la teva cartera mai no les revela en primer lloc.

A continuació hi ha una vista simplificada de com es connecta Bitcoin Safe quan CBF està activat. Observa com reflecteix la manera en què els nodes de Bitcoin Core ja es comuniquen entre ells:


![Bitcoin Safe descarrega filtres compactes de blocs de diversos peers aleatoris de Bitcoin Core.](logo.jpg)
{ .img-fluid .mb-5   style="max-width: 450px;" }


Pots triar amb quants peers ha de connectar-se Bitcoin Safe. Més peers requereixen més amplada de banda i fan que la sincronització sigui més lenta. El valor per defecte és 2.

 
### Què pots esperar durant la sincronització

CBF modifica el temps d'espera segons el que estiguis fent:

1. ✨ **Crear o recuperar una cartera:** Ja sigui que creïs una nova cartera o recuperis una existent, la sincronització inicial descarrega els filtres per a tot l'historial de la teva cartera. Espera que aquest procés d'una sola vegada trigui **entre 5 i 30 minuts**, depenent de la velocitat d'Internet.
2. 🚀 **Obrir una cartera que ja estava sincronitzada:** Bitcoin Safe només necessita obtenir els filtres més nous des de la teva última sessió. Aquesta actualització normalment finalitza en **menys de 30 segons**.
3. 🔄 **Canviar de servidors Electrum a CBF:** Com que la cartera estava prèviament sincronitzada amb servidors Electrum, Bitcoin Safe només necessita obtenir els filtres més nous, cosa que normalment serà **menys de 30 segons**.

### Mantingues-te informat sobre pagaments no confirmats

Els filtres compactes de blocs cobreixen només els **blocs confirmats**. Per rebre avisos sobre transaccions entrants abans que es confirmin, assegura't també d'habilitar [Notificacions instantànies de transaccions]({{< ref "knowledge/instant-transactions-notifications/" >}}). Aquesta funció escolta els missatges en viu peer-to-peer d'un node Bitcoin aleatori perquè puguis reaccionar a l'activitat de la mempool sense renunciar a la privadesa.


<br>
<br>



### Detalls tècnics


- *Per a desenvolupadors que vulguin aprofundir:* els filtres compactes de blocs segueixen l'[especificació BIP158](https://bips.dev/158/) i s'expliquen a la [visió general d'Elle Mouton sobre conjunts codificats amb Golomb](https://ellemouton.com/posts/bip158/). La implementació de Bitcoin Safe es basa en el mòdul de filtres compactes de blocs de codi obert [Kyoto compact block filter module for BDK](https://github.com/rustaceanrob/kyoto).
- Pots afegir el teu propi node Bitcoin Core als peers per sincronitzar els filtres compactes de blocs, triant el _Node inicial_ de la _Supervisió de la xarxa Bitcoin_.


![](inital-node.png)
{ .img-fluid .mb-5   style="max-width: 414px;" }