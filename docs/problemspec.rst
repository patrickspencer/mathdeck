Problem Spec
============

This document outlines how a Mathdeck problem should be defined.

All mathdeck problems are python modules. They look like this:

::
   
   # problem-library/example1
   __init__.py
   mathdeck_meta_data.py
   templates/
   └── default.jinja2

Meta data
---------

All problem files should have a file called :code:`mathdeck_meta_data.py`. A sample meta data file will look like this:

::

   # problem-library/example1/mathdeck_meta_data.py
   # ID should be unique somehow (need a way to do this)
   ID = 0123456789
   AUTHORS = [
   {
       'name':Bob Hope,
       'institution': 'University of Missouri',
       'email': 'bhope@missou.edu',
       'edited': '2010-2012'
   }
       'name': Bruce Wayne,
       'institution': University of Kentucky',
       'email': 'bwayne@uky.edu',
       'edited': '2013-2016'
   }
   MAJOR_CATEGORIES = ['Calculus', 'Diffeq']
   MINOR_CATEGORIES = ['Slope of line', 'unique solutions']
   
All the meta data labels are capitalized because, in python, constants are capitalized.

Available meta data fields
~~~~~~~~~~~~~~~~~~~~~~~~~~

:code:`ID`: some id that is unique against all other problem files in
the world. (maybe use an MD5 hash of the original version of the
problem file to come up with this)

:code:`AUTHORS`: a python list of dictionaries which keep tabs on the problem authors
      

Problem file hooks
------------------

These are hooks that mathdeck use to know about the problem when it loads the problem module.

:code:`_answers`
~~~~~~~~~~~~~~~~

:code:`_answers`: a python list of answers. Each answer is an instance of the :class:`mathdeck.Answer` class.

.. code-block:: python
   
   # problem-library/example1/__init__.py
   from mathdeck import Answer

   ans1 = Answer(value=5)
   ans2 = Answer(value=101)
   _answers = [ans1, ans2]

This makes two answers of value 5 and 101 respectively and loads into
the mathdeck hook :code:`_answers`.  The answers can be accessed by the
:code:`answers` attribute in an instance of a problem file loaded
by :code:`Problem(module_path)`:

.. code-block:: python

   >>> from mathdeck import Problem
   >>> problem = Problem('problem-library/example1')
   >>> print(problem.answers)
   [<mathdeck.Answer>, <mathdeck.Answer>]
   >>> print(type.answers[0])
   <mathdeck.Answer>
   >>> print(type.answers[0].value)
   5
   >>> print(type.answers[1].value)
   101

:code:`_template_vars`
~~~~~~~~~~~~~~~~~~~~~~

:code:`_template_vars`: a python dictionary of variables that can be called in templates.

Say our problem module looks like this:

::
   
   # problem-library/example2/
   __init__.py
   mathdeck_meta_data.py
   templates/
   └── default.jinja2

with

.. code-block:: python

   # problem-library/example2/__init__.py
   from mathdeck import Problem, Answer

   ans1 = Answer(value=5)
   a = (ans1.value)*3

   _answers = [ans1]
   _template_vars = {'temp_var': a}

Mathdeck now knows that we can use a template variable called
:code:`temp_var` in templates like this:

.. sourcecode:: html+jinja

   <!-- problem-library/example2/templates/default.jinja2 -->
   What is {{ temp_var }} divided by 3?
   
.. code-block:: python

   >>> from mathdeck import Problem

   >>> problem = Problem('problem-library/example1')
   >>> problem.display()
   What is 15 divided by 3?
