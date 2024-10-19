

employee_data = ('John', 'Doe', 34, 'Developer', 'New York')

def unpack_employee_data(data):
    first_name, last_name, age, position, location = data
    return first_name, last_name, age, position, location


first_name, last_name, age, position, location = unpack_employee_data(employee_data)
print(f"\nEmployee Details:\nName: {first_name} {last_name}\nAge: {age}\nPosition: {position}\nLocation: {location}")

is_developer_present = 'Developer' in employee_data
print(f"\nIs 'Developer' present in employee_data? {is_developer_present}")

employee_list = list(employee_data)
employee_list.append('Full-time')
print("Employee list after adding 'Full-time':", employee_list)
