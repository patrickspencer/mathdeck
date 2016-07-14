Mathdeck Docs
=============

Mathdeck is a program suite for managing the computations involved in
writing displaying, and grading mathematical based homework problems. It
is written to abstract the computations so that other responsibilities
such as managing users and grades can be left to more apt systems such
as online course management systems.

The program is written with one central idea: problem files are plain
`python modules
<https://docs.python.org/3/tutorial/modules.html>`_. This makes it so
you can use plain python and all the scientific python libraries such as
scipy, numpy, matplotlib, etc. in problem files.

Quick tour
----------

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

We can check the answer against a predefined answer. 0 means not a
match and 1 means is a match.

.. code-block:: python

   >>> from mathdeck import Problem
   >>> problem = Problem('problem-library/example1')
   >>> print(problem.answers)
   5
   >>> problem.check(problem.answers[0], Answer(value=4))
   0
   >>> problem.check(problem.answers[0], Answer(value=5))
   1
   >>> problem.check(problem.answers[1], Answer(value=101))
   1

Example problem file

.. code-block:: python

   # problem-library/example2/__init__.py
   from mathdeck import Problem, Answer

   ans1 = Answer(value=5)
   a = (ans1.value)*3

   _answers = [ans1]
   _template_vars = {'temp_var': a}

.. code-block:: python

   >>> from mathdeck import Problem
   >>> problem = Problem('problem-library/example1')
   >>> print(problem.answers)
   [<mathdeck.Answer>]

Let's make a couple templates so we know how to display the question. Mathdeck uses `Jinja2 templates <http://jinja.pocoo.org/>`_ for its templating system.

.. sourcecode:: html+jinja

   <!-- problem-library/example2/templates/default.jinja2 -->
   What is {{ temp_var }} divided by 3?

.. sourcecode:: html+jinja

   <!-- problem-library/example2/templates/template2.jinja2 -->
   What is {{ temp_var }} times 6 divided by 3 and then divided by 2?

Our module file directory looks like this now:

::

   # problem-library/example2/
   __init__.py
   templates/
   ├── default.jinja2
   └── template2.jinja2

.. code-block:: python

   >>> from mathdeck import Problem

   >>> problem = Problem('problem-library/example1')
   >>> print(problem.answers)
   [<mathdeck.Answer>]
   >>> ans = problem.answers[0]
   >>> print(ans.value)
   5
   >>> print(ans.type)
   Integer
   >>> problem.display()
   What is 15 divided by 3?
   >>> problem.display(template=template2.jinja2)
   What is 15 times 6 divided by 3 and then divided by 2?

A more advanced problem file using sympy, the display function, the check
function and seed values would look something like this:

.. code-block:: python

   # problem-library/example3/__init__.py
   from mathdeck import Problem, Answer
   from mathdeck.helpers import random
   from sympy import var, expand, latex

   # choose two random integers between 0 and 10. The second should not
   # be the same as the first
   root1 = random.randrange(0,10)
   root2 = random.randrange(0,10).neq(root1)

   # specify our variables
   var(x)

   # define a polynomial whose roots are root1, root2, and root3 and
   # expand it
   p = (x-root1)*(x-root2).expand()

   ans1 = Answer({
     'value': root1,
     'type': 'number',
     'domain': 'real',
     'label': 'first_ans'
   })
   ans1 = Answer({
     'value': root2,
     'type': 'number',
     'domain': 'real',
     'label': 'second_ans'
   })

   _answers = [ans1, ans2]
   _template_vars = {'poly': p}

.. sourcecode:: html+jinja

   <!-- problem-library/example3/templates/default.jinja2 -->
   Find the roots of the polynomial $p(x) = {{poly | format=latex}}$:

When :code:`mathdeck.Problem.loadproblem` is called it uses a seed value to make
sure :code:`mathdeck.random` is predictable by the computer. Say a seed
value of 20 makes :code:`root1 = 1` and :code:`root2 = -1`

.. code-block:: python

   >>> from mathdeck import Problem
   >>> problem = Problem('problem-library/example1')
   >>> problem.display(seed=20)
   Find the roots of the polynomial $p(x) = x^2-1$
   >>> problem.check({'first_ans': -1, 'second_ans': 3}, seed=20)
   # first_ans is correct but second_ans is incorrect
   {'first_ans': 1, 'second_ans': 0}
   >>> problem.check({'first_ans': -1, 'second_ans': 1}, seed=20)

Contents
--------

.. toctree::
   :maxdepth: 2

   api
   problemspec
   install

Features
--------

- A system for writing homework problems.
- A system for displaying problem files with templates.
- A system for measuring how close a proposed solution is to a
  predefined solution and offering suggestions for improvement to lead a
  student in the right direction.

Goals
-----

- Clear API
- Clear documentation.
- Comprehensive test suite.
- Creating problems should be as easy as possible for people who are
  mathematically inclined and would be able to pick up the basics of
  python in a couple days.

License
-------

Mathdeck is licensed under the Apache 2.0 license. See LICENSE file for
more details.
