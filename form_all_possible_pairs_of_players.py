"""
Give a set of five player names
Write a python script to form all possible pairs of players that is selecting two
players at a time
"""

# creating a set of player names
players_name_set = set()

# taking player names from the user
i = 1
while i <= 5 :
    players_name_set.add(input("Enter %d player name : " %(i)))
    i += 1

# forming pairs of player 
i = 0 
temp_list = list(players_name_set)

for e in players_name_set :
    del temp_list[i]
    while i < len(temp_list) :
        print(e, '-', temp_list[i])
        i += 1
    i = 0
    