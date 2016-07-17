# -*- coding: utf-8 -*-

"""
mathdeck.answer
~~~~~~~~~~~~~~~

This module defines a generic answer class.

:copyright: (c) 2014-2016 by Patrick Spencer.
:license: Apache 2.0, see ../LICENSE for more details.
"""

import os
import sys

class Answer():
    """
    :param value: the value of the answer. This could be an integer, string,
    whatever.
    """

    def __init__(self, value):
        self.value = value
