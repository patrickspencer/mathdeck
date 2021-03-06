# -*- coding: utf-8 -*-

import unittest
import os
from mathdeck import load


class TestMathdeckLoadProblem(unittest.TestCase):

    def test_loadproblem_has_answers_attribute(self):
        file_name = 'has_answers_attribute.py'
        file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                'fixtures','load', file_name)
        problem = load.load_file_as_module(file)
        self.assertTrue(hasattr(problem,'answers'))

    def test_loadproblem_has_no_answers_attribute(self):
        file_name = 'has_no_answers_attribute.py'
        file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                'fixtures','load', file_name)
        self.assertRaises(Exception, load.load_file_as_module(file))

if __name__ == '__main__':
    unittest.main()
