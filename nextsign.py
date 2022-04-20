import requests
import os
import sys
import time
import pyfiglet

Negrito = '\033[;1m'
Branco = '\033[1;97m'
Verde = '\033[1;32m'
Vermelho = '\033[1;31m'
Amarelo = '\033[1;33m'
Magenta = '\033[1;35m'
Cinza = '\033[1;90m'
Azul = '\033[1;34m'
Cyan = '\033[1;36m'
Reset = '\033[0;0m'

Logo = pyfiglet.figlet_format("Next Sign") 

def main():
    x = 1
    while x == 1:
        os.system("clear")
        url = requests.get('https://nextsign.000webhostapp.com/eurusd')
        query = url.json()
        print(f'{Cyan}'+Logo)
        print(f'{Negrito}{Magenta}EUR{Amarelo}/{Azul}USD{Branco}...\n\n')
        print(f'{Cyan}➫ {Vermelho}Warnings {Amarelo}[]{Branco}:\n\n')
        print(f'{Cyan}➫ {Branco}[{Verde}+{Branco}] {Amarelo}= {Verde}⇧ Up/Win{Branco}')
        print(f'{Cyan}➫ {Branco}[{Vermelho}-{Branco}] {Amarelo}= {Vermelho}⇩ Down/Loss{Branco}')
        print(f'{Cyan}➫ {Branco}[{Amarelo}%{Branco}] {Amarelo}= {Cinza}Time Taken/Probability{Branco}\n\n')
        print(f'{Cyan}➫ {Vermelho}Result {Amarelo}[]{Branco}:\n\n')
        print(f'{Cyan}➫ {Amarelo}%{Branco}: '+f'{Cinza}'+'{}'.format(query['porcentagem'])+f'{Reset}')
        time.sleep(30)
main()