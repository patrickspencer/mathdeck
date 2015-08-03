from sympy import symbols, cos, sin
from mathdeck import rand

metadata = {
  'author': 'Bob Hope',
  'institution': 'University of Missouri',
  'subject': 'algebra',
  'minor subject': 'polynomial equations',
  'tags': ['simplify','roots','intervals']
}

r = rand.Random()

# # choose three random integers between 0 and 10.
# root1 = r.randint(0,10)
# root2 = r.randint(0,10)
# root3 = r.randint(0,10)
#
# # specify our variables
x = symbols('x')
#
# # define a polynomial whose roots are root1 and root2 and expand it
#
# # define what the output will look like
# template = r"""
# Find the roots of the polynomial $p(x) = {{p | format=latex}}$:
# """
#
ans1 = {
    'name': 'ans1',
    'value': cos(x)**2-sin(x)**2,
    'type': 'function',
}

answers = [ans1]

