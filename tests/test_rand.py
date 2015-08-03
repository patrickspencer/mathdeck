# -*- coding: utf-8 -*-

import unittest
import sys
import random as stdrandom
from mathdeck import rand

class TestMathdeckRand(unittest.TestCase):

    def test_initial_seed_value_set_by_module(self):
        seed = 233
        _seed_holding_module = type('module', (), {'_seed': seed})
        sys.modules['_seed_holding_module'] = _seed_holding_module
        r = rand.Random()
        self.assertEqual(r._seed_value, 233)

    def test_initial_seed_value_not_set(self):
        try:
            del sys.modules['_seed_holding_module']
        except KeyError:
            pass
        r = rand.Random()
        self.assertEqual(r._seed_value, 1)

    def test_rand_incrementation(self):
        stdrandom.seed(1)
        r = rand.Random()
        r._seed_value = 1
        # assert our new random function matches the python std lib random
        # on the first seed of 1
        self.assertEqual(stdrandom.random(),r.random())
        # assert our new random function automatically increments its seed
        # value by 1 without just by being being called another time
        stdrandom.seed(2)
        self.assertEqual(stdrandom.random(),r.random())
        # assert our new random function automatically increments its seed
        # value by 1 without just by being being called another time
        stdrandom.seed(3)
        self.assertEqual(stdrandom.random(),r.random())
        self.assertNotEqual(stdrandom.random(),1)


if __name__ == '__main__':
    unittest.main()
