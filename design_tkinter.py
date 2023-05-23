# import python module
from tkinter import *
import pyfiglet
from calculator import Calculator

# Create notice text that the program starts
notice_text = pyfiglet.figlet_format("Calculator", font="slant")
print("\033[1;31m" + notice_text)

# Define a function called First_Window
class Design:
    
    def ask_first_input ():
        addition_window = Tk()
        addition_window.title("Addition")
        addition_window.geometry("450x200")
        addition_window.config(bg="gray")
        addition_window = Tk()
        
    # Create label for first input
        first_input_label = Label(addition_window, text="First input:", fg="black", bg="gray", font=("Arial", 12, "bold"))
        first_input_label.grid(row=1, column=5, pady=15)
        

        
        # Create textbox for first input
        first_input_textbox = Entry(addition_window, fg="black", font=("Arial", 12, "bold"))
        first_input_textbox.grid(row=1, column=20)
        
        addition_window.mainloop()
    
    def ask_second_input ():   
         
        addition_window = Tk()
        
        # Create label for second input
        second_input_label = Label(addition_window, text="Second input:", fg="black", bg="gray", font=("Arial", 12, "bold"))
        second_input_label.grid(row=2, column=5, pady=15)
        
        # Create textbox for second input
        second_input_textbox = Entry(addition_window, fg="black", font=("Arial", 12, "bold"))
        second_input_textbox.grid(row=2, column=20)

    
    
    
    # Define function and create window for addition operation 
    def addition():
        addition_window = Tk()
        addition_window.title("Addition")
        addition_window.geometry("450x200")
        addition_window.config(bg="gray")
        # Define function to apply addition operation
        calculate_button = Button(addition_window, command=sum, text="Calculate", fg="black", font=("Arial", 12, "bold"))
        calculate_button.grid(row=5, column=20, sticky=W)
            
            # Create empty label to show total 
        empty_label = Label(addition_window, fg="black", bg="gray", font=("Arial", 12, "bold"))
        empty_label.grid(row=15, column=20, sticky=W)
            
            # Create back button
        back_button = Button(addition_window, text="Back", bg="red", fg="white", command=addition_window.destroy)
        back_button.grid(row=5, column=50, sticky=W)

        
        addition_window.mainloop()
        
    # Define function and create window for subtraction operation 
    def subtraction():
        subtraction_window = Tk()
        subtraction_window.title("Subtraction")
        subtraction_window.geometry("450x200")
        subtraction_window.config(bg="gray")
        
        
        # Define function to apply subtraction operation
        def difference():
            
            # Use try-catch to show error inputs
            try:
                
                total = (float(first_input_textbox.get()) - float(second_input_textbox.get()))
                empty_label.config(fg="black", text="Total: " + str(total))
                
            except ValueError:
                empty_label.config(text="Please enter an integer!", fg="red") 
        
        # Create calculate button
        calculate_button = Button(subtraction_window, command=difference, text="Calculate", fg="black", font=("Arial", 12, "bold"))
        calculate_button.grid(row=5, column=20, sticky=W)
        
        # Create empty label to show total 
        empty_label = Label(subtraction_window, fg="black", bg="gray", font=("Arial", 12, "bold"))
        empty_label.grid(row=15, column=20, sticky=W)
        
        # Create back button
        back_button = Button(subtraction_window, text="Back", bg="red", fg="white", command=subtraction_window.destroy)
        back_button.grid(row=5, column=50, sticky=W)
        
        subtraction_window.mainloop()
        
        
    # Define function and create window for multiplication operation 
    def multiplication():
        multiplication_window = Tk()
        multiplication_window.title("Multiplication")
        multiplication_window.geometry("450x200")
        multiplication_window.config(bg="gray")
        
        
        # Define function to apply multiplication operation
        def product():
            
            # Use try-catch to show error inputs
            try:
                
                total = (float(first_input_textbox.get()) * float(second_input_textbox.get()))
                empty_label.config(fg="black", text="Total: " + str(total))
                
            except ValueError:
                empty_label.config(text="Please enter an integer!", fg="red") 
        
        # Create calculate button
        calculate_button = Button(multiplication_window, command=product, text="Calculate", fg="black", font=("Arial", 12, "bold"))
        calculate_button.grid(row=5, column=20, sticky=W)
        
        # Create empty label to show total 
        empty_label = Label(multiplication_window, fg="black", bg="gray", font=("Arial", 12, "bold"))
        empty_label.grid(row=15, column=20, sticky=W)
        
        # Create back button
        back_button = Button(multiplication_window, text="Back", bg="red", fg="white", command=multiplication_window.destroy)
        back_button.grid(row=5, column=50, sticky=W)
        
        multiplication_window.mainloop()

    # Define function and create window for division operation 
    def division():
        division_window = Tk()
        division_window.title("Division")
        division_window.geometry("450x200")
        division_window.config(bg="gray")
        
        
        
        # Define function to apply division operation
        def quotient():
            
            # Use try-catch to show error inputs
            try:
                total = (float(first_input_textbox.get()) / float(second_input_textbox.get()))
                empty_label.config(fg="black", text="Total: " + str(total))
                
            except ValueError:
                empty_label.config(text="Please enter an integer!", fg="red") 
                
            except ZeroDivisionError:
                empty_label.config(text="Zero division error! \n Please try again.", fg="red") 
        
        # Create calculate button
        calculate_button = Button(division_window, command=quotient, text="Calculate", fg="black", font=("Arial", 12, "bold"))
        calculate_button.grid(row=5, column=20, sticky=W)
        
        # Create empty label to show total 
        empty_label = Label(division_window, fg="black", bg="gray", font=("Arial", 12, "bold"))
        empty_label.grid(row=15, column=20, sticky=W)
        
        # Create back button
        back_button = Button(division_window, text="Back", bg="red", fg="white", command=division_window.destroy)
        back_button.grid(row=5, column=50, sticky=W)
        
        division_window.mainloop()

    # Create a window
    

