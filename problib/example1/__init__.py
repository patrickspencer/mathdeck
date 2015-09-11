from sympy import symbols, cos, sin, latex
from mathdeck import rand, answer

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

a1 = answer.Answer()
a1.value = cos(x)**2-sin(x)**2
a1.type = 'function'
a1.variables = ['x']
a1.domain = 'R'

a2 = answer.Answer()
a2.value = 'x+1'
a2.type = "function"
a2.variables = ['x','y']

answers = {
    'ans1': a1,
    'ans2': a2
    }

