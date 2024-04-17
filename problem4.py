# Largest Palindrome Product
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 
2-digit numbers is 9009 = 91 X 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def palindrome(num):
    x = num
    reversed_num = 0

    while num > 0:
        last_digit = num % 10
        reversed_num = reversed_num * 10 + last_digit
        num = num // 10
    if x == reversed_num:
        return True

    return False


digits = 3
largest = 0
max_range = 10 ** digits
min_range = 10 ** (digits - 1)

i = min_range
while i < max_range:
    j = min_range
    while j < max_range:
        product = i * j
        if palindrome(product) and (product) > largest:
            largest = product
        j += 1
    i += 1

print(largest)
