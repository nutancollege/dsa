import math

# Triangle area
base = float(input("Enter base of the triangle: "))
height = float(input("Enter height of the triangle: "))
area_triangle = 0.5 * base * height
print("Area of Triangle =", area_triangle)

# Rectangle area
length = float(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))
area_rectangle = length * breadth
print("Area of Rectangle =", area_rectangle)

# Circle area
radius = float(input("Enter radius of the circle: "))
area_circle = math.pi * radius * radius
print("Area of Circle =", area_circle)
