"""
Los archivos binarios son archivos normales que contienen información que el sistema puede leer. Los archivos binarios
podrían ser archivos ejecutables que indicaran al sistema que ha de realizar un trabajo. Los mandatos y los programas 
se almacenan en archivos binarios ejecutables.

? $whoami --> user 
? $id --> grupos a los que pertenece el user
Si el usuario pertenece al grupo sudo, tiene el privilegio de convertirse en root
?$ sudo su ---> entrar en modo root
?$ exit ---> salir de la seción de root

?$ cat /etc/group

?$ pwd ---> path

?$ which "name" or command -v ---> para saber la ruta absoluta de un comando | el binario de un programa

?$ whereis "name" ---> bucar el manual binario, fuente y de usuario de un programa

?$ find "path" -inam "name" ----> Buscar archivos y dirs por nombres

?$ kill %%  ----> Matar cosas en segundo plano

ruta absoluta ---> /usr/bin/whoami

ruta relativa ---> whoami

Porque un comando como whoami que se encuentra en un directorio se puede ejecutar sin aclarar la ruta absoluta?
Porque existe una variable de entorno $PATH ($ para ver el contenido): 
De izquierda a derecha se van a probar los paths:

/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games

El path se puede retocar.

| <-- pip, para "pipear", es decir, trabajar el output del comando previo

?$ grep --> aplicar filtro 

?$ grep -i  | grep -E  |    grep -o   | grep "^togrep$" -n
Insensitive | + 2 args | solo lo grep | que empieze y finalize , ver la línea

?$ cat /etc/group | grep "floppy" 

?$ alias name="command"  ---> para crear un alias de un comando

?$ source "name" ----> obtener un archivo

?$ cd -    ---> moverse al ultimo directorio en el que4 estaba

?$ uname -a  ---> ver informacion del sistema

?$ ls -a ---> incluir archivos ocultos    
?$ ls -l ---> formato de lista larga
?$ ls -lh --> formato legible por humanos
?$ ls -lah --> formato legible por humanos + archivos ocultos

?$ man ---> obtener informacion sobre un comando
 
?$ history ---> lista completa de comandos usados

?$ history "number" ---> lista reducida hasta el numero ingresado de comandos

?$ vim "name" ---> crear con editor de texto de consola un archivo

?$ touch ----> crear archivo

?$ mkdir ---> crear dir

?$ mv path path2 ----> mover archivo
?$ mv name name2 ----> editar name archivo

?$ nano name --> crear un archivo como con touch pero con la opción de crear el contenido en el momento

?$ cp archivo name ---> crear un nuevo archivo con la copia de otro

?$ rm -r name ---> borrar algo, flag r para que sea de forma recursiva, y para que no pregunte si queremos o no flag f rm -rf

?$ | more ----> para cuando un output es muy largo, poder escrolear con el enter

?$ ln -f -s {archivoa} {archivob}  ---> hacer enlace simbolico forzado de un archivo a otro

?$ ps --> process system

?$ ps -faux --> listar todos los procesos del sistema con full-format (-f), nombre o euid de user (-u), excepto procesos no asociados a la terminal y de ambos session leaders

?$ du -hc {file_name} --> Listar el peso de un archivo

?$ xrandr --> configurar salidas de video

?$ pactl ---> configurar salidas de audio 

?$ dpkg-reconfigure locales  ---> cambiar idioma del sistema

?$ crontab -e / -l  ---> editar las tareas cron del usuario / leer las tareas cron del usuario

pipelines o tuberias son la ejecución de varios comandos en una linea
Por ejemplo

?$ cat /etc/group | grep "root" -n | cat > newFileAboutGroup.txt

* CTRL + L ---> clear
* CTRL + R ---> para buscar comando
* CTRL + P ---> pegar lineas anteriores (o cambiar interfaz)
* CTRL + A ---> Mover el cursor al principio de la línea
* CTRL + U ---> Borrar la línea completa
* CTRL + E ---> Ir al principio de la linea
* CTRL + W ---> Borrar la ultima palabra escrita

?$ echo $HOME <---- Variable de entorno que indica dir personal de usuario

?$ cat /etc/passwd <--- Archivo que indicausuarios exitentes "name":x:"userId":"GroupId":"name":"pathEntornoPersonal":"tipoDeShell"

?$ echo #SHELL <--- Variable de entorno de shell que estas usando

?$ cat /etc/shells  <--- Archivo que indica las shells existentes, como se encuentran en la Variable de entrono $PATH podemos
?$ llamarla con bash, etc

; <--- para separar comandos

whoami; ls

&& <--- se ejecuta solo el sig si el anterior commando es exitoso

?$ echo $? <----- si es 0, ejecución previa exitosa, si no, no

|| <--- ejecuta el primero que de exitoso


!stderr-stdout, operadores, redirectores y procesos en segundo plano

stderr  <--- es como se define el error, de un comando fallido, etc y se puede representar como 2 (o estandar error)
stdout <--- outputs

> <--- redirectores 

?$  whoam 2>/dev/null     (los errores los quiero redirigir al devnull, devnull es un dir que seria un "agujero negro")

Redirigir outputs

cat /etc/hosts > dev/null    *Esto no daria resultado en consola ya que todo el stdout esta siendo redirigido al devnull

cat /etc/host > dev/null   *Mostraria un error en consola porque el stderr no forma parte del stdout

cat /etc/host > dev/null 2>&1    *Tampoco mostraria el error porq el stderr || 2 esta siendo redirigido o mejor dicho, el 
                                  stderr convertido a stout para que se redirija al devnull

cat /etc/host &>/dev/null     *Lo mismo que arriba, ni el stout ni el stderr se verian 

Porque? 

Existen programas o herramientas como wireshark se ejecutan y manda stout lo que se puede volver molesto

Asi mismo, podriamos ver que quedaria en escucha la consola, ya que la misma tiene la ejecución hija la cual queda corriendo
lo que podemos hacer es agregar un & al final para correrlo en segundo plano y devuelve el pid (n identificativo del proceso)

Esto lo que hace es que igualmente, no deja de ser un proceso hijo, por lo que si bien podriamos ejecutar más comandos, todavia
no podriamos separar y hacer que la ejecución no depende de la shell. Incluso no nos dejaria cerrar la consola.

La solución seria ademas de agregar el & un disown de manera que quede & disown para que el proceso quede corriendo en segundo
plano sin que este dependiendo de la shell.

?$ code-oss & disown

Redireccionar con > va a sobrescribir las cosas, para que haga un append seria >>

! Descriptores de archivos

Es una clave a una estructura de datos que reside en el núcleo, que contiene detalles de todos los archivos abiertos.
Una "construccion especial que apunta a un canal a un archivo", ya sea para leer, escribir o ambos.
Esto viene de la antigua filosofía de UNIX de tratar todo como un archivo, ¿quieres escribir en un dispositivo?, trátalo 
como un archivo, ¿quieres escribir en un socket y enviar datos a través de una red?, trátalo como un archivo, ¿quieres leer
y escribir en un archivo?, bueno... obviamente, tráta como un archivo. Por lo tanto, al administrar dónde van los resultados
y los errores de un comando, ese mismo destino lo estamos tratando como un archivo.

exec ---> permite manipular a los descriptores de archivo de shell en ejecuccion. Usado en el interior de un script
permite redirigir de manera global entradas/salidas del mismo.

?$ exec 3<> file

<   <--- Para lecutra >  para escritura

?$  file   <--- detectar tipo de archivo

Estamos usando un descriptor de archivo identificado con el numero 3

?$  whoami >&3    <--- enviar el output al descriptor del archivo

Para cerrar el descriptor del archivo   excec 3>&-

Tambien puedo crear copias entre descriptores de archivos

exec 8>&5     <--- Lo que hay en el descriptor de archivos 5 quiero crear una copia para el 8 que estoy creando ahora

Como el 8 es una copia, lo que meta en el 8 tambien lo voy a tener en el 5

exec 5<> example

exec 6>&5-     creo la copia a la par que cierro el orginal


! Lectura e interpretación de permisos

.rw-r--r-- k0v4ks k0v4ks ----> Grupo
|            |
|            V
|        Propietario    
V
El punto en lugar de un d, es porque no es un directorio

Se divide en 3

        .rw-        |          r--          |       r--

Permiso Porpietario | Permiso de los grupos | Permiso de otros

No siempre se asigna el grupo default que es igual al propietario.

* Rwx
*R ead ---> Lectura
*W rite ---> Escritura
*X ecute ---> Si esta en un dir, el que corresponda se puede meter, si es un archivo, es que se puede ejecutar


! Asignación de permisos

chmod ---> cambiar permisos

sin flag  o la u para el propietario
g para el grupo 
o para otros

Por ejemplo partiendo del archivo example.txt

Si quisieramos darle permisos de edición, lectura y ejecución al propietario, y ningun permiso al grupo y  otros

chmod 700 example.txt
o 
chmod +rwx example.txt
chmod g-rwx example.txt; chmod o-rwx example.txt

chgrp ---> cambiar el grupo
?$ chgrp k0v4ks name
chown ---> cambiar propietario
?$ chown k0v4ks name
Y tambien se puede cambiar ambas a la vez de la sig manera
?$ chown username:group name

?$ chmod u-x,g-rx,o+w,o-x

?$ useradd name -s /bin/bash -d /home/name
Para agregar un usuario a nivel de sistema, con la flag -s para asignar una shell y -d un directorio personal
?$ userdel name 
Para eliminar al usuario



?$ passwd name 
Para asignar una contraseña

?$ groupadd newGroup
Para agregar un nuevo grupo

?$ usermod -a -G newGroup username

! Notación octal de permisos:

Con directrices
0 = ---
1 = --x
2 = -w-
3 = -wx
4 = r--
5 = r-x
6 = rw-
7 = rwx

Estos números no es necesario de saberlos de memoria, simplemente es la sumatoria de lo sig:

r w -  |  r - - | - - -  

Donde haya un permiso sera un 1, y donde no lo haya un 0

r w -  |  r - - | - - -  
1 1 0  |  1 0 0 | 0 0 0 

Y ahora una simple suma de combersión binaria:

r w -  |  r - - | - - -  
1 1 0  |  1 0 0 | 0 0 0 
<
Si hay un 0 no lo sumamos 

r w -  = 1 1 0 = 2¹ + 2² (siempre elevamos el 2 a las posiciones) = 6

r - -  = 1 0 0 = 2² = 4

- - - = 0 0 0 = 0

Otro ejemplo:

r w x | r - x | r - -
1 1 1 | 1 0 1 | 1 0 0 

r w x = 1 1 1 = 2⁰ + 2¹ + 2² = 1 + 2 + 4 = 7 
r - x = 1 0 1 = 2⁰ + 2² = 1 + 4 = 5
r - - = 1 0 0 = 2² = 4

!Sticky Bit ---> Permisos especiales

El sticky bit aplicado a un directorio es un permiso especial que hace que solamente el propietario de 
un archivo contenido en el mismo (o root) puedan borrarlo.


Supongamos que tenemos un dir "notConfidential" en donde con el comando

?$ chmod 777 notConfidential

le damos permisos a otros de poder realizar cambios, borrar, etc.
Dentro del mismo creamos un archivo

?$ echo "hola probando" > test.txt

si vemos los permisos de este 

?$ ls -l 

Veremos que son ---> rw-r--r--

Por lo que con "otros" no se podria hacer nada más que leer...no?
Bueno, no, si nos cambiamos de usuarios e intentamos eliminar el archivo nos preguntara si se quiere
borrar el archivo protegido contra escritura, damos que s y se podra borrar, ya que la carpeta contenedora
permite edición de lo contenido.
Aca es donde entra en juego el sticky bit
A la carpeta contenedora le podriamos dar 

?$ chmod +t notConfidential
?$ chmod 1xxx notConfidential

Le metimos el sticky bit y no podremos eliminar lo contenido

! Control de atributos de ficheros. Chattr y Lsattr

lsattr ----> listar permisos avanzados 

lsattr -R ----> flag R ls de forma recursiva


chattr +i -V name ----> convertir en inmutable (+i) y ver de forma descriptiva lo que esta pasando (- Verbose)

chattr -i -V name ---> sacar el inmutable

chattr +A ----> cuando se acceda al fichero no se modifique el registro atime (de este modo no queda registrada la fecha del último)
chattr +c ----> que el ficher se comprima automaticamente en el disco por el kerne, cuando se lea se servira descomprimido
chattr +i ----> inmutable
chattr +u ----> para que cuando se borre, sus datos permanezcan guardados y permitan al usuario su recuperación

! Permisos especiales SUID y SGID

?$ chmod u+s /usr/bin/python3.9
?$ chmod 4755 /usr/bin/python3.9
SUID ---> chmod u+s binario 
SUID ---> chmod 4755 binario

?$  wich python3.9 | xargs ls -l
El wich nos devuelve la ubicacion del binario y en forma paralela (xargs) tratamos el output con un ls -l

Permisos de python en este ejemplo ---> rwxsr-xr-x

?$  find / -type f -perm -4000
Find para descrubrir files(archivos) desde la raiz los que tengan el privilegio de 4 (SUID)
Aca saldrian todos los binarios con permiso especial SUID

Cuando un binario sea SUID, sea cualquier usuario voy a poder ejecutar el mismo de forma temporal como el propietario

Entre ellos python, con el que podria
importar el repositorio os y empeza

import os 
os.setuid(0) ------> 0 = root 
os.system("whoami") ----> root
os.system("id")
os.system("bash")
os.system("zsh")


Si tuvieramos un archivo con permisos especiales SUID y el mismo puede ejecutar un comando, rapidamente pensariamos en pedir
una bash y poder operar de la misma con los prvilegios del propietario, pero para que esto funcione deberiamos usar la flag -p
o ejecutar una sh

SGID es lo mismo pero para los grupos 

?$ chmod g+s /usr/bin/python3.9
?$ chmod 2755 /usr/bin/python3.9

?$ find / -perm -2000

Permisos de python en este ejmplo: rwxr-sr-x

! CAPABILITIES:

*Capacidad/privilegio de un binario de ejecutar tareas

?$ getcap -r / 2>/dev/null
Para listar desde la raiz de forma recursiva y mandando los errores al null las capabilities de los archivos
que podean alguna

?$ setcap cap_setuid+ep {binario}
Setear una capabilitie (en este caso la de poder setear la id) a un binario

?$ getcap !$   
El !$ lo que hace es devolver lo ultimo escrito en el comando previo

?$ setcap -r {binario}

! ESTRUCTURA DE DIRECTORIOS DEL SISTEMA

(en la raiz):

KERNEL: Núcelo del sistema operativo

*bin ---> Dir estatico donde se almacenan los binarios necesarios para garantizar funciones necesarias a nivel USUARIO 

*boot ---> Dir estatico donde se almacenan todos los ejecutables y archivos que son usados en el proceso
* para el inicio del sistema

*dev ---> Dir incluye dispositivos de almacenamiento en forma de archivo (disco duro, usb, particion, etc) 
* mientras que el sistema puede entender a este como un volumen logico de almacenamiento

*etc ----> Dir encargado de almacenar archivos de configuracion a nivel de componentes del sistema operativo como apps y programas
* instalados despues ---> solo deberia haber archivos de configuración y no de bin
 
*home ---> Dir de user estandar --> lo que instale y demás y tambien incluye archivos temporales de apss ejecutadas de modo 
* usuario que sirven para guardar las configuraciones de programas etc

*lib ---> Dir que incluye bibliotecas escenciales necesarias para ejecutar todos los bins de bin y sbin, asi como los modulos 
* del kernel, en los sistemas operaticos x64, existe otro dir "lib64" para las bibliotecas de apps de 64 bits 

*media ---> Dir que representa el punto de montaje de todos los volumenes logicos que se montan temporalmente (sub, otras 
* particiones de disco, etc)

*opt ---> Dir que seria una "extensión" del dir usr pero van todos los archivos de solo lectura que son parte de programas 
* autocontenido 
 
*proc ----> Dir que contiene info de los procesos y apps que se estan ejecutando en un momento determinado en el sistema, se 
*almacenan arhivos virtuales ---> contenido null

*root --> Dir "home" pero del root 

*sbin ---> Dir estatico donde se almacenan los binarios para tareas de super usuario y sistema operativo, pero solo por el u root

*srv ---> Dir que sirve para almacenar archivos y dir relativos a servidores instalados dentro del sistema, http, ftp

*sys ---> Dir que al igual que el /proc pero que contiene archivos virtuales que proveen info del kernel relativa a eventos del
*sistema
 
*tmp ---> Dir para almacenar archivos temporales a nivel sistema y usuario
 
*usr ---> Dir que su nombre viene de "user system resources" y sirve para almacenar archivos de solo lecutar y relativos a las 
* utilidades del usuario incluso el software instalado a travez de gestores de paquetes, contiene subdirectorios: (bin, include,
* lib, lib32, lib64, local, sbin, share, src)
 
*var ---> Dir que contiene archivos con info del sistema, archivos de logs, emails de los users del sistema, base de datos, 
* info en la cache, como decir "archivo que contienen un registro del sistema"

# *Directorio Raíz

# El directorio raíz, simbolizado por el símbolo (/), es el directorio principal a partir del cual se ramifican todo el resto de 
# directorios.

#* Directorio /bin
# El directorio /bin es un directorio estático y compartible en el que se almacenan archivos binarios/ejecutables necesarios para
# el funcionamiento del sistema. Estos archivos binarios los pueden usar la totalidad de usuarios del sistema operativo.

#* Directorio /boot
# Es un directorio estático no compartible que contiene la totalidad de archivos necesarios para el arranque del ordenador excepto 
# archivos de configuración. Algunos de los archivos indispensables para el arranque del sistema que acostumbra a almacenar el 
# directorio /boot son el kernel y el gestor de arranque Grub.

# *Directorio /dev
# El sistema operativo Gnu-Linux trata los dispositivos de hardware como si fueran un archivo. Estos archivos que representan 
# nuestros dispositivos de hardware se hallan almacenados en el directorio /dev.

# Algunos de los archivos básicos que podemos encontrar en este directorio son:

#     cdrom que representa nuestro dispositivo de CDROM.
#     sda que representa nuestro disco duro sata.
#     audio que representa nuestra tarjeta de sonido.
#     psaux que representa el puerto PS/2.
#     lpx que representa nuestra impresora.
#     fd0 que representa nuestra disquetera.

# *Directorio /etc
# El directorio /etc es un directorio estático que contiene los archivos de configuración del sistema operativo. 
# Este directorio también contiene archivos de configuración para controlar el funcionamiento de diversos programas.

# Algunos de los archivos de configuración de la carpeta /etc pueden ser sustituidos o complementados por archivos de 
# configuración ubicados en nuestra carpeta personal /home.

# *Directorio /home
# El directorio /home se trata de un directorio variable y compartible. Este directorio está destinado a alojar la totalidad
#  de archivos personales de los distintos usuarios del sistema operativo a excepción del usuario root. Algunos de los archivos 
# personales almacenados en la carpeta /home son fotografías, documentos de ofimática, vídeos, etc.

# *Directorio /lib
# El directorio /lib es un directorio estático y que puede ser compartible. Este directorio contiene bibliotecas compartidas
#  que son necesarias para arrancar los ejecutables que se almacenan en los directorios /bin y /sbin.

# *Directorio /mnt
# El directorio /mnt tiene la finalidad de albergar los puntos de montaje de los distintos dispositivos de almacenamiento como 
# por ejemplo discos duros externos, particiones de unidades externas, etc.

# *Directorio /media
# La función del directorio /media es similar a la del directorio /mnt. Este directorio contiene los puntos de montaje de los 
# medios extraíbles de almacenamiento como por ejemplo memorias USB, lectores de CD-ROM, unidades de disquete, etc.

# *Directorio /opt
# El contenido almacenado en el directorio /opt es estático y compartible. La función de este directorio es almacenar programas
#  que no vienen con nuestro sistema operativo como por ejemplo Spotify, Google-earth, Google Chrome, Teamviewer, etc.

# *Directorio /proc
# El directorio /proc se trata de un sistema de archivos virtual. Este sistema de archivos virtual nos proporciona información 
# acerca de los distintos procesos y aplicaciones que se están ejecutando en nuestro sistema operativo.

# *Directorio /root
# El directorio /root se trata de un directorio variable no compartible. El directorio /root es el directorio /home del 
# administrador del sistema (usuario root).

# *Directorio /sbin
# El directorio /sbin se trata de un directorio estático y compartible. Su función es similar al directorio /bin, pero a 
# diferencia del directorio /bin, el directorio /sbin almacena archivos binarios/ejecutables que solo puede ejecutar el usuario 
# root o administrador del sistema.

# *Directorio /srv
# El directorio /srv se usa para almacenar directorios y datos que usan ciertos servidores que podamos tener instalados en
#  nuestro ordenador.

# *Directorio /tmp
# El directorio /tmp es donde se crean y se almacenan los archivos temporales y las variables para que los programas puedan 
# funcionar de forma adecuada.

# *Directorio /usr
# El directorio /usr es un directorio compartido y estático. Este directorio es el que contiene la gran mayoría de programas 
# instalados en nuestro sistema operativo.

# Todo el contenido almacenado en la carpeta /usr es accesible para todos los usuarios y su contenido es solo de lectura.

# *Directorio /var
# El directorio /var contiene archivos de datos variables y temporales como por ejemplo los registros del sistema (logs), los
#  registros de programas que tenemos instalados en el sistema operativo, archivos spool, etc.

# La principal función del directorio /var es la detectar problemas y solucionarlos. Se recomienda ubicar el directorio /var 
# en una partición propia, y en caso de no ser posible es recomendable ubicarlo fuera de la partición raíz.

# *Directorio /sys
# Directorio que contiene información similar a la del directorio /proc. Dentro de esta carpeta podemos encontrar información 
# estructurada y jerárquica acerca del kernel de nuestro equipo, de nuestras particiones y sistemas de archivo, de nuestros 
# drivers, etc.

# *Directorio /lost-found
# Directorio que se crea en las particiones de disco con un sistema de archivos ext después ejecutar herramientas para restaurar 
# y recuperar el sistema operativo como por ejemplo fsch.

! Bashrc y zshrc

?$ ls -la <-- a permite detectar archivos ocultos (. al principio)

Archivo de configuracion (si usas zsh el archivo de zshrc, si usas bash bashrc)

?$ nano zshrc ---> para poder crear funciones en tu shell 

awk '{print $1}'---> printear argumentos seleccionado parametros 

Ejemplo:

?$ hostname -I 

192.168.1.38 2802:8010:4967:700:4c31:791:da20:92d3 2802:8010:4967:700:6d9:f5ff:fe8a:863f 

?$ hostname -I | awk '{print $1}'

192.168.1.38

O cut

?$ hostname -I | cut " " -f 1 ---> cortar por un espacio y quedarme con el (fild) campo 1 

----

?$ echo "Tu IP privada es: $(hostname -I | cut " " -f 1)"

~/.zshrc  ---> ~/. para ir al dir personal de tu usuario "home/user"

! Upgrade y update

?$ apt update
Actualizar sistema porque puede ser que haya paquetes con actualizaciones pero algunos no seran actualizados

?$ apt upgrade ----> Upgrade del sistema y todos los paquetes

! TMUX

tmux new -s {name}

CTRL + 1, 2, 3 ---> Pestañas

CTRL + B --> PREFIX KEY

CTRL + B --> , ---> Poder renombrar una ventana 

CTRL + B --> C ---> Crear ventana nueva

CTRL + BM ---> Mouse 

CTRL + B ---> SHIFT 2 ---> Splitear ventanas 

CTRL + B O ---> Alternar ventanas

exit ----> salir de 1 ventana

CTRL + B ---> X ---> y

Renombrar sesion CTRL + B  --> $ (SHIFT + 4)

esplitar de forma vertical ---> CTRL + B --> % (SHIFT + 5)

CTRL + B --> M ---> Cambiar size

CTRL + B ---> CTRL + -> || <- 

*MODO COPIA

CTRL + B ---->  ALTGR + [ ---> Puedo moverme por las lineas con las flechas
CTRL + space -----> Puedo irme para la derecha abajo y copiar 
tecla fin para hasta el final de la linea
ALT + W
CTRL + B
ALTGR + ] ---> Pegar 

CTRL B ---> D (dteached) --> en segundo plano

?$ tmux list-sessions ---> listar sesiones 

si es una

?$ tmux attach

?$ tmux attach -t {name}

Con más de una sesion --> CTRL + B --> W ---> Ver las sesiones --> Enter para migrar


! Kitty

comando = CTRL + SHIFT 

comando + enter ---> nueva pestaña
comando + b ---> mandar para abajo la pestaña actual
comando + f ----> mandar para arriba la pestaña actual
comando + l ----> diferentes formatos para organizar 
comando + w ---> cerrar pestaña 
comando + 1, 2 ----> cambiar de pestaña
comando + alt + t ---> renombrar area de trabajo
comando + t ----> nueva ventana 
comando alt + t ----> renombrar esta area
comando + izq | der
comando + r ----> ajustar size
comando + , ---> mover marco de trabajo a la izquierda
comando + . ----> mover marco de trabajo a la izquierda
comando + c ---> copiar
comando + z ----> zoom a ventana de trabajo

?$ kitty +kitten icat {image_name} 
Para ver una imagen en consola

Si no,

?$ display {image_name}


! Busqueda a nivel de sistema 

?$ find / -name passwd 2>/dev/null | xargs ls -l
Buscar desde la raiz de forma recursiva donde el nombre sea passwd enviando el stderr al null y en forma paralela listar los
permisos especiales

?$ find / -perm -4000 2>/dev/null
Buscar desde la raiz de forma recursiva archivos con permiso SUID 

?$ find / -type d -group k0v4ks -perm -4000 2>/dev/null
Buscar desde la raiz de forma recursiva directorios con grupo k0v4ks y permisos SUID

?$ find / -user root -writeble 2>/dev/null
Buscar de forma recursiva desde la raiz archivos del usuario root que sean editables

?$ find / -user root -executable -type f 2>/dev/null
Buscar desde la raiz de forma recursiva archivos del usuario root que sean ejecutables

?$ find / -name dex\* 2>/dev/null
Buscar desde la raiz de forma recursiva archivos que empiezen con dex

?$ find / -name \*exdum\* 2>/dev/null
Buscar desde la raiz de forma recursiva archivos que contengan la palabra exdum 

?$ find / -name dex\*.sh 2>/dev/null
Buscar desde la raiz de forma recursiva archivos que empiezen con dex y terminen con .sh

?$ find / -name dex\*.sh -ls 2>/dev/null
Buscar desde la raiz de forma recursiva archivos que empiezen con dex y terminen con .sh a la vez que 
muestre los permisos avanzados

?$ find / -type d -perm -1000 -group root 2>/dev/null 
Buscar desde la raiz de forma recursiva directorios con permisos especiales Sticky Bit y que pertenezcan 
al grupo root

! Scripts en bash 

Ejecutar serie de comandos de bash en script

#!bin/bash

echo "Tu ip priv es: $(ip a | grep "eth0" | tail -n 1 | awk '{print $2})' | cut -d '/' -f 1


ip a | grep "eth0" | tail -n 1 | awk '{print $2}' | awk '{print $1}' FS="/"


ip a | grep "eth0" | tail -n 1 | awk '{print $2}' | tr '/' ' ' | awk '{print $1}


! Edito vim

alt + u = ctrl + z
0 ---> principio 
$ ---> fin
por palabras ---> w
3 + w ---> 3 palabras
d + w ---> eliminar palabra
3 + d + w ---> eliminar 3 palabras
d + d ---> eliminar linea
2 + d + d ---> eliminar 2 lineas
alt + v ---> modo visual
con una seleccion ---> y ----> copiar
p ---> pegar
o --> nueva linea 
j + 0 + .
bajar, ir al inicio y repetir lo ultimo hecho

macros ----> alt + q --> + {a} ---> recording ---> registro de pulsaciones ---> q ---> guardar
alt --> num + @ + {a}

esc + shift + 7 ---> buscar
esc + shift + :%s/{name}/{nametoreplace}
 
! Conexiones SSH

SSH es el nombre de un protocolo y del programa que lo implementa cuya principal funcion es el acceso remoto a un servidor
por medio de un canal seguro en el que toda la información está cifrada.

sshpass -p '{password}' shh {user}@{servidor} -p {port}

export TERM=xterm

!# Bash pura

Al intentar leer archivos con el nombre - el sistema lo tomara como flag

Soluciones ---> 
?$  cat ./- 
?$  cat  /path/-  
?$  cat $(pwd)/-
?$  grep -r "\w" 2>/dev/null | tail -n 1 | awk '{print $2}' FS=":"
?$  grep -r "\w" 2>/dev/null | tail -n 1 | tr ':' ' ' | awk '{print $2}'
?$  grep -r "\w" 2>/dev/null | tail -n 1 | cut -d ':' -f 2
?$  grep -r "\w" 2>/dev/null | tail -n 1 | tr ':' ' ' | awk 'NF{print $NF}'   <--- cuando queremos referenciar al ultimo arg
?$  grep -r "\w" 2>/dev/null | tail -n 1 | tr ':' ' ' | rev | awk '{print $1}' | rev   <--- rev --> reverse
?$  grep -oP '.*?'
-o ---> only matchers
-P ---> expresiones regulares 
.*? ---> data expresada en regex

Al intentar leer archivos con un nombre separado como spaces in this filename el cat intentara hacerlo de manera separada

cat {tab (tecla)}
cat "{name with spaces}"
cat /path/s* || cat /path/*

?$ find .
?$ find . -type f | xargs cat | 
?$ find . -type f | grep "hidden" | xargs cat
?$ find . -type f | grep -vE "bashrc|profile"
Grep -v para quitar aquellos que tengan ese str, y la E mayuscula para que acepte multiples

?$ find . | xargs file --mime-type
Output:
./-file03: application/octet-stream
./-file04: application/octet-stream
./-file09: application/octet-stream
./-file07: text/plain
./-file08: application/octet-stream
./-file06: application/octet-stream
./-file05: application/octet-stream
./-file01: application/octet-stream
./-file02: application/octet-stream
./-file00: application/octet-stream

Escapar un str --> \ por ejemplo el - se debe escapar \-

?$ find . -type f ! -executable -size 1033c | xargs cat | xargs  <--- este xargs final es para acomodar el output en casos
?$ find . -type f ! -executable -size 1033c | xargs cat | head -n 1


?$ for i in (seq 1 20); do echo "[+] Iteración numper $i"; done
Esta es la manera de iterar con un bucle en bash, el comando seq sirve para crear im secuencia

?$ for i in (seq 1 50); do echo "[+] Probando con la seq n°$i"; cat archivo.txt | cut -d ' ' -f $i; done

?$ cat data.txt | grep "millionth" | xargs | tr ' ' '\n' | tail -n 1
tr ---> sustituciones

?$ cat data.txt | grep "millionth" | xargs | sed 's/prueba/probando'  <--- cambia la palabra y con un /g todas
xargs solo ---> formatea la cadeba
sed ---> sustituir una PALABRA 

En un archivo en el que hay muchas repeticiones:

con el comando sort puedo ordenarlo y con el uniq -u pedirle la unica linea que no se repite

?$ sort cat data.txt | uniq -u


?$ strings data.txt 
Strings para ver unicamente los caracteres legibles del archivo

?$ echo "hola" | base64 -w 0
Comando base64 para encodear el contenido, -w 0 para indicar que sea todo en una sola linea para el caseo de archivos

?$ echo "alksjfjkhKAHSJKFHKjasdaksdhaijHSF" | base64 -d
Si tenemos una cadena encodead la podemos decodear con el -d

Nos enfrentamos a un rot13, es decir, una cadena la cual se han rotado posiciones 13 veces, para esto exiten derotadore
online, pero en bash podriamos resolverlo de la sig manera

Tememos el abcdario -> a b c d e f g h i j k l m n o p q r s t u v w x y z

Por lo que si se roto para atras, la g, nos daria por la t

Por lo que podriamos decirle:

?$ cat data.txt | tr '[G-ZA-Fg-za-f]' '[T-ZA-St-za-s]'

o más facil 

?$ cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'

?$ cat data.txt | xxd -ps   <--- transformar a exadesimal

?$ cat hostCopy | xxd -ps | xargs | tr -d ' ' | xxd -ps -r
Cateo un archivo que codifico a exa y lo comprimo con xargs dejando solo 1 espacio borrando estos para decodearlo xd 

Una concepto de linux es que si estamos modificando un archivo y queremos guardar en el mismo filtros o comandos que le aplicamos
con un doble redirector >>, o el comando tee o un unico redirector > no funcionria de la manera que queremos, la solucion seria
entonces tirar de sponge

#!/data.txt
Hola esto es una prueba

?$ cat data.txt | awk '{print $3}' | sponge data.txt

#!/data.txt 
es 

! 7z
Herramienta descomprensora de cualquier archivo

?$ 7z l {name}

Para listar el contenido del archivo

?$ 7z x {name} 

Para extraer el contenido


Otra situación es la de un archivo en hexadecimal el cual se comprimio multiples veces 

cat {archivo} xxd -r | sponge {archivo}

Y ahora es cuando nos damos cuenta de que el mismo sufrio multiples veces el ser comprimido
Lo que lo podemos solucionar con un simple archivo bash

#!/bin/bash

function ctrl_c(){
        echo -e "\n\n[!] Saliendo del programa....\n"
}

trap ctrl_c INT
#----------------

file="{archivo}"

while [ $file ]; do
        echo -e "\n\n[+] Descomprimiendo el archivo: $file\n"
        file="$(7z l $file 2>/dev/null | tail -n 3 | head -n 1 | awk 'NF{print $NF}')"
        7z x $file &>/dev/null
done

#!---------------------------------------------

! Manejo de pares claves y conexiones SSH

Las keys deben tener el permiso 600 --> rw-------

Un demonio es un programa que se ejecuta en segundo plano 

Par clave ssh ---> public - privada

Para habilitar el ssh

?$ sudo systemctl start sshd
Levantar el demonio de ssh

*Manera 1:

Una vez levantado el demonio en el sistema, podria conectarme desde otros equipos terceros a mi sistema proporcionando la password
?$ ssh {username}@{ip} 
?$ ssh k0v4ks@localhost 

Pero como hago para que los mismos no tengan que dar contraseña?

#~/home/k0v4ks/.ssh
?$ ssh-keygen

Esto para crear una clave privada y otra publica.

Con la clave publica, tengo que convertir la misma en el dir privado .ssh como clave autorizada 

?$ touch authorized_keys 

Y dentro guardar la clave publica, al tener una clave publica en un archivo "authorized_keys" la conexion ssh se da
facilmente y sin proporcionar contraseña

*Manera 2

La clave privada la hacemos autorizada para que cualquiera que tenga la misma pueda conectarse a la maquina

?$ ssh-copy-id -i id_rsa {name}@{ip}
?$ ssh-copy-id -i id_rsa k0v4ks@localhost 
-i (identity_file)
id_rsa(clave privada)

Nos loggeamos, y de esta manera volvemos la clave privada autorizada y cualquiera que tenga la misma podra conectarse otra vez
sin credenciales:
*Otro equipo (teniendo el archivo id_rsa en .ssh)

?$ ssh-copy-id -i id_rsa k0v4ks@localhost
?$ ssh -i {file_with_key} {name}@{ip}

! Netcat y puertos

Puertos ---> 65535 

Netcat --> nc -nlvp 443

?$ netstat -nat  <--- ver puertos corriendo en el sistema

?$ ss -nltp  <--- tambien ver puertos corriendo

?$ cat /proc/net/tcp <---- tambien puedo ver corriendo puertos, segunda columna en exadecimal

?$ sudo lsof -i:{puerto} <---- obtener información de que servicio esta corriendo el puerto
-i ---> Archivo de indentidad


cat /proc/net/tcp --->

sl  local_address rem_address   st tx_queue rx_queue tr tm->when retrnsmt   uid  timeout inode                                                     
2   │    0: 0100007F:9159 00000000:0000 0A 00000000:00000000 00:00000000 00000000  1000        0 24958 1 00000000d680902f 100 0 0 10 0                     
3   │    1: 0100007F:1538 00000000:0000 0A 00000000:00000000 00:00000000 00000000   124        0 807 1 000000004854a627 100 0 0 10 0                       
4   │    2: 00000000:0BB8 00000000:0000 0A 00000000:00000000 00:00000000 00000000  1000        0 658038 1 00000000cc85f403 100 0 0 10 0                    
5   │    3: 0100007F:193F 00000000:0000 0A 00000000:00000000 00:00000000 00000000  1000        0 22960 1 00000000bd9dc7f1 100 0 0 10 0                     
6   │    4: 00000000:9EC1 00000000:0000 0A 00000000:00000000 00:00000000 00000000  1000        0 142376 1 0000000016c5e23d 100 0 0 10 0   

                      |
                      V

Esta linea indica los puertos

!Procesos corren

?$  echo "9159
?$  1538
?$  0BB8
?$  193F
?$  9EC1" | sort -u | while read line; do echo "[+] Corriendo puerto ---> $(echo "obase=10; ibase=16; $line" | bc)"; done

----

?$  for line in (echo "9159
?$  1538
?$  0BB8
?$  193F
?$  9EC1"); do echo "[+] Corriendo puerto ----> $(echo "obase=10; ibase=16; $line" | bc)"; done

?$ ps -faux     <--- listar procesos del sistema

?$ ps -eo command  <--- listar comandos especificos que se estan ejecutando

! Conexiones encriptadas

herramienta ncat tiene una prop --ssl --> encriptacion ssl (no puede viajar en texto plano "Secure Socket Layer")

nmap --open -T5 -v -n -p31000-32000 127.0.0.1

*Scripts en bash:


#!/bin/bash
   2   │ 
   3   │ function ctrl_c(){
   4   │     echo -e "\n[!] Quiting....\n"
   5   │     tput cnorm; exit -1 
   6   │ }
   7   │ 
   8   │ # Ctrl + c
   9   │ trap ctrl_c INT
  10   │ 
  11   │ 
  12   │ sleep 10
  13   │ 
  14   │ tput civis # Ocultar cursor
  15   │ 
  16   │ for ip_frag in $(seq 1 254); do
  17   │     timeout 1 bash -c "ping -c 1 192.168.1.$ip_frag &>/dev/null" && echo "[+] Host 192.168.1.$ip_frag - ACTIVE" &
  18   │ done; wait
  19   │ 
  20   │ tput cnorm # Recuperar cursor

------------------

──────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/bin/bash
   2   │ 
   3   │ function ctrl_c(){
   4   │     echo -e "\n[!] Quiting....\n"
   5   │     tput cnorm
   6   │     exit -1 
   7   │ }
   8   │ 
   9   │ # Ctrl + c
  10   │ trap ctrl_c INT
  11   │ 
  12   │ 
  13   │ sleep 10
  14   │ 
  15   │ tput civis # Ocultar cursor
  16   │ 
  17   │ for port in $(seq 1 65535); do
  18   │     (echo "" > /dev/tcp/127.0.0.1/$port) 2>/dev/null && echo -e "\n[+] Port $port OPEM
       │ .\n" &
  19   │ done; wait
  20   │ 
  21   │ tput cnorm # Recuperar cursor


Ambos scrips funcionan de manera similar, uno se encarga de enviar un str vacio a un puerto para comprobar si el mismo
se encuentra abierto, esto solo es funcional desde bash ya que zsh no contiene el dir /dev/tcp
Mientras que el otro tambien en un ciclo, prueba con un timout de 1 s realizar un ping a un dirección ip.

Ambos utilizan hilos ---> el & final  y el wait despues de done; para esperar a los mismos


! Diferencias entre archivos
 
?$ wc -l {archivo}|*

?$ diff {file1} {file2}    <---- diferencia entre archivos

Podemos intentar injectar comandos a la hora de realizar un concexion ssh, por ejemplo, en el caso de que se hubiera modificado
el archiv bashtsrc / zshrc para que nos expulse a la hora de ingresar podriamos hacer lo sig

?$ sshpass -p "{password}" ssh {username}@{ip} -p {port} {command}

?$ sshpass -p "owenNash3!#" ssh k0v4ks@127.0.0.1 -p 3000 bash

De esta manera podriamos intentar burlar lo antes mencionado pidiendo una bash con la cual poder operar de igual manera

! Conexiones

?$ nc -nlvp {port}
-n --> no dns
-l --> listen
-v --> verbose
-p --> puerto

Para ponerse en escucha en un puerto 

! Tareas CRON

Tareas que se ejecutan en el sistema a intervalos regulares de tiempo

/etc/cron.d
Dentro podremos ver las tareas 
Las cuales tmb podremos ver 

* * * * *

*1 Minutos: de 0 a 59.
*2 Horas: de 0 a 23.
*3 Día del mes: de 1 a 31.
*4 Mes: de 1 a 12.
*5 Día de la semana: de 1 a 6 lunes a sábado (1=lunes, 2=martes, etc.) y 0 o 7 el domingo.

El * va si queremos decir que determinada posicion se ejecuta a cada (minuto, hora, dia, nes, dia puntual)

Ejemplos:

Una tarea que se ejecuta cada minuto, a cada hora, todos los dias, todos los meses

? * * * * *  {tarea}

A las 9:30 am del dia 20 de julio y que sea jueves

? 30 9 20 7 4   {tarea}

A las 9:30 del dia 20 de julio

? 30 9 20 7 *  {tarea}

Al minuto 20 de cada hora de todos los sabados

? 20 * * * 6  {tarea}

Al minuto 10 de cada hora de los sabados de enero

? 20 * * 1 6   {tarea}

Pasado un minuto de cada hora

? 1 * * * *

Cada 1 minuto

? */1 * * * *

Cada minuto pero entre las 2 y las 2:59

? * 2 * * * *

A las 2:02 pm

? 2 14 * * * *

Cada dos minutos entre las 2 y 2:59

? */2 14 * * *

Cada dos minutos cada dos horas

? */2 */2 * * *

Cada minuto en el día 2 del mes

? * * 2 * *

Cada 5 minutos, solo en junio

? 5 * * 6 *

A las 10:05 de la mañana, el día 5 del mes, pero solo en junio

? 5 10 5 6 *

Cada minuto cada dos días

? */2 *  * * */2

L --> Ultimo día del mes 
L --> Sabado


?$ echo "Vamos a hashear este stout para poder corroborrar si el mismo en algun momento sufre cambios" | md5sum

for i in * .*;     <--- para recorrer cada uno de los recursos del dir actual
do   
done

?$ watch -n 1 ls -l    <---- watch -n 1  (para monitorizar cada segundo el repositorio)

Podemos crear un ataque de fuerza bruta de pin codes:

for pin in {0000..9999}; do
        echo "$pin"
done

En este caso un puerto esperaba una password junto a un ping dentro del rango de 0000 a 9999

?$ for pin in {0000..9999}; do echo "password $pin"; done > archivo.txt

?$ cat archivo.txt | nc localhost 30002 | grep -vE "Wrong|Please enter"

Bucle while para leer un archivo

?$ while IFS= read -r line; do echo $line; done < input_file

!Escapando del contexto de un comando

Nos enfrentamos a un caso en el que al conectarnos mediante ssh, al ingresar no tenemos una bash y nos saca de la conexion,
al investigar un poco más nos damos cuenta de que con el comando cat

?$ cat /etc/passwd | grep {username}
?$ grep {username} /etc/passwd


bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext   <---- 

?$ cat /usr/bin/showtext


*#!/bin/sh

*export TERM=linux

*exec more ~/text.txt
*exit 0

Se trata un script el cual ejecuta un comando more del archivo text.txt,
El comando more te permite navegar de arriba abajo en el stdout

Cuando el tamaño es muy grande, parece que entra en modo less, es decir, que no nos deja navegar, ni siquiera navegar 

Una vez que logramos hacer que aparezca el more, podemos entrar en el modo visual con la letra "v"
Para posteriormente con "ESC" + "SHIFT" + ":" podemos poner comandos, con lo que podemos setear una shell para usar
?$ v
?$ esc + shift + :
?$ set shell=/bin/bash
?$ esc + shift + :
?$ shell

Esto es especialmente útil para casos en los que se 
ejecutan comandos que puedan llegar a causar un gran desplazamiento.
Para pasar a la página siguiente, tienes que presionar la barra espaciadora en el teclado.
Puedes continuar presionando espacio hasta llegar al final del resultado o puedes presionar la tecla “q” directamente para salir.


! Operando con proyectos de Github

git clone <--- clonar un proyecto 
git log <---- ver el log de commits con sus respectivos ids realizados 
git show commit.id <--- para ver en consola los cambios realizados en el dicho commit
git checkout commit.id <--- volver a un estado del proyecto antiguo (el del commit)
git branch -a  <---- ver las ramas del proyecto
git checkout {name} <---- cambiarse a las ramas
git tag <---- ver puntos en la historia de una rama que persiste inalterable
git show {name} <--- ver el tag anteriormente listado

!Argumentos posicionales

[$0]: Representa el nombre del script que se invocó desde la terminal.

[$1]: Es el primer argumento desde la línea de comandos.

[$2]: Es el segundo argumento desde la línea de comandos y así sucesivamente.

[$#]: Contiene el número de argumentos que son recibidos desde la línea de comandos.

[$*]: Contiene todos los argumentos que son recibidos desde la línea de comandos, guardados todos en la misma variable.

! --------------------------------------------------------------------------------------------------------

! PROYECTO EN BASH 1 

?$ curl -s -X GET {url}  <--- para lanzar una peticion
-s ---> para no ver info verbose
-X GET --> metodo con el cual vamos a lanzar la peticion

--

Script en bash:

Para recibir flags como en todos los comandos, ya sea desde el tipico de help -h o --help, podemos hacer lo sig

?$  while getopts "m:h" arg; do

?$  done
 
Aca le indicamos con la palabra getopts para que reciba los operators "m" que va a recibir algo, por eso los ":", y h
que no va a recibir nada

Dentro del flujo del while, analizaremos los casos

?$ declare -i counter=0 

?$  case $arg in
?$       m) machineName=$OPTARG; let counter+=1;;
?$       h) ;;
?$  esac

Analizamos losas casos con case e invertimos la palabra cuando finalize este analizis, con la palabra del arg seguido de )
indicamos el caso, caso m = m), que en ese caso guarda en la variable machineName lo que se haya ingresado seguido del -m, 
es decir si se uso -m "Raspberri" el $OPTARG = "Raspberri" y posteriormente aumentamos el valor de una variable.

Para los casos condicionales como el if, tambien se cierra invirtiendo "fi"

?$   if [ $counter -eq 1 ]; then
?$       codigo...
?$   else 
?$       codigo...
?$   fi

-eq ---> para los números, equal
-lt ---> less than

Cuando una funcion recibe parametros los invoca con $1

Pasarle props a una function

?$  nameFunction $parameter

awk no solo sirve para seleccionar un parametro, si no tambien lo podemos usar para pedir delecciones, por ejemplo, del archivo
bundle, selecciona desde donde el nombre sea Owen hasta resuelta

?$ cat bundle.js | awk "/name: \"Owen\"/", "/resuelta:/"
El  \" \" es para justamente escapar las comillas, ya que estamos buscando donde sea name: "Owen" pero esto iria dentro de un str

?$ tr -d ','  
Eliminar las comas

?$ grep "ip: \"$ipAddress\"" -B 3 
3 lineas para arriba desde donde se filtra

?$ grep "ip: \"$ipAddress\"" -A 4 
4 lineas para abajo desde donde se filtra

?$ grep "ip: \"$ipAddress\"" -C 4
4 lineas para abajo y para arriba desde donde se filtra

?$ grep "nashe" -i
-i de Insensitive NASHE=nashe=Nashe=nAshe=naShe=nasHe=nashE=etc...

?$ sed 's/^ *//'
Regex donde todo lo que empieze con espacio lo deja sin

?$ sed 's/** */-/'
Regex que agrega al principio de cada palabra, un -
k0v4ks   ------>  -k0v4ks
Owen     ------>  -Owen
Nashe    ------>  -Nashe

Se pueden hacer dobles condiciones con 

?$ if [ condition 1 ] && [ condition 2 ]; then

Se pueden fusionar flags con "chivatos" utilizando esta doble condición

! PROYECTO EN BASH 2

El modulo $RANDOM devuelve un número random, para jugar con rangos máximos podriamos hacer


?$ $RANDOM  
stdout: 3421

?$ echo $(($RANDOM % {num_máximo + 1}))
?$ echo $(($RANDOM % 37))
stdout:  12

A la hora de hacer un grep, se le puede indicar que empieze con algo con ^ y que termine con $, así como las lineas con -n

?$ cat {file} | grep "^1$" -n
Filtrar el archivo {file} por los números 1 y mostrarme las lineas

Para declarar un array

?$ declare -a {name}=({elements})

?$ declare -a myArray=(1 2 3 5)

Para mostrar una posición

?$ echo ${myArray[2]}

Para mostrar el ultimo

?$ echo ${myArray[-1]}

Para conocer el length

?$ echo ${#myArray[@]}

Para listar todos 

?$ echo ${{name}[@]}

?$ echo "${myArray[@]}"

Para iterar

?$ for elem in ${myArray[@]}; do
?$ 
?$ done

Para agregar un valor

?$ myArray+=({valueToAdd})

Para sacar valores

?$ unset myArray[0]

Pero entra en conflictos en situaciones devido a que recuerda los valores previos, por lo q es recomendable 
post sacar elementos, es igualar el array al nuevo valor

?$ myArray=(${myArray[@]})

Listar secuencias largas 

?$ ./ruleta.sh -m 10000 -t inverseLabraouchere | tee output

?$ cat output | grep -oP '\[.*?\]' | grep -v '\[\]' | tr -d '[]' | while read line; do echo $line | wc -c; done | sort -n > output

Esto para con el comando wc -c contar la cantidad de caracteres, ordenarla y vemos la secuencia más grande "23"

?$ cat output | grep -oP '\[.*?\]' | grep -v '\[\]' | tr -d '[]' | while read line; do if [ "$(echo $line | wc -c)" -eq "23" ]; then
?$ echo "Secuencia: $line"; fi; done

------ SYSTEMD --------
Asi como launchd son dos sistemas  de gestion de procesos en sistemas Linux y MacOS. Estos permiten ejecutar tareas
programadas y servicions automaticamente

Por ejemplo, podriamos dirijirnos a  /etc/systemd/system y crear un archivo llamado discord.service 
(esto para solucionar el error de que discord de cierra repentinamente)

Con las sigs linead

/etc/systemd/system/discord.service 
---------------------------------------------------------

[Unit]
Description=Discord launcher
After=network.target

[Service]
ExecStart=/bin/bash /path/to/your/script.sh
User=yourusername
Group=yourgroup
Restart=always
RestartSec=5
Environment=DISPLAY=:0
Environment=XAUTHORITY=/home/yourusername/.Xauthority

---------------------------------------------------------

Con esto lo que hacemos es crear un servicio llamado discord.service con la descripcion de Discord Launcher que se encarga
de ejecutar un script el cual podria tener un bucle infinito que compruebe si ds se encuentra abierto y en caso de que no lo 
abriria, en caso de que el servicio falle se reiniciaria 5s dsps del fallo, y ejecturia el script con el usuario y el grupo 
ingresado

De esta manera solo quedaria reiniciar el demonio

?$ sudo systemctl daemon-reload

Y posteriormente correr este nuevo servicio

?$ sudo systemctl start/stop/status discord.service

Y en caso de querer que al inciar el sistema el mismo se inicie, podriamos ejecutar

?$ sudo systemctl enable discord.service






"""
