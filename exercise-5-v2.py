"""
Addition program using GUI (tkinter)

Created by: Matthew Cheng
Modified from exercise 5

Version 1: meets brief specifications
"""

from tkinter import *

def quit():
    '''Close the window'''
    root.destroy()
    
    
def print_text():
    '''Print the text in the entry box'''
    num1 = int(top_box.get())
    num2 = int(box.get())
    
    answer = num1 + num2
    #print(answer)
    result.set(answer) # Change label to answer
   
    
def clear_entry():
    '''Clear entry boxes for number input'''
    top_box.delete(0, END) # Clears top box
    box.delete(0, END) # Clears bottom box
    
    result.set("") # Resets to blank input 
    
# Main program
root = Tk()
root.title("Exercise 5")
root.resizable(0,0)

# Initialise the result label
result = IntVar()
result.set("") # Set it to nothing when program first starts

# Create a entry box above the plus sign
top_box = Entry(root, justify = CENTER)
top_box.pack(fill=X, ipady = 10)

# Create a label for the plus sign
plus_sign = Label(root, text = "+", font = "Arial 30 bold")
plus_sign.pack(fill=X)

# Create an entry box below the plus sign
box = Entry(root, justify = CENTER)
box.pack(fill=X, ipady = 10)

# Create label which will print out result of calculation
output = Label(root, font = "Arial 30",
               textvariable = result)
output.pack(fill=X, ipady = 10)

# Create print button
button_print = Button(root, text = "Print", width = 10, command = print_text)
button_print.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

# Create reset button
button_reset = Button(root, text = "Reset", width = 10, command = clear_entry)
button_reset.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

# Create quit button
button_quit = Button(root, text = "Quit", width = 10, command = quit)
button_quit.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

# Create window
root.mainloop()