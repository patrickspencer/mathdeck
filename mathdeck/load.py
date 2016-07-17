# -*- coding: utf-8 -*-

"""
mathdeck.loadproblem
~~~~~~~~~~~~~~~~~~~~

This module loads a problem file as a module.

:copyright: (c) 2014-2016 by Patrick Spencer.
:license: Apache 2.0, see ../LICENSE for more details.
"""

import os
import sys

def load_module_from_path(path):
    """
    Load problem module as a module. Loads the :code:`__init__.py` file from
    the designated path. Note, since it only loads the :code:`__init__.py` file
    then it does not load any other modules in the path. For example if path is
    :code:`/problib/example1` and example1 looks like this:

        example1
        └─ module2/
           ├─ __init__.py
           └─ bar.py

    then we couldn't do something like

        problem = load_module_from_path(path)
        from problem import bar

    :code:`problem` only represents the :code:`__init__.py` file.

    :param path: The full path to the problem file
    :return: A python module

    Usage::

        >>> settings_path = mathdeck.settings.ProblemLibs().get_dir()
        >>> module_name = 'example1'
        >>> path = os.path.join(settings_path, module_name)
        >>> problem = mathdeck.load.load_module_from_path(path)

    :note: I thought about using sys.path.insert(1,path)
        to insert the path of the problem library folder into the system path
        but I saw two things wrong with this:
            1. If we did that we would then have to load the module somehow.
               We could try doing something like :code:`import modulename` but
               modulename would be a variable so we would need to do something
               like :code:`importlib.import_module(modulename)` but then we
               couldn't call the module very easily. I want to get attributes
               like this: modulename.__author__ but I don't think the variable
               modulename can also stant for the module. Since we can't access
               the submodules in a module by adding the path to the system path
               then we might as well use the :code:`SourceFileLoader` way so we
               can atleast give the newly import module a new name that we can
               refer to is as.
            2. How would we split up the path? use :code:`newpath =
               os.path.split(path)` and then use
               :code:`os.path.abspath(os.path.join(yourpath, os.pardir))` to get
               the directory where the problem module lives? I am worried that
               someone might put a backslash or forwardslash in a file directory
               and mess up the path splitting.

    """

    # for python 2
    if sys.version_info[0] == 2:
        import imp
        problem_module = imp.load_source('prob_mod_pkg', path)

    # for python 3.3 and 3.4
    vinfmaj = sys.version_info[0]
    vinfmin = sys.version_info[1]
    if vinfmaj == 3 and (vinfmin == 3 or vinfmin == 4):
        from importlib.machinery import SourceFileLoader
        problem_module = SourceFileLoader('prob_mod_pkg', path, '__init__.py').load_module()

    try:
        problem_module.answers
    except AttributeError:
        raise AttributeError('Problem file has no \'answers\' attribute')

    return problem_module

