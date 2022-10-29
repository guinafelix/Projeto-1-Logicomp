from formula import *
from functions import *
from semantics import *

#print(f"Numero de conectivos: {number_of_connectives(Implies(Not(Atom('p')), Not(Atom('q'))))}")
#print(f"Numero de conectivos: {number_of_connectives(And(Atom('p'), Atom('q')))}")
#print(f"Atoms: {atoms(Or(And(Atom('p'), Not(Implies(Atom('p'), Not(Atom('q'))))), Not(Atom('q'))))}")
#print(f"is negation normal form: {is_negation_normal_form(Or(Not(And(Atom('p'), Atom('s'))), Atom('p')))}")
#print(is_negation_normal_form(Not(And(Atom('a'), Atom('b')))))
#print(f"number of atoms: {number_of_atoms(And(Atom('p'), Atom('q')))}")
#print(f"Is Literal: {is_literal(Not(And(Atom('a'), Atom('b'))))}")
#print(f"Is Term: {is_term(Or(Not(Atom('p')), Atom('r')))}")
#print(f"Is Clause: {is_clause()}")
#print(f"Is CNF: {is_cnf(And(Atom('p'),Or(Not(Atom('Q')), And(Not(Atom('p')), Atom('r')))))}")
#print(f"Is CNF: {is_cnf(And(And(Atom('p1'),Or(Or(Not(Atom('p2')), Atom('p3')),Atom('p4'))), Or(Or(Not(Atom('p1')),Not(Atom('p4'))),Atom('p1'))))}")
#print(f"Is DNF: {is_dnf(Or(Atom('p'), And(Not(Atom('q')),Or(Not(Atom('q')), Atom('r')))))}")
#print(f"Is DNF: {is_dnf(Or(Or(Atom('p1'), And(And(Not(Atom('p2')), Atom('p3')),Atom('p4'))),And(And(Not(Atom('p1')),Not(Atom('p4'))),Atom('p1'))))}")
#print(f"Is DNNF: {is_decomposable_negation_normal_form(Or(And(Or(Atom('a'), Not(Atom('b'))), Or(Atom('c'),Atom('d'))),And(Or(Atom('a'),Atom('b')), Or(Not(Atom('c')),Not(Atom('d'))))))}")
#print(atoms(Or(Atom('p'), Atom('p'))))
#print(f"Is DNNF: {is_decomposable_negation_normal_form(Or(And(Or(Atom('a'),Not(Atom('b'))),Or(Not(Atom('a')),Atom('d'))),And(Or(Atom('a'),Atom('b')),Or(Not(Atom('c')),Not(Atom('d'))))))}")
#print(f"substitution: {substitution(Implies(And(Atom('p'), Not(Atom('q'))), Atom('r')),Not(Atom('q')), Or(Atom('r'),Atom('t')),)}")
ex = {'a': False, 'b': False}
print(satisfiability_brute_force(Not(Or(Atom('a'), Atom('b')))))
#print(truth_value(Or(Atom('a'),Atom('b')), ex))

