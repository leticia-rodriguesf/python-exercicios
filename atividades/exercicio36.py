casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Salário do comprador: R$ '))
ano = int(input('Quantos anos de financiamento? '))
prestacao = (casa / (ano*12))
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, ano,prestacao))
minimo = salario * (30/100)
if prestacao <= minimo:
    print('EMPRESTIMO CONCEDIDO')
else:
    print('EMPRESTIMO NEGADO')