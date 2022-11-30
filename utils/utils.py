from utils.utils import *
from default.semantics import *
from constraints.constraints_cnf import *
from pysat.formula import IDPool


var_pool = IDPool()

# FUNÇÕES AUXILIARES


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


def pretty_formula_printer(formula):
    for clause in formula:
        for literal in clause:
            if literal > 0:
                print(var_pool.obj(literal), ' ',  end='')
            else:
                print('Not', var_pool.obj(literal*-1), ' ',  end='')
        print('')


def print_solution(formula):
    for literal in formula:
        if literal > 0:
            print(var_pool.obj(literal), ' ',  end = '')
        else:
            print('Not', var_pool.obj(literal*-1), ' ',  end = '')
    print('')


def get_rules_cnf(formula, q_regras):
    rules = {}
    for j in range(q_regras):
        rules[str(j + 1)] = ''
    for literal in formula:
        lis = str(var_pool.obj(literal)).split(',')
        if literal > 0 and len(lis) == 3:
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


def solve_function_cnf(mat, q_atributos, q_regras):
    clauses1 = constraint_1_cnf(mat, int(q_atributos), q_regras)
    clauses2 = constraint_2_cnf(mat, int(q_atributos), q_regras)
    clauses3 = constraint_3_cnf(mat, int(q_atributos), q_regras)
    clauses4 = constraint_4_cnf(mat, int(q_atributos), q_regras)
    clauses5 = constraint_5_cnf(mat, int(q_atributos), q_regras)
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
        print('Solução não encontrada')
