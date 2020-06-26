'''     Distância entre dois pontos
   Leia os quatro valores correspondentes aos eixos x e y de dois pontos no plano, p1 (x1, y1) e p2 (x2, y2) e
   calcule a distância entre eles, mostrando quatro casas decimais após a vírgula, de acordo com a fórmula :
   Distancia = math.sqrt(((math.pow(x2), 2) - (math.pow(x1), 2)) + ((math.pow(y2), 2) - (math.pow(y1), 2)))

    Formato do resultado(saída) Ex: 4.4721
'''

x1, y1 = input().split()
x2, y2 = input().split()
x1, y1, x2, y2 = float(x1),float(y1),float(x2),float(y2)

distancia = (pow((x2 - x1), 2) + pow((y2 - y1),2)) ** 0.5
print('{:.4f}'.format(distancia))

