import tkinter as tk

def display1():
    print("Checkbox of x " , x.get())

def display2():
    print("Checkbox of y " , y.get())

win = tk.Tk()
win.title("My First Application")
win.minsize(500,500)

x = tk.IntVar()
y = tk.IntVar()
ch1 = tk.Checkbutton(win, text="C++", variable=x, command=display1)
ch2 = tk.Checkbutton(win, text="Java", variable=y, command=display2)
x.set(0)
y.set(0)

ch1.pack()
ch2.pack()



win.mainloop()