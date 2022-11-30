import csv
from constraints.constraints_cnf import *

arquivo = open('column_bin_3a_2p.csv')
arquivo2 = open('test.csv')
arquivo3 = open('column_bin_3a_3p.csv')
nome_arquivo = 'column_bin_3a_2p.csv'

q_atributos = nome_arquivo[11]

linhas = csv.reader(arquivo)

matriz = []
for linha in linhas:
    matriz.append(linha)

solve_function_cnf(matriz, int(q_atributos), 2)