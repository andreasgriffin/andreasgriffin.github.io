---
title: "ダウンロード"
description: "Bitcoin Safe をダウンロード"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}

✅ **Bitcoin Safe は新しいバージョンがあると通知し、正当性を自動で検証します。**


Windows のバイナリは署名されています。[コード署名ポリシー]({{< ref "code-signing-policy" >}}) を確認してください。こちらも [Bitcoin Safe プライバシーポリシー]({{< ref "code-signing-policy" >}}) をご覧ください。macOS のバイナリは署名されていないため、警告メッセージは無視してください。

<br>
<br>

###  macOS 

macOS で Bitcoin Safe を実行するには、次の手順に従ってください:
- アプリケーションフォルダにコピーします
- 開こうとすると警告が表示されます
- *システム設定* --> *プライバシーとセキュリティ* --> *とにかく開く* に移動します
- これで開けるようになります


<img src="/images/mac/copy-app.png" alt="macOS アプリをコピー"   /> 
<img src="/images/mac/warning.png" alt="macOS 警告"   /> 
<img src="/images/mac/disable.png" alt="macOS で Bitcoin Safe を開く"   /> 



<br>
<br>

### Debian/Ubuntu（APT リポジトリ）

{{< apt_repo_install >}}

<br>
<br>

###  署名の検証

すべてのソフトウェアは私の秘密鍵で署名されています。ダウンロードが正当なものであることを次の手順で確認してください:

私の [公開鍵]({{< gpg_key_link >}}) をインポートし、以下で署名を検証してください：
```bash
{{< gpg_import_code >}}
```



<br> 
<br>


<!-- ### Alternative install  via pip  on Mac, Linux, or Windows 
PyPi: https://pypi.org/project/bitcoin-safe/
python -m pip install bitcoin-safe
python -m bitcoin_safe
-->