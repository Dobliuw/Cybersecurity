
"""
TCP/IP ----> Define como se mueve la info desde el remitente hasta el destinatario. 

Este protoclo cuenta con capas las cuales son 

Capa de aplicación ------------> aplicación
Capa de transporte ------------> UDP - TCP
Capa de red -------------------> Protocolo internet
Capa de interfaz de red -------> Interfaz de red
Hardware ----------------------> Red fisica

Los programas de apps en primer lugar envian mensajes o corrientes de datos a uno de los protocolos de la capa de transporte de
Internet (UDP - User Datagram Protocol o TCP - transmission Control Protocol). Estos se encargan de recibir los datos y 
transformarlos en paquetes con direccion de destino y se pasan a la sig capa, red de internet.

Esta capa pone el paquete en un datagrama de IP (Internet Protocol), pone la cabecera y la cola de datagrama, decide donde eviar
el datagrama (directamente a un destiono o a una pasarela) y pasa el datagrama a la capa de interfaz de red.

*Datagrama ---> Unidad de transferencia básica asociada acon una red de conmutaciópn de paquetes. Suelen estar estructurados 
*con una sección de cabecera y carga util.

En esta capa de red, se acepta los datagramas IP y se los transmite como *tramas* a través de un hardware de red especifico, 
por ejemplo redes ethernet o de red en anillo.


-----------------------------------------------------

DNS -------> Domain Name System
Este sistema es un sistema de nomencaltura jrárquico descentralizado para dispositivos conectados a redes IP. 
Asocia información variada con nombres. Ejemplo 31.13.94.35 ----> facebook.com 
Esto podemos verlo con la herramienta nslookup al dominio o haciendole un ping tambien al dominio

-----------------------------------------------------

DHCP ---->  Dynamic Host Configuration Protocol.
Se usa para asignar dirección IP y configuraciones de red automaticamente.
Router's default IP address (192.168.1.1 or 192.168.0.1)

-----------------------------------------------------

PSK ---> (Pre Shared Key) Clave Pre-Compartida. Cualquiera que la tenga se puede conectar al acceso (wifi)

-----------------------------------------------------

NetMask --> (Mascara de red) Se utiliza para dividir una dirección IP en dos partes. La dirección de red y 
la dirección de host.
La dirección de red es a la que pertenece un dispositvio mientras que la dirección host identifica de manera
unica a ese dispositivo dentro de la red.
La notación de netmask es una serie de numeros separados por puntos como 255.255.255.0, los números 255 indican los bits de la 
dirección IP que forman parte de la dirección de la red, mientras que los números 0 indican los bits que forman parte 
de la dirección de host. 

Ejemplo: 255.255.255.128. En este ejemplo los 25 primeros bits indican que forman parte de la derección de red, mientras que los 
ultimos 7 bits forman parte de la dirección de host. Indicando que solo hay 128 posibles direcciones de host disponibles dentro
de esa red.

-----------------------------------------------------

Interfaz de red "lo" ---> interfaz de loopbuck creada para poder enviar y recibir paquetes de red a si mismo para realizar pruebas
y para comunicarse consigo mismo en una maquina local.


"""
