from constraints import constraints
from default.semantics import *
from default.formula import *

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
        attribute_split = attribute.split(',')
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


def solve_function(matriz, q_atributos, q_regras):
    list_for_solution = [constraints.constraint_1(matriz, int(q_atributos), q_regras),
                         constraints.constraint_2(matriz, int(q_atributos), q_regras),
                         constraints.constraint_3(matriz, int(q_atributos), q_regras),
                         constraints.constraint_4(matriz, int(q_atributos), q_regras),
                         constraints.constraint_5(matriz, int(q_atributos), q_regras)]

    and_all_list = and_all(list_for_solution)
    result = satisfiability_brute_force(and_all_list)
    get_rules(result, q_regras)