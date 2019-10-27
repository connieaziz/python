class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2

    def circumference(self):
        return 2*3.14*self.radius

class Square:
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side*self.side

    def perimetre(self):
        return 4*self.side
   
class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w

    def area(self):
        return self.l*self.w

    def perimeter(self):
        return 2*(self.l+self.w)

class Sphere:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 4*3.14*self.radius**2

    def volume(self):
        return 4/3*3.14*self.radius*self.radius*self.radius