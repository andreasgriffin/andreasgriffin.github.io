---
title: "なぜ Bitcoin Safe を選ぶのか？"
description: "デスクトップ向けのBitcoinウォレットはいくつもあります。Bitcoin Safeが際立つ理由をご覧ください。"
draft: false
tags: ["Featured","Features"]
images: ["logo.png"]
keywords: ["ビットコインセーフ", "ユニークな機能", "セキュアウォレット", "使いやすい"]
weight: 1000
---



## {{< page-title >}} 
<!-- {{< page-description >}}  -->

<br>
<!-- <br> -->

### ✔ 簡単にできる安全なBitcoin保管 
<!-- - ❌ 2-of-3 Multisignature is complex to use in other wallets -->
<!-- - 2-of-3 Multi-signature is a good choice  
    - Robust against loss or leak of 1 seed  -->
- {{<text-name-with-logo>}} の <a  href={{< ref "knowledge/setup-singlesig-wallet" >}} role="button">セットアップウィザード</a> は、非技術者でもシングル署名とマルチ署名を**簡単**に設定できます
    --> 各ステップに従うだけで安全なウォレットを設定できます。   
    <img  src="/images/multisig-steps.png" style="max-width: 600px; width: 100%;" alt="Multisig setup steps">
    - <a  href={{< ref "features/pdf-export" >}}   role="button"> <img  src="pdf-export.png" width="100" alt="PDF export">  PDF エクスポート</a> により、各シードとともに重要なウォレット記述子をバックアップできます。
    - 各ハードウェア署名機器に対してマルチ署名を登録する
    - 受取と支出のテストを含み、主要なハードウェア署名機がすべて動作することを確認します
<br>


<br>

#### ✔ ラベルの同期とバックアップ

{{<text-name-with-logo>}} は暗号化された <a href="https://nostr.com/ ">nostr</a> メッセージの力で自動的に
- <a  href="{{< ref "features/label-sync" >}}" role="button">コインカテゴリとラベルを同期</a> してコンピュータ間で共有
- コインカテゴリとラベルをバックアップ。必要なのは短いバックアップキーをバックアップすることだけです。
 

<br>

####  ✔ マルチパーティによるマルチシグ協力

3-of-5のマルチシグウォレットに参加しますか？

- ウォレット作成後、{{<text-name-with-logo>}} は協力用の暗号化された <a href="https://nostr.com/ ">nostr</a> グループチャットを作成し、署名のために PSBT を回し合えるようにします（<a  href="{{< ref "features/collaboration" >}}" role="button">PSBT の送信</a>）。
- もちろん <a  href="{{< ref "features/label-sync" >}}" role="button">ラベル同期</a> も機能します。
- セキュリティのため、各参加者はお互いを認証する（簡単なクリックで）必要があります。


<br>


#### ✔ コインカテゴリでアドレスを整理

 <img  src="coin-categories.png" width="150" alt="Coin categories"> 
 
- アドレスを **コインカテゴリ** にクラスタ化できます。各アドレスにラベルを付けるよりも簡単です。
- 作成する各 PSBT に対して一致するコインカテゴリを選択すると、{{<text-name-with-logo>}} はそのカテゴリからのみ入力（inputs）を選択します。   
- PSBT やトランザクションがコインカテゴリを混在させている場合、{{<text-name-with-logo>}} は警告します。


<br>


#### ✔ ミスの可能性を排除

過去に多くの高額なミスが発生しています。それらの多くは人がシードをコンピュータに入力してしまうことを避ければ防げます。{{<text-name-with-logo>}} はコンピュータ上でシードを使用することを防ぎ、ハードウェア署名機の使用を推奨します。

- {{<text-name-with-logo>}} は最も一般的なハードウェア署名機をフルサポートしています（例： <a href="https://store.coinkite.com/promo/8BFF877000C34A86F410">Coldcard</a>, 
            <a href="https://store.coinkite.com/promo/8BFF877000C34A86F410">Coldcard Q</a>, 
            <a href="https://shop.bitbox.swiss/?ref=MOB4dk7gpm">Bitbox02</a>, 
            <a href="https://store.blockstream.com/?code=XEocg5boS77D">Blockstream Jade</a>,    
            <a href="https://affil.trezor.io/SHtN">Trezor Safe</a>,
            <a href="https://foundation.xyz/passport">Foundation Passport</a>,
            <a href="https://keyst.one/?rfsn=8630473.c25550a&utm_source=refersion&utm_medium=affiliate&utm_campaign=8630473.c25550a">Keystone</a>,
            <a href="https://shop.ledger.com/?r=400f1fff75b5">Ledger</a>,
            <a href="https://clavastack.com/en/?coupon=bitcoin-safe">Specter DIY</a>)  
- 各ハードウェア署名機ごとにスクリーンショット付きの手順を含んでおり、すべてのステップを案内します 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-images "hardware-signer-screenshots" >}}
    </div>

   

<br>




#### ✔ 🔋 必要な機能は全部入り🔋 


{{<text-name-with-logo>}} は使いやすさを重視して設計されていますが、重要なパワーユーザ向け機能はすべて含まれています。
- お好みの electrum/esplora サーバー、mempool インスタンス、nostr リレーを選択可能
- あらゆる場所での CSV インポート＆エクスポート
- RBF、トランザクションのキャンセル、確定済み PSBT の編集
- さらにたくさん：<a href="https://github.com/andreasgriffin/bitcoin-safe?tab=readme-ov-file#comprehensive-feature-list">完全な機能一覧</a> をご覧ください


<br>