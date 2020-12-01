#!/usr/bin/python3

##############################################################################################
# Tek Sistem İle Proxy, PHP7,NodeJS Kurulumu Created: Stalker
# Açık Kaynak Olarak Paylaştım İstek Gelirse 'C' Olarak Kodlarım İstediğiniz Gibi Düzenliyebilirsiniz.
# İletisim: instagram.com/davwr1514 & twitter.com/ToprakAyvaz2 & facebook.com/ByBafrali1 & 
# Toprak Ayvaz & EmreRoot  İşbirligiyle Kodlanmıştır
# yargılanıcaksın,eleştirileceksin,alay edilceksin,taklit edilceksin 
# kimseyi takma hayallerini gerçekleştir acı olmadan kazanç olmaz herkese iyi kodlamalar dilerim :)
##############################################################################################

import os,time,requests,webbrowser,random,sys,threading
from colorama import *

r = Fore.RED
g = Fore.GREEN
w = Fore.WHITE
b = Fore.BLUE
y = Fore.YELLOW
m = Fore.MAGENTA
res = Style.RESET_ALL

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])

cls()

def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
    

##############################################################################################
# Tek Sistem İle Proxy, PHP7,NodeJS Kurulumu Created: Stalker
# Açık Kaynak Olarak Paylaştım İstek Gelirse 'C' Olarak Kodlarım İstediğiniz Gibi Düzenliyebilirsiniz.
# İletisim: instagram.com/davwr1514 & twitter.com/ToprakAyvaz2 & facebook.com/ByBafrali1 & 
# Toprak Ayvaz & EmreRoot  İşbirligiyle Kodlanmıştır
# yargılanıcaksın,eleştirileceksin,alay edilceksin,taklit edilceksin 
# kimseyi takma hayallerini gerçekleştir acı olmadan kazanç olmaz herkese iyi kodlamalar dilerim :)
##############################################################################################


    _______.  ______   ______    _______  __   _______  __       _______  
    /       | /      | /  __  \  |   ____||  | |   ____||  |     |       \ 
   |   (----`|  ,----'|  |  |  | |  |__   |  | |  |__   |  |     |  .--.  |
    \   \    |  |     |  |  |  | |   __|  |  | |   __|  |  |     |  |  |  |
.----)   |   |  `----.|  `--'  | |  |     |  | |  |____ |  `----.|  '--'  |
|_______/     \______| \______/  |__|     |__| |_______||_______||_______/ 
                                                                           



    """
import os,  time, requests, sys, threading
CheckVersion = str(sys.version)

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])

cls()




def xx(PROXY, url):
    try:
        sess = requests.session()
        sess.proxies = {'http': PROXY}
        sess.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                      ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        aa = sess.get(url, timeout=5, proxies={'http': PROXY})
        if aa.status_code == 800:
            print (PROXY + '   Aktif')
            with open('aktif.txt', 'a') as xX:
                xX.write(PROXY + '\n')
        else:
            print (PROXY + '   Pasif')
    except:
        print (PROXY + '   Pasif')


def main():
    try:
        if '3.' in CheckVersion:
            try:
                fileproxy = input(' Proxy.txt Dosyanızı Girin --> ')
            except:
                print('  [-] Hata : Proxylerinizi Yükleyin!')
                sys.exit()
        elif '2.' in CheckVersion:
            try:
                fileproxy = raw_input(' Proxy.txt --> ')
            except:
                print('  [-] Hata : Proxylerinizi Yükleyin!')
                sys.exit()
        else:
            print(' Python2 Sürümü!')
    except:
        pass
        sys.exit()
    with open(fileproxy, 'r') as x:
        prox = x.read().splitlines()
    thread = []
    for proxy in prox:
        t = threading.Thread(target=xx, args=(proxy, 'https://instagram.com'))
        t.start()
        thread.append(t)
        time.sleep(0.1)
    for j in thread:
        j.join()

main()



