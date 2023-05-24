class Calculator:
    
    # define method for addition operation
    def addition(self, num1, num2):
        return num1 + num2
    
    # define method for subtraction operation
    def subtraction(self, num1, num2):
        return num1 - num2

    # define method for multiplication operation
    def multiplication(self, num1, num2):
        return num1 * num2

    # define method for division operation
    def division(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            raise ZeroDivisionError("Cannot divide by zero.")
