# Create a inheritance for square root's design

from designed_calculator import Design
from sqrt_inheritance import Calculator

# Create a class for square root calculator
class SqrtCalc(Design, Calculator):
    def __init__(self):
        super().__init__()
        self.calculator = Calculator()