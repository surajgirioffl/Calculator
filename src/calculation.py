from tkinter import Entry, StringVar


def setIdentifiers(userTextRef: StringVar, resultTextRef: StringVar, entryObjectRef: Entry) -> None:
    global userText, resultText, entryObject
    userText = userTextRef
    resultText = resultTextRef
    entryObject = entryObjectRef


allText = str()


def digitButtonClick(value: str | int) -> None:
    global allText
    allText = userText.get()  # fetching the current text from the entry widget
    allText += str(value)  # appending the button's value to the 'allText'
    userText.set(allText)  # updating the widget with new text


def operatorButtonClick(value: str | int) -> None:
    digitButtonClick(f" {value} ")


def equalToButtonClick() -> None:
    global allText
    allText = userText.get()  # to fetch the current text from the entry widget
    if allText != "":
        allText = allText.replace("x", "*")
        allText = allText.replace("÷", "/")
        allText = allText.replace("%", "*0.01")
        print(allText)
        try:
            result = eval(allText)
        except ZeroDivisionError:
            resultText.set("∞")
        except:
            resultText.set("Error")
        else:
            resultText.set(result)
    else:
        resultText.set("Null")


def clearButtonClick() -> None:
    global allText
    allText = ""
    userText.set("")
    resultText.set("")


def backspaceButtonClick() -> None:
    global allText
    allText = userText.get()  # to fetch the current text from the entry widget
    # to delete last character from the string
    entryObject.delete(len(allText)-1, len(allText))
    # updating the allText with the current text from the entry widget to use it.
    # we can also use 'userText.get()' instead of it.
    allText = entryObject.get()


def decimalButtonClick() -> None:
    digitButtonClick(".")
