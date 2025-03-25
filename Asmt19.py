# 1.Implement a Custome decorator

import time

def execution_timer(func):
    def wrapper(*args, **kwargs):
        Start_time = time.perf_counter()
        Result = func(*args, **kwargs)
        End_time = time.perf_counter()
        Execution_time = End_time - Start_time
        print(f'Execution time: {Execution_time:.6f} seconds')
        return Result
    return wrapper

@execution_timer
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Test case
Num = 5
print(f'Factorial of {Num} is: {factorial(Num)}')


# 2.Create a Custom iterator

class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        else:
            Result = self.current
            self.current += 2
            return Result

# Test case
Evens = EvenNumbers(10)

for num in Evens:
    print(num)
