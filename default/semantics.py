"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """

from default.formula import *
from default.functions import atoms, is_literal


def truth_value(formula, interpretation: dict):
    """Determines the truth value of a formula in an interpretation (valuation).
    An interpretation may be defined as dictionary. For example, {'p': True, 'q': False}.
    """
    left = Formula
    right = Formula
    if isinstance(formula, And) or isinstance(formula, Or) or isinstance(formula, Implies):
        left = truth_value(formula.left, interpretation)
        right = truth_value(formula.right, interpretation)
    if isinstance(formula, Atom):
        if interpretation.__contains__(formula.__str__()):
            return interpretation[formula.__str__()]
        else:
            return None
    if isinstance(formula, Not):
        temp = formula.inner
        if isinstance(temp, And) or isinstance(temp, Or) or isinstance(temp, Implies):
            return not truth_value(temp, interpretation)
        if isinstance(temp, Atom):
            if interpretation.__contains__(temp.__str__()):
                return not interpretation[temp.__str__()]
            else:
                return None
    if isinstance(formula, And):
        if left is None or right is None:
            return None
        else:
            return left and right
    if isinstance(formula, Or):
        return left or right
    if isinstance(formula, Implies):
        if left is True and right is False:
            return False
        if left is None or right is None:
            return None
        else:
            return True


def is_logical_consequence(premises, conclusion):  # function TT-Entails? in the book AIMA.
    """Returns True if the conclusion is a logical consequence of the set of premises. Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========


def is_logical_equivalence(formula1, formula2):
    """Checks whether formula1 and formula2 are logically equivalent."""
    pass
    # ======== YOUR CODE HERE ========


def is_valid(formula):
    """Returns True if formula is a logically valid (tautology). Otherwise, it returns False"""
    pass
    # ======== YOUR CODE HERE ========


def satisfiability_brute_force(formula):
    """Checks whether formula is satisfiable.
    In other words, if the input formula is satisfiable, it returns an interpretation that assigns true to the formula.
    Otherwise, it returns False."""
    list_atoms = atoms(formula)
    interpretation = pre_process(formula)
    if interpretation is not {}:
        for a in interpretation.keys():
            list_atoms.remove(a.__str__())
    return sat(formula, list_atoms.copy(), interpretation)



def pre_process(formula):
    if isinstance(formula, Atom):
        return {formula.__str__(): True}
    if isinstance(formula, Not):
        a = formula.inner
        if isinstance(a, Atom):
            return {a.__str__(): False}
        else:
            return {}
    elif isinstance(formula, And):
        left = pre_process(formula.left)
        right = pre_process(formula.right)
        if left is not {} and right is not {}:
            return {**left, **right}
    else:
        return {}


def sat(formula, atoms_f, interpretation: dict):
    if not atoms_f:
        if truth_value(formula, interpretation):
            return interpretation
        else:
            return False
    atom = atoms_f.pop()
    interpretation1 = {**interpretation.copy(), **{atom: True}}
    interpretation2 = {**interpretation.copy(), **{atom: False}}
    result = sat(formula, atoms_f.copy(), interpretation1)
    if result:
        return result
    return sat(formula, atoms_f.copy(), interpretation2)


def implication_free(formula):
    if isinstance(formula, Implies):
        left = implication_free(formula.left)
        right = implication_free(formula.right)
        return Or(Not(left), right)
    if isinstance(formula, And):
        return And(implication_free(formula.left), implication_free(formula.right))
    if isinstance(formula, Or):
        return Or(implication_free(formula.left), implication_free(formula.right))
    if isinstance(formula, Not):
        return Not(implication_free(formula))
    if isinstance(formula, Atom):
        return formula


def negation_normal_form(formula):
    if is_literal(formula):
        return formula
    if isinstance(formula, Not) and isinstance(formula.inner, Not):
        return negation_normal_form(formula.inner)
    if isinstance(formula, And):
        return And(negation_normal_form(formula.left), negation_normal_form(formula.right))
    if isinstance(formula, Or):
        return Or(negation_normal_form(formula.left), negation_normal_form(formula.right))
    if isinstance(formula, Not) and isinstance(formula.inner, And):
        return Or(negation_normal_form(Not(formula.left)), negation_normal_form(Not(formula.right)))
    if isinstance(formula, Not) and isinstance(formula.inner, Or):
        return And(negation_normal_form(Not(formula.left)), negation_normal_form(Not(formula.right)))


def distributive(formula):
    if is_literal(formula):
        return formula
    if isinstance(formula, And):
        return And(distributive(formula.left), distributive(formula.right))
    if isinstance(formula, Or):
        left = distributive(formula.left)
        right = distributive(formula.right)
        if isinstance(left, And):
            return And(distributive(Or(left.left, right)), distributive(Or(left.right, right)))
        if isinstance(right, And):
            return And(distributive(Or(right.left, left)), distributive(Or(right.right, left)))
        return Or(left, right)


def to_cnf(formula):
    b = implication_free(formula)
    c = negation_normal_form(b)
    d = distributive(c)
    return d
