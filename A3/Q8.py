# main.py

from Q1 import area_of_circle
from datetime import datetime
import math

def current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

check_starts_with_a = lambda s: s[0].lower() == 'a'
def factorial_of_number(n):
    return math.factorial(n)

def round_list(numbers):
    return [round(num) for num in numbers]

def round_to_one(numbers):
    return list(map(lambda x: round(x, 1), numbers))

def add_lists(list1, list2):
    return list(map(lambda x, y: x + y, list1, list2))

radius = 5
area = area_of_circle(radius)
print(f"The area of a circle with radius {radius} is: {area:.2f}")

print("Current date and time:", current_datetime())

print(check_starts_with_a("Apple")) 
print(check_starts_with_a("Banana")) 

print(f"Factorial of 5 is: {factorial_of_number(5)}")

print(round_list([1.2, 2.5, 3.8])) 

print(round_to_one([3.14159, 2.71828, 1.61803]))

print(add_lists([1, 2], [3, 4])) 
