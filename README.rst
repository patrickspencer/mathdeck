Mathdeck
========

Mathdeck is a program suite for managing the computations involved in
writing, displaying, and grading mathematical based homework
problems. It is written to abstract away computations so that other
responsibilities such as managing users and grades can be left to more
apt systems such as online course management systems.

Intended features
-----------------

- Tool suite and standard spec for writing homework problems.
- A system for displaying problem files.
- A system for measuring how close a proposed solution is to a predefined
  solution and offering suggestions for improvement to lead a student in
  the right direction.

Programming Goals
-----------------

- Clear developer API.
- Clear and comprehensive documentation.
- Comprehensive test suite.
- Creating problems should be as easy as possible for people who
  are mathematically inclined and would be able to pick up the basics of
  python in a couple days.
- Python 2.7+ and 3+ support

Support
-------

Source files are hosted on `Github
<https://github.com/patrickspencer/mathdeck/>`_ and `PyPI
<https://pypi.python.org/pypi/mathdeck/>`_.

Documentation source files are found in the `docs/` folder within the
source. Compiled documentation files are hosted on `Read the Docs
<http://mathdeck.readthedocs.org/>`_.

Issues are hosted on `Github Issues
<https://github.com/patrickspencer/mathdeck/issues/>`_.

Discussion is on `Google Groups
<https://groups.google.com/d/forum/mathdeck>`_.

Requirements
------------

- Python 2.7+ or 3+
- Sympy 0.7.5+ (for writing and checking problems)
- Jinja2 2.7.3+ (for displaying problems)

For developers
--------------

It's recommended you first use the python package "virtualenv" to create a
separate virtual environment before installing. To install mathcheck for
development purposes run :code:`python setup.py develop` in the command line in
the root of the project folder (the folder with setup.py). To run the tests run
:code:`python -m unnittest discover` (requires python 2.7+) in the root folder.

Contributing
----------

There are two ways to contribute:


#. Via Github issues
#. Sending git patches through email

See `CONTRIBUTING.rst
<https://github.com/patrickspencer/mathdeck/blob/master/CONTRIBUTING.rst>`_
for more information.

About the name
--------------

Mathdeck is short for math display and check, the program's two main
functions.

License
-------

Mathdeck is licensed under the Apache 2.0 license. See
`LICENSE
<https://github.com/patrickspencer/mathdeck/blob/master/LICENSE>`_ file
for more details.

