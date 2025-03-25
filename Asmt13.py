#1.Number Squaring with exceptional handling:
def square_number():
    try:
        Num = float(input("Enter a number: "))
        print(f"Square of {Num} is {Num ** 2}.")
    except ValueError:
        print("Error: Invalid input! Please enter a number.")
    except TypeError:
        print("Error: Unexpected issue occurred!")

square_number()

#2.Even or odd number checking with exceptional handling:
def check_even_odd():
    try:
        Num = int(input("Enter a number: "))
        if Num % 2 == 0:
            print(f"{Num} is an even number.")
        else:
            print(f"{Num} is an odd number.")
    except ValueError:
        print("Error: Invalid input! Please enter a valid number.")

check_even_odd()

#3.Reverse string with exceptional handling 
def reverse_string():
    try:
        Text = input("Enter a string: ").strip()
        if not Text:
            raise ValueError("Error: Input cannot be empty!")
        print(f"Reversed string: {Text[::-1]}")
    except ValueError as e:
        print (f"{e}")


reverse_string()