def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Testing the function
print("Vowels Count:", count_vowels("Hello World"))  # Example: 3 vowels
print("Vowels Count:", count_vowels("Python Programming"))  # Example: 4 vowels