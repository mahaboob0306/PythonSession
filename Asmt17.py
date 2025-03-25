# 1.Recursive  Function  for  Exponentiation

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

# Example Test Cases
print(power(2, 3))  # Output: 8 (2^3 = 2 * 2 * 2)
print(power(5, 0))  # Output: 1 (Any number raised to 0 is 1)

# 2.Recursive  Function for GCD  using Euclidean Algorithm 

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Example Test Cases
print(gcd(48, 18))  # Output: 6
print(gcd(56, 98))  # Output: 14
