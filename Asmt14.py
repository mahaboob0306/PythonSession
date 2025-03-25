# Understanding OOP Concepts:

# a) Define Object-Oriented Programming (OOP) and explain how it differs from procedural programming.

# Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects, which encapsulate data and behavior (methods). OOP focuses on designing programs using classes and objects, promoting reusability, modularity, and scalability.

# Differences between OOP and Procedural Programming:
# Here are the answers to your assignment questions:

# 1. Understanding OOP Concepts:

# a) Define Object-Oriented Programming (OOP) and explain how it differs from procedural programming.

# Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects, which encapsulate data and behavior (methods). OOP focuses on designing programs using classes and objects, promoting reusability, modularity, and scalability.

# Differences between OOP and Procedural Programming:



# 2. Comparison of Procedural vs. OOP Approach:

# a) Convert the given procedural approach for storing employee details into an OOP-based approach.

# Procedural Approach (Example):

Employees = []

def add_employee(name, age, salary):
    Employees.append({'name': name, 'age': age, 'salary': salary})

def display_employees():
    for emp in Employees:
        print(f'Name: {emp['name']}, Age: {emp['age']}, Salary: {emp['salary']}')

add_employee('Alice', 30, 50000)
display_employees()

#OOP Approach (Example):

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'

Employees = []
Employees.append(Employee('Alice', 30, 50000))

for emp in Employees:
    print(emp)

# b) Explain the benefits of the OOP approach in this scenario.

# Encapsulation: Employee data is encapsulated within an object.

# Reusability: The class can be reused to create multiple employee objects.

# Abstraction: Users interact with objects rather than managing raw data structures.

# Modularity: Code is more organized and easier to maintain.


# c) Implement the __str__() method in your class.

# The __str__() method is implemented in the OOP approach above, returning a meaningful string representation of the Employee object.



# 3. Class & Static Methods, Access Modifiers:

# a) Differentiate between instance variables, class variables, and static variables with examples.

# Example Code:

class Employee:
    Company_name = 'TechCorp'  # Class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age  # Instance variable

    @staticmethod
    def company_policy():
        return 'Work Hard'

#b) Implement a Python class BankAccount with a private attribute __balance and methods to deposit, withdraw, and check balance.

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposited: {amount}')
        else:
            print('Deposit amount must be positive.')

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f'Withdrawn: {amount}')
        else:
            print('Invalid withdrawal amount.')

    def check_balance(self):
        return f'Balance: {self.__balance}'

# Example usage
Account = BankAccount(1000)
Account.deposit(500)
Account.withdraw(200)
print(Account.check_balance())

# c) Demonstrate the use of @classmethod and @staticmethod in a class.

class Person:
    Species = 'Human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def set_species(cls, new_species):
        cls.species = new_species

    @staticmethod
    def greet():
        return 'Hello, welcome!'

# Example usage
print(Person.greet())  # Static method call
Person.set_species('Homo Sapiens')  # Class method call
print(Person.Species)