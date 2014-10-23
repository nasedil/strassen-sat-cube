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
    """Check that our transformation of the <d = (a and e) xor (b and c)> is correct.

    Check whether
    d = (a and e) xor (b and c)
    is equivalent to
    (~a | ~e | ~b | ~c | ~d) ∧ (a ∨ b ∨ ~d) ∧ (e ∨ b ∨ ~d) ∧ (a ∨ c ∨ ~d) ∧ (e ∨ c ∨ ~d) ∧ (a ∨ ~b | ~c ∨ d) ∧ (e ∨ ~b | ~c ∨ d) ∧ (~a | ~e ∨ b ∨ d) ∧ (~a | ~e ∨ c ∨ d)
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

test_and_assignment()
test_double_and_assignment()
test_xor_with_assignment_1()
test_xor_with_assignment_2()