from tkinter import *


class IconsLoader:
    """
        IconsLoader class for loading all icons for calculator.

        Attributes:
            abspath (str): Absolute path of the icons directory.
            relpath (str): Relative path of the icons directory.

        Methods:
            ...
    """

    def __init__(self, abspath: str, relpath: str = ...) -> None:
        """
            Constructor for IconsLoader class.
        Args:
            abspath (str): Absolute path of the icons directory.
            relpath (str, optional): Relative path of the icons directory. Defaults to ....
        """
        self.abspath = abspath
        self.relpath = relpath

    def __str__(self) -> str:
        return f"IconsLoader: (abspath={self.abspath}, relpath={self.relpath})"

    def __repr__(self) -> str:
        return self.__str__()

    def loadDigitIcons(self) -> tuple[PhotoImage, ...]:
        """
        Summary:
            Method to load all digits icons.

        Parameters:
            None

        Returns:
            tuple[PhotoImage, ...]: PhotoImage objects of all digits.
        """
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
        """
        Summary:
            Method to load all operators icons.

        Parameters:
            None

        Returns:
            tuple[PhotoImage, ...]: PhotoImage objects of all operators icons.
        """

        abspath = self.abspath
        add = PhotoImage(file=f"{abspath}add.png")
        subtract = PhotoImage(file=f"{abspath}subtract.png")
        multiply = PhotoImage(file=f"{abspath}multiply.png")
        divide = PhotoImage(file=f"{abspath}divide.png")
        percentage = PhotoImage(file=f"{abspath}percentage.png")
        equalTo = PhotoImage(file=f"{abspath}equalTo.png")
        return (add, subtract, multiply, divide, percentage, equalTo)

    def loadOtherIcons(self) -> tuple[PhotoImage, ...]:
        """
        Summary:
            Method to load rest icons.

        Parameters:
            None

        Returns:
            tuple[PhotoImage, ...]: PhotoImage objects of all remaining icons.
        """

        abspath = self.abspath
        clear = PhotoImage(file=f"{abspath}clear.png")
        backspace = PhotoImage(file=f"{abspath}backspace.png")
        dot = PhotoImage(file=f"{abspath}decimal.png")
        return (clear, backspace, dot)
