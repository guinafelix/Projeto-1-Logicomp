"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """

from formula import *
from functions import atoms


def truth_value(formula, interpretation: dict):
    """Determines the truth value of a formula in an interpretation (valuation).
    An interpretation may be defined as dictionary. For example, {'p': True, 'q': False}.
    """
    if isinstance(formula, Atom):
        if interpretation.__contains__(formula.__str__()):
            return interpretation[formula.__str__()]
        else:
            return None
    if isinstance(formula, Not):
        if interpretation.__contains__(formula.__str__()):
            return interpretation[formula.inner]
        else:
            return None
    if isinstance(formula, And):
        if (truth_value(formula.left, interpretation) is None) or (truth_value(formula.right, interpretation) is None):
            return None
        else:
            return truth_value(formula.left, interpretation) and truth_value(formula.right, interpretation)
    if isinstance(formula, Or):
        return truth_value(formula.left, interpretation) or truth_value(formula.right, interpretation)
    if isinstance(formula, Implies):
        if (truth_value(formula.left, interpretation) is True) and (
                truth_value(formula.right, interpretation) is False):
            return False
        if (truth_value(formula.left, interpretation) is None) or (truth_value(formula.right, interpretation) is None):
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
    for a in interpretation.keys():
        list_atoms.remove(a.__str__())
    return sat(formula, list_atoms.copy(), interpretation)



def pre_process(formula):
    if isinstance(formula, Atom):
        return {formula.__str__(): True}
    if isinstance(formula, Not):
        return {formula.inner: False}
    if isinstance(formula, And):
        left = pre_process(formula.left)
        right = pre_process(formula.right)
        if left and right is not None:
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
