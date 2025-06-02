from tkinter import *

def quit():
    '''Close the window'''
    root.destroy()
    
def print_text():
    '''Print the text in the entry box'''
    print(box.get())
    
# Main program
root = Tk()
root.title("Exercise 5")
root.resizable(0,0)

# Create an entry box
box = Entry(root, justify = CENTER)
box.pack(fill=X, ipady = 10)

# Create two buttons
button_print = Button(root, text = "Print", width = 10, command = print_text)
button_print.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

button_quit = Button(root, text = "Quit", width = 10, command = quit)
button_quit.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

root.mainloop()