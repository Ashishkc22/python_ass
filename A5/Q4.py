people = {
    'John': {'age': 45, 'city': 'New York'},
    'Mike': {'age': 22, 'city': 'Los Angeles'},
    'Sarah': {'age': 32, 'city': 'New York'},
    'Anna': {'age': 28, 'city': 'Chicago'}
}

result = [name for name, info in people.items() if info['age'] > 30 and info['city'] == 'New York']
print("People over 30 in New York:", result)