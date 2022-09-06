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
root.geometry("600x850")
# root.configure(bg="black")


class IconsLoader:

    def __init__(self, abspath: str, relpath: str = ...) -> None:
        self.abspath = abspath
        self.relpath = relpath

    def __str__(self) -> str:
        return f"IconsLoader: (abspath={self.abspath}, relpath={self.relpath})"

    def __repr__(self) -> str:
        return self.__str__()

    def loadDigitIcons(self) -> tuple[PhotoImage, ...]:
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

    def loadOperatorIcons(self) -> tuple[PhotoImage, ...]:
        abspath = "D:\Programming\Projects\Python\GUI Projects\Calculator\icons\operators\\"
        add = PhotoImage(file=f"{abspath}add.png")
        subtract = PhotoImage(file=f"{abspath}subtract.png")
        multiply = PhotoImage(file=f"{abspath}multiply.png")
        divide = PhotoImage(file=f"{abspath}divide.png")
        percentage = PhotoImage(file=f"{abspath}percentage.png")
        equalTo = PhotoImage(file=f"{abspath}equalTo.png")
        return (add, subtract, multiply, divide, percentage, equalTo)

    def loadOtherIcons(self) -> tuple[PhotoImage, ...]:
        abspath = "D:\Programming\Projects\Python\GUI Projects\Calculator\icons\others\\"
        clear = PhotoImage(file=f"{abspath}clear.png")
        backspace = PhotoImage(file=f"{abspath}backspace.png")
        dot = PhotoImage(file=f"{abspath}decimal.png")
        return (clear, backspace, dot)


class PlaceIcons:
    def __init__(self, master: str, border: str = "0") -> None:
        ...

    def createDigitButtons(self) -> None:
        digitIconsTuple = IconsLoader().loadDigitIcons()
        self.zero_btn = Button(root, image=digitIconsTuple[0], border="0")
        self.one_btn = Button(root, image=digitIconsTuple[1], border="0")
        self.two_btn = Button(root, image=digitIconsTuple[2], border="0")
        self.three_btn = Button(root, image=digitIconsTuple[3], border="0")
        self.four_btn = Button(root, image=digitIconsTuple[4], border="0")
        self.five_btn = Button(root, image=digitIconsTuple[5], border="0")
        self.six_btn = Button(root, image=digitIconsTuple[6], border="0")
        self.seven_btn = Button(root, image=digitIconsTuple[7], border="0")
        self.eight_btn = Button(root, image=digitIconsTuple[8], border="0")
        self.nine_btn = Button(root, image=digitIconsTuple[9], border="0")

    def createOperatorButtons(self) -> None:
        addIcon, subtractIcon, multiplyIcon, divideIcon, percentageIcon, equalToIcon = IconsLoader().loadOperatorIcons()
        self.add_btn = Button(root, image=addIcon, border="0")
        self.subtract_btn = Button(root, image=subtractIcon, border="0")
        self.multiply_btn = Button(root, image=multiplyIcon, border="0")
        self.divide_btn = Button(root, image=divideIcon, border="0")
        self.percentage_btn = Button(root, image=percentageIcon, border="0")
        self.equalTo_btn = Button(root, image=equalToIcon, border="0")

    def createOtherButtons(self) -> None:
        clearIcons, backspaceIcon, decimalIcon = IconsLoader().loadOtherIcons()
        self.clear_btn = Button(root, image=clearIcons, border="0")
        self.backspaceIcon_btn = Button(root, image=backspaceIcon, border="0")
        self.decimalIcon_btn = Button(root, image=decimalIcon, border="0")

    def placeButtons(self) -> None:
        # Packing the buttons
        # space between two button on x-axis (column width) = 120 units
        # space between two rows on y-axis (row height) = 120 units

        # 0th row
        self.clear_btn.place(x=50, y=80)
        self.backspaceIcon_btn.place(x=170, y=80)
        self.percentage_btn.place(x=290, y=80)
        self.divide_btn.place(x=410, y=80)
        # first row
        self.seven_btn.place(x=50, y=200)
        self.eight_btn.place(x=170, y=200)
        self.nine_btn.place(x=290, y=200)
        self.multiply_btn.place(x=410, y=200)
        # 2nd row
        self.four_btn.place(x=50, y=320)
        self.five_btn.place(x=170, y=320)
        self.six_btn.place(x=290, y=320)
        self.subtract_btn.place(x=410, y=320)
        # 3rd row
        self.one_btn.place(x=50, y=440)
        self.two_btn.place(x=170, y=440)
        self.three_btn.place(x=290, y=440)
        self.add_btn.place(x=410, y=440)
        # 4th row
        self.zero_btn.place(x=170, y=560)
        self.decimalIcon_btn.place(x=290, y=560)
        self.equalTo_btn.place(x=410, y=560)


root.mainloop()
