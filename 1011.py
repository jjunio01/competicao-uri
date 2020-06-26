'''     Esfera
    Faça um programa que calcule e mostre o volume de uma esfera que recebe o valor de seu raio (R).
    A fórmula para calcular o volume é: (4/3) * pi * R 3 . Considere (atribuir) para pi o valor 3,14159.

    Dica: Use (4 / 3.0) ou (4.0 / 3) em sua fórmula, porque alguns idiomas (incluindo C ++) assumem que
    o resultado da divisão entre dois números inteiros é outro número inteiro.

    Formato do resultado(saída) Ex: VOLUME = 113.097
'''
R = float(input())
VOLUME = (4 / 3.0) * 3.14159 * (R ** 3)
print('VOLUME = {:.3f}'.format(VOLUME))