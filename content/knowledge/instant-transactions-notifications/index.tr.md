---
title: "Anlık işlem bildirimleri"
description: "Bitcoin Safe'in Anlık İşlem Bildirimlerini Nasıl Aldığı"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [ "işlem"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---



![](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }


### {{< page-title >}}  
 
  


**Bitcoin Safe** (sürüm **1.5.0** ve sonrasında) cüzdanınızla ilgili gelen Bitcoin işlemleri için anlık bildirimleri destekler. İşte bunun altyapıda nasıl çalıştığı:



##### 1. 📡 Bitcoin P2P Ağına Dinleme

Bitcoin Safe doğrudan bir veya daha fazla **Bitcoin Core node'una** bağlanır; bu node'lar küresel **eşler arası (P2P)** ağında yer alır. Bu node'lar, **mempool**'a dahil edilmek üzere yeni yayınlanan işlemleri sürekli olarak birbirleriyle paylaşırlar.

Bitcoin Safe, bu yayınlanan mesajları pasif şekilde dinler ve şunlardan herhangi birinin olup olmadığını kontrol eder:

* herhangi bir işlemin cüzdanınızdaki **adresler** veya **UTXO'lar** ile ilgili olup olmadığı.

✅ **Gizliliği Korumaya Yönelik**
Bu yöntem tamamen **özel**dir. Dış dünyaya cüzdanınız hakkında **hiçbir şey açıklamaz**.
Bitcoin Safe, tıpkı normal bir Bitcoin Core node'u gibi davranır: yalnızca genel P2P trafiğini dinler — cüzdanınızla ilgili hiçbir şeyi duyurmaz veya istemez.



##### 2. 🧠 Eşleşme Bulundu — Sonra Ne Olur?

Eşleşen bir işlem bulunursa, Bitcoin Safe kullandığınız arka uca bağlı olarak farklı şekilde tepki verir:

###### Seçenek A: ⚡ Electrum veya Esplora Arka Ucu

* Bitcoin Safe, tam işlemi ve cüzdan durumunu sunucudan almak için **arka planda bir eşitleme başlatır**.

###### Seçenek B: 🔍 Kompakt Blok Filtreleri (Neutrino Modu)

* Cüzdan, **onaylanmamış işlemi doğrudan** yerel cüzdan verinize ekleyecektir — ek bir sorgulama gerekmez.



#### ⚙️ Tercihe Bağlı / Devre Dışı Bırakma Davranışı

Kullanıcı tercihleri ve gizlilik ayarlarına saygı göstermek için:

* 🔒 **Mevcut kullanıcılar** 1.5.0 veya daha yeni sürüme yükselttiğinde, bu özellik varsayılan olarak **tercihe bağlı (opt-in)** — ağ ayarlarında manuel olarak etkinleştirebilirsiniz.
* 🚀 **Yeni kullanıcılar** için bu özellik varsayılan olarak **etkin (opt-out)** durumundadır; çünkü hem **gizliliği korur** hem de cüzdan etkinliğini gerçek zamanlı takip etmek için **çok kullanışlıdır**.

Tam kontrol sizde kalır ve bu özelliği istediğiniz zaman açıp kapatabilirsiniz.
 
 


#### ⚠️  Sadece onaylanmış işlemlere güvenilebilir

Bitcoin Safe, yayınlanan bir işlemin geçerli olduğunu **doğrulayamaz**. Bir saldırgan — özellikle hem Electrum sunucunuzu hem de bağlı olduğunuz Bitcoin node'unu kontrol ediyorsa — şunları yapabilir:

* Adresinizle ilgili sahte bir işlem oluşturmak
* Cüzdan bildirimini tetiklemek için bunu yayınlamak
* İşlemin **geçersiz** olması veya **konsensüs kurallarıyla çakışması** nedeniyle hiçbir zaman onaylanmamasını sağlamak


  


#### ✅ Özet

Sürüm **1.5.0** itibarıyla Bitcoin Safe anlık işlem bildirimlerini şu yollarla destekler:

* Bitcoin P2P ağına pasif şekilde dinleme (Bitcoin Core gibi)
* Cüzdanınızdaki **adresler** veya **UTXO'lar** ile ilgili işlemleri eşleme
* Tam ayrıntıları Electrum/Esplora aracılığıyla getirme veya Kompakt Blok Filtreleri aracılığıyla doğrudan ekleme
* Dış dünyaya cüzdan verisi asla açıklamama