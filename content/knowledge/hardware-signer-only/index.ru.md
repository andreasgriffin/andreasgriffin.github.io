---
title: "Требуются аппаратные кошельки"
description: "Bitcoin Safe требует использование только аппаратных seed-фраз в Mainnet для максимальной безопасности и во избежание рисков хранения ключей в программном обеспечении. Вот почему это важно."
draft: false
tags: ["Featured", "Knowledge" ]
keywords: [
  "Bitcoin Safe",
  "аппаратный кошелёк",
  "программная seed-фраза",
  "Coldcard",
  "Trezor",
  "SeedSigner",
  "мультиподпись",
  "PSBT",
  "самостоятельное хранение",
  "безопасность Биткоина",
  "подмена адреса",
  "инструменты Биткоина"
]
images: ["logo.png" ]
# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=dbSmQmt0uDI"
weight: 21
---

 

![Bitcoin Safe logo](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }

## 🚫 Почему Bitcoin Safe запрещает программные seed-фразы в Mainnet?

🤔 Это неудобно?

🔥 На самом деле — это **существенное усиление безопасности**.

Bitcoin Safe **разрешает программные seed-фразы только в Testnet, Signet и Regtest** — никогда в Mainnet. Вот почему:

### ✅ Причины, по которым программные seed-фразы блокируются в Mainnet

- 🧠 **Программные seed-фразы небезопасны** 
  - На компьютерах полно рисков: перехват содержимого буфера обмена, вредоносное ПО, уязвимости в браузерах.
  - Один промах — и ваша seed-фраза скомпрометирована — всё потеряно.
  - Холодное хранение не должно начинаться в горячей среде.

</br>

- 🧊 **Холодное хранение должно рождаться холодным**
  - Пользователи часто генерируют seed-фразы в программных кошельках, а затем переносят их в аппаратные устройства.
  - Но первоначальное воздействие уже произошло — назад пути нет.
  - Истинное холодное хранение = создано на аппаратном подписанте с самого начала.

</br>

- 🎣 **Фишинг процветает из-за привычки вводить seed-фразы в приложения**
  - Ввод seed-фраз в приложения приучает доверять плохим шаблонам UX.
  - Только-аппаратное требование принуждает к лучшим привычкам и сокращает риск.
  - ✅ Отсутствие seed-фраз в Mainnet = меньше жертв фишинга.

</br>

- 🧪 **Разработчики всё ещё имеют гибкость**
  - Программные seed-фразы *разрешены* в:
    - Testnet
    - Signet
    - Regtest
  - Идеально для разработчиков. Никакого риска для реальных сатоши. 🧡



</br>


- 🔐 **Mainnet требует аппаратных подписантов — без исключений**
  - 🔌 USB, 📷 QR и 💾 SD-карта со всеми основными устройствами
    - [Coldcard]({{< ref "knowledge/supported-hardware-signers" >}})
    - [BitBox02]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Blockstream Jade]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Foundation Passport Core]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Trezor Safe]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Ledger]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Keystone]({{< ref "knowledge/supported-hardware-signers" >}})
    - [Specter DIY]({{< ref "knowledge/supported-hardware-signers" >}})
    - [SeedSigner]({{< ref "knowledge/supported-hardware-signers" >}})
  - [Посмотреть все поддерживаемые устройства →]({{< ref "knowledge/supported-hardware-signers" >}})


---

## 🛡️ Защита от подмены адресов

Bitcoin Safe **подсвечивает адреса получателя цветом**, чтобы подмена адреса становилась очевидной:

- 🟢 Зелёный = проверенный адрес для получения  
- 🟡 Жёлтый = адрес для сдачи (change)  

Если кто-то попытается подменить ваш буфер обмена фальшивым адресом, вы увидите это мгновенно.

![Пример обнаружения подмены адреса](https://i.postimg.cc/Pr4QwkgZ/431986530-187e3dbc-05f5-4386-8f80-f15eb2170fb1.png)
{ .img-fluid .mb-5 }

---

## ✅ Проверка адреса через USB или QR

Проверяйте адреса получения прямо на вашем аппаратном подписанте — не нужно полагаться на экран приложения.

{{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}

---



## ✅ Инструкции для каждого аппаратного подписанта
 
- {{<text-name-with-logo>}} включает пошаговые инструкции с скриншотами для каждого аппаратного подписанта, чтобы провести вас через каждый шаг 
    <div style="max-width: 500px;  width: 100%;">
        {{< carousel-images >}}
    </div>

   
---



## 🤝 Совместная мультиподпись стала проще

Bitcoin Safe делает мультиподпись удобной и готовой для командной работы:

- 🔐 Зашифрованный чат в Nostr  
- 🔁 Однокликовый обмен PSBT  
- 🔌 USB, 📷 QR и 💾 SD-карта

{{< youtube-embed link="https://www.youtube.com/watch?v=oQB2qzYZ_cw" >}}

---

## 🛠️ Мощные функции для всех пользователей

- 🟧 Мастер создания singlesig-кошелька  
- 🟨 Настройка 2 из 3 multisig  
- 🟩 Любая конфигурация n-of-m  
- 🖨️ Печатаемые PDF-листы для резервного копирования  
- 🔁 Синхронизация меток через Nostr  
- 🔍 Полная диаграмма потоков денег и поиск по истории транзакций

![Диаграмма транзакций в Bitcoin Safe](/images/bitcoin-safe-diagram-overview.png)

---

## 🌍 Глобально и удобно для пользователей

- Мультиязычная поддержка: {{< flags-short >}}
- Работает на: Windows, macOS и Linux  
- Перетаскивание PSBT / CSV  
- Расширенные фильтры для транзакций, UTXO, сумм и других параметров

---

## 💡 Кратко

Bitcoin Safe = настоящее хранение Биткоинов:

✅ Только аппаратные в Mainnet  
✅ Никакого воздействия программных seed-фраз  
✅ Дружественная к новичкам мультиподпись  
✅ Среды для разработчиков с тестированием  
✅ Функции для семьи и команд  

🔗 [Bitcoin-Safe.org]({{< ref "/" >}})  
🎥 Канал YouTube →: https://youtube.com/@BitcoinSafeOrg