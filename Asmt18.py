# 1.Create a lamba function for Temperature function 

Celsius_to_fahrenheit = lambda c: (c * 9/5) + 32

# Example usage
print(Celsius_to_fahrenheit(0))   # Output: 32.0
print(Celsius_to_fahrenheit(100)) # Output: 212.0

# 2.Implement a list  Comprehensive for filtering words
Words = ['apple', 'banana', 'grape', 'kiwi', 'mango', 'orange']
Filtered_words = [word for word in Words if len(word) <= 5]

# Expected Output
print(Filtered_words)  # Output: [‘apple’, ‘grape’, ‘kiwi’, ‘mango’]
