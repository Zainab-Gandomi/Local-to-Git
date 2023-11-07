
"""
def testgen(index):
    weekdays = ['sun','mon','tue','wed','thu','fri','sat']
    yield weekdays[index]
    yield weekdays[index+1]

day = testgen(0)
print (day)

"""

# How to convert a list into a string?

weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsString = ' '.join(weekdays)
print(listAsString)


 # How to convert a list into a tuple?

weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsTuple = tuple(weekdays)
print(listAsTuple)

# How to convert a list into a set?

weekdays = ['sun','mon','tue','wed','thu','fri','sat','sun','tue']
listAsSet = set(weekdays)
print(listAsSet)

 # How to count the occurrences of a particular element in the list?

weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print(weekdays.count('mon'))


weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print([[x,weekdays.count(x)] for x in set(weekdays)])


print([[ x, weekdays.count(x) ] for x in set(weekdays)])

#  What is NumPy array?

#A) NumPy arrays are more flexible then lists in Python. By using NumPy arrays reading and writing items is faster and more efficient.

# How can you create Empty NumPy Array In Python?

#A) We can create Empty NumPy Array in two ways in Python,

#1) import numpy
#numpy.array([])

#2) numpy.empty(shape=(0,0))


import array
a = [1, 2, 3]
print (a[-3])
print (a[-2])
print (a[-1])

names = ['Chris', 'Jack', 'John', 'Daman']
print(names[-1][-1])
print(names[-2][-3])