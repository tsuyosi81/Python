# # NOTE Printing

# print("Day 1 - Python Print Function")

# print("The function is declared like this:")

# print("print('what to print')")

# # NOTE Debugging Practice

# print("Day 1 - String Manipulation")

# print('String Concatenation is done with the "+" sign.')

# print('e.g. print("Hello " + "world")')

# print("New lines can be created with a backslash and n.")

# # NOTE Input Function

# print(len(input("What is your name?")))

# # NOTE Variables

# a = input("a: ")

# b = input("b: ")

# # 🚨 Don't change the code above 👆

#

# #Write your code below this line 👇

# c = a

# a = b

# b= c

# #Write your code above this line 👆

#

# # 🚨 Don't change the code below 👇

# print("a: " + a)

# print("b: " + b)

# # NOTE Data Types

# two_digit_number = input("Type a two digit number: ")

# # 🚨 Don't change the code above 👆

#

# #Write your code below this line 👇

# first_digit = two_digit_number[0]

# second_digit = two_digit_number[1]

# output = int(first_digit) + int(second_digit)

# print(output)

# # NOTE BMI Calculator

# height = input("enter your height in m: ")

# weight = input("enter your weight in kg: ")

# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# bmi = int(weight) / (float(height) \*\* 2)

# print(int(bmi))

# # NOTE Life in Weeks

# # 🚨 Don't change the code below 👇

# age = input("What is your current age?")

# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# life_span_in_years= 90

# life_span_in_days = life_span_in_years \* 365

# life_span_in_weeks = life_span_in_years \* 52

# life_span_in_months = life_span_in_years \* 12

# current_age_in_days = int(age) \* 365

# current_age_in_weeks = int(age) \* 52

# current_age_in_months = int(age) \* 12

# days_left = life_span_in_days - current_age_in_days

# weeks_left = life_span_in_weeks - current_age_in_weeks

# months_left = life_span_in_months - current_age_in_months

# print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

# # NOTE Odd or Even

# # 🚨 Don't change the code below 👇

# number = int(input("Which number do you want to check? "))

# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# odd_or_even = number % 2

# if odd_or_even == 0:

# print("This is an even number.")

# else:

# print("This is an odd number.")

# # NOTE BMI 2.0

# # 🚨 Don't change the code below 👇

# height = float(input("enter your height in m: "))

# weight = float(input("enter your weight in kg: "))

# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# bmi = round(weight / height \*\* 2)

# if bmi < 18.5:

# print(f"Your BMI is {(bmi)}, you are underweight.")

# elif bmi <= 25:

# print(f"Your BMI is {(bmi)}, you have a normal weight.")

# elif bmi <= 30:

# print(f"Your BMI is {(bmi)}, you are slightly overweight.")

# elif bmi <= 35:

# print(f"Your BMI is {(bmi)}, you are obese.")

# elif bmi > 35:

# print(f"Your BMI is {(bmi)}, you are overweight.")

# # NOTE Leap Year

# # 🚨 Don't change the code below 👇

# year = int(input("Which year do you want to check? "))

# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# # leap_4 = year % 4

# # leap_100= year % 100

# # leap_400 = year % 400

# # if leap_4 == 0 and leap_100 != 0:

# # print("Leap year.")

# # elif leap_100 == 0 and leap_400 == 0:

# # print("Leap year.")

# # elif leap_400 != 0:

# # print("Not leap year.")

# # else:

# # print("Not leap year.")

# if year % 4 == 0 and year % 100 != 0:

# print("Leap year.")

# elif year % 100 == 0:

# print("Leap year.")

# elif year % 400 != 0:

# print("Not leap year.")

# # NOTE Pizza Order Practice

# # 🚨 Don't change the code below 👇

# print("Welcome to Python Pizza Deliveries!")

# size = input("What size pizza do you want? S, M, or L ")

# add_pepperoni = input("Do you want pepperoni? Y or N ")

# extra_cheese = input("Do you want extra cheese? Y or N ")

# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# bill = 0

# if size == 'S':

# bill += 15

# elif size == 'M':

# bill += 20

# elif size == 'L':

# bill += 25

# if add_pepperoni == 'Y':

# if size == 'S':

# bill += 2

# elif size == 'M':

# bill += 3

# elif size == 'L':

# bill += 3

# elif add_pepperoni == 'N':

# bill += 0

# else:

# bill += 0

# if extra_cheese == 'Y':

# bill += 1

# elif extra_cheese == 'N':

# bill += 0

# else:

# bill += 0

# print(f"Your final bill is: ${bill}.")

# # NOTE Love Calculator

# # 🚨 Don't change the code below 👇

# print("Welcome to the Love Calculator!")

# name1 = input("What is your name? \n")

# name2 = input("What is their name? \n")

# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# combined_string = name1 + name2

# lower_case_string = combined_string.lower()

# t = lower_case_string.count('t')

# r = lower_case_string.count('r')

# u = lower_case_string.count('u')

# e = lower_case_string.count('e')

# true = t + r + u + e

# l = lower_case_string.count('l')

# o = lower_case_string.count('o')

# v = lower_case_string.count('v')

# e = lower_case_string.count('e')

# love = l + o + v + e

# love_score = int(str(true) + str(love))

# if (love_score < 10) or (love_score > 90):

# print(f"Your score is {love_score}, you go together like coke and mentos.")

# elif (love_score > 40) and (love_score < 50):

# print(f"Your score is {love_score}, you are alright together.")

# else:

# print(f"Your score is {love_score}.")

# # NOTE Heads or Tails

# #Remember to use the random module

# #Hint: Remember to import the random module here at the top of the file. 🎲

# import random

# # 🚨 Don't change the code below 👇

# test_seed = int(input("Create a seed number: "))

# random.seed(test_seed)

# # 🚨 Don't change the code above 👆 It's only for testing your code.

# #Write the rest of your code below this line 👇

# random_side = random.randint(0,1)

# if random_side == 1:

# print('Heads')

# else:

# print('Tails')

# # NOTE Banker Roulette

# import random

# # 🚨 Don't change the code below 👇

# # test_seed = int(input("Create a seed number: "))

# # random.seed(test_seed)

# # Split string method

# names_string = input("Give me everybody's names, separated by a comma. ")

# names = names_string.split(", ")

# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# number_of_items = len(names)

# random_choice = random.randint(-1, number_of_items)

# print(f"{names[random_choice]} is going to buy the meal today!")

# # NOTE Treasure Map

# # 🚨 Don't change the code below 👇

# row1 = ["⬜️","⬜️","⬜️"]

# row2 = ["⬜️","⬜️","⬜️"]

# row3 = ["⬜️","⬜️","⬜️"]

# map = [row1, row2, row3]

# print(f"{row1}\n{row2}\n{row3}")

# position = input("Where do you want to put the treasure? ") #23

# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# horizontal = int(position[0]) #2

# vertical = int(position[1]) #3

# map[vertical - 1][horizontal - 1] = "X"

# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇

# print(f"{row1}\n{row2}\n{row3}")

# # NOTE Average Height

# # 🚨 Don't change the code below 👇

# student_heights = input("Input a list of student heights ").split()

# for n in range(0, len(student_heights)):

# student_heights[n] = int(student_heights[n])

# # 🚨 Don't change the code above 👆

# total_height = 0

# for height in student_heights:

# total_height = total_height + height

# number_of_students = 0

# for student in student_heights:

# number_of_students += 1

# average_height = total_height / number_of_students

# print(round(average_height))

# #Write your code below this row 👇

# # NOTE High Score

# # 🚨 Don't change the code below 👇

# student_scores = input("Input a list of student scores ").split()

# for n in range(0, len(student_scores)):

# student_scores[n] = int(student_scores[n])

# print(student_scores)

# # 🚨 Don't change the code above 👆

# highest_score = 0

# for score in student_scores:

# if score > highest_score:

# highest_score = score

# print(f'The highest score in the class is: {highest_score}')

# # NOTE Adding Even Numbers

# #Write your code below this row 👇

# total = 0

# for number in range(2, 101, 2):

# total += number

# print(total)

# # NOTE FizzBizz

# #Write your code below this row 👇

# for number in range(1, 101):

# if number % 3 == 0 and number % 5 == 0:

# number = 'FizzBuzz'

# elif number % 3 == 0:

# number = 'Fizz'

# elif number % 5 == 0:

# number = 'Buzz'

# print(number)

# # NOTE Paint Area Calculator

# #Write your code below this line 👇

# import math

# def paint_calc(height, width, cover):

# num_cans = math.ceil(((height \* width) / cover)+.4)

# print(f"You'll need {num_cans} cans of paint.")

# #Write your code above this line 👆

# # Define a function called paint_calc() so that the code below works.

# # 🚨 Don't change the code below 👇

# test_h = int(input("Height of wall: "))

# test_w = int(input("Width of wall: "))

# coverage = 5

# paint_calc(height=test_h, width=test_w, cover=coverage)

# # NOTE Prime Numbers

#Write your code below this line 👇

# def prime_checker(number):
# is_prime = True
# for i in range(2, number):
# if number % i == 0:
# is_prime = False
# if is_prime:
# print("It's a prime number.")
# else:
# print("It's not a prime number.")

# #Write your code above this line 👆

# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

# NOTE Grading Program

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.

# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇

# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# # 🚨 Don't change the code below 👇
# print(student_grades)

# NOTE Dictionary in List

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇

# def add_new_country(Visited_country, Visited_Times, Visited_cities):
#     new_country = {}
#     new_country["country"] = Visited_country
#     new_country["visits"] = Visited_Times
#     new_country["cities"] = Visited_cities
#     travel_log.append(new_country)

# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# NOTE Days in Month

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         print("Leap year.")
#       else:
#         print("Not leap year.")
#     else:
#       print("Leap year.")
#   else:
#     print("Not leap year.")

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#   if is_leap(year) and month == 2:
#       return 29
#   return month_days[month - 1]    
        
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)







