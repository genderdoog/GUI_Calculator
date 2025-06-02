"""
Addition program using GUI (tkinter)

Created by: Matthew Cheng
Modified from exercise 5

Version 1: meets brief specifications
Version 2: program converted to "Program" object
"""

from tkinter import *

class Program:
    
    def __init__(self, master):
        self.master = master
        
        master.title("Exercise 5")
        master.resizable(0,0)
        
        # Initialise the result label
        self.result = IntVar()
        self.result.set("") # Set it to nothing when program first starts 
        
        # Create a entry box above the plus sign
        self.top_box = Entry(root, font = "Arial 20",
                             justify = CENTER)
        self.top_box.pack(fill=X, ipady = 10)
        
        # Create a label for the plus sign
        self.plus_sign = Label(root, text = "+", font = "Arial 30 bold")
        self.plus_sign.pack(fill=X)
        
        # Create an entry box below the plus sign
        self.box = Entry(root, font = "Arial 20",
                         justify = CENTER)
        self.box.pack(fill=X, ipady = 10)
        
        # Create label which will print out result of calculation
        self.output = Label(root, font = "Arial 30 bold",
                       textvariable = self.result)
        self.output.pack(fill=X, ipady = 10)      
        
        # Create print button
        self.button_print = Button(root, text = "Print", width = 10, command = self.print_text)
        self.button_print.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)
        
        # Create reset button
        self.button_reset = Button(root, text = "Reset", width = 10, command = self.clear_entry)
        self.button_reset.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)
        
        # Create quit button
        self.button_quit = Button(root, text = "Quit", width = 10, command = self.quit)
        self.button_quit.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)        

    def quit(self):
        '''Close the window'''
        self.master.destroy()
        
        
    def print_text(self):
        '''Print the text in the entry box'''
        num1 = int(self.top_box.get())
        num2 = int(self.box.get())
        
        answer = num1 + num2
        #print(answer)
        self.result.set(answer) # Change the output label to answer
       
        
    def clear_entry(self):
        '''Clear entry boxes for number input'''
        self.top_box.delete(0, END) # Clears top box
        self.box.delete(0, END) # Clears bottom box
        
        self.result.set("") # Resets to blank input 
        
# Main program
root = Tk()
app = Program(root)
root.mainloop()
