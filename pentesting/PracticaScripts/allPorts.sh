#!/bin/bash


echo -e "\n\t[i] Esto es una prueba de script en bash\n"

sleep 2

echo -e "\n[*] Puertos abiertos de la primera forma...\n"

sleep 1

/usr/bin/bat /proc/net/tcp | awk '{print $2}' | awk '{print $2}' FS=':' | sort -u | while read line; do
  echo -e "\n[!] Port $(echo "obase=10;  ibase=16; $line" | bc ) open"
done

sleep 2

echo -e "\n\n[*] Puertos abiertos de la segunda forma...\n\n"

sleep 1

for port in $(/usr/bin/bat /proc/net/tcp | awk '{print $2}' | awk '{print $2}' FS=':' | sort -u | xargs); do
  echo -e "\n[!] Port $(echo "obase=10;  ibase=16; $port" | bc ) open"
done
