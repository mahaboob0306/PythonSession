#1.Temperature Converter:
def convert_temperature(temp, unit):
    if unit == 'C':
        F = (temp * 9/5) + 32
        K = temp + 273.15
    elif unit == 'F':
        C = (temp - 32) * 5/9
   
        K = C + 273.15
        return C, K
    elif unit == 'K':
        C = temp - 273.15
        F = (C * 9/5) + 32
        return C, F
    else:
        return 'Invalid unit'

    return F, K

# Example usage:
print(convert_temperature(100, 'C'))  # (212.0, 373.15)
print(convert_temperature(32, 'F'))   # (0.0, 273.15)
print(convert_temperature(273.15, 'K'))  # (0.0, 32.0)

#2.Grade Calculator:
def calculate_grade(scores):
    Avg = sum(scores) / len(scores)
    
    if Avg >= 90:
        return 'A'
    elif Avg >= 80:
        return 'B'
    elif Avg >= 70:
        return 'C'
    elif Avg >= 60:
        return 'D'
    else:
        return 'F'

# Example usage:
print(calculate_grade([85, 90, 78, 92]))  # B
print(calculate_grade([50, 60, 55]))      # F


#3.Prime Number Checker:
def is_prime(n):
    if n < 2:
        return False
    for I in range(2, int(n ** 0.5) + 1):
        if n % I == 0:
            return False
    return True

def find_primes(start, end):
    return [n for n in range(start, end + 1) if is_prime(n)]

# Example usage:
print(is_prime(7))  # True
print(find_primes(10, 20))  # [11, 13, 17, 19]

#4.character Counter 
def count_characters(string):
    Char_count = {}
    for char in string:
        Char_count[char] = Char_count.get(char, 0) + 1
    return Char_count

# Example usage:
print(count_characters('hello world'))  
# {‘h’: 1, ‘e’: 1, ‘l’: 3, ‘o’: 2, ‘ ‘: 1, ‘w’: 1, ‘r’: 1, ‘d’: 1}

#5.Fibonacci Sequence Generator:
def generate_fibonacci(n):
    Fib = [0, 1]
    for _ in range(n - 2):
        Fib.append(Fib[-1] + Fib[-2])
    return Fib[:n]

# Example usage:
print(generate_fibonacci(10))  
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]