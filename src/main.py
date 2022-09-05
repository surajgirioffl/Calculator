"""
    Calculator (GUI) using Tkinter and Python 3.10.5
     @author: Suraj Kumar Giri.
     @Date: 05-09-2022 (Started)
     @Time: 02: 34: 39 (Started)
"""
from tkinter import *
from sys import path
path[0] = "D:\\Programming\\Projects\\Python\\GUI Projects\\Calculator"
root = Tk()  # master/root windows
root.title("Calculator")
root.geometry("600x700")
# root.configure(bg="black")


def loadDigitsImages():
    abspath = "D:\Programming\Projects\Python\GUI Projects\Calculator\icons\digits\\"
    zero = PhotoImage(file=f"{abspath}zero.png")
    one = PhotoImage(file=f"{abspath}one.png")
    two = PhotoImage(file=f"{abspath}two.png")
    three = PhotoImage(file=f"{abspath}three.png")
    four = PhotoImage(file=f"{abspath}four.png")
    five = PhotoImage(file=f"{abspath}five.png")
    six = PhotoImage(file=f"{abspath}six.png")
    seven = PhotoImage(file=f"{abspath}seven.png")
    eight = PhotoImage(file=f"{abspath}eight.png")
    nine = PhotoImage(file=f"{abspath}nine.png")
    return (zero, one, two, three, four, five, six, seven, eight, nine)


digitImagesTuple = loadDigitsImages()
zero_btn = Button(root, image=digitImagesTuple[0], border="0")
one_btn = Button(root, image=digitImagesTuple[1], border="0")
two_btn = Button(root, image=digitImagesTuple[2], border="0")
three_btn = Button(root, image=digitImagesTuple[3], border="0")
four_btn = Button(root, image=digitImagesTuple[4], border="0")
five_btn = Button(root, image=digitImagesTuple[5], border="0")
six_btn = Button(root, image=digitImagesTuple[6], border="0")
seven_btn = Button(root, image=digitImagesTuple[7], border="0")
eight_btn = Button(root, image=digitImagesTuple[8], border="0")
nine_btn = Button(root, image=digitImagesTuple[9], border="0")

# Packing the buttons
# space between two button on x-axis (column width) = 120 units
# space between two rows on y-axis (row height) = 120 units
# first row
seven_btn.place(x=50, y=200)
eight_btn.place(x=170, y=200)
nine_btn.place(x=290, y=200)
# 2nd row
four_btn.place(x=50, y=320)
five_btn.place(x=170, y=320)
six_btn.place(x=290, y=320)
# 3rd row
one_btn.place(x=50, y=440)
two_btn.place(x=170, y=440)
three_btn.place(x=290, y=440)
# 4th row
zero_btn.place(x=170, y=560)


root.mainloop()
