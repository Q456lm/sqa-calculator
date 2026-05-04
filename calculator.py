import math

class calculator:
    @staticmethod
    def add(a,b):
        return a + b
    @staticmethod
    def subtract(a,b):
        return a - b
    @staticmethod
    def multiply(a,b):
        return a * b
    @staticmethod
    def divide(a,b):
        if b == 0:
            raise ZeroDivisionError("You can't divide by zero!")
        return a / b
    @staticmethod
    def power(base,exp):
        if base == 0 and exp == 0:
            raise ValueError("Erm actually in high level contexts zero raised to the power of zero is undefined!")
        return pow(base,exp)
    @staticmethod
    def square_root(a):
        if a < 0:
            raise ValueError("You can't take the square root of a negative number!")
        return math.sqrt(a)
    @staticmethod
    def modulus(a,b):
        if b == 0:
            raise ZeroDivisionError("You can't divide by zero!")
        return a % b
    @staticmethod    
    def floor_divide(a,b):
        if b == 0:
            raise ZeroDivisionError("You can't divide by zero!")
        return a // b