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
from mathdeck import loadproblem, settings
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols, cos, sin


def compare_functions(func1,func2):
    if func1.equals(func2):
        return 1
    else:
        return 0


def check_single_ans(problem_answer,user_answer):

    prob_ans = problem_answer['value']

    if not isinstance(user_answer,str):
        raise TypeError('user answer is not a string')

    user_ans = parse_expr(user_answer,evaluate=False)

    if problem_answer['type'] == 'function':
        return compare_functions(prob_ans,user_ans)

def make_single_ans_report(request):
    """
    Request is a json document in the following format:
    request = {
        "name": "ans1",
        "problem_file": "example1/__init__.py",
        "problem_library": "main",
        "proposed_answer": "x+1",
    }
    """
    prob_lib_path = settings.problem_libs[request['problem_library']]

    # Strip beginning slash becasue otherwise with might be an absolute path so
    # os.path.join will ignore the main_prob_lib_path
    request['problem_file'].strip('/')
    problem_file = os.path.join(prob_lib_path,
                      request['problem_file'].strip('/'))
    problem = loadproblem.load_file_as_module(problem_file)
    print(problem_file)
    ans_report = {}
    # this just grabs the first answer. We need to fix it so it grabs the
    # answer by request['name']
    # ans_report['name'] = problem.answers['name']
    proposed_answer = request['proposed_answer']
    actual_answer = problem.answers[request['name']]
    ans_report['assesment'] = check_single_ans(actual_answer,proposed_answer)
    ans_report['problem_library'] = request['problem_library']
    ans_report['problem_library_dir'] = prob_lib_path
    ans_report['problem_file'] = request['problem_file']
    ans_report['answer_given'] = request['proposed_answer']
    return ans_report

