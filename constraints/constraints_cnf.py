from utils.utils import *
from pysat.formula import IDPool

var_pool = IDPool()


# RESTRIÇÕES PARA FUNÇÃO EM CNF


def constraint_1_cnf(mat, attributes, q_rules):
    list_to_return = []
    for i in range(q_rules):
        or_list = []
        for j in range(attributes):
            or_list.append(var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'le'))
            or_list.append(var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'))
            or_list.append(var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 's'))
            list_to_return.append([-1 * var_pool.id((mat[0][j] + ',' + str(i + 1) + ',' + 'le')), -1 *
                                   var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'gt')])
            list_to_return.append([
                -1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'le'),
                -1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 's')])
            list_to_return.append([
                -1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'),
                -1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 's')])
        list_to_return.append(or_list)
    return list_to_return


def constraint_2_cnf(mat, attributes, q_rules):
    list_to_return = []
    for i in range(q_rules):
        or_list = []
        for j in range(attributes):
            or_list.append(-1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 's'))
        list_to_return.append(or_list)
    return list_to_return


def constraint_3_cnf(mat, attributes, q_rules):
    list_to_return = []
    for k in range(1, len(mat)):
        if mat[k][attributes] == '0':
            for i in range(q_rules):
                or_list = []
                for j in range(attributes):
                    if mat[k][j] == '0':
                        or_list.append(var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'le'))
                    else:
                        or_list.append(var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'))
                list_to_return.append(or_list)
    return list_to_return


def constraint_4_cnf(mat, attributes, q_rules):
    list_to_return = []
    cont_p = 0
    for k in range(1, len(mat)):
        if mat[k][attributes] == '1':
            cont_p += 1
            for i in range(q_rules):
                for j in range(attributes):
                    if mat[k][j] == '0':
                        list_to_return.append([-1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'le'),
                                               -1 * var_pool.id('C' + str(i + 1) + ',' + str(cont_p))])
                    else:
                        list_to_return.append([-1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'),
                                               -1 * var_pool.id('C' + str(i + 1) + ',' + str(cont_p))])
    return list_to_return


def constraint_5_cnf(mat, attributes, q_rules):
    list_to_return = []
    cont_p = 0
    for k in range(1, len(mat)):
        if mat[k][attributes] == '1':
            cont_p += 1
            or_list = []
            for i in range(q_rules):
                or_list.append(var_pool.id('C' + str(i + 1) + ',' + str(cont_p)))
            list_to_return.append(or_list)
    return list_to_return
