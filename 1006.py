'''     Razoável 2
    Ler três valores de ponto flutuante e armazenar nas variáves A, B e C, que correspondem a três notas.
    Calcular a média considerando que a nota A tem peso 2, a nota B tem peso 3 e a nota C peso 5.

    Obs. As notas podem variar de 0.0 a 10.0 sempre com uma casa decimal.

    Formato do resultado(saída) Ex: MEDIA = 10.0
'''
A = float(input())
B = float(input())
C = float(input())
MEDIA = (A * 2 + B * 3 + C * 5) / 10
print('MEDIA = {:.1f}'.format(MEDIA))
