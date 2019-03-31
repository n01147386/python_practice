argOne = 0
argTwo = 0
inputMode = ""

def promptForNumbers():
    print("Enter the first number")
    global argOne
    argOne = int(input())
    print("Enter the second number")
    global argTwo 
    argTwo = int(input())

def addition():
    sum = argOne + argTwo
    return str(sum)

def subtraction():
    val = argOne - argTwo
    return str(val)

def multiplication():
    val = argOne * argTwo
    return str(val)

def division():
    val = argOne / argTwo
    return str(val)


def processRequest():
#print("You chose : " + inString)
    if (inputMode == "0"):
        quit()
    elif (inputMode == "1"):
        promptForNumbers()
        print("The answer is : " + addition())
        mainMenu()
    elif (inputMode == "2"):
        promptForNumbers()
        print("The answer is : " + subtraction())
        mainMenu()
    elif (inputMode == "3"):
        promptForNumbers()
        print("The answer is : " + multiplication())
        mainMenu()
    elif (inputMode == "4"):
        promptForNumbers()
        print("The answer is : " + division())
        mainMenu()
    else : print ("You chose invalid option")

def mainMenu():
    print("Choose the function you want to use")
    print("0 to quit")
    print("1 for Addition")
    print("2 for Subtraction")
    print("3 for Multiplication")
    print("4 for Division")
    global inputMode
    inputMode = str(input()) 
    processRequest()

mainMenu()


