from sympy import symbols, cos, sin, latex
from mathdeck import rand

metadata = {
  'author': 'Bob Hope',
  'institution': 'University of Missouri',
  'subject': 'algebra',
  'minor subject': 'polynomial equations',
  'tags': ['simplify','roots','intervals']
}

r = rand.Random()

# choose three random integers between 0 and 10.
root1 = r.randint(0,10)
root2 = r.randint(0,10)
root3 = r.randint(0,10)
#
# # specify our variables
x = symbols('x')
p = ((x-root1)*(x-root2)).expand(basic=True)

template_variables = {
    'p': latex(p),
    }

ans1 = {
    'value': cos(x)**2-sin(x)**2,
    'type': 'function',
}

answers = {
    "ans1": ans1
    }

