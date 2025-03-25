# Library Management System using Inheritance 

# Base class
class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id

    def display_info(self):
        print(f'Title: {self.title}, Author: {self.author}, Item ID: {self.item_id}')

# Derived class for Book
class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre

    def display_info(self):
        print(f'Title: {self.title}, Author: {self.author}, Item ID: {self.item_id}, Genre: {self.genre}')

# Derived class for Magazine
class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number):
        super().__init__(title, author, item_id)
        self.issue_number = issue_number

    def display_info(self):
        print(f'Title: {self.title}, Author: {self.author}, Item ID: {self.item_id}, Issue Number: {self.issue_number}')

# Test cases
Book1 = Book('Python Programming', 'John Doe', 'B001', 'Programming')
Book2 = Book('Data Science Basics', 'Jane Smith', 'B002', 'Data Science')
Magazine1 = Magazine('Tech World', 'Alex Brown', 'M001', 25)

Book1.display_info()
Book2.display_info()
Magazine1.display_info()


# 2.Secure Banking System Using Encapsulation:


# Base class
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposited: {amount}')
        else:
            print('Invalid deposit amount')

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f'Withdrawn: {amount}')
        else:
            print('Invalid or insufficient balance')

    def get_balance(self):
        return self.__balance  # Accessor method

# Derived class with added functionality
class SavingsAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.02):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        Interest = self.get_balance() * self.interest_rate
        self.deposit(Interest)
        print(f'Interest added: {Interest}')

# Test cases
Account = BankAccount(1000)
Account.deposit(500)
Account.withdraw(300)
print(f'Balance: {Account.get_balance()}')

# Trying to access private balance directly (will raise an error)
try:
    print(Account.__balance)
except AttributeError as e:
    print(f'Error: {e}')

# Savings Account test
Savings = SavingsAccount(2000, 0.05)
Savings.add_interest()
print(f'Savings Balance: {Savings.get_balance()}')
