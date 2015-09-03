# -*- coding: utf-8 -*-

"""
mathdeck.loadproblem
~~~~~~~~~~~~~~~~~~~~

This module loads a problem file as a module.

:copyright: (c) 2015 by Patrick Spencer.
:license: Apache 2.0, see ../LICENSE for more details.

"""

import os
import sys

# Load problem file as
def load_file_as_module(file_path):
    """
    Load problem file as a module.

    :param file: The full path to the problem file

    returns a module represented by the problem file
    """

    # Create a new module to hold the seed variable so
    # the loaded module can reference the seed variable

    if sys.version_info[0] == 2:
        import imp
        problem_module = imp.load_source('prob_mod_pkg',file_path)

    if sys.version_info[0] == 3:
        import importlib.machinery
        problem_module = importlib.machinery \
                                  .SourceFileLoader('prob_mod_pkg',file_path) \
                                  .load_module()

    try:
        problem_module.answers
    except AttributeError:
        raise AttributeError('Problem file has no \'answers\' attribute')

    return problem_module

