# Analise de credito bancario
salario_bruto = float(input("Digite seu salario bruto: "))
parcela_que_deseja_pagar = float(input("Digite o valor da parcela que deseja pagar: "))

taxa_parcela = salario_bruto * 0.3

if taxa_parcela <= parcela_que_deseja_pagar :
    print("Crédito Recusado! ")
else:
    print("Crédito Aprovado! ")