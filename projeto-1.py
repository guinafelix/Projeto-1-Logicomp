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

linhas = csv.reader(arquivo3)

matriz = []
for linha in linhas:
    matriz.append(linha)

list_for_sat = [rule_1(matriz, 3, 2), rule_2(matriz, 3, 2), rule_3(matriz, 3, 2), rule_4(matriz, 3, 2),
                rule_5(matriz, 3, 2)]

andall = and_all(list_for_sat)
#print(andall)
result = satisfiability_brute_force(andall)


def get_rules(result_dict: dict, q_regras):
    rules = {}
    for j in range(q_regras):
        rules[str(j + 1)] = ''
    for a in result_dict.keys():
        lis = a.split(',')
        if result_dict[a] is True and len(lis) == 3:
            if lis[2] == 'le':
                if rules[lis[1]] == '':
                    rules[lis[1]] = lis[0]
                else:
                    rules[lis[1]] = (rules[lis[1]] + ', ' + lis[0])
            if lis[2] == 'gt':
                if rules[lis[1]] == '':
                    rules[lis[1]] = lis[0][0:2] + ' > ' + lis[0][-5:]
                else:
                    rules[lis[1]] = rules[lis[1]] + ', ' + lis[0][0:2] + ' > ' + lis[0][-5:]
    return print_rules(rules)


def print_rules(rules: dict):
    for a in rules.keys():
        print('[' + rules[a] + ']' + ' => P')


get_rules(result, 2)
# print(rule_4(matriz, 3, 2).__str__())
