class Car:

    def __init__ (carObj, make, model, year, color):
        carObj.make = make
        carObj.model = model
        carObj.year = year
        carObj.color = color
        carObj.mileage = 0

    def driveMiles(self, miles):
        self.mileage += miles

    def printMake(car):
        print("Car make is : " + car.make)

    def printModel(car):
        print("Car model is : " + car.make)

    def printYear(car):
        print("Car year is : " + str( car.year))

    def printColor(car):
        print("Car color is : " + car.color)

    def printProperties(car):
        print("Car make is : " + car.make)
        print("Car model is : " + car.make)
        print("Car year is : " + str( car.year))
        print("Car color is : " + car.color)
        print("Car mileage is : " + str(car.mileage))

    def getCurMileage(car):
        return str(car.mileage)
#car1 = Car("Toyota", "Corolla", 2003, "Grey")
#car1.printProperties()
