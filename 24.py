import itertools

x = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))

print(x[10**6 - 1])