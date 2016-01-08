from sympy import symbols, cos, sin, latex
from mathdeck import rand, answer


r = rand.Random()

# choose three random integers between 0 and 10.
root1 = r.randint(0,10)
root2 = r.randint(0,10)
root3 = r.randint(0,10)
#
# # specify our variables
x = symbols('x')
p = ((x-root1)*(x-root2)).expand(basic=True)

func = cos(x)**2-sin(x)**2

a1 = answer.Answer(
        value=func,
        type='function',
        vars=['x'])
a2 = answer.Answer(value='x+1',type='function',vars=['x'])

answers = {
    'ans1': a1,
    'ans2': a2
    }

template_variables = {
    'p': latex(p),
    }

