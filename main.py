from tkinter import *

win = Tk()
win.title("mile to km converter")
win.minsize(width=400, height=100)
x = 0


def cal():
    if x == 0:
        kmp = str(round(float(input_mile.get()) * 1.609, 2))
        output_km.delete(1.0, END)
        output_km.insert(END, kmp)
    else:
        kmp = str(round(float(input_mile.get()) / 1.609, 2))
        output_km.delete(1.0, END)
        output_km.insert(END, kmp)


def switch():
    global x
    if x == 0:
        x = 1
        mile.grid(column=2, row=1)
        km.grid(column=2, row=0)
    else:
        x = 0
        mile.grid(column=2, row=0)
        km.grid(column=2, row=1)


mile = Label(text="Mile")
mile.grid(column=2, row=0)
km = Label(text="Km")
km.grid(column=2, row=1)
is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)
is_equal.config(padx=50)
input_mile = Entry(width=13)
input_mile.grid(column=1, row=0)
output_km = Text(height=1, width=10)
output_km.grid(column=1, row=1)
clac = Button(text="calculate", command=cal)
clac.grid(column=1, row=2)
switch_button = Button(text="switch", command=switch)
switch_button.grid(column=1, row=3)

mainloop()