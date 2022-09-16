from IconsLoader import IconsLoader
from typing import Literal
from functools import partial
from tkinter import *


class PlaceIcons:
    """
    Summary:
        Class for placing all icons in the GUI.
    """

    def __init__(self, master: Tk, border: str = "0", cursorType: Literal["circle", "hand2", "..."] = "arrow") -> None:
        """
            Summary:
                Constructor for PlaceIcons class.

        Args:
            master (Tk):
                Description: The window where you want to place all the icons.
            border (str, optional): 
                Description: Defaults to "0".
            cursorType (Literal["circle","hand2","..."], optional): 
                Description: Defaults to "arrow".

        Returns:
            None
        """
        self.root = master
        self.border = border
        self.cursorType = cursorType
        self.digitButtons = []

    def createDigitButtons(self) -> None:
        """
            summary:
                Creates digit buttons and stores them in a list 'digitButtons' attribute of the instance.
                digitButtons is a list of 10 buttons in which button are stored in the order of their index.
                E.g., digitButtons[0] is the button for 0, digitButtons[1] is the button for 1 and so on.
            Parameter:
                None
            Returns:
                None
        """
        digitIconsTuple = IconsLoader(
            "D:\Programming\Projects\Python\GUI Projects\Calculator\icons\digits\\").loadDigitIcons()
        for i in range(10):
            self.digitButtons.append(Button(
                self.root, image=digitIconsTuple[i], border=self.border, cursor=self.cursorType, command=partial(print, i)))

        """
            Issue:
                * Icons are not showing up in the GUI.
                * The reason is that Python Garbage Collector is deleting the PhotoImage objects because they are stored as a local variable at somewhere in 'Button' objects.
                * So, Now we will create an custom attribute name 'saveImage' in 'Button' class and store the PhotoImage object in it.
                * So, now the PhotoImage object's reference stored in 'saveImage' attribute of 'Button' class and if local variable containing the same reference deleted then also only alias will deleted, not the actual object reference.
                * Now, the attribute 'saveImage' will an instance attribute and will not be deleted by Python Garbage Collector until existence of 'Button' object.
                * In Button object, the PhotoImage object referenced pointed by it, will still available in it's scope because it's reference are stored in one of it's attribute.
                * See more: https://stackoverflow.com/questions/3359717/cannot-display-an-image-in-tkinter
        """

        for i in range(10):
            self.digitButtons[i].saveImage = digitIconsTuple[i]

    def createOperatorButtons(self) -> None:
        """
            Summary:
                Creates operator buttons (with the help of class IconsLoader) and stores all as attributes of the instance.
            Parameters:
                None
            Returns:
                None
        """
        addIcon, subtractIcon, multiplyIcon, divideIcon, percentageIcon, equalToIcon = IconsLoader(
            "D:\Programming\Projects\Python\GUI Projects\Calculator\icons\operators\\").loadOperatorIcons()
        self.add_btn = Button(self.root, image=addIcon,
                              border=self.border, cursor=self.cursorType)
        self.subtract_btn = Button(
            self.root, image=subtractIcon, border=self.border, cursor=self.cursorType)
        self.multiply_btn = Button(
            self.root, image=multiplyIcon, border=self.border, cursor=self.cursorType)
        self.divide_btn = Button(
            self.root, image=divideIcon, border=self.border, cursor=self.cursorType)
        self.percentage_btn = Button(
            self.root, image=percentageIcon, border=self.border, cursor=self.cursorType)
        self.equalTo_btn = Button(
            self.root, image=equalToIcon, border=self.border, cursor=self.cursorType)

        # adding a 'saveImage' attribute to all 'Button' instances to store the reference of the PhotoImage object. So, that garbage collection will not delete them.
        self.add_btn.saveImage = addIcon
        self.add_btn.subtract_btn = subtractIcon
        self.multiply_btn.saveImage = multiplyIcon
        self.divide_btn.saveImage = divideIcon
        self.percentage_btn.saveImage = percentageIcon
        self.equalTo_btn.saveImage = equalToIcon

    def createOtherButtons(self) -> None:
        """
            Summary:
                Creates rest others buttons (with the help of class IconsLoader) and stores all as attributes of the instance.
            Parameters:
                None
            Returns:
                None
        """
        clearIcons, backspaceIcon, decimalIcon = IconsLoader(
            "D:\Programming\Projects\Python\GUI Projects\Calculator\icons\others\\").loadOtherIcons()
        self.clear_btn = Button(
            self.root, image=clearIcons, border=self.border, cursor=self.cursorType)
        self.backspaceIcon_btn = Button(
            self.root, image=backspaceIcon, border=self.border, cursor=self.cursorType)
        self.decimalIcon_btn = Button(
            self.root, image=decimalIcon, border=self.border, cursor=self.cursorType)

        # adding a 'saveImage' attribute to all 'Button' instances to store the reference of the PhotoImage object. So, that garbage collection will not delete them.
        self.clear_btn.saveImage = clearIcons
        self.backspaceIcon_btn.saveImage = backspaceIcon
        self.decimalIcon_btn.saveImage = decimalIcon

    def placeButtons(self) -> None:
        """
            Summary:
                Place all buttons in the GUI at absolute position.
            Parameters:
                None
            Returns:
                None
        """
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
