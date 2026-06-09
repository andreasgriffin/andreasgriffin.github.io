---
title: "Seguretat i reproductibilitat"
description: "Bitcoin Safe segueix un estàndard alt de seguretat binària: builds reproduïbles, commits signats, versions signades i monitoratge extern independent."
draft: false
tags: ["Featured", "Features", "Security"]
images: ["logo.png"]
keywords: ["reproducible builds", "verify binaries", "signed commits", "signed releases", "appimage", "flatpak", "windows exe", "binary security"]
weight: 18
---

### {{< page-title >}}
{{< page-description >}}
<br>

![Resultats de builds reproduïbles per a Bitcoin Safe](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 500px;" }

Hem implementat diverses capes de protecció per a la integritat de les descàrregues del lloc web, perquè l'aplicació que descarregues coincideixi realment amb el codi font públic:

- **Builds reproduïbles**: Els builds Linux `deb`, `AppImage` i `Flatpak`, així com els fitxers Windows `portable exe` i `setup exe`, es poden reproduir byte per byte. Si un fitxer reconstruït coincideix exactament, això és una prova forta que el binari s'ha construït a partir del mateix codi font.
- **Historial del repositori signat**: El [repositori de Bitcoin Safe a GitHub](https://github.com/andreasgriffin/bitcoin-safe/commits/main) publica commits signats i verificats, perquè els revisors puguin comprovar qui va crear el codi que ha entrat en una versió.
- **Binàries signades**: Els fitxers de les versions es signen amb la [clau pública PGP]({{< gpg_key_link >}}) de Bitcoin Safe, i les binàries de Windows també segueixen la [política de signatura de codi]({{< ref "code-signing-policy" >}}).
- **Comprovacions independents de reproductibilitat**: [WalletScrutiny](https://walletscrutiny.com/desktop/bitcoin.safe/) segueix Bitcoin Safe de manera independent i mostra l'estat de verificació reproduïble de les versions d'escriptori.
- **Monitoratge continu de signatures**: [BinaryWatch](https://binarywatch.org/) comprova regularment els fitxers de les versions de Bitcoin Safe i si les seves signatures continuen sent vàlides contra la [clau pública PGP]({{< gpg_key_link >}}) de Bitcoin Safe.
- **Verificació d'actualitzacions**: Les actualitzacions es mostren a Bitcoin Safe i la seva signatura es verifica automàticament.

En conjunt, aquestes mesures situen Bitcoin Safe dins d'un grup petit de projectes que tracten la seguretat binària com una part essencial de la seguretat de l'usuari, i no com un detall afegit a posteriori.

### La seguretat és el criteri principal en cada aspecte de Bitcoin Safe

Més enllà de la integritat binària, Bitcoin Safe està construït al voltant de configuracions segures per defecte, bones pràctiques operatives i una guia clara per a l'usuari. Alguns exemples:

- **Custòdia centrada en maquinari**: Bitcoin Safe requereix [signadors de maquinari]({{< ref "knowledge/supported-hardware-signers" >}}), de manera que les llavors romanguin en dispositius dedicats en lloc de convertir-se en secrets calents en un ordinador generalista.
- **Flux de configuració més segur**: L'assistent de configuració ajuda a crear wallets realment preparades per a l'ús real, incloent proves de [signadors de maquinari]({{< ref "knowledge/supported-hardware-signers" >}}), [fulls PDF de còpia de seguretat]({{< ref "features/pdf-export/" >}}) i orientacions sobre com guardar els dispositius i les còpies de seguretat de les llavors.
- **Verificació de les adreces de recepció**: Bitcoin Safe facilita [verificar les adreces de recepció]({{< ref "knowledge/verify-receive-address/" >}}) en el mateix signador abans de compartir-les.
- **Detecció d'address poisoning**: Avisa sobre [adreces sospitoses i semblants]({{< ref "features/address-poisoning/" >}}).
- **Seguretat multisig**: Bitcoin Safe admet wallets multisig, de manera que quantitats més grans poden quedar protegides per diversos dispositius o persones en lloc d'un únic punt de fallada.
- **Col·laboració que fa el multisig més fàcil**: Bitcoin Safe fa pràctica la [col·laboració multisig]({{< ref "features/collaboration/" >}}), de manera que coordinar la configuració i la signatura és molt més senzill en l'ús real.
- **Fluxos de signatura clars**: Les pantalles de signatura específiques per dispositiu redueixen la confusió durant la revisió de PSBT i ajuden els usuaris a fer l'acció correcta en el signador correcte.
