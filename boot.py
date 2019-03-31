from car import *
from driver import *

myDriver = Driver("John", 35, "Male")
myDriver.printProperties()

myCar = Car("Toyota", "Corolla", 2004, "Grey")
myCar.printProperties()

myCar.driveMiles(500)
myCar.driveMiles(250)
print("After driving around, the new mileage is : " + myCar.getCurMileage())
