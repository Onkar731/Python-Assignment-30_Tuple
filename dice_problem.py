"""
Write a python script to create a set of tuples, where each tuple has two elements
representing dice upper face number.
Take a number N from the user and generate all possible tuples, in such a way that 
tuple elements sums to N.
"""

# taking input from the user
N = int(input("Enter a number : "))

# defining a set to store all tuples
tuple_set = set()

# generating all possible tuple
i = 1

while i <= 6 :
    j = 1
    while j <= 6 :
        if i+j == N :
            tuple_set.add(tuple([i, j]))
        j += 1
    i += 1

# printing all generated tuples
print("All possible tuple elements sums is %d are :" %(N), tuple_set)