import random
print("")
arquivo = open("save.txt", "w")

a = int(random.randint(1, 10))
b = int(random.randint(1, 10))

def jogo():
    if b > a:
        print("B é maior que A")
    elif b == a:
        print("A e B são iguais")
    elif b < a:
        print("A é maior que B")

    c = int(a + b)
    print(f"A + B é {c}")
    print(f"A * B é {a * b}")
    print()
    ra = int(input("O que A é? "))
    if ra == a:
        rb = int(input("Boa! E B? O que é a B? "))
        if rb == b:
            arquivo.write("feito = 1")
            input(f"Parabens! Você descobriu que A = {a} e B = {b}")
            print("")
        else:
            perdeu()
    else:
        perdeu()

def perdeu():
    print("Você errou")
    print("")
    arquivo.write("feito = 2")
jogo()
arquivo.close()