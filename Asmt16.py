# 1.Develop  a Student Management system using JSON

import json

# File to store student data
FILE_NAME = 'students.json'

# Function to load student data from JSON file
def load_data():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Function to save student data to JSON file
def save_data(data):
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)

# Function to add a student
def add_student(name, age, subjects, grades):
    Students = load_data()
    Students[name] = {'age': age, 'subjects': subjects, 'grades': grades}
    save_data(Students)
    print(f'Student {name} added successfully!')

# Function to retrieve a student’s record
def get_student(name):
    Students = load_data()
    return Students.get(name, 'Student not found.')

# Function to update a student’s record
def update_student(name, key, value):
    Students = load_data()
    if name in Students:
        Students[name][key] = value
        save_data(Students)
        print(f'Student {name}’s {key} updated successfully!')
    else:
        print('Student not found.')

# Function to delete a student’s record
def delete_student(name):
    Students = load_data()
    if name in Students:
        del Students[name]
        save_data(Students)
        print(f'Student {name} deleted successfully!')
    else:
        print('Student not found.')

# Test Cases
add_student('Alice', 20, ['Math', 'Science'], {'Math': 90, 'Science': 85})
print(get_student('Alice'))
update_student('Alice', 'age', 21)
delete_student('Alice')

# 2.Convert JSON  String to  Dictionary and Modify data


import json

# Given JSON string
Json_string = {'name': 'John', 'age': 25, 'city': 'New York'}

# Convert JSON string to Python dictionary
# Data = json.loads(Json_string)
Data = Json_string

# Modify a specific key-value pair
Data['age'] = 26

# Convert dictionary back to JSON
Updated_json_string = json.dumps(Data, indent=4)

# Output results
print('Updated Dictionary:', Data)
print('Updated JSON String:', Updated_json_string)
