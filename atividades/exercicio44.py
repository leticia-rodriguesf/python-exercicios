print('=-=-=-=-=-'*5)
print('             LOJAS AMERICANAS   ')
print('=-=-=-=-=-'*5)
produto = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão ''')
opção = int(input('Qual é a opção: '))
if opção == 1:
    desconto = produto - (produto * (10/100))
    print('-> PRODUTO: R${},00'.format(produto))
    print('-> TOTAL A PAGAR (com desconto): R${},00'.format(desconto))
elif opção == 2:
    desconto = produto - (produto * (5/100))
    print('-> PRODUTO: R${:.2f}'.format(produto))
    print('-> TOTAL A PAGAR (com desconto): R${},00'.format(desconto))
elif opção == 3:
    parcela = produto/2
    print('-> PRODUTO: R${:.2f}'.format(produto))
    print('-> TOTAL A PAGAR (com parcelas de 2x): R${},00'.format(parcela))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = (produto) + (produto* (20/100))
    parcela = total / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, parcela))
    print('No final, você irá pagar R${:.2f}'.format(total))
else:
    print('Opção inválida.')