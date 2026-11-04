---
aliases:
  - "/news/coldcard-insecure-seed/"
title: "COLDCARD Insecure Seed"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "Minimal guidance for moving funds away from a seed generated on a Coinkite device."
---

[Coinkite has disclosed a weakness in seed generation on affected COLDCARD firmware](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). See also [Block's technical analysis of the predictable RNG fallback and 32-bit reseed](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware). Updating the firmware does not repair an existing seed.

**If you created a seed with any Coinkite product, migrate SOON!**

## Migration checklist

1. Generate a completely new seed on a **non-COLDCARD signing device** ([see supported devices]({{< ref "library/supported-hardware-signers" >}})). Do not reuse the old seed. Then use that signer with Bitcoin-Safe's setup wizard to create either a new [single-signature wallet]({{< ref "library/setup-singlesig-wallet" >}}) or [multisignature wallet]({{< ref "library/setup-multisig-wallet" >}}).
   - If no non-COLDCARD hardware signer is available, [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}}) is an option on a dedicated, factory-reset Android device that is kept offline and used only for signing.
   - Complete the wizard's receive-and-send test to ensure the new wallet is set up correctly: verify its backup and a receive address on the new signer, receive a small test amount, and successfully self-send it to another verified address in the new wallet.
2. Sign the migration transaction:
   - **If the affected wallet is single-signature:** broadcast it normally with a high fee so it confirms quickly.
   - **If the affected wallet is multisignature:** do not broadcast it normally, because doing so reveals its public keys in the public mempool. Copy the signed raw transaction and submit it directly through [MARA Slipstream](https://slipstream.mara.com/).
3. Keep the old COLDCARD until the full balance has arrived and confirmed in the new wallet, then upgrade it to the latest firmware.

If you are helping someone migrate, never ask them to share, photograph, or type their seed words. The seed should remain private and be entered only on the signing device.
