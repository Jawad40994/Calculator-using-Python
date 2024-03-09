# Importing necessary libraries
from tkinter import *
from tkinter import Button

# Creating main window
win = Tk()
win.title('Calculator')
win.geometry('515x365')
win.resizable(0, 0)

# Function to handle button click events

def btn_click(item):
   global expression
   expression = expression + str(item)
   input_text.set(expression)

# Function to clear the input field

def bt_clear():
   global expression
   expression = ""
   input_text.set("")

# Function to evaluate the expression and display the result


def bt_equal():
   global expression
   result = str(eval(expression))
   input_text.set(result)
   expression = ""

# Initializing global variables

expression = ""
input_text = StringVar()

# Creating input field

input_frame = Frame(win, width= 312, height= 50)
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), width=45, justify= RIGHT, textvariable= input_text)
input_field.pack(ipady= 10)

# Creating buttons frame

btns_frame = Frame(win, width= 310, height=270)
btns_frame.pack()


# Creating buttons and assigning functions to them

clear = Button(btns_frame, text='C', width=38, height=3,  command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
Divide = Button(btns_frame, text='/', width=10, height=3, command=lambda: btn_click('/')).grid(row=0, column=3, padx=1, pady=1)


#First Row

Seven = Button(btns_frame, text='7', width=10, height=3, command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
Eight = Button(btns_frame, text='8', width=10, height=3, command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
Nine = Button(btns_frame, text='9', width=10, height=3, command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

#Second Row

Multiply = Button(btns_frame, text='*', width=10, height=3, command=lambda: btn_click('*')).grid(row=1, column=3, padx=1, pady=1)
Four = Button(btns_frame, text='4', width=10, height=3, command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
Five = Button(btns_frame, text='5', width=10, height=3, command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

#Third Row

Six = Button(btns_frame, text='6', width=10, height=3, command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
Minus = Button(btns_frame, text='-', width=10, height=3, command=lambda: btn_click('-')).grid(row=2, column=3, padx=1, pady=1)
One = Button(btns_frame, text='1', width=10, height=3, command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

#Fourth Row

Two = Button(btns_frame, text='2', width=10, height=3, command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
Three = Button(btns_frame, text='3', width=10, height=3, command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
Plus = Button(btns_frame, text='+', width=10, height=3, command=lambda: btn_click('+')).grid(row=3, column=3, padx=1, pady=1)

#Fifth Row

Zero = Button(btns_frame, text='0', width=24, height=3, command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = Button(btns_frame, text='.', width=10, height=3, command=lambda: btn_click('.')).grid(row=4, column=2, padx=1, pady=1)
Equal = Button(btns_frame, text='=', width=10, height=3, command= lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)


win.mainloop()