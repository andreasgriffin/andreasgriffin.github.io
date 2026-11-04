---
title: "安全でない COLDCARD シード"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "Coinkite デバイスで生成されたシードから資金を移行するための簡潔なガイドです。"
---

[Coinkite は、影響を受ける COLDCARD ファームウェアのシード生成における脆弱性を公表しました](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/)。[予測可能な RNG フォールバックと 32 ビット reseed に関する Block の技術分析](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware)も参照してください。ファームウェアを更新しても、既存のシードは修復されません。

**Coinkite 製品でシードを作成した場合は、早めに移行してください！**

## 移行チェックリスト

1. **COLDCARD 以外の署名デバイス**（[対応デバイスを見る]({{< ref "library/supported-hardware-signers" >}})）で、完全に新しいシードを生成します。古いシードは再利用しないでください。その後、その署名デバイスを Bitcoin-Safe のセットアップウィザードで使用し、新しい[シングルシグウォレット]({{< ref "library/setup-singlesig-wallet" >}})または[マルチシグウォレット]({{< ref "library/setup-multisig-wallet" >}})を作成します。
   - COLDCARD 以外のハードウェア署名デバイスがない場合は、初期化済みの専用 Android デバイスをオフラインに保ち、署名だけに使用する条件で [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}})を利用できます。
   - 新しいウォレットが正しく設定されたことを確認するため、ウィザードの受取・送金テストを完了してください。バックアップと新しい署名デバイス上の受取アドレスを確認し、少額のテスト資金を受け取った後、新しいウォレット内の別の確認済みアドレスへ self-send を成功させます。
2. 移行トランザクションに署名します。
   - **影響を受けるウォレットがシングルシグの場合：** 早く承認されるよう、高い手数料を設定して通常どおりブロードキャストします。
   - **影響を受けるウォレットがマルチシグの場合：** 公開 mempool に公開鍵が露出するため、通常の方法ではブロードキャストしないでください。署名済み raw transaction をコピーし、[MARA Slipstream](https://slipstream.mara.com/) から直接送信します。
3. 全残高が新しいウォレットに到着して承認されるまで古い COLDCARD を保管し、その後で最新のファームウェアに更新してください。

他の人の移行を手伝う場合でも、シードワードの共有、撮影、入力を求めてはいけません。シードは非公開のまま保ち、署名デバイスにだけ入力してください。
