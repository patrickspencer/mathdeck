# -*- coding: utf-8 -*-

"""
mathdeck.rand
~~~~~~~~~~~~

This module redefines the random module to base the
generatation of random numbers off how many times the random
functions have been called before.

:copyright: (c) 2015 by Patrick Spencer.
:license: Apache 2.0, see LICENSE for more details.

"""

import random as stdrandom

# use in a problem:
# from mathdeck import rand
# r = rand.Random(seed_value)
# r.random()  # current seed = seed_value
# r.random()  # current seed = seed_value + 1
# r.random()  # current seed = seed_value + 2
#
# using standard 'random'        using rand.py
# -----------------------        -----------------------
# import random as stdrandom     from mathdeck import rand
# stdrandom.seed(1)              r = rand.Random(1) # 1 is the initial seed
# stdrandom.random()             r.random()
# > 0.13436424411240122          > 0.13436424411240122
# stdrandom.seed(2)
# stdrandom.randint(1,10)        r.randint(1,10)
# > 10                           > 10
# stdrandom.seed(3)
# stdrandom.randint(1,10)        r.randint(1,10)
# > 3                            > 3


class Random(stdrandom.Random):

    # used to count how many times the random function has been called
    count = 0

    # When rand.Random() is called it will load the current seed in the currect
    # context from a module called _seed_holding_module which has an attribute
    # called _seed. This is so a program can pass a seed value to a problem
    # file.

    def __init__(self):
        import importlib
        try:
            self._seed_value = __import__('_seed_holding_module')._seed
        except ImportError:
            self._seed_value = 1

    def random(self):
        stdrandom.seed(self._seed_value + self.count)
        # line = "seed value: " + str(self.seed_value + self.count)
        output = stdrandom.random()
        self.count += 1
        return output

    def randint(self,a,b):
        stdrandom.seed(self._seed_value + self.count)
        # line = "seed value: " + str(self.seed_value + self.count)
        output = stdrandom.randint(a,b)
        self.count += 1
        return output

