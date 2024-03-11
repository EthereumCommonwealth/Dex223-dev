

# Online Python - IDE, Editor, Compiler, Interpreter
import math
import numpy as np

def price(a):
    return (math.sqrt(a) * 2**96)

a = int(input('Enter price: '))

print(np.format_float_positional(price(a), trim='-'))
