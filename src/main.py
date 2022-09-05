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


def loadDigitIcons():
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


def loadOperatorIcons():
    abspath = "D:\Programming\Projects\Python\GUI Projects\Calculator\icons\operators\\"
    add = PhotoImage(file=f"{abspath}add.png")
    subtract = PhotoImage(file=f"{abspath}subtract.png")
    multiply = PhotoImage(file=f"{abspath}multiply.png")
    divide = PhotoImage(file=f"{abspath}divide.png")
    percentage = PhotoImage(file=f"{abspath}percentage.png")
    equalTo = PhotoImage(file=f"{abspath}equalTo.png")
    return (add, subtract, multiply, divide, percentage, equalTo)


digitIconsTuple = loadDigitIcons()
zero_btn = Button(root, image=digitIconsTuple[0], border="0")
one_btn = Button(root, image=digitIconsTuple[1], border="0")
two_btn = Button(root, image=digitIconsTuple[2], border="0")
three_btn = Button(root, image=digitIconsTuple[3], border="0")
four_btn = Button(root, image=digitIconsTuple[4], border="0")
five_btn = Button(root, image=digitIconsTuple[5], border="0")
six_btn = Button(root, image=digitIconsTuple[6], border="0")
seven_btn = Button(root, image=digitIconsTuple[7], border="0")
eight_btn = Button(root, image=digitIconsTuple[8], border="0")
nine_btn = Button(root, image=digitIconsTuple[9], border="0")

addIcon, subtractIcon, multiplyIcon, divideIcon, percentageIcon, equalToIcon = loadOperatorIcons()
add_btn = Button(root, image=addIcon, border="0")
subtract_btn = Button(root, image=subtractIcon, border="0")
multiply_btn = Button(root, image=multiplyIcon, border="0")
divide_btn = Button(root, image=divideIcon, border="0")
percentage_btn = Button(root, image=percentageIcon, border="0")
equalTo_btn = Button(root, image=equalToIcon, border="0")


# Packing the buttons
# space between two button on x-axis (column width) = 120 units
# space between two rows on y-axis (row height) = 120 units

# 0th row
percentage_btn.place(x=290, y=80)
divide_btn.place(x=410, y=80)
# first row
seven_btn.place(x=50, y=200)
eight_btn.place(x=170, y=200)
nine_btn.place(x=290, y=200)
multiply_btn.place(x=410, y=200)
# 2nd row
four_btn.place(x=50, y=320)
five_btn.place(x=170, y=320)
six_btn.place(x=290, y=320)
subtract_btn.place(x=410, y=320)
# 3rd row
one_btn.place(x=50, y=440)
two_btn.place(x=170, y=440)
three_btn.place(x=290, y=440)
add_btn.place(x=410, y=440)
# 4th row
zero_btn.place(x=170, y=560)
equalTo_btn.place(x=410, y=560)


root.mainloop()
