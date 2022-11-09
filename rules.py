from semantics import *

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

def rule_1(mat, atributos, q_regras):
    list_to_return = []
    for i in range(q_regras):
        list_aux = []
        list_aux2 = []
        for j in range(atributos):
            list_aux.append(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'le'))
            list_aux.append(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'))
            list_aux.append(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 's'))
            temp = or_all(list_aux)
            list_aux2.append(Not(And(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'le'),
                                     Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'))))
            list_aux2.append(
                Not(And(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'le'),
                        Atom(mat[0][j] + ',' + str(i + 1) + ',' + 's'))))
            list_aux2.append(
                Not(And(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 'gt'),
                        Atom(mat[0][j] + ',' + str(i + 1) + ',' + 's'))))
            temp2 = and_all(list_aux2)
            list_to_return.append(And(temp, temp2))
    return and_all(list_to_return)


def rule_2(mat, atributos, q_regras):
    list_to_return = []
    for i in range(q_regras):
        list_aux = []
        for j in range(atributos):
            list_aux.append(Not(Atom(mat[0][j] + ',' + str(i + 1) + ',' + 's')))
        list_to_return.append(or_all(list_aux))
    return and_all(list_to_return)


def rule_3(mat, atributos, q_regras):
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


def rule_4(mat, atributos, q_regras):
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


def rule_5(mat, atributos, q_regras):
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

