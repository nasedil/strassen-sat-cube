# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 21:59:29 2014

@author: Eugene Petkevich
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
    """Check out big xor transformation.
    """
    a = [True for i in range(16)]
    b = [True for i in range(16)]
    concluded = []

    def try_b():
        for b[1] in TF:
            for b[2] in TF:
                for b[3] in TF:
                    for b[4] in TF:
                        for b[5] in TF:
                            for b[6] in TF:
                                for b[7] in TF:
                                    for b[8] in TF:
                                        for b[9] in TF:
                                            for b[10] in TF:
                                                for b[11] in TF:
                                                    for b[12] in TF:
                                                        for b[13] in TF:
                                                            for b[14] in TF:
                                                                for b[15] in TF:
                                                                    original = (c == ((a[1] and b[1]) != (a[2] and b[2]) != (a[3] and b[3]) != (a[4] and b[4]) != (a[5] and b[5]) != (a[6] and b[6]) != (a[7] and b[7]) != (a[8] and b[8]) != (a[9] and b[9]) != (a[10] and b[10]) != (a[11] and b[11]) != (a[12] and b[12]) != (a[13] and b[13]) != (a[14] and b[14]) != (a[15] and b[15])))
                                                                    if not original:
                                                                        positive = []
                                                                        negative = []
                                                                        if c:
                                                                            negative.append('c')
                                                                        else:
                                                                            positive.append('c')
                                                                        for i in range (1,16):
                                                                            if a[i]:
                                                                                negative.append('a' + str(i))
                                                                            else:
                                                                                positive.append('a' + str(i))
                                                                            if b[i]:
                                                                                negative.append('b' + str(i))
                                                                            else:
                                                                                positive.append('b' + str(i))
                                                                        clause = {}
                                                                        clause['positive'] = positive
                                                                        clause['negative'] = negative
                                                                        concluded.append(clause)

    for c in TF:
        for a[1] in TF:
            for a[2] in TF:
                for a[3] in TF:
                    for a[4] in TF:
                        for a[5] in TF:
                            for a[6] in TF:
                                for a[7] in TF:
                                    for a[8] in TF:
                                        for a[9] in TF:
                                            for a[10] in TF:
                                                for a[11] in TF:
                                                    for a[12] in TF:
                                                        for a[13] in TF:
                                                            for a[14] in TF:
                                                                for a[15] in TF:
                                                                    try_b()
    print(str(concluded))


def test_xor_with_assignment_4():
    """Check out big xor transformation.
    """
    a = [True for i in range(6)]
    b = [True for i in range(6)]
    concluded = []

    def try_b():
        for b[1] in TF:
            for b[2] in TF:
                for b[3] in TF:
                    for b[4] in TF:
                        for b[5] in TF:
                            original = (c == ((a[1] and b[1]) != (a[2] and b[2]) != (a[3] and b[3]) != (a[4] and b[4]) != (a[5] and b[5])))
                            if not original:
                                positive = []
                                negative = []
                                if c:
                                    negative.append('c')
                                else:
                                    positive.append('c')
                                for i in range (1,6):
                                    if a[i]:
                                        negative.append('a' + str(i))
                                    else:
                                        positive.append('a' + str(i))
                                    if b[i]:
                                        negative.append('b' + str(i))
                                    else:
                                        positive.append('b' + str(i))
                                clause = {}
                                clause['positive'] = positive
                                clause['negative'] = negative
                                concluded.append(clause)

    for c in TF:
        for a[1] in TF:
            for a[2] in TF:
                for a[3] in TF:
                    for a[4] in TF:
                        for a[5] in TF:
                            try_b()
    print(str(len(concluded)))


def test_xor_with_assignment_5():
    """Check out big xor transformation.
    """
    a = [True for i in range(6)]
    b = [True for i in range(6)]
    concluded = []

    def try_b():
        for b[1] in TF:
            for b[2] in TF:
                original = (c == ((a[1] and b[1]) != (a[2] and b[2])))
                print(original)
                if not original:
                    positive = []
                    negative = []
                    if c:
                        negative.append('c')
                    else:
                        positive.append('c')
                    for i in range (1,3):
                        if a[i]:
                            negative.append('a' + str(i))
                        else:
                            positive.append('a' + str(i))
                        if b[i]:
                            negative.append('b' + str(i))
                        else:
                            positive.append('b' + str(i))
                    clause = {}
                    clause['positive'] = positive
                    clause['negative'] = negative
                    concluded.append(clause)

    for c in TF:
        for a[1] in TF:
            for a[2] in TF:
                try_b()
    for clause in concluded:
        print(clause['positive'])
        print(clause['negative'])


test_and_assignment()
test_double_and_assignment()
test_xor_with_assignment_1()
test_xor_with_assignment_2()
test_xor_with_assignment_5()
