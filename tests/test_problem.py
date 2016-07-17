# -*- coding: utf-8 -*-

import unittest
import os
from mathdeck import Problem

class TestProblem(unittest.TestCase):

    def test_get_problem_path(self):
        path = 'problem-library/example1'
        problem = Problem(path)
        self.assertEqual(problem.path, path)

if __name__ == '__main__':
    unittest.main()
