'''     Consumo
    Calcule o consumo médio de um carro, fornecendo a distância total percorrida (em Km) e o total de combustível usado (em litros).

    O arquivo de entrada contém dois valores: um valor inteiro X que representa a distância total (em Km)
    e o segundo é um número de ponto flutuante Y que  representa o total de combustível gasto, com um dígito após o ponto decimal.

    Formato do resultado(saída) Ex: 14.286 km/l
'''
X =int(input())
Y = float(input())
CONSUMO = X / Y
print('{:.3f} km/l'.format(CONSUMO))