from constraints.constraints import *
from default.semantics import *
import csv

# ATRIBUTOS
# ângulo de incidência pélvica (PI)
# ângulo de versão pélvica (PT)
# ângulo de lordose (LA)
# inclinacão sacral (SS)
# raio pélvico (RP)
# grau de deslizamento (GS)


arquivo = open('arquivos_csv/test.csv')

q_atributos = 3

linhas = csv.reader(arquivo)

matriz = []
for linha in linhas:
    matriz.append(linha)

solve_function(matriz, q_atributos, 3)