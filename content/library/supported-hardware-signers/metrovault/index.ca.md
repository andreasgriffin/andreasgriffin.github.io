---
aliases:
- /ca/knowledge/supported-hardware-signers/metrovault/
title: MetroVault
signer: metrovault
bucket: knowledge
---

MetroVault pot convertir un dispositiu Android antic en un dispositiu dedicat de signatura de Bitcoin fora de linia per a Bitcoin Safe. No l'instal·lis al teu telefon d'us diari. Restableix primer el dispositiu, mantingues-lo **SENSE CONNEXIO** i desconnectat d'internet, i fes-lo servir nomes com a signador.

## Que cal esperar

- Restableix un dispositiu Android antic abans de la instal·lacio i fes-lo servir nomes com a signador.
- No instal·lis altres aplicacions, no iniciis sessio en comptes, no hi posis una targeta SIM ni reconnectis el dispositiu a internet.
- Intercanvia dades del moneder, descriptors i PSBT amb Bitcoin Safe mitjancant codis QR.
- Registra descriptors multifirma i exporta dades del signador per a Bitcoin Safe.
- Verifica tots els detalls a la pantalla de MetroVault abans de signar.

## Restableix el dispositiu Android i fes-lo servir nomes com a signador fora de linia

La documentacio original de MetroVault ara te una [guia completa de configuracio del dispositiu](https://github.com/gorunjinian/MetroVault/blob/main/docs/DEVICE_SETUP.md). Recomanem fermament seguir-la pas a pas i tractar-la com un requisit: fes servir un telefon dedicat, restablert de fabrica i **SENSE CONNEXIO** que continu desconnectat d'internet despres de la configuracio i que s'utilitzi nomes per signar.

1. Restableix de fabrica el telefon abans de la instal·lacio.
2. Omet la configuracio del compte de Google i mantingues el dispositiu fora de linia.
3. Deixa el mode avio activat de manera permanent.
4. Desactiva el Wi-Fi, el Bluetooth, l'NFC i les dades mobils.
5. Treu la targeta SIM.
6. Desactiva la depuracio USB.
7. No instal·lis altres aplicacions ni facis servir el telefon per a res que no sigui signar.

Per a l'us en produccio, compila des del codi font sempre que sigui possible. Si no pots mantenir el dispositiu fora de linia i dedicat nomes a signar, no l'utilitzis per a fons de produccio amb MetroVault.
