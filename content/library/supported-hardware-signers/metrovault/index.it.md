---
aliases:
- /it/knowledge/supported-hardware-signers/metrovault/
title: MetroVault
signer: metrovault
bucket: knowledge
---

MetroVault puo trasformare un vecchio dispositivo Android in un dispositivo dedicato di firma Bitcoin offline per Bitcoin-Safe. Non installarlo sul tuo telefono di tutti i giorni. Ripristina prima il dispositivo, mantienilo **OFFLINE** e scollegato da internet, e usalo solo per firmare.

## Cosa aspettarsi

- Ripristina un vecchio dispositivo Android prima dell'installazione e usalo solo come firmatore.
- Non installare altre app, non accedere ad account, non inserire una SIM e non ricollegare il dispositivo a internet.
- Scambia dati del wallet, descrittori e PSBT con Bitcoin-Safe tramite codici QR.
- Registra i descrittori multisig ed esporta i dati del firmatore per Bitcoin-Safe.
- Verifica tutti i dettagli sullo schermo di MetroVault prima di firmare.

## Ripristina il dispositivo Android e usalo solo come firmatore offline

La documentazione upstream di MetroVault include ora una [guida completa alla configurazione del dispositivo](https://github.com/gorunjinian/MetroVault/blob/main/docs/DEVICE_SETUP.md). Consigliamo vivamente di seguirla passo dopo passo e di trattarla come un requisito: usa un telefono dedicato, ripristinato alle impostazioni di fabbrica e **OFFLINE** che rimanga scollegato da internet dopo la configurazione e venga usato solo per firmare.

1. Ripristina il telefono alle impostazioni di fabbrica prima dell'installazione.
2. Salta la configurazione dell'account Google e mantieni il dispositivo offline.
3. Lascia la modalita aereo attivata in modo permanente.
4. Disattiva Wi-Fi, Bluetooth, NFC e dati mobili.
5. Rimuovi la SIM.
6. Disattiva il debug USB.
7. Non installare altre app e non usare il telefono per altro oltre alla firma.

Per l'uso in produzione, compila dal codice sorgente quando possibile. Se non puoi mantenere il dispositivo offline e dedicato solo alla firma, non usarlo per fondi di produzione con MetroVault.
