#!/usr/bin/python
import sys
import math

def is_prime(number):
    if (number <= 1):
        return False
    return all(number % i != 0 for i in range(2, 1 + int(math.sqrt(number))))

number = input("Enter a number : ")

if is_prime(int(number)):
    print '{} is a prime number'.format(number)
else:
    print '{} is not a prime number'.format(number)
