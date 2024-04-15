# Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

# initial sum
total = 0

# Natural numbers are all positive integers from 1 to infinity. So will loop from 1 to 1000 and store the sum in `total`
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(total)


