---
aliases:
  - "/ja/features/readme/"
title: "すべての機能"
description: "Bitcoin Safe の主要機能の包括的な概要"
draft: false
bucket: features
images: ["logo.png"]
keywords: [
  "Bitcoin Safe",
  "ビットコイン貯蓄ウォレット",
  "マルチシグウォレット",
  "マルチシグセットアップウィザード",
  "ハードウェア署名デバイス",
  "セキュアなシード保管",
  "Coldcard",
  "Coldcard Q",
  "Bitbox02",
  "Blockstream Jade",
  "Trezor",
  "Foundation Passport Core",
  "Keystone",
  "Ledger",
  "Specter DIY",
  "BDK",
  "多言語対応",
  "アドレスラベリング",
  "トランザクションフローダイアグラム",
  "PSBT",
  "手数料選択",
  "mempool",
  "Electrum server",
  "Compact Block Filters",
  "CSVエクスポート",
  "CSVインポート",
  "BIP329",
  "ドラッグアンドドロップ",
  "Replace-by-Fee",
  "バックアップPDF",
  "メッセージ署名",
  "MicroSD",
  "USB",
  "QR codes",
  "アニメーションQRコード",
  "検索とフィルタリング",
  "ウォレットチャット",
  "ラベル同期",
  "regtest",
  "Docker",
  "Nigiri",
  "クロスプラットフォーム",
  "インストール",
  "開発"
]
weight: -10
---
<!-- header-end -->
# Bitcoin Safe

#### 家族全員向けのビットコイン貯蓄ウォレット

- **簡単** なマルチシグウォレット設定
  - PDFバックアップシート付きで安全なマルチシグ設定をステップバイステップで案内
  - テストトランザクションにより全てのハードウェア署名デバイスが準備済みであることを確認
  - [Coldcard](https://store.coinkite.com/promo/8BFF877000C34A86F410)、[Coldcard Q](https://store.coinkite.com/promo/8BFF877000C34A86F410)、[Bitbox02](https://shop.bitbox.swiss/?ref=MOB4dk7gpm)、[Blockstream Jade](https://store.blockstream.com/?code=XEocg5boS77D)、[Trezor](https://affil.trezor.io/SHtN)、[Foundation Passport Core](https://foundation.xyz/?ref=cbyqjjxumy)、[Keystone](https://keyst.one)、[Ledger](https://shop.ledger.com/?r=400f1fff75b5)、[Specter DIY](https://clavastack.com/en/?coupon=bitcoin-safe)、[SeedSigner](https://seedsigner.com)、[Krux](https://selfcustody.github.io/krux) をフルサポートし、*QR*、*USB*、*SDカード* を使用可能
- **安全**：ハードウェア署名デバイスのみ
  - すべてのウォレットは安全なシード保管のためにハードウェア署名デバイス／ウォレットを必要とします
  - **[BDK](https://github.com/bitcoindevkit/bdk)** により動作
- **多言語対応**:
  - 🇺🇸 English、🇨🇳 Chinese - 简体中文、🇪🇸 Spanish - español de España、🇯🇵 Japanese - 日本語、🇷🇺 Russian - русский、🇵🇹 Portuguese - português europeu、🇮🇳 Hindi - हिन्दी、Arabic - العربية、🇮🇹 Italian - italiano、🇫🇷 French - Français、🇩🇪 German - Deutsch、🇲🇲 Burmese - မြန်မာ、🇰🇷 Korean - 한국어、🇹🇭 Thai - ภาษาไทย、 🇮🇷 Persian (Farsi) - فارسی、🇵🇱 Polish - Polski、🇪🇸 Catalan - Català、（要望に応じてさらに追加）
- **シンプル化** されたアドレスラベル（カテゴリを使用、例：「KYC」「Non-KYC」「Work」「Friends」...）
  - カテゴリ内での自動コイン選択
  - 入出力を可視化するトランザクションフローダイアグラム。入力や出力をクリックして資金の流れを追跡可能
- **送金** を非技術系ユーザー向けに簡素化
  - mempool-ブロック情報によるワンクリック手数料選択
  - 手数料が低いときのUTXO自動統合
- **同期 & チャット**:
  - ラベルの暗号化クラウドバックアップ（nostr 経由）
  - 異なるコンピュータ間でのラベル同期
  - 異なるコンピュータ間でのウォレットチャットとPSBT共有
- **高速**:
  - Electrumサーバー同期
  - Bitcoin Safe 2.0 リリースでは **Compact Block Filters** へのアップグレードを予定




### 機能充実 — 簡単で強力

| **マルチシグセットアップウィザード**          | **PSBTの作成、署名、ブロードキャスト**                     |
|--------------------------------|----------------------------|
| ![Multisig setup](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/multisig-setup.gif) |  ![Send transaction](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/send.gif) |
| **ダイアグラムによるトランザクション探索**          | **すべてのウォレットでの入力して検索**                    |
| ![Explorer](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/explorer.gif) |  ![Global search](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/global-search.gif) |
|   **自動ラベル同期**      | **マルチパーティによるマルチシグ共同作業**                  |
| ![Label sync](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/label-sync.gif)  |   ![PSBT share](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/psbt-share.gif) |
|   **コインカテゴリ**      |                 |
| ![Category drag and drop](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/category-drag-and-drop.gif)  |   |



### すべてのプラットフォームで利用可能
| ![Windows](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-win.png) | ![Mac OS X](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-mac.png) | ![Linux](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-linux.png) |
|-----------------------------|-----------------------------|----------------------------|
| Windows                    | Mac OS X                   | Linux                     |


## 包括的な機能一覧

- **インポートとエクスポート機能**
  
  - すべてのリストのCSVエクスポート
  - バッチトランザクションのCSVインポート
  - [BIP329](https://bip329.org/) を使用したラベルのインポート/エクスポート
  - Electrumウォレットからのラベルインポート
  - マネーフローダイアグラムをsvgでエクスポート
  - トランザクション、PSBT、CSVファイルのドラッグアンドドロップ

- **ウォレット機能**
  
  - KYC、Non-KYC、Work、Friends のようなカテゴリを使った簡易アドレスラベリング
  - トランザクションの手数料引き上げ（Replace-by-Fee 経由）
  - 早く受け取りたい場合の受信支援（Child Pays For Parents）
  - 暗号化されたウォレットストレージ
  - ディスクリプタ付きバックアップPDF（テキストとQRコード）
  - USBおよびQR経由のメッセージ署名

- **ハードウェア署名デバイス接続**
  
  - MicroSD（ファイル）
  - USB
  - QRコード（ノートパソコンのカメラ向けに強化されたQRコード検出）
  - [Coldcard/BBQr](https://bbqr.org/) や [UR](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md) フォーマットを含むアニメーションQRコード

- **検索とフィルタリングオプション**
  
  - txid、utxo、ラベル、日付、金額、カテゴリにわたる高速フィルタリング
  - 開いているすべてのウォレット、txid、utxo、ラベル、日付、金額、カテゴリ全体での検索

- **言語**
  
  - 🇺🇸 English、🇨🇳 Chinese - 简体中文、🇪🇸 Spanish - español de España、🇯🇵 Japanese - 日本語、🇷🇺 Russian - русский、🇵🇹 Portuguese - português europeu、🇮🇳 Hindi - हिन्दी、Arabic - العربية、🇮🇹 Italian - italiano、🇫🇷 French - Français、🇩🇪 German - Deutsch、🇲🇲 Burmese - မြန်မာ、🇰🇷 Korean - 한국어、🇹🇭 Thai - ภาษาไทย、🇮🇷 Persian (Farsi) - فارسی、🇵🇱 Polish - Polski、🇪🇸 Catalan - Català、（要望に応じてさらに追加）

- **トランザクション / PSBT 作成**
  
  - ワンクリック手数料選択とmempoolブロックプレビュー
  - 手数料が低い場合のUTXO自動統合
  - 自分のアドレスのハイライト表示

- **セキュリティと信頼性**
  
  - メインネット上でのシード生成や保管は行わない
  - シード保管には別のハードウェア署名デバイスが必要
  - アップデート通知と署名検証
  - [Bitcoin Development Kit (BDK)](https://github.com/bitcoindevkit/bdk) により動作

- **マルチシグウォレットの使いやすさ**
  
  - ステップバイステップの手順とPDFバックアップシートを含むマルチシグウォレットの簡易セットアップ
  - すべてのハードウェア署名デバイスでのテスト署名
  - nostr 経由のチャットやPSBT共有、信頼できるデバイス間のラベル同期を含む共同ウォレット管理
  - 任意のカスタム nostr サーバーを設定可能

- **今後の機能**
  
  - 2.0 リリース向け
    - デフォルトでの **Compact Block Filters**
      - Compact Block Filters は **高速** かつ **プライベート**
      - Compact Block Filters（bdk）は [開発中](https://github.com/bitcoindevkit/bdk/issues/679) で、bdk 1.1 に含まれる予定です。現時点では RPC、Electrum、Esplora が使用可能ですが、最終的には Compact Block Filters に完全移行されます。


## Git リポジトリからのインストール


### Ubuntu、Debian

- 依存関係をインストール:
sudo apt-get install qt6-tools-dev-tools libzbar-dev libxcb-cursor0 '^libqt6.*$'
- `poetry` をインストールして `bitcoin_safe` を実行
git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
  pip install poetry  && poetry install && poetry run python -m bitcoin_safe
### Mac

- `bitcoin_safe` をクローン
open "/Applications/Python 3.12/Install Certificates.command"
  export SSL_CERT_FILE=$(python3 -m certifi) # to fix ssl errors
  git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
- *任意*: 依存関係 `zbar`
brew install zbar
- `bitcoin_safe` を実行
python3 -m pip install poetry && python3 -m poetry install && python3 -m poetry run python3 -m bitcoin_safe
## 開発

* デバッグ用に precommit を手動で実行
poetry run pre-commit run --all-files
#### electrs と mempool を含む Regtest の Docker 環境

* docker をインストール
# see https://docs.docker.com/engine/install/ubuntu/
* docker 上での regtest 環境と mempool インスタンスの設定
curl https://getnigiri.vulpem.com | sudo bash # see https://nigiri.vulpem.com/#install
sudo nigiri start
xdg-open http://localhost:5000/
* これにより作成されるもの
  * esplora localhost:3000
    electrs localhost:50000 
  * および GUI ブロックエクスプローラが http://localhost:5000 で利用可能
* mempool インスタンスのセットアップ
sudo apt install docker-compose
git clone https://github.com/ngutech21/nigiri-mempool.git

pushd nigiri-mempool
sudo docker-compose up -d
sleep 10
# データベースが起動するまで時間が必要なためこれが必要です 
sudo docker-compose up -d
popd
xdg-open http://localhost:8080/

# mempool が永遠に読み込み中の場合、デバッグ出力を取得するには
sudo docker-compose logs -f mempool-api
* これにより http://localhost:8080/ で mempool が開きます

#### Regtest 環境の制御

* アドレスにコインを取得する
nigiri rpc generatetoaddress 1 bcrt1qgsnt3d4sny4w4zd5zl9x6jufc5rankqmgphyms9vz0ds73q4xfms655y4c # mine blocks

# or use the internal faucet
nigiri faucet bcrt1qgsnt3d4sny4w4zd5zl9x6jufc5rankqmgphyms9vz0ds73q4xfms655y4c 0.01
<!-- * ## Installation from PyPi

### Ubuntu, Debian, Windows

- Install `poetry` and run `bitcoin_safe`
pip install bitcoin-safe
  python -m bitcoin_safe
### Mac

- Run `bitcoin_safe`
python3 -m pip install bitcoin-safe
  python3 -m bitcoin_safe
-->

### Qt デザイナ

Qt コンポーネントは qt designer で確認できます:
virtualenv .env-qt-designer
source .env-qt-designer/bin/activate
pip install pyqt6-tools 
pyqt6-tools designer
## コード署名ポリシー


無料のコード署名は [SignPath.io](https://about.signpath.io/) によって提供され、証明書は [SignPath Foundation](https://signpath.org/) によります。


## プライバシーポリシー
このプログラムはデフォルトで以下を使用します
- ブロックチェーンデータ取得のために [blockstream.com](https://blockstream.com/) の electrum/esplora サーバー
- 手数料情報取得のために [mempool.space](https://mempool.space/)

「ネットワーク設定」で両方に対して自分の（個人の）サーバーを指定できます。

Sync&Chat 機能を有効にすると、デフォルトのリレー群([default relays](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py)) が暗号化されたデータを承認済みの信頼できるデバイスに送信するために使用されます。Sync&Chat の設定で自分のリレーを指定できます。

このプログラムは、ユーザーやインストール・運用者が明示的に要求しない限り、他のネットワークシステムに追加の情報を送信することはありません。