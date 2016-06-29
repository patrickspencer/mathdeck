# -*- coding: utf-8 -*-

"""
mathdeck.settings
~~~~~~~~~~~~~~~~~

This module accesses the settings file located at
/etc/mathdeck/mathdeckconf.json

:copyright: (c) 2015 by Patrick Spencer.
:license: Apache 2.0, see ../LICENSE for more details.
"""

import json
import os


# Make this a class so we can pass conf_dir value. We want this so
# testings is easier.

class ProblemLibs:
    def __init__(self,conf_dir=os.path.expanduser('~')):
        self.conf_dir = conf_dir

    @classmethod
    def get_dir(cls):
        with open('/etc/mathdeck/mathdeckconf.json') as file:
                data = json.load(file)
        return data['prob_lib_dir']

