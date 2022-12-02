from utils.utils import *
from pysat.formula import IDPool, CNF
from pysat.solvers import Cadical


var_pool = IDPool()


# RESTRIÇÕES PARA FUNÇÃO EM CNF


def constraint_1_cnf(mat, attributes, q_rules):
    list_to_return = []
    for i in range(q_rules):
        or_list = []
        for j in range(attributes):
            list_to_return.append([
                var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'le'),
                var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'),
                var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 's')
            ])
            list_to_return.append([
                -1 * var_pool.id((mat[0][j] + ',' + str(i + 1) + ',' + 'le')),
                -1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'gt')])
            list_to_return.append([
                -1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'le'),
                -1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 's')])
            list_to_return.append([
                -1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'),
                -1 * var_pool.id(mat[0][j] + ',' + str(i + 1) + ',' + 's')])
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


def pretty_formula_printer(formula):
    for clause in formula:
        for literal in clause:
            if literal > 0:
                print(var_pool.obj(literal), ' ',  end='')
            else:
                print('Not', var_pool.obj(literal*-1), ' ',  end='')
        print('')


def print_solution(formula):
    print(f"SOLUÇÃO:  \n"
          f"{formula}")
    print()
    for literal in formula:
        if literal > 0:
            print(var_pool.obj(literal), ' ',  end='')
        else:
            print('Not', var_pool.obj(literal*-1), ' ',  end='')
    print('')


def get_rules_cnf(formula, q_regras):
    rules = {}
    for j in range(q_regras):
        rules[str(j + 1)] = ''
    for literal in formula:
        literal_split = str(var_pool.obj(literal)).split(',')
        if literal > 0 and len(literal_split) == 3:
            if literal_split[2] == 'le':
                if rules[literal_split[1]] == '':
                    rules[literal_split[1]] = literal_split[0]
                else:
                    rules[literal_split[1]] = (rules[literal_split[1]] + ', ' + literal_split[0])
            if literal_split[2] == 'gt':
                if rules[literal_split[1]] == '':
                    rules[literal_split[1]] = literal_split[0][0:2] + ' > ' + literal_split[0][-5:]
                else:
                    rules[literal_split[1]] = rules[literal_split[1]] + ', ' + literal_split[0][0:2] + ' > ' + literal_split[0][-5:]
    return print_rules(rules)


def solve_function_cnf(mat, q_attribute, q_regras):
    clauses1 = constraint_1_cnf(mat, int(q_attribute), q_regras)
    clauses2 = constraint_2_cnf(mat, int(q_attribute), q_regras)
    clauses3 = constraint_3_cnf(mat, int(q_attribute), q_regras)
    clauses4 = constraint_4_cnf(mat, int(q_attribute), q_regras)
    clauses5 = constraint_5_cnf(mat, int(q_attribute), q_regras)
    clauses = clauses1 + clauses2 + clauses3 + clauses4 + clauses5
    cnf = CNF(from_clauses=clauses)

    solver = Cadical()
    solver.append_formula(cnf.clauses)

    if solver.solve():
        solution = solver.get_model()
        print_solution(solution)
        get_rules_cnf(solution, q_regras)
        print(f'Time to solve: {solver.time()}')
    else:
        print('Solução não encontrada.')
