# Casar ou Comprar uma Bicicleta?

print (" Casar ou Comprar uma Bicicleta ?")

resposta = input (" Você esta gordo ? s/n: ")

if resposta == "s" :
    quer_emagrecer = input ("Você quer emagrecer ? s/n: ")
    if quer_emagrecer == "s" :
        print ("Compre ums bicicleta!")
    else:
        print("Então case!")
else:
    quer_engordar = input("Você quer engordar ? s/n: ")
    if quer_engordar == "s" :
        print("Então case!")
    else:
        print("Compre ums bicicleta! ")