from formula import *
from functions import *
from semantics import *

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

print("a")