"""
    Calculator (GUI) using Tkinter and Python 3.10.5
     @author: Suraj Kumar Giri.
     @Date: 05-09-2022 (Started)
     @Time: 02: 34: 39 (Started)
     @last modified: 13th Sep 2022
"""

from tkinter import *
from sys import path
path[0] = "D:\\Programming\\Projects\\Python\\GUI Projects\\Calculator"


class IconsLoader:

    def __init__(self, abspath: str, relpath: str = ...) -> None:
        self.abspath = abspath
        self.relpath = relpath

    def __str__(self) -> str:
        return f"IconsLoader: (abspath={self.abspath}, relpath={self.relpath})"

    def __repr__(self) -> str:
        return self.__str__()

    def loadDigitIcons(self) -> tuple[PhotoImage, ...]:
        abspath = self.abspath
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
        abspath = self.abspath
        add = PhotoImage(file=f"{abspath}add.png")
        subtract = PhotoImage(file=f"{abspath}subtract.png")
        multiply = PhotoImage(file=f"{abspath}multiply.png")
        divide = PhotoImage(file=f"{abspath}divide.png")
        percentage = PhotoImage(file=f"{abspath}percentage.png")
        equalTo = PhotoImage(file=f"{abspath}equalTo.png")
        return (add, subtract, multiply, divide, percentage, equalTo)

    def loadOtherIcons(self) -> tuple[PhotoImage, ...]:
        abspath = self.abspath
        clear = PhotoImage(file=f"{abspath}clear.png")
        backspace = PhotoImage(file=f"{abspath}backspace.png")
        dot = PhotoImage(file=f"{abspath}decimal.png")
        return (clear, backspace, dot)


class PlaceIcons:
    def __init__(self, master: Tk, border: str = "0") -> None:
        self.root = master
        self.border = border
        self.digitButtons = []

    def createDigitButtons(self) -> None:
        """
            summary:
                Creates digit buttons and stores them in a list 'digitButtons' attribute of the instance.
                digitButtons is a list of 10 buttons in which button are stored in the order of their index.
                E.g., digitButtons[0] is the button for 0, digitButtons[1] is the button for 1 and so on.
        """
        digitIconsTuple = IconsLoader(
            "D:\Programming\Projects\Python\GUI Projects\Calculator\icons\digits\\").loadDigitIcons()
        for i in range(10):
            self.digitButtons.append(Button(
                self.root, image=digitIconsTuple[i], border=self.border))

    def createOperatorButtons(self) -> None:
        addIcon, subtractIcon, multiplyIcon, divideIcon, percentageIcon, equalToIcon = IconsLoader(
            "D:\Programming\Projects\Python\GUI Projects\Calculator\icons\operators\\").loadOperatorIcons()
        self.add_btn = Button(self.root, image=addIcon, border=self.border)
        self.subtract_btn = Button(
            self.root, image=subtractIcon, border=self.border)
        self.multiply_btn = Button(
            self.root, image=multiplyIcon, border=self.border)
        self.divide_btn = Button(
            self.root, image=divideIcon, border=self.border)
        self.percentage_btn = Button(
            self.root, image=percentageIcon, border=self.border)
        self.equalTo_btn = Button(
            self.root, image=equalToIcon, border=self.border)

    def createOtherButtons(self) -> None:
        clearIcons, backspaceIcon, decimalIcon = IconsLoader(
            "D:\Programming\Projects\Python\GUI Projects\Calculator\icons\others\\").loadOtherIcons()
        self.clear_btn = Button(
            self.root, image=clearIcons, border=self.border)
        self.backspaceIcon_btn = Button(
            self.root, image=backspaceIcon, border=self.border)
        self.decimalIcon_btn = Button(
            self.root, image=decimalIcon, border=self.border)

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
        self.digitButtons[7].place(x=50, y=200)  # for button 7
        self.digitButtons[8].place(x=170, y=200)  # for button 8
        self.digitButtons[9].place(x=290, y=200)  # for button 9
        self.multiply_btn.place(x=410, y=200)
        # 2nd row
        self.digitButtons[4].place(x=50, y=320)  # for button 4
        self.digitButtons[5].place(x=170, y=320)  # for button 5
        self.digitButtons[6].place(x=290, y=320)  # for button 6
        self.subtract_btn.place(x=410, y=320)
        # 3rd row
        self.digitButtons[1].place(x=50, y=440)  # for button 1
        self.digitButtons[2].place(x=170, y=440)  # for button 2
        self.digitButtons[3].place(x=290, y=440)  # for button 3
        self.add_btn.place(x=410, y=440)
        # 4th row
        self.digitButtons[0].place(x=170, y=560)  # for button 0
        self.decimalIcon_btn.place(x=290, y=560)
        self.equalTo_btn.place(x=410, y=560)

    def placeIconsOnGUI(self):
        self.createDigitButtons()
        self.createOperatorButtons()
        self.createOtherButtons()
        self.placeButtons()


def main():
    root = Tk()  # master/root windows
    root.title("Calculator")
    root.geometry("600x850")
    # root.configure(bg="black")

    PlaceIcons(root).placeIconsOnGUI()
    input()
    root.mainloop()


if __name__ == '__main__':
    main()
