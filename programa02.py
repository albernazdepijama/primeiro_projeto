nome = input ("Digite seu nome: ") #input e o que vc vai pedir para o usuario digitar
#idade = input ("Digite a sua idade: ")
nome2 = input ("Digite o nome do seu melhor amigo: ")

print(f"Ola {nome}, seja bem vindo ao  meu programa")
ano_nascimento = int ( input(f"Prazer em te conhecer {nome}, \nDigite seu ano de nascimento: "))
idade = 2026 - ano_nascimento
print(f"Parabens por seus {idade} anos")
print(f"o seu melhor amigo e {nome2}")