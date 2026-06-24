#while
continuar = "S"

while continuar.lower()== "s":
    num = float(input("Digite um numero : "))
    print(num %2)
    if num %2 == 0:
        print("Par")
    else:
        print("Impar")
continuar = input("Deseja continuar ? ")