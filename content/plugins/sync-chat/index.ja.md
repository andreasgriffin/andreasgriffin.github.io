---
title: "Sync & Chat"
description: "ウォレットの他の参加者を見つけ、ラベルとカテゴリを同期し、安全にチャットして、PSBT をワンクリックで共有します。"
draft: false
tags: ["Plugins", "sync-chat-mainpage"]
images: ["logo.png"]
weight: 30
faq:
  title: "Sync & Chat に関するよくある質問"
  items:
    - question: "デバイス同士はどのように見つけ合うのですか？"
      answer: "Sync & Chat は、同じウォレットのディスクリプターを使用している他のデバイスを探します。ディスクリプターは検索に使う前にハッシュ化されるため、平文のまま公開されることはありません。さらに、見つかった各デバイスは手動で追加し、信頼できるものとして設定する必要があります。そのため、ディスクリプターが秘密でなくても、チャットは安全に保たれます。"
    - question: "実際の共同作業はどのように進みますか？"
      answer: "1. セットアップ（初回のみ）: 各参加者のデバイスを追加し、信頼できるものとして設定します。\n2. 作成: 参加者の 1 人が PSBT を作成し、自分の署名を追加します。\n3. 共有: PSBT をすべての参加者、または選んだ参加者だけに送ります。\n4. 署名: 各参加者が署名を追加し、取引が完全に署名されるまで続けます。\n5. 送信: 最後の署名者が取引をブロードキャストすると、その取引が全参加者のウォレットに表示されます。"
    - question: "何が同期されますか？"
      answer: "Sync & Chat は次を同期します:\n- コインのカテゴリとラベル（署名者間で、異なる OS の間でも同期）\n- ワンクリックでの PSBT 共有"
    - question: "チャットは非公開ですか？"
      answer: "はい。ウォレットのチャットは暗号化され、Nostr を経由します。ラベルのバックアップも、Nostr を通じて暗号化された状態で保存されます。"
---

### {{< page-title >}}

<p class="lead">マルチシグの署名者を調整し、Bitcoin-Safe の中でウォレットの情報を同期したままにできます。</p>

<ul class="plugin-features">
<li>同じウォレットのディスクリプターを使用している他のデバイスを見つける</li>
<li>署名者間でラベルとカテゴリを同期する</li>
<li>安全にチャットし、PSBT をワンクリックで共有する</li>
</ul>

### ラベルの同期

{{< video src="../../library/label-sync/label-sync.mp4" controls="true" >}}

### 共同署名

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

マルチシグの共同署名の詳しい手順は、[マルチシグでの共同作業]({{< ref "library/collaboration/" >}})をご覧ください。

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">Bitcoin-Safe をダウンロード</h2>
<p class="text-muted mb-3">プラグインは Bitcoin-Safe に含まれています。アプリをダウンロードして試せます。</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">Bitcoin-Safe をダウンロード</a>
<small class="text-muted">無料・オープンソース · Windows, macOS, Linux</small>
</div>
</section>

### よくある質問

<details>
<summary>デバイス同士はどのように見つけ合うのですか？</summary>

Sync & Chat は、同じウォレットのディスクリプターを使用している他のデバイスを探します。ディスクリプターは検索に使う前にハッシュ化されるため、平文のまま公開されることはありません。さらに、見つかった各デバイスは手動で追加し、信頼できるものとして設定する必要があります。そのため、ディスクリプターが秘密でなくても、チャットは安全に保たれます。

</details>

<details>
<summary>実際の共同作業はどのように進みますか？</summary>

1. **セットアップ（初回のみ）:** 各参加者のデバイスを追加し、信頼できるものとして設定します。
2. **作成:** 参加者の 1 人が PSBT を作成し、自分の署名を追加します。
3. **共有:** PSBT をすべての参加者、または選んだ参加者だけに送ります。
4. **署名:** 各参加者が署名を追加し、取引が完全に署名されるまで続けます。
5. **送信:** 最後の署名者が取引をブロードキャストすると、その取引が全参加者のウォレットに表示されます。

</details>

<details>
<summary>何が同期されますか？</summary>

Sync & Chat は次を同期します:

- コインのカテゴリとラベル（署名者間で、異なる OS の間でも同期）
- ワンクリックでの PSBT 共有

</details>

<details>
<summary>チャットは非公開ですか？</summary>

はい。ウォレットのチャットは暗号化され、Nostr を経由します。ラベルのバックアップも、Nostr を通じて暗号化された状態で保存されます。

</details>

{{< sync-page-box >}}
</content>
