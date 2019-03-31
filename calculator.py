
#print user 4 modes (sum, substract, multiply, divide)
print("Choose the function you want to use")
print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Division")

# input 
inputMode = str(input()) 

def addition(num1, num2):
    sum = num1 + num2 
    return str(sum)

def presentOptions():
    #print("You chose : " + inString)
    if (inputMode == "1"):
        #print("You chose 1")
        print("Enter the first number")
        argOne = int(input())
        print("Enter the second number")
        argTwo = int(input())
        print("The sum is : " + addition(argOne,argTwo))
    elif (inputMode == "2"):
        print("You chose 2")
    elif (inputMode == "3"):
        print("You chose 3")
    elif (inputMode == "4"):
        print("You chose 4")
    else : print ("You chose invalid option")


presentOptions()
