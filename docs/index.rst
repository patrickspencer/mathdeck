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
   from mathdeck import Problem, Answer

   ans1 = Answer(value=5)
   Problem.addAnswer(ans1)

The answers can be accessed in `problems.answers`:

.. code-block:: python

   >>> from mathdeck import Problem
   >>> problem = Problem('problem-library/example1')
   >>> print(problem.answers)
   [<mathdeck.Answer>]
   >>> print(type.answers[0])
   <mathdeck.Answer>
   >>> print(type.answers[0].value)
   5

We can check the answer against a predefined answer. `0` means not a
match and `1` means is a match.

.. code-block:: python

   >>> from mathdeck import Problem
   >>> problem = Problem('problem-library/example1')
   >>> print(problem.answers)
   5
   >>> problem.check(problem.answers,'4')
   0
   >>> problem.check(problem.answers,'5')
   1

Example problem file

*Note*: Not sure how to define an answer within a problem file. The
following is perhaps one way:

.. code-block:: python

   # problem-library/example2/__init__.py
   from mathdeck import Problem, Answer

   ans1 = Answer(value=5)
   a = (ans1.value)*3

   Problem.addAnswer(ans1)

.. code-block:: python

   >>> from mathdeck import Problem
   >>> problem = Problem('problem-library/example1')
   >>> print(problem.answers)
   [<mathdeck.Answer>]
   
.. sourcecode:: html+jinja

   <!-- problem-library/example2/template1.jinja2 -->
   What is {{a}} divided by 3?
   
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
   >>> problem.display(template=template1.jinja2)
   What is 15 divided by 3?

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

   Problem.addAnswer(ans1, ans2)

.. sourcecode:: html+jinja

   <!-- problem-library/example3/template1.jinja2 -->
   Find the roots of the polynomial $p(x) = {{p | format=latex}}$:
   
When :code:`mathdeck.Problem.loadproblem` is called it uses a seed value to make
sure :code:`mathdeck.random` is predictable by the computer. Say a seed
value of 20 makes :code:`root1 = 1` and :code:`root2 = -1`

.. code-block:: python

   >>> from mathdeck import Problem
   >>> problem = Problem('problem-library/example1')
   >>> problem.display(template=template1.jinja2, seed=20)
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
