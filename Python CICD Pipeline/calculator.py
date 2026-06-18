import math

class ScientificCalculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Can't divide by zero")
        return a / b

    def power(self, a, b):
        return a ** b

    def square_root(self, x):
        if x < 0:
            raise ValueError("Can't calculate square root of negative number")
        return math.sqrt(x)

    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        return math.factorial(n)

    def modulus(self, a, b):
        return a % b

    def absolute(self, x):
        return abs(x)

    def percentage(self, part, whole):
        if whole == 0:
            raise ValueError("Whole cannot be zero")
        return (part / whole) * 100

    def sin(self, angle):
        return round(math.sin(math.radians(angle)), 5)

    def cos(self, angle):
        return round(math.cos(math.radians(angle)), 5)

    def tan(self, angle):
        return round(math.tan(math.radians(angle)), 5)

    def logarithm(self, x):
        if x <= 0:
            raise ValueError("Logarithm only defined for positive numbers")
        return round(math.log10(x), 5)

    def average(self, numbers):
        if len(numbers) == 0:
            raise ValueError("List cannot be empty")
        return sum(numbers) / len(numbers)

    def maximum(self, numbers):
        return max(numbers)

    def minimum(self, numbers):
        return min(numbers)