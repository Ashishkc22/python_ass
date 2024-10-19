def reverse_string(string):
    reversed_str = ""
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str


print("Reversed String:", reverse_string("hello"))  
print("Reversed String:", reverse_string("Python"))  