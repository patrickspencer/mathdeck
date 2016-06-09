# -*- coding: utf-8 -*-

"""
mathdeck.display
~~~~~~~~~~~~~~~~

This module displays a problem by running the main
problem file through a given template.

:copyright: (c) 2014-2016 by Patrick Spencer.
:license: Apache 2.0, see ../LICENSE for more details.
"""

import os
from jinja2 import Environment, FileSystemLoader

class Template(object):
    """
    usage:
    >> from mathdeck import load, settings
    >>
    >> problem = 'example1'
    >> problem_lib = settings.problem_libs['main']
    >> problem_path = problem_lib + problem + '/__init__.py'
    >> problem_module = load.load_file_as_module(problem_path)
    >> print(display_prob_from_template(problem_path,'web'))
    """
    def __init__(self,prob_path,template_name):
        self.prob_dir = prob_path
        self.template_name = template_name
        self.prob_dir = os.path.dirname(prob_path)
        self.template_path = prob_dir + '/templates'
        self.env = Environment(loader=FileSystemLoader(template_path))
        self.template_name = '%s.jinja2' % template
        self.template = env.get_template(template_name)

    def render(self)
        context = problem_module.template_variables
        return template.render(**context)
