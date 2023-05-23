
from tkinter import *
from design_tkinter import Design


class Operations:
    
    def calc_operation():
        
        root = Tk()
        root.geometry("450x200")
        root.configure(bg="gray")
        root.title("Calculator")

        # Create label for direction
        direction_label = Label(root, text="Select an operation", bg="gray", fg="black", font=("Arial", 16, "bold"))
        direction_label.pack()

        # Create close button
        close_button = Button(root, text="Close", bg="red", fg="white", command=root.destroy)
        close_button.pack(side="bottom")

        
        # Create addition operation button
        addition_button = Button(root, text="Addition", bg="black", fg="white", command=Design.subtraction)
        addition_button.pack()
        
        # Create subtraction operation button
        subtraction_button = Button(root, text="Subtraction", bg="black", fg="white", command=Design.subtraction)
        subtraction_button.pack()
        
        # Create multiplication operation button
        multiplication_button = Button(root, text="Multiplication", bg="black", fg="white", command=Design.multiplication)
        multiplication_button.pack()

        # Create division operation button
        division_button = Button(root, text="Division", bg="black", fg="white", command=Design.division)
        division_button.pack()

        root.mainloop()
    