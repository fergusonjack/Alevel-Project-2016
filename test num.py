import itertools

list = list(itertools.product([1,2,3,4], repeat=4))

for i in list:
    print (i)
