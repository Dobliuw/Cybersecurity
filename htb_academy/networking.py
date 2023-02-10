"""
ISP (Internet Service Provider) ----> Organización que brinda servicios para acceder a internet.
DNS (Domain Name Server) ----> Se encarga de cambiar las direciones ip de todo servidor. Ejemplo, se encarga de traducir 186.130.129.250 
a google.com 
URL (Uniform Resource Locator) --> Es la dirección que ingresamos en la web para referirnos a un sitio web, tambien se lo conoce como 
FQDN (Fully Qualified Domain Name)
NODES (Nodos) -------> Los nodos de red son puntos finales, comunicacion o puntos de redistribucion a travez de una red que pueden recibir,
almacenar y enviar datos a lo largo de rutas distribuidas

URL vs FQDN

FQDN (www.hackthebox.eu)
URL (https://www.hackthebox.eu/example?floor=2&office=dev&employee=16)

OSPF (Open Shortest Path First) ---> , Abrir el camino más corto primero en español, es un protocolo de red para encaminamiento jerárquico 
de pasarela interior o Interior Gateway Protocol, que usa el algoritmo Dijkstra, para calcular la ruta más corta entre dos nodos

SPOOFING ----> Suplantacion de identidad. Un atacante se hace pasar por una entidad distinta a travez de falsificación.

IP Phones ---> Teloefnos que usan internet para enviar y recibir data de voz.

!Flujo de internet: (Ej. al conectarse a una web como hackthebox)

Tenemos por un lado Dobliuws Network, representando al cliente y por otro Hacktheboxs Network. representando la compañia.

Nosotros conocemos la direccion de donde se tienen que enviar los paquetes (Direccion ip que se obtiene tras consultar al servicio DNS), pero no la geolocalizacion exacta.
Pero igualmente nuestros paquetes viajan a la ISP (Nuestro proveedor de servicio de internet).

Por lo tanto, cuando enviamos paquetes con nuestro router el paquete viaja hasta el ISP, esta buscan la direccion registrada en el servidor DNS que nos devuelve la direccion
IP con la geolocalizacion y ahora que sabemos la localizacion, nuestros paquetes se envian directamente. Una vez que  el web server recibe los paquetes, este lo envia
directamente al router de la compañia con la IP a la cual responder


                    
Dobliuw's Network  
(Home Network)              
       |
       V
     Router  (A travez de router se envian los paquetes con el destino "https://www.hackthebox.com")  
       |
       V
    Packages 
       |
       V
      ISP  (Los mismos son recibidos por el nuestro proveedor de internet)
       |
       V
      DNS  (El cual consulta al registro de dns cual es la geolocalizacion a la que tiene que enviar los paquetes
       |    si la direccion que se solicito es www.hackthebox, el cual la devuelve (IP)
       V
       IP  (Una vez obtenida la misma, los paquetes siguen su camino con este nuevo destino (IP))
       |
       V
    Web Server (Los cuales son recibidos por el servidor web)
       |
       V
    packages (El cual envía los mismos junto a la ip a la cual responder siendo esta la del sipositivo usado para consultar
       |     desde Dobliuw's Network)
       V
     router  (Son recibidos por el router de la empresa)
       |
       V
    Packages IP
       | 
       V
Hackthebox's Network   (La cual respondera con la solicitud realizada por Dobliuw's Network)
(Company Network)

!Puntos a tener en cuenta.

El Servidor Web deberia estar en una DMZ (Demilitarized Zone) porque los clientes de internet pueden inicializar 
comunicaciones con el sitio web haciendo que sea más probable que sea comprometido (Hablando de una red que se comunica con un 
switch que conecta a todos los dispositivos). De lo contrario, si se coloca en redes
separadas los administradores pueden colocar protercciones de red entre el servidor y los otros dispositivos.

La estacion de trabajo (Los dispositivos que se utilizan para trabajar) deberian estar en su propia red, a si como tener reglas de 
firewall basada en host que impida comunicarse con otras workstation, ya que si una workstation esta en la misma red que un servidor
los ataquesz de red como "man in the middle" o "spoofing" podrian ser mucho más graves

El Switch (Aparato que permite conectar multiples dispositivos) y el router deberian estar en una red de Administracion 
(Administration Network). Ya que esto evita que la/s workstation sufran de snooping en cualquier comunicación entre estos 
dispositivos. Muchas veces se ve en redes de compañias OSPF (Open Shortest Path First)

Los Telefonos IP deberian estar en la propia red para evitar que las computadoras puedan espiar comunicación. Además de la seguridad,
los teledonos son únicos en el sentido de que la latencia es significativa. Ubicarlos en la propia red puede permitir a los admins de red
priorizar si tráfico para evitar una alta latencia.

Las impresoras deberian estar en la propia red, ya que es casi imposible asegurar una impresora debido a como funciona windows. Si una 
impresora dice que se requiere autenticación durante un trabajo de impresión, la computadora intentará una auntenticación NTLMv2 
(New Technology LAN Manager ---> Hash que se genera en cada autenticación cliente/servidor) lo que puede provocar el robo de contraseñas
asi como tambien hay que tener en cuenta que las impresoras reciben muchas veces muchos documentos e información confidencial asi com tambien
sirven para ganar persistencia.

!NETWORK TYPES

Las redes pueden estar estructuradas de manera diferente y pueden ser configuradas individualmente. Por esto se llaman "types" o 
"topologies" se han desarrollado para que se pueda categorizar a las redes.

?TERMINOLOGIA COMUN

WAN (Wide Area Network) ------------------------> Internet
LAN (Local Area Network) -----------------------> Redes internas (Casa, oficina, etc)
WLAN (Wireless Local Area Network) -------------> Redes internas accesibles a travez de Wi-Fi
VPN (Virtual Private Netwrok) ------------------> Conecta multiples sitios de red a una LAN

!WAN (Wide Area Network):

Comunmente nos referimos a esto como "INTERNET". Cuando se trata de equipos de red, generalmente tendremos una direccion WAN y una LAN.
La WAN es la dirección con la que accedemos a internet. Una WAN es una gran cantidad de LAN unidas. Muchas empresas greandes o agencias 
gubernamentales tendrán una "WAN Interna" (A veces llamada Intranet, Airgap, etc). De manera general podemos identificar una red WAN por
usar protocolos de enrutamientos especificos como BGP (Border Gateway Protocol) y si el esquema IP no está dentro de RFC 1918
(10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 - Conexiones tipicas de redes privadas)

!LAN (Local Area Network) / WLAN (Wireless Local Area Network):

LANs y WLANs asignaran mayormente direcciones IP desiganas por un uso local RFC 1918 (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)
En algunos casos, como colegios o hoteles, es posible que se asigne una direccion IP enrutable (Internet) al unirse a su LAN, pero
esto es poco comúb. La unica diferencia entre LAN y WLAN es que estas introducen la capacidad de transmitir datos sin cables, principalmente
una designación de seguridad.

!VPN (Virtual Private Network)

Existen tres tipos principales de VPNs, pero las 3 tienen la misma meta, que es hace que el usuario sienta que esta en una red diferente.

- Site-To-Site VPN

El cliente y el servidor, ambos son Dispositivos de Red, (Mayormente tambien lo son los Routers y los Firewalls) y comparten rangos
de red completos. Esto se usa más comunmente para unir las redes de la empresa a través de internet, lo que permite que varias ubicaciones
se comuniquen a través de internet como si fueran locales.

- Remote Acces VPN

Esto implica que la computadora del cliente crea una interfaz virtual que se comporta como si estuviera en la red de un cliente. Hack The Box
utiliza OpenVPN que crea un "TUN Adapter" (Adaptador TUN) que permite al cliente acceder a los laboratorios. Una pieza importante de esta VPN
es la tabla de enrutamiento que se crea al unirse. Si la VPN solo crea rutas para resdes especificas, esto se denomina "Split-Tuenl VPN" 
(VPN de Tunel Dividido), lo que significa que la conexión a internet no sale de la VPN. De esta manera htb solo brinda acceso al laboratorio
sin la preocupación de privacidad de que puedan monitorear su conexión a internet.

- SSL VPN 

Esta es una VPN que se realiza esencialmente dentro de nuestro navegador web, por lo general estos transmitiran aplicaciones o sesiones de
escritorio completas al navegador. 

?TERMINOLOGIA DE LIBRO

GAN (Global Area Network) ----------------------> Red global (Internet)
MAN (Metropolitan Area Network) ----------------> Redes regional (Multiples LANs)
WPAN (Wireless Personal Area Network) ----------> Red personal (Bluetooh)

!GAN (Global Area Network):

Una red mundial como Internet se conoce como (GAN). Sin embargo internet no es la única red de estas. Las empresas activas internacionalmente
tambien mantienen aisladas que abarcan varias WAN y conectan las computadoras de empresa en todo el munod. Las GAN utilizan la 
infraestructura de vidrio e las redes de área amplia y las interconectan mediante cables submarinos internaciones o transmisión por satélite.

!MAN (Metropolitan Area Network):

Las redes metropolitanas son una red de telecomunicacionse de banda ancha que conecta varias lan en proximidad geografica, se trata de 
sucursales infividuales de una empresa conectadas a través de una MAN a traves de lineas alquiladas. Se usan enrutadores de alto rendimiento
y conexiones de alto rendimiento basadas en fibra de vidrio. Los operadores de red que operan internacionalmente proporcionan la infra
para las MAN. Las ciudades conectadas como redes de área metropolitana pueden integrarse suprarregionalmente en redes de área amplia (WAN) o
internacionalmente en redes de área global (GAN).

!PAN (Pesonal Area Network)/ WPAN (Wireless Personal Area Network):

Los dispositivos actuales como celulares, tablets, pc's, etc. se pueden conectar para formar una red que permita el intercambio de datos.
Esto se puede hacer por cable en dorma de red de area personal (PAN). La variante inalambrica (WPAN) se basa en tecnologias Bluetooh o USB
inalambrico. Una PAN y WPAN generalmente se extienden unos pocos metros y por lo tanto, no son adecuados para conectar dispositivos en 
habitaciones separadas o en edificios. En el contexto de IOT (Internet Of Things), las WPAN se utilizan para comunicar aplicaciones de control
y monitoreo con velocidades de datos bajas. Protocolos como "Insteon", "Z-Wave" y "ZigBee" se diseñaron explicitamente para hogares inteligentes.

!NETWORKING TOPOLOGIES

Las topologias de redes son arreglos fisicos a logicos de conexion de dispositivos en una red. Las computadoras son HOSTS, asi como los 
clientes y servidores que utlizan activamente la red. Tambien incluyen componentes de redes como "switches", "bridges" y "routers", que 
tienen la funcion de distribucion y aseguran que todos los hosts puedan establecer conexión logica entre si. La topologia de la red determina
los componentes a utilizar y los metodos de acceso a los medios de transmision.

Podemos dividir toda el area de topologia de la red en 3:

!1. CONEXIONES

Conexiones inalambricas             Conexiones de cableado 
Wi-Fi                               Cableado Coaxial
Celular                             Cableado de fibra de vidrio
Statelite                           Cableado de par trenzado
Otras                               Otros

!2. Nodos - NICs (Network Interface Controller)

Repeaters, Router/Modem, Hubs, Gateways, Bridges, Firewalls, Switches

?Repeater: Dispositivo que opera en el nivel fisico del modelo OSI, amplificando o regenerando las señales que llegan antes de retransmitirlas
-
?Router: Dispositivo encargado de manejar el trafico en tre las redes reenviando paquetes a direcciones IP y permitiendo que varios dispositivos
? utilicen la misma conexión a internet
-
?Hubs: Es un nodo que transmite datos a cada dispositivo basado en Ethernet conectado a el. Es menos sofisticado que un switch, estos son los
? mas adecuados para entornos de red LAN.
-
?Gateways: La tarea de esto es vincular redes realizando la traduccion entre diferentes protocolos y formatos de datos.
-
?Bridges: Dispositivo que crea una unica red agregada a partir de multiples redes de comunicacion o segmentos de red.
-
?Firewalls: Dispositivo de serguridad de redes que filtra el trafico de red entrante y saliente basado en las politicas de privacidad establecidas
? previamente. Es una barrera entre una red privada y el internet publico.
-
?Switches: Dispositivo que conecta dispositivos a la red y usa la conmutacion de paquetes para enviar recibir o reenviar paquetes de datos a 
? tramas de datos a través de la red. 

Los nodos de la red son puntos de conexion del medio de transmision a los transmisores y receptores de señales electricas, opticas o de 
radio en el medio. Un nodo puede estar conectado a un host, pero ciertos tipos pueden tener solo un microcontrolador en un nodo o pueden no 
tener ningun dispositivo programable.

!3. CLASIFICACIONES

Podemos imaginarnos una TOPOLOGY como una estructura de una red. Estas pueden ser fisicas o logicas, por ejemplo computadoras en una red
LAN pueden organizarse en un círculo en un dormitorio, pero es muy poco probable que tenga una topologia de anillo real...

Las topologias de red se dividen en los siguientes ocho tipos:

Point-to-Point
Bus
Star
Ring
Mesh
Tree
Hybrid
Daisy Chain

Se pueden crear redes más complejas pero tienen que crearse como hibridos de las topologias mencionadas anteriormente.

!Point-to-Point

La topologia de red más simple con una conexion dedicada entre dos host es un point-to-point. En esta topologia solo existe un enlace 
fisico y directo entre ellos. Estos dos dispositivos pueden utilizar estas conexiones para la comunicacion mutua. Esta es distinta a 
P2P (Peer-To-Peer)

.____                                      ____
[____] ---------------------------------- [____]
HOST A                                    HOST B


!Bus

En esta topologia todos los host estan conectados via de un medio de transmision en la topologia de bus. Cada host tiene acceso al medio 
de transmision y las señales que se transmiten a través de él. No hay componente de red central que controle los procesos en él. El medio de 
transmicion para esto puede ser por ejemplo, un cable coaxial.
Dado que el medio se comparte con todos los demás, solo un host puede enviar, y todos los demás solo pueden recibir y evaluar los datos y ver
si estan destinados a si mismos.

.____                                 _____                                    ____
[____]                               [_____]                                  [____]
HOST A                                HOST C                                  HOST E
  |                                     |                                        |
  |_____________________________________|________________________________________|
  |                                     |                                        |
._|__                                 __|__                                    __|__                                  
[____]                               [_____]                                  [_____]
HOST B                               HOST D                                   HOST F


!Star

La topologia en estrellas es un componente de red que mantiene una conexion con todos los hosts. Cada host esta conectado al componente de 
red central a traves de un enlace separado. Suele ser un router, un hub o un switch. Estos manejan la funcion de reenvio de los paquetes de
datos. El trafico en el componente de red central puede ser muy alto ya que todos los datos y conexione spasan por el

                              ._____
                              [_____]
                              HOST B
                                 |
                                 |
                                 |
                                 |
                                 |
                                 |
.____                          __|__                          ____
[____] -----------------------[_____]----------------------- [____]
HOST A                        ROUTER                          HOST C
                                 |
                                 |
                                 |
                                 |
                                 |
                                 |
                               __|__
                              [_____]
                              HOST D


!Ring

La topologia de anillo fisico es tal que cada host o nodo esta conectado al anillo con dos cables

- Uno para las señales entrantes
- Otro para las señales salientes

Esto significa que llega an cable a cada host y sale un cable. La topologia en anillo normalmente no requiere un componente de red activo.
El control de acceso al medio esta controlado por un protocolo al que se adhiere todas las estaciones (hosts, clientes).
Una topologia anillo logica se basa en una topologia de estrella fisica, donde un distribuidor en el nodo simula el anillo reenviando de 
un puerto al sig. La info se transmite en una direccion de transmision predeterminada. Por lo general se accede secuencialmente al medio de 
trasmision se una estacion a otra utilizando un sistema de recuperacion desde la estacion central o un toke (Patron de bits que pasa continuamente
a traves de una red en anillo en una direccion, que funciona de acuerdo con el proceso del toke de reclamacion)

                                          .______
                                     _____[______]_____
                                   /       HOST B      \
                                  /                     \
                                 /                       \
                            .___/__                     __\___
                            [______]                   [______] 
                             HOST A                     HOST C
                                \                         /
                                 \                       /
                                  \       .______       /
                                   \ _____[______]_____/
                                           HOST D


!Mesh


"""   
