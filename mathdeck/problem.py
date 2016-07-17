# -*- coding: utf-8 -*-

"""
mathdeck.problem
~~~~~~~~~~~~~~~~

This module holds the class definition for Problem().

:copyright: (c) 2014-2016 by Patrick Spencer.
:license: Apache 2.0, see LICENSE for more details.
"""

class Problem:
    """
    this class is the main class :class:`Problem`

    :param problem_file_path: the location of the problem file that needs to be
        loaded relative to the default library location as set in mathconf.py
        file.
    """

    def __init__(self, path):
        self.path = path

