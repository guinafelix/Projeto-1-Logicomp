from pysat.formula import IDPool
from pysat.formula import CNF
from pysat.solvers import Cadical
from utils.utils import *

var_pool = IDPool()

#RESTRIÇÕES PARA FUNÇÃO EM CNF


def constraint_1_cnf(mat, atributos, q_regras):
    list_to_return = []
    for i in range(q_regras):
        or_list = []
        for j in range(atributos):
            or_list.append(var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'le'))
            or_list.append(var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'))
            or_list.append(var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 's'))
            list_to_return.append([-1 * var_pool.id((mat[0][j] + ',' + str(i + 1) + ',' + 'le')), -1 *
                              var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'gt')])
            list_to_return.append([
               -1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'le'), -1 *
                    var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 's')])
            list_to_return.append([
                -1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'),
                        -1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 's')])
        list_to_return.append(or_list)
    return list_to_return


def constraint_2_cnf(mat, atributos, q_regras):
    list_to_return = []
    for i in range(q_regras):
        or_list = []
        for j in range(atributos):
            or_list.append(-1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 's'))
        list_to_return.append(or_list)
    return list_to_return


def constraint_3_cnf(mat, atributos, q_regras):
    list_to_return = []
    for k in range(1, len(mat)):
        if mat[k][atributos] == '0':
            for i in range(q_regras):
                or_list = []
                for j in range(atributos):
                    if mat[k][j] == '0':
                        or_list.append(var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'le'))
                    else:
                        or_list.append(var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'))
                list_to_return.append(or_list)
    return list_to_return


def constraint_4_cnf(mat, atributos, q_regras):
    list_to_return = []
    cont_p = 0
    for k in range(1, len(mat)):
        if mat[k][atributos] == '1':
            cont_p += 1
            for i in range(q_regras):
                for j in range(atributos):
                    if mat[k][j] == '0':
                        list_to_return.append([-1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'le'),
                                                -1 * var_pool.id('C' + str(i + 1) + ',' + str(cont_p))])
                    else:
                        list_to_return.append([-1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'),
                                               -1 * var_pool.id('C' + str(i + 1) + ',' + str(cont_p))])
    return list_to_return


def constraint_5_cnf(mat, atributos, q_regras):
    list_to_return = []
    cont_p = 0
    for k in range(1, len(mat)):
        if mat[k][atributos] == '1':
            cont_p += 1
            or_list = []
            for i in range(q_regras):
                or_list.append(var_pool.id('C' + str(i + 1) + ',' + str(cont_p)))
            list_to_return.append(or_list)
    return list_to_return




