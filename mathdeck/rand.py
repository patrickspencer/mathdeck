# -*- coding: utf-8 -*-

"""
mathdeck.rand
~~~~~~~~~~~~

This module redefines the random module to base the
generatation of random numbers off how many times the random
functions have been called before.

:copyright: (c) 2014 by Patrick Spencer.
:license: BSD3, see LICENSE for more details.

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
# import random
# stdrandom.seed(1)              r = rand.Random(1)
# stdrandom.random()             r.random()
# > 0.13436424411240122          > 0.13436424411240122
# stdrandom.seed(2)
# stdrandom.randint(1,10)        r.randint(1,10)
# > 10                           > 10
# stdrandom.seed(3)
# stdrandom.randint(1,10)        r.randint(1,10)
# > 3                            > 3



class Random(stdrandom.Random):

    count = 0
    seed_value = 1

    def __init__(self, seed_value=1):
        self.seed_value = seed_value

    def random(self):
        stdrandom.seed(self.seed_value + self.count)
        # line = "seed value: " + str(self.seed_value + self.count)
        output = stdrandom.random()
        self.count += 1
        return output

    def randint(self,a,b):
        stdrandom.seed(self.seed_value + self.count)
        # line = "seed value: " + str(self.seed_value + self.count)
        output = stdrandom.randint(a,b)
        self.count += 1
        return output





