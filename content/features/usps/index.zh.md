---
title: "为什么选择 Bitcoin Safe?"
description: "市面上有多款桌面比特币钱包。了解是什么让 Bitcoin Safe 脱颖而出。"
draft: false
tags: ["Featured","Features"]
images: ["logo.png"]
keywords: ["比特币安全", "独特的功能", "固定钱包", "方便使用的"]
weight: 1000
---



## {{< page-title >}} 
<!-- {{< page-description >}}  -->

<br>
<!-- <br> -->

### ✔ 轻松实现安全的比特币存储 
<!-- - ❌ 2-of-3 Multisignature is complex to use in other wallets -->
<!-- - 2-of-3 Multi-signature is a good choice  
    - Robust against loss or leak of 1 seed  -->
- The {{<text-name-with-logo>}} <a  href={{< ref "knowledge/setup-singlesig-wallet" >}} role="button">设置向导</a>    让单签名和多重签名对非技术用户也变得**简单**
    --> 只需按步骤操作即可建立一个安全的钱包。   
    <img  src="/images/multisig-steps.png" style="max-width: 600px; width: 100%;">
    - The <a  href={{< ref "features/pdf-export" >}}   role="button"> <img  src="pdf-export.png" width="100">  PDF 导出</a>   帮助您备份每个种子对应的重要钱包描述符。
    - 将多重签名在每个硬件签名器上注册
    - 包括测试从钱包接收和支出，以确保所有主要硬件签名器都能工作
<br>


<br>

#### ✔ 标签同步与备份

{{<text-name-with-logo>}} 将通过加密的 <a href="https://nostr.com/ ">nostr</a> 消息神奇地实现：
- <a  href="{{< ref "features/label-sync" >}}" role="button">同步</a> 您的币种分类和标签到多台电脑
- 备份您的币种分类和标签。您所需做的只是备份一个简短的备份密钥。
 

<br>

####  ✔ 多方多签协作

想参与一个 3-of-5 多重签名钱包吗？

- 钱包创建后，{{<text-name-with-logo>}} 会创建一个加密的 <a href="https://nostr.com/ ">nostr</a> 群聊用于协作，并可以 <a  href="{{< ref "features/collaboration" >}}" role="button">传递 PSBT</a> 以供签名。 
- <a  href="{{< ref "features/label-sync" >}}" role="button">标签同步</a> 当然也可用。
- 为了安全，每位参与者都必须对其他用户进行身份验证（一个简单的点击）


<br>


#### ✔ 在币种类别中组织地址

 <img  src="coin-categories.png" width="150"> 
 
- 您可以将地址聚合到 **币种类别** 中。这比为每个地址单独打标签更方便。
- 对于您创建的每个 PSBT，选择匹配的币种类别，{{<text-name-with-logo>}} 将只从该类别中选择输入。   
- 如果 PSBT 或交易混合了币种类别，{{<text-name-with-logo>}} 会发出警告。


<br>


#### ✔ 减少出错的可能性

过去有人犯下许多代价高昂的错误。如果人们从不在电脑上输入种子，大多数错误都可以避免。{{<text-name-with-logo>}} 会阻止您在电脑上使用种子，并鼓励您使用硬件签名器。

- {{<text-name-with-logo>}} 完全支持最常见的硬件签名器（例如 <a href="https://store.coinkite.com/promo/8BFF877000C34A86F410">Coldcard</a>, 
            <a href="https://store.coinkite.com/promo/8BFF877000C34A86F410">Coldcard Q</a>, 
            <a href="https://shop.bitbox.swiss/?ref=MOB4dk7gpm">Bitbox02</a>, 
            <a href="https://store.blockstream.com/?code=XEocg5boS77D">Blockstream Jade</a>,    
            <a href="https://trezor.io/trezor-safe-5-bitcoin-only">Trezor Safe</a>,
            <a href="https://foundation.xyz/passport">Foundation Passport</a>,
            <a href="https://keyst.one/?rfsn=8630473.c25550a&utm_source=refersion&utm_medium=affiliate&utm_campaign=8630473.c25550a">Keystone</a>,
            <a href="https://shop.ledger.com/pages/ledger-nano-s-plus">Ledger</a>,
            <a href="https://clavastack.com/en/?coupon=bitcoin-safe">Specter DIY</a>)  
- {{<text-name-with-logo>}} 为每款硬件签名器提供截图说明，引导您完成每一步 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-hardware-signer-screenshots >}}
    </div>

   

<br>




#### ✔ 🔋内置全部功能🔋 


{{<text-name-with-logo>}} 的设计注重易用性，同时包含了所有重要的高级用户功能。
- 选择您自己的 electrum/esplora 服务器、mempool 实例和 nostr 中继
- 到处支持 CSV 导入与导出
- RBF、取消交易以及编辑已完成的 PSBT
- 以及更多功能：请参见 <a href="https://github.com/andreasgriffin/bitcoin-safe?tab=readme-ov-file#comprehensive-feature-list">完整功能列表</a>


<br>