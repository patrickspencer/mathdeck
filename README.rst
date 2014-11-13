Mathdeck
========

Mathdeck is a program suite for managing the computations involved in
writing, displaying, and grading mathematical based homework
problems. It is written to abstract the computations so that other
responsibilities such as managing users and grades can be left to more
apt systems such as online course management systems.

Features
--------

- A system for writing homework problems.
- A system for displaying problem files.
- A system for measuring how close a proposed solution is to a predefined
  solution and offering suggestions for improvement to lead a student in
  the right direction.

Goals
-----

- Clear API
- Clear documentation.
- Comprehensive test suite.
- Creating problems should be as easy as possible for people who
  are mathematically inclined and would be able to pick up the basics of
  python in a couple days.
- Python 2.7 and 3+ support

Documentation
-------------

Documentation source files are found in the `docs/` folder. Compiled html pages are hosted on Read the Docs here: `http://mathdeck.readthedocs.org/ <http://mathdeck.readthedocs.org/>`_

Requirements
------------

- Python 2.7+
- Sympy 0.7.5+ (for writing and checking problems)
- Jinja2 2.7.3+ (for displaying problems)

For developers
--------------

It's recommended you first use the python package "virtualenv" to create a
separate virtual environment before installing. To install mathcheck for
development purposes run :code:`python setup.py develop` in the command line in
the root of the project folder (the folder with setup.py). To run the tests run
:code:`python -m unnittest discover` (requires python 2.7+) in the root folder.

About the name
--------------

Mathdeck is short for math display and check, the program's two main functions.

License
-------

Mathdeck is licensed under the BSD 3-Clause license. See
LICENSE file for more details.
