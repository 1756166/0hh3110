# -*- coding: utf-8 -*-

import pickle
import numpy as np
x = pickle.load(open("row.p", "rb"))
threes = pickle.load(open('threes.p', 'rb'))
threes = threes.tolist()
print len(threes)
thing = []
z = 0

def check_three(matrix):
    rotated = [''.join(i) for i in zip(*matrix[::-1])]
    if any(['111' in j or '222' in j for j in rotated]):
        return True
    return False

for three in threes:
    z+=1
    if z%10000 == 0:
        print z
    for row in x:
        if row in three:
            break
        else:
            #row = np.array([row])
            #first = np.append(row, three)
            #second = np.append(three, row)
            first = three + [row]
            second = [row]+three
            if not(check_three(first)):
                thing.append(first)
            if not(check_three(second)):
                thing.append(second)
print thing[0] #Make sure it looks reasonable
pickle.dump(thing, open("fours.p", "wb"))