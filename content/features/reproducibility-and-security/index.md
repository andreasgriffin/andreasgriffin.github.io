---
aliases:
  - "/features/reproducibility/"
title: "Security and reproducibility"
description: "Bitcoin Safe follows a high standard for binary security: reproducible builds, signed commits, signed releases, and independent external monitoring."
draft: false
tags: ["Featured", "Features", "Security"]
images: ["logo.png"]
keywords: ["reproducible builds", "verify binaries", "signed commits", "signed releases", "appimage", "flatpak", "windows exe", "binary security"]
weight: 18
---

### {{< page-title >}}
{{< page-description >}}
<br>

![Reproducible build outputs for Bitcoin Safe](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 500px;" }


We implemented multiple ways to protect the integrity of the downloads on the website, so the app you download really matches the public source code:

- **Reproducible builds**: Linux `deb`, `AppImage`, and `Flatpak` builds, plus Windows  `portable exe` and `setup exe`, can be reproduced byte-for-byte. If a rebuilt file matches exactly, that is strong evidence that the binary was built from the same source code.
- **Signed repository history**: the [Bitcoin Safe GitHub repository](https://github.com/andreasgriffin/bitcoin-safe/commits/main) publishes verified signed commits, so reviewers can check who authored the code that went into a release.
- **Signed binaries**: release files are signed with the Bitcoin Safe [public PGP key]({{< gpg_key_link >}}), and Windows binaries also follow the [code signing policy]({{< ref "code-signing-policy" >}}).
- **Independent reproducibility checks**: [WalletScrutiny](https://walletscrutiny.com/desktop/bitcoin.safe/) tracks Bitcoin Safe independently and exposes reproducible-verification status for desktop releases.
- **Ongoing signature monitoring**: [BinaryWatch](https://binarywatch.org/) regularly checks Bitcoin Safe release files and whether their signatures still validate against the Bitcoin Safe [public PGP key]({{< gpg_key_link >}}).
- **Update verification**: Updates are shown in Bitcoin Safe, and it's signature is automatically verified.  

Taken together, these measures put Bitcoin Safe in a small group of projects that treat binary security as a first-class part of user safety, not an afterthought.





### Security is key consideration

Beyond binary integrity, Bitcoin Safe is built around secure defaults, good operational practices, and clear user guidance. A few examples:

- **Hardware-first custody**: Bitcoin Safe requires [hardware signers]({{< ref "knowledge/supported-hardware-signers" >}}), so seeds stay on dedicated devices instead of becoming hot secrets on a general-purpose computer.
- **Safer setup flow**: The setup wizard helps users create wallets that are actually ready for real use, including [hardware signer]({{< ref "knowledge/supported-hardware-signers" >}}) testing and [PDF recovery sheets]({{< ref "features/pdf-export/" >}}) for clear backups.
- **Receive-address verification**: Bitcoin Safe makes it easy to [verify receive addresses]({{< ref "knowledge/verify-receive-address/" >}}) on the signer itself before sharing them.
- **Address-poisoning detection**: It warns about suspicious [look-alike addresses]({{< ref "features/address-poisoning/" >}}).
- **Multisig security**: Bitcoin Safe supports multisignature wallets, so larger holdings can be protected by multiple devices or people instead of a single point of failure.
- **Collaboration that makes multisig easier**: Bitcoin Safe makes [multisignature collaboration]({{< ref "features/collaboration/" >}}) practical, so coordinating setup and signing is much easier in real-world use.
- **Clear signing flows**: Device-specific signing screens reduce confusion during PSBT review and help users take the right action on the right signer.
