---
title: "Niebezpieczny seed COLDCARD"
date: "2026-08-02"
images: ["https://raw.githubusercontent.com/thebitcoinhole/database/refs/heads/master/item-types/hardware-wallets/img/coldcard-mk5-thumb.webp"]
draft: false
description: "Krótka instrukcja przeniesienia środków z seeda wygenerowanego na urządzeniu Coinkite."
---

[Coinkite ujawniło słabość generowania seedów w zagrożonym firmware COLDCARD](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/). Zobacz także [analizę techniczną Block dotyczącą przewidywalnego mechanizmu awaryjnego RNG i 32-bitowego reseedu](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware). Aktualizacja firmware nie naprawia istniejącego seeda.

**Jeśli seed został utworzony przy użyciu dowolnego produktu Coinkite, przenieś środki WKRÓTCE!**

## Lista kontrolna migracji

1. Wygeneruj całkowicie nowy seed na **urządzeniu podpisującym innym niż COLDCARD** ([zobacz obsługiwane urządzenia]({{< ref "library/supported-hardware-signers" >}})). Nie używaj ponownie starego seeda. Następnie użyj tego signera w kreatorze konfiguracji Bitcoin-Safe, aby utworzyć nowy [portfel z jednym podpisem]({{< ref "library/setup-singlesig-wallet" >}}) albo [portfel multisig]({{< ref "library/setup-multisig-wallet" >}}).
   - Jeśli nie masz sprzętowego signera innego niż COLDCARD, możesz użyć [MetroVault]({{< ref "library/supported-hardware-signers/metrovault" >}}) na dedykowanym urządzeniu z Androidem, przywróconym do ustawień fabrycznych, pozostającym offline i używanym wyłącznie do podpisywania.
   - Ukończ w kreatorze test odbierania i wysyłania, aby upewnić się, że nowy portfel jest poprawnie skonfigurowany: sprawdź jego kopię zapasową i adres odbiorczy na nowym signerze, odbierz niewielką kwotę testową i wykonaj udaną wysyłkę do innego zweryfikowanego adresu tego samego nowego portfela.
2. Podpisz transakcję migracyjną:
   - **Jeśli zagrożony portfel jest portfelem z jednym podpisem:** rozgłoś ją w zwykły sposób z wysoką opłatą, aby została szybko potwierdzona.
   - **Jeśli zagrożony portfel jest portfelem multisig:** nie rozgłaszaj jej w zwykły sposób, ponieważ ujawnia to jego klucze publiczne w publicznym mempoolu. Skopiuj podpisaną surową transakcję i prześlij ją bezpośrednio przez [MARA Slipstream](https://slipstream.mara.com/).
3. Zachowaj stary COLDCARD do czasu, aż całe saldo dotrze do nowego portfela i zostanie potwierdzone, a następnie zaktualizuj go do najnowszego firmware.

Jeśli pomagasz komuś w migracji, nigdy nie proś o udostępnienie, sfotografowanie ani wpisanie słów seeda. Seed powinien pozostać prywatny i być wprowadzany wyłącznie na urządzeniu podpisującym.
