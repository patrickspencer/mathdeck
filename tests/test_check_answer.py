# -*- coding: utf-8 -*-

import unittest
import os
from mathdeck import check_answer, loadproblem
from sympy import symbols, expand

class TestCheckAnswerModule(unittest.TestCase):

    def setUp(self):
        x = symbols('x')
        self.x = x

    def test_compare_functions_equal(self):
        a = self.x+1
        b = 1+self.x
        self.assertTrue(check_answer.compare_functions(a,b))

    def test_compare_functions_not_equal(self):
        a = self.x+1
        b = self.x
        self.assertFalse(check_answer.compare_functions(a,b))


if __name__ == '__main__':
    unittest.main()
