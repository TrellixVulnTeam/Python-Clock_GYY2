from tkinter import *
from time import strftime
root = Tk()
root.title("Python Clock")


def time():
    currenttime = strftime('%I:%M:%S %p')
    label.config(text=currenttime)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 90), backgroun="black", foreground="green")
label.pack(anchor='center')
time()
mainloop()