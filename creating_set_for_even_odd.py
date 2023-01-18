"""
Write a python script to create two sets from a given set of numbers to
seperate even and odd numbers
"""

# creating a set of even odd numbers
mix_set = {12, 34, 45, 89, 78, 243, 79, 789, 434, 54, 876, 123, 432, 98,}

# creating two sets to store even and odd numbers from given set
even_set, odd_set = set(), set()

# adding elements in even_set and odd_set
for e in mix_set :
    if e%2 == 0 :
        even_set.add(e)
    else :
        odd_set.add(e)
        
# printing both the sets
print("Even set :", even_set, "\nOdd set :", odd_set)