import time
import random
import platform
import os

pcnome = platform.node()
so = platform.platform
print(pcnome)

crashou = random.randint(1,100)
if crashou <= 5:
    print("FINAL: CRASHOU")
    print("crashou uai")
    input()
    exit()

for i in range(40):
    print()
print("-------")
for i in range(10):
    print(  )

print("Olá")
print("Recomendo jogar com o Terminal em tela cheia e de zoom até sumir os traços que estão em cima desse texto, pressione ENTER para cotinuar")

for i in range(10):
    print()
input("")

for i in range(20):
    print()
print("BEM-VINDO")
time.sleep(0.5)
print("Ao jogo do ano")
time.sleep(0.5)
print("O mais épico")
for i in range(20):
    time.sleep(0.1)
    print("")
print("EPICO JOGO.COM")
for i in range(10):
    time.sleep(0.1)
    print("")
input("Aperte ENTER para começar")

for i in range(99999999):
    if crashou <= 3:
        crashou = random.randint(1,100)
        print("FINAL: CRASHOU")
        print("crashou uai")
        input()
        exit()
    print("Carregando....")
    os.system("python3 jogo.py")
    print()
    print("Digite nada para reiniciar | 2 para sair")
    escolha = input("")
    if escolha == "2":
        exit()