from constraints.constraints_cnf import *
from pysat.formula import IDPool
from default.formula import *

var_pool = IDPool()

# FUNÇÕES AUXILIARES


def and_all(literal_splitt_formulas):
    """
    Returns a BIG AND formula from a literal_splitt of formulas
    For example, if literal_splitt_formulas is [Atom('1'), Atom('p'), Atom('r')], it returns
    And(And(Atom('1'), Atom('p')), Atom('r')).
    :param literal_splitt_formulas: a literal_splitt of formulas
    :return: And formula
    """
    first_formula = literal_splitt_formulas[0]
    del literal_splitt_formulas[0]
    for formula in literal_splitt_formulas:
        first_formula = And(first_formula, formula)
    return first_formula


def or_all(literal_splitt_formulas):
    """
    Returns a BIG OR of formulas from a literal_splitt of formulas.
    For example, if literal_splitt_formulas is [Atom('1'), Atom('p'), Atom('r')], it returns
    Or(Or(Atom('1'), Atom('p')), Atom('r')).
    :param literal_splitt_formulas: a literal_splitt of formulas
    :return: Or formula
    """
    first_formula = literal_splitt_formulas[0]
    del literal_splitt_formulas[0]
    for formula in literal_splitt_formulas:
        first_formula = Or(first_formula, formula)
    return first_formula


def get_rules(result_dict: dict, q_regras):
    rules = {}
    for j in range(q_regras):
        rules[str(j + 1)] = ''
    for attribute in result_dict.keys():
        attribute_split = attribute.plit(',')
        if result_dict[attribute] is True and len(attribute_split) == 3:
            if attribute_split[2] == 'le':
                if rules[attribute_split[1]] == '':
                    rules[attribute_split[1]] = attribute_split[0]
                else:
                    rules[attribute_split[1]] = (rules[attribute_split[1]] + ', ' + attribute_split[0])
            if attribute_split[2] == 'gt':
                if rules[attribute_split[1]] == '':
                    rules[attribute_split[1]] = attribute_split[0][0:2] + ' > ' + attribute_split[0][-5:]
                else:
                    rules[attribute_split[1]] = rules[attribute_split[1]] + ', ' + attribute_split[0][0:2] + ' > ' + attribute_split[0][-5:]
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
        print('Solução não encontrada')
