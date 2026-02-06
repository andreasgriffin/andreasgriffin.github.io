---
title: "Notificaciones instantáneas de transacciones"
description: "Cómo Bitcoin Safe recibe notificaciones instantáneas de transacciones"
draft: false
tags: ["Knowledge" ]
# Download the logo from here https://i.ytimg.com/vi/xxxxxxxx/maxresdefault.jpg
images: ["logo.png" ]
keywords: [
  "cartera Bitcoin segura para familias",
  "bitcoin",
  "ahorro en bitcoin",
  "firmador de hardware",
  "Custodios de Bitcoin",
  "Asesores financieros",
  "cartera bitcoin",
  "trezor",
  "bitcoin EE. UU.",
  "BTC",
  "HODL",
  "Seguridad de Bitcoin",
  "Notificaciones instantáneas de transacciones"
]

# embedding videos can be done with 
# {{< youtube-embed link="https://www.youtube.com/watch?v=dbSmQmt0uDI" >}}
# or the list will be rendered below the content
# videos:
#   - "https://www.youtube.com/watch?v=GykmXP6Z1zM"
weight: 0
---



![Bitcoin Safe logo](logo.png)
{ .img-fluid .mb-5 .float-end style="max-width: 300px;" }


### {{< page-title >}}  
 
  


**Bitcoin Safe** (a partir de la versión **1.5.0**) admite notificaciones instantáneas de transacciones entrantes de Bitcoin relevantes para tu monedero. Así es como funciona internamente:




##### 1. 📡 Escuchando la red P2P de Bitcoin

Bitcoin Safe se conecta directamente a uno o más **nodos Bitcoin Core**, que participan en la red global **peer-to-peer (P2P)**. Estos nodos intercambian continuamente las transacciones recién difundidas destinadas a ser incluidas en la **mempool**.

Bitcoin Safe escucha pasivamente esos mensajes difundidos y comprueba si:

* alguna transacción involucra **direcciones** o **UTXOs** de tu monedero.

✅ **Preservación de la privacidad**
Este método es **completamente privado**. No **revela nada** sobre tu monedero al mundo exterior.
Bitcoin Safe se comporta justo como un nodo normal de Bitcoin Core: solo escucha el tráfico P2P público — nunca anuncia ni solicita nada específico de tu monedero.



##### 2. 🧠 Coincidencia encontrada — ¿qué ocurre a continuación?

Si se encuentra una transacción coincidente, Bitcoin Safe reaccionará de forma diferente según el backend que estés usando:

###### Opción A: ⚡ Backend Electrum o Esplora

* Bitcoin Safe **iniciará una sincronización en segundo plano** para obtener la transacción completa y el estado del monedero desde el servidor.

###### Opción B: 🔍 Filtros compactos de bloques (modo Neutrino)

* El monedero **añadirá directamente la transacción no confirmada** a los datos locales del monedero — no se necesita más búsqueda.



#### ⚙️ Comportamiento Opt-In / Opt-Out

Para respetar las preferencias del usuario y los ajustes de privacidad:

* 🔒 **Para usuarios existentes** que actualicen a la versión 1.5.0 o posterior, esta función está **desactivada por defecto (requiere opt-in)** — puedes habilitarla manualmente en la configuración de red.
* 🚀 **Para nuevos usuarios**, esta función está **activada por defecto (opt-out)**, ya que es **respetuosa con la privacidad** y **muy útil** para seguir la actividad del monedero en tiempo real.

Mantienes el control total y puedes activar o desactivar esta función en cualquier momento.
 
 

![Notification settings screenshot](config.png)
{ .img-fluid .mb-5 }


#### ⚠️ Solo las transacciones confirmadas pueden considerarse fiables

Bitcoin Safe no puede validar por sí mismo que una transacción difundida sea válida. Un atacante —especialmente uno que controle tanto tu servidor Electrum como el nodo Bitcoin al que estás conectado— podría:

* Fabricar una transacción falsa que involucre tu dirección
* Difundirla para desencadenar una notificación en el monedero
* Asegurarse de que nunca se confirme, porque es **inválida** o **entra en conflicto con las reglas de consenso**


  


#### ✅ Resumen

A partir de la versión **1.5.0**, Bitcoin Safe soporta notificaciones instantáneas de transacciones mediante:

* Escuchar pasivamente la red P2P de Bitcoin (como Bitcoin Core)
* Coincidir transacciones que involucren las **direcciones** o **UTXOs** de tu monedero
* Obtener los detalles completos vía Electrum/Esplora o añadirlas directamente mediante Filtros compactos de bloques
* No revelar nunca ningún dato del monedero al mundo exterior