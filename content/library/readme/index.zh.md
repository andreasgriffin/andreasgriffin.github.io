---
aliases:
  - "/zh/features/readme/"
title: "所有功能"
description: "Bitcoin-Safe 大部分功能的全面概述"
draft: false
bucket: features
images: ["logo.png"]
keywords: [
  "Bitcoin-Safe",
  "比特币储蓄钱包",
  "多重签名钱包",
  "Multisig 设置向导",
  "硬件签名器",
  "安全的种子存储",
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
  "多语言支持",
  "地址标签",
  "交易流向图",
  "PSBT",
  "费用选择",
  "mempool",
  "Electrum 服务器",
  "Compact Block Filters",
  "CSV 导出",
  "CSV 导入",
  "BIP329",
  "拖放",
  "Replace-by-Fee",
  "备份 PDF",
  "消息签名",
  "MicroSD",
  "USB",
  "二维码",
  "动画二维码",
  "搜索与过滤",
  "钱包聊天",
  "标签同步",
  "regtest",
  "Docker",
  "Nigiri",
  "跨平台",
  "安装",
  "开发"
]
weight: -10
---
<!-- header-end -->
# Bitcoin-Safe

#### 一个面向全家人的比特币储蓄钱包

- **简单** 的 Multisig 钱包设置
  - 提供逐步说明，用于安全的 MultiSig 设置，并带有 PDF 备份表
  - 测试交易确保所有硬件签名器已准备就绪
  - 完整支持 [Coldcard](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Coldcard Q](https://store.coinkite.com/promo/8BFF877000C34A86F410), [Bitbox02](https://shop.bitbox.swiss/?ref=MOB4dk7gpm), [Blockstream Jade](https://store.blockstream.com/?code=XEocg5boS77D), [Trezor](https://affil.trezor.io/SHtN), [Foundation Passport Core](https://foundation.xyz/?ref=cbyqjjxumy), [Keystone](https://keyst.one), [Ledger](https://shop.ledger.com/?r=400f1fff75b5), [Specter DIY](https://clavastack.com/en/?coupon=bitcoin-safe), [SeedSigner](https://seedsigner.com), [Krux](https://selfcustody.github.io/krux)，通过 *QR*、*USB* 和 *SD 卡* 进行交互
- **安全**：仅使用硬件签名器
  - 所有钱包都需要硬件签名器/钱包以安全存储种子
  - 由 **[BDK](https://github.com/bitcoindevkit/bdk)** 提供支持
- **多语言**：
  - 🇺🇸 英语, 🇨🇳 中文 - 简体中文, 🇪🇸 西班牙语 - español de España, 🇯🇵 日语 - 日本語, 🇷🇺 俄语 - русский, 🇵🇹 葡萄牙语 - português europeu, 🇮🇳 印地语 - हिन्दी, 阿拉伯语 - العربية, 🇮🇹 意大利语 - italiano, 🇫🇷 法语 - Français, 🇩🇪 德语 - Deutsch, 🇲🇲 缅甸语 - မြန်မာ, 🇰🇷 韩语 - 한국어, 🇹🇭 泰语 - ภาษาไทย, 🇮🇷 波斯语 (法尔西) - فارسی, 🇵🇱 波兰语 - Polski, 🇪🇸 加泰罗尼亚语 - Català，（如有需求可添加更多语言）
- **更简单** 的地址标签（使用分类，例如 “KYC”、“Non-KYC”、“工作”、“朋友”等）
  - 类别内的自动币选择
  - 交易流向图，可视化输入和输出，点击输入或输出可追踪资金流向
- **适合非技术用户的发送功能**
  - 通过 mempool-blocks 提供一键费用选择
  - 在费用较低时自动合并 UTXO
- **同步与聊天**：
  - 使用 nostr 的标签加密云备份
  - 不同电脑间的标签同步
  - 不同电脑间的钱包聊天和 PSBT 共享
- **快速**：
  - Electrum 服务器同步
  - 计划在 Bitcoin-Safe 2.0 发布时升级为 **Compact Block Filters**




### 功能全面 —— 简单且强大

| **Multisig 设置向导**          | **创建 PSBT、签名并广播**                     |
|--------------------------------|----------------------------|
| ![Multisig setup](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/multisig-setup.gif) |  ![Send transaction](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/send.gif) |
| **通过图表探索交易**          | **在所有钱包中按类型搜索**                    |
| ![Explorer](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/explorer.gif) |  ![Global search](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/global-search.gif) |
|   **自动标签同步**      | **多方 Multisig 协作**                  |
| ![Label sync](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/label-sync.gif)  |   ![PSBT share](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/psbt-share.gif) |
|   **币类分类**      |                 |
| ![Category drag and drop](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/category-drag-and-drop.gif)  |   |



### 在所有平台上可用
| ![Windows](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-win.png) | ![Mac OS X](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-mac.png) | ![Linux](https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/tx-linux.png) |
|-----------------------------|-----------------------------|----------------------------|
| Windows                    | Mac OS X                   | Linux                     |


## 详尽的功能清单

- **导入与导出功能**
  
  - 所有列表的 CSV 导出
  - 批量交易的 CSV 导入
  - 使用 [BIP329](https://bip329.org/) 的标签导入与导出
  - 从 Electrum 钱包导入标签
  - 将资金流向图导出为 svg
  - 交易、PSBT 和 CSV 文件的拖放支持

- **钱包功能**
  
  - 使用诸如 KYC、Non-KYC、工作、朋友 等类别简化地址标签
  - 对交易进行提费（通过 Replace-by-Fee）
  - 更快接收（通过 Child Pays For Parents）
  - 加密钱包存储
  - 含描述符（文本和二维码）的 PDF 备份
  - 通过 USB 和二维码进行消息签名

- **硬件签名器连接性**
  
  - MicroSD（文件）
  - USB
  - 二维码（为笔记本摄像头增强的二维码检测）
  - 动画二维码，包括 [Coldcard/BBQr](https://bbqr.org/) 和 [UR](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md) 格式

- **搜索与过滤选项**
  
  - 在 txid、utxo、标签、日期、金额、类别 中快速过滤
  - 在所有打开的钱包中搜索 txid、utxo、标签、日期、金额、类别

- **语言**
  
  - 🇺🇸 英语, 🇨🇳 中文 - 简体中文, 🇪🇸 西班牙语 - español de España, 🇯🇵 日语 - 日本語, 🇷🇺 俄语 - русский, 🇵🇹 葡萄牙语 - português europeu, 🇮🇳 印地语 - हिन्दी, 阿拉伯语 - العربية, 🇮🇹 意大利语 - italiano, 🇫🇷 法语 - Français, 🇩🇪 德语 - Deutsch, 🇲🇲 缅甸语 - မြန်မာ, 🇰🇷 韩语 - 한국어, 🇹🇭 泰语 - ภาษาไทย, 🇮🇷 波斯语 (法尔西) - فارسی, 🇵🇱 波兰语 - Polski, 🇪🇸 加泰罗尼亚语 - Català，（如有需求可添加更多语言）

- **交易 / PSBT 创建**
  
  - 一键费用选择及 mempool 区块预览
  - 在费用较低时自动合并 UTXO
  - 高亮显示自有地址

- **安全性与可靠性**
  
  - 在主网不会生成或存储种子
  - 种子存储需要单独的硬件签名器
  - 更新通知与签名验证
  - 由 [Bitcoin Development Kit (BDK)](https://github.com/bitcoindevkit/bdk) 提供支持

- **多重签名钱包的易用性**
  
  - 简化的 multisig 钱包设置，包括逐步说明和 PDF 备份表
  - 与所有硬件签名器进行测试签名
  - 协作式钱包管理，包括通过 nostr 的聊天与 PSBT 共享，以及受信设备之间的标签同步
  - 可选的自定义 nostr 服务器

- **即将到来的功能**
  
  - 面向 2.0 版本
    - 默认启用 **Compact Block Filters**
      - Compact Block Filters 既 **快速** 又 **私密**
      - Compact Block Filters（bdk）正在被[开发中](https://github.com/bitcoindevkit/bdk/issues/679)，并将包含在 bdk 1.1 中。目前可使用 RPC、Electrum 和 Esplora，但将被 Compact Block Filters 完全替代。


## 从 Git 仓库安装


### Ubuntu、Debian

- 安装依赖项： 
sudo apt-get install qt6-tools-dev-tools libzbar-dev libxcb-cursor0 '^libqt6.*$'
- 安装 `poetry` 并运行 `bitcoin_safe`
git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
  pip install poetry  && poetry install && poetry run python -m bitcoin_safe
### Mac

- 克隆 `bitcoin_safe`
open "/Applications/Python 3.12/Install Certificates.command"
  export SSL_CERT_FILE=$(python3 -m certifi) # 修复 ssl 错误
  git clone https://github.com/andreasgriffin/bitcoin-safe.git
  cd bitcoin-safe
- *可选*：依赖项 `zbar`
brew install zbar
- 运行 `bitcoin_safe`
python3 -m pip install poetry && python3 -m poetry install && python3 -m poetry run python3 -m bitcoin_safe
## 开发

* 手动运行 precommit 以便调试
poetry run pre-commit run --all-files
#### 使用 electrs 和 mempool 的 Regtest Docker 环境

* 安装 docker
# 参见 https://docs.docker.com/engine/install/ubuntu/
* 在 docker 中设置 regtest 环境并带有 mempool 实例
curl https://getnigiri.vulpem.com | sudo bash # 参见 https://nigiri.vulpem.com/#install
sudo nigiri start
xdg-open http://localhost:5000/
* 这将创建
  * esplora localhost:3000
    electrs localhost:50000 
  * 以及一个 GUI 区块浏览器在 http://localhost:5000
* 设置 mempool 实例
sudo apt install docker-compose
git clone https://github.com/ngutech21/nigiri-mempool.git

pushd nigiri-mempool
sudo docker-compose up -d
sleep 10
# 这是必须的，因为数据库需要时间启动 
sudo docker-compose up -d
popd
xdg-open http://localhost:8080/

# 如果 mempool 一直在加载，则获取调试输出
sudo docker-compose logs -f mempool-api
* 这会在 http://localhost:8080/ 打开一个 mempool 实例

#### 控制 Regtest 环境

* 给某个地址获取硬币
nigiri rpc generatetoaddress 1 bcrt1qgsnt3d4sny4w4zd5zl9x6jufc5rankqmgphyms9vz0ds73q4xfms655y4c # 挖块

# 或使用内部 fauc et
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

### Qt 设计器

可以使用 Qt Designer 查看 Qt 组件：
virtualenv .env-qt-designer
source .env-qt-designer/bin/activate
pip install pyqt6-tools 
pyqt6-tools designer
## 代码签名政策


由 [SignPath.io](https://about.signpath.io/) 提供的免费代码签名，证书由 [SignPath Foundation](https://signpath.org/) 提供


## 隐私政策
本程序默认使用：
- [blockstream.com](https://blockstream.com/) 的 electrum/esplora 服务器来获取区块链数据
- 从 [mempool.space](https://mempool.space/) 获取 mempool 费用信息

你可以在“网络设置”中为两者指定你自己的（个人）服务器。

启用 Sync&Chat 功能时，会使用默认中继（[default relays](https://github.com/andreasgriffin/bitcoin-nostr-chat/blob/main/bitcoin_nostr_chat/default_relays.py)）将加密数据传输到你批准的受信设备。你可以在 Sync&Chat 设置中指定自己的中继。

除非用户或安装/操作该程序的人明确请求，否则本程序不会向其他网络系统传输任何其他信息。