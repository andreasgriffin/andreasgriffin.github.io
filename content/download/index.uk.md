---
aliases:
  - "/download/"
title: "Завантажити"
description: "Завантаження Bitcoin Safe"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}

✅ **Bitcoin Safe сповіщає про новішу версію та автоматично перевіряє справжність.**


Бінарні файли для Windows підписані, дивіться [Політику підпису коду]({{< ref "code-signing-policy" >}}). Також дивіться [політику конфіденційності Bitcoin Safe]({{< ref "code-signing-policy" >}}). Бінарні файли для macOS не підписані, тому попередження можна ігнорувати.

<br>
<br>

###  macOS 

Будь ласка, виконайте ці кроки, щоб запустити Bitcoin Safe на macOS:
- Скопіюйте його в папку програм (Applications)
- Спробуйте відкрити — з’явиться попередження
- Перейдіть у *System Settings* --> *Privacy & Security* --> *Open Anyway*
- Тепер можна відкривати


<img src="/images/mac/copy-app.png" alt="macOS copy-app"   /> 
<img src="/images/mac/warning.png" alt="macOS warning"   /> 
<img src="/images/mac/disable.png" alt="macOS open Bitcoin Safe"   /> 



<br>
<br>

### Debian/Ubuntu (APT-репозиторій)

{{< apt_repo_install >}}

<br>
<br>

###  Перевірка підпису

Усе програмне забезпечення підписане моїм приватним ключем. Перевірте справжність завантаження за такими кроками:

Імпортуйте мій [публічний ключ]({{< gpg_key_link >}}) та перевірте підпис командою:

{{< gpg_verify_tabs >}}




<br> 
<br>


<!-- ### Alternative install  via pip  on Mac, Linux, or Windows 
PyPi: https://pypi.org/project/bitcoin-safe/
```bash
python -m pip install bitcoin-safe
python -m bitcoin_safe
``` -->
