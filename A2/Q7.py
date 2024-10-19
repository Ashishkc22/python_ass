def multiply(a, *args):
    result = a
    for num in args:
        result *= num
    return result


print("Product:", multiply(2, 3, 4)) 
print("Product:", multiply(5, 6))  