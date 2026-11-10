---
title: "ウォレット通知"
description: "Bitcoin-Safe のウォレットおよびアプリの通知を、設定した送信先へ転送します。配信、プライバシー、タイミングを細かく制御できます。"
draft: false
tags: ["Plugins"]
images: ["notifications.png"]
weight: 35
faq:
  title: "ウォレット通知に関するよくある質問"
  items:
    - question: "Bitcoin-Safe はどこへ通知を送信できますか？"
      answer: "Bitcoin-Safe は次の宛先に通知を送信できます:\n- Webhook: 汎用 JSON、または Slack 互換、Discord、Google Chat、Microsoft Teams、Telegram Bot API、ntfy、Gotify の形式\n- Nostr のダイレクトメッセージ\n- Telegram ボット\n- SMTP によるメール\n- CalDAV カレンダー"
    - question: "通知から機密情報を除外できますか？"
      answer: "はい。機密情報を隠す設定を有効にすると、メッセージには Bitcoin-Safe の通知イベントが発生したという一般的な通知だけが含まれます。"
    - question: "どのイベントをどの宛先へ送るか制御できますか？"
      answer: "宛先ごとに個別のルールがあります。受け取るイベントの種類を選択できます:\n- ウォレットの取引\n- 予定された支払い\n- 同期とチャット\n- 警告\n\nオプションで配信のランダムな遅延も設定できます。"
    - question: "アプリはロックを解除したままにしておく必要がありますか？"
      answer: "いいえ。「ロックしてトレイに最小化」を使うと、ウォレットがロックされていても Bitcoin-Safe をバックグラウンドで動作させ続けられます。"
---

### {{< page-title >}}

<p class="lead">ご利用のチャネルで、ウォレットの動きに関する通知を受け取れます。</p>

<ul class="plugin-features">
<li>受信・送信の取引、Sync&Chat のメッセージ、期限が来た予定支払いなど ...</li>
<li>Webhook、Nostr、Telegram、メール、カレンダーなどへ通知を転送</li>
<li>各宛先が受け取るイベントを選択し、機密情報を隠す</li>
<li>Bitcoin-Safe をバックグラウンドで実行: <strong>ロックしてトレイに最小化</strong>を使うと、ウォレットがロックされていてもアプリが動作し続けます</li>
</ul>

### Webhook の設定

{{< video "webhook.mp4" controls >}}

### Nostr ダイレクトメッセージ

{{< video "nostr.mp4" controls >}}

### カレンダー通知

{{< video "calendar.mp4" controls >}}

### 送信先の接続

- 送信先を 1 つ以上追加します。それぞれに受信者と配信ルールを設定できます。
- **メール:** ホスト、ポート、認証情報、送信者、セキュリティ設定を使って SMTP サーバーに直接接続します。Gmail や Outlook の管理された連携ではありません。
- **Telegram:** ボットを使ってチャットへ送信します。ボットと会話を始めると、動作確認や最近のチャット ID の検出ができます。
- **Nostr DM:** 送信者の鍵を使い、設定したリレー経由で `npub` の受信者へ暗号化された NIP-17 メッセージを送信します。
- **CalDAV:** 設定済みの Nextcloud カレンダーなど、既存のカレンダーにイベントを追加します。
- **Webhook:** 汎用 JSON、または Slack 互換のエンドポイント、Discord、Google Chat、Microsoft Teams、Telegram Bot API、ntfy、Gotify 向けの形式で送信します。一般的なエンドポイントの種類は自動検出される場合があります。
- 送信先の設定を保存し、対応している場合はテスト機能を使ってください。

### 送信内容の選択

- 各送信先が受け取るイベントの種類を選択します:
  - ウォレットの取引
  - 予定された支払い
  - 同期とチャット
  - 警告
- 機密情報を隠せます。その場合、メッセージには Bitcoin-Safe の通知イベントが発生したという一般的な通知だけが含まれます。
- 選択した最大時間までの、ランダムな配信遅延を設定できます。
- 利用可能で詳細を隠していない場合、ウォレットの取引メッセージにブロックエクスプローラーのリンクが含まれることがあります。

### 配信の確認

- 最近の履歴には、各イベント、送信先、アダプター、時刻、結果（送信済み、一部成功、失敗）が表示されます。
- 配信は、設定した送信先とその利用可否によって異なります。外部サービスに送信する情報に注意してください。

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
<summary>Bitcoin-Safe はどこへ通知を送信できますか？</summary>

Bitcoin-Safe は次の宛先に通知を送信できます:

- Webhook: 汎用 JSON、または Slack 互換、Discord、Google Chat、Microsoft Teams、Telegram Bot API、ntfy、Gotify の形式
- Nostr のダイレクトメッセージ
- Telegram ボット
- SMTP によるメール
- CalDAV カレンダー

</details>

<details>
<summary>通知から機密情報を除外できますか？</summary>

はい。機密情報を隠す設定を有効にすると、メッセージには Bitcoin-Safe の通知イベントが発生したという一般的な通知だけが含まれます。

</details>

<details>
<summary>どのイベントをどの宛先へ送るか制御できますか？</summary>

宛先ごとに個別のルールがあります。受け取るイベントの種類を選択できます:

- ウォレットの取引
- 予定された支払い
- 同期とチャット
- 警告

オプションで配信のランダムな遅延も設定できます。

</details>

<details>
<summary>アプリはロックを解除したままにしておく必要がありますか？</summary>

いいえ。「ロックしてトレイに最小化」を使うと、ウォレットがロックされていても Bitcoin-Safe をバックグラウンドで動作させ続けられます。

</details>
</content>
