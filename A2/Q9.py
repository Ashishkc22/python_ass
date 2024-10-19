
my_dict = {
    "name": "Ashish",
    "age": 25,
    "country": "India",
    "profession": "Developer",
    "language": "Python"
}

my_dict["city"] = "Pune"
print("Dictionary after adding city:", my_dict)

my_dict["age"] = 26
print("Dictionary after updating age:", my_dict)

del my_dict["profession"]
print("Dictionary after deleting profession:", my_dict)