import csv
from constraints.constraints_cnf import *

arquivo = open('arquivos_csv/column_bin_3a_6p.csv')

q_atributos = 3

linhas = csv.reader(arquivo)

matriz = []
for linha in linhas:
    matriz.append(linha)

solve_function_cnf(matriz, int(q_atributos), 3)
