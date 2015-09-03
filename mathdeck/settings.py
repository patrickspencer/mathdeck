# -*- coding: utf-8 -*-

"""
mathdeck.settings
~~~~~~~~~~~~~~~~~

This module accesses the settings file located at
~/mathdeck_settings.json

:copyright: (c) 2015 by Patrick Spencer.
:license: Apache 2.0, see ../LICENSE for more details.

"""

import json
import os

# use as follows:
# from mathdeck import settings
# dir = settings.problems_libs['main']
home = os.path.expanduser('~')
settings_file = os.path.join(home,'mathdeck_settings.json')

with open(settings_file) as file:
    settings = json.load(file)

problem_libs = settings['problem libraries']
