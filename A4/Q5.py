
power_lambda = lambda x, y: x ** y

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

power_results = list(map(power_lambda, list1, list2))
print("\nPower results:", power_results) 