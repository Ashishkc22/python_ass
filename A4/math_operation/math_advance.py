import math

def power(base, exponent):
    return base ** exponent

def square_root(number):
    if number >= 0:
        return math.sqrt(number)
    else:
        return "Cannot take square root of a negative number."
