# -*- coding: utf-8 -*-

"""
mathdeck.settings
~~~~~~~~~~~~~~~~~

This module accesses the settings file located at
~/mathdeck.conf

:copyright: (c) 2015 by Patrick Spencer.
:license: Apache 2.0, see ../LICENSE for more details.

"""

import json
import os
import sys

"""
Make this a class so we can pass conf_dir value. We want this so testings
is easier.
"""
class ProblemLibs:
    def __init__(self,conf_dir=os.path.expanduser('~')):
        self.conf_dir = conf_dir

    def get_libs(self):
        settings_file = os.path.join(self.conf_dir,'mathdeck.conf')

        if sys.version_info[0] == 2:
            import ConfigParser

            config = ConfigParser.RawConfigParser()
            config.read(settings_file)

        if sys.version_info[0] == 3:
            from configparser import ConfigParser

            config = ConfigParser()
            config.read(settings_file)

        lib_section='Problem library locations'
        libs = config[lib_section]
        problem_libs = {}
        for key in config[lib_section]:
            problem_libs[key] = config[lib_section][key]
        return problem_libs
