#imports
from car import *
from driver import *

#make a driver object
myDriver = Driver("John", 35, "Male")
myDriver.printProperties()

#make a car object
myCar = Car("Toyota", "Corolla", 2004, "Grey")
myCar.printProperties()

# do action
# lets drive some miles

myCar.driveMiles(500)
myCar.driveMiles(250)
print("After driving around, the new mileage is : " + myCar.getCurMileage())
