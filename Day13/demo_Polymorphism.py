import math
print(1+2)
print("Hi"+"World")

print(len("Hiii"))
print(len([1,2,3,4,"Hi"]))


class Shape:
    def area(self):
        return "Hi"

class Square(Shape):
    def __init__(self,s):
        self.s = s
    def area(self):
        print("Area of square: {}".format(str(self.s*self.s)))

class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        print("Area of Circle: {}".format(str(math.pi*self.r*self.r)))



c = Circle(5)
s = Square(5)
c.area()
s.area()
