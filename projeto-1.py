from rules import *
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
nome_arquivo = 'column_bin_3a_3p.csv'

q_atributos = nome_arquivo[11]

linhas = csv.reader(arquivo)

matriz = []
for linha in linhas:
    matriz.append(linha)

list_for_sat = [rule_1(matriz, int(q_atributos), 2), rule_2(matriz, int(q_atributos), 2),
                rule_3(matriz, int(q_atributos), 2), rule_4(matriz, int(q_atributos), 2),
                rule_5(matriz, int(q_atributos), 2)]

and_all_list = and_all(list_for_sat)

result = satisfiability_brute_force(and_all_list)

#get_rules(result, 2)

