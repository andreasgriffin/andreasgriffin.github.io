---
title: "Скачать"
description: "Скачать Bitcoin Safe"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}


✅ **Bitcoin Safe автоматически уведомляет вас о наличии новой версии и проверяет её подлинность.**


Windows binary files are signed, check the [Code signing policy]({{< ref "code-signing-policy" >}}). See here the   [Bitcoin Safe privacy policy]({{< ref "code-signing-policy" >}}).  The  MacOS binaries are not signed, so please disregard the warning message.

<br>
<br>

###  macOS 

Следуйте этим шагам, чтобы запустить Bitcoin Safe на macOS:
- Скопируйте его в папку *Приложения*
- При попытке открыть его появится предупреждение
- Перейдите в *Системные настройки* --> *Конфиденциальность и безопасность* --> *Открыть в любом случае*
- Теперь вы можете открыть его


<img src="/images/mac/copy-app.png" alt="Копирование приложения (macOS)"   /> 
<img src="/images/mac/warning.png" alt="Предупреждение (macOS)"   /> 
<img src="/images/mac/disable.png" alt="Открытие Bitcoin Safe (macOS)"   /> 

<br>
<br>

###  Проверка подписи

Всё программное обеспечение подписано моим приватным ключом. Проверьте подлинность загрузки, выполнив следующие шаги:

Импортируйте мой [публичный ключ]({{< gpg_key_link >}}) и проверьте подпись с помощью:
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