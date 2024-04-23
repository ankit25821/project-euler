# Special Pythagorean Triplet
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

                            a^2 + b^2 = c^2.

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
'''

sum_value = 1000
product = 0

for m in range(2, int(sum_value**0.5)):
    for n in range(1, m):
        # using Euclid's formula
        if (m*(m+n) == sum_value/2):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            product = a * b * c

print(product)
