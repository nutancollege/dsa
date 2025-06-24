import math

# Define a class named Circle
class Circle:
    # Constructor to initialize radius
    def __init__(self, radius):
        self.radius = radius

    # Method to calculate diameter
    def get_diameter(self):
        return 2 * self.radius

    # Method to calculate circumference
    def get_circumference(self):
        return 2 * math.pi * self.radius

    # Method to calculate area
    def get_area(self):
        return math.pi * self.radius * self.radius

# Input radius from user
r = float(input("Enter the radius of the circle: "))

# Create object of Circle class
c = Circle(r)

# Call and print all values
print("Diameter:", c.get_diameter())
print("Circumference:", c.get_circumference())
print("Area:", c.get_area())
