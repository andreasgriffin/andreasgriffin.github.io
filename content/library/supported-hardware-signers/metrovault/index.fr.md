---
aliases:
- /fr/knowledge/supported-hardware-signers/metrovault/
title: MetroVault
signer: metrovault
bucket: knowledge
---

MetroVault peut transformer un ancien appareil Android en dispositif dedie de signature Bitcoin hors ligne pour Bitcoin-Safe. Ne l'installez pas sur votre telephone de tous les jours. Reinitialisez d'abord l'appareil, gardez-le **HORS LIGNE** et deconnecte d'internet, et utilisez-le uniquement pour signer.

## A quoi s'attendre

- Reinitialisez un ancien appareil Android avant l'installation et utilisez-le uniquement comme appareil de signature.
- N'installez pas d'autres applications, ne vous connectez a aucun compte, n'inserez pas de carte SIM et ne reconnectez pas l'appareil a internet.
- Echangez les donnees du portefeuille, les descripteurs et les PSBT avec Bitcoin-Safe a l'aide de codes QR.
- Enregistrez les descripteurs multisig et exportez les donnees du signataire pour Bitcoin-Safe.
- Verifiez tous les details sur l'ecran de MetroVault avant de signer.

## Reinitialisez l'appareil Android et utilisez-le uniquement comme signataire hors ligne

La documentation amont de MetroVault contient maintenant un [guide complet de configuration de l'appareil](https://github.com/gorunjinian/MetroVault/blob/main/docs/DEVICE_SETUP.md). Nous recommandons fortement de le suivre etape par etape et de le traiter comme une exigence : utilisez un telephone dedie, reinitialise en usine et **HORS LIGNE** qui reste deconnecte d'internet apres la configuration et qui sert uniquement a signer.

1. Reinitialisez le telephone aux parametres d'usine avant l'installation.
2. Ignorez la configuration du compte Google et gardez l'appareil hors ligne.
3. Laissez le mode avion active en permanence.
4. Desactivez le Wi-Fi, le Bluetooth, le NFC et les donnees mobiles.
5. Retirez la carte SIM.
6. Desactivez le debogage USB.
7. N'installez pas d'autres applications et n'utilisez le telephone pour rien d'autre que signer.

Pour un usage en production, construisez depuis le code source si possible. Si vous ne pouvez pas garder l'appareil hors ligne et reserve uniquement a la signature, ne l'utilisez pas pour des fonds de production MetroVault.
