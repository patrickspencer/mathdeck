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

Source files are hosted on `Github <https://github.com/patrickspencer/mathdeck/>`_ and `PyPI <https://pypi.python.org/pypi/mathdeck/>`_.

Documentation source files are found in the `docs/` folder within the source. Compiled documentation files are hosted on `Read the Docs <http://mathdeck.readthedocs.org/>`_.

Issues are hosted on `Github Issues <https://github.com/patrickspencer/mathdeck/issues/>`_.

Discussion is on `Google Groups <https://groups.google.com/d/forum/mathdeck>`_.

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

Contribute
----------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
#. If you feel uncomfortable or uncertain about an issue or your changes, feel free to email Patrick Spencer at patrick.spencer at mail.mizzou.edu and he will happily help you via email, irc, or whatever you are comfortable with.
#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS.rst.

About the name
--------------

Mathdeck is short for math display and check, the program's two main functions.

Acknowledgements
----------------

We would like to thank the members at `Sympy
<http://sympy.org/>`_ for creating a viable computer algebra system. We would also
like to thank the people at `Requests
<https://github.com/kennethreitz/requests/>`_ for
exemplifying what a good python project should look like.
Some of the setup to this project was based on their
practices and we hope imitation is form a flattery.

License
-------

Mathdeck is licensed under the BSD 3-Clause license. See
LICENSE file for more details.
