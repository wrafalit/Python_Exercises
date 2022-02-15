# OOP Exercise 3: 
# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    pass

autobus = Bus("mercedes", 140, 55_000)
print(f"Vehicle Name: {autobus.name}, Speed: {autobus.max_speed} Mileage: {autobus.mileage:,}")
