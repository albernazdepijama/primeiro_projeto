# Validador de acesso a conteudo

ano_de_nascimento = int(input("Digite seu ano de nascimento: "))

idade = 2026 - ano_de_nascimento

if idade >= 16:
    print(" Acesso ao filme liberado!")
else:
    print(" Acesso bloqueado: Conteúdo não recomendado para menores de 16 anos.")




