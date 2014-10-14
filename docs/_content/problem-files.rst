Problem Files
=============

Problem files are python files. They carry the extension .py.pf for
python (.py) problem file (.pf).

The only thing problem files need are predefined answers. so the following is an acceptable problem file:
Example problem file::

  # problem-library/example.py.pf

  answers.add(5)


Example problem file::

  # problem-library/example1.py.pf

  import mathdeck

  ans1 = 5
  a = ans1*3

  template = r"""
  What is {{a}} divided by 3?
  """

  answers.add(ans1)

A more advanced problem file::

  # problem-library/example3.py.pf

  from mathdeck.helpers import random as rand
  from sympy import var, expand, latex

  metadata = {
    'author': 'Bob Hope',
    'institution': 'University of Missouri',
    'subject': 'algebra',
    'minor subject': 'polynomial equations',
    'tags': ['simplify','roots','intervals']
  }

  # choose three random integers between 0 and 10.
  root1 = rand.randrange(0,10)
  root2 = rand.randrange(0,10).neq(root1)
  root3 = rand.randrange(0,10).neq(root1,root2)

  # specify our variables
  var(x)

  # define a polynomial whose roots are root1 and root2 and expand it
  p = (x-root1)*(x-root2)*(x-root3).expand

  # define what the output will look like
  template = r"""
  Find the roots of the polynomial $p(x) = {{p | format=latex}}$:
  """

  ans1 = {
    'value': root1,
    'type': 'number',
    'domain': 'real'
  }
  ans1 = {
    'value': root2,
    'type': 'number',
    'domain': 'real'
  }

  answers.add(ans1,ans2)

