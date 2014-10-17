# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 21:59:29 2014

@author: genio
"""

def test_and_assignment():
    """It checks that our transformations of the constraint are correct.

    It checks whether
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

test_and_assignment()