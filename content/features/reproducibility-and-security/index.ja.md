---
title: "セキュリティと再現可能性"
description: "Bitcoin Safe は、再現可能ビルド、署名付きコミット、署名付きリリース、独立した外部監視など、高いバイナリセキュリティ基準に従っています。"
draft: false
tags: ["Featured", "Features", "Security"]
images: ["logo.png"]
keywords: ["reproducible builds", "verify binaries", "signed commits", "signed releases", "appimage", "flatpak", "windows exe", "binary security"]
weight: 18
---

### {{< page-title >}}
{{< page-description >}}
<br>

![Bitcoin Safe の再現可能ビルド出力](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 500px;" }

ダウンロードするアプリが公開ソースコードと本当に一致していることを確認できるように、Web サイト上のダウンロードの完全性を守るための複数の保護レイヤーを実装しています。

- **再現可能ビルド**: Linux の `deb`、`AppImage`、`Flatpak` ビルドに加え、Windows の `portable exe` と `setup exe` は、バイト単位で再現できます。再構築したファイルが完全に一致すれば、そのバイナリが同じソースコードから作られた強い証拠になります。
- **署名付きリポジトリ履歴**: [Bitcoin Safe の GitHub リポジトリ](https://github.com/andreasgriffin/bitcoin-safe/commits/main) は検証済みの署名付きコミットを公開しているため、レビュー担当者はどのコードが誰によってリリースに入ったのか確認できます。
- **署名付きバイナリ**: リリースファイルは Bitcoin Safe の[公開 PGP キー]({{< gpg_key_link >}})で署名されており、Windows バイナリは[コード署名ポリシー]({{< ref "code-signing-policy" >}})にも従っています。
- **独立した再現性チェック**: [WalletScrutiny](https://walletscrutiny.com/desktop/bitcoin.safe/) は独立して Bitcoin Safe を追跡し、デスクトップリリースの再現可能な検証状況を公開しています。
- **継続的な署名監視**: [BinaryWatch](https://binarywatch.org/) は Bitcoin Safe のリリースファイルを定期的に確認し、その署名が Bitcoin Safe の[公開 PGP キー]({{< gpg_key_link >}})に対して引き続き有効かどうかを監視しています。
- **アップデート検証**: アップデートは Bitcoin Safe 内に表示され、その署名は自動的に検証されます。

これらを合わせると、Bitcoin Safe はバイナリセキュリティを後付けではなく、ユーザー安全性の中核として扱う少数のプロジェクトの一つになります。

### セキュリティは Bitcoin Safe のあらゆる側面で最優先の考え方です

バイナリの完全性だけでなく、Bitcoin Safe は安全なデフォルト設定、良い運用慣行、そして明確なユーザーガイダンスを中心に設計されています。いくつか例を挙げます。

- **ハードウェア中心の保管**: Bitcoin Safe は[ハードウェアサイナー]({{< ref "knowledge/supported-hardware-signers" >}})を前提としているため、シードは汎用コンピュータ上のホットシークレットではなく、専用デバイス上に留まります。
- **より安全なセットアップフロー**: セットアップウィザードは、[ハードウェアサイナー]({{< ref "knowledge/supported-hardware-signers" >}})のテスト、[PDF バックアップシート]({{< ref "features/pdf-export/" >}})、そしてデバイスやシードバックアップの保管方法に関する案内を含め、実運用に本当に耐えられる wallet の作成を支援します。
- **受取アドレスの確認**: Bitcoin Safe では、共有前にサイナー上で[受取アドレスを確認すること]({{< ref "knowledge/verify-receive-address/" >}})が簡単にできます。
- **アドレスポイズニング検知**: 不審な[よく似たアドレス]({{< ref "features/address-poisoning/" >}})について警告します。
- **multisig のセキュリティ**: Bitcoin Safe は multisig wallet をサポートしているため、より大きな資金を単一障害点ではなく複数のデバイスや複数の人で守ることができます。
- **multisig を使いやすくするコラボレーション**: Bitcoin Safe は[multisig コラボレーション]({{< ref "features/collaboration/" >}})を実用的にし、実際の運用でセットアップや署名の調整をずっと簡単にします。
- **明確な署名フロー**: デバイスごとの署名画面により、PSBT レビュー時の混乱が減り、正しいサイナーで正しい操作を行いやすくなります。
