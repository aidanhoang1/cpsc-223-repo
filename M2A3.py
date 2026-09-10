# Name: Aidan
# Student ID:  836253799
# Section: 18254
# Assignment: Module 2 Assignment 3

uber_list = list(range(100, 201, 2))
 
start = int(input("What is the start of your slice? "))
end = int(input("What is the end of your slice? "))
 
data_list = uber_list[start:end]
 
total_int = 0
for value in data_list:
    total_int += value
 
size = len(data_list)
average = total_int / size
 
print(f"Your slice contains {size} values and has an average value of {average}")
