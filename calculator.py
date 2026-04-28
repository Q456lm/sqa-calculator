import math

class Calculator:
    
    def add(a,b):
        return a + b
    
    def subtract(a,b):
        return a - b
    
    def multiply(a,b):
        return a * b
    
    def divide(a,b):
        if (b == 0):
            raise ZeroDivisionError
        return a / b
    
    def power(base,exp):
        return pow(base,exp)
    
    def square_root(a):
        if (a < 0):
            raise ValueError
        return math.sqrt(a)

    def modulus(a,b):
        if (b == 0):
            raise ZeroDivisionError
        return a%b

    def floor_divide(a,b):
        if (b == 0):
            raise ZeroDivisionError
        return a//b