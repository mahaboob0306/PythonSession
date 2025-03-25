num=int(input("Enter a number"))
Is_even = num % 2 == 0

#If is_positive and is_even:
if(Is_even):
    print(f'{num} is positive and even')
else:
    print(f'{num} is not both positive and even')

#4.Bitwise Operator :
A = int(input('Enter first number: '))
B = int(input('Enter second number: '))

print(f'Bitwise AND: {A & B}')
print(f'Bitwise OR: {A | B}')
print(f'Bitwise XOR: {A ^ B}')
45
#5.Assingment Operator:

X = int(input('Enter a number: '))

X += 5
print(f'x += 5 : {X}')

X -= 2
print(f'x -= 2 : {X}')

X *= 3
print(f'x *= 3 : {X}')

X /= 2
print(f'x /= 2 : {X}')

X //= 2
print(f'x //= 2 : {X}')

X %= 3
print(f'x %= 3 : {X}')

X **= 2
print(f'x **= 2 : {X}')


#6.Membership Operator:

Fruits = ['apple', 'banana', 'mango', 'grapes']
Fruit_name = input('Enter a fruit name: ')

if Fruit_name in Fruits:
    print(f'{Fruit_name} is in the list')
else:
    print(f'{Fruit_name} is not in the list')


#7.Identity  Operator:
List1 = [1, 2, 3]
List2 = [1, 2, 3]

if List1 is List2:
    print('Both lists refer to the same object in memory')
else:
    print('Lists are identical but do not refer to the same memory object')
