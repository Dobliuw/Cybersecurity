"""
Download ----> http://www.microsoft.com/en-us/download/details.aspx?id=34595

!Customizar la shell
Click izquierdo arriba a la derecha en el icono, propierties 

start-process porweshell -verb runas 
cls / clear-host / clear -> Limpiar la pantalla
cd / set-location ---> Change directory
dir / getchild-item / ls --> Listar contenido de dir
type ---> Listar contenido de un archivo
Copy ---> Copiar un dir/file
md / mkdir ---> MakeDirectory

get-alias / gal {command} ---> Listar los aliases 
gal g* | gal *sv
get-alias -Definition {command} | get-alias -Definition get-proccess
help / man ---> Ayuda

notepad --> Abrir bloc de notas
ping dc --> hacer un ping a nuestra maquina
calc ---> calculadora
mspaint ---> paint
ipconfig /all---> interfazes de red

update-help -Force
help {command}
get-help *service* ---> buscar ayuda para buscar comandos que trabajen con services
get-help *service* -Detailed / -Examples / -full / -Online / -ShowWindow
get-verb 
get-verb |measure

Syntax [-Name <String[]>]
[                ] ---> Optional parameter
-Name -----> parameter 
<> ---> argument
<[]> --> allow multiple args

https://www.youtube.com/watch?v=UVUd9_k9C6A

"""