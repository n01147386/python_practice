class Driver:
    def __init__(driverObj, name, age, sex):
        driverObj.name = name
        driverObj.age = age
        driverObj.sex = sex
        driverObj.valid = "yes"
    
    def printName(driver):
        print("Driver name is : " + driver.name)

    def printAge(driver):
        print("Driver age is : " + str(driver.age))

    def printSex(driver):
        print("Driver sex is " + driver.sex)

    def printProperties(driver):
        print("Driver name is : " + driver.name)
        print("Driver age is : " + str(driver.age))
        print("Driver sex is " + driver.sex)
