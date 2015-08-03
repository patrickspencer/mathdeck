# -*- coding: utf-8 -*-

"""
mathdeck.loadproblem
~~~~~~~~~~~~

This module loads a problem file as a module.

:copyright: (c) 2015 by Patrick Spencer.
:license: Apache 2.0, see ../LICENSE for more details.

"""

import os
import sys

# Load problem file as
def load_file_as_module(full_dir, file_name):
    """
    Load problem file as a module.

    :param problem_dir: The directory where the problem file is
    :param file_name: The name of the file

    returns a module represented by the problem file
    """

    file = os.path.join(full_dir,file_name)

    # Create a new module to hold the seed variable so
    # the loaded module can reference the seed variable

    if sys.version_info[0] == 2:
        import imp
        problem_module = imp.load_source('prob_module',file)

    if sys.version_info[0] == 3:
        import importlib.machinery
        problem_module = importlib.machinery \
                                  .SourceFileLoader("prob_module", file) \
                                  .load_module()

    try:
        problem_module.answers
    except AttributeError:
        raise AttributeError('Problem file has no \'answers\' attribute')

    return problem_module

