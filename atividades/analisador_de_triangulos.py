#Analisador de triangulos
reta01 = float(input("Digite o valor da primeira reta: "))
reta02 = float(input("Digite o segundo valor da reta: "))
reta03 = float(input("Digite o terceiro valor da reta: "))

if reta01 + reta02 < reta03 or reta01 + reta03 < reta02 or reta02 + reta03 < reta01 :
    print("Triangulo invalido")
else:
    print("Triangulo valido")
    if reta01 == reta02 == reta03:
        print("Equilatero")
    elif reta01 != reta02 != reta03:
        print("Escaleno")
    else:
        print("Isosceles")

