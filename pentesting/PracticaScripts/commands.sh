#!/bin/bash

#Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

function ctrl_c(){
  echo -e "\n${redColour}[!]${endColour} ${grayColour}Quiting...${endColour}\n"
  exit 1 
}

trap ctrl_c INT

function help_panel(){
  echo -e "\n${purpleColour}[i]${endColour} ${grayColour}Usage:${endColour}\n"
  echo -e "\t${yellowColour}[*]${enColour}${grayColour} $0 ${turquoiseColour}-c${endColour} ${yellowColour}<${endColour}${purpleColour}technology${endColour}${yellowColour}>${endColour}${endColour} ${yellowColour}--->${endColour} ${grayColour}Know some commands about a technology.${endColour}\n"
  echo -e "\t${redColour}[!]${endColour} ${grayColour}Available technologies${endColour}${redColour}:${endColour}"
  echo -e "\t${redColour}-${endColour} ${grayColour}git${endColour}"
  echo -e "\t${redColour}-${endColour} ${grayColour}bash${endColour}"
  echo -e "\t${redColour}-${endColour} ${grayColour}docker${endColour}"
  echo -e "\t${redColour}-${endColour} ${grayColour}pentesting${endColour}"
  echo -e "\n\t${yellowColour}[*]${enColour}${grayColour} $0 ${turquoiseColour}-d${endColour} ${yellowColour}--->${endColour} ${grayColour}Know about system directorys.${endColour}\n"
  echo -e "\n\t${yellowColour}[*]${enColour}${grayColour} $0 ${turquoiseColour}-m${endColour} ${yellowColour}--->${endColour} ${grayColour}Know manual about shkd and kitty.${endColour}\n"
  [[ "$1" ]] && exit 1 || exit 0 
}

function git(){
  echo -e "\n${turquoiseColour}[i]${endColour} ${yellowColour}$1${endColour}${grayColour} commands${endColour}${turquoiseColour}:${endColour} \n"
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}init${endColour} ${yellowColour}----------------------------------->${endColour} ${turquoiseColour}i)${endColour} ${grayColour}Initialize a git repository.${endColour}"
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}clone${endColour} ${purpleColour}{repository_url}${endColour} ${yellowColour}----------------->${endColour} ${turquoiseColour}i)${endColour} ${grayColour}Clone the repository hosted at the url.${endColour}"
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}status${endColour} ${yellowColour}--------------------------------->${endColour} ${turquoiseColour}i)${endColour} ${grayColour}Check the status of the repository.${endColour}" 
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}add${endColour} ${purpleColour}{file_to_add}${endColour} ${yellowColour}---------------------->${endColour} ${turquoiseColour}i)${endColour} ${grayColour}Add trace to indicated file.${endColour} ${turquoiseColour}(${endColour}${grayColour}With a . we would add traces to all changed files${endColour}${turquoiseColour})${endColour}"
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}commit${endColour} ${turquoiseColour}-m${endColour} ${purpleColour}{message_to_save_change}${endColour} ${yellowColour}----->${endColour} ${turquoiseColour}i)${endColour} ${grayColour}Add changes to save under a descriptive name.${endColour}" 
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}push${endColour} ${purpleColour}{url_or_branch}${endColour} ${yellowColour}------------------->${endColour} ${turquoiseColour}i)${endColour} ${grayColour}Update the branch with the changes previously commited.${endColour}" 
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}checkout${endColour} ${purpleColour}{branch_name}${endColour} ${yellowColour}----------------->${endColour} ${turquoiseColour}i)${endColour} ${grayColour}Switch to an existing branch.${endColour}" 
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}checkout${endColour} ${turquoiseColour}-b${endColour} ${purpleColour}{branch_name}${endColour} ${yellowColour}-------------->${endColour} ${turquoiseColour}i)${endColour} ${grayColour}Create a branch and switch.${endColour}" 
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}branch${endColour} ${yellowColour}--------------------------------->${endColour} ${turquoiseColour}i)${endColour} ${grayColour}See local branches.${endColour}"
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}branch${endColour} ${turquoiseColour}-a${endColour} ${yellowColour}------------------------------>${endColour} ${turquoiseColour}i)${endColour} ${grayColour}View existing branches in the repository.${endColour}"  
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}branch${endColour} ${turquoiseColour}-D${endColour} ${purpleColour}{branch_name}${endColour} ${yellowColour}---------------->${endColour} ${turquoiseColour}i)${endColour} ${grayColour}Delete a local branch.${endColour}"
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}log${endColour} ${yellowColour}------------------------------------>${endColour} ${turquoiseColour}i)${endColour} ${grayColour}View commit history.${endColour}"
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}show${endColour} ${purpleColour}{commit_id}${endColour} ${yellowColour}----------------------->${endColour} ${turquoiseColour}i)${endColour} ${grayColour}View the changes made in that commit.${endColour}"
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}checkout${endColour} ${purpleColour}{commit_id}${endColour} ${yellowColour}------------------->${endColour} ${turquoiseColour}i)${endColour} ${grayColour}Return to the project state of that commit.${endColour}" 
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}reset${endColour} ${turquoiseColour}--hard${endColour} ${purpleColour}HEAD^${endColour} ${yellowColour}--------------------->${endColour} ${turquoiseColour}i)${endColour} ${grayColour}Remove the last commit.${endColour}"
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}reset${endColour} ${turquoiseColour}--hard${endColour} ${purpleColour}HEAD~{num}${endColour} ${yellowColour}---------------->${endColour} ${turquoiseColour}i)${endColour} ${grayColour}Remove the last {num} commits entered.${endColour}" 
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}tag${endColour} ${yellowColour}------------------------------------>${endColour} ${turquoiseColour}i)${endColour} ${grayColour}View points in the history of a branch that persists unchanged.${endColour}"
  echo -e "\t ${turquoiseColour}-${endColour} ${yellowColour}git${endColour} ${grayColour}show${endColour} ${purpleColour}{tag_name}${endColour} ${yellowColour}------------------------>${endColour} ${turquoiseColour}i)${endColour} ${grayColour}View the tag selected.${endColour}"
}


function bash(){
  echo -e "\n${turquoiseColour}[i]${endColour} ${yellowColour}$1${endColour}${grayColour} commands${endColour}${turquoiseColour}:${endColour} \n"
  echo -e "\n${yellowColour}----------------------------------------${endColour} ${redColour}COMANDOS DEL SISTEMA${endColour} ${yellowColour}------------------------------------------${endColour}\n"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}kill %%${endColour} ${yellowColour}----------->${endColour} ${grayColour}Matar procesos en segundo plano.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}ln${endColour} ${yellowColour}----------->${endColour} ${grayColour}Enlace simbolico.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}cut${endColour} ${turquoiseColour}'{delimitador}' -f {select_fild}${entered} ${yellowColour}----------->${endColour} ${grayColour}Cortar un str.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}tr${endColour} ${yellowColour}----------->${endColour} ${grayColour}Eliminar o remplazar un str.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}xxd -ps${endColour} ${yellowColour}----------->${endColour} ${grayColour}Encodear o decodear a hexadecimal o de hexadecimal.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}echo \$(echo \"obase=10; ibase=16; {str}\")${endColour} ${yellowColour}----------->${endColour} ${grayColour}Decodear str de heaxadecimal.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}ps -a${endColour} ${yellowColour}----------->${endColour} ${grayColour}Listar procesos ejecutandose.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}ps -faux${endColour} ${yellowColour}----------->${endColour} ${grayColour}Listar procesos del sistema.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}ps -eo command${endColour} ${yellowColour}----------->${endColour} ${grayColour}Listar comandos ejecutandose en el sistema.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}xclip -sel clip${endColour} ${yellowColour}----------->${endColour} ${grayColour}Copiar algo al porta papeles.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}shrd -zun 10 -v {file}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Eliminar archivo y la tabla de indices para que no sea recuperable por tecnicas forenses.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}uname -a${endColour} ${yellowColour}----------->${endColour} ${grayColour}Informacion del Sistema.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}lsb_release -a${endColour} ${yellowColour}----------->${endColour} ${grayColour}Información del Sistema operativo.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}gzip -d${endColour} ${yellowColour}----------->${endColour} ${grayColour}Descomprimir archivo .gz.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}wc -l/-w/-c {file}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Cuente las lineas/palabras/bytes de un archivo.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}diff {file1} {file2}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Muestra las diferencias entre dos archivos.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}top${endColour} ${yellowColour}----------->${endColour} ${grayColour}Muestra lao procesos del sistema y la memoria que utiliza.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}watch -n {num} {command}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Quedar a la escucha en el repo por un cierto intervalo de tiempo la ejecución del comando.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}cat {file} ${turquoiseColour}|${endColour} ${purpleColour}less${endColour} ${yellowColour}----------->${endColour} ${grayColour}Leer el contenido de un archivo y evitar el scroll (up,down,space,b,q).${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}free -h${endColour} ${yellowColour}----------->${endColour} ${grayColour}Ver ram usada y disponible.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}lsof -i:{port}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Listar Información del puerto abierto.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}airmon-ng start/stop {interfaz}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Encender/Apagar el modo monitor en una interfaz de red.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}.*?${endColour} ${yellowColour}----------->${endColour} ${grayColour}Representación de data en regex.${endColour}"
  echo -e "\n${yellowColour}------------------------------------------${endColour} ${redColour}SCRIPTING EN BASH${endColour} ${yellowColour}--------------------------------------------${endColour}\n"
  echo -e "\t${turquoiseColour}LISTAS: ${endColour}\n"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}declare -a lista${turquoiseColour}=(${endColour}${redColour}{elements}${endColour}${turquoiseColour})${endColour}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Declarar una lista.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}echo ${yellowColour}\${${endColour}${purpleColour}lista${endColour}${redColour}[${endColour}${purpleColour}pos${enColour}${redColour}]${endColour}${yellowColour}}${enColour} ${endColour} ${yellowColour}----------->${endColour} ${grayColour}Mostrar una posición de la lista.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}echo ${yellowColour}\${${endColour}${redColour}#${enColour}${purpleColour}lista${enColour}${redColour}[@]${endColour}${yellowColour}}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Conocer el length de una lista.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}echo ${yellowColour}\${${endColour}${purpleColour}lista${enColour}${redColour}[@]${endColour}${yellowColour}}${endColour} ${endColour} ${yellowColour}----------->${endColour} ${grayColour}Listar todos los valores de la lista.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}lista${turquoiseColour}+=(${endColour}${purpleColour}valueToAdd${endColour}${turquoiseColour})${endColour} ${yellowColour}----------->${endColour} ${grayColour}Agregar un valor a la lista.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}unset list${redColour}[${endColour}${purpleColour}pos${endColour}${redColour}]${endColour}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Eliminar un elemento de la lista.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}lista${turquoiseColour}=(${endColour}${yellowColour}\${${endColour}${purpleColour}lista${endColour}${redColour}[@]${endColour}${yellowColour}}${endColour}${turquoiseColour})${endColour}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Redeclarar una lista despues de haber eliminado un elem. para evitar conflictos.${endColour}"
  echo -e "\n\t${turquoiseColour}BUCLES: ${endColour}\n"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}for ${redColour}elem${endColour} ${purpleColour}in${endColour} ${yellowColour}\$(${endColour}${redColour}seq${endColour} ${grayColour}1 10${endColour}${yellowColour})${endColour}${purpleColour};${endColour} ${redColour}do${endColour} ${grayColour}x${endColour}${purpleColour};${endColour} ${redColour}done${endColour} ${yellowColour}----------->${endColour} ${grayColour}Recorrer una secuencia.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}for ${redColour}elem${endColour} ${purpleColour}in${endColour} ${yellowColour}{${endColour}${redColour}0000..9999${endColour}${yellowColour}}${endColour}${purpleColour};${endColour} ${redColour}do${endColour} ${grayColour}x${endColour}${purpleColour};${endColour} ${redColour}done${endColour} ${yellowColour}----------->${endColour} ${grayColour}Recorrer una secuencia grande.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}for ${redColour}line${endColour} ${purpleColour}in${endColour} ${yellowColour}\$(${endColour}${redColour}stdout${endColour}${yellowColour})${endColour}${purpleColour};${endColour} ${redColour}do${endColour} ${grayColour}x${endColour}${purpleColour};${endColour} ${redColour}done${endColour} ${yellowColour}----------->${endColour} ${grayColour}Recorrer lineas del cat de un archivo o stdout de un comando.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}${redColour}stdout${endColour} ${turquoiseColour}|${endColour} ${purpleColour}while${endColour} ${yellowColour}read line${endColour}${purpleColour};${endColour} ${redColour}do${endColour} ${grayColour}x${endColour}${purpleColour};${endColour} ${redColour}done${endColour} ${yellowColour}----------->${endColour} ${grayColour}Recorrer lineas del cat de un archivo o stdout de un comando con while.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}while ${turquoiseColour}IFS=${endColour} ${yellowColour}read${endColour} ${turquoiseColour}-r${endColour} ${yellowColour}line${endColour}${purpleColour};${endColour} ${redColour}do${endColour} ${purpleColour}echo${endColour} ${yellowColour}\$line${endColour}${purpleColour};${endColour} ${redColour}done${endColour} ${turquoiseColour}<${endColour} ${purpleColour}{file}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Leer 1 x 1 las lineas de un archivo.${endColour}"
  echo -e "\n\t${turquoiseColour}CONDICIONALES: ${endColour}\n"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}if${endColour} ${yellowColour}[${endColour} ${redColour}\"condition\"${endColour} ${yellowColour}]${endColour}${purpleColour};${endColour} ${purpleColour}then${endColour} ${grayColour}x${endColour}${purpleColour};${endColour} ${purpleColour}fi${endColour} ${yellowColour}----------->${endColour} ${grayColour}Condicional if para ejecutar una acción en base a una condición.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}if${endColour} ${yellowColour}[${endColour} ${redColour}\"condition\"${endColour} ${yellowColour}]${endColour}${purpleColour}; then${endColour} ${grayColour}x${endColour}${purpleColour}; else${endColour} ${grayColour}x${endColour}${purpleColour}; fi${endColour} ${yellowColour}----------->${endColour} ${grayColour}Condicional if para realizar una acción si se cumple la condición y otra diferente si no.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}if${endColour} ${yellowColour}[${endColour} ${redColour}\"condition\"${endColour} ${yellowColour}]${endColour}${purpleColour};${endColour} ${purpleColour}then${endColour} ${grayColour}x${endColour}${purpleColour};${endColour} ${purpleColour}elif${endColour} ${yellowColour}[${endColour} ${redColour}\"condition2\"${endColour} ${yellowColour}]${endColour}${purpleColour};${endColour} ${purpleColour}then${endColour} ${grayColour}x${endColour}${purpleColour};${endColour} ${purpleColour}else${endColour} ${grayColour}x${endColour}${purpleColour};${endColour} ${purpleColour}fi${endColour}\n\t${grayColour}  Si se cumple la condición se realiza una acción, si no, si se cumple una segunda condición se realiza una acción, si no se cumple ninguna se relaliza otra.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}${yellowColour}[[${endColour} ${redColour}\"condition\"${endColour} ${yellowColour}]]${endColour} ${turquoiseColour}&&${endColour} ${grayColour}x${endColour} ${turquoiseColour}||${endColour} ${grayColour}x${endColour} ${yellowColour}----------->${endColour} ${grayColour}Ternario if else.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}while getopts "m:h" arg, do case \$arg in m) \$OPTARG; let counter+=1;; esac done ${endColour} ${yellowColour}----------->${endColour} ${grayColour}Bucle while que recibe los args posibles, en este ejemplo la m que va a recibir un arg (OPTARG) y la h que no. Luego se suma la var counter que deberia ser decalara (declare -i counter=0) para evaluar a que caso se ingreso.${endColour}"
  echo -e "\n${yellowColour}------------------------------------------${endColour} ${redColour}TRATAMIENTO TTY${endColour} ${yellowColour}--------------------------------------------${endColour}\n"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}script /dev/null -c bash${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}ctrl + z${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}stty raw -echo${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}fg${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}reset${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}xterm${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}export TERM=xterm${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}export SHELL=bash${endColour}"
  echo -e "\t ${turquoiseColour}-${endColour} ${purpleColour}stty -a${endColour} ${yellowColour}----------------------->${endColour} ${turquoiseColour}i)${endColour} ${grayColour}Ver las filas y columnas para poder setear correctamente las proporciones.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}stty rows {num_rows} columns {num_columns}${endColour}"
}


function dir(){
  echo -e "\n${turquoiseColour}[i]${endColour} ${yellowColour}Directorios${endColour}${turquoiseColour}:${endColour} \n"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}bin${endColour} ${yellowColour}----------->${endColour} ${grayColour}Dir donde se almacenan los binarios necesarios para garantizar funciones a nivel de usuario.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}boot${endColour} ${yellowColour}---------->${endColour} ${grayColour}Dir donde se almacenan los ejecutables y archivos utilizados en el arranque.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}dev${endColour} ${yellowColour}----------->${endColour} ${grayColour}Dir que incluye dispositivos de almacenamiento en forma de archivo(disco duro, usb, etc).${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}etc${endColour} ${yellowColour}----------->${endColour} ${grayColour}Dir encargado de almacenar archivos de configuración a nivel de componentes del os.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}home${endColour} ${yellowColour}---------->${endColour} ${grayColour}Dir donde se almacena archivos temporales, lo que el usuario instale, etc.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}lib${endColour} ${yellowColour}----------->${endColour} ${grayColour}Dir que incluye bibliotecas escenciales para ejecutar todos los bins del dir bin, sbin y modulos del kernel.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}media${endColour} ${yellowColour}--------->${endColour} ${grayColour}Dir que representa el punto de montaje de todos los volumenes logicos que se montan temporalmente.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}opt${endColour} ${yellowColour}----------->${endColour} ${grayColour}Dir \"extención\" del dir \"usr\", pero aca van todoslos archivos de solo lectura que son parte de programas autcontenidos.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}proc${endColour} ${yellowColour}---------->${endColour} ${grayColour}Dir que contiene info. de los procesos y apps que se estan ejecutando en un momento determinado del os (files virtuales, contenido null).${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}sbin${endColour} ${yellowColour}---------->${endColour} ${grayColour}Dir donde se almacenan los binarios para tareas de super usuario y os, pero solo por el usuario root.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}srv${endColour} ${yellowColour}----------->${endColour} ${grayColour}Dir que sirve para almacenar archivos y dirs relativos a servidores instalados dentro del sistema (http, ftp).${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}sys${endColour} ${yellowColour}----------->${endColour} ${grayColour}Dir que (al igual que \"proc\") pero que contienee files virtuales que proveen info. del kernel relativa a eventos de os.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}tmp${endColour} ${yellowColour}----------->${endColour} ${grayColour}Dir para almacenar files temporales a nivel os y user.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}usr${endColour} ${yellowColour}----------->${endColour} ${grayColour}Dir (\"User System Resources\") que sirve para almacenar files de solo lectura y relativos a las utilidades del user.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}var${endColour} ${yellowColour}----------->${endColour} ${grayColour}Dir que contiene files con info. del os, logs, emails de los users del sistema, dbs, info. en la cache.${endColour}"
}


function dcker(){ 
  echo -e "\n${turquoiseColour}[i]${endColour} ${yellowColour}$1${endColour}${grayColour} commands${endColour}${turquoiseColour}:${endColour} \n"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}docker ps${endColour} ${yellowColour}----------->${endColour} ${grayColour}Listar los containers que estan corriendo.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}docker-compose up -d${endColour} ${yellowColour}----------->${endColour} ${grayColour}Levantar el container del directorio.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}docker stasts${endColour} ${yellowColour}----------->${endColour} ${grayColour}Listar las stats de los containers que estan corriendo.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}docker resatrt {name}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Reiniciar un container.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}docker start/stop/kill {name}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Levantar/Parar/Matar un container.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}docker images${endColour} ${yellowColour}----------->${endColour} ${grayColour}Listar todas las imagenes locales.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}docker rmi {image}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Eliminar una imagen.${endColour}"
}

function pentesting(){
  echo -e "\n${turquoiseColour}[i]${endColour} ${yellowColour}Algunos servicios${endColour}${turquoiseColour}:${endColour} \n"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}telnet {ip}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Conectarse a telnet (suele correr en 23) A probar root, admin, administrador.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}ftp {ip}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Concectarse a una maquina con file transfer protocol (suele correr en servidor 21) Probar anonymous, guest, admin, animo, etc. (get para bajar files).${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}smbclient -L {ip}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Conectarse a un Server Message Block que suelen correr en el p 445 con el nombre \"microsoft-ds\".${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}smbclient \\\\{ip}\\{recurso}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Intentar conectarse a un recurso de un servidor smb.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}redis-cli -h {ip}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Conectarse a un servidor de redis (db en ram) (info = listar info y estadistica del srv, select {num} = usar db, keys * = listar keys, get key = descargar key.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}responder -I tun0${endColour} ${yellowColour}----------->${endColour} ${grayColour}Utilizar herramienta responder para intentar capturar el NetNTLMv2 de una maquina windows.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}john -w=/u/s/w/rock.you.txt {file}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Utilizar la herramienta john para intentar romper el hash del NetNLTMv2.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}evil-winrm -i {ip} -u {user} -p {password}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Nos conectamos con la herramienta evil-winrm a una ip, con la password obtenida.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}aws configure${endColour} ${yellowColour}----------->${endColour} ${grayColour}Confiurar las credenciales de aws.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}aws --endpoint={url} s3 ls s3:{domain}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Listar el contenido del bucket.${endColour}"
  echo -e "\t${turquoiseColour}-${endColour} ${purpleColour}aws --endpoint={url} s3 cp {file} s3:{domain}${endColour} ${yellowColour}----------->${endColour} ${grayColour}Copiar un archivo en el bucket.${endColour}"
}


function shkd(){
  /bin/cat /bin/manualOs
}


function commands(){ 
  if [ "$1" == "git" ]; then
    git $1
  elif [ "$1" == "bash" ]; then
    bash $1
  elif [ "$1" == "docker" ]; then
    dcker $1
  elif [ "$1" == "pentesting" ]; then
    pentesting
  else
    echo -e "\n${redColour}[!]${endColour} ${yellowColour}$1${endColour} ${grayColour}it isn't an allowed technology.${endColour}\n"
    echo -e "${redColour}############################################################################################${endColour}"
    help_panel true 
  fi
}


declare -i selector=0

while getopts "c:dmh" arg;do 
  case $arg in
    c) tech=$OPTARG; let selector+=1;;
    d) let selector+=2;;
    m) let selector+=3;;
    h) ;;
  esac
done

if [ $selector -eq 1 ]; then
  commands $tech
elif [ $selector -eq 2 ]; then
  dir
elif [ $selector -eq 3 ]; then
  shkd
else 
  help_panel
fi
