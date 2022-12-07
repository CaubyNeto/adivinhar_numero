import random
while True:
    topo = input("Digite um número para ser o topo do seu palpite: ")
    if topo.isdigit():
        topo = int(topo)
        if topo < 0:
            print("Por favor, digite um número maior que 0.")
        else:
            print("Certo!")
            break
    else:
        print("Por favor, digite um número.")
numero_aleatorio = random.randint(0, topo)

while True:
    palpite = input("Digite um número: ")
    if palpite.isdigit():
        palpite = int(palpite)
    else:
        print("Por favor, digite um número.")
    if palpite == numero_aleatorio:
        print("Você acertou!")
        break
    elif palpite < numero_aleatorio:
        print("Muito baixo. Tente novamente.")
    else:
        print("Muito alto. Tente novamente.")

