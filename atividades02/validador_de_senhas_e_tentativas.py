numero_da_senha = 99678
for i in range (3):
    senha = int(input(f"Digite a sua senha: "))
    if senha == numero_da_senha :
        print("Senha correta")
        break
else:
    print("Conta bloqueada")