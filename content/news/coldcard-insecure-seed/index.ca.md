---
title: "Seed COLDCARD insegura"
date: "2026-08-02"
draft: false
description: "Coinkite ha revelat una debilitat crítica en la generació de seeds del firmware COLDCARD afectat. Si has creat una seed amb qualsevol dispositiu Coinkite afectat, trasllada els teus fons a una seed nova."
images: ["COLDCARD Security Advisory Notice - Migrate ASAP.png"]
---

## Resum

[Coinkite ha revelat una debilitat crítica en la generació de seeds del firmware COLDCARD afectat](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). [L'anàlisi tècnica de Block](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware) ha determinat que la causa és un generador de nombres aleatoris per programari previsible usat en lloc de l'RNG de maquinari del dispositiu, i adverteix que **hi ha una explotació activa en curs**. Actualitzar el firmware **no** repara una seed existent.

**Si has creat una seed amb qualsevol dispositiu Coinkite afectat, trasllada els teus fons a una seed nova.**

## El meu dispositiu està afectat?

L'exposició depèn de la **versió del firmware instal·lada quan es va generar la seed**, no de quan es va fabricar el dispositiu.

| Dispositiu | Firmware usat per generar la seed | Estat |
|---|---|---|
| Mk1 | Tot el firmware publicat | No afectat |
| Mk2 / Mk3 | v3.2.2 o anterior | No afectat (usa RNG de maquinari) |
| Mk2 / Mk3 | v4.0.0 – v4.1.9 | **Vulnerable** — sense reseed segur |
| Mk4 | Producció v5.0.0 en endavant | **Vulnerable** — limitat a ~72 bits d'entropia |
| Q | Tot el firmware de producció | **Vulnerable** — limitat a ~72 bits d'entropia |
| Mk5 | Tot el firmware de producció | **Vulnerable** — limitat a ~72 bits d'entropia |
| TAPSIGNER, OPENDIME, SATSCARD | — | No afectat (codi diferent) |

Tingues en compte que exportar una seed insegura i importar-la en un altre moneder **no** la corregeix: la seed en si continua afectada.

## Instal·la el firmware corregit abans de generar una seed nova

Ja hi ha firmware corregit disponible per a cada model i canal de llançament afectats. No generis una seed nova en una COLDCARD fins que no l'hagis instal·lat.

| Dispositiu | Firmware corregit |
|---|---|
| Mk2 / Mk3 | 4.2.0 o posterior |
| Mk4 / Mk5 (standard) | 5.6.0 o posterior |
| Q (standard) | 1.5.0Q o posterior |
| Mk4 / Mk5 (Edge) | 6.6.0X o posterior |
| Q (Edge) | 6.6.0QX o posterior |

Standard i Edge són canals de llançament separats. Si fas servir Edge, instal·la la versió Edge corregida per al teu model: no donis per fet que una versió antiga d'Edge 6.x està corregida només perquè el seu número sigui més alt que el de la versió standard.

## Els llançaments de daus o una frase de contrasenya em protegeixen?

- **Llançaments de daus:** el defecte només afecta l'entropia generada pel dispositiu. Si has introduït almenys **50 llançaments de daus independents i privats** en crear la seed (99 o més per a aproximadament 256 bits d'entropia), la introducció de daus per si sola ha aportat almenys 128 bits d'entropia independent i no es considera que la seed corri risc per aquest sol problema. Amb menys de 50 llançaments — o si no estàs segur de quants se'n van introduir o de si eren privats — **migra**.
- **Frase de contrasenya BIP-39:** una frase de contrasenya BIP-39 forta i única (no el PIN de COLDCARD) afegeix una barrera independent, però **no** repara la seed afectada. Si la teva frase de contrasenya és curta, comuna, reutilitzada o endevinable — o no estàs segur de la seva fortalesa — tracta els fons com a en risc i migra immediatament. Fins i tot amb una frase de contrasenya forta, migra cap a una seed acabada de generar tan aviat com sigui possible.

## Llista de verificació per a la migració

Migra amb calma i cura. Afanyar una migració de moneder pot crear un risc més immediat que el problema que intentes resoldre.

1. **Instal·la el firmware corregit** del teu model abans de generar una seed de recanvi. Si ho prefereixes, genera la seed nova en un **dispositiu de signatura que no sigui COLDCARD** ([consulta els dispositius compatibles]({{< ref "library/supported-hardware-signers" >}})) — en qualsevol cas, **no** reutilitzis la seed antiga.
2. Genera una seed completament nova i **registra-la**. Abans de dipositar fons, verifica la còpia de seguretat escrita, l'empremta del moneder i una adreça de recepció.
3. Fes servir l'assistent de configuració de Bitcoin-Safe per crear un nou [moneder de signatura única]({{< ref "library/setup-singlesig-wallet" >}}) o [moneder de multisignatura]({{< ref "library/setup-multisig-wallet" >}}) amb la seed nova.
4. Completa la prova de recepció i enviament de l'assistent: verifica la còpia de seguretat i una adreça de recepció en el nou signant, rep una petita quantitat de prova i envia-te-la amb èxit a una altra adreça verificada del moneder nou.
5. Signa i transmet la transacció de migració:
   - **Moneder de signatura única:** transmet-lo normalment amb una comissió alta perquè es confirmi ràpidament.
   - **Moneder de multisignatura:** no el transmetis normalment, perquè això revela les seves claus públiques al mempool públic. Copia la transacció en brut signada i envia-la directament mitjançant [MARA Slipstream](https://slipstream.mara.com/).
6. Conserva la COLDCARD antiga i la seva còpia de seguretat fins que el **saldo complet** hagi arribat i s'hagi confirmat al moneder nou. Només aleshores esborra la seed antiga.

Si la Mk2/Mk3 és el teu únic dispositiu de signatura, instal·la primer el firmware 4.2.0 o posterior: genera correctament les seeds de recanvi, així que no necessites una COLDCARD més nova per completar la migració. Segueix els mateixos passos, alternant amb cura entre la seed antiga i la nova en l'únic dispositiu, i conserva la còpia de seguretat antiga fins que la migració estigui completament confirmada.

## Si fas servir la multisignatura

Si una configuració de multisignatura està composta **exclusivament** per dispositius afectats, la vulnerabilitat continua aplicant-se. Protegeix la configuració amb un quòrum que inclogui almenys un dispositiu de signatura no afectat.

## Si ajudes algú altre a migrar

No li demanis mai que comparteixi, fotografiï o escrigui les seves paraules seed. La seed ha de romandre privada i només s'ha d'introduir en el propi dispositiu de signatura.
