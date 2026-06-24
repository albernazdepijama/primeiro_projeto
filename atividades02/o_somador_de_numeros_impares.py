#calculadora de numeros impares
soma_do_calculo = 0
for i in range (1,100):
    if i %2 !=0 and i %3 ==0:
        soma_do_calculo += i
        print(i)
print("A soma dos impares multiplos de 3 e igual a ", soma_do_calculo)