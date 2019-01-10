from collections.abc import Iterable
from scipy.io import loadmat
import os
import sys, os




def rec(start):
    found = None
    todo = [start]
    while len(todo) != 0:
        current = todo.pop(0)
        if str(type(current)) == "<class 'scipy.sparse.csc.csc_matrix'>":
            found = current
            todo = []
        elif isinstance(current, Iterable) or str(type(current)) == "<class 'numpy.void'>":
            for c in current:
                todo.append(c)
    return found

y = repr(sys.argv[0])
y = y[:87]
print(y + 'mat/')
for folder in os.listdir(y + 'mat/'):
    for matrix in os.listdir(y + 'mat/' + folder + '/'):
        f = loadmat('/mat/' + folder + '/' + matrix)
    #print(rec(f['Problem']))
    x = rec(f['Problem'])
    x.todense()
    print(x.shape)
