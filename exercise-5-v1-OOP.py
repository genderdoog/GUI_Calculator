'''
Object oriented program version of exercise 5 

Create by: Matthew Cheng
'''

from tkinter import *

class Program: 
    
    def __init__(self, master):
        self.master = master
        
        master.title("Exercise 5")
        master.resizable(0,0)
        
        # Create an entry box
        self.box = Entry(root, justify = CENTER)
        self.box.pack(fill=X, ipady = 10)
        
        # Create two buttons
        self.button_print = Button(root, text = "Print", width = 10, command = self.print_text)
        self.button_print.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)
        
        self.button_quit = Button(root, text = "Quit", width = 10, command = self.quit)
        self.button_quit.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)        
        
    def quit(self):
        '''Close the window'''
        self.master.destroy() # Closes the window
        
    def print_text(self):
        '''Print the text in the entry box'''
        print(self.box.get())
    
# Main program
root = Tk() # Create a tkinter window
app = Program(root) # Create object named app with Program class using the newly created tkinter window
root.mainloop() # Show window