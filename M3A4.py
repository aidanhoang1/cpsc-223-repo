# Name: Aidan Hoang
# Student ID: 836253799
# Section: 18254
# Assignment: Module 3 Assignment 4

currentyear = int(input("What year is now? "))
birthyear = int(input("What year were you born?"))

age_int= currentyear-birthyear

if age_int == 50:
    print("The future is unclear")
elif age_int > 50:
    print("Death will come for you soon")
elif age_int % 2 == 0:
    print("This will be a great year")
else:
    print("This year will be tough")
