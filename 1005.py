'''     Razoável 1
    Ler dois valores de ponto flutuante e armazenar nas variáves A e B, que correspondem a duas notas.
    Calcular a média considerando que a nota A tem peso 3.5 e a nota B 7.5

    Obs. As notas podem variar de 0.0 a 10.0 sempre com uma casa decimal.

    Formato do resultado(saída) Ex: MEDIA = 10.00000
'''

A = float(input())
B = float(input())
MEDIA = (A * 3.5 + B *7.5) / 11.0
print('MEDIA = {:.5f}'.format(MEDIA))