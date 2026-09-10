# Name: Aidan Hoang
# Student ID:  836253799
# Section: 18254
# Assignment: Module 2 Assignment 1

g_list = []

game1 = input("What is your favorite game?")
g_list.append(game1.title())

game2 = input("What is your second favorite game?")
g_list.append(game2.title())

game3 = input ("What is your third favorite game?")
g_list.append(game3.title())

print(f"One of your favorite games is {g_list.pop()}")
print(f"One of your favorite games is {g_list.pop()}")
print(f"One of your favorite games is {g_list.pop()}")
