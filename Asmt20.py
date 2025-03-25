# 1.SQL lite Crud Operations 
#        Python Program 

import sqlite3

# Connect to SQLite database (or create if it doesn’t exist)
Conn = sqlite3.connect('company.db')
Cursor = Conn.cursor()

# Create employees table
Cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                    Id INTEGER PRIMARY KEY, 
                    Name TEXT, 
                    Department TEXT, 
                    Salary REAL)''')

# Insert at least 3 employees
Employees_data = [
    (1, 'Alice', 'HR', 50000),
    (2, 'Bob', 'IT', 60000),
    (3, 'Charlie', 'Finance', 55000)
]

Cursor.executemany('INSERT INTO employees (id, name, department, salary) VALUES (?, ?, ?, ?)', Employees_data)
Conn.commit()

# Fetch and print all employees
print('\nAll Employees:')
Cursor.execute('SELECT * FROM employees')
for row in Cursor.fetchall():
    print(row)

# Update salary of one employee
Cursor.execute('UPDATE employees SET salary = 65000 WHERE id = 2')
Conn.commit()

# Fetch and print updated data
print('\nUpdated Employee Data:')
Cursor.execute('SELECT * FROM employees WHERE id = 2')
print(Cursor.fetchone())

# Delete an employee
Cursor.execute('DELETE FROM employees WHERE id = 1')
Conn.commit()

# Fetch and print remaining records
print('\nRemaining Employees:')
Cursor.execute('SELECT * FROM employees')
for row in Cursor.fetchall():
    print(row)

# Close the database connection
Conn.close()

# Regular Expression -Data Extraction 

import re

# Sample paragraph input
Paragraph = input('Enter a paragraph of text: ')

# Email regex pattern
Email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
# Phone number regex pattern
Phone_pattern = r'\d{10}|\d{3}-\d{3}-\d{4}'

# Extract emails and phone numbers
Emails = re.findall(Email_pattern, Paragraph)
Phones = re.findall(Phone_pattern, Paragraph)

# Print extracted information
print('\nExtracted Email Addresses:')
for email in Emails:
    print(email)

print('\nExtracted Phone Numbers:')
for phone in Phones:
    print(phone)
