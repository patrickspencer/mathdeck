# -*- coding: utf-8 -*-

"""
mathdeck.check
~~~~~~~~~~~~

This module checks if a user submitted answer is equal to an
answer defined in a problem file.

:copyright: (c) 2015 by Patrick Spencer.
:license: Apache 2.0, see ../LICENSE for more details.

"""

import os
import sys
from mathdeck import loadproblem
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols, cos, sin


def compare_functions(func1,func2):
    return func1.equals(func2)


def check_single_ans(problem_answer,user_answer):

    prob_ans = problem_answer['value']

    if not isinstance(user_answer,str):
        raise TypeError('user answer is not a string')

    user_ans = parse_expr(user_answer,evaluate=False)

    if problem_answer['type'] == 'function':
        return compare_functions(prob_ans,user_ans)

