# Create a inheritance for square root's design

# Import modules
from tkinter import *
from designed_calculator import Design
from sqrt_inheritance import Calculator

# Create a class for square root calculator
class SqrtCalc(Design, Calculator):
    
    def __init__(self):
        super().__init__()
        self.calculator = Calculator()
        
    # Define function and create window for square root operation 
    def square_root(self):
        square_root_window = Tk()
        square_root_window.title("Square Root")
        square_root_window.geometry("450x200")
        square_root_window.config(bg="gray")
        
        # Create label for input
        input_label = Label(square_root_window, text="Input:", fg="black", bg="gray", font=("Arial", 12, "bold"))
        input_label.grid(row=1, column=5, pady=15)
        
        # Create textbox for input
        input_textbox = Entry(square_root_window, fg="black", font=("Arial", 12, "bold"))
        input_textbox.grid(row=1, column=20)
        
        # Define function to calculate square root
        def calculate_square_root():
            try:
                num = float(input_textbox.get())
                result = self.calculator.square_root(num)
                empty_label.config(fg="black", text="Result: " + str(result))
            except ValueError:
                empty_label.config(text="Please enter a valid number!", fg="red")
        
        # Create calculate button
        calculate_button = Button(square_root_window, command=calculate_square_root, text="Calculate", fg="black", font=("Arial", 12, "bold"))
        calculate_button.grid(row=5, column=20, sticky=W)
        
        # Create empty label to show total
        empty_label = Label(square_root_window, fg="black", bg="gray", font=("Arial", 12, "bold"))
        empty_label.grid(row=15, column=20, sticky=W)
        
        # Create back button
        back_button = Button(square_root_window, text="Back", bg="red", fg="white", command=square_root_window.destroy)
        back_button.grid(row=5, column=50, sticky=W)
        
        square_root_window.mainloop()
        