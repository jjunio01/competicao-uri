'''     Calcular Simples
    Nesse problema, a tarefa é ler o código de um produto 1, o número de unidades do produto 1, o preço de uma unidade do produto 1,
    o código de um produto 2, o número de unidades do produto 2 e o preço para uma unidade do produto 2.
    Depois disso, calcule e mostre o valor a ser pago.

    O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores:
    dois inteiros e um valor flutuante com 2 dígitos após o ponto decimal.

    Formato do resultado(saída) Ex: VALOR A PAGAR: R$ 15.50
'''

codigo1, quant_produto1, valor_unitario1 = input().split(' ')
codigo2, quant_produto2, valor_unitario2 = input().split(' ')
preco_total = int(quant_produto1) * float(valor_unitario1) + int(quant_produto2) * float(valor_unitario2)
print('VALOR A PAGAR: R$ {:.2f}'.format(preco_total))