import random

def palpite(x):
    numero_aleatorio = random.randint(1, x)
    palpite = 0
    contagem_de_palpite = 0
    fora_de_palpite = False
    while palpite != numero_aleatorio and not(fora_de_palpite):
        if contagem_de_palpite < 10:
            palpite = int(input(f'Adivinhe um número entre 1 e {x}: '))
            if palpite < numero_aleatorio:
                print("Muito baixo. Tente novamente.")
            elif palpite > numero_aleatorio:
                print("Muito alto. Tente novamente")
            contagem_de_palpite += 1
        else:
            fora_de_palpite = True
    if fora_de_palpite:
        print("Você alcançou o limite de palpites. Você perdeu.")
    else:
        print("Parabéns. Você adivinhou o número.")

palpite(random.randint(1, 20))
