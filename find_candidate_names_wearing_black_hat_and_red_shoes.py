"""
You have a list of names of candidates, some of them are wearing black hat,
some of them are wearing red shoes and some of them are wearing both. 
Now you have given a list of names of candidates wearing black hat. There is
another list of names of candidates wearing red shoes.

Write a python script to find out the names of the candidates wearing black hat red shoes.
"""


# defining a list of candidates - mixed
mix_list = ['onkar', 'raj', 'nikhil', 'yogesh', 'rohan', 'akshay', 'vijay', 'kaivalya', 'Shubham', 'kartik',]

# defining a list of candidates who are wearing black hat
black_hat_list = ['kaivalya', 'raj', 'onkar']

# defining a list of candidates who are wearing red shoes
red_shoes_list = ['rohan', 'akshay', 'vijay']

# defining a set of candidates who are wearing both
wearing_both_set = set()

# adding elements in set who wear's both the black hat and red shoes
for name in mix_list :
    if name not in black_hat_list and name not in red_shoes_list :
        wearing_both_set.add(name)

# printing all names who wear's both the black hat and red shoes
print("Candidate names who wears both black hat and red shoes :")
for name in wearing_both_set :
    print(name)