'''     Área
    Faça um programa que leia três valores de ponto flutuante: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem a base A e a altura C.
b) a área do círculo de raio C (pi = 3,14159)
c) a área do trapézio que tem A e B por base e C por altura.
d) a área do quadrado que possui o lado B.
e) a área do retângulo que possui os lados A e B.

    Formato do resultado(saída) Ex: TRIANGULO: 7.800
                                    CIRCULO: 84.949
                                    TRAPEZIO: 18.200
                                    QUADRADO: 16.000
                                    RETANGULO: 12.000
'''

A, B, C = map(float, input().split(' '))
TRIANGULO = (A * C) / 2
CIRCULO = 3.14159 * C ** 2
TRAPEZIO = ((A + B) * C) /2
QUADRADO = B * B
RETANGULO = A * B
print('TRIANGULO: {:.3f}\n'
      'CIRCULO: {:.3f}\n'
      'TRAPEZIO: {:.3f}\n'
      'QUADRADO: {:.3f}\n'
      'RETANGULO: {:.3f}'.format(TRIANGULO,CIRCULO,TRAPEZIO,QUADRADO,RETANGULO))