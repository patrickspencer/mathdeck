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
    Main class for holding settings related methods.
    """
    default_file = '/etc/mathdeck/mathdeckconf.json'
    default_lib_name ='main_lib'

    def __init__(self):
        pass

    @classmethod
    def get_dir(cls, settings_file = default_file, lib_name = default_lib_name):
        """
        Return path of problem library. By default it looks in
        :code:`/etc/mathdeck/mathdeckconf.json` and returns the
        ['problem_libs']['main_lib'] entry in this json file. :code:`mathdeckconf.json` looks like

        .. code-block:: python

            # default mathdeckconf.json
            {
                "problem_libs": {
                    "main_lib": "/main/lib/dir/",
                    "alt_lib": "/another/problem/lib/dir/"
                }
            }

        :param settings_file: The path to the settings file. Defaults to
            :code:`/etc/mathdeck/mathdeckconf.json`.
        :param lib_name: the name of the library to get (see how to specify
            different libraries by looking at the code block above for how
            mathdeckconf.json looks). Defaults to :code:`main_lib`.

        Usage::

            >>> # with the above default mathdeckconf.json
            >>> mathdeck.settings.ProblemLibs().get_dir()
            `/main/lib/dir/`
            >>> mathdeck.settings.ProblemLibs().get_dir(lib_name = 'alt_lib')
            `/another/problem/lib/dir/'
        """
        with open(settings_file) as file:
                data = json.load(file)
        return data["problem_libs"][lib_name]

