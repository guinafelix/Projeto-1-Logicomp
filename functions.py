"""The goal in this module is to define functions that take a formula as input and
do some computation on its syntactic structure. """

from formula import *


def length(formula):
    """Determines the length of a formula in propositional logic."""
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return length(formula.inner) + 1
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return length(formula.left) + length(formula.right) + 1


def subformulas(formula):
    """Returns the set of all subformulas of a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for subformula in subformulas(my_formula):
        print(subformula)

    This piece of code prints p, s, (p v s), (p → (p v s))
    (Note that there is no repetition of p)
    """
    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return {formula}.union(subformulas(formula.inner))
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        sub1 = subformulas(formula.left)
        sub2 = subformulas(formula.right)
        return {formula}.union(sub1).union(sub2)


#  we have shown in class that, for all formula A, len(subformulas(A)) <= length(A).


def atoms(formula):

    """Returns the set of all atoms occurring in a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for atom in atoms(my_formula):
        print(atom)

    This piece of code above prints: p, s
    (Note that there is no repetition of p)
    """
    # pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========
    if isinstance(formula, Atom):
        return {formula.__str__()}
    if isinstance(formula, Not):
        return atoms(formula.inner)
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return atoms(formula.left).union(atoms(formula.right))


def number_of_atoms(formula):
    """Returns the number of atoms occurring in a formula.
    For instance,
    number_of_atoms(Implies(Atom('q'), And(Atom('p'), Atom('q'))))

    must return 3 (Observe that this function counts the repetitions of atoms)
    """
    #pass   ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        if isinstance(formula.inner, Atom):
            return 1
        else:
            return number_of_atoms(formula.inner)
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return number_of_atoms(formula.left) + length(formula.right)


def number_of_connectives(formula):
    """Returns the number of connectives occurring in a formula."""
    # pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========
    if isinstance(formula, Not):
        return number_of_connectives(formula.inner) + 1
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return number_of_connectives(formula.left) + number_of_connectives(formula.right) + 1
    if isinstance(formula, Atom):
        return 0


def is_literal(formula):
    """Returns True if formula is a literal. It returns False, otherwise"""
    # pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========
    if isinstance(formula, Atom):
        return True
    elif isinstance(formula, Not):
        return is_literal(formula.inner)
    else:
        return False


def substitution(formula, old_subformula, new_subformula):
    """Returns a new formula obtained by replacing all occurrences
    of old_subformula in the input formula by new_subformula."""
    #pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========
    if isinstance(formula, Atom) and (not (formula.__eq__(old_subformula))):
        return formula
    if formula.__eq__(old_subformula):
        return new_subformula
    if isinstance(formula, Not) and (not formula.__eq__(old_subformula)):
        return Not(substitution(formula.inner, old_subformula, new_subformula))
    if isinstance(formula, And) and (not formula.__eq__(old_subformula)):
        return And(substitution(formula.left, old_subformula, new_subformula), substitution(formula.right, old_subformula, new_subformula))
    if isinstance(formula, Or) and (not formula.__eq__(old_subformula)):
        return Or(substitution(formula.left, old_subformula, new_subformula), substitution(formula.right, old_subformula, new_subformula))
    if isinstance(formula, Implies) and (not formula.__eq__(old_subformula)):
        return Implies(substitution(formula.left, old_subformula, new_subformula), substitution(formula.right, old_subformula, new_subformula))


def is_clause(formula):
    """Returns True if formula is a clause. It returns False, otherwise"""
    #pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========
    if isinstance(formula, Or):
        return is_clause(formula.left) and is_clause(formula.right)
    if is_literal(formula):
        return True
    else:
        return False


def is_negation_normal_form(formula):
    """Returns True if formula is in negation normal form.
    Returns False, otherwise."""
    # pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========
    if isinstance(formula, Not):
        if isinstance(formula.inner, And) or isinstance(formula.inner, Or) or isinstance(formula.inner, Implies):
            return False
        else:
            return True
    if isinstance(formula, And) or isinstance(formula, Or):
        return is_negation_normal_form(formula.left) and is_negation_normal_form(formula.right)
    if isinstance(formula, Atom):
        return True


def is_cnf(formula):
    """Returns True if formula is in conjunctive normal form.
    Returns False, otherwise."""
    #pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========
    if isinstance(formula, And):
        return is_cnf(formula.left) and is_cnf(formula.right)
    elif is_clause(formula):
        return True
    else:
        return False


def is_term(formula):
    """Returns True if formula is a term. It returns False, otherwise"""
    #pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========
    if isinstance(formula, And):
        return is_term(formula.left) and is_term(formula.right)
    elif is_literal(formula):
        return True
    else:
        return False


def is_dnf(formula):
    """Returns True if formula is in disjunctive normal form.
    Returns False, otherwise."""
    #pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========
    if isinstance(formula, Or):
        return is_dnf(formula.left) and is_dnf(formula.right)
    elif is_term(formula):
        return True
    else:
        return False


def is_decomposable_negation_normal_form(formula):
    """Returns True if formula is in decomposable negation normal form.
    Returns False, otherwise."""
    #pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========
    if is_negation_normal_form(formula):
        if isinstance(formula, And):
            if len(set(atoms(formula.left)).intersection(atoms(formula.right))) == 0:
                return True
            else:
                return False
        elif isinstance(formula, Or):
            return is_decomposable_negation_normal_form(formula.left) and is_decomposable_negation_normal_form(formula.right)
    else:
        return False

