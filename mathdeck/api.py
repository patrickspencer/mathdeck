# -*- coding: utf-8 -*-

"""
mathdeck.api
~~~~~~~~~~~~

This module implements the Mathdeck API.

:copyright: (c) 2015 by Patrick Spencer.
:license: Apache 2.0, see LICENSE for more details.
"""

from mathdeck.problem import *
from mathdeck.load import *
from mathdeck.answer import *

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
