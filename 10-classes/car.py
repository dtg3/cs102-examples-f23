# Declare a class named Car
#   Classes can go in a separate file (a Module) or they can be used
#   from a single file. This is a trivial example, so it is all in one
#   file for convenience.
class Car:
    
    # constructor (must be called __init__) initializes object when called
    #   the first paramter for all class methods refers to the instance of the
    #   object. The name self is used by convention to refer to the object, in
    #   this case, and instance of the car class. All other parameters follow
    #   the same rules that functions do.
    def __init__(self, givenColor, givenYear):

        # Attributes are properties or "state" that the object maintains.
        #   These are assigned to the object instance using self
        self.color = givenColor
        self.year = givenYear
        self.mileage = 0 # We can even set default values for attributes
    

    # This method operates on the Car instance and updates the car's mileage
    def drive(self, miles):
        self.mileage += miles
    

    # This method simply returns the mileage value it is holding so far
    def getMileage(self):
        return self.mileage


# Call the constructor to create an instance of the object and
#   initialize it's attributes
myCar = Car("red", 2014)

# call any methods that are defined on a Car object
myCar.drive(100)
print( "Mileage is: ", myCar.getMileage() )
myCar.drive(300)
print( "Mileage is: ", myCar.getMileage() )

# You can create an "unlimited" number of instances of the same object
ddCar = Car("blue", 2021)
print(ddCar.getMileage())