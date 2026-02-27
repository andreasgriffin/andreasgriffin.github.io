---
title: "Pobierz"
description: "Pobierz Bitcoin Safe"
draft: false
menu:
  footer:
    weight: 10
---

### {{< page-title >}} 

<br>

{{< latest_release >}}

✅ **Bitcoin Safe automatycznie powiadamia o nowszej wersji i weryfikuje autentyczność.**


Pliki binarne dla Windows są podpisane — sprawdź [Zasady podpisywania kodu]({{< ref "code-signing-policy" >}}). Zobacz także [Politykę prywatności Bitcoin Safe]({{< ref "code-signing-policy" >}}). Binarne pliki dla macOS nie są podpisane, więc zignoruj komunikat ostrzegawczy.

<br>
<br>

###  macOS 

Postępuj zgodnie z poniższymi krokami, aby uruchomić Bitcoin Safe na macOS:
- Skopiuj go do folderu Aplikacje
- Spróbuj go otworzyć — pojawi się ostrzeżenie
- Przejdź do *Ustawienia systemowe* --> *Prywatność i bezpieczeństwo* --> *Otwórz mimo to*
- Teraz możesz go otworzyć


<img src="/images/mac/copy-app.png" alt="macOS: kopiowanie aplikacji"   /> 
<img src="/images/mac/warning.png" alt="macOS: ostrzeżenie"   /> 
<img src="/images/mac/disable.png" alt="macOS: otwarcie Bitcoin Safe"   /> 



<br>
<br>

### Debian/Ubuntu (repozytorium APT)

{{< apt_repo_install >}}

<br>
<br>

###  Weryfikacja podpisu

Wszystkie programy są podpisane moim kluczem prywatnym. Aby zweryfikować autentyczność pobrania, wykonaj następujące kroki:

Zaimportuj mój [klucz publiczny]({{< gpg_key_link >}}) i zweryfikuj podpis za pomocą:

{{< gpg_verify_tabs >}}



<br> 
<br>


<!-- ### Alternative install  via pip  on Mac, Linux, or Windows 
PyPi: https://pypi.org/project/bitcoin-safe/
python -m pip install bitcoin-safe
python -m bitcoin_safe
-->