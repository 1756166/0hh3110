# -*- coding: utf-8 -*-

from itertools import permutations
import pickle
import numpy as np
x = pickle.load(open("row.p", "rb"))
thing = np.array([])
z = 0

def check_three(matrix):
    rotated = [''.join(i) for i in zip(*matrix[::-1])]
    if any(['111' in j or '222' in j for j in rotated]):
        return True
    return False
    
for i in permutations(x, 3):
    z += 1
    if z % 100000 == 0:
        print z
    if check_three(i):
        continue
    else:
        thing = np.append(thing, i)

thing = thing.reshape(len(thing)/3, 3)
print thing[0]
pickle.dump(thing, open("threes.p", "wb")) #This one worked fine
