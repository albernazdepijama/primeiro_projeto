# Tabuada
# no inicio podemos utilizar o mesmo principio do if e else


numero = int(input("digite o numero da tabuada que deseja : "))
print(f"Tabuada de {numero}: ")

# para repetir um bloco numero especifico de vezes, usamos a funcao range (fim) ou range (inicio, fim)
#repete 3 vezes (de 0 a 2)
#for i in range (3)
#print (f"Contagem : {i}")
for i in range (1, 11): #sempre que eu quiser que ele conte ate onde eu quero eu preciso adicionar um numero a mais
    print(f"{numero} x {i} = {numero*i}")
