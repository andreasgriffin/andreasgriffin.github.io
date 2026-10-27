---
aliases:
  - "/news/coldcard-insecure-seed/"
title: "COLDCARD Insecure Seed"
date: "2026-08-02"
draft: false
description: "Coinkite disclosed a critical weakness in seed generation on affected COLDCARD firmware. If you created a seed on any affected Coinkite device, migrate your funds to a new seed."
images: ["COLDCARD Security Advisory Notice - Migrate ASAP.png"]
previewimage: "COLDCARD Security Advisory Notice - Migrate ASAP.png"
---

## Summary

[Coinkite has disclosed a critical weakness in seed generation on affected COLDCARD firmware](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). [Block's technical analysis](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware) root-caused the issue to a predictable software random-number generator being used instead of the device's hardware RNG, and warns that **active exploitation is under way**. Updating the firmware does **not** repair an existing seed.

**If you created a seed with any affected Coinkite device, migrate your funds to a new seed.**

## Is my device affected?

Exposure depends on the **firmware version that was installed when the seed was generated** — not on when the device was manufactured.

| Device | Firmware used to generate the seed | Status |
|---|---|---|
| Mk1 | All released firmware | Not affected |
| Mk2 / Mk3 | v3.2.2 or earlier | Not affected (uses hardware RNG) |
| Mk2 / Mk3 | v4.0.0 – v4.1.9 | **Vulnerable** — no secure reseed |
| Mk4 | Production v5.0.0 onward | **Vulnerable** — limited to ~72 bits of entropy |
| Q | All production firmware | **Vulnerable** — limited to ~72 bits of entropy |
| Mk5 | All production firmware | **Vulnerable** — limited to ~72 bits of entropy |
| TAPSIGNER, OPENDIME, SATSCARD | — | Not affected (different codebase) |

Note that exporting an insecure seed and importing it into another wallet does **not** fix it — the seed itself remains affected.

## Install fixed firmware before generating a new seed

Fixed firmware is now available for every affected model and release track. Do not generate a new seed on a COLDCARD until it is installed.

| Device | Fixed firmware |
|---|---|
| Mk2 / Mk3 | 4.2.0 or later |
| Mk4 / Mk5 (standard) | 5.6.0 or later |
| Q (standard) | 1.5.0Q or later |
| Mk4 / Mk5 (Edge) | 6.6.0X or later |
| Q (Edge) | 6.6.0QX or later |

Standard and Edge are separate release tracks. If you use Edge, install the fixed Edge release for your model — do not assume an older Edge 6.x release is fixed simply because its version number is higher than the standard release.

## Do dice rolls or a passphrase protect me?

- **Dice rolls:** the bug affects the device-generated entropy only. If you entered at least **50 independent, private dice rolls** when creating the seed (99 or more for approximately 256 bits of entropy), the dice input alone contributed at least 128 bits of independent entropy and the seed is not considered at risk from this issue alone. Fewer than 50 rolls — or if you are unsure how many were entered or whether they were private — **migrate**.
- **BIP-39 passphrase:** a strong, unique BIP-39 passphrase (not the COLDCARD PIN) adds an independent barrier, but it does **not** repair the affected seed. If your passphrase is short, common, reused, or guessable — or you are unsure of its strength — treat the funds as at risk and migrate immediately. Even with a strong passphrase, migrate to a newly generated seed as soon as practical.

## Migration checklist

Migrate calmly and carefully. Rushing a wallet migration can create a more immediate risk than the issue you are trying to address.

1. **Install the fixed firmware** for your model before generating a replacement seed. If you prefer, generate the new seed on a **non-COLDCARD signing device** ([see supported devices]({{< ref "library/supported-hardware-signers" >}})) — either way, do **not** reuse the old seed.
2. Generate a completely new seed and **record it**. Before depositing any funds, verify the written backup, the wallet fingerprint, and a receive address.
3. Use Bitcoin-Safe's setup wizard to create a new [single-signature wallet]({{< ref "library/setup-singlesig-wallet" >}}) or [multisignature wallet]({{< ref "library/setup-multisig-wallet" >}}) with the new seed.
4. Complete the wizard's receive-and-send test: verify the backup and a receive address on the new signer, receive a small test amount, and successfully self-send it to another verified address in the new wallet.
5. Sign and broadcast the migration transaction:
   - **Single-signature wallet:** broadcast it normally with a high fee so it confirms quickly.
   - **Multisignature wallet:** do not broadcast it normally, because doing so reveals its public keys in the public mempool. Copy the signed raw transaction and submit it directly through [MARA Slipstream](https://slipstream.mara.com/).
6. Keep the old COLDCARD and its backup until the **full balance** has arrived and is confirmed in the new wallet. Only then erase the old seed.

If the Mk2/Mk3 is your only signing device, install firmware 4.2.0 or later first — it generates replacement seeds correctly, so you do not need a newer COLDCARD to complete the migration. Follow the same steps, carefully alternating between the old and new seed on the single device, and keep the old backup until the migration is confirmed complete.

## If you use multisignature

If a multisignature arrangement is composed **exclusively** of affected devices, the vulnerability still applies. Protect the arrangement with a quorum that includes at least one signing device that is not affected.

## Helping someone else migrate

Never ask them to share, photograph, or type their seed words. The seed must remain private and be entered only on the signing device itself.
