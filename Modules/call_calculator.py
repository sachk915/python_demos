

import Modules.calculator_02
print(Modules.calculator_02.add(44, 56))
print(Modules.calculator_02.sub(50, 20))

import Modules.calculator_02 as cl1

print(cl1.add(22, 44))
print(cl1.div(77, 7))


from Modules.calculator_02 import sub
print(sub(33,5))

from Modules.calculator_02 import *
print(add(4, 4))
print(sub(4, 3))
print(mul(2,5))
