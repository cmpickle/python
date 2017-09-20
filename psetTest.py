from more_itertools import powerset
from itertools import permutations
import sys

def get_powerset (list):
    perm = []
    if len(list) == 0:
        perm.append("")
        return perm
    first = list[0]
    print "first = " + str(first)
    rem = list[1:len(list)]
    print "rem = " + str(rem)
    words = get_powerset(rem)
    perm.extend(words)
    for word in words:
        perm.append(first+word)

    return perm

pset = list(powerset(str(sys.argv[1])))

for i in range(len(pset)):
    print(list(permutations(pset[i])))