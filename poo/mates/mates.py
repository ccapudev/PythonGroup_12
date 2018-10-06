from math import factorial as fct


def factorial(n):
    return fct(n)

def gcd(a, b):
    return gcd(b, a % b)