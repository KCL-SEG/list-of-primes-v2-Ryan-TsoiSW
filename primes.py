"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError('')
    else:
        count = 0
        num = 2
        isPrime = True
        while count<number_of_primes:
            for i in range (2,  num ):
                    if num % i==0:
                        isPrime = False
            if isPrime == True:
                list.append(num)
                count +=1
            num+=1
            isPrime = True
    return list
