from tkinter import *

window = Tk()
window.title("First Python GUI")
window.minsize(width=700, height=500)
window.config(padx=20, pady=20)

def button_listener():
    my_label.config(text=input.get())

my_label = Label(text="This is a label.", font=("Arial", 24, "italic"))
my_label.grid(column=0, row=0)

button2 = Button(text="Click Me 2!")
button2.grid(column=2, row=0)

button = Button(text="Click Me!", command=button_listener)
button.grid(column=1, row=1)

input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
