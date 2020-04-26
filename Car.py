class Car:
    # Properties
    color = ""
    brand = ""
    number_of_wheel = 4
    munber_of_seats = 4
    maxspedd = 0

    # Construtor
    def __init__(self, color, brand, number_of_wheel, munber_of_seats, maxspedd):
        self.color = color
        self.brand = brand
        self.number_of_wheel = number_of_wheel
        self.munber_of_seats = munber_of_seats
        self.maxspedd = maxspedd
    # Create method ser color

    def setcolor(self, x):
        self.color = x

    def setbrand(self, x):
        self.brand = x

    def setspeed(self, x):
        self.maxspedd = x

    def printdata(self):
        print("Color of this car is", self.color)
        print("Brand of this car is", self.brand)
        print("Max Speed of this car is", self.maxspedd)

    # Deconstrutor

    def __del__(self):
        print()
