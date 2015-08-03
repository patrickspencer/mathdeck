# -*- coding: utf-8 -*-

import unittest
import os
from mathdeck import loadproblem


class TestMathdeckLoadProblem(unittest.TestCase):

    def test_loadproblem_has_answers_attribute(self):
        file_name = 'has_answers_attribute.py'
        problem_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                'fixtures','loadproblem')
        problem = loadproblem.load_file_as_module(problem_dir,file_name)
        self.assertTrue(hasattr(problem,'answers'))

    def test_loadproblem_has_no_answers_attribute(self):
        file_name = 'has_no_answers_attribute.py'
        problem_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                'fixtures','loadproblem')
        self.assertRaises(Exception, loadproblem. \
            load_file_as_module(problem_dir,file_name))

if __name__ == '__main__':
    unittest.main()
