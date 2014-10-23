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

def test_xor_with_assignment():
    """Check that our transformation of the <d = a xor (b and c)> is correct.

    Check whether
    d = a xor (b and c)
    is equivalent to
    (~A ∨ ~B ∨ ~C) ∧ (A ∨ B ∨ ~C) ∧ (A ∨ ~B ∨ C) ∧ (~A ∨ B ∨ C)
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

test_and_assignment()
test_double_and_assignment()