from formula import *
from functions import *
from semantics import *
import csv

#ATRIBUTOS
# ângulo de incidência pélvica (PI)
# ângulo de versão pélvica (PT)
# ângulo de lordose (LA)
# inclinacão sacral (SS)
# raio pélvico (RP)
# grau de deslizamento (GS)

#FUNÇÕES AUXILIARES
def and_all(list_formulas):
    """
    Returns a BIG AND formula from a list of formulas
    For example, if list_formulas is [Atom('1'), Atom('p'), Atom('r')], it returns
    And(And(Atom('1'), Atom('p')), Atom('r')).
    :param list_formulas: a list of formulas
    :return: And formula
    """
    first_formula = list_formulas[0]
    del list_formulas[0]
    for formula in list_formulas:
        first_formula = And(first_formula, formula)
    return first_formula


def or_all(list_formulas):
    """
    Returns a BIG OR of formulas from a list of formulas.
    For example, if list_formulas is [Atom('1'), Atom('p'), Atom('r')], it returns
    Or(Or(Atom('1'), Atom('p')), Atom('r')).
    :param list_formulas: a list of formulas
    :return: Or formula
    """
    first_formula = list_formulas[0]
    del list_formulas[0]
    for formula in list_formulas:
        first_formula = Or(first_formula, formula)
    return first_formula

arquivo = open('column_bin_3a_2p.csv')
linhas = csv.reader(arquivo)

matriz = []
for linha in linhas:
    matriz.append(linha)


def rule_2(mat, atributos, q_regras):
    list_to_return = []
    for i in range(q_regras):
        for j in range(atributos):
            list_to_return.append(Not(Atom(mat[0][j] + ',' + str(i+1) + ',' + 's')))
    return list_to_return


def rule_3(mat, atributos, q_regras):
    list_to_return = []
    for k in range(1, len(mat)):
        if mat[k][q_regras + 1] == '0':
            for i in range(q_regras):
                for j in range(atributos):
                    if j >= atributos - 2:
                        list_to_return.append(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'))
                    else:
                        list_to_return.append(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'le'))
    return or_all(list_to_return)


def rule_4(mat, atributos, q_regras):
    list_to_return = []
    cont_p = 0
    for k in range(1, len(mat)):
        if mat[k][atributos] == '1':
            cont_p += 1
            for i in range(q_regras):
                for j in range(atributos):
                    if mat[k][j] == '0':
                        list_to_return.append(Implies(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'le'), Not(Atom('C' + str(i+1) + ',' + str(cont_p)))))
                    else:
                        list_to_return.append(Implies(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'),
                                                      Not(Atom('C' + str(i+1) + ',' + str(cont_p)))))
    return list_to_return


def rule_5(mat, atributos, q_regras):
    list_to_return = []
    cont_p = 0
    for k in range(1, len(mat)):
        if mat[k][atributos] == '1':
            cont_p += 1
            for i in range(q_regras):
                list_to_return.append(Atom('C' + str(i + 1) + ',' + str(cont_p)))
    return list_to_return


test = rule_5(matriz, 3, 2)
for a in test:
    print(a)
