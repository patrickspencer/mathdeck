# -*- coding: utf-8 -*-

"""
mathdeck.settings
~~~~~~~~~~~~~~~~~

This module accesses the settings file located at
/etc/mathdeck/mathdeckconf.json

:copyright: (c) 2014-2016 by Patrick Spencer.
:license: Apache 2.0, see ../LICENSE for more details.
"""

import json
import os


# Make this a class so we can pass conf_dir value. We want this so
# testings is easier.

class ProblemLibs:
    """
    By default, mathdeck looks for the settings file in
    /etc/mathdeck/mathdeckconf.json. We can change where get_dir() looks
    for the settings file in tests
    """
    default_file = '/etc/mathdeck/mathdeckconf.json'
    default_lib_name ='main_lib'

    def __init__(self):
        pass

    @classmethod
    def get_dir(cls, settings_file = default_file, lib_name = default_lib_name):
        with open(settings_file) as file:
                data = json.load(file)
        return data["problem_libs"][lib_name]

