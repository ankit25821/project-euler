# 10001st Prime
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 16th prime is 13.

What is the 10001st prime number?
'''

known_primes = [2, 3]
num_to_check = 4

while (len(known_primes) < 10001):

    is_prime = True

    for i in known_primes:
        if (num_to_check % i == 0):
            is_prime = False
            break

    if (is_prime):
        known_primes.append(num_to_check)

    num_to_check += 1

print(known_primes[-1])
