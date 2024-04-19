# Smallest Multiple
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def gcd(a, b):
    """Function to find the greatest common divisor"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Function to find the least common multiple."""
    return a * b // gcd(a, b)


n = 20
result = 1
for i in range(1, n + 1):
    result = lcm(result, i)

print(result)
