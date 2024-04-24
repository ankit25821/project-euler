# Summation of Primes
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

# Using Sieve of Eratosthenes algorithm

limit = 20_00_000
sum_of_primes = 0


# assuming all `True` are prime numbers from 0 - 20_00_001
sieve = [True] * (limit + 1)
sieve[0] = sieve[1] = False  # setting `False` to 0 & 1 as non prime

for i in range(2, limit + 1):
    if sieve[i]:
        # if given idex is prime adding it to sum
        sum_of_primes += i
        for j in range(i*i, limit + 1, i):
            sieve[j] = False

print(sum_of_primes)
