#!/bin/python3 
import subprocess, signal, sys, re

def run():
    print("test")
    rute = '/proc/net/tcp'
    proc = subprocess.Popen(["/usr/bin/bat %s | awk '{print $2}' | awk '{print $2}' FS=':' | sort -u | xargs" % rute, ""], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
   
    str_ports = str(out)
    ports = str_ports.split()
    ports = [p for p in ports if re.search(r"[A-Z][0-999]", p)]
    print(f"aca ---> {ports}")
    for port in ports:
        hex_port = '0x' + port
        print(f'supuesto non-hex {hex_port}')
        print(f"Port {bytes.fromhex(hex_port).decode('utf-8')} open.")

if __name__ == "__main__":
    run()
