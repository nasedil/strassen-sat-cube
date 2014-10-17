# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 19:31:50 2014

@author: genio
"""

import satmaker

# To make an input for a SAT-solver, we need to associate each variable with
# a number automatically, while keeping string reference for ourselves.
# For this we use a VariableFactory and ConstraintCollector classes.

vf = satmaker.VariableFactory();
cc = satmaker.ConstraintCollector();

# We start with basic variables, 8 variables for each of the 7
# final computed multiplications:  4 for each of elements of first matrix (A),
# and 4 for second matrix (B).

a = [[[vf.next()
       for ja in range(2)]
      for ia in range(2)]
     for k in range(7)]
b = [[[vf.next()
       for jb in range(2)]
      for ib in range(2)]
     for k in range(7)]

# For each multiplication vector m_k we define a variable
# for each combination of a and b variables
# that correspond to value of their product (exists or not in m_k).

m = [[[[[vf.next()
         for jb in range(2)]
        for ib in range(2)]
       for ja in range(2)]
      for ia in range(2)]
     for k in range(7)]

# Now we define first series of constraints,
# that link basic variables and multiplication vectors.
# For each k in 1..7, {ia, ja, ib, jb} in 1..2:
# m_k_ia_ja_ib_jb = a_k_ia_ja AND b_k_ib_jb
# or in short:  c = a and b
# which can be rewritten as
# (c or not(a) or not(b)) and (not(c) or a) and (not(c) or b)
# This is correct and tested in test.test_and_assignment(),
# and explained also in https://en.wikipedia.org/wiki/Tseitin_transformation

for k in range(7):
    for ia in range(2):
        for ja in range(2):
            for ib in range(2):
                for jb in range(2):
                    va = a[k][ia][ja]
                    vb = b[k][ib][jb]
                    vc = m[k][ia][ja][ib][jb]
                    cc.add(positive=[vc],
                           negative=[va, vb])
                    cc.add(positive=[va],
                           negative=[vc])
                    cc.add(positive=[vb],
                           negative=[vc])

# Now we calculate result vectors of the product matrix C (C=A*B).

c = []
for ic in range(2):
    c.append([])
    for jc in range(2):
        c[ic].append([])
        for ia in range(2):
            c[ic][jc].append([])
            for ja in range(2):
                c[ic][jc][ia].append([])
                for ib in range(2):
                    c[ic][jc][ia][ja].append([])
                    for jb in range(2):
                        c[ic][jc][ia][ja][ib].append(False)
for ic in range(2):
    for jc in range(2):
        for l in range(2):
            c[ic][jc][ic][l][l][jc] = True

# Now we define coefficients q_k_ic_jc, k in 1..7, {ic, jc} in 1..2,
# for linking multiplication and result verctors:
# <xor for all k in 1..7> m_k_ia_ja_ib_jb and q_k_ic_jc = c_ic_jc_ia_ja_ib_jb
# for {ic, jc, ia, ja, ib, jb} in 1..2.

q = [[[vf.next()
       for jc in range(2)]
      for ic in range(2)]
     for k in range(7)]

# Now we define second series of constraints,
# that link multiplication vectors and result vectors.
# We rewrite previous constraints as a step by step computation,
# with introducing additional variables p_k_ic_jc and t_k_ic_jc,
# such that:
# p_k_ic_jc_ia_ja_ib_jb = m_k_ia_ja_ib_jb and q_k_ic_jc,
# k in 1..7, {ic, jc, ia, ja, ib, jb} in 1..2;
# and
# t_k_ic_jc_ia_ja_ib_jb = p_k_ic_jc_ia_ja_ib_jb xor p_(k+1)_ic_jc_ia_ja_ib_jb,
# k in 1..6, {ic, jc, ia, ja, ib, jb} in 1..2;
# and
# t_6_ic_jc_ia_ja_ib_jb = c_ic_jc_ia_ja_ib_jb,
# {ic, jc, ia, ja, ib, jb} in 1..2;
# The last one is rewritten as
# t_7_ic_jc_ia_ja_ib_jb or not(t_7_ic_jc_ia_ja_ib_jb),
# depending on c_ic_jc_ia_ja_ib_jb value, which is known by definition.

# So we define variables p and constraints for them:

p = [[[[[[[vf.next()
           for jb in range(2)]
          for ib in range(2)]
         for ja in range(2)]
        for ia in range(2)]
       for jc in range(2)]
      for ic in range(2)]
     for k in range(7)]

for k in range(7):
    for ic in range(2):
        for jc in range(2):
            for ia in range(2):
                for ja in range(2):
                    for ib in range(2):
                        for jb in range(2):
                            va = m[k][ia][ja][ib][jb]
                            vb = q[k][ic][jc]
                            vc = p[k][ic][jc][ia][ja][ib][jb]
                            cc.add(positive=[vc],
                                   negative=[va, vb])
                            cc.add(positive=[va],
                                   negative=[vc])
                            cc.add(positive=[vb],
                                   negative=[vc])

# So we define variables t and constraints for them. First, a transformation:
# c = a xor b
# can be rewritten as
# c = (a or b) and (not(a) or not(b))
# which in turn is
# (c or not((a or b)) or not((not(a) or not(b)))) and (not(c) or (a or b)) and (not(c) or (not(a) or not(b)))
# which is equal to
# (c or (not(a) and not(b)) or (a and b)) and (not(c) or a or b) and (not(c) or not(a) or not(b))
# which is equal to
# (c or not(a) or b) and (c or a or not(b)) and (not(c) or a or b) and (not(c) or not(a) or not(b))
# This is correct, see https://en.wikipedia.org/wiki/Tseitin_transformation

t = [[[[[[[vf.next()
           for jb in range(2)]
          for ib in range(2)]
         for ja in range(2)]
        for ia in range(2)]
       for jc in range(2)]
      for ic in range(2)]
     for k in range(6)]

for k in range(6):
    for ic in range(2):
        for jc in range(2):
            for ia in range(2):
                for ja in range(2):
                    for ib in range(2):
                        for jb in range(2):
                            va = p[k][ic][jc][ia][ja][ib][jb]
                            vb = p[k+1][ic][jc][ia][ja][ib][jb]
                            vc = t[k][ic][jc][ia][ja][ib][jb]
                            cc.add(positive=[vc, va],
                                   negative=[vb])
                            cc.add(positive=[vc, vb],
                                   negative=[va])
                            cc.add(positive=[va, vb],
                                   negative=[vc])
                            cc.add(positive=[],
                                   negative=[vc, va, vb])

# And last constraints:
# t_6_ic_jc_ia_ja_ib_jb = c_ic_jc_ia_ja_ib_jb,
# {ic, jc, ia, ja, ib, jb} in 1..2.

for ic in range(2):
    for jc in range(2):
        for ia in range(2):
            for ja in range(2):
                for ib in range(2):
                    for jb in range(2):
                        if c[ic][jc][ia][ja][ib][jb]:
                            cc.add(positive=[t[5][ic][jc][ia][ja][ib][jb]], negative=[])
                        else:
                            cc.add(positive=[], negative=[t[5][ic][jc][ia][ja][ib][jb]])

# We have in the end 1028 variables and 3280 constraints.

# Now we will output all the constraints to a file that will be an input to
# a SAT solver.
# For printing we will use a SatPrinter class.

sp = satmaker.SatPrinter(vf, cc);
file = open('input.txt', 'wt')
sp.print(file)
file.close()
