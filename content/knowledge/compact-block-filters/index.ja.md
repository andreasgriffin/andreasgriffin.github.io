---
title: "コンパクトブロックフィルター"
description: "コンパクトブロックフィルターが何か、そしてElectrumサーバーと比べてどのようにプライバシーを向上させるかを理解する。"
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "コンパクトブロックフィルター"
  - "CBF"
  - "プライバシー"
  - "ビットコインウォレット"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}

**コンパクトブロックフィルター（CBF）** を使うと、[Bitcoin Safe]({{< ref "/" >}}) は Electrum サーバーにアドレスを尋ねずにブロックチェーンをスキャンできます。

![Bitcoin Safe が複数のランダムな Bitcoin Core ピアからコンパクトブロックフィルターをダウンロードします。](logo.jpg)
{ .img-fluid .float-end .ms-4 .mb-3 style="max-width: 260px;" }

中央サーバーに問い合わせる代わりに、Bitcoin Safe は各ブロックの小さなフィルターをランダムな Bitcoin Core ピアからダウンロードします。ウォレットはそれをローカルで確認し、必要なときだけ完全なブロックを取得します。

### CBF と Electrum

<div class="table-responsive mb-4">
  <table class="table table-striped align-middle">
    <thead>
      <tr>
        <th scope="col">項目</th>
        <th scope="col">コンパクトブロックフィルター</th>
        <th scope="col">Electrum サーバー</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">プライバシー</th>
        <td><span class="text-success fw-semibold">良い</span> - ウォレットデータはローカルに保持される</td>
        <td><span class="text-danger fw-semibold">悪い</span> - サーバーがあなたのアドレスや履歴を把握できる</td>
      </tr>
      <tr>
        <th scope="row">データ元</th>
        <td><span class="text-success fw-semibold">良い</span> - ランダムな Bitcoin Core ピア</td>
        <td><span class="text-warning fw-semibold">中立</span> - 1つの選んだサーバー</td>
      </tr>
      <tr>
        <th scope="row">初回同期</th>
        <td><span class="text-warning fw-semibold">中立</span> - たいてい遅い</td>
        <td><span class="text-success fw-semibold">良い</span> - たいてい速い</td>
      </tr>
      <tr>
        <th scope="row">継続同期</th>
        <td><span class="text-success fw-semibold">良い</span> - 初回同期後はとても速い</td>
        <td><span class="text-success fw-semibold">良い</span> - たいてい速い</td>
      </tr>
      <tr>
        <th scope="row">向いている人</th>
        <td><span class="text-success fw-semibold">良い</span> - プライバシーを重視する人</td>
        <td><span class="text-success fw-semibold">良い</span> - 最速で設定・復元したい人</td>
      </tr>
    </tbody>
  </table>
</div>

### CBF を使う理由

- より高いプライバシー: ウォレットがサーバーに自分のアドレスを尋ねることはありません。
- 信頼できるインデクサー不要: Bitcoin Safe は Bitcoin ネットワークと直接通信します。
- 軽量な同期: フィルターは小さいので、ブロックチェーン全体は不要です。

### 期待できること

- 新しいウォレットまたは復元: 初回同期は通常 **5〜30分** です。
- すでに同期済みのウォレット: 追いつきは **とても速く**、多くの場合 **30秒未満** です。
- Electrum から CBF への切り替え: これも通常 **30秒未満** です。

Bitcoin Safe が接続するピア数は選べます。ピアが増えるほど冗長性は上がりますが、帯域幅と同期時間は増えがちです。デフォルトは **2** ピアです。

### 未確認トランザクション

CBF がカバーするのは **確認済みブロック** だけです。未確認の入金も受け取りたい場合は、[インスタント取引通知]({{< ref "knowledge/instant-transactions-notifications/" >}}) を有効のままにしてください。これが既定の設定です。

### 技術メモ

コンパクトブロックフィルターは [BIP158](https://bips.dev/158/) で定義されています。Bitcoin Safe はオープンソースの [Kyoto compact block filter module for BDK](https://github.com/2140-dev/kyoto) を使用しています。

_Bitcoin network monitoring_ 設定で、初期ピアとして自分の Bitcoin Core ノードを使うこともできます。

![初期ノード設定](inital-node.svg)
{ .img-fluid .mb-5   style="max-width: 414px;" }
