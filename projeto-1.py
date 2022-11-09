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

linhas = csv.reader(arquivo2)

matriz = []
for linha in linhas:
    matriz.append(linha)

list_for_sat = [rule_1(matriz, 3, 2), rule_2(matriz, 3, 2), rule_3(matriz, 3, 2), rule_4(matriz, 3, 2),
                rule_5(matriz, 3, 2)]

and_all_list = and_all(list_for_sat)

result = satisfiability_brute_force(and_all_list)

get_rules(result, 2)

