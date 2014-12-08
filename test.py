# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 21:59:29 2014

@author: genio
"""

TF = [True, False]

def test_and_assignment():
    """Check that our transformation of the <c = a and b> is correct.

    Check whether
    c = a and b
    is equivalent to
    (c or not(a) or not(b)) and (not(c) or a) and (not(c) or b)
    where a, b and c are boolean values.
    """
    for a in [True, False]:
        for b in [True, False]:
            for c in [True, False]:
                expression_original = c == (a and b)
                expression_concluded = ((c or not(a) or not(b))
                    and (not(c) or a)
                    and (not(c) or b))
                assert(expression_original == expression_concluded)

def test_double_and_assignment():
    """Check that our transformation of the <d = a and b and c> is correct.

    Check whether
    d = a and b and c
    is equivalent to
    (d or ~a or ~b or ~c) and (~d or a) and (~d or b) and (~d or c)
    where a, b and c are boolean values.
    """
    for a in TF:
        for b in TF:
            for c in TF:
                for d in TF:
                    original = (d == (a and b and c))
                    concluded = ((d or not a or not b or not c) and
                                 (not d or a) and
                                 (not d or b) and
                                 (not d or c))
                    assert (original == concluded)

def test_xor_with_assignment_1():
    """Check that our transformation of the <d = a xor (b and c)> is correct.

    Check whether
    d = a xor (b and c)
    is equivalent to
    (~a | ~b | ~c | ~d) ∧ (a ∨ b ∨ ~d) ∧ (a ∨ c ∨ ~d) ∧ (a ∨ ~b | ~c ∨ d) ∧ (~a ∨ b ∨ d) ∧ (~a ∨ c ∨ d)
    where a, b and c are boolean values.
    """
    for a in TF:
        for b in TF:
            for c in TF:
                for d in TF:
                    original = (d == (a != (b and c)))
                    concluded = ((not a or not b or not c or not d) and
                                 (a or b or not d) and
                                 (a or c or not d) and
                                 (a or not b or not c or d) and
                                 (not a or b or d) and
                                 (not a or c or d))
                    assert (original == concluded)

def test_xor_with_assignment_2():
    """Check that our transformation of the <c = (a1 and b1) xor ... xor (a15 and b15)> is correct.

    Check whether
    c = (a1 and b1) xor ... xor (a15 and b15)
    is equivalent to

    where a, b and c are boolean values.
    """
    for a in TF:
        for b in TF:
            for c in TF:
                for d in TF:
                    for e in TF:
                        original = (d == ((a and e) != (b and c)))
                        concluded = ((not a or not e or not b or not c or not d) and
                                     (a or b or not d) and
                                     (a or c or not d) and
                                     (e or b or not d) and
                                     (e or c or not d) and
                                     (a or not b or not c or d) and
                                     (e or not b or not c or d) and
                                     (not a or not e or b or d) and
                                     (not a or not e or c or d))
                        assert (original == concluded)

def test_xor_with_assignment_3():
    """Check that our transformation of the <d = (a and e) xor (b and c)> is correct.

    Check whether
    d = (a and e) xor (b and c)
    is equivalent to
    (~a | ~e | ~b | ~c | ~d) ∧ (a ∨ b ∨ ~d) ∧ (e ∨ b ∨ ~d) ∧ (a ∨ c ∨ ~d) ∧ (e ∨ c ∨ ~d) ∧ (a ∨ ~b | ~c ∨ d) ∧ (e ∨ ~b | ~c ∨ d) ∧ (~a | ~e ∨ b ∨ d) ∧ (~a | ~e ∨ c ∨ d)
    where a, b and c are boolean values.
    """
    for c in TF:
        for a1 in TF:
            for a2 in TF:
                for a3 in TF:
                    for a4 in TF:
                        for a5 in TF:
                            for a6 in TF:
                                for a7 in TF:
                                    for a8 in TF:
                                        for a9 in TF:
                                            for a10 in TF:
                                                for a11 in TF:
                                                    for a12 in TF:
                                                        for a13 in TF:
                                                            for a14 in TF:
                                                                for a15 in TF:
                                                                    for b1 in TF:
                                                                        for b2 in TF:
                                                                            for b3 in TF:
                                                                                for b4 in TF:
                                                                                    for b5 in TF:
                                                                                        for b6 in TF:
                                                                                            for b7 in TF:
                                                                                                for b8 in TF:
                                                                                                    for b9 in TF:
                                                                                                        for b10 in TF:
                                                                                                            for b11 in TF:
                                                                                                                for b12 in TF:
                                                                                                                    for b13 in TF:
                                                                                                                        for b14 in TF:
                                                                                                                            for b15 in TF:
                                                                                                                                original = (c == ((a1 and b1) != (a2 and b2) != (a3 and b3) != (a4 and b4) != (a5 and b5) != (a6 and b6) != (a7 and b7) != (a8 and b8) != (a9 and b9) != (a10 and b10) != (a11 and b11) != (a12 and b12) != (a13 and b13) != (a14 and b14) != (a15 and b15)))
                                                                                                                                concluded = ((not c or not a1 or not b1 or not a2 or not b2 or not a3 or not b3 or not a4 or not b4 or not a5 or not b5 or not a6 or not b6 or not a7 or not b7 or not a8 or not b8 or not a9 or not b9 or not a10 or not b10 or not a11 or not b11 or not a12 or not b12 or not a13 or not b13 or not a14 or not b14 or not a15 or not b15) and
                                                                                                                                             (a or b or not d) and
                                                                                                                                             (a or c or not d) and
                                                                                                                                             (e or b or not d) and
                                                                                                                                             (e or c or not d) and
                                                                                                                                             (a or not b or not c or d) and
                                                                                                                                             (e or not b or not c or d) and
                                                                                                                                             (not a or not e or b or d) and
                                                                                                                                             (not a or not e or c or d))
                                                                                                                                assert (original == concluded)

test_and_assignment()
test_double_and_assignment()
test_xor_with_assignment_1()
test_xor_with_assignment_2()
test_xor_with_assignment_3()