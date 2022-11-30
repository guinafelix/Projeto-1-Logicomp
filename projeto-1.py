from constraints.constraints import *
import csv

# ATRIBUTOS
# ângulo de incidência pélvica (PI)
# ângulo de versão pélvica (PT)
# ângulo de lordose (LA)
# inclinacão sacral (SS)
# raio pélvico (RP)
# grau de deslizamento (GS)


arquivo = open('column_bin_3a_2p.csv')
arquivo2 = open('test.csv')
arquivo3 = open('column_bin_3a_3p.csv')
nome_arquivo = 'column_bin_3a_2p.csv'

q_atributos = nome_arquivo[11]

linhas = csv.reader(arquivo)

matriz = []
for linha in linhas:
    matriz.append(linha)

list_for_sat = [constraint_1(matriz, int(q_atributos), 2), constraint_2(matriz, int(q_atributos), 2),
              constraint_3(matriz, int(q_atributos), 2), constraint_4(matriz, int(q_atributos), 2),
              constraint_5(matriz, int(q_atributos), 2)]

and_all_list = and_all(list_for_sat)
print(constraint_4(matriz, int(q_atributos), 2).__str__())
result = satisfiability_brute_force(and_all_list)
form = constraint_1(matriz, int(q_atributos), 2)
print(form.__str__())
get_rules(result, 2)

