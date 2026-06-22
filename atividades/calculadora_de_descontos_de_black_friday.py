#calculadora de desconto


valor_total_da_compra = float(input("Digite o valor da compra aqui: "))

if valor_total_da_compra <=100 :
    print("Nao ha Descontos Disponiveis ")
elif valor_total_da_compra <= 300 :
    print (f"5% de desconto, valor da compra {valor_total_da_compra}, valor do desconto{valor_total_da_compra * 5 / 100}, total a pagar {valor_total_da_compra -(valor_total_da_compra * 5 / 100)}")
elif valor_total_da_compra <= 500 :
    print(f"10% de desconto, valor da compra{valor_total_da_compra}, valor do desconto {valor_total_da_compra * 10 / 100}, total a pagar {valor_total_da_compra -(valor_total_da_compra * 10 / 100)}")
else:
    print(
        f"15% de desconto, valor da compra {valor_total_da_compra}, valor do desconto {valor_total_da_compra * 15 / 100}, total a pagar {valor_total_da_compra - (valor_total_da_compra * 15 / 100)}")