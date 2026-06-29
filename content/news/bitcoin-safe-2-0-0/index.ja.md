---
title: "Bitcoin Safe 2.0.0"
date: "2026-06-09"
draft: false
description: "Bitcoin Safe 2.0.0 のリリースノート。再構築されたセットアップウィザード、Compact Block Filters によるプライベート同期、そして拡張されたハードウェアウォレット対応を含みます。"
images: ["wizard single sig.png"]
previewimage: "wizard single sig.png"
---

<div class="card border-0 shadow-none my-4">
  <div class="card-body p-4 p-lg-5 text-start">
    <p class="text-uppercase text-muted fw-semibold mb-2">リリースのお知らせ</p>
    <h2 class="display-6 mb-3">Bitcoin Safe 2.0 - ガイド付きウォレット設定、プライベートなチェーン同期、デバイス中心の署名フロー</h2>
    <p class="lead mb-4">このリリースでは、再構築されたセットアップウィザード、Compact Block Filters を使ったプライベートなチェーン同期、そして各ハードウェアデバイスを中心に整理された署名フローが加わりました。cold storage に興味はあるものの不安があった方にこそ試してほしいリリースです。</p>
    <div class="d-flex justify-content-start gap-3 flex-wrap">
      <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Bitcoin Safe 2.0 をダウンロード</a>
      <a class="btn btn-outline-primary btn-lg px-4" href="#setup-flow" role="button">新機能を見る</a>
    </div>
  </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4 my-4">
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#setup-flow">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">ステップごとのウォレット設定</h2>
          <p class="mb-0">新しいウィザードは各ステップを説明し、あいまいさを減らし、multisig の強みを失わずに初めてのユーザーが正しい道を選べるようにします。</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#private-sync-default">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">プライベートなウォレット同期</h2>
          <p class="mb-0">新しいウォレットは最初から Compact Block Filters で同期されるため、サードパーティの Electrum indexer に頼らず、プライベートにチェーンをスキャンできます。</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a class="text-decoration-none text-reset d-block h-100" href="#device-focused-signing">
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5">デバイス中心の署名</h2>
          <p class="mb-0">署名フローは目の前のデバイスを中心に進むようになり、QR、USB、Bluetooth、ファイル、multisig の調整について次に何をすべきかがより分かりやすくなりました。</p>
        </div>
      </div>
    </a>
  </div>
</div>

<br><br>
## self-custody へのガイド付きの道 {#setup-flow}

初回起動時の体験は一から作り直されました。Bitcoin Safe は引き続き、ハードウェアを使った multisig を含む本格的な self-custody を目指しており、2.0 では新しいユーザーにもその設定を順番に進められるガイドが用意されています。新しいウィザードは、今何が起きているのか、フローのどこにいるのか、そして先に進む前に各 signer が何を必要としているのかを説明します。

<p class="small text-muted">実装の詳細は <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/627">PR #627</a> を参照してください。</p>

主なリデザイン内容:

- 初めて使う人が正しい出発点を選べる新しいウェルカム画面
- ウォレット作成中のステップごとの進行フロー
- 集中した案内と文脈に応じたヘルプを備えたデバイス別の署名画面
- バックアップを明確に保つための、デバイス名とアイコン入り recovery PDF

{{< video src="wizard.mp4" controls=true autoplay=true muted=true playsinline=true align="start" >}}


<br><br>
## Compact Block Filters によるプライベートで堅牢なチェーン同期 {#private-sync-default}

[Compact Block Filters]({{< ref "library/compact-block-filters" >}}) は、Bitcoin Safe 2.0 の新しいウォレット同期の基盤になりました。Electrum サーバーにどのアドレスが自分のものかを問い合わせる代わりに、Bitcoin Safe はランダムな Bitcoin Core peer から compact filters をダウンロードし、ローカルで確認することでプライベートにチェーンをスキャンできます。

<p class="small text-muted">実装の詳細は <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/559">PR #559</a> を参照してください。</p>


- ウォレット同期は最初の起動からプライベートなまま
- サードパーティの Electrum サーバーに依存しない
- Electrum を好むユーザーのために、引き続き利用可能
- [最初のウォレットスキャン後は即時同期]({{< ref "library/compact-block-filters" >}})
- [リレーされたトランザクションの即時通知]({{< ref "library/instant-transactions-notifications/" >}})

{{< carousel-images folder="cbf-sync" align="start" maxwidth="740" >}}

<br><br>
## すべてのデバイスに対応するデバイス中心の署名フロー {#device-focused-signing}

このリデザインは、ウォレット作成後の署名フローも作り直しています。すべての signer に共通の一画面ではなく、Bitcoin Safe は今使っている具体的なデバイスを中心に操作をまとめるようになりました。

<p class="small text-muted">実装の詳細は <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/639">PR #639</a> を参照してください。</p>

- QR、USB、Bluetooth、ファイルのエクスポート/インポート、Sync & Chat の操作が、アクティブな signer カード上に直接表示されます
- 残っている signer、すでに署名済みのデバイス、次に必要な操作が一目で分かります
- 複数デバイスが混在する multisig フローでも、PSBT 全体を通して signer の識別が見えるため読みやすさが保たれます
- single-sig と multisig の入力が混ざる複雑なトランザクションも正しく扱われ、各署名ステップが明確になります

![QR、USB、Bluetooth、ファイルのエクスポート、Chat & Sync のデバイス別操作を表示する signer カード](signing-device-actions.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## ビジネス向けワークフローと power user のためのプラグインアーキテクチャ

Bitcoin Safe 2.0 は、Bitcoin ビジネスや power user 向けの追加プラグインに向けた土台も整えます。今後何が出てくるか、ぜひ注目してください :-)

<p class="small text-muted">実装の詳細は <a href="https://github.com/andreasgriffin/bitcoin-safe/pull/602">PR #602</a> を参照してください。</p>

- 外部の *sources* リポジトリを通じたプラグイン配布
- 各プラグインは [andreasgriffin]({{< gpg_key_link >}}) によって *GPG 署名* され、セキュリティ、完全性、配布を守ります
- 個別のプラグインバージョン管理と更新により、より速く独立したプラグイン開発が可能になります

![QR、USB、Bluetooth、ファイルのエクスポート、Chat & Sync のデバイス別操作を表示する signer カード](plugins.png)
{ .img-fluid .mb-5 style="max-width: 700px;" }

<br><br>
## より広いデバイス対応と仕上げの改善 {#hardware-support}

- アニメーション QR コードが **30%** 高速化し、より素早くスキャン可能に
- [Trezor Safe 7]({{< ref "library/supported-hardware-signers/trezor-safe-7" >}}) が USB 経由でサポートされました
- [Blockstream Jade/Jade Plus]({{< ref "library/supported-hardware-signers/jade" >}}) は USB と QR に加えて **Bluetooth** もサポート
- [Foundation Passport Prime]({{< ref "library/supported-hardware-signers/passport-prime" >}}) と [COLDCARD Mk5]({{< ref "library/supported-hardware-signers/coldcard-mk5" >}}) が対応デバイスに追加されました
- [対応デバイスの一覧]({{< ref "library/supported-hardware-signers" >}})を見る
- [再現性]({{< ref "library/reproducibility-and-security" >}}) のための自動チェックを追加
- 改善点の[完全な一覧](https://github.com/andreasgriffin/bitcoin-safe/compare/1.8.1...2.0.0)はこちら


{{< carousel-images folder="signers" align="start" maxwidth="640" >}}


<br><br>
## これまでの強みもそのまま残っています

2.0 リリースはリセットではありません。新しい onboarding と署名フローの下でも、Bitcoin Safe はこれまで日常的に役立ってきた機能をそのまま備えています。共同 multisig、PDF バックアップ、検索可能なウォレット履歴、資金フローの可視化、label sync などです。

{{< library-cards
  items="collaboration,label-sync,chart-zooming,address-tab-filters,balance-statement,pdf-export,address-poisoning,money-flow-diagram,multi-language,search,reproducibility-and-security"
  columns="3"
>}}

<div class="alert alert-primary text-start my-5" role="alert">
  <h2 class="h4 mb-2">Bitcoin Safe 2.0 を試す準備はできましたか？</h2>
  <p class="mb-3">最新リリースをダウンロードして、新しい onboarding、プライベート同期、そしてハードウェアウォレットの改善を自分で確かめてみてください。</p>
  <a class="btn btn-primary btn-lg px-4" href='{{< ref "download" >}}' role="button">Bitcoin Safe をダウンロード</a>
</div>


<br><br>

## ありがとうございます

このリリースは、貢献者、テスター、そして[プロジェクトを支えてくれる方々]({{< ref "donate" >}})の多くの努力の上に成り立っています:

- **[@design-rrr](https://github.com/design-rrr)** ([nostr](https://nostr.com/npub12lg6yexfh0gsk8aupv5cr5fnj46l0kxg6lp6rz0zw6kwx603lmsshmac9c),  [X](https://x.com/deSign__r)) に、ウィザードのリデザイン、プラグイン UI 作業、そして**素晴らしく粘り強い** UI/UX サポートをありがとう
- [@rustaceanrob](https://github.com/rustaceanrob) ([website](https://rustaceanrob.com/)) に、新しいウォレットのプライベート同期を支える Compact Block Filter クライアントをありがとう
- Bitcoin Safe の中核ライブラリを提供する [Bitcoin Dev Kit チーム](https://github.com/bitcoindevkit/) に感謝
- nostr 機能を支えるライブラリを提供する [ndk チーム](https://github.com/nostr-dev-kit/ndk) に感謝
- release candidate のテスト、バグ報告、ページ翻訳、sats の送付、そしてプロジェクトを前に進め続けてくれた Bitcoin Safe コミュニティの皆さんに感謝
- [翻訳者]({{< ref "donate/#translators" >}}) の皆さん。たとえば <a href="https://github.com/qdyg-vn" target="_blank"><img src="https://github.com/qdyg-vn.png" alt="qdyg-vn 🇻🇳 (ベトナム語)" title="qdyg-vn 🇻🇳 (ベトナム語)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://x.com/bsn21m" target="_blank"><img src="https://unavatar.io/x/bsn21m" alt="bsn21m 🇩🇪 (ドイツ語)" title="bsn21m 🇩🇪 (ドイツ語)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://github.com/cyphra" target="_blank"><img src="https://github.com/cyphra.png" alt="cyphra 🇪🇸 (スペイン語)" title="cyphra 🇪🇸 (スペイン語)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>
<a href="https://hosted.weblate.org/user/DaGrindDontStop/" target="_blank"><img src="https://unavatar.io/x/DaGrindDontStop" alt="DaGrindDontStop 🇨🇳 (中国語)" title="DaGrindDontStop 🇨🇳 (中国語)" style="width: 1.2em; height: 1.2em; object-fit: cover; border-radius: 50%; vertical-align: text-bottom;" /></a>


次のリリースを支援したい場合は、こちらから寄付できます: {{< donation_btc >}}
