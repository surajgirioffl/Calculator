def setIdentifiers(userTextRef, resultTextRef):
    global userText, resultText
    userText = userTextRef
    resultText = resultTextRef


allText = str()


def digitButtonClick(value: str | int) -> None:
    global userText, resultText, allText
    allText += str(value)
    userText.set(allText)
    # resultText.set(value)


def operatorButtonClick(value: str | int) -> None:
    digitButtonClick(f" {value} ")


def equalToButtonClick() -> None:
    global allText, resultText
    allText = allText.replace("x", "*")
    allText = allText.replace("÷", "/")
    allText = allText.replace("%", "*0.01")
    print(allText)
    try:
        if allText == "":
            global userText
            result = eval(userText.get())
        else:
            result = eval(allText)
    except ZeroDivisionError:
        resultText.set("∞")
    except:
        resultText.set("Error")
    else:
        resultText.set(result)
        ...
    # finally:


def clearButtonClick() -> None:
    global allText, userText, resultText
    allText = ""
    userText.set("")
    resultText.set("")


def backspaceButtonClick() -> None:
    global allText, userText
    allText = allText[:-1]
    userText.set(allText)


def decimalButtonClick() -> None:
    digitButtonClick(".")
