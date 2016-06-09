# -*- coding: utf-8 -*-

"""
mathdeck.api
~~~~~~~~~~~~

This module implements the Mathdeck API.

:copyright: (c) 2015 by Patrick Spencer.
:license: Apache 2.0, see LICENSE for more details.
"""

class Problem:
    """
    this class is the main class :class:`Problem`
    
    :param problem_file_path: the location of the problem file that needs to be
        loaded relative to the default library location as set in mathconf.py
        file.
    """

    def __init__(self, problem_file_path):
        return NotImplemented

def display_problem(file, seed):
    """
    Constructs and sends a :class:`Problem <Problem>`.
    Returns :class:`Problem <Problem>` object.

    :param file: method for the new :class:`Request` object.
    :param seed: Seed number to used to base random number generation off of

    Usage::

      >>> import mathdeck
      >>> output = mathdeck.display('file.py', 12345)
      Solve the following: $1+1=$<input type="text" name="ans1">
    """
    from jinja2 import Template
    template = u"""
      <html>
    """
    m = Template(u"{% set a, b = 'foo', 'föö' %}")

    return file, seed

def check_problem(module, seed):
    _seed_holding_module = type('module', (), {'_seed': seed})
    sys.modules['_seed_holding_module'] = _seed_holding_module
