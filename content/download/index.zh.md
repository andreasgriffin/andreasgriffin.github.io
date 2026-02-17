---
title: "下载"
description: "下载 Bitcoin Safe"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}


✅ **Bitcoin Safe 会自动通知您有新版本并验证其真实性。**


Windows 二进制文件已签名，请查看 [代码签名策略]({{< ref "code-signing-policy" >}})。在此查看 [Bitcoin Safe 隐私政策]({{< ref "code-signing-policy" >}})。MacOS 的二进制文件未签名，因此请忽略警告信息。

<br>
<br>

###  macOS 

请按照以下步骤在 macOS 上运行 Bitcoin Safe：
- 将其复制到您的应用程序文件夹
- 尝试打开它时会出现警告
- 进入 *系统设置* --> *隐私与安全性* --> *仍要打开*
- 现在您可以打开它


<img src="/images/mac/copy-app.png" alt="macOS 复制应用"   /> 
<img src="/images/mac/warning.png" alt="macOS 警告"   /> 
<img src="/images/mac/disable.png" alt="macOS 打开 Bitcoin Safe"   /> 

<br>
<br>

###  验证签名

所有软件均使用我的私钥进行签名。请按照以下步骤验证下载是否为正版：

导入我的 [公钥]({{< gpg_key_link >}}) 并使用以下命令验证签名：
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