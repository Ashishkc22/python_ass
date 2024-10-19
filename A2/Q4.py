def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Testing the function
print_details(name="Ashish", age=25, country="India")
print_details(course="Python", level="Advanced")