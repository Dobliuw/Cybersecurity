"""
Para cambiar la dirección mac

?$ ifconfig {interfaz} down 

Esto porque siempre hay que bajar la interfaz a la que le queremos realizar un cambio

?$ ifconfig {interfaz} hw ether {new_mac}

Esto para hacer un cambio en el hardware (hw) 

?$ ifconfig {interfaz} up 

Cuando se interactua en internet constantemente se estan enviando paquetes

source mac: 00:11:22:33:44
destination mac: 00:11:12:23:44

los cuales pueden ser capturados con un adaptador wifi con modo monitor siempre y cuando la red
no tenga cifrado, en caso de tenerlo (sea WPA/WPA2) vamos a tener que formar parte a esa red para poder
ver dichos paquetes

Poner el adaptador en modo monitor:

?$ airmon-ng {interfaz} start

o

?$ iwconfig {interfaz} mode monitor

Para poder interceptar o capturar los paquetes alrededor, vamos a usar la sweet Airodump-ng que pertenece
a la sweet de aircrack-ng

?$ airodump-ng {interfaz_en_modo_monitor}

De esta manera veriamos algo similar a esto 

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


!BANDAS WIFI

a ---> 5 Ghz
b,g ---> 2.4 Ghz
n ----> 5 Ghz y 2.4 Ghz
ac ----> < 6 Ghz

Poder buscar en base a bandas

?$ airodump-ng --band abg {interfaz_monitor}

Escanear una red en particular

?$ airodump-ng --bssid {bssid} --channel {CH} --write {file_name} {interfaz}

Esto para escanear la red ingresada en el bssid en el canal que se encuentra, y todo el trafico alojarlo y
escribirlo en el file ingresado


"""