import math

class Circle:
    
    def __init__(self, radius):
       
        self.radius = radius

    def area(self):
       
        area_val = math.pi * self.radius**2
        print(f"The area of the circle is: {area_val:.2f}")

    def perimeter(self):
        
        perimeter_val = 2 * math.pi * self.radius
        print(f"The perimeter of the circle is: {perimeter_val:.2f}")


my_circle = Circle(7)

# Call the methods to print the results directly
my_circle.area()
my_circle.perimeter()

