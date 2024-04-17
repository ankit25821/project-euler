# Largest Prime Factor
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

num = 6_00_851_475_143

largest_factor = 0
divisor = 2  # smallest factor is 2


while num > 1:
    if num % divisor:
        divisor += 1
    else:
        num //= divisor
        largest_factor = divisor

print(largest_factor)
