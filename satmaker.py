# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 19:39:06 2014

@author: genio
"""

class VariableFactory(object):

    """A class for a SAT maker that number variables.

    It keeps track of variable numbers
    """

    def __init__(self):
        """Create a factory for a SAT-input."""
        self.count = 0

    def next(self):
        """Create and return a new variable."""
        variable = {}
        self.count += 1
        variable["number"] = self.count
        return variable

class ConstraintCollector(object):

    """A class for a SAT maker that collects constraints.

    It stores all constraints.
    """

    def __init__(self):
        """Create a constraint collector."""
        self.constraints = []

    def add(self, positive, negative):
        """Add constraint.

        Arguments:
        positive: a list of non-negated variables;
        negative: a list of negated variables.
        """
        constraint = {}
        constraint["positive"] = positive
        constraint["negative"] = negative
        self.constraints.append(constraint)

class SatPrinter(object):

    """A class for printing SAT input."""

    def __init__(self, vf, cc):
        """Create a SAT printer.

        Arguments:
        vf: a variable factory;
        cc: a constraints collector.
        """
        self.vf = vf
        self.cc = cc

    def print(self, file):
        """Print SAT input into a file object."""
        file.write('p cnf ' +
                   str(self.vf.count) + ' ' +
                   str(len(self.cc.constraints)) + '\n')
        for constraint in self.cc.constraints:
            for variable in constraint['positive']:
                file.write(str(variable["number"]) + ' ')
            for variable in constraint['negative']:
                file.write('-' + str(variable["number"]) + ' ')
            file.write('0 \n')