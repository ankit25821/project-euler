'''
Largest Prime Factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

num = 600851475143

factors = []
divisor = 2 # smallest factor is 2


while num > 1:
    if num % divisor:
        divisor += 1
    else:
        num //= divisor
        factors.append(divisor)


# print(factors)
# print(','.join(str(x) for x in factors))
print(factors[-1])
