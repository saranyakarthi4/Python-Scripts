
from fractions import Fraction
from functools import reduce

def product(fracs):
    print (fracs)
    t = reduce(lambda x,y : x*y , fracs)
    return (t.numerator, t.denominator)


fracs = [[1,2],[3,4],[5,6]]
for i in range(3):
    fracs.append(Fraction(fracs[i]))
result = product(fracs)
print (*result)