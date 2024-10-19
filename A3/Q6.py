def round_to_one(numbers):
    return list(map(lambda x: round(x, 1), numbers))

print(round_to_one([3.14159, 2.71828, 1.61803]))  