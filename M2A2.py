# Name: Student Aidan Hoang
# Student ID:  836253799
# Section: 18254
# Assignment: Module 2 Assignment 2

g_list = ['Mortal Kombat', 'Contra', 'Streets Of Rage', 'Shinobi', 'Sonic', 'Phantasy Star']

print ("Here are the top sega games")
for game in g_list:
    print (game)

removed_game = input("Which one do you think should be removed? ")
g_list.remove(removed_game)
 
print("Here are the new top Sega games:")
for game in g_list:
    print(game)
