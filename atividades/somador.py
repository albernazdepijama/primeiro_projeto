soma = 0

while True:
    num = int(input("Digite o numero para a soma ser realizada: "))
    if num == 0:
        break
    soma += num
print(f"A soma e: {soma} ")