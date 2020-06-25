'''     Salário
    Escreva um programa que leia o número de um funcionário, o número de horas trabalhadas em um mês
    e o valor que ele recebeu por hora.
    Imprima o número e o salário do funcionário que ele receberá no final do mês, com duas casas decimais.

    Formato do resultado(saída) Ex: NÚMERO = 25
                                    SALÁRIO = U $ 550,00
'''
numero = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())
SALARIO = horas_trabalhadas * valor_hora

print('NUMBER = {}\n'
      'SALARY = U$ {:.2f}'.format(numero, SALARIO))