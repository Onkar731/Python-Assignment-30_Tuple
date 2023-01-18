"""
Write a python script to print distinct element of a list. Use set to solve the problem
"""

# creating a list
l1 = [1,3,5,2,5,6,7,8,9,10,20,3,5,4,2,1,0,3,2,1,4,5,]

# creating a set using set method to get distinct element of list
l1 = list(set(l1))

# printing distinct element of list
print("Distinct element of list are :", l1)