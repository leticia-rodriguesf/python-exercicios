print('=='*20)
preco = float(input('Digite o preço do produto: ' ))
desconto = preco - (preco * (5/100) )
print('O produto com o desconto é R$ {:.2f},00!'.format(desconto))
print('=='*20)