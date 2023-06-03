# Create an inheritance from calculator.py

import math
from calculator import Calculator

class Calculator (Calculator):
    
    def square_root(self, num1):
        square_root = math.sqrt (num1)
        return square_root