"""
    Calculator (GUI) using Tkinter and Python 3.10.5
     * author: Suraj Kumar Giri.
     * Date: 05-09-2022 (Started)
     * Time: 02: 34: 39 (Started)
     * last modified: 16th Sep 2022
"""

from tkinter import *
from sys import path
from PlaceIcons import PlaceIcons
path[0] = "D:\\Programming\\Projects\\Python\\GUI Projects\\Calculator"


def main():
    """
        Summary:
            Main function of the program from where execution of the program starts.
    """
    root = Tk()  # master/root windows
    root.title("Calculator")
    root.geometry("570x850")
    root.minsize(560, 760)
    # Creating a Canvas on root then place the icons on it instead of root. So that icons will also change it's position if we resize the root window.
    # Because when window is resized (restore down, maximize, minimize) then canvas will also resize according to it and icons placed on canvas, so by default will move with it.
    iconsArea = Canvas(root, width=600, height=850)
    iconsArea.create_rectangle(
        30, 50, 540, 690, outline="#2575fc", fill=None, width=10)
    iconsArea.pack()
    PlaceIcons(iconsArea, cursorType="hand2").placeIconsOnGUI()
    PlaceIcons(iconsArea).placeIconsOnGUI()
    userText = Entry(iconsArea, width=20, font="Calibri 30",
                     textvariable=StringVar(value="0"))
    userText.place(x=25, y=700)

    resultLabel = Label(iconsArea, width=5,
                        font="Calibri 30", bg=None, text=None)
    resultLabel.place(x=440, y=700)
    root.mainloop()
    # root.configure(bg="black")


if __name__ == '__main__':
    main()
