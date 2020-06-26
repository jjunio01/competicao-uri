'''     O Maior
    Faça um programa que leia 3 valores inteiros e apresente o maior, seguido da mensagem "eh o maior".
    Use a seguinte fórmula:

            MaiorAB = (a + b + abs(a-b)) / 2

    O arquivo de entrada contém 3 valores inteiros.

    Formato do resultado(saída) Ex: 106 eh o maior
'''

A, B, C = map(int, input().split(' '))
MaiorAB = (A + B + abs(A-B)) / 2
Maior = (MaiorAB + C + abs(MaiorAB - C)) / 2
print('{} eh o maior'.format(int(Maior)))