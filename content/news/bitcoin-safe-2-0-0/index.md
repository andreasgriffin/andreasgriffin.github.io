---
aliases:
  - "/news/bitcoin-safe-2-0-0/"
title: "Bitcoin-Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "Release notes for Bitcoin-Safe 2.0.0, featuring a rebuilt setup wizard, private Compact Block Filter sync, and expanded hardware wallet support."
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">Release announcement</p>
    <h2 class="display-6 mb-3">Bitcoin-Safe 2.0 - guided wallet setup, private chain sync, and device-focused signing</h2>
    <p class="lead mb-4">This release brings a rebuilt setup wizard, private chain sync with Compact Block Filters, and a signing flow organized around each hardware device. If you have been curious about cold storage but were unsure, this is the release to try.</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Download Bitcoin-Safe 2.0</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">See what is new</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Step-by-step wallet setup</h2>
          <p class="mb-0">The new wizard explains each step, reduces ambiguity, and helps new users choose the right path without losing the power of multisig.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Private wallet sync</h2>
          <p class="mb-0">New wallets now sync with Compact Block Filters out of the box, so you can scan the chain privately without leaning on a third-party Electrum indexer.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">Device-focused signing</h2>
          <p class="mb-0">Signing flows now stay centered on the device in front of you, with clearer next steps for QR, USB, Bluetooth, files, and multisig coordination.</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## A guided path into self-custody {#setup-flow}

The first-run experience has been rebuilt from the ground up. Bitcoin-Safe still aims at serious self-custody, including hardware-backed multisig, and 2.0 now gives new users a guided path through that setup. The new wizard explains what is happening, where you are in the flow, and what each signer needs from you before you move on.

<p class="small text-muted">For implementation details, see <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a>.</p>

Highlights from the redesign:

- A new welcome screen that helps first-time users pick the right starting point
- A step-by-step progress flow during wallet creation
- Device-specific signing screens with focused instructions and contextual help
- Recovery PDFs with device names and icons so backups stay unambiguous

{{< video src="sped-up wizard cropped.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## Private and robust chain sync with Compact Block Filters {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) now power wallet sync for new wallets in Bitcoin-Safe 2.0. Instead of asking an Electrum server which addresses belong to you, Bitcoin-Safe can now scan the chain privately by downloading compact filters from random Bitcoin Core peers and checking them locally.

<p class="small text-muted">For implementation details, see <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a>.</p>


- Wallet sync stays private from first launch
- No dependence on a third-party Electrum servers
- Electrum still remains available for users who prefer it
- [Instant sync after the initial wallet scan]({{< ref "library/compact-block-filters" >}})
- [Instant notifications of relayed transactions]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## A device-focused signing flow for every device {#device-focused-signing}

The redesign also reshapes the signing flow after wallet creation. Instead of one generic screen for every signer, Bitcoin-Safe now centers the actions around the specific device you are using.

<p class="small text-muted">For implementation details, see <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a>.</p>

- QR, USB, Bluetooth, file export/import, and Sync & Chat actions are shown directly on the active signer card
- Remaining signers, already signed devices, and the next required action stay visible at a glance
- Mixed-device multisig flows stay readable because signer identity remains visible throughout the PSBT
- Complex transactions with a mix of single-sig and multisig inputs are handled correctly, such that each signing step is clear

![Signer card with device-specific actions for QR, USB, Bluetooth, file export, and Chat & Sync](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Plugin architecture for business workflows and power users

Bitcoin-Safe 2.0 also lays the groundwork for future additional plugins targeted for Bitcoin buinesses and power-Bitcoiners. So keep an eye out for what is to come :-)

<p class="small text-muted">For implementation details, see <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a>.</p>

- Plugin distribution via an external *sources* repository
- Each plugin is *GPG signed* by [andreasgriffin]({{< gpg_key_link >}})  to ensure plugin security, integrity and delivery
- Individual plugin versioning, and updates allow faster and independent plugin development

![Signer card with device-specific actions for QR, USB, Bluetooth, file export, and Chat & Sync](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## Broader device support and polish {#hardware-support}

- **30%** faster animated QR codes for quicker scanning
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) via USB is now supported
- [Blockstream Jade/ Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) now supports **Bluetooth**, additional to USB and QR
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}})  and [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) added as supported devices
- See the [entire list of supported devices]({{< ref "library/supported-hardware-signers" >}})
- Added automated checks for [reproducibility]({{< ref "library/reproducibility-and-security" >}})
- See here the [full list](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0) of improvements


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## Existing strengths that are still here

The 2.0 release is not a reset. Under the new onboarding and signing flow, Bitcoin-Safe still carries the features that made it useful day to day: collaborative multisig, PDF backups, searchable wallet history, money-flow visualizations, label sync, and more.

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">Ready to try Bitcoin-Safe 2.0?</h2>
  <p class="mb-3">Download the latest release and explore the new onboarding, private sync, and hardware wallet improvements for yourself.</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Download Bitcoin-Safe</a>
</div>


<br><br>

## Thank you

This release stands on a lot of work from contributors, testers, and [supporters across the project]({{< ref "donate" >}}):

- **[@design-rrr](https://github.com/design-rrr)**  ([nostr](https://yakihonne.com/profile/nprofile1qqs905dzvnymh5gtr77qk2vp6yee2a0hmryd0sap3838dt8rd8clacgmv8ejx),  [X](https://x.com/deSign__r)) for the wizard redesign, plugin UI work, and **awesome and relentless** UI/UX support
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) for the Compact Block Filter client that now powers private wallet sync for new wallets
- The [Bitcoin Dev Kit team](https://github.com/bitcoindevkit/) ([nostr](https://yakihonne.com/profile/nprofile1qqs8sccnw8c4ns0xjen9mgdgks25d46k2kcssk60uxs635zmngxh5nsen4k6c)) for the libraries at the core of Bitcoin-Safe
- The [ndk team](https://github.com/nostr-dev-kit/ndk) ([nostr](https://yakihonne.com/profile/nprofile1qqsx3kq3vkgczq9hmfplc28h687py42yvms3zkyxh8nmkvn0vhkyyuspz9mhxue69uhkummnw3ezuamfdejj7qg4waehxw309aex2mrp0yhxgctdw4eju6t09uq32amnwvaz7tmwdaehgu3wdau8gu3wv3jhvtc8quffm)) for the libraries that power nostr functionality
- Everyone in the Bitcoin-Safe community who tested release candidates, reported bugs, translated pages, sent sats, and kept pushing the project forward
- [Translators]({{< ref "donate/#translators" >}}) including <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (Vietnamese)" title="qdyg-vn 🇻🇳 (Vietnamese)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (German)" title="bsn21m 🇩🇪 (German)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (Spanish)" title="cyphra 🇪🇸 (Spanish)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (Chinese)" title="DaGrindDontStop 🇨🇳 (Chinese)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/TamilNeram" target="_blank"><img src="https://unavatar.io/github/TamilNeram" alt="TamilNeram 🇮🇳 (Tamil)" title="TamilNeram 🇮🇳 (Tamil)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>




If you want to help fund the next release, you can also donate here: {{< donation_btc >}}
