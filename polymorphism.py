#Polymorphism example
import math
class shape():
    def area(self):
        pass
class square(shape):
    def area(self,side):
        print("Area of Square is ",side*side)
class circle(shape):
    def area(self,radius):
        print("Area of Circle is ",math.pi*radius*radius)
class rectangle(shape):
    def area(self,length,breadth):
        print("Area of Rectangle is ",length*breadth)
s=square()
c=circle()
r=rectangle()
s.area(4)
c.area(3)
r.area(3,4)

