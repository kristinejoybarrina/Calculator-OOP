
from tkinter import *

class Calculator:

    def sum():
        addition_window = Tk()    
        first = Design.addition
        print (first)

        def first_input ():
            first = first_input_textbox.get()
            return first
                
        def second_input ():
            second = second_input_textbox.get()
            return second
                    # Use try-catch to show error inputs
        try:
                        
            total = "haha"
            empty_label.config(fg="black", text="Total: " + str(total))
                        
        except ValueError:
            empty_label.config(text="Please enter an integer!", fg="red") 
            
            # Create calculate button
 
    
    