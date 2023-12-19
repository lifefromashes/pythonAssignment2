'''
Copyright (c) 2019 Python Forensics, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

'''
from __future__ import print_function

# Python Sets
# Python Fundementals
#
# Python Sets
#
# Python Forensics, Inc.

print("\nPython Sets\n")

# Set Demonstration
print("Simple Demonstration of Sets in Python")
print("======================================")
print()

# Create an empty set
emptySet = set()
print("Empty Set", emptySet)
print()

# Create a set with initial values
setA = {1, 2, 3, 4}

print("set A = ", setA)
print()

# Add a value to a set
setA.add(5)
print("Added Value 5 to set A = ", setA)
print()

# Create a new set B
setB = {3, 4, 11, 13, 15, 17}
print("setB = ", setB)
print()

# Create a union of two sets
setC = setA.union(setB)
print("Union of Set A and B = ", setC)
print()

# Create the intersection of two sets
setD = setA.intersection(setB)

print("Intersection of Set A and B = ", setD)
print()

caseA = {"Kevin Mitnick", "Jonathon James", "Kevin Poulsen", "Robert Morris"}
caseB = {"Kevin Poulsen", "Robert Morris", "Stephen Wosniak", "Richard Stallman"}
unionCaseAB = caseA.union(caseB)
intersectionCaseAB = caseA.intersection(caseB)

print("Suspects Case A =          ", caseA)
print("Suspects Case B =          ", caseB)
print("Union of Suspects =        ", unionCaseAB)
print("Intersection of Suspects = ", intersectionCaseAB)
print()

print("\nIterate through the union of suspects")
print("notice that the sort order has not changed")

for value in unionCaseAB:
    print(value)

print()

newList = list(unionCaseAB)
newList.sort()
print(newList)

# Sorting a set

print("Sorted Set = ", sorted(unionCaseAB))
print()

print("Because sets are unordered, only the output is sorted not the actual set")
print("This is fundamental to math, as sorting sets is irrelevant")
print("\nIterating through the union of suspects again yields the same result")
for value in unionCaseAB:
    print(value)

print()

