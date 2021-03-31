from itertools import permutations as perm
from string import ascii_lowercase
# using numpy for the matrix
from numpy import matrix

# creating the function
def permutations(string):
    newArray = []
    for i in string: newArray.append(i)
    per = perm(newArray)
    newPer = []
    for i in per:
        newArray2 = ""
        for j in i:
            newArray2 += j
        newPer.append(newArray2)
    newPer = list(dict.fromkeys(newPer))
    return (newPer)


print((matrix(permutations('DANIEL'))))
