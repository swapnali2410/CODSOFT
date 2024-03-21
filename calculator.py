from tkinter import *

expression = "" 

def press(num): 
    global expression 
    expression = expression + str(num) 
    equation.set(expression) 

def equalpress():  
    try: 
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = "" 
    except: 
        equation.set(" error ") 
        expression = "" 

def clear(): 
    global expression 
    expression = "" 
    equation.set("") 

if __name__ == "__main__": 
    gui = Tk() 
    gui.configure(background="#e8b7ed") 
    gui.title("Simple Calculator") 

    # Increase the size of the window
    gui.geometry("350x250") 

    equation = StringVar() 

    expression_field = Entry(gui, textvariable=equation,font=('Arial', 12), justify='right', bd=5, relief=SUNKEN, width=30) 
    expression_field.grid(row=0, column=0, columnspan=4, pady=10) 

    # Create buttons for digits and operations
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    # Place buttons in a grid
    row = 1
    col = 0
    for button in buttons:
        if button == '=':
            b = Button(gui, text=button, fg='black', bg='#a221b0', command=equalpress, height=1, width=7)
        elif button == '0':
            b = Button(gui, text=button, fg='black', bg='#a221b0', command=lambda: press(0), height=1, width=10)
        else:
            b = Button(gui, text=button, fg='black', bg='#a221b0', command=lambda button=button: press(button), height=1, width=7)
        b.grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col > 3:
            col = 0
            row += 1

    # Center the calculator within the window
    gui.update_idletasks()
    width = gui.winfo_width()
    height = gui.winfo_height()
    x = (gui.winfo_screenwidth() // 2) - (width // 2)
    y = (gui.winfo_screenheight() // 2) - (height // 2)
    gui.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # Start the GUI 
    gui.mainloop()
