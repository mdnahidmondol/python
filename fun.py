# The keyword lambda is a shortcut for creating one-line functions. for example, the polynomails 
# f(x) = 6x3 + 4x2 - x + 3 and g(x, y, z) = x + y2 - z3


def f(x):
    """Return the function""" 
    return 6*x**3 + 4*x**2 - x + 3

def g(x, y, z):
    return x + y**2 - z**3


#Equivalently, Define the polyomials quickly using "lamdda"

f = lambda x : 6*x**3 + 4*x**2 -x + 3
g = lambda x, y, z : x + y**2 - z**3 
