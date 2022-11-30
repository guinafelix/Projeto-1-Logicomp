from utils.utils import *
from default.formula import *

# RESTRIÇÕES


def constraint_1(mat, atributos, q_regras):
    list_to_return = []
    for i in range(q_regras):
        or_list = []
        and_list = []
        for j in range(atributos):
            or_list.append(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'le'))
            or_list.append(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'))
            or_list.append(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 's'))
            temp = or_all(or_list)
            and_list.append(Not(And(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'le'),
                                    Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'))))
            and_list.append(
                Not(And(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'le'),
                        Atom(mat[0][j] + ',' + str(i + 1) + ',' + 's'))))
            and_list.append(
                Not(And(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'),
                        Atom(mat[0][j] + ',' + str(i + 1) + ',' + 's'))))
            temp2 = and_all(and_list)
            list_to_return.append(And(temp, temp2))
            or_list.clear()
            and_list.clear()
    return and_all(list_to_return)


def constraint_2(mat, atributos, q_regras):
    list_to_return = []
    for i in range(q_regras):
        list_aux = []
        for j in range(atributos):
            list_aux.append(Not(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 's')))
        list_to_return.append(or_all(list_aux))
    return and_all(list_to_return)


def constraint_3(mat, atributos, q_regras):
    list_to_return = []
    for k in range(1, len(mat)):
        if mat[k][atributos] == '0':
            for i in range(q_regras):
                list_aux = []
                for j in range(atributos):
                    if mat[k][j] == '0':
                        list_aux.append(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'le'))
                    else:
                        list_aux.append(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'))
                list_to_return.append(or_all(list_aux))
    return and_all(list_to_return)


def constraint_4(mat, atributos, q_regras):
    list_to_return = []
    cont_p = 0
    for k in range(1, len(mat)):
        if mat[k][atributos] == '1':
            cont_p += 1
            list_aux = []
            for i in range(q_regras):
                for j in range(atributos):
                    if mat[k][j] == '0':
                        list_aux.append(Implies(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'le'),
                                                Not(Atom('C' + str(i + 1) + ',' + str(cont_p)))))
                    else:
                        list_aux.append(Implies(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'),
                                                Not(Atom('C' + str(i + 1) + ',' + str(cont_p)))))
            list_to_return.append(and_all(list_aux))
    return and_all(list_to_return)


def constraint_5(mat, atributos, q_regras):
    list_to_return = []
    cont_p = 0
    for k in range(1, len(mat)):
        if mat[k][atributos] == '1':
            cont_p += 1
            list_aux = []
            for i in range(q_regras):
                list_aux.append(Atom('C' + str(i + 1) + ',' + str(cont_p)))
            list_to_return.append(or_all(list_aux))
    return and_all(list_to_return)
