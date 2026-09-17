# Name: Aidan Hoang
# Student ID: 836253799
# Section: 18254
# Assignment: Module 3 Assignment 6

student_name = input("What is the student name?")
student_score = int(input("What is their score?"))

if student_score >= 90:
    grade = "an A"
elif student_score >= 80:
    grade = "a B"
elif student_score >= 70:
    grade = "a C"
elif student_score >= 60:
    grade = "a D"
else:
    grade = "an F"
 
print(f"{student_name} earned {grade}")
