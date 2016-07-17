# -*- coding: utf-8 -*-

import unittest
import os
from mathdeck import Answer

class TestAnswers(unittest.TestCase):

    def test_get_answer_value(self):
        ans1 = Answer(value=1)
        self.assertEqual(ans1.value, 1)

if __name__ == '__main__':
    unittest.main()
