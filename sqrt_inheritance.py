# Create an inheritance from calculator.py

import math
from calculator import Calculator

class Calculator (Calculator):
    
    def square_root(self, num1, num2):
        square_root = math.sqrt (num1, num2)
        return square_root