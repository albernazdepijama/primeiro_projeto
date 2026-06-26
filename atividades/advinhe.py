import random

numero = random.randint (1,20)
advinhacao = 0
while advinhacao != numero:
 advinhacao= int(input("Advinhe o numero que eu pensei: "))
 if advinhacao < numero:
    print("Muito baixo, tente denovo !")
 elif advinhacao > numero:
    print("Muito alto, tente novamente!")
 else:
    print("Voce acertou, Muito bem!")
    break