'''     Salário com bônus
    Faça um programa que leia o nome do vendedor, seu salário fixo e o total da venda feito por si mesmo no mês (em dinheiro).
    Considerando que este vendedor recebe 15% sobre todos os produtos vendidos,
    escreva o salário final (total) desse vendedor no final do mês, com duas casas decimais.

    Formato do resultado(saída) Ex: TOTAL = R$ 684.54
'''
nome = input()
salario_fixo = float(input())
total_vendas = float(input())
salario_total = salario_fixo + (total_vendas * 0.15)
print('TOTAL = R$ {:.2f}'.format(salario_total))