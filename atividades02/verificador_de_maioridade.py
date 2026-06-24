maior_de_idade = 0
menor_de_idade = 0

for i in range (1, 8):
    ano01= int(input(f"Digite seu ano de nascimento {i}: "))
    idade = 2026- ano01
    if idade >= 18:
        maior_de_idade +=1
    else:
        menor_de_idade +=1
print(f"Sao de maior {maior_de_idade}")
print(f"Sao de menor {menor_de_idade}")


