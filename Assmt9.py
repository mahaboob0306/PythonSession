#1. 1.Conditional Statements:
Marks = int(input('Enter marks: '))  
if 90 <= Marks <= 100:  
    print('Grade: A')  
elif 80 <= Marks <= 89:  
    print('Grade: B')  
elif 70 <= Marks <= 79:  
    print('Grade: C')  
elif 60 <= Marks <= 69:  
    print('Grade: D')  
else:  
    print('Grade: F')

#1.2.Check if number within range:
Num = int(input('Enter a number: '))
if 10 <= Num <= 20:
    print(f'{Num} is within the range (10-20)')
else:
    print(f'{Num} is out of range')

#1.3.Rock paper scissors game :
import random

Choices = ['rock', 'paper', 'scissors']
User_choice = input('Enter rock, paper, or scissors: ').lower()
Computer_choice = random.choice(Choices)

print(f'Computer chose: {Computer_choice}')

if User_choice == Computer_choice:
    print('It’s a tie!')
elif (User_choice == 'rock' and Computer_choice == 'scissors') or \
     (User_choice == 'paper' and Computer_choice == 'rock') or \
     (User_choice == 'scissors' and Computer_choice == 'paper'):
    print('You win!')
else:
    print('You lose!')

#2.Loops: First 15 Multiples of given Number:
Num = int(input('Enter a number: '))

for i in range(1, 16):
    print(Num * i)

#2.2Some of odd Numbers between 1 and  50 Using While loop

Sum_odd = 0
Num = 1

while Num <= 50:
    Sum_odd += Num
    Num += 2

print("Sum of odd numbers from 1 to 50:", Sum_odd)

#2.3Fibonacci  Sequence up to limit Using while loop

Limit = int(input("Enter the limit: "))

A, b = 0, 1
while A <= Limit:
    print(A, end="")
    A, b = b, A + b

#3.Loop Control Statement 
#Some of Numbers in a list (ignoring negative Numbers using continue)

Numbers = [10, -5, 20, -3, 30, -2, 40]
Sum_positive = 0

for num in Numbers:
    if num < 0:
        continue
    Sum_positive += num

print('Sum of positive numbers:', Sum_positive)

#3.2Search for a character in a string using break 

Text = input("Enter a string: ")
Char_to_find = input("Enter the character to search: ")

for index, char in enumerate(Text):
    if char == Char_to_find:
        print("f'Character '{Char_to_find}' found at index {index}'")
        break
else:
    print('Character not found')


#4.Terenary Operator: check if number even or odd


Num = int(input('“Enter a number: “'))
Result = 'Even' if Num % 2 == 0 else 'Odd'
print(f'The number is {Result}')

#5.Case statement (Match -Case) in python 
#Convert month Number in to month name

Month = int(input('Enter month number (1-12): '))

match Month:
    case 1:
        print("“January”")
    case 2:
        print("“February”")
    case 3:
        print("“March”")
    case 4:
        print("“April”")
    case 5:
        print("“May”")
    case 6:
        print("“June”")
    case 7:
        print("“July”")
    case 8:
        print("“August”")
    case 9:
        print("“September”")
    case 10:
        print("“October”")
    case 11:
        print("“November”")
    case 12:
        print("“December”")
    case default:
        print("Invalid month number")