---
title: "Kompaktowe filtry bloków"
description: "Dowiedz się, czym są kompaktowe filtry bloków i jak poprawiają prywatność w porównaniu z serwerami Electrum."
draft: false
tags: ["Featured", "Knowledge" ]
images: ["logo.jpg" ]
keywords:
  - "Bitcoin Safe"
  - "kompaktowe filtry bloków"
  - "CBF"
  - "prywatność"
  - "portfel Bitcoin"
  - "Bitcoin Core"
  - "BDK"
weight: 0
---

## {{< page-title >}}


Bitcoin Safe   1.6.0 wprowadza **kompaktowe filtry bloków (CBF)** jako opcjonalny sposób synchronizacji portfela. Zamiast pytać scentralizowany serwer Electrum o historię swojego portfela, Bitcoin Safe może teraz pobierać mały plik podsumowujący dla każdego bloku bezpośrednio od losowych peerów Bitcoin Core. Te podsumowania działają jak krótka lista kontrolna, która pozwala Twojemu portfelowi samodzielnie zdecydować, czy dany blok może zawierać jedną z Twoich transakcji.

Ponieważ Bitcoin Safe podejmuje decyzje lokalnie, żaden serwer zewnętrzny nigdy nie dowiaduje się, które adresy lub transakcje są dla Ciebie istotne. Otrzymujesz te same dane potrzebne do potwierdzeń, jakie przechowuje pełny węzeł, ale w lżejszym formacie odpowiednim dla codziennych urządzeń.

**Dlaczego to jest lepsze:**

- 📦 **Małe pobrania:** Każdy filtr zajmuje tylko kilka kilobajtów, więc możesz synchronizować się przez zwykłe domowe łącza bez przechowywania całego łańcucha bloków.
- 🔐 **Bezpośrednio z sieci:** Bitcoin Safe łączy się z wieloma losowymi węzłami Bitcoin Core, tak jak robią to inne węzły, zmniejszając szansę, że pojedynczy obserwator będzie mógł Cię profilować.
- 🕵️ **Dopasowanie lokalne:** Twój portfel sprawdza filtry lokalnie. Jeśli filtr wydaje się istotny, dopiero wtedy pobiera konkretny blok, chroniąc Twoje adresy.

Serwery Electrum, w przeciwieństwie do tego, przeszukują łańcuch bloków w Twoim imieniu. Każde zapytanie ujawnia adresy Twojego portfela operatorowi serwera, który mógłby te informacje rejestrować. Dzięki kompaktowym filtrom bloków Bitcoin Safe pobiera te same neutralne dane, którymi wymieniają się wszystkie węzły. Nikt nie może stwierdzić, które adresy należą do Ciebie, ponieważ Twój portfel nigdy ich nie ujawnia.

Poniżej prosty widok pokazujący, jak Bitcoin Safe łączy się, gdy CBF jest włączone. Zwróć uwagę, jak odzwierciedla to sposób, w jaki węzły Bitcoin Core już się komunikują:


![Bitcoin Safe pobiera kompaktowe filtry bloków od kilku losowych peerów Bitcoin Core.](logo.jpg)
{ .img-fluid .mb-5   style="max-width: 450px;" }


Możesz wybrać, z ilu peerów Bitcoin Safe powinien się łączyć. Więcej peerów wymaga większej przepustowości i skutkuje wolniejszym czasem synchronizacji. Domyślnie jest to 2.  

 
### Czego się spodziewać podczas synchronizacji

CBF zmienia czas oczekiwania w zależności od tego, co robisz:

1. ✨ **Tworzenie lub odzyskiwanie portfela:** Niezależnie od tego, czy tworzysz nowy portfel, czy odzyskujesz istniejący, początkowa synchronizacja pobiera filtry dla całej historii Twojego portfela. Spodziewaj się, że ten jednorazowy proces potrwa **od 5 do 30 minut**, w zależności od szybkości Twojego internetu.
2. 🚀 **Otwarcie już zsynchronizowanego portfela:** Bitcoin Safe musi pobrać tylko najnowsze filtry od czasu Twojej ostatniej sesji. To uzupełnienie zwykle kończy się **w mniej niż 30 sekund**.
3. 🔄 **Przejście z serwerów Electrum na CBF:** Ponieważ portfel był wcześniej synchronizowany za pomocą serwerów Electrum, Bitcoin Safe musi pobrać tylko najnowsze filtry, co zwykle zajmuje **mniej niż 30 sekund**.

### Bądź na bieżąco z niepotwierdzonymi płatnościami

Kompaktowe filtry bloków dotyczą tylko **potwierdzonych bloków**. Aby dowiadywać się o przychodzących transakcjach zanim zostaną potwierdzone, upewnij się, że masz również włączone [Powiadomienia o transakcjach natychmiastowych]({{< ref "knowledge/instant-transactions-notifications/" >}}). Ta funkcja nasłuchuje komunikatów P2P z losowego węzła Bitcoin, dzięki czemu możesz reagować na aktywność w mempoolu bez rezygnacji z prywatności.


<br>
<br>



### Szczegóły techniczne


- *Dla deweloperów, którzy chcą zgłębić temat:* kompaktowe filtry bloków stosują specyfikację [BIP158](https://bips.dev/158/) i są omówione w [przeglądzie Elle Mouton na temat zbiorów kodowanych Golombem](https://ellemouton.com/posts/bip158/). Implementacja Bitcoin Safe opiera się na otwartoźródłowym [module Kyoto compact block filter dla BDK](https://github.com/rustaceanrob/kyoto).
- Możesz dodać własny węzeł Bitcoin Core do peerów używanych do synchronizacji kompaktowych filtrów bloków, wybierając _Węzeł początkowy_ w ustawieniach _Monitorowanie sieci Bitcoin_.


![](inital-node.png)
{ .img-fluid .mb-5   style="max-width: 414px;" }