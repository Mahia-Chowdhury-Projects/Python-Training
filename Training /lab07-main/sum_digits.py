"""
Lab 7, Warm-up Task 0

Sums the digits of a non-negative number.
"""


def sum_digits(num):
    """Given a non-negative integer num, return the sum of the
    digits of num.
    >>> sum_digits(1)
    1
    >>> sum_digits(8)
    8
    >>> sum_digits(90)
    9
    >>> sum_digits(178)
    16
    >>> sum_digits(1234567890)
    45
    >>> sum_digits(0)
    0
    """
    #base case 
    if num == 0: 
        return num
    #num%10 outputs last digit and int(sum_digits(num/10)) outputs everything but last digit
    else: 
        return (num%10 + int(sum_digits(num/10)))


# Standard code to run the doc tests
if __name__ == '__main__':
    '''DO NOT MODIFY.'''
    import doctest
    doctest.testmod()
