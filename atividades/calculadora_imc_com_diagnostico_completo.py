#CALCULADORA IMC
peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

calculo = peso / (altura * altura)
print(f"O calculo do Imc e: {calculo :.2f} ")
if calculo < 18.5 :
    print("Abaixo do peso")
elif calculo < 24.9 :
    print("Peso ideal")
elif calculo < 29.9 :
    print("Levemente acima do peso")
elif calculo < 34.9 :
    print("Obesidade grau um")
else :
    print("obesidade morbida")